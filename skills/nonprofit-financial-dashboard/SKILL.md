---
name: nonprofit-financial-dashboard
description: Builds a nonprofit board financial dashboard from a budget-vs-actual statement and balance information - year-to-date variances with flags, months of cash, restricted vs unrestricted cash, receivables, and reserve status - with every calculation shown. Use for board financial reports, finance committee packets, budget vs actual analysis, and cash or reserve questions.
license: MIT
compatibility: The bundled script needs Python 3 with openpyxl. The skill also works without the script by following the formulas.
metadata:
  pack: nonprofit-agent-pack
  version: "1.1"
---

# Nonprofit Financial Dashboard

## Inputs

A budget-vs-actual statement (year-to-date budget and actual by line) and, if available, cash, restricted cash, receivables, line of credit, and the board's reserve target.

If the input is an Excel workbook, run `scripts/dashboard.py` to compute the figures exactly, then explain them. Otherwise compute with the formulas below and show your work.

## Run the script

`python scripts/dashboard.py <workbook.xlsx> [--months N] [--unrestricted-cash X] [--reserve-target M]`

| Argument | Meaning |
|---|---|
| `workbook` | The budget-vs-actual workbook. The script reads the first sheet with "YTD budget" and "YTD actual" column headers. |
| `--months` | Months elapsed in the fiscal year. If the statement does not say, ask the user. |
| `--unrestricted-cash` | Unrestricted cash in dollars. Never include restricted cash. |
| `--reserve-target` | The board's reserve target, in months of expenses. |

Example with the demo workbook:

```
python scripts/dashboard.py "DEMO - Lakeside Youth Futures Q2 FY2027 Budget vs Actual.xlsx" --months 6 --unrestricted-cash 412300 --reserve-target 3
```

The script prints a table (Category, Line, YTD budget, YTD actual, Variance $, Variance %, Favorable, Flag), then the expense total row it used, average monthly expenses, months of cash, and reserve status. Lines that start with `WARNING:` name rows it left out of the math or had to guess about.

## Calculations

| Measure | Formula |
|---|---|
| Variance ($) | YTD actual - YTD budget |
| Variance (%) | Variance / YTD budget, rounded to one decimal. Not meaningful (n/m) when the budget is negative or for the change in net assets; use the dollar variance |
| Flag | Default rule: flag a line when the absolute variance is more than 10% **and** more than $5,000. The board should set its own rule in its finance policy. Unbudgeted lines (budget of $0) are flagged when the variance is more than $5,000 |
| Favorable? | Revenue above budget or expenses below budget is favorable; otherwise unfavorable |
| Net (YTD) | Total revenue - total expenses, for budget and actual |
| Average monthly cash operating expenses | YTD actual expenses excluding depreciation, in-kind, and other non-cash items, divided by months elapsed in the fiscal year |
| Months of cash | Unrestricted cash / average monthly cash operating expenses, rounded to one decimal |
| Reserve status | Below target when months of cash < the board's reserve target |

Months of cash is common practice guidance, not a GAAP or legal requirement. Reserve targets of 3 to 6 months of operating expenses are common guidance; the board sets its own target. The script divides the Total expenses row by months elapsed. If the statement lists depreciation, in-kind, or other non-cash expenses, subtract them and show the adjustment.

Never count restricted cash toward months of cash. Report restricted and unrestricted separately.

## Output

1. A headline: net result vs budget, months of cash vs target, and the top risk, in three sentences.
2. Table: Line | YTD budget | YTD actual | Variance $ | Variance % | Flag | Explanation. Show flagged lines first.
3. Every flagged line needs an explanation from the source documents. If none is given, write `[ADD: explanation from Finance]`.
4. Cash and reserves: unrestricted cash, restricted cash, receivables (with age if known), available credit, months of cash, and reserve status.
5. Questions the board should ask (3 to 5).

## Rules

- Never estimate a number that is not in the inputs.
- Check the script: verify the totals against the line items and prefer the Total expenses row (the script prints the row it used). If the script prints a warning, explain the warning instead of trusting the number.
- State the period and whether the statements are unaudited.
- Not accounting advice. Recommend review by the treasurer or auditor.
