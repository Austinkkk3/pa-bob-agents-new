# Lab 2.3 — Configure the SalesLens API Connection

**Duration:** ~10 minutes  
**Prerequisite:** [Lab 2.2](../lab-02-2-pa-agent/README.md) ✅

---

## Goal

Create the `saleslens-api-key` connection and store team credentials so CRM and ERP agents can authenticate with the SalesLens Mock API.

**Credentials from your facilitator:**
- **App URL:** `<SALESLENS_ENDPOINT_URL>`
- **API Key:** `<SALESLENS_API_KEY>` (header: `X-Api-Key`)

---

## Step 1 — Create the Connection

1. **Manage → Security → Connections** tab → **Add connection**
2. Fill in:

| Field | Value |
|-------|-------|
| **Connection ID** | `saleslens-api-key` |
| **Display name** | `SalesLens API Key` |

3. **Next** → Authentication type: **API Key** · Server URL: `<SALESLENS_ENDPOINT_URL>` · Credential type: **Team credential**
4. **Next** → **Paste draft configuration** to copy to live
5. **Add connection**

---

## Step 2 — Add Team Credentials

1. **Manage → Security → Team credentials** tab → **Live** environment → **Add team credential**
2. Select `SalesLens API Key` from the dropdown
3. Enter the API Key value provided by your facilitator
4. **Connect and save** — status should show ✅

> If the connection already exists, skip to Step 2 and verify the key is set.

---

## ✅ Done when

`saleslens-api-key` shows ✅ in **Manage → Security → Team credentials**.

---

## Troubleshooting

| Symptom | Fix |
|---------|-----|
| "Connection failed" on save | Verify `curl <APP_URL>/health` returns 200; check no trailing slash in URL |
| Connection ID already exists | Verify it has API Key + Team credentials set, then proceed |

---

**→ [Lab 2.4 — Create the CRM & ERP Agents](../lab-02-4-crm-erp-agents/README.md)**
