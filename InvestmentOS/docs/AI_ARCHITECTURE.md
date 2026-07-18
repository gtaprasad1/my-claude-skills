# InvestmentOS AI Architecture

## 1. Purpose

This document defines the AI architecture of InvestmentOS. It describes how AI models interact with deterministic business engines to provide explainable, reliable, and model-agnostic investment recommendations.
## 2. AI Design Principles

- AI explains; it does not decide.
- AI operates only on validated evidence.
- Business logic remains deterministic.
- AI models must be interchangeable.
- AI outputs must be structured and explainable.
- Every AI response must be auditable.
## 3. AI Responsibilities

AI is responsible for:

- Explaining investment decisions
- Summarizing evidence
- Identifying contradictions
- Answering user questions
- Generating investment reports
- Producing structured outputs
## 4. AI Limitations

AI must never:

- Calculate deterministic scores
- Override validation failures
- Ignore business rules
- Modify risk assessments
- Fabricate financial information
## 5. AI Processing Flow

Validated Evidence
        │
        ▼
Business Engines
        │
        ▼
AI Reasoning
        │
        ▼
Devil's Advocate
        │
        ▼
Decision Card
## 6. Model Abstraction

Supported Models:

- Claude
- GPT
- Gemini
- Future Models

All models communicate through a common AI abstraction layer.
## 7. Prompt Strategy

Prompts must:

- Use structured evidence
- Request structured outputs
- Avoid free-form reasoning
- Include confidence context
- Require evidence-backed explanations
## 8. Structured Outputs

AI responses should include:

- Executive Summary
- Key Findings
- Supporting Evidence
- Risks
- Confidence
- Recommendation Explanation
- Next Actions
## 9. Tool Calling

AI may invoke:

- Evidence Engine
- Financial Analysis
- Technical Analysis
- News Analysis
- Portfolio Analysis
- Report Generation

AI never accesses external systems directly.
## 10. Memory Strategy

Supported memory types:

- Session Memory
- Portfolio Context
- Watchlist Context
- Investment Journal
- Historical Decisions

Memory provides context but never alters deterministic calculations.
## 11. Future AI Roadmap

Future enhancements:

- Multi-agent collaboration
- LangGraph orchestration
- MCP integration
- Hybrid RAG
- Knowledge Graph
- AI self-evaluation
- Continuous learning