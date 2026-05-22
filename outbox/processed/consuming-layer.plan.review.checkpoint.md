---
id: "packet-consuming-layer-plan-review-checkpoint"
slug: "consuming-layer-plan-review-checkpoint"
doctype: "inbox_packet"
status: "ready_for_routing"
version: "0.1.0"
owner: "fre-meta-harness"
artifact_id: "PACKET-20260521-PLANREVIEW"
artifact_type: ".checkpoint.md"
producer_role: "research"
target_scope: "portable_parent_wrapper"
repo_root: "/Volumes/PixelTable/VW_iTWIN_Bridge/meta"
parent_only: true
structured_contract_ref: "contracts/inbox-packet.yaml"
prompt_candidate_class: "review_of_council_candidate_A"
routing_tags:
  - "inbox-first"
  - "review"
  - "amendments"
  - "truth-correction"
required_consumers:
  - "architect"
  - "orchestrator-validator"
upstream_refs:
  - "inbox/consuming-layer.plan.md"
  - "inbox/consuming-layer.plan.json"
evidence_refs:
  - "outbox/2026-05-21-pipeline-ideas-and-implementation.handoff.md"
  - "outbox/2026-05-21-operational-capability-matrix-and-schemas.handoff.md"
  - "pixeltable-operational-substrate.md"
  - "agentics-library.md"
  - "library.yaml"
  - "gold-goals.md"
created_at: "2026-05-21T00:00:00Z"
updated_at: "2026-05-21T00:00:00Z"
---

# Review of consuming-layer.plan.md against existing wrapper authorities

## 0. How this review is structured

```yaml
review_axes:
  - axis: truth_corrections
    severity: critical
    purpose: "Plan marks artifacts as 'new' that already exist. Fabrication risk."
  - axis: missing_concepts
    severity: high
    purpose: "Reviewed files surface load-bearing concepts the plan omits."
  - axis: structural_distinctions
    severity: high
    purpose: "Plan flattens two pipelines into one. They are different things."
  - axis: substrate_stack
    severity: critical
    purpose: "Plan undershoots the Pixeltable -> Arrow/Parquet -> DuckDB WASM gold goal."
  - axis: registry_reconciliation
    severity: high
    purpose: "Plan invents a tools/ registry that overlaps library.yaml. Pick one spine."
  - axis: cross_cutting_concerns
    severity: medium
    purpose: "InfraNodus, evidence-strength taxonomy, parent_lane_classification."
amendment_format: per_phase_delta_yaml
```

## 1. Truth corrections (CRITICAL)

The plan tags many contracts as `status: new`. Per `library.yaml`, these already
exist and are governed. Correcting fabrication risk:

```yaml
truth_corrections:
  phase_1:
    - file: contracts/agent-role-contract.yaml
      plan_status: "new"
      actual_status: "exists"
      evidence: "library.yaml references kind: contract source: contracts/agent-role-contract.yaml; describes peer-mesh roles (host, production_gatekeeper, dev_driver, mesh_verifier)"
      recommended_status: "exists_extend"
      amendment: "Phase 3 role contracts must EXTEND not REPLACE this. The contract is currently peer-mesh-shaped; we add front-door role profiles, we do not overwrite."
    - file: contracts/agent-extension-request.yaml
      plan_status: "new"
      actual_status: "exists"
      evidence: "library.yaml kind: contract source: contracts/agent-extension-request.yaml"
      recommended_status: "exists_finalize"
    - file: contracts/inbox-packet.yaml
      plan_status: "exists_finalize"
      actual_status: "exists"
      evidence: "library.yaml + agentics-library §inbox-first paragraph; example at examples/governed-inbox-packet.protocol.valid.md"
      recommended_status: "exists_active"
    - file: contracts/inbox-routing-decision.yaml
      plan_status: "exists_finalize"
      actual_status: "exists"
      evidence: "library.yaml; user CLAUDE.md references"
      recommended_status: "exists_active"
    - file: contracts/delegation-bundle.yaml
      plan_status: "exists_finalize"
      actual_status: "exists"
      evidence: "library.yaml"
      recommended_status: "exists_active"
    - file: contracts/front-door-runtime-topology.yaml
      plan_status: "exists_finalize"
      actual_status: "exists"
      evidence: "library.yaml"
      recommended_status: "exists_active"
    - file: contracts/capability-matrix.yaml
      plan_status: "exists_finalize"
      actual_status: "exists_with_compiled_evidence"
      evidence: "library.yaml + compiled artifact at evaluation/research/compiled/feature-matrix.json"
      recommended_status: "exists_extend"
      amendment: "The handoff doc proposes appending 8 operational rows. Phase 6 must consume and reconcile that proposal, not generate a parallel matrix."
    - file: contracts/three-agent-topology.yaml
      plan_status: "exists_finalize"
      actual_status: "exists"
      evidence: "library.yaml"
      recommended_status: "exists_active"
  phase_2:
    - file: schemas/governed-agent-profile.schema.json
      plan_status: "not_mentioned"
      actual_status: "exists"
      evidence: "library.yaml kind: schema source: schemas/governed-agent-profile.schema.json"
      recommended_action: "Add as upstream ref for Phase 3 role contracts. Phase 3 contracts conform to this schema."
    - file: schemas/compiled-capability-harvest.schema.json
      plan_status: "not_mentioned"
      actual_status: "exists"
      evidence: "handoff 2 §5 + library.yaml references compiled-capability-harvest evaluation"
      recommended_action: "Add to Phase 2 schemas list as exists_active."
    - file: schemas/compiled-feature-matrix.schema.json
      plan_status: "not_mentioned"
      actual_status: "exists"
      evidence: "handoff 2 §5"
      recommended_action: "Add to Phase 2 schemas list as exists_active."
    - file: schemas/gap-placement-map.schema.json
      plan_status: "not_mentioned"
      actual_status: "exists"
      evidence: "handoff 2 §5"
      recommended_action: "Add to Phase 2 schemas list as exists_active."
    - file: schemas/source-index.schema.json
      plan_status: "not_mentioned"
      actual_status: "exists"
      evidence: "handoff 2 §5"
      recommended_action: "Add to Phase 2 schemas list as exists_active."
  phase_4_and_above:
    - files_referenced_but_not_marked_existing:
        - contracts/observability-event.yaml
        - contracts/observability-ingest.yaml
        - contracts/policy-decision.yaml
        - contracts/library-distribution.yaml
        - contracts/benchmark-emission.yaml
        - contracts/peer-mesh-runtime.yaml
        - contracts/peer-mesh.yaml
        - contracts/peer-message.yaml
        - contracts/peer-lifecycle.yaml
        - contracts/hook-manifest.yaml
        - contracts/research-packet-manifest.yaml
        - contracts/parent-capability-metrics.yaml
        - contracts/agent-eval-parent-lane.yaml
      recommended_action: "All exist. Phase 1 must list these as exists_active references the plan extends from, not as omitted-prior-art."
```

Impact: **a v0.2.0 of the plan would drop ~14 'new' tags to 'exists_active'**.
That changes the work in Phase 1 from "author the contract family" to
"extend the contract family with the 6 truly new contracts" — agent-role
front-door extensions, upstream-handshake, schema-evolution-loop, consume-request,
promotion-decision, action-log. The other ~14 are already authored.

## 2. Missing concepts (HIGH severity)

```yaml
missing_concepts:
  - id: MC-001
    name: "Substrate full stack: Pixeltable -> Arrow/Parquet -> DuckDB WASM"
    where: "gold-goals.md + pixeltable-operational-substrate.md"
    plan_says: "Phase 7 binds Pixeltable + DuckDB"
    truth: "The gold goal explicitly names DuckDB WASM as the analytical browser surface over Arrow/Parquet-served Pixeltable data."
    amendment: |
      Phase 7 must add:
        - substrate/arrow-parquet-export-rules.md
        - substrate/duckdb-wasm-browser-surface.md
        - substrate/adapters/pixeltable-to-arrow.md
        - substrate/adapters/arrow-to-duckdb-wasm.md
      And reword 'binds Pixeltable + DuckDB' to 'binds Pixeltable -> Arrow/Parquet -> DuckDB-WASM'.
  - id: MC-002
    name: "Evidence-strength taxonomy"
    where: "handoff 2 §3.2 (schemas/evidence-strength.schema.json proposal)"
    enum:
      - transcript_only
      - transcript_plus_context_summary
      - task_capture_without_terminal_frames
      - task_stub_without_terminal_frames
      - terminal_or_frame_verified
    plan_says: "no evidence-strength concept"
    truth: "This taxonomy already governs the compiled research artifacts and is non-negotiable for the consuming layer (which ingests transcripts, PDFs, web captures with varying provenance strength)."
    amendment: |
      Phase 2 must add schemas/evidence-strength.schema.json as foundational.
      Phase 4 stages 05-08 must require every extracted claim to carry an evidence_strength field.
      Phase 12 must add tests/test_evidence_strength_present.py.
  - id: MC-003
    name: "parent_lane_classification enum"
    where: "contracts/capability-matrix.yaml (existing) + handoff 2 operational matrix rows"
    enum:
      - core
      - gated
      - deployment_specific
      - reference
      - blocked_with_exact_dependency
    plan_says: "no lane classification"
    truth: "The existing capability matrix already classifies every capability into one of these lanes. The plan's Phase 6 'capabilities/matrix.yaml' must use this enum."
    amendment: |
      Phase 6 capabilities/matrix.yaml must include lane classification per CAP.
      Phase 2 schemas/capability-matrix.schema.json must enforce this enum.
  - id: MC-004
    name: "Operational feature matrix (8 rows from handoff 2)"
    where: "outbox/2026-05-21-operational-capability-matrix-and-schemas.handoff.md §1"
    plan_says: "no acknowledgment"
    truth: "The handoff proposed 8 specific operational capability rows that map directly to the plan's phases (inbox normalization, transcription, extracted-vs-enriched, capability matrix, gap placement, policy gate, observability bundle, pixeltable persistence). These ARE the plan's phases in matrix form."
    amendment: |
      Phase 6 capabilities/matrix.yaml must consume these 8 rows on first emission.
      Phase 12 must regression-check that every plan phase appears in the matrix.
  - id: MC-005
    name: "Existing compiled artifacts are upstream refs"
    where: "library.yaml + evaluation/research/compiled/*"
    plan_says: "Phase 6 produces capabilities/matrix.yaml as 'new'"
    truth: "evaluation/research/compiled/{capability-harvest,feature-matrix,gap-placement-map,source-index}.json already exist as compiled artifacts. Phase 6 must extend, not regenerate."
    amendment: |
      Phase 6 must add evaluation/research/compiled/* as upstream_refs and declare which file Phase 6 outputs UPDATE vs. NEW.
  - id: MC-006
    name: "Trauma-safe / sensitive-content handling"
    where: "handoff 1 §A item 1 + §E risks"
    plan_says: "no sensitive-content policy"
    truth: "Transcripts may contain PII, medical, mental-health, or other sensitive material. The Robert Rhu transcript itself triggered this. Phase 8 must include a sensitivity policy gate."
    amendment: |
      Phase 8 must add:
        - policies/sensitive-content.yaml
        - policies/redaction.yaml
        - protocols/trauma-safe-intake.md
      Phase 4 stage 02 (conversation_capture) must reference these policies before persisting raw transcripts.
  - id: MC-007
    name: "Non-authoritative evidence role"
    where: "library.yaml understand-anything-intake-graph (kind: evaluation, source: evaluation/understand-anything-intake.json) is explicitly bounded as 'non-authoritative evidence role'"
    plan_says: "no evidence_role field"
    truth: "Some artifacts inform but cannot be cited as authoritative. The taxonomy must distinguish authoritative vs. supporting evidence."
    amendment: |
      Phase 2 schemas/artifact-registry.schema.json must add evidence_role: enum [authoritative | supporting | non_authoritative_reference].
  - id: MC-008
    name: "InfraNodus phase-tool-map as cross-cutting"
    where: "library.yaml capability: infranodus source: infranodus-phase-tool-map.json + agentics-library §infranodus 'used across every lifecycle gate'"
    plan_says: "InfraNodus mentioned only in §17 explicit_non_goals as 'optional'"
    truth: "The agentics library says InfraNodus is used at EVERY lifecycle gate as the comparison engine. The plan should reference it as a required cross-cutting check at every gate transition, even if the local bounded substitute is the default until live MCP wiring."
    amendment: |
      Phase 0, 1-12 acceptance criteria must include 'InfraNodus comparison emitted (live OR local bounded substitute) at gate transition' as a required artifact.
      The §17 non-goal language should be downgraded from 'optional' to 'live mode optional; local bounded substitute mandatory'.
  - id: MC-009
    name: "Existing scripts as upstream refs"
    where: "library.yaml jobs section + handoff 1 §F (7-day plan names exact scripts)"
    existing_scripts:
      - scripts/score-parent-wrapper.py
      - scripts/refresh-parent-tool-health.py
      - scripts/build-parent-infranodus-artifacts.py
      - scripts/run-parent-ratchet.sh
      - scripts/run-parent-agent-eval.sh
      - scripts/run-parent-peer-mesh-local.sh
      - scripts/watchers/inbox_router.py
    proposed_scripts_in_handoff:
      - scripts/consume_inbox_packets.py
      - scripts/extract_requirements_from_transcripts.py
      - scripts/build_operational_capability_matrix.py
      - scripts/run_policy_gates.py
      - scripts/emit_observability_bundle.py
      - scripts/compile_research_outputs.py
    plan_says: "scripts deliberately excluded (§17 explicit_non_goals: implementation_code)"
    truth: "The plan correctly excludes implementation code, BUT must reference existing scripts as upstream_refs because they bind validation commands. The 6 proposed scripts in handoff 1 should be listed as PROPOSED scripts surfaced for council review, not authored in this packet."
    amendment: |
      Phase 0 evidence_refs must include scripts/* enumerated.
      Phase 12 should add a sub-section listing the 6 proposed-but-not-yet-authored scripts as 'gated implementation candidates' to be promoted via agent-extension-request.yaml.
  - id: MC-010
    name: "Schema drift risk as Phase 12 gate"
    where: "handoff 1 §E + handoff 2 §6"
    plan_says: "Phase 12 test_no_governance_runtime_collapse + test_three_framings_preserved but no schema-drift check"
    truth: "Schema drift between contracts/* and compiled outputs evaluation/research/compiled/* is a named risk. Phase 12 must test for it."
    amendment: |
      Phase 12 add tests/test_schema_drift_contracts_vs_compiled.py.
```

## 3. Structural distinctions the plan flattens (HIGH)

```yaml
structural_distinctions:
  - id: SD-001
    name: "Two distinct pipelines flattened into one"
    plan_has: "Phase 4: 12-stage consuming lifecycle (project_attach -> ... -> promotion_or_block)"
    handoff_has: "9-stage consume pipeline (Stage 00 Intake -> ... -> Stage 08 Compiled Outputs + Handoff)"
    distinction: |
      The 12-stage flow is the FRONT-DOOR lifecycle: user-facing, conversation-oriented, project-attach-driven.
      The 9-stage flow is the INTERNAL CONSUME pipeline: data-transformation-oriented, packet-driven, no human in the loop after intake.
      These are NOT the same pipeline. Front-door drives entry; consume pipeline processes payload. They meet at stage 05 (drop_ingest) -> Stage 01 (parse/transcribe/extract).
    amendment: |
      Phase 4 must be renamed 'front_door_lifecycle' and the 12 stages preserved as the user-facing flow.
      A new Phase 4b 'internal_consume_pipeline' must be added with the 9 stages 00-08 from handoff 1 §B.
      Phase 5 (upstream prompt flow) sits between them: stage 12 of front-door triggers stage 00 of consume; stage 08 of consume re-emits upstream into front-door via the readiness-ack.
      Phase graph must add Phase 4b: blocked_by [1, 3], blocks [5, 11, 12].
  - id: SD-002
    name: "Three role families, plan only names two clearly"
    plan_has: "triad (governance) + front-door runtime (intake)"
    repo_has:
      - "triad: orchestrator-validator, research, architect (parent governance)"
      - "front-door runtime: user-facing-agent, spec-interpreter, intake-mapper, semantic-cartographer, filesystem-router, wrapper-synthesizer (intake + routing)"
      - "peer-mesh runtime: peer_mesh_host, production_gatekeeper, dev_driver, mesh_verifier (per existing contracts/agent-role-contract.yaml)"
    truth: "The peer-mesh role family is a third runtime layer already in the repo. The plan must explicitly distinguish all three families and forbid collapse across any pair."
    amendment: |
      Phase 3 must add three role-family contracts:
        - contracts/role-families/triad-governance.yaml (orchestrator-validator + research + architect)
        - contracts/role-families/front-door-runtime.yaml (six front-door roles)
        - contracts/role-families/peer-mesh-runtime.yaml (existing four roles, finalized reference)
      Phase 11 protocols/three-framings-non-collapse.md must be extended to three-role-families-non-collapse.md (or a sibling protocol added).
      Phase 12 tests/test_no_governance_runtime_collapse.py must be split into:
        - tests/test_no_triad_frontdoor_collapse.py
        - tests/test_no_triad_peermesh_collapse.py
        - tests/test_no_frontdoor_peermesh_collapse.py
  - id: SD-003
    name: "Library spine reconciliation: tools/ vs library.yaml"
    plan_has: "Phase 6 creates tools/REGISTRY.md and tools/manifest.yaml"
    repo_has: "library.yaml already carries the catalog spine with prompts, capabilities, references, jobs, distribution_units"
    distinction: |
      The plan invents a parallel registry. library.yaml is the existing canonical spine.
      Tools should appear in library.yaml as a new section OR as distribution_units with unit_type: tool, NOT as a parallel tools/manifest.yaml.
    amendment: |
      Phase 6 must REPLACE tools/REGISTRY.md and tools/manifest.yaml with:
        - extension of library.yaml under library.tools: with same shape as library.capabilities:
        - new distribution_units entries with unit_type: tool, unit_type: hook
      Phase 6 keeps capabilities/taxonomy.yaml and capabilities/matrix.yaml as those are not yet in library.yaml.
      Phase 6 must add capabilities/, skills/, hooks/, agents/ as new library.yaml sections, NOT as parallel registries.
```

## 4. Substrate stack underspecification (CRITICAL)

```yaml
substrate_stack_correction:
  current_plan_phase_7: "binds Pixeltable + DuckDB"
  gold_goal_actual: "Pixeltable operational substrate -> Arrow/Parquet export -> DuckDB WASM analytical browser surface"
  missing_layer: "Arrow/Parquet export layer + DuckDB WASM browser-side analytical surface"
  why_it_matters: |
    The substrate is not a backend database — it is a multi-tier stack where:
    1. Pixeltable holds tools/tasks/artifacts/events/scorecards (UDFs, computed columns, multimodal)
    2. Arrow/Parquet is the portable export format for cross-system distribution
    3. DuckDB WASM runs IN THE BROWSER as the analytical surface — meaning end users / downstream consumers can query the artifact lake without backend dependencies
    This is also why pixeltable-operational-substrate.md says 'analytics are expected to flow through Arrow or Parquet into DuckDB WASM'.
  amendment: |
    Phase 7 must add:
      - substrate/pixeltable/computed-columns.md (UDFs and computed columns doctrine)
      - substrate/export/arrow-export.md
      - substrate/export/parquet-export.md
      - substrate/duckdb-wasm/browser-surface.md
      - substrate/duckdb-wasm/query-recipes.md
      - substrate/adapters/pixeltable-to-arrow.md
      - substrate/adapters/arrow-to-duckdb-wasm.md
      - substrate/adapters/duckdb-wasm-to-frontend.md
    Phase 7 acceptance must add:
      - 'every Pixeltable table has a documented Arrow export shape'
      - 'every DuckDB WASM query is portable to browser without backend dependency'
```

## 5. Cross-cutting concerns the plan undersells (MEDIUM)

```yaml
cross_cutting_amendments:
  - concern: "Multi-format paired output pattern"
    where: "handoff 1 §A (audio -> txt + json + srt + vtt + tsv + provenance map)"
    plan_says: "stages emit outputs but format unspecified"
    amendment: |
      Phase 4 stage 02 (conversation_capture) must declare the standard transcript artifact family: .txt, .json, .srt, .vtt, .tsv all paired with provenance.json.
      Phase 6 tool-catalog must include a 'transcript_artifact_emitter' tool with this exact output family.
  - concern: "Exact-blocker doctrine"
    where: "agentics-library 'keeps cross-device, provider-backed, sandbox, and browser follow-ons explicitly blocked or gated instead of implying they came alive'"
    plan_says: "blocked_by lists phase IDs"
    amendment: |
      Every blocked_by entry should support either a phase ID OR an exact-blocker string (e.g. 'remote-provider credential X not configured'). Phase 12 should test this.
  - concern: "Dual-artifact rule (machine + markdown)"
    where: "agentics-library 'Structured YAML/JSON artifacts remain machine truth, while ...follow-up-prompt.template.md provides the companion Markdown surface'"
    plan_says: "implied by .plan.md + .plan.json pairing"
    amendment: |
      Phase 1 should add an explicit invariant statement: every governed artifact has both a structured form (YAML or JSON) and a Markdown companion. This is already true of the plan but should be elevated to a contract-level rule.
  - concern: "Existing same-host runtime lane"
    where: "library.yaml jobs: parent-peer-mesh-local-cycle + scripts/run-parent-peer-mesh-local.sh + evaluation/tool-health/peer-mesh-local.json"
    plan_says: "no acknowledgment that a real runtime lane already exists"
    amendment: |
      Phase 12 must add an upstream_ref to evaluation/tool-health/peer-mesh-local.json as the existing live-runtime baseline. Phase 12 acceptance: integration-report must reference this baseline.
```

## 6. Summary delta — what changes if all amendments land

```yaml
delta_summary:
  phases_unchanged: [0, 5, 8, 9, 10, 11]
  phases_amended:
    - phase: 1
      changes:
        - "drop ~7 'new' contracts to 'exists_active'"
        - "add 4 truly new contracts: upstream-handshake, schema-evolution-loop, consume-request, promotion-decision, action-log"
        - "add explicit invariant: every governed artifact has structured + markdown forms"
    - phase: 2
      changes:
        - "add schemas/evidence-strength.schema.json as foundational"
        - "add schemas/operational-feature-matrix.schema.json from handoff 2"
        - "mark 5 compiled-* schemas as exists_active"
        - "add evidence_role enum to artifact-registry schema"
    - phase: 3
      changes:
        - "add contracts/role-families/triad-governance.yaml"
        - "add contracts/role-families/front-door-runtime.yaml"
        - "add contracts/role-families/peer-mesh-runtime.yaml (finalize reference)"
        - "conform to existing schemas/governed-agent-profile.schema.json"
    - phase: 4
      changes:
        - "rename to front_door_lifecycle (12 stages preserved)"
        - "stage 02 declares transcript artifact family (.txt/.json/.srt/.vtt/.tsv + provenance)"
        - "stage 05 references new policies/sensitive-content.yaml before persisting"
    - phase: 6
      changes:
        - "REPLACE tools/REGISTRY.md + tools/manifest.yaml with extension of library.yaml"
        - "consume 8 operational rows from handoff 2 on first emission"
        - "use parent_lane_classification enum"
        - "extend, not regenerate, evaluation/research/compiled/*"
    - phase: 7
      changes:
        - "expand to Pixeltable -> Arrow/Parquet -> DuckDB WASM"
        - "8 new substrate files for the full stack"
        - "acceptance criteria expanded"
    - phase: 12
      changes:
        - "split test_no_governance_runtime_collapse into 3 tests (triad/front-door/peer-mesh pair tests)"
        - "add tests/test_evidence_strength_present.py"
        - "add tests/test_schema_drift_contracts_vs_compiled.py"
        - "reference evaluation/tool-health/peer-mesh-local.json as live-runtime baseline"
  phases_added:
    - phase: "4b"
      name: internal_consume_pipeline
      blocked_by: [1, 3]
      blocks: [5, 11, 12]
      gate: manifest_gate
      stages: 9  # from handoff 1 §B
  total_files_delta:
    plan_v01_count: 154
    plan_v02_estimated: 175
    net_new: 21
    status_reclassifications: 19
```

## 7. Recommended next move

```yaml
next_move:
  option_a:
    label: emit_plan_v02
    action: "Architect emits inbox/consuming-layer.plan.md@v0.2.0 with all amendments merged."
    pro: "Single source of truth; council reviews one document."
    con: "Big single artifact; harder to review in pieces."
  option_b:
    label: emit_per_phase_amendments
    action: "Architect emits one inbox/consuming-layer.phase-N.amendment.md per amended phase."
    pro: "Reviewable in pieces; per-phase council acceptance possible."
    con: "More artifacts to track."
  option_c:
    label: hold_for_council
    action: "Don't amend yet. Wait for council to pick winning candidate first (A vs. unstated B/C)."
    pro: "Avoids amending an artifact that may be deprecated."
    con: "Council can't pick between candidates that have known truth-correction debt."
  recommended: option_a
  rationale: "Truth corrections (§1) are non-controversial. Substrate stack (§4) is in the gold goal. Structural distinctions (§3) are repo facts. Cross-cutting (§5) are inheritance, not invention. Holding until council picks A/B/C while leaving fabrications in §1 unaddressed is the worst path."
```

## 8. Confidence per axis

```yaml
confidence_per_axis:
  truth_corrections: 0.97
  missing_concepts: 0.90
  structural_distinctions: 0.93
  substrate_stack: 0.95
  registry_reconciliation: 0.88
  cross_cutting: 0.85
  overall_recommendation_confidence: 0.91
```

## 9. What I did NOT do (deliberately)

```yaml
deliberate_omissions:
  - "did not edit consuming-layer.plan.md in place — that's the council's call"
  - "did not draft Candidate B or C — those are separate council inputs"
  - "did not run inbox_router.py — that's the next-iteration owner's call"
  - "did not promote any artifact — readiness/promotion is orchestrator-validator's call"
  - "did not assume the council will accept all amendments — each is independently rejectable"
```

---bottom-matter---
validation_status: "pending_council_review"
status_summary:
  completeness: 0.91
  confidence: high
  doc_state: "governed_inbox_packet_review_checkpoint"
gate_progress:
  - gate_id: harvest_gate
    status: green
    notes: "All six reviewed files consumed; cross-references resolved."
  - gate_id: registry_gate
    status: green
    notes: "Existing contract/schema/script inventory confirmed against library.yaml."
  - gate_id: manifest_gate
    status: amber
    notes: "Amendments enumerated but not authored as separate files."
  - gate_id: verification_gate
    status: amber
    notes: "Awaiting council acceptance of which amendments land."
  - gate_id: state_gate
    status: amber
    notes: "Substrate stack correction requires Phase 7 file additions, not yet authored."
  - gate_id: health_gate
    status: green
    notes: "Review is self-contained and cites all sources."
  - gate_id: promotion_gate
    status: red
    notes: "Cannot promote review until amendments are accepted or rejected."
open_questions:
  - "Council: option A (emit v0.2.0) vs. option B (per-phase amendments) vs. option C (hold)?"
  - "Do the 6 proposed-but-not-authored scripts in handoff 1 §F get promoted via agent-extension-request, or do they remain proposals?"
  - "Should the 8 operational matrix rows from handoff 2 §1 be merged into contracts/capability-matrix.yaml directly, or kept as a separate operational-feature-matrix artifact?"
  - "DuckDB WASM browser surface — is there an existing UI consumer planned, or is the substrate exported speculatively?"
pending_validations:
  - "Validate every 'exists' claim in §1 by inspecting the repo (architect)."
  - "Confirm the 9-stage consume pipeline and the 12-stage front-door lifecycle are genuinely distinct, not redundant (architect)."
promotion_criteria:
  - "Council picks one of option A/B/C."
  - "If A or B, architect emits the amended artifact(s)."
  - "Validator re-runs cleanly on the amended plan."
blocked_by:
  - "Council acceptance of one of the three next-move options."
next_iteration:
  owner: "architect"
  objective: "Choose between option A/B/C and emit the corresponding amendment artifact(s). If A, produce consuming-layer.plan.md@v0.2.0. If B, produce one .amendment.md per affected phase."
