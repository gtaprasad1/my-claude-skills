# InvestmentOS Decision Framework

## Purpose

The Decision Framework defines the standard process InvestmentOS follows to evaluate every investment opportunity. It ensures every recommendation is based on structured evidence, deterministic scoring, risk assessment, and explainable AI reasoning rather than model opinions.

This framework is the foundation for all investment strategies, including Long-term Investing, BTST, STBT, Swing Trading, Positional Trading, Portfolio Analysis, and future capabilities.

## Design Principles
- Evidence before opinion
- Deterministic scoring before AI reasoning
- Explain every recommendation
- AI assists decision-making; it does not replace business logic
- Risk assessment is mandatory
- Recommendations must consider portfolio context
- Every decision must be repeatable and auditable

## Decision Workflow
1. Receive User Request
2. Collect Required Evidence
3. Validate Data Quality
4. Analyze Evidence
5. Calculate Scores
6. Assess Risks
7. Evaluate Portfolio Impact
8. Generate Recommendation
9. Challenge Recommendation (Devil's Advocate)
10. Produce Final Decision Card 

## Evidence Collection
### Mandatory Evidence

- Company Fundamentals
- Financial Statements
- Valuation Metrics
- Technical Indicators
- Market Trend
- News & Sentiment
- Corporate Actions
- Sector Performance
- Macro Economic Factors
- User Portfolio (if applicable)

### Evidence Rules

- Use trusted and verifiable data sources.
- Validate data freshness before analysis.
- Flag missing or incomplete evidence.
- Never infer unavailable data.

## Validation
### Validation Rules

- Verify all mandatory evidence is available.
- Check data freshness before analysis.
- Detect conflicting or inconsistent data.
- Identify missing critical information.
- Flag low-confidence evidence.
- Halt analysis if essential data is unavailable.

### Validation Outcome

- PASS – Analysis can continue.
- WARNING – Proceed with reduced confidence.
- FAIL – Stop analysis and inform the user.

## Scoring
### Scoring Principles

- Use objective and measurable criteria.
- Assign scores to each evidence category.
- Apply strategy-specific weightages.
- Calculate an overall investment score.
- Record the reason behind every score.
- AI may explain scores but cannot modify them.

### Scoring Outcome

- Overall Score (0–100)
- Confidence Level
- Supporting Evidence

## Risk Assessment
### Risk Categories

- Financial Risk
- Business Risk
- Technical Risk
- Market Risk
- Sector Risk
- Liquidity Risk
- Event Risk

### Risk Principles

- Identify all applicable risks.
- Assess risk severity.
- Highlight critical risks.
- Include risk in the final recommendation.
## Portfolio Impact
### Portfolio Checks

- Diversification
- Sector Exposure
- Position Size
- Risk Concentration
- Cash Availability

### Portfolio Principles

- Avoid excessive concentration.
- Consider existing holdings.
- Evaluate impact before recommending.
## Devil's Advocate Review
### Challenge Questions

- What could invalidate this recommendation?
- What evidence contradicts the analysis?
- What risks may have been underestimated?
- What assumptions require verification?

### Outcome

- Confirm Recommendation
- Revise Recommendation
- Reject Recommendation
## Final Recommendation
### Recommendation Types

- Strong Buy
- Buy
- Hold
- Reduce
- Sell
- Strong Sell

### Recommendation Principles

- Base recommendations on evidence and scores.
- Explain key drivers.
- Clearly communicate confidence.
## Decision Card
### Decision Card Includes

- Recommendation
- Overall Score
- Confidence Level
- Key Strengths
- Key Risks
- Portfolio Impact
- Supporting Evidence
- Devil's Advocate Summary
- Next Actions