
from engines.validation_engine import ValidationEngine
from models.analysis_context import AnalysisContext
from models.investment_request import InvestmentRequest


def test_validation():

    engine = ValidationEngine()

    request = InvestmentRequest(
        symbol="TEST",
        exchange="NSE",
        strategy="LONG_TERM",
    )

    context = AnalysisContext(request=request)

    context.evidence = {
        "success": True,
        "error": None,
        "company": {},
        "financials": {},
        "balance_sheet": {},
        "cashflow": {},
        "income_statement": {},
        "price_history": {},
        "news": {},
    }

    result = engine.validate(context)

    assert result["status"] == "PASS"