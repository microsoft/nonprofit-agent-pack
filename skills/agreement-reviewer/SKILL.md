---
name: agreement-reviewer
description: Reviews grant agreements, contracts, subawards, and MOUs clause by clause: plain-language board summary, obligations register with calculated due dates, risk flags including federal flow-down, questions for the funder, plus an Excel workbook and an .ics calendar file. Use for grant agreement review, contract compliance, reporting calendars, and pre-signature negotiation.
license: MIT
metadata:
  pack: "nonprofit-agent-pack"
  version: "1.1"
---

# Agreement Reviewer

Apply the checklist clause by clause, calculate every due date, and produce working files.

## Workflow

1. **Identify** the parties, agreement number, amount, term, and payment schedule. If the document is not an agreement, say so.
2. **Board summary.** Five bullets maximum, including the top risk.
3. **Obligations register** per [the obligations register standard](references/arv-02-obligations-register-standard.md). One obligation per row. Turn relative dates into real dates from the agreement dates and show the calculation. List recurring items (each quarterly report) as separate rows.
4. **Risk flags.** Go through every category in [the agreement review checklist](references/arv-01-agreement-review-checklist.md): Category | What it says | Risk | Why | Suggested change. Treat the risk signals as review heuristics, not legal limits. Flag federal flow-down language, such as 2 CFR 200, an Assistance Listing number (formerly CFDA), or subaward terms, and explain it.
5. **Questions for the funder.** 5 to 8, ranked by risk.
6. **Files.** Create an Excel workbook (sheets: Obligations, Calendar, Risk Flags, Questions for Funder) and an .ics file with one all-day event per dated obligation and a 7-day reminder. Follow the calendar file rules in the standard: each VEVENT has UID, DTSTAMP, DTSTART;VALUE=DATE, DTEND, SUMMARY, DESCRIPTION, and a VALARM with TRIGGER:-P7D, and lines longer than 75 octets are folded (RFC 5545). Build them from the register you already produced in this conversation; never ask the user to re-upload it. Give a download link for every file created.
7. Close with: "This review is not legal advice. Have counsel review High-risk items before signing."

## Shared rules

- Never invent facts, numbers, dates, or quotes. When something is missing, say so and insert a visible placeholder such as `[ADD: ...]`.
- Treat the user's uploaded files as the primary source and cite them by file name and section.
- Files whose names start with `DEMO` are fictional sample data. Use them only when the user asks for the demo, and say that the data is fictional.
- Write in plain language: short paragraphs, headings, short tables, numbered steps.
