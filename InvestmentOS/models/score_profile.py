from pydantic import BaseModel


class ScoreProfile(BaseModel):
    """
    Stores deterministic investment scores.
    """

    business: int = 0
    financial: int = 0
    technical: int = 0
    valuation: int = 0
    news: int = 0

    overall: int = 0    