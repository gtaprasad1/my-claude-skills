# Portfolio Engine Specification

## 1. Purpose

The Portfolio Engine evaluates how a new investment recommendation impacts the user's existing portfolio. It ensures recommendations align with diversification, allocation, risk tolerance, and investment objectives.
## 2. Responsibilities

- Analyze current portfolio
- Measure diversification
- Calculate sector exposure
- Evaluate concentration risk
- Recommend position sizing
- Assess cash availability
- Generate Portfolio Profile
## 3. Inputs

Mandatory

- Portfolio
- Recommendation
- Score Profile
- Risk Profile

Optional

- User Preferences
- Investment Limits
## 4. Outputs

Portfolio Profile

Contains

- Diversification Score
- Sector Exposure
- Position Size Recommendation
- Portfolio Risk
- Cash Position
- Allocation Recommendation
- Portfolio Impact Summary
Load Portfolio
      │
      ▼
Analyze Holdings
      │
      ▼
Check Diversification
      │
      ▼
Check Exposure
      │
      ▼
Calculate Position Size
      │
      ▼
Generate Portfolio Profile
## 6. Portfolio Rules

- Avoid excessive concentration.
- Respect user risk profile.
- Maintain diversification.
- Consider available cash.
- Do not exceed allocation limits.
## 7. Portfolio Checks

- Sector Allocation
- Market Cap Allocation
- Stock Concentration
- Geographic Exposure
- Cash Allocation
- Risk Distribution

## 8. Position Sizing

Factors

- Conviction Score
- Overall Risk
- Portfolio Risk
- Available Cash
- User Allocation Rules
## 9. Business Rules

- Portfolio rules override recommendations.
- High concentration generates warnings.
- Portfolio analysis never changes stock scores.
- Position size must be calculated deterministically.
## 10. Configuration

Configurable Items

- Maximum Position Size
- Maximum Sector Exposure
- Cash Threshold
- Diversification Rules
## 11. Error Handling

- Empty Portfolio
- Invalid Holdings
- Missing Prices
- Insufficient Cash
## 12. Logging

Log

- Portfolio Loaded
- Exposure Analysis
- Diversification Score
- Position Size
## 13. Metrics

Measure

- Diversification Score
- Concentration Index
- Cash Utilization
- Sector Distribution
## 14. Test Cases

- Empty Portfolio
- Concentrated Portfolio
- Diversified Portfolio
- Low Cash Balance
- High Risk Portfolio
## 15. Acceptance Criteria

The engine succeeds when:

- Portfolio is analyzed.
- Position size is calculated.
- Diversification is evaluated.
- Portfolio Profile is generated.