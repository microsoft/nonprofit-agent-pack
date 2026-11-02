# Copyright (c) Microsoft Corporation.
# Licensed under the MIT License.
"""Compute a nonprofit financial dashboard from a budget-vs-actual workbook.

Usage: python dashboard.py <workbook.xlsx> [--months N] [--unrestricted-cash X] [--reserve-target M]

Reads the first sheet with a header row containing "YTD budget" and "YTD actual" (case-insensitive).
Rows named "Total ..." and the bottom line (such as "Change in net assets") are subtotals and are never
flagged. Other lines are flagged when the variance is more than 10% of budget and more than $5,000;
unbudgeted lines are flagged when the variance is more than $5,000. Rows with no budget and no actual
are read as headings. Months of cash uses the "Total expenses" row, else the last expense subtotal.
WARNING lines list rows that were left out or guessed. Check them before using the numbers.
"""
import argparse
import re
import sys

from openpyxl import load_workbook

FLAG_PCT, FLAG_DOLLARS = 10, 5000  # Default flag rule. The board should set its own in its finance policy.
NAME_HEADERS = ("account", "description", "item", "line")
LABELS = {"rev": "Revenue", "exp": "Expenses"}
AMOUNT = re.compile(r"(-?)\$?(-?)(\d{1,3}(?:,\d{3})+(?:\.\d+)?|\d+(?:\.\d+)?|\.\d+)")
# Bottom-line rows such as "Change in net assets", "Net income (loss)", or "Excess of revenue over expenses".
NET_ROW = re.compile(r"(net )?(change|increase|decrease)\b.*net assets|net (income|loss|surplus|deficit|operating)\b"
                     r"|(surplus|deficit|excess)\b.*\b(deficit|deficiency|surplus|over)\b|net$")


def clean(v):
    """Return a cell value as text with spacing collapsed ("" when blank)."""
    return " ".join(str(v).split()) if v is not None else ""


def num(v):
    """Return a cell value as a number, reading text like "$100,000", "(5,000)", or "1,234.50". None if not a number."""
    if isinstance(v, (int, float)) and not isinstance(v, bool):
        return float(v)
    s = clean(v).replace(" ", "")
    paren = s.startswith("(") and s.endswith(")")
    m = AMOUNT.fullmatch(s[1:-1] if paren else s)
    if not m:
        return None
    x = float(m.group(3).replace(",", ""))
    return -x if paren or m.group(1) or m.group(2) else x


def side(text):
    """Return "exp" or "rev" when the text names expenses or revenue, else None."""
    t = text.lower()
    if "expen" in t or t.startswith("exp"):
        return "exp"
    return "rev" if any(w in t for w in ("revenue", "income", "support")) else None


def money(x):
    return ("-" if x < 0 else "") + f"${abs(x):,.0f}"


def find_header(wb):
    """Return the first sheet with "YTD budget" and "YTD actual" headers, the header row number, and the headers."""
    for ws in wb.worksheets:
        for r, row in enumerate(ws.iter_rows(values_only=True), start=1):
            cols = [clean(v).lower() for v in row]
            if "ytd budget" in cols and "ytd actual" in cols:
                return ws, r, cols
    sys.exit("Could not find a header row with 'YTD budget' and 'YTD actual'.")


def name_column(cols, data, ic):
    """Return the line-name column: a header naming lines or accounts, else the first text column."""
    others = [i for i, h in enumerate(cols) if i != ic and "budget" not in h and "actual" not in h]
    named = [i for i in others if any(k in cols[i] for k in NAME_HEADERS)]

    def is_text(i):
        vals = [clean(r[i]) for r in data if clean(r[i])]
        return bool(vals) and 2 * sum(num(v) is None for v in vals) > len(vals)

    il = next((i for i in named + others if is_text(i)), named[0] if named else None)
    if il is None:
        sys.exit("Could not find the line-name column. Add a header such as 'Line item' or 'Account' above the names.")
    return il


def read_rows(data, first_row, ib, ia, ic, il, stale):
    """Return one record per row with amounts, and {reason: rows} for rows left out of the math."""
    rows, skipped, cat = [], {}, ""
    for r, row in enumerate(data, start=first_row):
        cat = (clean(row[ic]) if ic is not None else "") or cat  # Carry the category down past blank or merged cells.
        name = clean(row[il]).replace("|", "/")
        key = name.lower().rstrip(":")
        net = bool(NET_ROW.match(key)) or cat.lower() == "net"
        sub = net or key.startswith(("total", "subtotal", "sub-total", "sub total"))
        texts, b, act = (clean(row[ib]), clean(row[ia])), num(row[ib]), num(row[ia])
        if {(r, ib + 1), (r, ia + 1)} & stale:
            why = "a formula has no saved value"
        elif not any(texts) and not sub:
            if ic is None and side(name):
                cat = name  # A heading such as "Revenue" or "Operating expenses".
            continue
        elif not name:
            why = "the row has no line name"
        elif not all(texts):
            why = "the budget or actual is blank"
        elif b is None or act is None:
            why = "the budget or actual is not a number"
        else:
            why = None
        if why:
            bad = ", ".join(repr(t) for t, n in zip(texts, (b, act)) if t and n is None)
            skipped.setdefault(why, []).append(f"{name or '(no name)'} (row {r}{': ' + bad if bad else ''})")
        rows.append(dict(row=r, name=name, key=key, cat=cat, net=net, sub=sub, b=b, a=act, ok=not why))
    return rows, skipped


def classify(rows):
    """Mark each row as revenue, expense, or net. Return the rows whose type is a guess."""
    rev_row = next((x["row"] for x in rows if x["key"].startswith("total") and side(x["key"]) == "rev"), None)
    unsure = []
    for x in rows:
        x["kind"], x["how"] = ("net" if x["net"] else side(x["cat"])), ""
        if not x["kind"]:  # No usable category: infer from the position below "Total revenue" and from the name.
            by_pos = None if rev_row is None else "exp" if x["row"] > rev_row else "rev"
            by_name = side(x["key"])
            x["kind"] = by_pos or by_name or "rev"
            x["how"] = "inferred" if len({by_pos, by_name} - {None}) == 1 else "unsure"
            if x["how"] == "unsure" and x["ok"]:
                unsure.append(f"{x['name']} (row {x['row']}, treated as {LABELS[x['kind']].lower()})")
    return unsure


def months_of_cash(a, rows):
    """Print average monthly expenses, months of cash, and reserve status, or exit saying why they can't be computed."""
    exact = [x for x in rows if x["key"] in ("total expenses", "total expense")]
    total = (exact or [x for x in rows if x["sub"] and x["kind"] == "exp"] or [None])[-1]
    if not a.months or a.months <= 0:
        sys.exit("Months of cash needs --months, the number of months elapsed in the fiscal year.")
    if total is None:
        sys.exit("No expense total row (such as 'Total expenses') was found, so months of cash was not computed.")
    where = f"{total['name']} (row {total['row']})"
    if total["a"] is None:
        sys.exit(f"The expense total row {where} has no usable YTD actual (see the warnings above), "
                 "so months of cash was not computed.")
    if total["a"] <= 0:
        sys.exit(f"The expense total row {where} shows {money(total['a'])}, so months of cash cannot be computed.")
    print(f"\nExpense total used: {where}" + ("" if exact else ", the last expense subtotal (no 'Total expenses' row)"))
    avg = total["a"] / a.months
    print(f"Average monthly expenses = ${total['a']:,.0f} / {a.months:g} months = ${avg:,.0f}")
    if a.unrestricted_cash is None:
        if a.reserve_target is not None:
            sys.exit("Reserve status needs --unrestricted-cash.")
        return
    m = a.unrestricted_cash / avg
    print(f"Months of cash = ${a.unrestricted_cash:,.0f} / ${avg:,.0f} = {m:.1f} months")
    if a.reserve_target is not None:
        status = "BELOW" if m < a.reserve_target else "At or above"
        print(f"Reserve status: {status} the {a.reserve_target:g}-month target")


def main():
    ap = argparse.ArgumentParser(description="Board financial dashboard from a budget-vs-actual workbook.")
    ap.add_argument("workbook")
    ap.add_argument("--months", type=float, help="months elapsed in the fiscal year (default: ask the user)")
    ap.add_argument("--unrestricted-cash", type=float)
    ap.add_argument("--reserve-target", type=float, help="reserve target in months")
    a = ap.parse_args()

    wb = load_workbook(a.workbook, data_only=True)
    ws, hdr, cols = find_header(wb)
    data = list(ws.iter_rows(min_row=hdr + 1, values_only=True))
    # Formulas in a file that was never opened and saved in Excel have no saved values and read as blank.
    stale = {(c.row, c.column) for row in load_workbook(a.workbook)[ws.title].iter_rows(min_row=hdr + 1)
             for c in row if c.data_type == "f" and ws.cell(c.row, c.column).value is None}
    ib, ia = cols.index("ytd budget"), cols.index("ytd actual")
    ic = next((i for i, h in enumerate(cols) if "category" in h), None)
    rows, skipped = read_rows(data, hdr + 1, ib, ia, ic, name_column(cols, data, ic), stale)
    unsure = classify(rows)

    if ws is not wb.worksheets[0]:
        print(f"Using sheet '{ws.title}'.")
    if stale:
        print(f"WARNING: {len(stale)} formula cell(s) have no saved value, so they read as blank. "
              "Open the workbook in Excel, save it, and run the script again.")
    for why, items in skipped.items():
        print(f"WARNING: Left out of the math because {why}: {'; '.join(items)}.")
    if unsure:
        print(f"WARNING: Could not tell revenue from expenses for: {'; '.join(unsure)}. "
              "Add a Category column or check the Favorable column.")

    print("| Category | Line | YTD budget | YTD actual | Variance $ | Variance % | Favorable | Flag |")
    print("|---|---|---|---|---|---|---|---|")
    for x in (x for x in rows if x["ok"]):
        b, act = x["b"], x["a"]
        v = round(act - b, 2)
        pct = "n/m" if x["net"] or b < 0 else "n/a (unbudgeted)" if b == 0 else f"{v / b * 100:.1f}%"
        fav = v <= 0 if x["kind"] == "exp" else v >= 0
        flag = not x["sub"] and abs(v) > FLAG_DOLLARS and abs(v) * 100 > FLAG_PCT * abs(b)
        cat = "Net" if x["net"] else x["cat"] or f"{LABELS[x['kind']]} ({x['how']})"
        print(f"| {cat} | {x['name']} | {money(b)} | {money(act)} | {money(v)} | {pct} | "
              f"{'Yes' if fav else 'No'} | {'FLAG' if flag else ''} |")

    if a.months is not None or a.unrestricted_cash is not None or a.reserve_target is not None:
        months_of_cash(a, rows)


if __name__ == "__main__":
    main()
