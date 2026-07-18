# Decision Card UI Specification

## Purpose

Defines the user interface, layout, visual hierarchy, interaction model, and presentation standards for the InvestmentOS Decision Card.

The Decision Card is the primary output of InvestmentOS. It must present deterministic investment analysis in a concise, explainable, and actionable format.

---

# Design Principles

- One-screen executive summary
- Evidence before opinion
- Explainability first
- Minimal cognitive load
- Progressive disclosure
- Mobile friendly
- Professional institutional appearance
- Consistent visual language

---

# Layout

```
========================================================

Company

Recommendation

Investment Score

Confidence

Current Price

Investment Horizon

========================================================

Executive Summary

--------------------------------------------------------

Investment Decision

Why

Top Strengths

Top Risks

========================================================

Overall Score

Business

Financial

Growth

Valuation

Technical

Risk

Portfolio Fit

========================================================

Evidence Coverage

Business

Financial

Valuation

Technical

News

Macro

Portfolio

========================================================

Business Analysis

========================================================

Financial Analysis

========================================================

Valuation Analysis

========================================================

Technical Analysis

========================================================

Risk Analysis

========================================================

Portfolio Analysis

========================================================

Devil's Advocate

========================================================

Final Recommendation

========================================================

Suggested Actions

========================================================
```

---

# Header

Display

- Company Name
- Symbol
- Exchange
- Analysis Date
- Current Price
- Investment Strategy
- Investment Horizon

---

# Executive Summary

Must include

- Recommendation
- Overall Score
- Confidence
- Why
- Key Strengths
- Key Risks

Maximum 10 lines.

---

# Score Section

Display

Overall Score

Business Score

Financial Score

Growth Score

Valuation Score

Technical Score

Risk Score

Portfolio Score

Each score should display

- Numeric Score
- Weight
- Confidence
- Expand button

---

# Evidence Coverage

Display

Business

Financial

Valuation

Technical

News

Macro

Portfolio

Each category shows

- Coverage %
- Status
- Missing Evidence

---

# Risk Section

Display

Business Risk

Financial Risk

Execution Risk

Market Risk

Valuation Risk

Governance Risk

Liquidity Risk

Overall Risk Rating

Display as heatmap.

---

# Portfolio Section

Display

Diversification

Sector Exposure

Suggested Position Size

Cash Requirement

Portfolio Impact

If portfolio unavailable

Display

Portfolio Analysis Skipped

---

# Devil's Advocate

Display

Contradicting Evidence

Missing Evidence

Hidden Risks

Worst Case Scenario

Events that invalidate recommendation

---

# Recommendation Section

Display

Recommendation

Investment Horizon

Expected Holding Period

Confidence

Overall Score

Risk Rating

---

# Suggested Actions

Possible Actions

- Buy
- Accumulate
- Hold
- Watch
- Reduce
- Exit

Display rationale for every action.

---

# Expandable Sections

Every section should support expansion.

Collapsed

Executive Summary only.

Expanded

Detailed evidence.

---

# Visual Indicators

Use

🟢 Strong

🟡 Moderate

🟠 Caution

🔴 Weak

---

# Confidence Indicator

Display

High

Medium

Low

Show reason for confidence.

---

# Evidence Traceability

Every important metric should include

- Source
- Collection Date
- Reliability

Users should always know where information originated.

---

# Missing Evidence

If evidence is unavailable

Display

Missing

Reason

Impact on confidence

Do not estimate values.

---

# User Experience Rules

Never overwhelm users.

Always show

Summary

↓

Expand Details

Avoid scrolling through long reports.

---

# Accessibility

Support

- Desktop
- Tablet
- Mobile
- Dark Theme
- Light Theme

---

# Future Enhancements

- Interactive Charts
- Portfolio Simulator
- Scenario Analysis
- AI Chat
- Historical Decisions
- Compare Multiple Stocks
- PDF Export
- Presentation Mode