from models.analysis_context import AnalysisContext
from models.investment_request import InvestmentRequest

from engines.company_engine import CompanyEngine
from engines.decision_rules_engine import DecisionRulesEngine
from engines.evidence_engine import EvidenceEngine
from engines.financial_engine import FinancialEngine
from engines.report_engine import ReportEngine
from engines.risk_engine import RiskEngine
from engines.scoring_engine import ScoringEngine
from engines.technical_engine import TechnicalEngine
from engines.validation_engine import ValidationEngine
from engines.valuation_engine import ValuationEngine


class DecisionEngine:
    """
    InvestmentOS Workflow Orchestrator
    """

    def __init__(self):

        self.evidence_engine = EvidenceEngine()
        self.validation_engine = ValidationEngine()

        self.company_engine = CompanyEngine()

        self.financial_engine = FinancialEngine()
        self.technical_engine = TechnicalEngine()
        self.valuation_engine = ValuationEngine()

        self.scoring_engine = ScoringEngine()

        # Single Source of Truth
        self.decision_rules_engine = DecisionRulesEngine()

        self.risk_engine = RiskEngine()
        self.report_engine = ReportEngine()

    def analyze(self, request: InvestmentRequest):

        context = AnalysisContext(request=request)

        # --------------------------------------------------
        # Step 1 - Collect Evidence
        # --------------------------------------------------
        context.evidence = self.evidence_engine.collect(context)

        # --------------------------------------------------
        # Step 2 - Validate
        # --------------------------------------------------
        context.validation = self.validation_engine.validate(context)

        if context.validation["status"] != "PASS":
            return context

        # --------------------------------------------------
        # Step 3 - Company Profile
        # --------------------------------------------------
        context.company_profile = self.company_engine.calculate(context)

        # --------------------------------------------------
        # Step 4 - Financial Analysis
        # --------------------------------------------------
        context.financial_score = self.financial_engine.calculate(context)

        # --------------------------------------------------
        # Step 5 - Technical Analysis
        # --------------------------------------------------
        context.technical_score = self.technical_engine.calculate(context)

        # --------------------------------------------------
        # Step 6 - Valuation Analysis
        # --------------------------------------------------
        context.valuation_score = self.valuation_engine.calculate(context)

        # --------------------------------------------------
        # Step 7 - Overall Score
        # --------------------------------------------------
        context.score = self.scoring_engine.calculate(context)

        # --------------------------------------------------
        # Step 8 - Final Decision (Single Source of Truth)
        # --------------------------------------------------
        context.decision = self.decision_rules_engine.evaluate(context)

        # --------------------------------------------------
        # Step 9 - Risk Assessment
        # --------------------------------------------------
        context.risk = self.risk_engine.assess(context)

        # --------------------------------------------------
        # Step 10 - Decision Card
        # --------------------------------------------------
        context.decision_card = self.report_engine.generate(context)

        return context