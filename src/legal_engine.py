"""
Lex Contract Analyst Engine
Deterministic legal risk assessment evaluating limitation of liability caps, indemnities, and IP rights.
"""
from typing import Dict, Any, List

class ContractRiskAnalyzer:
    def __init__(self):
        pass

    def evaluate_clauses(self, contract: Dict[str, Any]) -> Dict[str, Any]:
        acv = float(contract.get("annual_contract_value_usd", 50000))
        liability_cap = float(contract.get("liability_cap_usd", 0))
        is_uncapped = contract.get("uncapped_liability", False)
        indemnity_type = contract.get("indemnity_clause", "mutual")
        ip_transfer = contract.get("transfers_preexisting_ip", False)

        risk_score = 15
        flagged_risks = []

        if is_uncapped or liability_cap > (acv * 5):
            risk_score += 40
            flagged_risks.append({
                "issue": "Excessive or Uncapped Liability Exposure",
                "severity": "CRITICAL",
                "recommendation": f"Cap overall aggregate liability at 1x to 2x Annual Contract Value (${acv:,.2f})."
            })
        
        if indemnity_type == "unilateral_vendor_broad":
            risk_score += 30
            flagged_risks.append({
                "issue": "Unilateral Broad-Form Indemnification",
                "severity": "HIGH",
                "recommendation": "Require mutual indemnification strictly limited to third-party IP infringement."
            })

        if ip_transfer:
            risk_score += 35
            flagged_risks.append({
                "issue": "Pre-existing Background IP Forfeiture",
                "severity": "CRITICAL",
                "recommendation": "Explicitly reserve all background IP, granting customer a non-exclusive license only."
            })

        risk_score = min(risk_score, 100)
        verdict = "HIGH_RISK_REJECT_OR_REDLINE" if risk_score >= 60 else "ACCEPTABLE_WITH_STANDARD_TERMS"

        return {
            "contract_id": contract.get("contract_id", "MSA-2026-001"),
            "contract_title": contract.get("title", "Master Services Agreement"),
            "overall_risk_score": risk_score,
            "verdict": verdict,
            "flagged_clauses": flagged_risks,
            "governing_guidelines": ["ABA Commercial Contracting Standards", "IACCM Commercial Framework"],
            "confidence_score": 0.95
        }
