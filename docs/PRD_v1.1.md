| Section                       | Change                                                                                                                     |
| ----------------------------- | -------------------------------------------------------------------------------------------------------------------------- |
| **3 Scope**                   | Ingestion now done **manually** via Contextual AI console to leverage hierarchy parser. Code-driven upload deferred to v2. |
| **6.2 Datastore & Retriever** | Uses Contextual’s default 400-token hierarchy chunks.                                                                      |
| **Prompt Library**            | `system.yaml` + `classifier.yaml` + 3 few-shot examples complete.                                                          |
| **Classifier JSON schema**    | Arrays for `naics`, `sic`; `iso_gl` list of objects; `vehicle_types` list with `count`.                                    |
| **Open Risks**                | Manual upload omission risk → weekly document-count check in console.                                                      |
