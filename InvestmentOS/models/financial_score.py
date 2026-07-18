
from pydantic import BaseModel


class FinancialScore(BaseModel):
    """
    Stores detailed financial analysis results.
    """

    # ---------- Metrics ----------
    revenue_growth: float = 0.0
    eps_growth: float = 0.0
    roe: float = 0.0
    debt_equity: float = 0.0
    operating_margin: float = 0.0
    net_margin: float = 0.0
    free_cash_flow: float = 0.0

    # ---------- Scores ----------
    revenue_growth_score: int = 0
    eps_growth_score: int = 0
    roe_score: int = 0
    debt_score: int = 0
    operating_margin_score: int = 0
    net_margin_score: int = 0
    free_cash_flow_score: int = 0

    # ---------- Final ----------
    overall: int = 0