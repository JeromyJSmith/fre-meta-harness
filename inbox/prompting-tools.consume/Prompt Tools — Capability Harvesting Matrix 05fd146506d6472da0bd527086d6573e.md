# Prompt Tools — Capability Harvesting Matrix

<aside>
🧠

**Purpose**: Build the **capability inventory** and the **capability matrix** that lets the harness map “what we have” to “what the target application needs”.

</aside>

## 0) Before → After

- **Before**: prompts/tools exist as a pile of text + lore.
- **After**: every tool/prompt/agent declares:
    - capability claims (CAP-xxxx)
    - support level (native/partial/composed/planned)
    - evidence (tests/examples/quotes)
    - constraints (input limits, policies, latency/cost)

## 1) Core deliverables

1) Capability taxonomy (hierarchical)

2) CapabilityMatrix (module ↔ capability claims)

3) Gap report (target app requirements ↔ missing/partial capabilities)

4) Tool roadmap (new ToolSpecs required to close gaps)

## 2) Capability taxonomy template

- CAP-0001: Source ingestion
- CAP-0002: Extraction (source-faithful)
- CAP-0003: Enrichment (labeled)
- CAP-0004: Schema authoring
- CAP-0005: Policy authoring
- CAP-0006: Tool endpoint packaging
- CAP-0007: Observability emission
- CAP-0008: Evaluation + regression
- CAP-0009: Pixeltable persistence
- CAP-0010: DuckDB query surfaces

(Extend; keep IDs stable.)

## 3) Pixeltable tables (recommended)

- capability_taxonomy
- capability_matrix
- capability_evidence
- gap_reports

## 4) Tasklist

- [ ]  Freeze CAP taxonomy v0 (IDs + definitions)
- [ ]  Define CapabilitySpec JSON Schema
- [ ]  Define CapabilityMatrix JSON Schema
- [ ]  Generate matrix for current PromptPack
- [ ]  Add evidence artifacts (examples/tests) to Pixeltable
- [ ]  Create gap report for: “Prompt → Tool packaging” + “ICM workspace pipelines”