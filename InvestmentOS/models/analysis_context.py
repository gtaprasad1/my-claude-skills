from typing import Any

from pydantic import BaseModel, ConfigDict, Field

from models.company_profile import CompanyProfile
from models.decision_result import DecisionResult
from models.financial_score import FinancialScore
from models.investment_request import InvestmentRequest
from models.technical_score import TechnicalScore
from models.valuation_score import ValuationScore


class AnalysisContext(BaseModel):
    """
    Shared object passed through every InvestmentOS engine.
    """

    model_config = ConfigDict(arbitrary_types_allowed=True)

    # --------------------------------------------------
    # Request
    # --------------------------------------------------
    request: InvestmentRequest

    # --------------------------------------------------
    # Workflow
    # --------------------------------------------------
    evidence: Any | None = None
    validation: Any | None = None

    # --------------------------------------------------
    # Company
    # --------------------------------------------------
    company_profile: CompanyProfile | None = None

    # --------------------------------------------------
    # Analysis Engines
    # --------------------------------------------------
    financial_score: FinancialScore | None = None
    technical_score: TechnicalScore | None = None
    valuation_score: ValuationScore | None = None

    # --------------------------------------------------
    # Decision
    # --------------------------------------------------
    score: Any | None = None
    decision: DecisionResult | None = None
    risk: Any | None = None

    # --------------------------------------------------
    # Future Engines
    # --------------------------------------------------
    portfolio: Any | None = None
    ai_reasoning: Any | None = None

    # --------------------------------------------------
    # Output
    # --------------------------------------------------
    decision_card: Any | None = None

    # --------------------------------------------------
    # Metadata
    # --------------------------------------------------
    metadata: dict = Field(default_factory=dict)