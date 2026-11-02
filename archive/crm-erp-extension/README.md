# Archive — CRM / ERP extension (not part of the workshop)

These materials extended the FP&A Variance Autopilot with a mock CRM/ERP API ("SalesLens") so the orchestrator could look up root causes in external systems. They are kept for reference only and are **not tested** against the current labs.

| Folder / file | Was | Why archived |
|---|---|---|
| `lab-02-3-saleslens-connection/` | Lab 2.3 — Orchestrate connection to the SalesLens API | The hosted SalesLens API is no longer available |
| `lab-02-4-crm-erp-agents/` | Lab 2.4 — CRM and ERP context agents | Depends on SalesLens. The core path reads root causes from the `FPA_Variance` cube instead |
| `lab-02-6-agentops/` | Lab 2.6 — AgentOps tracing and a with/without CRM-ERP comparison | The comparison needs the Lab 2.4 agents |
| `saleslens-api/` | Node.js / Express mock CRM-ERP API (+ Code Engine deploy guide) | Only used by Labs 2.3, 2.4 and 2.6 |
| `fpa-variance-agent-crm-erp.yaml` | Earlier single-agent version that called CRM/ERP | Replaced by `lab-02-2-pa-agent/pa-data-agent.yaml` |

To revive the extension: deploy `saleslens-api/` (see its README), update the URLs in the Lab 2.3 and 2.4 instructions, and re-test on the current Orchestrate UI. The menu paths in these files are out of date.

Original authors: Shan (SalesLens API, CRM/ERP agents, AgentOps lab) and Lorenzo Laderchi.
