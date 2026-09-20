import pytest
from src.legal_engine import ContractRiskAnalyzer

def test_safe_standard_contract():
    analyzer = ContractRiskAnalyzer()
    contract = {
        "contract_id": "SAFE-01",
        "annual_contract_value_usd": 100000,
        "liability_cap_usd": 100000,
        "uncapped_liability": False,
        "indemnity_clause": "mutual",
        "transfers_preexisting_ip": False
    }
    res = analyzer.evaluate_clauses(contract)
    assert res["overall_risk_score"] < 50
    assert res["verdict"] == "ACCEPTABLE_WITH_STANDARD_TERMS"
    assert len(res["flagged_clauses"]) == 0

def test_high_risk_uncapped_liability():
    analyzer = ContractRiskAnalyzer()
    contract = {
        "contract_id": "RISK-02",
        "annual_contract_value_usd": 50000,
        "uncapped_liability": True,
        "indemnity_clause": "unilateral_vendor_broad",
        "transfers_preexisting_ip": True
    }
    res = analyzer.evaluate_clauses(contract)
    assert res["overall_risk_score"] >= 80
    assert res["verdict"] == "HIGH_RISK_REJECT_OR_REDLINE"
    assert len(res["flagged_clauses"]) == 3
