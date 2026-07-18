from models.company_profile import CompanyProfile


class CompanyEngine:

    def calculate(self, context):

        company = context.evidence["company"]

        profile = CompanyProfile()

        profile.symbol = context.request.symbol
        profile.name = company.get("longName", "")
        profile.sector = company.get("sector", "")
        profile.industry = company.get("industry", "")
        profile.market_cap = company.get("marketCap", 0)

        return profile