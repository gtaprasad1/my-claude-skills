from providers.yahoo_provider import YahooFinanceProvider


class EvidenceEngine:
    """
    Collects all evidence required for investment analysis.
    """

    def __init__(self):
        self.provider = YahooFinanceProvider()

    def collect(self, context):

        symbol = context.request.symbol

        evidence = {
            "success": True,
            "error": None,

            "company": None,

            "financials": None,
            "balance_sheet": None,
            "cashflow": None,
            "income_statement": None,

            "price_history": None,
            "news": None,
        }

        try:

            evidence["company"] = self.provider.get_company_profile(symbol)

            evidence["financials"] = self.provider.get_financials(symbol)

            evidence["balance_sheet"] = self.provider.get_balance_sheet(symbol)

            evidence["cashflow"] = self.provider.get_cashflow(symbol)

            evidence["income_statement"] = self.provider.get_income_statement(symbol)

            evidence["price_history"] = self.provider.get_price_history(symbol)

            evidence["news"] = self.provider.get_news(symbol)

            if not evidence["company"]:
                evidence["success"] = False
                evidence["error"] = "Invalid stock symbol."

        except Exception as ex:

            evidence["success"] = False
            evidence["error"] = str(ex)

        return evidence
