
from pydantic import BaseModel


class DecisionCard(BaseModel):
    symbol: str
    strategy: str
    score: int
    risk: str
    confidence: str
    recommendation: str