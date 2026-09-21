"""
Lex Contract Clause Parser & Risk Analyzer
Segments legal documents into clause classifications and evaluates unilateral risk exposures.
"""
import re
from typing import List, Dict, Any

class ContractClauseAnalyzer:
    CLAUSE_KEYWORDS = {
        "INDEMNIFICATION": ["indemnify", "hold harmless", "defend"],
        "LIMITATION_OF_LIABILITY": ["limitation of liability", "consequential damages"],
        "TERMINATION_FOR_CONVENIENCE": ["terminate for convenience", "without cause"],
        "GOVERNING_LAW": ["governing law", "jurisdiction", "governed by"]
    }

    @classmethod
    def analyze_document(cls, text: str) -> Dict[str, Any]:
        paragraphs = [p.strip() for p in text.split("\n\n") if p.strip()]
        findings = []

        for idx, para in enumerate(paragraphs, 1):
            lower_para = para.lower()
            matched_clause = None

            for clause_type, kws in cls.CLAUSE_KEYWORDS.items():
                if any(kw in lower_para for kw in kws):
                    matched_clause = clause_type
                    break

            if matched_clause:
                is_high_risk = False
                redline = None

                if matched_clause == "INDEMNIFICATION":
                    if "unconditionally" in lower_para or "without monetary limitation" in lower_para:
                        is_high_risk = True
                        redline = "REVISE: Remove 'without monetary limitation'; insert liability cap."
                elif matched_clause == "TERMINATION_FOR_CONVENIENCE":
                    if "without cause" in lower_para:
                        redline = "NOTE: Verify mutual termination rights."

                findings.append({
                    "section_index": idx,
                    "clause_type": matched_clause,
                    "risk_tier": "HIGH" if is_high_risk else "STANDARD",
                    "snippet": para[:120] + "...",
                    "redline_recommendation": redline
                })

        high_risk_count = sum(1 for f in findings if f["risk_tier"] == "HIGH")

        return {
            "total_clauses_detected": len(findings),
            "high_risk_clauses": high_risk_count,
            "overall_posture": "UNFAVORABLE_REVISE" if high_risk_count > 0 else "ACCEPTABLE",
            "findings": findings
        }

    @classmethod
    def analyze_file(cls, filepath: str) -> Dict[str, Any]:
        with open(filepath, "r", encoding="utf-8") as f:
            text = f.read()
        res = cls.analyze_document(text)
        res["filepath"] = filepath
        return res
