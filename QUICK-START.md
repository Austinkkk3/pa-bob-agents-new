# Quick Start — Dev Day Workshop

Everything you need to get going in the first 5 minutes.

---

## Your Credentials

| Item | Value |
|------|-------|
| **PA URL (TechZone)** | Ask your facilitator |
| **Tenant ID** | Ask your facilitator |
| **PA Username** | `pm` |
| **PA Password** | `IBMDem0s` |
| **Cube MCP URL** | `http://<HOST>:<PORT>/api/<TENANT_ID>/v0/agentic-ai/cube/mcp` |
| **Server MCP URL** | `http://<HOST>:<PORT>/api/<TENANT_ID>/v0/agentic-ai/analysis/mcp` |
| **Orchestrate URL** | Ask your facilitator |
| **Bob base64 auth** | `cG06SUJNRGVtMHM=` (`pm:IBMDem0s`) |

---

## 3-Step Validation (do this first)

**Step 1 — MCP is connected**  
In Bob, send:
```
List all available TM1 servers
```
Expected: list of 14 servers including `smartco`.

**Step 2 — Warm up the query engine (30 seconds)**  
Open the PAW URL in your browser → log in as `pm` / `IBMDem0s`  
→ Data and Models → New workbench → right-click any cube → Add new view → wait 30s.  
*(Skip this and MDX queries will return a 409 error.)*

**Step 3 — Query works**  
In Bob (📊 Planning Analytics mode), send:
```
Show me the dimensions of the FPA_Variance cube on smartco
```
Expected: 6 dimensions — FPA_Account, FPA_Department, FPA_Scenario, FPA_Time, FPA_Version, FPA_Measures.

---

## Lab Navigation

| Lab | What you build | Key tool |
|-----|----------------|----------|
| [Lab 0](lab-00-setup/README.md) | MCP config, skill, mode | Bob settings |
| [Lab 1](lab-01-bob-planning-analytics-mcp/README.md) | Query, analyse, build TM1 model | Bob + PA MCP |
| [Lab 2](lab-02-fpa-variance-autopilot/README.md) | Multi-agent variance autopilot ([⚡ fast path](lab-02-fpa-variance-autopilot/lab-02-fast-path-build-with-bob/README.md): Bob builds it) | watsonx Orchestrate |
| [Lab 3](lab-03-forecast-replan-autopilot/README.md) | Forecast write-back to PA | Bob |

---

## Key Things to Know

**Which Bob mode?**

| Work | Mode |
|------|------|
| Anything with Planning Analytics data: Lab 1, Lab 2.0, Lab 2.2 Step 6, Lab 3 | 📊 Planning Analytics |
| [Lab 2 Fast Path](lab-02-fpa-variance-autopilot/lab-02-fast-path-build-with-bob/README.md): Bob installs the Orchestrate ADK and runs commands on your laptop | 🤖 Agent |

Switch with the mode selector at the bottom left of the Bob chat, or press **⌘ + .** (Ctrl + . on Windows) to move to the next mode. Bob does not reliably switch out of Planning Analytics mode by itself: if it gives you commands to copy instead of running them, switch to Agent mode yourself. Switch back to Planning Analytics mode afterwards; the expected results in the labs were tested in that mode.

**Shared Orchestrate tenant?**  
Prefix all your agent names with your initials — `JD_pa_data_agent` not `pa_data_agent`. Change the `name:` field in the YAML too before importing. On the Lab 2 fast path, putting your initials in `VARIANT` does this for you.

**FPA_Variance data layout:**  
`V1` = Actual · `V2` = Budget · `V3` = Reforecast  
`Scenario "Actual"` + `Version V1` = actual values  
`Scenario "Budget"` + `Version V2` = budget values

**Imported agents have no tools yet:**  
ADK `agents import` creates the agent shell only. Add MCP tools in the agent's **Tools** tab → **Add tool → MCP server** in the Orchestrate UI. (The Lab 2 fast path script creates the toolkit first, so its agents come with their tools.)

**Testing agents:**  
Use **Active inventory → Agents → (your agent) → Preview panel** — not the Chat page. Chat only shows published (Live) agents.

---

## ADK Quick Reference

```bash
# Activate environment
echo "<API_KEY>" | orchestrate env activate <env-name>

# Import agents
orchestrate agents import --file ./pa-data-agent.yaml
orchestrate agents import --file ./fpa-orchestrator-agent.yaml

# List agents
orchestrate agents list

# List connections
orchestrate connections list

# Configure a connection credential
orchestrate connections configure \
  --app-id <app-id> \
  --environment live \
  --type team \
  --kind basic \
  -e username=pm \
  -e password=IBMDem0s \
  -e server_url="<MCP_URL>"
```

---

**Made with IBM Bob — Planning Analytics × watsonx Orchestrate Workshop**
