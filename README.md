# Planning Analytics × Bob × watsonx Orchestrate Workshop

**Duration:** 6 hours · Intermediate · Instructor-led

> 🚀 **New here?** Start with [QUICK-START.md](./QUICK-START.md) — credentials, 3-step validation, and key things to know on one page.

---

## What You'll Build

| | Lab | What you do |
|-|-----|-------------|
| 🛠 | [Lab 0 — Setup](./lab-00-setup/README.md) | Install PA mode & skill, configure MCP — all via Bob |
| 📊 | [Lab 1 — Bob + PA via MCP](./lab-01-bob-planning-analytics-mcp/README.md) | Query TM1 cubes, run variance analysis, build a model from CSV |
| 🤖 | [Lab 2 — FP&A Variance Autopilot](./lab-02-fpa-variance-autopilot/README.md) | Build agents in watsonx Orchestrate that detect material variances in PA, read the root causes stored in the cube and write a CFO-ready report. Use the [🚀 pre-built agents](./lab-02-fpa-variance-autopilot/lab-02-ready-to-use/README.md), or take the [⚡ fast path](./lab-02-fpa-variance-autopilot/lab-02-fast-path-build-with-bob/README.md) and let Bob build your own copy |
| ✍️ | [Lab 3 — Forecast Replan with Bob](./lab-03-forecast-replan-autopilot/README.md) *(optional)* | Use Bob to calculate an adjusted Q1 forecast and write it back to PA |
| 💡 | [Session 3 — Your Scenario](./session-03-your-scenario/README.md) | Adapt the autopilot pattern to your own use case |

---

## Agenda

| Session | Duration |
|---------|----------|
| Welcome + watsonx Orchestrate overview | 40 min |
| Bob overview + PA demo | 30 min |
| **Lab 0** — Environment setup | 30 min |
| *Break* | 15 min |
| **Lab 1** — Bob + Planning Analytics via MCP | 60 min |
| FP&A Variance Autopilot overview | 10 min |
| *Lunch* | 60 min |
| **Lab 2** — FP&A Variance Autopilot | 90 min |
| **Session 3** — Your Scenario | 15 min |
| Wrap-up + Q&A | 10 min |

---

## Prerequisites

| Requirement | Details |
|-------------|---------|
| **IBM Bob IDE** | [Download](https://bob.ibm.com/download) · min 200 coins |
| **IBM Planning Analytics** | TechZone environment — URL + credentials from facilitator |
| **watsonx Orchestrate** | Trial or SaaS tenant — confirm with facilitator |
| **Laptop** | macOS or Windows with internet access |

---

## Repository Structure

```
pa-bob-agents-new/
├── lab-00-setup/                         ← Environment setup (Bob-assisted)
├── lab-01-bob-planning-analytics-mcp/    ← Lab 1: Bob + PA via MCP
│   └── assets/                           ← CSV files for Exercise 5
├── lab-02-fpa-variance-autopilot/        ← Lab 2: FP&A Variance Autopilot
│   ├── assets/                           ← Screenshots
│   ├── lab-02-ready-to-use/              ← Ready to use: talk to the agents the facilitator pre-built
│   ├── lab-02-fast-path-build-with-bob/  ← Fast path: Bob builds both agents with the Orchestrate ADK
│   └── lab-02-*/                         ← Step-by-step sub-labs (2.0, 2.1, 2.2, 2.5; optional: 2.7, 2.8)
├── lab-03-forecast-replan-autopilot/     ← Lab 3 (optional): forecast write-back with Bob
├── planning-analytics-skill/             ← Bob skill installed in Lab 0
├── session-03-your-scenario/             ← Adapt to your use case
└── archive/                              ← Retired CRM/ERP extension (not part of the workshop)
```

---

**→ [Start with Lab 0](./lab-00-setup/README.md)**
