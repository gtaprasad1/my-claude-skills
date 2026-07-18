class ValidationEngine:
    """
    Validates collected evidence.
    """

    REQUIRED_FIELDS = [
        "company",
        "financials",
        "price_history",
        "news",
    ]

    def validate(self, evidence: dict):

        missing = []

        for field in self.REQUIRED_FIELDS:
            if field not in evidence or evidence[field] is None:
                missing.append(field)

        if missing:
            return {
                "status": "WARNING",
                "missing": missing,
                "confidence": "MEDIUM"
            }

        return {
            "status": "PASS",
            "missing": [],
            "confidence": "HIGH"
        }