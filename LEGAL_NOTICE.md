# Legal Information Notice & Contract Risk Taxonomy

## 1. Unauthorized Practice of Law (UPL) Disclosure
Lex Commercial Contract Analyst is an automated natural language processing and semantic clause segmentation tool designed to assist legal professionals, contract managers, and procurement officers.

> [!IMPORTANT]
> **No Attorney-Client Privilege or Representation**:
> - Use of this software does not create an attorney-client relationship between the user and `@naman-swami` or any contributor.
> - The analytical classifications, risk ratings, and clause redlines produced by this tool do NOT constitute legal advice or formal legal opinions under **American Bar Association (ABA) Model Rule 5.5** or corresponding state and international bar association regulations.
> - All contract evaluations must be reviewed, verified, and approved by qualified in-house or external legal counsel licensed in the governing jurisdiction prior to contract execution.

---

## 2. Contract Clause Risk Grading Taxonomy
The clause segmentation engine (`parsers/clause_segmenter.py`) classifies commercial agreement clauses against standardized risk tiers:

### A. Indemnification & Defense Obligations
- **Market Standard**: Mutual indemnification limited to third-party claims arising from gross negligence, willful misconduct, or intellectual property infringement.
- **High Risk**: Broad unilateral indemnification requiring customer to indemnify vendor for direct contract breaches.
- **Critical Risk**: Unilateral indemnity covering indirect, consequential, or punitive damages without reciprocal obligations.

### B. Limitation of Liability (LoL) & Damages Exclusion
- **Market Standard**: Aggregate liability mutual cap equal to fees paid in the preceding 12 months, with mutual waiver of consequential and punitive damages.
- **High Risk**: Unilateral liability cap favoring one party, or carve-outs that leave confidentiality obligations uncapped without mutual reciprocity.
- **Critical Risk**: Complete absence of liability limitation (uncapped financial exposure).

### C. Termination Rights & Survival
- **Market Standard**: Termination for convenience upon 30 or 60 days written notice, with pro-rata refund of unearned prepaid fees.
- **High Risk**: Forfeiture of all prepaid fees upon termination for convenience by vendor.

### D. Governing Law & Dispute Resolution
- **Market Standard**: Established neutral commercial forums (e.g., State of Delaware, State of New York, English Law) with binding arbitration or state/federal court jurisdiction.
- **High Risk**: Onerous foreign jurisdiction requiring in-person proceedings and mandatory prevailing-party attorney fee shifting.

---

## 3. Redlining Principles & Verification Workflow
Lex generates standard fallback redlines based on **World Commerce & Contracting (WorldCC)** benchmarks:
1. Extract and segment text blocks via regex and semantic boundary heuristics.
2. Cross-reference clause language against `ontologies/contract_clauses.yaml`.
3. Highlight high-risk triggers and output redline recommendation diffs directly to the reviewing counsel.
