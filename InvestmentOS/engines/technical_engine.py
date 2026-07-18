import pandas as pd

from models.technical_score import TechnicalScore


class TechnicalEngine:
    """
    Performs technical analysis from historical prices.
    """

    def calculate(self, context):

        history = context.evidence["price_history"]

        score = TechnicalScore()

        if history is None or history.empty:
            return score

        close = history["Close"]

        score.current_price = round(close.iloc[-1], 2)
        score.sma20 = round(close.rolling(20).mean().iloc[-1], 2)
        score.sma50 = round(close.rolling(50).mean().iloc[-1], 2)
        score.sma200 = round(close.rolling(200).mean().iloc[-1], 2)

        delta = close.diff()

        gain = delta.clip(lower=0)
        loss = -delta.clip(upper=0)

        avg_gain = gain.rolling(14).mean()
        avg_loss = loss.rolling(14).mean()

        rs = avg_gain / avg_loss

        score.rsi = round(
            (100 - (100 / (1 + rs))).iloc[-1],
            2,
        )

        overall = 50

        # ---------------------------------------
        # Trend (40 Marks)
        # ---------------------------------------

        if (
            score.current_price > score.sma20 >
            score.sma50 >
            score.sma200
        ):
            score.trend = "STRONG BULLISH"
            overall += 40

        elif (
            score.current_price > score.sma50 and
            score.current_price > score.sma200
        ):
            score.trend = "BULLISH"
            overall += 30

        elif score.current_price > score.sma200:
            score.trend = "NEUTRAL"
            overall += 15

        else:
            score.trend = "BEARISH"
            overall -= 20

        # ---------------------------------------
        # RSI (30 Marks)
        # ---------------------------------------

        if 45 <= score.rsi <= 65:
            overall += 30

        elif 35 <= score.rsi < 45:
            overall += 20

        elif 65 < score.rsi <= 75:
            overall += 15

        elif score.rsi < 30:
            overall += 10

        else:
            overall += 0

        # ---------------------------------------
        # Momentum (20 Marks)
        # ---------------------------------------

        momentum = (
            (score.current_price - score.sma50)
            / score.sma50
        ) * 100

        if momentum >= 10:
            overall += 20
        elif momentum >= 5:
            overall += 15
        elif momentum >= 0:
            overall += 10
        elif momentum >= -5:
            overall += 5

        # ---------------------------------------
        # Price vs 200 SMA (10 Marks)
        # ---------------------------------------

        if score.current_price > score.sma200:
            overall += 10

        score.overall = max(0, min(100, round(overall)))

        return score