# Lab 2 Fast Path — Let Bob Build the Agents

**For:** technical participants who are comfortable pasting a command into a terminal
**Duration:** ~15 minutes
**Replaces:** Labs 2.1, 2.2 (Steps 1–5) and 2.5 (Steps 1–4). You end with the same two agents and the same report.
**Prerequisite:** [Lab 0](../../lab-00-setup/README.md) ✅ · [Lab 2.0](../lab-02-0-fpa-dataset-catchup/README.md) ✅ · a watsonx Orchestrate environment where you can build agents

> Want to see every piece being built in the Orchestrate UI? Use the [step-by-step path](../README.md#step-by-step-path) instead.

---

## In this lab

> 📍 **Where:** Bob in 🤖 Agent mode and the VS Code terminal, then watsonx Orchestrate in your browser  
> 🎯 **What you do:** Send Bob one prompt. Bob installs the Orchestrate ADK and builds both Lab 2 agents, with your initials in their names.  
> ⚡ **Why it matters:** About 15 minutes instead of about 60 clicking through Labs 2.1–2.5. The agents are built from YAML files, so the same build can be repeated in any Orchestrate environment.  
> ✅ **You leave with:** Your own FP&A Variance Autopilot, giving the same report as the shared one.

## What gets built

Instead of clicking through the Orchestrate UI, you give Bob one prompt. Bob sets up the watsonx Orchestrate **Agent Development Kit (ADK)** on your laptop and gives you one command to run. That command creates everything below in Orchestrate. Then Bob checks the result.

| What | Name (`AZ` = your initials) | Notes |
|------|------|-------|
| PA connection | `planning-analytics-basic-az` | Basic Auth, team credentials, draft and live |
| PA MCP toolkit | `planning-analytics-cube-mcp-az` | 6 read-only tools |
| Sub-agent | **PA Data Agent (AZ)** · `pa_data_agent_az` | Same tested instructions as Lab 2.2 |
| Orchestrator | **FP&A Variance Autopilot (AZ)** · `fpa_variance_autopilot_az` | Same instructions as Lab 2.5, with the PA Data Agent as collaborator |

Your initials are added to every name, so your agents never overwrite someone else's when several people build in the same Orchestrate environment.

---

## Before you start

**On your laptop**

| You need | Check |
|----------|-------|
| IBM Bob | From Lab 0 |
| Python 3.11–3.13 | `python3 --version`. The Python that ships with macOS is too old: install Python 3.12 from python.org or with Homebrew |
| git | `git --version`. On a Mac, the first `git` command may ask you to install the Command Line Tools: accept and wait a few minutes |
| Access to github.com and pypi.org | Bob downloads this repo and the ADK from them. Some company networks block them; if so, try another network |
| macOS or Linux | Tested on macOS. On Windows the script needs a bash terminal (WSL or Git Bash); without one, use the [step-by-step path](../README.md#step-by-step-path) |

**Values to collect**

| Value | How to get it | Where it goes |
|-------|---------------|---------------|
| Orchestrate service instance URL | In Orchestrate, click the **Profile icon** (top right) → **Settings** → **API details** tab → copy the **Service instance URL**. It looks like `https://api.<region>.watson-orchestrate.cloud.ibm.com/instances/<id>` | Into the prompt |
| PA MCP URL | The **Cube MCP URL** you used in Lab 0 (see [QUICK-START](../../QUICK-START.md#your-credentials)). It looks like `http://<HOST>:<PORT>/api/<TENANT_ID>/v0/agentic-ai/cube/mcp` | Into the prompt |
| Your initials | Letters and digits only, for example `AZ` | Into the prompt |
| Orchestrate API key | Same **API details** tab → **Generate API key**. Copy it right away; it is shown only once | Typed in the terminal only |
| PA password | For user `pm`, from your facilitator (see [QUICK-START](../../QUICK-START.md#your-credentials)) | Typed in the terminal only |

> 🔒 Never paste the API key or the PA password into the Bob chat. Bob's chat and its own command runner show everything you type. You enter both only in the VS Code terminal in Step 3, where they stay hidden.

---

## Step 1 — Edit the prompt and send it to Bob

1. In Bob, open a new task (**+**) and switch the mode to **🤖 Agent**: click the mode selector at the bottom left of the chat box, or press **⌘ + .** (Ctrl + . on Windows) until it shows Agent.

> **Why Agent mode?** This is the only part of the workshop that runs commands on your laptop (git, Python, the ADK installer). Everything else, including Lab 1, Lab 2.0 and Lab 3, uses **📊 Planning Analytics** mode, which carries the PA rules the expected results were tested with.
>
> Bob can change modes by itself in some cases (for example from Plan to Agent), but in our tests it did not leave Planning Analytics mode on its own. It handed over the commands to copy instead of running them. So switch to Agent mode yourself before you send the prompt, and switch back to Planning Analytics mode when you are done.
2. Copy the prompt below and replace the three values in step 3 of the prompt:

| In the prompt | Replace with |
|---------------|--------------|
| `<ORCHESTRATE_URL>` | Your Orchestrate service instance URL |
| `<PA_MCP_URL>` | The PA MCP URL |
| `<INITIALS>` | Your initials, for example `AZ` |

Leave everything else as it is.

```
Build the Lab 2 agents in my watsonx Orchestrate environment with the Orchestrate ADK.
Use the files in the repo exactly as they are: do not rewrite the YAML files, the script
or the agent instructions. Run steps 1, 2 and 4 yourself in the terminal, one at a time.
1. Clone https://github.com/Austinkkk3/pa-bob-agents-new.git into ~/pa-bob-agents-client,
   or run git pull if it is already there.
2. Check that Python 3.11-3.13 is available, create the virtual environment
   ~/pa-bob-agents-client/.venv-adk with it and install ibm-watsonx-orchestrate.
3. Do not run setup-agents.sh yourself: it asks for my Orchestrate API key and PA password,
   and your command runner cannot hide what I type. Give me one command to paste into the
   VS Code terminal that goes to lab-02-fpa-variance-autopilot/lab-02-fast-path-build-with-bob,
   activates the virtual environment and runs ./setup-agents.sh with these values:
   WXO_URL=<ORCHESTRATE_URL>
   PA_MCP_URL=<PA_MCP_URL>
   VARIANT=<INITIALS>
   Never ask me to paste the key or the password into the chat. Wait until I say it finished.
4. Then run "orchestrate agents list" and "orchestrate toolkits list" and confirm that the
   agents pa_data_agent and fpa_variance_autopilot and the toolkit planning-analytics-cube-mcp
   are there, each with my VARIANT in lowercase at the end of its name.
   If a step fails, show me the error and fix it.
```

For example, step 3 of the prompt could end up like this:

```
   WXO_URL=https://api.ca-tor.watson-orchestrate.cloud.ibm.com/instances/b1269f10-...
   PA_MCP_URL=http://xx.services.cloud.techzone.ibm.com:30123/api/TENANT123/v0/agentic-ai/cube/mcp
   VARIANT=AZ
```

3. Send the prompt.

---

## Step 2 — Approve Bob's commands

Bob asks before it runs each command. Read each one and click **Approve once**. In order, Bob will:

1. Clone (or update) the repo into `~/pa-bob-agents-client`
2. Check which Python version you have
3. Create the virtual environment `.venv-adk`
4. Install the ADK (`ibm-watsonx-orchestrate`). This takes 1–2 minutes
5. Read `setup-agents.sh` and give you the command to run

---

## Step 3 — Run the command in the VS Code terminal

1. Open the VS Code terminal: **View → Terminal** (or ⌘J / Ctrl+J).
2. Paste the command Bob gave you and press Enter.
3. When you see `Paste your Orchestrate API key and press Enter`, paste the API key and press Enter.
4. When you see `PA password for pm`, type the PA password and press Enter.

Nothing is shown while you type the key or the password; that is expected.

Apart from some `[INFO]` lines from the ADK, the terminal shows:

```
Building: pa_data_agent_az, fpa_variance_autopilot_az (connection planning-analytics-basic-az, toolkit planning-analytics-cube-mcp-az)
== 1/5 Connect to Orchestrate (wxo-xxxxxxxx)
   Paste your Orchestrate API key and press Enter (nothing is shown while you type):
   PA password for pm (nothing is shown while you type):
== 2/5 PA connection (planning-analytics-basic-az)
== 3/5 PA MCP toolkit (planning-analytics-cube-mcp-az, 6 read-only tools)
== 4/5 Import the agents
== 5/5 Deploy to Live
[INFO] - Successfully deployed agent pa_data_agent_az
[INFO] - Successfully deployed agent fpa_variance_autopilot_az

Done. Open Orchestrate > Chat, pick 'FP&A Variance Autopilot (AZ)' and ask: ...
```

It takes 1–2 minutes. If it stops at `3/5` with `502 ... ConnectTimeout`, Orchestrate could not reach the PA server in time. Wait a minute, press ↑ and Enter to run the same command again, and enter the key and password again. It reuses what was already created.

---

## Step 4 — Let Bob check the result

Back in Bob, send:

```
It finished.
```

Bob runs `orchestrate agents list` and `orchestrate toolkits list` and confirms your two agents and your toolkit. You can also see the agents in Orchestrate under **Active inventory → Agents**.

---

## Step 5 — Test in Orchestrate

In Orchestrate → **Chat**, pick **FP&A Variance Autopilot (AZ)** (with your initials) and send:

```
Run the FP&A variance analysis for January 2024 on the FPA_Variance cube on smartco.
Identify all material variances, explain the root causes, and generate a full variance report.
```

Expected: the same report as [Lab 2.5](../lab-02-5-orchestrator/README.md#step-5--run-the-end-to-end-autopilot), with 4 material variances:

- 🔴 HIGH — NA Sales REV-001: -$175,000
- 🔴 HIGH — NA Sales OPEX-001: +$25,000
- 🟡 MEDIUM — IT OPEX-007: +$14,000
- ✅ FAVORABLE — NA Sales OPEX-004: -$17,500

Company totals: revenue -$147,000 (-7.44%). Expect 1–2 minutes for the answer.

---

## Next

- Switch Bob back to **📊 Planning Analytics** mode for the rest of the workshop.
- Try the prompts in [Lab 2.5 — More Prompts to Try](../lab-02-5-orchestrator/README.md#more-prompts-to-try) with your agent.
- Change the agent's materiality rule with Bob in [Lab 2.2 Step 6](../lab-02-2-pa-agent/README.md#step-6--change-the-agent-with-bob-5-minutes). Open **PA Data Agent (AZ)** where that step says "your PA Data Agent".
- **→ [Lab 3 — Forecast Replan with Bob](../../lab-03-forecast-replan-autopilot/README.md)** *(optional)*: back in Bob, start a new task in 📊 Planning Analytics mode.
- **→ [Continue to Session 3](../../session-03-your-scenario/README.md)**

---

## What is in this folder

Bob runs these files as they are. The PA Data Agent's fixed MDX query was tested and is easy to break, so the prompt tells Bob not to rewrite anything.

| File | Purpose |
|------|---------|
| [`pa-data-agent.adk.yaml`](pa-data-agent.adk.yaml) | PA Data Agent with its 6 tools, GPT-OSS 120B, ReAct Core style |
| [`fpa-orchestrator.adk.yaml`](fpa-orchestrator.adk.yaml) | Orchestrator with the PA Data Agent as collaborator |
| [`setup-agents.sh`](setup-agents.sh) | Creates the connection and toolkit, imports both agents with your initials added, deploys them to Live |

Without `VARIANT`, the script builds the agents under their plain names (`pa_data_agent`, `fpa_variance_autopilot`) and updates them if they already exist. Facilitators can use this to pre-build the agents in an environment.

---

## Troubleshooting

| Symptom | Fix |
|---------|-----|
| Bob gives you commands to copy instead of running them | Bob is still in Planning Analytics mode. Switch to **Agent** mode (mode selector or ⌘ + .) and ask it to run the steps itself |
| `Run this script yourself in the VS Code terminal` | Bob tried to run `setup-agents.sh` itself. Paste the command into the VS Code terminal and run it there |
| `VARIANT may contain only letters and digits` | `<INITIALS>` was not replaced, or contains a space or symbol. Use only letters and digits, for example `AZ` |
| `orchestrate: command not found` | The virtual environment is not active. Use the full command from Bob, which starts with `cd` and `source .../.venv-adk/bin/activate` |
| Python version error during install | Install Python 3.12 and ask Bob to recreate `.venv-adk` with it |
| `Error getting IBM_IAM Token` or `401` | The API key is wrong or was not pasted completely. Generate a new key and check that `WXO_URL` is the service instance URL from **API details** |
| `401 ... Invalid authentication credentials` when creating the toolkit | The PA password was wrong (for example the API key was pasted again). Run the command again and type the PA password by hand |
| `502 ... ConnectTimeout` when creating the toolkit | Wait a minute and run the command again; it reuses the connection that was already created |
| Agent import says a tool is not found | Ask Bob to run `orchestrate tools list` and check that the 6 tools start with your toolkit name (`planning-analytics-cube-mcp-az:`) |
| Bob rewrites the YAML or the instructions | Stop it and resend the prompt; the files must be used as they are |
| You pasted the API key into the Bob chat by mistake | Delete that key in Orchestrate (**Settings → API details**), generate a new one, and delete that Bob task |
