# Deliverable 2 — Operational Schemas, Features, and Capability Matrix (fre-meta-harness consumable)

## 1) Operational feature matrix (pipeline capabilities)

```json
{
  "schema_version": "1.0.0",
  "packet_type": "operational_feature_matrix",
  "status": "proposed",
  "rows": [
    {
      "capability_id": "inbox_packet_normalization",
      "parent_surface_type": "communication_plane",
      "target_contract_surface": "contracts/inbox-packet.yaml",
      "runtime_trigger": "new_consume_artifact_detected",
      "runtime_actor": "inbox_review_agent",
      "validation_method": "Validate packet has front matter, bottom matter marker, and required body sections.",
      "evidence_artifact": "evaluation/research/compiled/source-index.json",
      "blocker_or_dependency": "Requires markdown parser + schema validator.",
      "parent_lane_classification": "core"
    },
    {
      "capability_id": "transcription_and_doc_extraction",
      "parent_surface_type": "distribution_plane",
      "target_contract_surface": "contracts/research-packet-manifest.yaml",
      "runtime_trigger": "audio_or_pdf_or_html_intake",
      "runtime_actor": "intake_mapper",
      "validation_method": "Validate extracted text coverage and source provenance map per artifact.",
      "evidence_artifact": "evaluation/research/harvest-manifest.json",
      "blocker_or_dependency": "ASR and parser tools must be available.",
      "parent_lane_classification": "core"
    },
    {
      "capability_id": "extracted_vs_enriched_labeling",
      "parent_surface_type": "policy_plane",
      "target_contract_surface": "contracts/policy-decision.yaml",
      "runtime_trigger": "requirement_generation",
      "runtime_actor": "spec_interpreter",
      "validation_method": "Reject unlabeled claims and require source refs for extracted claims.",
      "evidence_artifact": "evaluation/research/compiled/capability-harvest.json",
      "blocker_or_dependency": "Requires policy ruleset for claim provenance.",
      "parent_lane_classification": "core"
    },
    {
      "capability_id": "capability_matrix_compilation",
      "parent_surface_type": "observability_plane",
      "target_contract_surface": "contracts/capability-matrix.yaml",
      "runtime_trigger": "post_feature_synthesis",
      "runtime_actor": "semantic_cartographer",
      "validation_method": "Validate output against schemas/capability-matrix.schema.json.",
      "evidence_artifact": "evaluation/research/compiled/feature-matrix.json",
      "blocker_or_dependency": "Requires all required classification enums and doctrine flags.",
      "parent_lane_classification": "core"
    },
    {
      "capability_id": "gap_placement_generation",
      "parent_surface_type": "arbitration_lane",
      "target_contract_surface": "schemas/gap-placement-map.schema.json",
      "runtime_trigger": "after_capability_compile",
      "runtime_actor": "architect",
      "validation_method": "Each missing capability maps to exact blocker/dependency and proposed closure lane.",
      "evidence_artifact": "evaluation/research/compiled/gap-placement-map.json",
      "blocker_or_dependency": "Needs baseline target feature set definition.",
      "parent_lane_classification": "gated"
    },
    {
      "capability_id": "policy_gate_evaluator",
      "parent_surface_type": "policy_plane",
      "target_contract_surface": "contracts/policy-decision.yaml",
      "runtime_trigger": "pre_promotion",
      "runtime_actor": "orchestrator_validator",
      "validation_method": "Run allow/block/ask and loop budget checks with violations persisted.",
      "evidence_artifact": "evaluation/tool-health/status.json",
      "blocker_or_dependency": "Requires gate runner and persistent violation sink.",
      "parent_lane_classification": "core"
    },
    {
      "capability_id": "observability_bundle_emission",
      "parent_surface_type": "observability_plane",
      "target_contract_surface": "contracts/observability-event.yaml",
      "runtime_trigger": "task_lifecycle_events",
      "runtime_actor": "mesh_verifier",
      "validation_method": "Emit event envelopes with correlation IDs and benchmark metrics.",
      "evidence_artifact": "evaluation/tool-health/peer-mesh-local-events.jsonl",
      "blocker_or_dependency": "Requires ingest adapter and benchmark schema conformance.",
      "parent_lane_classification": "core"
    },
    {
      "capability_id": "pixeltable_duckdb_persistence",
      "parent_surface_type": "distribution_plane",
      "target_contract_surface": "pixeltable-operational-substrate.md",
      "runtime_trigger": "artifact_write",
      "runtime_actor": "filesystem_router",
      "validation_method": "Persist tools/tasks/artifacts/events/scorecards and verify query recipes.",
      "evidence_artifact": "evaluation/copilot-ratchet-report.json",
      "blocker_or_dependency": "Adapter implementation pending for live tables.",
      "parent_lane_classification": "gated"
    }
  ]
}
```

## 2) Capability matrix (fre-meta-harness aligned)
- Existing canonical matrix is already present and valid at:
  - `contracts/capability-matrix.yaml`
  - `schemas/capability-matrix.schema.json`
  - `evaluation/research/compiled/feature-matrix.json`

### Extension recommendation
Append the 8 operational rows above into compiled matrix generation so “consume pipeline” capabilities become first-class entries alongside upstream imported capabilities.

## 3) Schema package additions (proposed)

### 3.1 `schemas/operational-feature-matrix.schema.json`
```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "$id": "https://fre-meta-harness/schemas/operational-feature-matrix.schema.json",
  "title": "Operational Feature Matrix",
  "type": "object",
  "required": ["schema_version", "packet_type", "status", "rows"],
  "properties": {
    "schema_version": {"type": "string"},
    "packet_type": {"type": "string", "const": "operational_feature_matrix"},
    "status": {"type": "string", "enum": ["proposed", "refreshed"]},
    "rows": {
      "type": "array",
      "items": {
        "type": "object",
        "required": [
          "capability_id",
          "parent_surface_type",
          "target_contract_surface",
          "runtime_trigger",
          "runtime_actor",
          "validation_method",
          "evidence_artifact",
          "blocker_or_dependency",
          "parent_lane_classification"
        ],
        "properties": {
          "capability_id": {"type": "string"},
          "parent_surface_type": {"type": "string"},
          "target_contract_surface": {"type": "string"},
          "runtime_trigger": {"type": "string"},
          "runtime_actor": {"type": "string"},
          "validation_method": {"type": "string"},
          "evidence_artifact": {"type": "string"},
          "blocker_or_dependency": {"type": "string"},
          "parent_lane_classification": {
            "type": "string",
            "enum": ["core", "gated", "deployment_specific", "reference", "blocked_with_exact_dependency"]
          }
        }
      }
    }
  }
}
```

### 3.2 `schemas/evidence-strength.schema.json`
```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "$id": "https://fre-meta-harness/schemas/evidence-strength.schema.json",
  "title": "Evidence Strength",
  "type": "object",
  "required": ["source_ref", "strength"],
  "properties": {
    "source_ref": {"type": "string"},
    "strength": {
      "type": "string",
      "enum": [
        "transcript_only",
        "transcript_plus_context_summary",
        "task_capture_without_terminal_frames",
        "task_stub_without_terminal_frames",
        "terminal_or_frame_verified"
      ]
    },
    "notes": {"type": "string"}
  }
}
```

## 4) Extraction capabilities from reviewed consume folders

### prompting-tools.consume
- Tool catalog contractization
- Policy gate design
- Observability/event model
- Capability harvesting doctrine
- Pixeltable/DuckDB substrate requirements

### transcribe.consume
- Transcript-to-product-package transformer pattern
- Structured handoff spec and schema-first workflow

### file-system-structure-research.consume
- ICM pattern: folder-as-agent-orchestrator
- stage-scoped context loading
- strong fit for your consume pipeline architecture

## 5) Consumption contract for fre-meta-harness
For compatibility, emit outputs into existing authoritative compiled paths:
- `evaluation/research/compiled/capability-harvest.json`
- `evaluation/research/compiled/feature-matrix.json`
- `evaluation/research/compiled/gap-placement-map.json`
- `evaluation/research/compiled/source-index.json`

and validate against:
- `schemas/compiled-capability-harvest.schema.json`
- `schemas/compiled-feature-matrix.schema.json`
- `schemas/gap-placement-map.schema.json`
- `schemas/source-index.schema.json`

## 6) Immediate next actions
1. Implement matrix extension compiler for operational rows.
2. Add evidence-strength tagging into all compiled packets.
3. Add policy gate step before writing compiled outputs.
4. Add regression check against previous compiled feature matrix.
