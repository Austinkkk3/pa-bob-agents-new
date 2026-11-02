# Lab 2.4 — Create the CRM & ERP Agents

**Duration:** ~30 minutes  
**Prerequisite:** [Lab 2.3](../lab-02-3-saleslens-connection/README.md) ✅

---

## Goal

Build two focused sub-agents. Each gets 3 tools from the SalesLens OpenAPI spec.

> **Before you start:** Open [`saleslens-openapi-spec.json`](saleslens-openapi-spec.json), replace `<SALESLENS_ENDPOINT_URL>` in the `"servers"` block with your actual URL, and save.

---

## Part A — CRM Context Agent

### Create the Agent

**Orchestrate UI:** Build → All agents → Create agent

| Field | Value |
|-------|-------|
| **Name** | `CRM Context Agent` |
| **Description** | Queries the SalesLens CRM API for deal slippage and pipeline context. Returns root cause narratives for revenue variances. Does not query Planning Analytics or ERP. |
| **Model** | `granite-4-h-small` |

**ADK:** `orchestrate agents import --file ./crm-agent.yaml`

### Import Instructions

**Instructions** tab → **Import from YAML** → open [`crm-agent.yaml`](crm-agent.yaml) → paste → **Apply**

### Import CRM Tools via OpenAPI

1. Toolset → **Add tool** → **OpenAPI**
2. Drag and drop `saleslens-openapi-spec.json`
3. Select only the **3 CRM operations:**

```
✅ getCrmVarianceContext     GET /crm/variance-context
✅ getCrmDeals               GET /crm/deals
✅ getCrmPipelineSummary     GET /crm/pipeline-summary
```

4. **Next** → Connection: `SalesLens API Key` → **Done**

### Test

```
Get CRM variance context for DEPT-NA-SALES in January 2024.
```

Expected: 2 slipped deals ($200K), context summary, pipeline coverage 1.7x.

---

## Part B — ERP Context Agent

### Create the Agent

| Field | Value |
|-------|-------|
| **Name** | `ERP Context Agent` |
| **Description** | Queries the SalesLens ERP API for unbudgeted purchase orders and headcount events. Returns root cause narratives for OpEx and COGS variances. Does not query Planning Analytics or CRM. |
| **Model** | `granite-4-h-small` |

**ADK:** `orchestrate agents import --file ./erp-agent.yaml`

### Import Instructions

**Instructions** tab → **Import from YAML** → open [`erp-agent.yaml`](erp-agent.yaml) → paste → **Apply**

### Import ERP Tools via OpenAPI

1. Toolset → **Add tool** → **OpenAPI**
2. Drag and drop `saleslens-openapi-spec.json`
3. Select only the **3 ERP operations:**

```
✅ getErpCostContext         GET /erp/cost-context
✅ getErpPurchaseOrders      GET /erp/purchase-orders
✅ getErpHeadcountEvents     GET /erp/headcount-events
```

4. **Next** → Connection: `SalesLens API Key` → **Done**

### Test

```
Get ERP cost context for DEPT-NA-SALES in January 2024.
```

Expected: 1 unbudgeted PO ($18K TechWorld), 1 headcount event ($8.5K/mo new hire).

---

## Troubleshooting

| Symptom | Fix |
|---------|-----|
| File upload fails / no operations appear | Validate JSON: `python3 -m json.tool saleslens-openapi-spec.json` |
| 401 Unauthorized when agent calls tool | Open tool → Edit details → confirm `SalesLens API Key` connection is set |
| Empty `slipped_deals` | Check dept_id format: `DEPT-NA-SALES` (all caps, hyphens); period: `2024-01` |

---

**→ [Lab 2.5 — Create the Orchestrator Agent](../lab-02-5-orchestrator/README.md)**
