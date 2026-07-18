
from engines.evidence_engine import EvidenceEngine
from models.analysis_context import AnalysisContext
from models.investment_request import InvestmentRequest


def test_collect_evidence():

    request = InvestmentRequest(
        symbol="AMARAJABATTERY.NS",
        strategy="LONG_TERM",
    )

    context = AnalysisContext(request=request)

    engine = EvidenceEngine()

    evidence = engine.collect(context)

    assert evidence is not None
    assert "company" in evidence
    assert "financials" in evidence
    assert "price_history" in evidence
    assert "news" in evidence