from engines.financial_engine import FinancialEngine
from engines.evidence_engine import EvidenceEngine
from models.analysis_context import AnalysisContext
from models.investment_request import InvestmentRequest


def test_financial_engine():

    request = InvestmentRequest(
        symbol="TCS.NS",
        strategy="LONG_TERM"
    )

    context = AnalysisContext(request=request)

    evidence = EvidenceEngine().collect(context)

    context.evidence = evidence

    engine = FinancialEngine()

    score = engine.calculate(context)

    assert score is not None
    assert score.overall >= 0