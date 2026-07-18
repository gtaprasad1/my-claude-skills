
from abc import ABC, abstractmethod


class MarketDataProvider(ABC):

    @abstractmethod
    def get_company_profile(self, symbol: str):
        pass

    @abstractmethod
    def get_financials(self, symbol: str):
        pass

    @abstractmethod
    def get_balance_sheet(self, symbol: str):
        pass

    @abstractmethod
    def get_cashflow(self, symbol: str):
        pass

    @abstractmethod
    def get_income_statement(self, symbol: str):
        pass

    @abstractmethod
    def get_price_history(self, symbol: str):
        pass

    @abstractmethod
    def get_news(self, symbol: str):
        pass