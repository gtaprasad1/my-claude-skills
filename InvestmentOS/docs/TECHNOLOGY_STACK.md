# InvestmentOS Technology Stack

## 1. Purpose

This document defines the approved technology stack for InvestmentOS. It establishes the technologies, frameworks, libraries, and tools used to build, deploy, and maintain the platform.
## 2. Technology Principles

- Open standards where possible.
- AI-model agnostic.
- Cloud portable.
- Modular architecture.
- Python-first development.
- API-first design.
- Containerized deployment.
## 3. Programming Languages

Backend
- Python 3.13+

Frontend
- React
- TypeScript

Scripting
- Python
## 4. Backend Framework

Framework
- FastAPI

Reasons

- High performance
- Automatic API documentation
- Async support
- Excellent AI ecosystem
## 5. Frontend

Framework
- React

Language
- TypeScript

UI
- Tailwind CSS

Charts
- Recharts
## 6. AI Framework

Primary

- Direct LLM APIs

Future

- LangGraph
- MCP
- CrewAI (evaluation only)

Do not introduce orchestration frameworks until they provide measurable value.
## 7. Database

Application Database

- PostgreSQL

Caching

- Redis

Vector Database (Future)

- pgvector

Object Storage

- Local
## 8. AI Providers

Supported

- Claude
- GPT
- Gemini

Architecture

AI Provider Abstraction Layer
## 9. Market Data

Version 1

- Yahoo Finance

Future

- Polygon
- Alpha Vantage
- NSE APIs
## 10. Testing

Backend

- pytest

API

- FastAPI TestClient

Frontend

- Playwright

Performance

- Locust
## 11. Deployment

Container

- Docker

Future

- Kubernetes

Reverse Proxy

- Nginx
## 12. CI/CD

Repository

- GitHub

Automation

- GitHub Actions

Quality

- Ruff
- Black
- MyPy
## 13. Development Tools

IDE

- VS Code

AI Development

- Claude Code

Version Control

- Git

Documentation

- Markdown
## 14. Observability

Logging

- Loguru

Metrics

- Prometheus

Dashboards

- Grafana
## 15. Future Technologies

- LangGraph
- MCP
- Knowledge Graph
- Hybrid RAG
- Event-driven Architecture
- Streaming Analytics