# Lab 3 — Facilitator Setup Guide

**Time required:** ~10 minutes  
**When to run:** Before the workshop session that includes Lab 3. Run once per TechZone environment.

---

## What This Setup Does

Creates the `FPA_Write_Forecast` and `FPA_Reset_Forecast` TI processes on `smartco`, so participants can use Bob to write V3 forecast values into the `FPA_Variance` cube and the facilitator can clear them afterwards.

> **Good news — nothing else is needed:**
> - `V3` already exists in the `FPA_Version` dimension ✅
> - `FC-Q1` already exists in the `FPA_Scenario` dimension ✅
> - `FPA_Variance` cube is already built on `smartco` ✅ (on a fresh environment, build it first: see [Section 2b of the root facilitator guide](../FACILITATOR-SETUP.md#section-2b--fresh-environment-build-fpa_variance-on-smartco))

---

## Option A — Use Bob (Recommended, 3–5 minutes)

Switch to **Planning Analytics mode** in Bob and run this prompt. It creates both Lab 3 processes and tests them. Tested on November 3, 2026 on a fresh environment.

```
Stay in Planning Analytics mode. Lab 3 setup on the smartco server (the FPA_Variance cube already exists there).
(1) Create the TI process FPA_Write_Forecast with parameters pTime (String, default 2024-01), pAccount (String,
default REV-001), pDept (String, default DEPT-NA-SALES), pScenario (String, default FC-Q1), pVersion (String,
default V3) and pAmount (Numeric, default 0), whose epilog is
CellPutN(pAmount, 'FPA_Variance', pAccount, pDept, pScenario, pTime, pVersion, 'Amount');
(2) create the TI process FPA_Reset_Forecast with no parameters that sets Amount to 0 for scenario FC-Q1, version V3,
months 2024-01, 2024-02 and 2024-03, for every leaf account and every leaf department, and touches no other scenario,
version or month. Write each procedure as one physical line, statements separated by semicolons, no comments.
(3) Test: run FPA_Write_Forecast to write 325000 to REV-001 / DEPT-NA-SALES / FC-Q1 / 2024-01 / V3 and read it back;
then run FPA_Reset_Forecast and confirm that cell is 0 again and that FC-Q1 / V4 for the same cell is still 480000.
Report the results as a short list. Do not change anything else.
```

Expected: the write reads back as 325,000, the reset brings it back to 0, and FC-Q1 / V4 stays 480,000. V4 holds the seeded forecasts from the CSV, so `FPA_Reset_Forecast` must never touch it.

---

## Option B — Manual Steps

If Bob is unavailable, create the process manually via the TM1 REST API or Architect:

### Process parameters

| Name | Type | Default |
|------|------|---------|
| `pTime` | String | `2024-01` |
| `pAccount` | String | `REV-001` |
| `pDept` | String | `DEPT-NA-SALES` |
| `pScenario` | String | `FC-Q1` |
| `pVersion` | String | `V3` |
| `pAmount` | Numeric | `0` |

### Epilog procedure (single line, no line breaks)

```
CellPutN(pAmount, 'FPA_Variance', pAccount, pDept, pScenario, pTime, pVersion, 'Amount');
```

Leave Prolog, Metadata, and Data procedures empty.

---

## Verify Setup is Complete

Run the following MDX in Bob (Planning Analytics mode) to confirm V3 is writable:

```
For NA Sales REV-001 and OPEX-001, January through March 2024, show:
- Actual (scenario Actual, version V1)
- Budget (scenario Budget, version V2)
- Reforecast (scenario FC-Q1, version V3)
side by side in FPA_Variance on smartco.
```

Expected (before Lab 3 runs):
- V1 Actual = 325,000 for REV-001 Jan; 145,000 for OPEX-001 Jan
- V2 Budget = 500,000 for REV-001 Jan; 120,000 for OPEX-001 Jan
- V3 FC-Q1 = 0 (empty — written by participants during Lab 3)

---

## Reset Between Workshop Runs

To clear V3 values before a fresh workshop run, ask Bob (Planning Analytics mode):

```
Run the FPA_Reset_Forecast process on smartco to clear the FC-Q1 / V3 reforecast,
then read back FC-Q1 / V3 for NA Sales REV-001 and OPEX-001, 2024-01 to 2024-03, and confirm they are all 0.
```

> Tested on October 26 and November 4, 2026: all 6 cells written in Lab 3 were cleared. `FPA_Reset_Forecast` only clears 2024-01 to 2024-03. Values written to other months are not cleared.

Or run this MDX to check what V3 values exist before clearing:

```
Show me all non-zero V3 values in FPA_Variance on smartco for scenario FC-Q1.
```

---

## Quick Reference — MCP Endpoints

| Endpoint | Tools available |
|----------|----------------|
| `.../v0/agentic-ai/cube/mcp` | cube read/query tools (`execute_mdx_and_get_view`, etc.) |
| `.../v0/agentic-ai/analysis/mcp` | server tools including `execute_tm1_processes_asynchronously`, `get_tm1_server_process_execution_error_logs` |

---

*Lab 3 — Forecast Replan with Bob · Facilitator Setup*  
*Made with IBM Bob — Planning Analytics × watsonx Orchestrate Workshop*
