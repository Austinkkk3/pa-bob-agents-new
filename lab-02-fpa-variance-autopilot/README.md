# Lab 2 — FP&A Variance Autopilot

**Duration:** ~20 minutes (fast path) or ~60 minutes (step-by-step path)
**Tools:** watsonx Orchestrate · IBM Planning Analytics · IBM Bob (fast path)
**Prerequisite:** [Lab 0](../lab-00-setup/README.md) ✅ · [Lab 1](../lab-01-bob-planning-analytics-mcp/README.md) ✅

---

## In this lab

> 📍 **Where:** Lab 2.0 in Bob; the agents in watsonx Orchestrate, in your browser  
> 🎯 **What you do:** Build two AI agents that read the `FPA_Variance` cube, flag the material variances, read the root cause stored with each one, and write a CFO-ready report.  
> ⚡ **Why it matters:** Month-end variance commentary usually takes an FP&A team 3–4 days of pulling numbers, chasing explanations and writing it up. The autopilot answers one chat question in 1–2 minutes, and anyone with access to Orchestrate can ask it.  
> ✅ **You leave with:** Your own working variance autopilot in watsonx Orchestrate.

## What You Will Build

A multi-agent system in watsonx Orchestrate that automatically:
1. **Detects** material budget variances in Planning Analytics (>$100K or >20%)
2. **Reads** root cause explanations embedded directly in the cube
3. **Generates** a CFO-ready variance report with stakeholder routing

Manual process: 3–4 days. With the autopilot: **under 5 minutes.**

---

## Architecture

```
User prompt
    │
    ▼
FP&A Variance Autopilot (Orchestrator)
    └── PA Data Agent  → IBM Planning Analytics (TM1)
                          reads variance data + embedded root causes
```

---

## Choose Your Path

Both paths end with the same two agents and the same variance report. Everyone starts with [Lab 2.0](lab-02-0-fpa-dataset-catchup/README.md) (5 min) to confirm the `FPA_Variance` cube.

| | ⚡ Fast path (recommended) | 🧭 Step-by-step path |
|-|---------------------------|---------------------|
| **Who** | Technical participants comfortable pasting a command into a terminal | Everyone who wants to see each piece in the Orchestrate UI |
| **How** | You send Bob one prompt; Bob sets up the Orchestrate ADK and builds both agents for you | You create the connection, the agents and their tools by hand in the Orchestrate UI |
| **Labs** | 2.0 → [Fast Path](lab-02-fast-path-build-with-bob/README.md) | 2.0 → 2.1 → 2.2 → 2.5 |
| **Time** | ~20 min | ~60 min |
| **You need** | Your own watsonx Orchestrate environment, Python 3.11–3.14, git and an Orchestrate API key | Your own watsonx Orchestrate environment with rights to create agents |

We recommend letting Bob build the agents (fast path): it is quicker, and the same build can be repeated in any Orchestrate environment. Take the step-by-step path when you want to see, or demo, how each piece fits together in the UI.

> 🚀 **About the "Ready to use" path:** the [Ready to Use](lab-02-ready-to-use/README.md) lab was written for a client workshop, where the agents were pre-built in that workshop's Orchestrate environment. **That environment has expired, so the path no longer works as written.** Build your own agents with one of the two paths above. If you need ready-to-use, pre-built agents for a demo or workshop, contact **Austin Zhang** (IBM Canada, Data & AI).

### Fast path

**→ [Lab 2 Fast Path — Let Bob Build the Agents](lab-02-fast-path-build-with-bob/README.md)**

You need your own watsonx Orchestrate environment, plus Python 3.11–3.14, git, and an Orchestrate API key on top of the Lab 0 setup. The fast path lists everything to prepare. It is the only part of the workshop that uses Bob's **🤖 Agent** mode, because Bob runs commands on your laptop; everything else uses **📊 Planning Analytics** mode.

### Step-by-step path

| Sub-Lab | Deliverable | Time |
|---------|-------------|------|
| [2.0](lab-02-0-fpa-dataset-catchup/README.md) | Confirm `FPA_Variance` cube | 5 min |
| [2.1](lab-02-1-pa-mcp-connection/README.md) | PA MCP connection in Orchestrate | 10 min |
| [2.2](lab-02-2-pa-agent/README.md) | PA Data Agent live, then changed with Bob | 25 min |
| [2.5](lab-02-5-orchestrator/README.md) | Full Autopilot running end-to-end | 20 min |

**→ [Start with Lab 2.0](lab-02-0-fpa-dataset-catchup/README.md)**

### Optional, for either path

| Sub-Lab | Deliverable | Time |
|---------|-------------|------|
| [2.7](lab-02-7-chat-embed/README.md) *(optional)* | Embedded chat page | 10 min |
| [2.8](lab-02-8-adk/README.md) *(bonus)* | Orchestrate ADK CLI, step by step | 30 min |

> **Note:** Root causes are read directly from the `FPA_Variance` cube — no CRM or ERP system is needed. The earlier CRM/ERP extension (Labs 2.3, 2.4, 2.6) is kept in [`archive/crm-erp-extension`](../archive/crm-erp-extension/README.md) for reference.

---

## Credentials Needed

- **PA:** `TECHZONE_HOST`, `PORT`, `TENANT_ID`, `USERNAME`, `PASSWORD` for a Planning Analytics environment that has the `FPA_Variance` cube on `smartco`. Reserve one on [TechZone (Planning Analytics)](https://techzone.ibm.com/my/reservations/create/69fe431559b0d2bd258c6c7b). A fresh reservation does not have the cube yet: build it once with Bob, see [FACILITATOR-SETUP, Section 2b](../FACILITATOR-SETUP.md#section-2b--fresh-environment-build-fpa_variance-on-smartco).
- **Orchestrate:** your own watsonx Orchestrate environment. Reserve one on [TechZone (watsonx Orchestrate)](https://techzone.ibm.com/collection/69cab99b72e4cbb50d5a1b45?platform=6a9827ac39d106720ddb08ed). For the fast path, also an **Orchestrate API key** (Profile icon → **Settings** → **API details**).

---

**→ [Continue to Session 3](../session-03-your-scenario/README.md)**
