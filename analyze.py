import argparse
import os
from parsers.clause_segmenter import ContractClauseAnalyzer

def main():
    parser = argparse.ArgumentParser(description="Lex Contract Intelligence CLI")
    parser.add_argument("--demo", action="store_true", help="Analyze benchmark NDA sample")
    args = parser.parse_args()

    contract_file = os.path.join(os.path.dirname(__file__), "fixtures", "contracts", "sample_nda.txt")

    if args.demo:
        res = ContractClauseAnalyzer.analyze_file(contract_file)
        print("=== LEX CONTRACT INTELLIGENCE ANALYSIS REPORT ===\n")
        print(f"Document: {os.path.basename(contract_file)}")
        print(f"Overall Posture: {res['overall_posture']} | High Risk Clauses: {res['high_risk_clauses']}\n")
        for f in res["findings"]:
            print(f"Section {f['section_index']}: [{f['clause_type']}] Tier: {f['risk_tier']}")
            print(f"  Excerpt: {f['snippet']}")
            if f["redline_recommendation"]:
                print(f"  Recommendation: {f['redline_recommendation']}")
            print("-" * 50)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
