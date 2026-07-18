# InvestmentOS Development Standards

## 1. Purpose

This document defines the engineering standards, coding practices, repository conventions, and AI development guidelines for InvestmentOS. It ensures consistency, maintainability, and high-quality software across all components.
## 2. Development Principles

- Build capabilities before optimization.
- Business logic must remain deterministic.
- AI is used for reasoning, never core calculations.
- Every feature must be testable.
- Reuse existing engines before creating new ones.
- Keep components loosely coupled.
## 3. Repository Standards

- One responsibility per folder.
- One responsibility per engine.
- Keep documentation under /docs.
- Keep reusable business logic under /engines.
- Keep user-facing capabilities under /skills.
- Keep reusable prompts/templates under /templates.
## 4. Engine Development Rules

Every engine must:

- Have a single responsibility.
- Accept well-defined inputs.
- Return structured outputs.
- Be independently testable.
- Avoid direct dependencies on AI models.
## 5. AI Development Rules

AI must:

- Explain decisions.
- Summarize evidence.
- Challenge assumptions.
- Produce structured outputs.

AI must never:

- Invent financial data.
- Override deterministic scores.
- Ignore validation failures.
## 6. Testing Standards

Every feature must include:

- Unit Tests
- Integration Tests
- AI Output Validation
- Decision Consistency Tests
## 7. Git Standards

- One feature per branch.
- One logical change per commit.
- Pull Requests require review.
- Update documentation with architectural changes.
## 8. Definition of Done

A feature is complete only when:

- Requirements are implemented.
- Tests pass.
- Documentation is updated.
- No critical defects remain.
- Code review is completed.