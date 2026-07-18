from engines.decision_engine import DecisionEngine
from models.investment_request import InvestmentRequest


SYMBOLS = [
    "TCS.NS",
    "INFY.NS",
    "RELIANCE.NS",
    "HDFCBANK.NS",
    "ICICIBANK.NS",
    "SBIN.NS",
    "ITC.NS",
    "LT.NS",
    "ASIANPAINT.NS",
    "CUPID.NS",
]


def run():

    engine = DecisionEngine()

    print("=" * 120)
    print(
        f"{'SYMBOL':<15}"
        f"{'FIN':>6}"
        f"{'TECH':>8}"
        f"{'VAL':>8}"
        f"{'TOTAL':>8}"
        f"{'RECOMMENDATION':>22}"
        f"{'RISK':>10}"
        f"{'CONF':>10}"
    )
    print("=" * 120)

    for symbol in SYMBOLS:

        request = InvestmentRequest(
            symbol=symbol,
            strategy="LONG_TERM",
        )

        try:

            context = engine.analyze(request)

            if context.validation["status"] != "PASS":
                print(f"{symbol:<15}FAILED - {context.validation['message']}")
                continue

            print(
                f"{symbol:<15}"
                f"{context.financial_score.overall:>6}"
                f"{context.technical_score.overall:>8}"
                f"{context.valuation_score.overall:>8}"
                f"{context.score.overall:>8}"
                f"{context.decision_card.recommendation:>22}"
                f"{context.decision_card.risk:>10}"
                f"{context.decision_card.confidence:>10}"
            )

        except Exception as ex:
            print(f"{symbol:<15}ERROR - {ex}")

    print("=" * 120)


if __name__ == "__main__":
    run()