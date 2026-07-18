from models.decision_result import DecisionResult


class DecisionRulesEngine:
    """
    Final Investment Committee.

    Decision Priority

    1. Financial Quality
    2. Valuation
    3. Technical Timing

    Technicals should improve or reduce conviction,
    not completely reject a fundamentally strong company.
    """

    def evaluate(self, context):

        financial = context.financial_score.overall
        technical = context.technical_score.overall
        valuation = context.valuation_score.overall
        rsi = context.technical_score.rsi

        result = DecisionResult(
            recommendation="HOLD",
            risk="MEDIUM",
            confidence="MEDIUM",
            reasons=[]
        )

        # --------------------------------------------------
        # Fatal Financial Weakness
        # --------------------------------------------------

        if financial < 40:
            result.recommendation = "SELL"
            result.risk = "HIGH"
            result.confidence = "HIGH"
            result.reasons.append("Weak financial fundamentals")
            return result

        # --------------------------------------------------
        # Overall Decision Score
        # --------------------------------------------------

        decision_score = (
            financial * 0.50 +
            valuation * 0.30 +
            technical * 0.20
        )

        # --------------------------------------------------
        # BUY
        # --------------------------------------------------

        if (
            decision_score >= 80
            and financial >= 80
            and valuation >= 70
        ):

            result.recommendation = "BUY"
            result.risk = "LOW"
            result.confidence = "HIGH"

            result.reasons.append("Strong financial quality")
            result.reasons.append("Attractive valuation")

            if technical >= 60:
                result.reasons.append("Healthy technical trend")
            else:
                result.reasons.append("Suitable for long-term accumulation")

            if rsi >= 75:
                result.risk = "MEDIUM"
                result.reasons.append("Short-term overbought")

            return result

        # --------------------------------------------------
        # BUY WITH CAUTION
        # --------------------------------------------------

        if (
            decision_score >= 70
            and financial >= 65
        ):

            result.recommendation = "BUY WITH CAUTION"
            result.risk = "MEDIUM"
            result.confidence = "HIGH"

            if valuation >= 70:
                result.reasons.append("Strong business fundamentals")
            else:
                result.reasons.append("Business quality is good")
                result.reasons.append("Valuation requires attention")

            if technical < 50:
                result.reasons.append("Wait for a better entry")

            if rsi >= 70:
                result.reasons.append("RSI indicates overbought conditions")

            return result

        # --------------------------------------------------
        # HOLD
        # --------------------------------------------------

        if decision_score >= 55:

            result.recommendation = "HOLD"
            result.risk = "MEDIUM"
            result.confidence = "MEDIUM"

            if valuation < 50:
                result.reasons.append("Valuation is stretched")

            if technical < 50:
                result.reasons.append("Weak short-term trend")

            if financial < 60:
                result.reasons.append("Financial quality needs monitoring")

            if not result.reasons:
                result.reasons.append("Balanced investment profile")

            return result

        # --------------------------------------------------
        # SELL
        # --------------------------------------------------

        result.recommendation = "SELL"
        result.risk = "HIGH"
        result.confidence = "HIGH"

        if valuation < 40:
            result.reasons.append("Significantly overvalued")

        if technical < 40:
            result.reasons.append("Weak technical trend")

        result.reasons.append("Investment quality below threshold")

        return result