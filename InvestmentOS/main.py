
from engines.decision_engine import DecisionEngine
from models.investment_request import InvestmentRequest


def main():

    print("=" * 60)
    print("InvestmentOS Analysis")
    print("=" * 60)

    symbol = input("Enter Stock Symbol (e.g. TCS.NS): ").strip()

    if not symbol:
        print("Stock symbol cannot be empty.")
        return

    strategy = input("Enter Strategy [Default: LONG_TERM]: ").strip()

    if not strategy:
        strategy = "LONG_TERM"

    request = InvestmentRequest(
        symbol=symbol,
        strategy=strategy,
    )

    engine = DecisionEngine()

    context = engine.analyze(request)

    if context.validation["status"] != "PASS":
        print("\nAnalysis Failed")
        print(context.validation["message"])
        return

    financial = context.financial_score
    technical = context.technical_score
    valuation = context.valuation_score
    card = context.decision_card

    print("\n")
    print("=" * 60)
    print("Company")
    print("-" * 60)
    print(f"Symbol               : {card.symbol}")
    print(f"Strategy             : {card.strategy}")

    print("\nFinancial Analysis")
    print("-" * 60)
    print(f"Revenue Growth (%)   : {financial.revenue_growth:.2f}")
    print(f"ROE (%)              : {financial.roe:.2f}")
    print(f"Debt / Equity        : {financial.debt_equity:.2f}")
    print(f"Operating Margin (%) : {financial.operating_margin:.2f}")
    print(f"Net Margin (%)       : {financial.net_margin:.2f}")
    print(f"Free Cash Flow (Cr)  : {financial.free_cash_flow:.2f}")
    print(f"Financial Score      : {financial.overall}")

    print("\nTechnical Analysis")
    print("-" * 60)
    print(f"Current Price        : {technical.current_price:.2f}")
    print(f"20 SMA               : {technical.sma20:.2f}")
    print(f"50 SMA               : {technical.sma50:.2f}")
    print(f"200 SMA              : {technical.sma200:.2f}")
    print(f"RSI                  : {technical.rsi:.2f}")
    print(f"Trend                : {technical.trend}")
    print(f"Technical Score      : {technical.overall}")

    print("\nValuation Analysis")
    print("-" * 60)
    print(f"PE Ratio             : {valuation.pe:.2f}")
    print(f"PB Ratio             : {valuation.pb:.2f}")
    print(f"PEG Ratio            : {valuation.peg:.2f}")
    print(f"EV / EBITDA          : {valuation.ev_ebitda:.2f}")
    print(f"Intrinsic Value      : {valuation.intrinsic_value:.2f}")
    print(f"Margin of Safety (%) : {valuation.margin_of_safety:.2f}")
    print(f"Valuation Rating     : {valuation.rating}")
    print(f"Valuation Score      : {valuation.overall}")

    print("\nOverall")
    print("-" * 60)
    print(f"Overall Score        : {card.score}")
    print(f"Risk                 : {card.risk}")
    print(f"Confidence           : {card.confidence}")
    print(f"Recommendation       : {card.recommendation}")

    print("=" * 60)


if __name__ == "__main__":
    main()