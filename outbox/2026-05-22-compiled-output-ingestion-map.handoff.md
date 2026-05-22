---
artifact_type: .handoff.md
handoff_id: HANDOFF-20260522-INGESTMAP
owner: research
parent_only: true
---

# Compiled-output ingestion map

| Compiled output | Ingestion rule | Policy gate |
| --- | --- | --- |
| `evaluation/research/compiled/capability-harvest.json` | Keep canonical capability rows aligned while appending a consume-source-quality compiler note. | Do not promote new runtime lanes from compile-only artifact strengthening. |
| `evaluation/research/compiled/feature-matrix.json` | Preserve canonical feature rows and use outbox guidance for any future extension. | Extension guidance stays advisory until a later governed slice approves canonical edits. |
| `evaluation/research/compiled/gap-placement-map.json` | Retain consume_source_quality as the bounded strengthening lane while related blocked lanes stay explicit. | Do not collapse live InfraNodus or persistence blockers into this slice. |
| `evaluation/research/compiled/source-index.json` | Attach evidence-strength records to every source and add first-party consume packets into the governed index. | Transcript-derived workflow claims remain blocked until frame or terminal proof exists. |

---bottom-matter---
validation_status: draft
structured_artifact_ref: evaluation/research/harvest-manifest.json
open_questions: []
