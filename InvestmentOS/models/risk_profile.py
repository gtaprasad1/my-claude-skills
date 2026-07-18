
from pydantic import BaseModel, Field


class RiskProfile(BaseModel):
    """
    Stores investment risk assessment.
    """

    overall: str = "LOW"
    confidence: str = "HIGH"

    financial_risk: str = ""
    technical_risk: str = ""
    valuation_risk: str = ""

    score: int = 0

    reasons: list[str] = Field(default_factory=list)