from models.financial_score import FinancialScore


class FinancialEngine:
    """
    Performs financial analysis from financial statements.
    """

    def calculate(self, context):

        score = FinancialScore()

        company = context.evidence.get("company", {})
        financials = context.evidence.get("financials")
        cashflow = context.evidence.get("cashflow")

        earned = 0
        possible = 0

        # -----------------------------
        # Revenue Growth
        # -----------------------------
        revenue_growth = company.get("revenueGrowth")

        if revenue_growth is not None:
            possible += 15

            score.revenue_growth = round(revenue_growth * 100, 2)

            if score.revenue_growth >= 15:
                score.revenue_growth_score = 15
            elif score.revenue_growth >= 10:
                score.revenue_growth_score = 10
            elif score.revenue_growth >= 5:
                score.revenue_growth_score = 5

            earned += score.revenue_growth_score

        # -----------------------------
        # ROE
        # -----------------------------
        roe = company.get("returnOnEquity")

        if roe is not None:
            score.roe = round(roe * 100, 2)

        elif financials is not None:
            try:
                net_income = financials.loc["Net Income"].iloc[0]
                equity = company.get("bookValue")
                shares = company.get("sharesOutstanding")

                if equity and shares:
                    total_equity = equity * shares
                    score.roe = round((net_income / total_equity) * 100, 2)
            except Exception:
                pass

        if score.roe > 0:
            possible += 15

            if score.roe >= 20:
                score.roe_score = 15
            elif score.roe >= 15:
                score.roe_score = 12
            elif score.roe >= 10:
                score.roe_score = 8
            elif score.roe >= 8:
                score.roe_score = 5

            earned += score.roe_score

        # -----------------------------
        # Debt / Equity
        # -----------------------------
        debt = company.get("debtToEquity")

        if debt is not None:
            possible += 15

            score.debt_equity = round(debt, 2)

            if debt <= 30:
                score.debt_score = 15
            elif debt <= 60:
                score.debt_score = 10
            elif debt <= 100:
                score.debt_score = 5

            earned += score.debt_score

        # -----------------------------
        # Operating Margin
        # -----------------------------
        margin = company.get("operatingMargins")

        if margin is not None:
            possible += 15

            score.operating_margin = round(margin * 100, 2)

            if score.operating_margin >= 20:
                score.operating_margin_score = 15
            elif score.operating_margin >= 15:
                score.operating_margin_score = 12
            elif score.operating_margin >= 10:
                score.operating_margin_score = 8
            elif score.operating_margin >= 8:
                score.operating_margin_score = 5

            earned += score.operating_margin_score

        # -----------------------------
        # Net Margin
        # -----------------------------
        net_margin = company.get("profitMargins")

        if net_margin is not None:
            possible += 15

            score.net_margin = round(net_margin * 100, 2)

            if score.net_margin >= 15:
                score.net_margin_score = 15
            elif score.net_margin >= 10:
                score.net_margin_score = 10
            elif score.net_margin >= 5:
                score.net_margin_score = 5

            earned += score.net_margin_score

        # -----------------------------
        # Free Cash Flow
        # -----------------------------
        if cashflow is not None:
            try:
                fcf = cashflow.loc["Free Cash Flow"].iloc[0]

                score.free_cash_flow = round(fcf / 1_00_00_000, 2)

                possible += 10

                if fcf > 0:
                    score.free_cash_flow_score = 10

                earned += score.free_cash_flow_score

            except Exception:
                pass

        if possible == 0:
            score.overall = 50
        else:
            score.overall = round((earned / possible) * 100)

        return score