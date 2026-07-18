
from engines.decision_engine import DecisionEngine
from models.investment_request import InvestmentRequest


def test_decision_engine():

    request = InvestmentRequest(
        symbol="TCS.NS",
        strategy="LONG_TERM",
    )

    engine = DecisionEngine()

    context = engine.analyze(request)

    assert context is not None

    assert context.evidence is not None

    assert context.validation["status"] == "PASS"

    assert context.financial_score is not None

    assert context.technical_score is not None

    assert context.score is not None

    assert context.score.overall >= 0
    assert context.score.overall <= 100

    assert context.risk is not None

    assert context.decision_card is not None