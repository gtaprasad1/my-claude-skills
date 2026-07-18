from models.score_profile import ScoreProfile


class ScoringEngine:
    """
    Combines all analysis engines into one overall score.
    """

    def calculate(self, context):

        score = ScoreProfile()

        financial = (
            context.financial_score.overall
            if context.financial_score
            else 0
        )

        technical = (
            context.technical_score.overall
            if context.technical_score
            else 0
        )

        valuation = (
            context.valuation_score.overall
            if context.valuation_score
            else 50
        )

        score.financial = financial
        score.technical = technical
        score.valuation = valuation

        score.overall = round(
            financial * 0.60 +
            technical * 0.30 +
            valuation * 0.10
        )

        return score