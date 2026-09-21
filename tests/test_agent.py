import os
import pytest
from parsers.clause_segmenter import ContractClauseAnalyzer

def test_indemnity_clause_detection():
    clause = "Recipient agrees to unconditionally indemnify, defend, and hold harmless Disclosing Party without monetary limitation."
    res = ContractClauseAnalyzer.analyze_document(clause)
    assert res["total_clauses_detected"] == 1
    assert res["high_risk_clauses"] == 1
    assert res["findings"][0]["clause_type"] == "INDEMNIFICATION"
    assert res["findings"][0]["risk_tier"] == "HIGH"

def test_standard_governing_law():
    clause = "This agreement shall be governed by the laws of the State of Delaware."
    res = ContractClauseAnalyzer.analyze_document(clause)
    assert res["total_clauses_detected"] == 1
    assert res["high_risk_clauses"] == 0
    assert res["findings"][0]["clause_type"] == "GOVERNING_LAW"

def test_benchmark_nda_file():
    doc_path = os.path.join(os.path.dirname(__file__), "..", "fixtures", "contracts", "sample_nda.txt")
    res = ContractClauseAnalyzer.analyze_file(doc_path)
    assert res["total_clauses_detected"] >= 3
    assert res["high_risk_clauses"] >= 1
    assert res["overall_posture"] == "UNFAVORABLE_REVISE"
