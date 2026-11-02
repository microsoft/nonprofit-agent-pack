# Agent Governance Playbook for Small IT Teams

> General guidance for US nonprofits as of October 2026, not legal, tax, or accounting advice. Rules elsewhere differ. Review with qualified advisors before relying on it.

A right-sized governance plan for nonprofits starting with Copilot Studio agents. Recommend controls in three tiers: Start (first 30 days), Grow (by 90 days), and Scale (when agents use sensitive data or serve the public).

| Area | Start (30 days) | Grow (90 days) | Scale |
|---|---|---|---|
| Who can build | Named makers only; everyone else uses shared agents. Before building, decide go or no-go for each use case (purpose, data, people affected) and add it to an agent inventory with an owner | Maker training and a request form | Maker community with reusable templates |
| Environments | Keep personal experiments separate from shared agents; create one shared environment for team agents | Separate test and production environments | Managed Environments (a premium capability) with pipelines from test to production |
| Data loss prevention | Block connectors you do not use (some core Microsoft connectors can't be blocked); keep business and consumer connectors apart | Review new connector requests monthly | Environment-specific policies for sensitive data |
| Credits and cost | Set a monthly capacity budget and review usage weekly. Agents on the GitHub Copilot harness use credits on every run, including tests | Assign capacity to the environments that need it; set a monthly credit limit for each agent with notifications (act at about 80%) | Chargeback or showback by department |
| Sharing | Share agents with named security groups, not the whole organization | Owner and backup owner for every agent | Publish approved agents to Teams and Microsoft Copilot through an approval step |
| Quality | Test 10 real questions before sharing | A saved test set re-run before each update | Automated evaluations and analytics review; evaluations help but don't guarantee an agent is safe |
| Monitoring | Review conversation analytics monthly | Track satisfaction and unanswered questions | Central inventory, telemetry, and incident process |
| Retirement | Delete unused experiments quarterly | Owner must re-certify agents every 6 months | Lifecycle policy with archive and removal |

## Roles

- Executive sponsor: approves policy and risk posture. AI lead: runs the program. IT admin: environments, data policies, and capacity. Agent owners: content, testing, and retirement.

## Ninety-day rollout

1. Weeks 1 to 2: approve the acceptable use policy, name the AI lead and makers.
2. Weeks 3 to 4: set up the shared environment, data policies, and credit budget.
3. Weeks 5 to 8: build two pilot agents with clear owners; test and share with one team.
4. Weeks 9 to 12: review analytics, gather feedback, decide which agents scale, and update the policy.
