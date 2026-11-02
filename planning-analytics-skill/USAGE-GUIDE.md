# Planning Analytics Skill - Usage Guide

This guide explains how to use the Planning Analytics skill to explore TM1 data, perform financial analysis, and generate business insights using natural language queries.

## Quick Start

### Step 1: Activate the Skill

```
"Show me Q1 compensation variance by department"
```

Or explicitly:
```
"Use planning-analytics skill to analyze sales data"
```

### Step 2: Ask Your Question

```
"Show Q1 2025 compensation budget vs actual by department"
"What's driving revenue variance in the East region?"
"Find unusual expense patterns in March"
"Compare this year to last year by product"
```

### Step 3: Review Results

The skill returns formatted data tables, key findings, data quality notes, and recommendations.

---

## Query Patterns

### Variance Analysis
```
"Show budget vs actual for Q1 by department"
"What's the variance in compensation expenses?"
"Compare this year to last year by product line"
```

### Trend Analysis
```
"Show sales trends over the last 12 months"
"What are the quarterly revenue patterns?"
"Identify seasonal variations in expenses"
```

### Outlier Detection
```
"Find unusual sales patterns in Q4"
"Show outliers in expense data"
"Identify departments with significant variances"
```

### Key Driver Analysis
```
"What's driving revenue changes?"
"Show key drivers of expense variance"
"What factors most impact profitability?"
```

---

## Understanding Results

Every response includes:

| Section | What it tells you |
|---------|------------------|
| **Data Table** | Formatted numbers with hierarchy |
| **Key Findings** | Most important insights |
| **Data Notes** | Quality issues or limitations |
| **Explanation** | Why certain data was selected |

---

## Advanced Analytics

### Outlier Detection
Ask: `"Find unusual sales patterns in Q4 2024"`  
Get: Multiple detection algorithms, statistical scores, business context, recommended actions.

### Key Driver Analysis
Ask: `"What's driving revenue variance in the East region?"`  
Get: Driver rankings, impact scores, business interpretation, action items.

### PDF Reports
Ask: `"Generate a PDF analysis report for Q1 revenue"`  
Get: Executive-ready PDF with charts and AI-generated insights.

---

## Best Practices

✅ **Be specific:** `"Show Q1 2025 compensation budget vs actual by department"`  
✅ **Include context:** `"Compare this year to last year by product line"`  
✅ **Use business terms:** `"What's the variance in compensation expenses?"`  

❌ **Avoid vague queries:** `"show me data"`  
❌ **Avoid MDX syntax:** `"SELECT FROM [Cube] WHERE..."`  

---

## Troubleshooting

| Issue | Solution |
|-------|----------|
| "No pre-analyzed cubes found" | List all cubes first; use explicit cube names |
| "Cannot find dimension member" | Use `lookup_potential_members`; check spelling |
| "Data not available for period" | Check available time periods; adjust query |
| "Cube not found" | List available cubes; verify server connection |

---

## Examples

### Monthly Variance Review
```
"Show me March 2025 compensation variance by department"
```
Returns: Budget vs Actual table, key findings, department hierarchy, recommendations.

### Trend Analysis
```
"What are the revenue trends over the last 12 months?"
```
Returns: Monthly data, growth rates, seasonal patterns, forecast implications.

### Outlier Detection
```
"Find unusual sales patterns in Q4 2024"
```
Returns: Detected anomalies, statistical significance, potential causes, recommended actions.

### Key Driver Analysis
```
"What's driving the revenue variance in Q1?"
```
Returns: Top drivers with impact scores, business interpretation, action plan.
