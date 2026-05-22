# Deliverable 1 — Ideas Discussed + Implementation Plan

## Scope processed
- Transcribed: `/Users/ojeromyo/Downloads/stem-separation/transcriptions/Call with Robert Rhu.m4a`
- Reviewed folders:
  - `/Volumes/PixelTable/VW_iTWIN_Bridge/meta/inbox/prompting-tools.consume`
  - `/Volumes/PixelTable/VW_iTWIN_Bridge/meta/inbox/transcribe.consume`
  - `/Volumes/PixelTable/VW_iTWIN_Bridge/meta/inbox/file-system-structure-research.consume`
- Reviewed current state:
  - `/Volumes/PixelTable/VW_iTWIN_Bridge/meta` contracts/schemas/evaluation structure

---

## A) Transcription result (Robert call)
Artifacts now available in:
- `Call with Robert Rhu.txt`
- `Call with Robert Rhu.json`
- `Call with Robert Rhu.srt`
- `Call with Robert Rhu.vtt`
- `Call with Robert Rhu.tsv`

### Extracted ideas from Robert call (implementation-relevant)
> Note: conversation is primarily personal/narrative. Limited direct product requirements.

1. **High-emotion narrative capture is valuable**
   - Implementation: add trauma-safe transcript workflow (`pause/resume`, draft checkpoints, private notes, redaction).
2. **Audio-to-structured memory transformation**
   - Implementation: transcript -> entity/event extraction -> timeline/knowledge graph packet.
3. **Source confidence labeling is required**
   - Implementation: every extracted claim labeled as `transcript_only | transcript_plus_context_summary | terminal_or_frame_verified`.
4. **Sensitive-topic handling**
   - Implementation: policy gate for medical/mental-health and personal identifiable narrative content before publication/redistribution.

---

## B) Unified pipeline for all reviewed consume folders

## Pipeline objective
Convert mixed inbox assets (transcripts, prompt docs, research docs/PDF/web captures) into:
1) implementation-ready feature and schema outputs,
2) governed capability matrix artifacts consumable by `fre-meta-harness`.

## Proposed stage pipeline (ICM-style filesystem orchestration)

1. **Stage 00 — Intake (inbox watcher)**
   - Input: `.consume` folders
   - Output: normalized packet index (`source-index`)
   - Contract refs: `contracts/inbox-packet.yaml`, `contracts/inbox-routing-decision.yaml`

2. **Stage 01 — Parse/Transcribe/Extract**
   - Audio: Whisper/FunASR -> txt/json/srt/vtt/tsv
   - Markdown/PDF/HTML: text extraction + chunking
   - Output: `raw_extracts/*` + provenance map

3. **Stage 02 — Idea & Requirement Extraction**
   - Split `Extracted` vs `Enriched`
   - Generate idea table + traceability
   - Output: `ideas.json`, `requirements.json`

4. **Stage 03 — Feature Synthesis**
   - Generate FEAT objects (MVP/V1/V2)
   - Link each feature to evidence quote/source refs
   - Output: `feature-specs.json`

5. **Stage 04 — Capability Harvest**
   - Build CAP taxonomy + capability claims + support level
   - Output: `capability-harvest.json`, `capability-matrix.json`
   - Contract refs: `contracts/capability-matrix.yaml`, `schemas/capability-matrix.schema.json`

6. **Stage 05 — Policy/Gates (Trust plane)**
   - allow/block/ask, redaction, loop-budget, completion checks
   - Output: `gate-results.json`, `violations.json`
   - Contract refs: `contracts/policy-decision.yaml`, `contracts/hook-manifest.yaml`

7. **Stage 06 — Observability + Benchmarks**
   - Emit event envelopes + benchmark points + scorecards
   - Output: `events.jsonl`, `benchmarks.json`, `scorecards.json`
   - Contract refs: `contracts/observability-event.yaml`, `contracts/observability-ingest.yaml`, `contracts/benchmark-emission.yaml`

8. **Stage 07 — Pixeltable/DuckDB Persistence**
   - Persist tools/tasks/artifacts/events/scores
   - Output: SQL-reportable artifact store

9. **Stage 08 — Compiled Outputs + Handoff**
   - Compile:
     - `evaluation/research/compiled/capability-harvest.json`
     - `evaluation/research/compiled/feature-matrix.json`
     - `evaluation/research/compiled/gap-placement-map.json`
     - `evaluation/research/compiled/source-index.json`
   - Produce handoff markdown + structured packet

---

## C) Feature set for this pipeline

### MVP
- Inbox packet normalization
- Audio/doc extraction
- Extracted-vs-enriched requirement tagging
- Capability matrix generation
- Policy gate pass/fail + violations
- Observability event emission
- Compiled artifact output generation

### V1
- Automated routing decision generation
- Regression baselines for capability matrix changes
- Pixeltable live ingestion adapters
- Gap-to-roadmap generator (auto creates proposed ToolSpecs)

### V2
- Multi-agent branching with bounded merge gates
- Cross-device runtime handshake checks
- Continuous fresh-research refresh + auto-PR for matrix updates

---

## D) Implementation mapping to current meta repo

Use existing authoritative surfaces (already present):
- Contracts: `contracts/*.yaml` (capability, policy, observability, routing, delegation)
- Schemas: `schemas/*.schema.json` (capability matrix + compiled feature matrix + event/policy artifacts)
- Compiled outputs path: `evaluation/research/compiled/*`

### Minimal coding tasks
1. Add `scripts/consume_inbox_packets.py` (or TS equivalent)
2. Add `scripts/extract_requirements_from_transcripts.py`
3. Add `scripts/build_operational_capability_matrix.py`
4. Add `scripts/run_policy_gates.py`
5. Add `scripts/emit_observability_bundle.py`
6. Add `scripts/compile_research_outputs.py`

---

## E) Risks and guardrails
- **Risk**: non-product/personal transcripts pollute product requirement extraction.
  - Guardrail: require explicit domain classifier + confidence threshold before feature generation.
- **Risk**: evidence inflation from weak sources.
  - Guardrail: mandatory evidence-strength labels.
- **Risk**: schema drift between contracts and compiled outputs.
  - Guardrail: schema validation gate before promotion.

---

## F) 7-day execution plan
1. Day 1: intake parser + source index compiler
2. Day 2: transcript extractor + idea normalization
3. Day 3: feature synthesis + traceability map
4. Day 4: capability harvest + matrix emitter
5. Day 5: policy gate engine + violations table
6. Day 6: observability + benchmark emitter
7. Day 7: full dry-run on all three `.consume` folders + handoff report
