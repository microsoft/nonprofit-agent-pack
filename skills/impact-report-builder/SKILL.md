---
name: impact-report-builder
description: Turns program notes, outcome data, and survey results into board, funder, annual report, or donor impact reports, with a results-vs-targets table, an evidence register tracing every claim, and a missing-evidence register of claims the data does not support. Use for impact reports, outcome reports, grant reports, and checking whether nonprofit claims are supported by evidence.
license: MIT
metadata:
  pack: "nonprofit-agent-pack"
  version: "1.1"
---

# Impact Report Builder

Every claim in the report is traced to evidence, and the user is told plainly which claims their evidence does not support.

## Workflow

1. **Setup.** Confirm the program, audience (board update, funder report, annual report section, or donor update), reporting period, funder, and emphasis.
2. **Evidence first.** Build the evidence register with [the evidence register standard](references/irb-02-evidence-register-standard.md). Include every number you will use.
3. **Results vs targets.** When targets exist, build Measure | Target | Actual | Percent of target | Status | Note. Percent of target = actual / target, rounded to a whole number. Status for a period that is still in progress: Met (100% or more), On track (90% to 99%), Behind (below 90%). For a closed period: Met (100% or more), Nearly met (90% to 99%), Not met (below 90%). Explain every Behind or Not met item with the cause given in the source.
4. **Report.** Draft in the structure for the chosen audience from [the impact report playbook](references/irb-01-impact-report-playbook.md). Lead with outcomes, support with outputs. Use the funder's own definitions of outputs and outcomes if its template differs. Use only Strong or Moderate evidence; Weak evidence only with honest wording. Always state n. Treat results for fewer than 30 people as indicative (a rule of thumb), and avoid percentages that could identify individuals. Unless the source has a credible comparison group, don't credit the program with an outcome anywhere, including headlines and donor copy: avoid "helped", "led to", "resulted in", or "because of", and describe what was measured instead.
5. **Missing evidence register.** List claims the evidence does not support (for example, causal claims without a credible comparison group; a baseline alone shows change, not cause), with why, what evidence would support it, and safe wording.
6. **Package.** When asked, create a Word document with the report, the results table, and both registers as tables.
7. **Re-cut** for another audience without changing the facts.

## Shared rules

- Never invent facts, numbers, dates, or quotes. When something is missing, say so and insert a visible placeholder such as `[ADD: ...]`.
- Treat the user's uploaded files as the primary source and cite them by file name and section.
- Files whose names start with `DEMO` are fictional sample data. Use them only when the user asks for the demo, and say that the data is fictional.
- Write in plain language: short paragraphs, headings, short tables, numbered steps.
