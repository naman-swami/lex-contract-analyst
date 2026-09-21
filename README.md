# Lex Contract Intelligence & Clause Analyst

[![OpenGAP](https://img.shields.io/badge/OpenGAP-0.1.0-blue.svg)](agent.yaml)
[![LegalTech](https://img.shields.io/badge/Domain-Contract_Intelligence_NLP-darkblue.svg)](docs/legal_clause_taxonomy.md)
[![Ontology](https://img.shields.io/badge/Standard-ABA_Clause_Taxonomy-teal.svg)](docs/legal_clause_taxonomy.md)
[![Python](https://img.shields.io/badge/Python-3.11+-blue.svg)](requirements.txt)
[![CI](https://img.shields.io/badge/CI-Passing-brightgreen.svg)](.github/workflows/ci.yml)

A legal contract analysis engine automating clause classification, unilateral indemnification exposure detection, and redline recommendation generation.

```
                    ┌─────────────────────────┐
                    │ Raw Legal Agreement Text│
                    └────────────┬────────────┘
                                 │
                                 ▼
                    ┌─────────────────────────┐
                    │ parsers/clause_segment  │
                    └────────────┬────────────┘
                                 │
                 ┌───────────────┴───────────────┐
                 ▼                               ▼
      ┌─────────────────────┐         ┌─────────────────────┐
      │  Clause Taxonomy    │         │  Unilateral Risk    │
      │  (Indemnity / Term) │         │ (Uncapped Liability)│
      └──────────┬──────────┘         └──────────┬──────────┘
                 │                               │
                 └───────────────┬───────────────┘
                                 ▼
                    ┌─────────────────────────┐
                    │ Redline Recommendation  │
                    │ (UNFAVORABLE_REVISE)    │
                    └─────────────────────────┘
```

## Features

- **Automated Clause Segmentation**: Identifies Indemnification, Limitation of Liability, Termination, and Governing Law.
- **Unilateral Exposure Warning**: Highlights dangerous uncapped indemnity language (`without monetary limitation`).
- **Benchmark Fixture**: Pre-loaded with bilateral Non-Disclosure Agreement (NDA) sample.

## Directory Structure

```
lex-contract-analyst/
├── agent.yaml                       # OpenGAP 0.1.0 Manifest
├── EXPLAINABILITY.md                # 7-checkpoint legal NLP provenance
├── parsers/
│   └── clause_segmenter.py          # Clause parsing and risk classification
├── ontologies/
│   └── contract_clauses.yaml        # Standard commercial clause definitions
├── fixtures/
│   └── contracts/
│       └── sample_nda.txt           # Benchmark contract fixture
├── docs/
│   └── legal_clause_taxonomy.md     # Legal risk taxonomy reference
├── tests/
│   └── test_agent.py                # Contract NLP test suite
├── analyze.py                          # Legal intelligence CLI
└── requirements.txt
```

## Quick Start

```bash
# Run contract parsing tests
pytest tests/ -v

# Analyze benchmark NDA sample
python analyze.py --demo
```
