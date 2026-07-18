from engines.evidence_engine import EvidenceEngine
from engines.technical_engine import TechnicalEngine
from models.analysis_context import AnalysisContext
from models.investment_request import InvestmentRequest


def test_technical_engine():

    request = InvestmentRequest(
        symbol="TCS.NS",
        strategy="LONG_TERM",
    )

    context = AnalysisContext(request=request)

    context.evidence = EvidenceEngine().collect(context)

    engine = TechnicalEngine()

    score = engine.calculate(context)

    assert score is not None
    assert score.current_price > 0