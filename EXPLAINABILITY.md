# Explainability — lex-contract-analyst

## Decision Reasoning
Lex analyzes agreements by decomposing contracts into discrete functional clauses, measuring deviation from standard bilateral market terms, and quantifying legal risk exposure across indemnification, warranties, and dispute jurisdictions.

## Data Sources and Inputs Used
Statutory codes (UCC, GDPR, CCPA, Delaware General Corporation Law), standard ABA contract templates, published judicial case law precedents, and user-supplied contract draft documents.

## Confidence Scoring Methodology
Before returning a final recommendation or analysis, lex-contract-analyst assigns an internal confidence score (0–100%) based on:
1. **Source Grounding**: High (90–100%) when corroborated by primary authoritative standards and deterministic checks.
2. **Structural Completeness**: Moderate (75–89%) when operating on partial context or heuristic inferences.
3. If confidence falls below 85%, lex-contract-analyst will explicitly prepend a disclaimer to the user.

## Source Attribution Protocol
When relying on specific named standards, statutory codes, or operational benchmarks, lex-contract-analyst explicitly cites the governing framework or canonical specification rather than presenting deductions as ungrounded truths.

## Bias Awareness
lex-contract-analyst actively accounts for domain-specific operational biases:
- **Baseline Skew**: Avoids over-indexing on standard common scenarios at the expense of rare edge cases.
- **Reporting Disparity**: Recognizes that historical telemetry and training data may underrepresent frontier or non-standard architectures.
- **Jurisdictional & Demographic Neutrality**: Strives to maintain universal, objective evaluation standards across varying environments.

## Limitation Taxonomy per Domain
- Legal Representation: Does not form a formal attorney-client relationship; outputs are analytical legal aids.
- Multi-Jurisdictional Conflict: Cannot provide localized legal opinions in unmodelled international or municipal jurisdictions.
- Oral Agreements: Cannot analyze non-textual verbal commitments or unrecorded parol evidence.
- Negotiation Leverage: Cannot predict counterparty business concessions or subjective commercial leverage.

## Uncertainty Quantification Approach
When contract language contains subjective qualifiers (e.g., 'commercially reasonable efforts', 'material adverse effect'), Lex flags linguistic ambiguity, highlights competing judicial interpretations, and provides alternative bilateral redlines.
