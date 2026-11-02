# Planning Analytics Skill

A comprehensive BOB skill for exploring IBM Planning Analytics and TM1 data through natural language queries, providing business-focused insights and executive-ready reporting.

## Overview

This skill transforms Planning Analytics into an accessible business intelligence platform, enabling users to:

- 🗣️ **Natural Language Queries** - Ask questions in plain English, not MDX
- 📊 **Variance Analysis** - Budget vs Actual, Forecast vs Actual, Period-over-Period
- 🔍 **Outlier Detection** - Identify anomalous patterns requiring attention
- 📈 **Key Driver Analysis** - Understand what's driving your results
- 📄 **Executive Reports** - Professional, business-ready formatting

## Quick Start

### Example Queries

```
"Show Q1 2025 compensation budget vs actual by department"
"What's driving revenue variance in the East region?"
"Find unusual expense patterns in March"
"Compare this year to last year by product"
"Show sales trends over the last 12 months"
```

## Installation

1. Create the skills directory in your workspace:
   ```bash
   mkdir -p .bob/skills/planning-analytics
   ```
2. Copy `SKILL.md`, `README.md`, and `USAGE-GUIDE.md` into `.bob/skills/planning-analytics/`
3. Restart Bob: `Cmd+Shift+P` → **Bob: Restart**
4. Verify: ask Bob `What skills do you have available?` — `planning-analytics` should appear.

## Key Features

### Financial Analysis
- Variance Analysis (Budget vs Actual, Forecast vs Actual, YoY)
- Trend Analysis (time-series, growth rates, seasonality)
- Outlier Detection (statistical anomalies)
- Key Driver Analysis (impact and sensitivity)

### Executive Reporting
- Clean table formatting with hierarchies
- Key findings summaries
- Data quality notes
- Actionable recommendations
- PDF report generation

### TM1 Expertise
- Cube design best practices
- Dimension structure guidance
- Rule and TurboIntegrator assistance
- Performance optimization tips

## Requirements

- IBM Planning Analytics or TM1 server access
- MCP server configured (`ibm-pa-tools-tz-cube`, `ibm-pa-tools-tz-server`)
- Pre-analyzed cubes for semantic queries (recommended)

## Limitations

| Can Do ✅ | Cannot Do ❌ |
|----------|-------------|
| Explore cubes with natural language | Create new cubes/dimensions |
| Variance and trend analysis | Write TurboIntegrator processes |
| Generate insights and reports | Modify cube data |
| TM1 guidance and best practices | Technical administration |

For tasks this skill cannot do, use **Advanced (Planning Analytics) mode**.

## Version

Current version: 1.0.0
