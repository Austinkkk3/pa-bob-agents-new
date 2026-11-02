# Session 3 — Your Scenario

**Duration:** 15 minutes  
**Prerequisite:** [Lab 2](../lab-02-fpa-variance-autopilot/README.md) ✅

---

## Map the Pattern to Your Own Use Case

Answer these three questions (one sentence each), then paste them into Bob.

**1. What is the planning object?**  
The cube / data you would monitor.  
*e.g. Headcount and comp by department · Capex by project · Manufacturing costs by plant*

**2. What is the variance story?**  
The comparison that matters.  
*e.g. Budget vs Actual at month-end · Forecast vs Actual mid-month · YoY performance*

**3. Where does the root cause live?**  
The external system that explains the variance.  
*e.g. HRIS (open positions, attrition) · ERP (POs, invoices) · Operations (downtime, yield)*

---

## Bob Prompt — Adapt the Autopilot

```
I want to adapt the FP&A Variance Autopilot for my own scenario:

- Planning object: [your answer to Q1]
- Variance story:  [your answer to Q2]
- Root cause system: [your answer to Q3]

Based on this:
1. What would the agent description look like for this use case?
2. What are the 2–3 most important changes to the orchestrator agent instructions?
3. What external API or data source would I need to connect?

Keep it concise — one paragraph per answer.
```

---

## Bob Prompt — Generate a Ready-to-Import Agent YAML *(optional)*

```
Generate a ready-to-import watsonx Orchestrate ADK agent YAML for my scenario:

- Planning object: [your answer to Q1]
- Variance story:  [your answer to Q2]
- Root cause system: [your answer to Q3]

Requirements:
- spec_version: v1, kind: native
- Clear name (snake_case) and one-line description
- Instructions: detect material variances, investigate root cause from external system,
  return a CFO-ready plain-language summary
- LLM: groq/openai/gpt-oss-120b
- style: default, no collaborators or tools yet

Return only the YAML.
```

Import it with: `orchestrate agents import -f your-scenario-agent.yaml`

---

## Inspiration

| Scenario | Planning Object | Root Cause System |
|----------|----------------|-------------------|
| Sales Performance | Revenue by rep/region | CRM deal pipeline |
| Headcount Monitor | HC and comp by dept | HRIS attrition + open positions |
| Capex Tracker | Project spend vs approved | ERP POs + invoices |
| Manufacturing Cost | Production costs by plant | MES downtime + scrap rates |
| Cash Flow Warning | Cash actuals vs forecast | AP/AR aging from ERP |

---

[← Back to Workshop Home](../README.md)
