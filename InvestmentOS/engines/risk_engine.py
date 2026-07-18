from models.risk_profile import RiskProfile


class RiskEngine:
    """
    Risk assessment based on the centralized decision result.
    """

    def assess(self, context):

        decision = context.decision

        risk = RiskProfile()

        risk.overall = decision.risk
        risk.confidence = decision.confidence
        risk.reasons = decision.reasons

        risk.financial_risk = (
            "LOW"
            if context.financial_score.overall >= 70
            else "HIGH"
        )

        risk.technical_risk = (
            "LOW"
            if context.technical_score.overall >= 70
            else "HIGH"
        )

        risk.valuation_risk = (
            "LOW"
            if context.valuation_score.overall >= 70
            else "HIGH"
        )

        risk.score = (
            context.financial_score.overall
            + context.technical_score.overall
            + context.valuation_score.overall
        ) // 3

        return risk