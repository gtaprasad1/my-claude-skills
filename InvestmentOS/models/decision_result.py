from dataclasses import dataclass, field


@dataclass
class DecisionResult:
    recommendation: str
    risk: str
    confidence: str
    reasons: list[str] = field(default_factory=list)