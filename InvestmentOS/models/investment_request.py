from typing import Optional

from pydantic import BaseModel, ConfigDict, Field


class InvestmentRequest(BaseModel):
    """
    Represents a user investment analysis request.
    This is the entry point for every InvestmentOS workflow.
    """

    model_config = ConfigDict(extra="forbid")

    symbol: str = Field(..., description="Stock symbol")
    exchange: str = Field(default="NSE", description="Stock exchange")
    strategy: str = Field(..., description="Investment strategy")
    portfolio_id: Optional[str] = Field(
        default=None,
        description="Optional portfolio identifier"
    )
    