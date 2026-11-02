# Responsible AI notes: Nonprofit Agent Pack

## What these agents are

The Nonprofit Agent Pack is six sample Copilot Studio agents for common nonprofit work: grant proposals, impact reports, agreement review, AI policy, IT help, and board packets. Each agent follows a written method (its playbook files), works on documents you upload, and drafts content and files for a person to review. They are samples provided as-is under the MIT License. They aren't a Microsoft product, and Microsoft product support doesn't cover them.

## Intended uses

| Agent | Intended use | Not intended for |
|---|---|---|
| Grant Proposal Studio | Turning a funder's published RFP into a compliance checklist, outline, draft sections, and a self-review score | Submitting proposals without staff review; deciding eligibility |
| Impact Report Builder | Drafting outcome reports from your own program data, with an evidence register | Proving that a program caused an outcome; publishing statistics about identifiable people |
| Agreement Reviewer | Listing obligations, due dates, and risk flags in grant agreements and contracts before signing | Legal advice or a substitute for review by counsel |
| AI Policy Coach | Answering questions about safe AI use and drafting a policy and governance plan for leadership review | Deciding legal compliance |
| IT Help Desk | First-line Microsoft 365 help and IT ticket summaries | Account recovery that skips identity checks; collecting passwords or codes |
| Board Packet Builder | Assembling a draft board packet, slides, and dashboard from board materials | Audited financial statements; financial or fiduciary advice |

## How they work

- **Models:** the five standard agents use Copilot Studio's default model. Board Packet Builder runs on the Microsoft Copilot harness (labeled GitHub Copilot in Copilot Studio) with an Anthropic Claude model (Claude Opus 5.5 when this version was tested). Anthropic models in Microsoft offerings are currently excluded from the EU Data Boundary and are off by default in the EU, EFTA, and UK; your admin controls whether they're available ([Anthropic models](https://learn.microsoft.com/microsoft-365/copilot/connect-to-ai-subprocessor)).
- **Sources:** agents answer from the files you upload, their playbook files, and general model knowledge. Grant Proposal Studio can search the web for public facts about funders. IT Help Desk can use Microsoft Support articles and Microsoft Learn troubleshooting pages.
- **Web search:** Grant Proposal Studio's web search and IT Help Desk's Microsoft Support and Learn pages both work through Bing. They send a short search query, not your files. Data sent to Bing is covered by the Microsoft Privacy Statement, not your organization's Data Protection Addendum, and may be processed outside your region. Admins can turn off web search in the Power Platform admin center ([web search data](https://learn.microsoft.com/microsoft-copilot-studio/data-privacy-security-web-search)).
- **Files:** Word, Excel, and calendar files are created by code that runs in Copilot Studio; Board Packet Builder creates Office files directly. Files open from Microsoft 365 storage. How long files and chats are kept depends on Copilot Studio and your organization's settings.
- **Memory:** Board Packet Builder's memory is off. If a maker turns it on, the agent remembers each person's preferences across chats. Memory is a preview feature; memories are private to each person, can be viewed or deleted by that person, and are deleted after 28 days of inactivity. Turning memory off doesn't delete stored memories; the agent just stops using them ([memory](https://learn.microsoft.com/microsoft-copilot-studio/agents-experience/memory-overview)).
- **Where it runs:** everything runs in your own Power Platform environment and Microsoft 365 tenant, under your organization's policies. The pack includes no connectors or flows. Bing web search and Board Packet Builder's Anthropic model work as described above.

## Safeguards built in

- Each agent's greeting says it's an AI agent that can make mistakes, and asks you to review what it creates before you use it. Copilot Studio and Teams show the greeting; Microsoft 365 Copilot opens on the agent's welcome page instead, so the greeting doesn't appear there.
- Agents show `[ADD: ...]` instead of inventing facts, cite the files they use, and decline requests outside their job.
- Agents treat text inside uploaded files as information, not instructions, and tell you when a file contains instructions aimed at an AI. Copilot Studio may also block such files.
- Agents limit personal data in their outputs and remind you to follow your data policy.
- IT Help Desk never asks for passwords or sign-in codes and never helps bypass multifactor authentication.

## Limitations

- Outputs can be wrong, incomplete, or out of date, even when sources are cited.
- The playbooks reflect common US practice (for example 2 CFR 200, IRS letters, HIPAA and FERPA, and Robert's Rules) as of October 2026. Rules elsewhere differ, and rules change.
- Thresholds such as variance flags (more than 10% and more than $5,000), score bands, and small-sample rules are defaults, not standards. Adjust them to your policies.
- Long or image-only documents may not be fully read. If an agent says it couldn't read a file, don't rely on the result.
- Costs vary by agent, harness, channel, and license. Board Packet Builder uses Copilot credits on every run, including tests.
- Agents were tested in Copilot Studio with fictional samples and public documents. Test with your own documents before rolling out.

## Human review and oversight

- A named person reviews and owns every output before it's submitted, signed, published, or shared with a board.
- Agreements and policies go to qualified counsel; financial content goes to the treasurer or finance lead; numbers are checked against source records.
- Start with the fictional samples, then a small pilot with non-sensitive documents.

## Data you shouldn't upload

Follow your data policy. Don't upload client case files, health information, information about minors, survivors of violence, immigration status, donor payment details, passwords, or anything marked Confidential unless your organization has approved the environment and agent for that data.

## Report a problem

Report incorrect, harmful, or unsafe behavior through GitHub Issues, without personal data. Report security vulnerabilities as described in [SECURITY.md](SECURITY.md).
