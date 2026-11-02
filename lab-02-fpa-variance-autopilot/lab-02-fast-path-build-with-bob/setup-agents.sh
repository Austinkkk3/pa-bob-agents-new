#!/usr/bin/env bash
# Lab 2 Fast Path (build with Bob): create the Lab 2 agents in one watsonx Orchestrate
# environment with the Orchestrate ADK.
#
# Creates, in order:
#   1. the PA connection (Basic Auth, team credentials, draft + live)
#   2. the PA MCP toolkit with the 6 read-only cube tools
#   3. pa_data_agent and fpa_variance_autopilot (imported from the YAML files here)
#   4. deploys both agents to Live
#
# Usage (from this folder, with the ADK installed in an active virtual environment):
#   export WXO_URL="https://api.<region>.watson-orchestrate.cloud.ibm.com/instances/<id>"
#   export PA_MCP_URL="http://<HOST>:<PORT>/api/<TENANT_ID>/v0/agentic-ai/cube/mcp"
#   VARIANT=AZ ./setup-agents.sh
#
# VARIANT (participants: your initials) adds a suffix to every name, so several people can
# build in the same Orchestrate environment: "PA Data Agent (AZ)" / pa_data_agent_az,
# "FP&A Variance Autopilot (AZ)" / fpa_variance_autopilot_az, connection and toolkit ending
# in -az. Without VARIANT (facilitator pre-build) the plain names are used.
#
# Run it in a real terminal (the VS Code terminal), not through Bob's command runner.
# The script asks for the Orchestrate API key and the PA password and never prints them.
# Safe to re-run: existing connection and toolkit are reused, agents are updated.

set -euo pipefail

: "${WXO_URL:?Set WXO_URL to the service instance URL from Orchestrate Settings > API details}"
: "${PA_MCP_URL:?Set PA_MCP_URL to http://<HOST>:<PORT>/api/<TENANT_ID>/v0/agentic-ai/cube/mcp}"
PA_USER="${PA_USER:-pm}"
ENV_NAME="${ENV_NAME:-workshop}"
VARIANT="${VARIANT:-}"
case "$VARIANT" in
  "") SUFFIX="" ;;
  *[!A-Za-z0-9]*) echo "VARIANT must be your initials, letters and digits only, for example VARIANT=AZ"; exit 1 ;;
  *) SUFFIX="$(printf '%s' "$VARIANT" | tr '[:upper:]' '[:lower:]')" ;;
esac
APP_ID="planning-analytics-basic${SUFFIX:+-$SUFFIX}"
TOOLKIT="planning-analytics-cube-mcp${SUFFIX:+-$SUFFIX}"
DATA_AGENT="pa_data_agent${SUFFIX:+_$SUFFIX}"
ORCH_AGENT="fpa_variance_autopilot${SUFFIX:+_$SUFFIX}"
LABEL="${VARIANT:+ ($VARIANT)}"
TOOLS="get_available_tm1_servers,get_tm1_cubes,get_cube_dimensions,get_cube_sample_members,execute_mdx_and_get_view,lookup_potential_members"
HERE="$(cd "$(dirname "$0")" && pwd)"

command -v orchestrate >/dev/null || { echo "The orchestrate CLI is not installed. Run: pip install ibm-watsonx-orchestrate"; exit 1; }

# The API key and the PA password must be typed in a real terminal so they stay hidden.
# Bob's command runner is not one: there, what you type would be echoed into the chat.
if [ ! -t 0 ]; then
  echo "Run this script yourself in the VS Code terminal (Terminal > New Terminal),"
  echo "so the API key and password you type stay hidden. Bob cannot run it for you."
  exit 2
fi

# The YAML files are used as they are; only the names change when VARIANT is set.
WORK="$(mktemp -d)"
trap 'rm -rf "$WORK"' EXIT
render() {
  sed -e "s/planning-analytics-cube-mcp:/$TOOLKIT:/g" \
      -e "s/pa_data_agent/$DATA_AGENT/g" \
      -e "s/^name: fpa_variance_autopilot\$/name: $ORCH_AGENT/" \
      -e "s/^display_name: \\(.*\\)\$/display_name: \\1$LABEL/" \
      "$HERE/$1" > "$WORK/$1"
}
render pa-data-agent.adk.yaml
render fpa-orchestrator.adk.yaml

echo "Building: ${DATA_AGENT}, ${ORCH_AGENT} (connection ${APP_ID}, toolkit ${TOOLKIT})"

echo "== 1/5 Connect to Orchestrate ($ENV_NAME)"
orchestrate env add -n "$ENV_NAME" -u "$WXO_URL" </dev/null >/dev/null 2>&1 || echo "   environment '$ENV_NAME' already exists, reusing it"
echo "   Paste your Orchestrate API key and press Enter (nothing is shown while you type):"
orchestrate env activate "$ENV_NAME"

read -r -s -p "   PA password for $PA_USER (nothing is shown while you type): " PA_PASSWORD; echo

echo "== 2/5 PA connection ($APP_ID)"
orchestrate connections add -a "$APP_ID" >/dev/null 2>&1 || echo "   connection already exists, reusing it"
for e in draft live; do
  orchestrate connections configure -a "$APP_ID" --env "$e" --type team --kind basic --url "$PA_MCP_URL"
  orchestrate connections set-credentials -a "$APP_ID" --env "$e" -u "$PA_USER" -p "$PA_PASSWORD"
done
unset PA_PASSWORD

echo "== 3/5 PA MCP toolkit ($TOOLKIT, 6 read-only tools)"
if COLUMNS=250 orchestrate toolkits list 2>/dev/null | grep -Eq "(^|[^[:alnum:]_-])${TOOLKIT}([^[:alnum:]_-]|\$)"; then
  echo "   toolkit already exists, reusing it"
else
  orchestrate toolkits add --kind mcp --name "$TOOLKIT" \
    --description "IBM Planning Analytics cube tools (read-only subset for the workshop)" \
    --url "$PA_MCP_URL" --transport streamable_http --tools "$TOOLS" --app-id "$APP_ID" || {
    echo "   Creating the toolkit failed. A 502 ConnectTimeout means Orchestrate could not reach"
    echo "   the PA server in time: wait a minute and run this script again (it reuses what exists)."
    exit 1
  }
fi

echo "== 4/5 Import the agents"
orchestrate agents import -f "$WORK/pa-data-agent.adk.yaml"
orchestrate agents import -f "$WORK/fpa-orchestrator.adk.yaml"

echo "== 5/5 Deploy to Live"
orchestrate agents deploy -n "$DATA_AGENT"
orchestrate agents deploy -n "$ORCH_AGENT"

echo
echo "Done. Open Orchestrate > Chat, pick 'FP&A Variance Autopilot${LABEL}' and ask:"
echo "  Run the FP&A variance analysis for January 2024 on the FPA_Variance cube on smartco."
echo "Expected: 4 material variances (2 HIGH, 1 MEDIUM, 1 FAVORABLE)."
