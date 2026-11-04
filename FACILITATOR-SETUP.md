# Facilitator Setup — Environment Values

Fill in the values below before each session. **Share the completed credential sheet with each participant** at the start of the workshop — keep this page open during the session.

**Workshop lab repo:** https://github.com/Austinkkk3/pa-bob-agents-new

---

## Section 1 — IBM Planning Analytics (TechZone)

TechZone shared instance — used in Lab 0, Lab 1, Lab 2, Lab 3.

| Placeholder | Your Value |
|-------------|------------|
| `<TECHZONE_HOST>` | |
| `<PORT>` | |
| `<TENANT_ID>` | |
| `<PA_USERNAME>` | `pm` |
| `<PA_PASSWORD>` | `IBMDem0s` |

**Full MCP URL to share with participants:**
```
http://<TECHZONE_HOST>:<PORT>/api/<TENANT_ID>/v0/agentic-ai/cube/mcp
```

**Bob MCP config** (`~/.bob/settings/mcp.json`) — already configured in Lab 0. No changes needed for Lab 2/3.

---

### Skill download for Lab 0

Participants download the Bob skill from [`lab-00-setup/planning-analytics-skill.zip`](lab-00-setup/planning-analytics-skill.zip). If you change anything in `planning-analytics-skill/`, rebuild the zip from the repo root so the two stay in sync:

```bash
rm -f lab-00-setup/planning-analytics-skill.zip && zip -rX lab-00-setup/planning-analytics-skill.zip planning-analytics-skill
```

### Practice server for Lab 1 Exercise 5

Exercise 5 has every participant build a cube, 6 dimensions and several TI processes. To keep `smartco` clean for Lab 2 and Lab 3, participants build on a separate TM1 server on the same PA instance: **`DemoGuide`** on the TechZone image (one near-empty cube, no rules, no system processes). If you use a different server, update the server name in the Exercise 5 prompts.

- **Before the session:** ask Bob `List all available TM1 servers` and confirm `DemoGuide` is there.
- **After the session:** delete the objects participants created on `DemoGuide` (all start with their initials).
- **Large groups:** each build takes about 6.5 minutes and about 9 Bob coins, and the load of many builds at once has not been tested. With 10+ participants, consider demoing Exercise 5 instead.

---

## Section 2 — watsonx Orchestrate

Used in Lab 2 only. Each participant gets their own Orchestrate environment.

### How to provision participant environments

1. Go to your IBM TechZone reservation or IBM Cloud account
2. For each participant, provision a **watsonx Orchestrate** instance or share access to your tenant
3. Each participant logs in at their own Orchestrate URL (format: `https://<tenant>.watson-orchestrate.ibm.com`)

### What to share with each participant

Give each person a credential card with:

| Item | Value |
|------|-------|
| Orchestrate URL | `https://<their-tenant>.watson-orchestrate.ibm.com` |
| Login | IBM ID (their own) or shared credentials |
| PA MCP URL | `http://<TECHZONE_HOST>:<PORT>/api/<TENANT_ID>/v0/agentic-ai/cube/mcp` |
| PA Username | `pm` |
| PA Password | `IBMDem0s` |

### If using a shared tenant (simplest option)

All participants log into **your** Orchestrate tenant. Ask each person to prefix their agent names with their initials to avoid collisions (e.g. `JD-PA-Data-Agent`).

---

## Section 2b — Fresh environment: build `FPA_Variance` on smartco

A newly reserved TechZone PA environment does **not** have the shared `FPA_Variance` cube that Lab 1 (Exercises 1–4), Lab 2 and Lab 3 use. Build it once per environment with Bob in **📊 Planning Analytics** mode, with this repo open as the workspace and Bob's MCP settings pointing at the new environment. Tested on November 3, 2026: about 6 minutes and about 6 Bob coins, no retries.

```
Stay in Planning Analytics mode: the PA MCP tools in this workspace can create dimensions, cubes and TI processes.
This is the facilitator setup for a fresh workshop environment. First list the TM1 servers and the cubes on smartco;
if a cube named FPA_Variance already exists, stop and tell me. Otherwise build the shared FPA_Variance model on the
smartco server from the CSV files in lab-01-bob-planning-analytics-mcp/assets/ (dim_account.csv, dim_department.csv,
dim_scenario.csv, dim_time.csv, dim_version.csv, fact_financial_data.csv), with exactly these names and no prefix.
(1) Dimensions FPA_Account, FPA_Department, FPA_Scenario, FPA_Time and FPA_Version; the members are the id column of
each CSV. In FPA_Account the parent_account column defines the hierarchy (ROOT > TOTAL-REV, TOTAL-COGS, TOTAL-OPEX >
accounts); in FPA_Department parent_dept defines it (TOTAL-COMPANY > BU-* > departments). Store the descriptive CSV
columns as text attributes, not aliases.
(2) Dimension FPA_Measures with exactly two members: Amount (Numeric) and RootCause (String).
(3) Cube FPA_Variance with the dimensions in this order: FPA_Account, FPA_Department, FPA_Scenario, FPA_Time,
FPA_Version, FPA_Measures.
(4) TI processes FPA_Build_Dimensions and FPA_Build_Time for the dimensions and FPA_Load_Facts for the data; the
processes cannot read local files, so embed the rows in the code. FPA_Load_Facts loads all 280 rows: CellPutN for
amount into Amount, and CellPutS for variance_explanation into RootCause where it is not empty (escape single quotes).
Write each procedure as one physical line with statements separated by semicolons and no comments; insert elements
with DimensionElementInsert in the Prolog and set every parent-child link explicitly with
DimensionElementComponentAdd(dimension, parent, child, 1), otherwise the totals stay 0; create and fill attributes
(AttrInsert, AttrPutS) in the Epilog, after the elements are committed.
(5) Run the processes and verify with MDX: 280 non-empty Amount cells at leaf level; 86 non-empty RootCause cells,
34 of them on scenario Actual; for 2024-01 at TOTAL-COMPANY, TOTAL-REV Budget (Budget, V2) 1,975,000 and Actual
(Actual, V1) 1,828,000, TOTAL-COGS 125,000 and 135,000, TOTAL-OPEX 1,250,000 and 1,308,500; FC-Q1 / V3 empty.
Report the results as a short list. Work only on smartco and do not change any other cube, dimension or process.
```

The rules in step (4) come from the first build, where Bob spent several extra minutes on attributes set before the elements existed and on totals that stayed 0 without explicit parent-child links.

Then create the two Lab 3 processes as described in Section 3, and in Orchestrate pre-build the Lab 2 agents with [`setup-agents.sh`](lab-02-fpa-variance-autopilot/lab-02-fast-path-build-with-bob/setup-agents.sh) (no `VARIANT`).

---

## Section 3 — Lab 3 Setup (Bob write-back)

Run once before Lab 3. On an environment prepared for an earlier session, `FPA_Write_Forecast` and `FPA_Reset_Forecast` already exist on `smartco`; on a fresh environment, create them with the prompt in [`lab-03-forecast-replan-autopilot/FACILITATOR-SETUP.md`](lab-03-forecast-replan-autopilot/FACILITATOR-SETUP.md). To verify:

```
In Bob (Planning Analytics mode):
"Show me the TI processes on smartco that start with FPA"
```

Expected: `FPA_Build_Dimensions`, `FPA_Build_Time`, `FPA_Load_Facts`, `FPA_Write_Forecast`, `FPA_Reset_Forecast`



---

## Quick Reference — All Placeholders

| Placeholder | Where used | Value |
|-------------|-----------|-------|
| `<TECHZONE_HOST>` | Lab 0, 1, 2, 3 | TechZone reservation details |
| `<PORT>` | Lab 0, 1, 2, 3 | TechZone reservation details |
| `<TENANT_ID>` | Lab 0, 1, 2, 3 | TechZone reservation details |
| `<PA_USERNAME>` | Lab 0, 1, 2, 3 | `pm` |
| `<PA_PASSWORD>` | Lab 0, 1, 2, 3 | `IBMDem0s` |
| `<ORCHESTRATE_URL>` | Lab 2 | Per-participant Orchestrate tenant |

---

## Troubleshooting

### PA grid service returns 409 on MDX queries

**Symptom:** Bob returns `Status code: 409` when querying cube data, even though the MCP connection is working and TI processes run fine.

**Cause:** The PA grid service (query engine) uses lazy initialisation and may not be running when the TM1 server first starts.

**Fix (< 1 minute):**
1. Open the Planning Analytics Workspace (PAW) URL from the TechZone reservation page
2. Log in as `pm` / `IBMDem0s`
3. Go to **Data and Models** → **New workbench** → expand any server → right-click any cube → **Add new view**
4. Wait ~30 seconds
5. Return to Bob and retry the query — the grid service will now be warm

**Why it works:** Opening a workbench view in PAW sends a real UI request to the grid service, which kickstarts it. This only needs to be done once per session.
