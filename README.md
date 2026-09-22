# Lex Commercial Contract Analyst

> **Automated Legal Clause Segmentation & Risk Exposure Assessment Platform**  
> Parsing Non-Disclosure Agreements, Master Services Agreements, and Vendor Contracts.

---

### Clause Risk Taxonomy

| Legal Clause Category | Standard Market Language | High-Risk Redline Trigger |
| :--- | :--- | :--- |
| **Indemnification** | Mutual indemnification for third-party IP infringement | **Unilateral** broad indemnification covering general breach |
| **Limitation of Liability** | Capped at aggregate 12-month contract value | **Uncapped** liability or one-sided liability exclusion |
| **Termination** | 30 days written notice for convenience or material breach | Termination for convenience with forfeiture of prepaid fees |
| **Governing Law** | Standard neutral commercial forum (DE / NY / UK) | Distant or unfavorable foreign jurisdiction with fee shifting |

---

### Contract Redline Demonstration

Sample analysis of high-risk indemnity clause (`fixtures/contracts/sample_nda.txt`):

```markdown
> "Recipient shall defend, indemnify, and hold harmless Discloser from any and all claims, 
> losses, liabilities, and expenses arising out of any breach of this Agreement."
```

**Legal Analyst Risk Assessment:**
- **Risk Tier**: **CRITICAL** (Unilateral & Uncapped)
- **Recommendation**: Redline to mutual indemnity, insert 1x annual fee liability cap, and limit damages strictly to third-party direct claims.

---

### Legal Analytics CLI

```bash
# Analyze benchmark commercial agreement
python analyze.py --demo

# Run legal clause segmentation unit tests
pytest tests/ -v
```

Full legal clause ontology definitions and attorney oversight notices are maintained in [LEGAL_NOTICE.md](LEGAL_NOTICE.md) and `ontologies/contract_clauses.yaml`.
