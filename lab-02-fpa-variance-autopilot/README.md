# Lab 2 — FP&A Variance Autopilot

**Duration:** ~20 minutes (fast path) or ~60 minutes (step-by-step path)
**Tools:** watsonx Orchestrate · IBM Planning Analytics · IBM Bob (fast path)
**Prerequisite:** [Lab 0](../lab-00-setup/README.md) ✅ · [Lab 1](../lab-01-bob-planning-analytics-mcp/README.md) ✅

---

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

Both paths build the same two agents and end with the same variance report. Everyone starts with [Lab 2.0](lab-02-0-fpa-dataset-catchup/README.md) (5 min) to confirm the `FPA_Variance` cube.

| | ⚡ Fast path | 🧭 Step-by-step path |
|-|-------------|---------------------|
| **Who** | Technical participants comfortable pasting a command into a terminal | Everyone who wants to see each piece in the Orchestrate UI |
| **How** | You send Bob one prompt; Bob sets up the Orchestrate ADK and builds both agents with you | You create the connection, the agents and their tools by hand in the Orchestrate UI |
| **Labs** | 2.0 → [Fast Path](lab-02-fast-path-build-with-bob/README.md) | 2.0 → 2.1 → 2.2 → 2.5 |
| **Time** | ~20 min | ~60 min |

### Fast path

**→ [Lab 2 Fast Path — Let Bob Build the Agents](lab-02-fast-path-build-with-bob/README.md)**

You need Python 3.11–3.13, git, and an Orchestrate API key on top of the Lab 0 setup. The fast path lists everything to prepare. It is the only part of the workshop that uses Bob's **🤖 Agent** mode, because Bob runs commands on your laptop; everything else uses **📊 Planning Analytics** mode.

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

Your facilitator will provide:
- **PA:** `TECHZONE_HOST`, `PORT`, `TENANT_ID`, `USERNAME`, `PASSWORD`
- **Orchestrate:** Tenant URL

For the fast path, you also generate an **Orchestrate API key** yourself (Profile icon → **Settings** → **API details**).

---

**→ [Continue to Session 3](../session-03-your-scenario/README.md)**
