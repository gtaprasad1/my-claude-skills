# InvestmentOS Business Rules

## 1. Purpose

This document defines the deterministic business rules governing investment analysis, scoring, risk assessment, portfolio evaluation, and recommendation generation. These rules ensure consistent, auditable, and explainable decisions across all investment strategies.
## 2. General Rules

- Every analysis must follow the Decision Framework.
- All recommendations require validated evidence.
- AI cannot bypass business rules.
- Missing critical data prevents recommendations.
- Every recommendation must include confidence and supporting evidence.
## 3. Strategy Rules

Each investment strategy defines:

- Required evidence
- Scoring weightages
- Risk thresholds
- Recommendation criteria

Supported Strategies:

- Long-term
- Value
- Growth
- Swing
- BTST
- STBT
- Positional
## 4. Validation Rules

Validation checks include:

- Data completeness
- Data freshness
- Source reliability
- Mandatory metrics availability
- Consistency across sources
## 5. Recommendation Rules

Recommendations require:

- Successful validation
- Completed scoring
- Risk assessment
- Portfolio assessment (if applicable)
- Devil's Advocate review
## 6. Override Rules

Recommendations are blocked when:

- Critical evidence is missing.
- Validation fails.
- Risk exceeds configured limits.
- User-defined investment rules prohibit execution.
## 7. Audit Rules

Every analysis must record:

- Input request
- Evidence used
- Scores
- Risks
- Final recommendation
- AI explanation
- Timestamp