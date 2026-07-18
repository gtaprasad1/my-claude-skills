# Technology Decisions (Frozen)

## Programming Language

- Python 3.12

Reason:
- Excellent AI ecosystem
- Type hints
- FastAPI support
- Mature libraries

---

## API Framework

- FastAPI

Reason:
- High performance
- Automatic OpenAPI
- Native Pydantic support

---

## Data Models

- Pydantic V2

Reason:
- Validation
- Serialization
- Type safety

---

## AI Orchestration

- LangGraph

Reason:
- Multi-agent workflow
- State management
- Deterministic execution

---

## LLM Support

- Claude
- GPT
- Gemini

Requirement:
Provider-independent architecture.

---

## Database

V1

- SQLite

Future

- PostgreSQL

---

## ORM

- SQLModel

---

## Configuration

- YAML

---

## Testing

- Pytest

---

## Linting

- Ruff

---

## Formatting

- Black

---

## Dependency Management

- uv

---

## Logging

- Structlog

---

## Environment Variables

- .env

---

## Version Control

- Git

---

## Documentation

- Markdown

---

## Design Principles

- Clean Architecture
- SOLID
- Domain-Driven Design
- Configuration over hardcoding
- Dependency Injection
- Deterministic business logic