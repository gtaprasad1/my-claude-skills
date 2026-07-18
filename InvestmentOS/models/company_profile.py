from pydantic import BaseModel


class CompanyProfile(BaseModel):

    name: str = ""
    symbol: str = ""
    sector: str = ""
    industry: str = ""
    market_cap: int = 0