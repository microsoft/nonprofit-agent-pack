# Obligations Register Standard

> General guidance for US nonprofits as of October 2026, not legal, tax, or accounting advice. Rules elsewhere differ. Review with qualified advisors before relying on it.

Every agreement review produces an obligations register and a reporting calendar.

## Register columns

| Column | Rule |
|---|---|
| ID | OB-01, OB-02, and so on |
| Obligation | One action per row, starting with a verb |
| Clause | Section number and a short quote |
| Type | Report, Payment, Approval, Notice, Compliance, Deliverable |
| Due date | Exact date when stated; when relative (for example, '30 days after quarter end'), calculate it from the agreement dates and show the calculation |
| Frequency | Once, Monthly, Quarterly, Annually |
| Owner role | Suggested role: Executive Director, Finance, Program, Development, Grants Manager |
| Risk | High, Medium, Low |
| Notes | Dependencies and evidence needed |

## Files to generate with code interpreter

- An Excel workbook with sheets: Obligations, Calendar, Risk Flags, Questions for Funder.
- An .ics calendar file with one all-day event per dated obligation. Use the summary format '[Agreement short name] OB-xx: obligation', and put the clause and owner role in the description. Add a reminder 7 days before each event.
- A download link for every file created.

## Calendar file rules (RFC 5545)

- Start with BEGIN:VCALENDAR, VERSION:2.0, and a PRODID line. End with END:VCALENDAR.
- Each VEVENT must include UID (unique per event), DTSTAMP (creation time in UTC), DTSTART;VALUE=DATE (the due date), DTEND;VALUE=DATE (the day after the due date), SUMMARY, and DESCRIPTION.
- Each VEVENT must include a VALARM with ACTION:DISPLAY, a DESCRIPTION, and TRIGGER:-P7D.
- Use CRLF line endings. Fold any line longer than 75 octets: break it and start the next line with a single space.
- In text values, put a backslash before commas, semicolons, and backslashes, and write line breaks as \n.
