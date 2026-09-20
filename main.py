import json
import argparse
from src.legal_engine import ContractRiskAnalyzer

def main():
    parser = argparse.ArgumentParser(description="Lex Contract Risk Analyzer CLI")
    parser.add_argument("--demo", action="store_true", help="Run simulated commercial SaaS agreement audit")
    args = parser.parse_args()

    analyzer = ContractRiskAnalyzer()
    sample_contract = {
        "contract_id": "MSA-ENTERPRISE-882",
        "title": "Cloud SaaS Enterprise Agreement",
        "annual_contract_value_usd": 120000,
        "liability_cap_usd": 10000000,
        "uncapped_liability": True,
        "indemnity_clause": "unilateral_vendor_broad",
        "transfers_preexisting_ip": True
    }

    report = analyzer.evaluate_clauses(sample_contract)
    print("="*60)
    print(" LEX LEGAL CONTRACT AUDIT & REDLINE ADVISORY")
    print("="*60)
    print(json.dumps(report, indent=2))
    print("="*60)

if __name__ == "__main__":
    main()
