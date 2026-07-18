from models.decision_card import DecisionCard


class ReportEngine:
    """
    Generates the final InvestmentOS Decision Card.
    """

    def generate(self, context):

        decision = context.decision

        return DecisionCard(
            symbol=context.request.symbol,
            strategy=context.request.strategy,
            score=context.score.overall,
            risk=decision.risk,
            confidence=decision.confidence,
            recommendation=decision.recommendation,
        )