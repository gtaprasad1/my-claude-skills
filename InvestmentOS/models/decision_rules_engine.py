from models.decision_result import DecisionResult


class DecisionRulesEngine:
    """
    Single source of truth for:
    - Recommendation
    - Risk
    - Confidence
    """

    def evaluate(self, context):

        financial = context.financial_score.overall
        technical = context.technical_score.overall
        valuation = context.valuation_score.overall
        rsi = context.technical_score.rsi

        # --------------------------------------------------
        # Weak Fundamentals
        # --------------------------------------------------
        if financial < 40:
            return DecisionResult(
                recommendation="SELL",
                risk="HIGH",
                confidence="HIGH",
                reasons=["Weak financials"],
            )

        # --------------------------------------------------
        # Extremely Overvalued
        # --------------------------------------------------
        if valuation < 40:
            return DecisionResult(
                recommendation="HOLD",
                risk="HIGH",
                confidence="HIGH",
                reasons=["Stock appears significantly overvalued"],
            )

        # --------------------------------------------------
        # Overbought
        # --------------------------------------------------
        if rsi >= 70:
            return DecisionResult(
                recommendation="HOLD",
                risk="MEDIUM",
                confidence="MEDIUM",
                reasons=["RSI above 70"],
            )

        # --------------------------------------------------
        # Strong Business
        # --------------------------------------------------
        if (
            financial >= 70
            and technical >= 70
            and valuation >= 70
        ):
            return DecisionResult(
                recommendation="BUY",
                risk="LOW",
                confidence="HIGH",
                reasons=["Strong across all pillars"],
            )

        # --------------------------------------------------
        # Good company, acceptable but not ideal valuation
        # --------------------------------------------------
        if (
            financial >= 70
            and technical >= 70
        ):
            return DecisionResult(
                recommendation="BUY WITH CAUTION",
                risk="MEDIUM",
                confidence="MEDIUM",
                reasons=["Strong business but valuation is not attractive"],
            )

        return DecisionResult(
            recommendation="HOLD",
            risk="MEDIUM",
            confidence="MEDIUM",
            reasons=["No strong signal"],
        )