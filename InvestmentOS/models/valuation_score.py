from pydantic import BaseModel


class ValuationScore(BaseModel):
    """
    Stores valuation analysis.
    """

    # --------------------------------------------------
    # Market
    # --------------------------------------------------
    current_price: float = 0.0
    market_cap: float = 0.0

    # --------------------------------------------------
    # Relative Valuation Metrics
    # --------------------------------------------------
    pe: float = 0.0
    pb: float = 0.0
    peg: float = 0.0
    ev_ebitda: float = 0.0

    # --------------------------------------------------
    # Intrinsic Valuation
    # --------------------------------------------------
    eps: float = 0.0
    book_value: float = 0.0
    intrinsic_value: float = 0.0
    margin_of_safety: float = 0.0

    # --------------------------------------------------
    # Relative Valuation
    # --------------------------------------------------
    relative_rating: str = ""
    relative_score: int = 0

    # --------------------------------------------------
    # Intrinsic Valuation
    # --------------------------------------------------
    intrinsic_rating: str = ""
    intrinsic_warning: str = ""

    # --------------------------------------------------
    # Backward Compatibility (MVP)
    # --------------------------------------------------
    rating: str = ""
    overall: int = 0

    # --------------------------------------------------
    # Risk
    # --------------------------------------------------
    valuation_risk: str = ""

    # --------------------------------------------------
    # Future
    # --------------------------------------------------
    dcf_value: float = 0.0
    fair_value: float = 0.0