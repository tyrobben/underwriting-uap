# Underwriting Automation Platform
Repo skeleton for UAP v1.0 – keeps context small for the LLM.

## 2025-06-04 Progress Snapshot

| Milestone | Status | Key Artifacts |
|-----------|--------|---------------|
| Repo scaffold + CI (Days 1-2) | ✅ complete | README, ADR-0001, GitHub Actions |
| **Knowledge Base v1** — PDFs uploaded via Contextual console (Days 3-5) | ✅ (2025-06-03) | *Datastore ID*: `dst_…` (≈ 600 docs) |
| Prompt Library v0 — system + classifier + examples (Days 6-8) | ✅ (2025-06-04) | `prompts/system.yaml`, `prompts/classifier.yaml`, `prompts/examples/*.md` |

### Key Decisions (PRD v1.1 Addendum)

1. **Manual hierarchy-aware upload**  
   PDFs were dragged into the Contextual AI console to leverage its native heading parser.  
   *Implication*: `make upload-kb` is optional until we automate incremental updates.

2. **Classifier schema (2025-06-04)**  
   ```json
   {
     "naics": [ "string" ],
     "sic": [ "string" ],
     "am_best_class": "string",
     "iso_gl": [ { "code": "string", "desc": "string" } ],
     "vehicle_types": [ { "type": "string", "count": int } ],
     "appetite_flag": "Quote|Refer|Decline",
     "citations": [ "source_id" ]
   }

## 📌 Project Snapshot — 2025-06-04

| Milestone | Status | Key Artifacts |
|-----------|--------|---------------|
| Repo scaffold & CI (Days 1-2) | ✅ complete | README, ADR-0001, GitHub Actions |
| Knowledge Base v1 (Days 3-5) | ✅ complete | Datastore **uap-kb** (~600 docs) |
| Prompt Library v0 (Days 6-8) | ✅ complete | `prompts/` folder |
| Snapshot Tests (P-3) (Days 9-11) | ✅ **2 tests passing** | `tests/test_classifier_prompt.py` |

**Current Classifier JSON schema**

```json
{
  "naics": ["string"],
  "sic": ["string"],
  "am_best_class": "string",
  "iso_gl": [{ "code": "string", "desc": "string" }],
  "vehicle_types": [{ "type": "string", "count": 0 }],
  "appetite_flag": "Quote|Refer|Decline",
  "citations": ["source_id"]
}
