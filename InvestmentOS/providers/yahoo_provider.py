
import yfinance as yf

from providers.market_data_provider import MarketDataProvider


class YahooFinanceProvider(MarketDataProvider):
    """
    Yahoo Finance implementation of the MarketDataProvider.
    """

    def __init__(self):
        pass

    def _ticker(self, symbol: str):
        return yf.Ticker(symbol)

    def get_company_profile(self, symbol: str):
        ticker = self._ticker(symbol)
        return ticker.info

    def get_financials(self, symbol: str):
        ticker = self._ticker(symbol)
        return ticker.financials

    def get_balance_sheet(self, symbol: str):
        ticker = self._ticker(symbol)
        return ticker.balance_sheet

    def get_cashflow(self, symbol: str):
        ticker = self._ticker(symbol)
        return ticker.cashflow

    def get_income_statement(self, symbol: str):
        ticker = self._ticker(symbol)
        return ticker.financials

    def get_price_history(self, symbol: str):
        ticker = self._ticker(symbol)
        return ticker.history(period="5y")

    def get_news(self, symbol: str):
        ticker = self._ticker(symbol)
        return ticker.news