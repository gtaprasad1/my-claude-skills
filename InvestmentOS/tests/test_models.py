
from models.analysis_context import AnalysisContext
from models.investment_request import InvestmentRequest


def test_investment_request():
    request = InvestmentRequest(
        symbol="AMARAJABATTERY",
        strategy="LONG_TERM",
    )

    assert request.symbol == "AMARAJABATTERY"
    assert request.exchange == "NSE"
    assert request.strategy == "LONG_TERM"
    assert request.portfolio_id is None


def test_analysis_context():
    request = InvestmentRequest(
        symbol="AMARAJABATTERY",
        strategy="LONG_TERM",
    )

    context = AnalysisContext(request=request)

    assert context.request.symbol == "AMARAJABATTERY"
    assert context.evidence is None
    assert context.validation is None
    assert context.score is None
    assert context.risk is None
    assert context.portfolio is None
    assert context.ai_reasoning is None
    assert context.decision_card is None