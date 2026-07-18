# InvestmentOS Data Model

## 1. Purpose

The Data Model defines the core business entities used throughout InvestmentOS. It provides a common language for all engines, APIs, AI components, and user interfaces, ensuring consistency, reusability, and scalability.
## 2. Core Business Entities

InvestmentOS is built around the following entities:

- User
- Portfolio
- Watchlist
- Stock
- Investment Strategy
- Evidence
- Score
- Risk
- Recommendation
- Decision Card
- Investment Journal
- Market Event
## 3. User

Represents the investor using InvestmentOS.

Attributes:

- User ID
- Name
- Investment Profile
- Risk Appetite
- Preferred Strategies
- Portfolio
- Watchlists
## 4. Stock

Represents a listed company.

Attributes:

- Symbol
- Exchange
- Company Name
- Sector
- Industry
- Market Capitalization
- Current Price
- Financial Data
- Technical Data
## 5. Investment Strategy

Defines how a stock is evaluated.

Supported Strategies:

- Long-term
- Value
- Growth
- Swing
- BTST
- STBT
- Positional
## 6. Evidence

Represents validated information used for decision making.

Sources:

- Financial Statements
- Technical Indicators
- Valuation
- News
- Market Data
- Corporate Actions
- Economic Indicators
## 7. Score

Represents deterministic evaluation results.

Includes:

- Category Scores
- Overall Score
- Confidence
- Evidence Coverage
## 8. Risk

Represents identified investment risks.

Categories:

- Financial
- Business
- Technical
- Market
- Sector
- Liquidity
- Event
## 9. Recommendation

Represents the final investment decision.

Types:

- Strong Buy
- Buy
- Hold
- Reduce
- Sell
- Strong Sell
## 10. Decision Card

The final output presented to the user.

Includes:

- Recommendation
- Overall Score
- Confidence
- Key Evidence
- Risks
- Portfolio Impact
- AI Explanation
- Next Actions