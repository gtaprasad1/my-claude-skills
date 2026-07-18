from pydantic import BaseModel


class TechnicalScore(BaseModel):
    """
    Stores technical analysis metrics.
    """

    current_price: float = 0.0

    sma20: float = 0.0
    sma50: float = 0.0
    sma200: float = 0.0

    rsi: float = 0.0

    trend: str = "UNKNOWN"

    overall: int = 0