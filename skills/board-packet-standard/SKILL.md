---
name: board-packet-standard
description: Assembles a nonprofit board meeting packet in a standard order with a consent agenda, draft motions, an executive director summary, committee highlights, and a decisions-needed list. Use when preparing board or committee meeting materials, consent agendas, motions, or board decks from source documents.
license: MIT
metadata:
  pack: "nonprofit-agent-pack"
  version: "1.1"
---

# Board Packet Standard

## Packet order

1. Cover page: organization, meeting date, time, location or link, and "DRAFT for board review".
2. Agenda with time allocations. Consent agenda items first.
3. Consent agenda: prior minutes, committee reports that need no discussion, routine renewals.
4. Executive Director summary (one page): highlights, program results vs targets, risks, and what's next.
5. Financial dashboard (apply the `nonprofit-financial-dashboard` skill).
6. Committee highlights: one short section per committee, with its recommendations to the board.
7. Decisions needed: each decision with background, options, recommendation, and the draft motion.
8. Action item tracker: open items from the prior minutes with owner, due date, and status (Done, On track, Overdue, Carried forward).
9. Appendix: list of source documents used.

## Consent agenda rules

Apply these rules unless your bylaws say otherwise.

- Include only items that need no discussion and have a committee or staff recommendation.
- Any board member can pull an item for discussion. Say so on the agenda.
- Tool policy (not a Robert's Rules requirement): never put the financial statements on the consent agenda if a variance was flagged or reserves are below target.

## Motion templates

Follow your bylaws and parliamentary authority.

- Minutes (chair's statement): "If there are no corrections, the minutes of the [date] meeting are approved as distributed." (With corrections: "...are approved as corrected.")
- "Motion to receive the [period] financial statements as presented by the Finance Committee."
- "Motion to adopt the [policy name], effective [date]."
- "Motion to authorize [officer] to [action] up to [amount], subject to [condition], through [date]."
- "Motion to authorize submission of the [funder] [program] proposal for [amount], including [match or commitment]."

Fill every bracket from the source documents. If a value is missing, keep `[ADD: ...]`.

## Action item tracker

Carry every action item from the prior minutes. Mark status from evidence in the current documents only. If there is no evidence, mark "No update" rather than assuming.

## Rules

- Never invent facts, numbers, names, or quotes. Use `[ADD: ...]` for gaps.
- Every number must match across the Word packet, the slides, and the Excel workbook.
- Files starting with `DEMO` are fictional. Use them only for the demo and say so.
- This is not legal or financial advice. Recommend review by the treasurer, auditor, or counsel where relevant.
