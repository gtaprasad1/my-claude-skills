from math import sqrt

from config.valuation_profiles import VALUATION_PROFILES
from models.valuation_score import ValuationScore


class ValuationEngine:
    """
    Performs valuation analysis.
    """

    def calculate(self, context):

        score = ValuationScore()

        company = context.evidence.get("company", {})

        score.current_price = company.get("currentPrice", 0.0) or 0.0
        score.market_cap = company.get("marketCap", 0.0) or 0.0

        score.pe = company.get("trailingPE", 0.0) or 0.0
        score.pb = company.get("priceToBook", 0.0) or 0.0
        score.peg = company.get("pegRatio", 0.0) or 0.0
        score.ev_ebitda = company.get("enterpriseToEbitda", 0.0) or 0.0

        score.eps = company.get("trailingEps", 0.0) or 0.0
        score.book_value = company.get("bookValue", 0.0) or 0.0

        # Graham Intrinsic Value
        if score.eps > 0 and score.book_value > 0:
            score.intrinsic_value = round(
                sqrt(22.5 * score.eps * score.book_value),
                2
            )

            if score.intrinsic_value > 0:
                score.margin_of_safety = round(
                    (
                        (score.intrinsic_value - score.current_price)
                        / score.intrinsic_value
                    ) * 100,
                    2
                )

        sector = company.get("sector", "")
        profile = VALUATION_PROFILES.get(
            sector,
            VALUATION_PROFILES["default"]
        )

        overall = 100

        if score.pe > profile["pe"]["expensive"]:
            overall -= 30
        elif score.pe > profile["pe"]["average"]:
            overall -= 20
        elif score.pe > profile["pe"]["good"]:
            overall -= 10

        if score.pb > profile["pb"]["expensive"]:
            overall -= 20
        elif score.pb > profile["pb"]["average"]:
            overall -= 10

        if score.peg > profile["peg"]["expensive"]:
            overall -= 20
        elif score.peg > profile["peg"]["average"]:
            overall -= 10

        if score.ev_ebitda > profile["ev_ebitda"]["expensive"]:
            overall -= 20
        elif score.ev_ebitda > profile["ev_ebitda"]["average"]:
            overall -= 10

        score.overall = max(overall, 0)

        if score.overall >= 80:
            score.relative_rating = "ATTRACTIVE"
            score.relative_score = 100
        elif score.overall >= 60:
            score.relative_rating = "FAIR"
            score.relative_score = 70
        elif score.overall >= 40:
            score.relative_rating = "EXPENSIVE"
            score.relative_score = 40
        else:
            score.relative_rating = "VERY EXPENSIVE"
            score.relative_score = 10

        if score.margin_of_safety >= 40:
            score.rating = "UNDERVALUED"
            score.intrinsic_rating = "UNDERVALUED"
        elif score.margin_of_safety >= 20:
            score.rating = "FAIR"
            score.intrinsic_rating = "FAIR"
        elif score.margin_of_safety >= 0:
            score.rating = "FULLY VALUED"
            score.intrinsic_rating = "FULLY VALUED"
        else:
            score.rating = "OVERVALUED"
            score.intrinsic_rating = "OVERVALUED"
            score.intrinsic_warning = "Trading above intrinsic value"

        return score