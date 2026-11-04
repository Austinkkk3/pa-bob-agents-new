# Lab 0 — Environment Setup

**Duration:** 10–15 minutes  
**Goal:** Install the Planning Analytics Bob mode & skill, configure MCP, and validate connectivity — all using Bob.

---

## Prerequisites

- IBM Bob IDE installed and logged in ([download here](https://bob.ibm.com/download))
- Your TechZone Planning Analytics URL (from your facilitator or your reservation page)
- Workshop folder open as your workspace root in Bob

> ⚠️ **Planning Analytics version must be 2.1.20** — other versions are not compatible with the MCP tools used in this workshop.

---

## Step 1 — Install the Skill

**Download the skill first:**
Click **[planning-analytics-skill.zip](https://github.com/Austinkkk3/pa-bob-agents-new/raw/main/lab-00-setup/planning-analytics-skill.zip)** to download it, then unzip it. You get a `planning-analytics-skill` folder with `SKILL.md`, `README.md` and `USAGE-GUIDE.md`; note where it is on your computer. If you cloned the repo, the same folder is at [`planning-analytics-skill/`](../planning-analytics-skill/).

> **Alternative:** Download directly from the IBM Building Blocks repo:
> Skill ZIP → [planning-analytics-skill.zip](https://github.com/ibm-self-serve-assets/building-blocks/blob/main/automation/optimize/budget-and-forecasting/bob-skills/planning-analytics-skill.zip)
> Mode ZIP → [planning-analytics-mode.zip](https://github.com/ibm-self-serve-assets/building-blocks/blob/main/automation/optimize/budget-and-forecasting/bob-modes/base-modes/planning-analytics-mode.zip)

**Then drag the folder into Bob's chat panel**, and send this message:

```
I've uploaded the planning-analytics-skill folder.
Please install it as a Bob skill:
1. Create the directory .bob/skills/planning-analytics/ in my workspace
2. Copy all files from the uploaded folder into .bob/skills/planning-analytics/
3. Confirm the files SKILL.md, README.md, and USAGE-GUIDE.md are in place
Then I'll restart Bob.
```

After Bob confirms, restart Bob: `Cmd+Shift+P` → **Bob: Restart**

✅ **Done when:** Ask Bob `What skills do you have available?` — `planning-analytics` appears in the list.

---

## Step 1b — Install the Planning Analytics Mode *(optional)*

The mode gives Bob deeper TM1 expertise and financial analysis workflows. Download `planning-analytics-mode.zip` from the [Building Blocks repo](https://github.com/ibm-self-serve-assets/building-blocks/tree/main/automation/optimize/budget-and-forecasting/bob-modes/base-modes), then tell Bob:

```
I've downloaded planning-analytics-mode.zip.
Please install it as a Bob mode:
1. Create .bob/modes/ if it doesn't exist
2. Unzip planning-analytics-mode.zip into .bob/modes/planning-analytics/
3. Move .bob/modes/planning-analytics/custom_modes.yaml to .bob/custom_modes.yaml
Then I'll restart Bob.
```

After Bob confirms, restart Bob. The mode selector should show **📊 Planning Analytics**.

---

## Step 2 — Configure MCP

MCP (Model Context Protocol) is the bridge that lets Bob call your Planning Analytics TM1 server directly. The whole setup is one prompt — just paste your TechZone URL and Bob does the rest.

### What you need

**One URL** — your Planning Analytics TechZone environment URL.  
It looks like one of these:

```
http://<region>.services.cloud.techzone.ibm.com:<PORT>/?accountId=<ACCOUNT_ID>&tenantId=<TENANT_ID>&perspective=pa-home
http://192.168.100.50:8080/api/abc123def/v0/...
```

The first form is the Planning Analytics Workspace link on the TechZone reservation page; either form works.

Where to find it:
- Your facilitator will display it on the screen, **or**
- Go to [techzone.ibm.com](https://techzone.ibm.com) → **My Reservations** → click your environment → copy the **Planning Analytics URL**

Your login credentials for this workshop are fixed:

| Field | Value |
|-------|-------|
| Username | `pm` |
| Password | `IBMDem0s` |

---

### The prompt — paste this into Bob

Copy the block below, **replace the URL on the first line** with your real TechZone URL, then send it to Bob:

```
My Planning Analytics TechZone URL is: http://<YOUR_TECHZONE_URL_HERE>
Username: pm
Password: IBMDem0s

Please configure my MCP connection by doing the following:
1. Parse the HOST, PORT, and TENANT_ID out of the URL I gave you.
   The URL is either http://<HOST>:<PORT>/api/<TENANT_ID>/v0/...
   or http://<HOST>:<PORT>/?accountId=...&tenantId=<TENANT_ID>&... (use the tenantId value, not the accountId).
2. Compute the Base64 encoding of "pm:IBMDem0s" — the result is cG06SUJNRGVtMHM=
3. Read the MCP template from lab-00-setup/mcp.json in my workspace.
4. Substitute all four placeholders in the template:
   - <TECHZONE_HOST> → the HOST you parsed
   - <PORT>          → the PORT you parsed
   - <TENANT_ID>     → the TENANT_ID you parsed
   - <BASE64_CREDENTIALS> → cG06SUJNRGVtMHM=
5. Open Cmd+Shift+P → Bob: Open MCP Settings and replace the entire
   contents of mcp.json with the fully substituted JSON.
6. Save the file.
7. Run Cmd+Shift+P → Bob: Restart.
8. After restarting, call the list-servers tool and confirm DemoGuide
   appears in the response.
```

Bob will parse the URL, fill in `mcp.json`, save it, restart, and verify the connection — no manual editing required.

---

### What Bob does behind the scenes

Given the URL `http://192.168.100.50:8080/api/abc123def/v0/agentic-ai/...`, Bob extracts:

| Placeholder | Extracted value |
|-------------|----------------|
| `<TECHZONE_HOST>` | `192.168.100.50` |
| `<PORT>` | `8080` |
| `<TENANT_ID>` | `abc123def` |
| `<BASE64_CREDENTIALS>` | `cG06SUJNRGVtMHM=` |

It then writes these into **both** server blocks in `mcp.json` (`ibm-pa-tools-tz-server` and `ibm-pa-tools-tz-cube`), saves, and restarts.

---

✅ **Done when:** Bob confirms it can see `DemoGuide` (or another TM1 server name) after restarting.

---

## Step 3 — Validate

Switch to **📊 Planning Analytics** mode and send:

```
List all available TM1 servers
```

✅ **Done when:** Bob returns at least one server name (e.g. `DemoGuide`).

---

## Troubleshooting

| Symptom | Fix |
|---------|-----|
| Mode not in selector | Check `.bob/custom_modes.yaml` exists → restart Bob |
| `401 Unauthorized` | Credentials wrong — confirm `pm` / `IBMDem0s` and that the Base64 value is `cG06SUJNRGVtMHM=` |
| `Connection refused` | Wrong HOST or PORT — re-check the URL with your facilitator; confirm you are on the same network |
| MCP servers show disconnected | Save `mcp.json` → Bob: Restart |
| Bob says it cannot find the URL pattern | Paste just the base URL (up to and including the TENANT_ID segment) and ask Bob to try again |

---

**→ [Continue to Lab 1](../lab-01-bob-planning-analytics-mcp/README.md)**
