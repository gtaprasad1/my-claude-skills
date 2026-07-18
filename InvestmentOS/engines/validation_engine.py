
class ValidationEngine:
    """
    Validates collected evidence.
    """

    def validate(self, context):

        evidence = context.evidence

        if not evidence["success"]:
            return {
                "status": "FAIL",
                "message": evidence["error"],
            }

        if evidence["company"] is None:
            return {
                "status": "FAIL",
                "message": "Company profile missing.",
            }

        if evidence["financials"] is None:
            return {
                "status": "FAIL",
                "message": "Financial statements missing.",
            }

        if evidence["price_history"] is None:
            return {
                "status": "FAIL",
                "message": "Price history missing.",
            }

        return {
            "status": "PASS",
            "message": "Validation successful.",
        }
    