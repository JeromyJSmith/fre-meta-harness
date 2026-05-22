---
prompt_schema_version: "1.0"
prompt_id: "PROMPT-20260521-PREFLIGHTSTEP0"
artifact_id: "PACKET-20260521-PREFLIGHTSTEP0PROMPT"
artifact_type: ".prompt.md"
artifact_class: "prompt_candidate"
candidate_label: "Preflight-Step-0"
target_agent: "user-facing-agent"
producer_role: "architect"
target_scope: "portable_parent_wrapper"
repo_root: "/Volumes/PixelTable/VW_iTWIN_Bridge/meta"
parent_only: true
structured_contract_ref: "agent-heavy-run-prompt.schema.json"
companion_markdown_ref: "inbox/prompt-candidate-Preflight-Step-0.prompt.md"
mode:
  execution_style: "heavy_bounded_run"
  autonomy: "medium"
  permission_model: "ask_when_blocked"
mission: >
  Perform the Preflight + Step-0 pass for the FRE Meta-Harness / Super Agentic
  Meta-Harness wrapper layer at /Volumes/PixelTable/VW_iTWIN_Bridge/meta.
  Audit current state, ingest every new inbox artifact, determine
  committed/dirty/undefined/missing-research surfaces, plan the canonical
  filesystem organization for an ICM-style fractal substrate, define the
  predefined feature-worktree promotion criteria that allow features to
  traverse RED -> Development -> Production -> main, and emit the governed
  Step-0 artifact bundle. Do NOT begin implementation work yet.
current_verified_state:
  six_file_scaffold_present: true
  fre_meta_harness_clone_present: true
  inbox_first_protocol_landed: true
  triad_governance_landed: true
  front_door_runtime_topology_landed: true
  same_host_peer_mesh_runtime_active: true
  cross_device_peer_mesh_runtime: "blocked_explicitly"
  pixeltable_substrate: "doctrine_present_live_tables_not_claimed"
  duckdb_wasm_browser_surface: "gold_goal_unimplemented"
  council_candidate_A_present: "inbox/consuming-layer.plan.md"
  council_candidate_review_present: "inbox/consuming-layer.plan.review.checkpoint.md"
  council_decision_status: "not_yet_made"
  red_folder: "does_not_yet_exist_as_governed_surface"
  development_folder: "does_not_yet_exist_as_governed_surface"
  production_folder: "does_not_yet_exist_as_governed_surface"
hard_rules:
  - "parent_only: stay strictly inside /Volumes/PixelTable/VW_iTWIN_Bridge/meta"
  - "external_authorities_read_only: never edit anything under external/"
  - "icm_not_ifc: the substrate vocabulary is Interpreted Context Methodology (arxiv 2603.16021), never IFC"
  - "project_agnostic_wrapper: this is the FRE Meta-Harness, do not reference any specific consumer project (no Lattice, no VW, no iTwin) in the wrapper artifacts"
  - "no_fake_green: validator-backed proof required for every gate-green claim"
  - "no_governance_runtime_collapse: triad governs, front-door intakes, peer-mesh runs; never merge permissions across families"
  - "no_three_framings_collapse: this layer is simultaneously system + subsystem + wrapper; preserve all three in every artifact"
  - "inbox_first: every actionable artifact enters via inbox/ as a governed packet (front matter + body + bottom matter); chat-only narration is not proof"
  - "prompt_before_payload: emit upstream-prepare-to-consume before any payload push; wait for upstream-readiness-ack"
  - "dual_artifact: every governed artifact has a structured form (YAML/JSON) and a Markdown companion"
  - "evidence_strength_required: every extracted claim labelled transcript_only | transcript_plus_context_summary | task_capture_without_terminal_frames | task_stub_without_terminal_frames | terminal_or_frame_verified"
  - "parent_lane_classification_required: every capability classified core | gated | deployment_specific | reference | blocked_with_exact_dependency"
  - "exact_blocker_doctrine: every blocker names the exact missing artifact/configuration, never approximate"
  - "library_yaml_is_the_spine: extend library.yaml, never fork a parallel registry"
  - "infranodus_at_every_gate: live MCP optional, bounded local substitute mandatory at every lifecycle gate transition"
  - "single_file_agents_first: IndieDevDan-style single-file agent pattern is the atomic shippable unit; agents compose into pipelines compose into workflows compose into ETL chains; fractal"
  - "agent_to_agent_pi_mesh_is_prerequisite_for_red: nothing promotes to RED until same-host peer-mesh is confirmed active and cross-device prerequisites are explicitly green-OR-explicitly-blocked-with-exact-dependency"
  - "no_premature_implementation: this prompt covers Preflight + Step-0 only; do not begin Phase 1+ work in this run"
allowed_paths:
  - "/Volumes/PixelTable/VW_iTWIN_Bridge/meta/**"
disallowed_paths:
  - "/Volumes/PixelTable/VW_iTWIN_Bridge/meta/external/**"
  - "anything outside /Volumes/PixelTable/VW_iTWIN_Bridge/meta"
required_reads:
  - "README.md"
  - "AGENTS.md"
  - "CLAUDE.md"
  - "GOAL.md"
  - "GOLDENPATH.md"
  - "MEMORY.md"
  - "program.md"
  - "library.yaml"
  - "agentics-library.md"
  - "body-registry.yaml"
  - "gold-goals.md"
  - "pixeltable-operational-substrate.md"
  - "agent-heavy-run-prompt-schema.md"
  - "agent-heavy-run-prompt.schema.json"
  - "agent-heavy-run-prompt-index.md"
  - "copilot-prompting-playbook.md"
  - "contracts/inbox-packet.yaml"
  - "contracts/inbox-routing-decision.yaml"
  - "contracts/delegation-bundle.yaml"
  - "contracts/front-door-runtime-topology.yaml"
  - "contracts/recursive-documentation-bundle.yaml"
  - "contracts/three-agent-topology.yaml"
  - "contracts/agent-role-contract.yaml"
  - "contracts/agent-extension-request.yaml"
  - "contracts/capability-matrix.yaml"
  - "contracts/research-packet-manifest.yaml"
  - "contracts/peer-mesh.yaml"
  - "contracts/peer-mesh-runtime.yaml"
  - "contracts/peer-message.yaml"
  - "contracts/peer-lifecycle.yaml"
  - "contracts/observability-event.yaml"
  - "contracts/observability-ingest.yaml"
  - "contracts/benchmark-emission.yaml"
  - "contracts/policy-decision.yaml"
  - "contracts/library-distribution.yaml"
  - "contracts/hook-manifest.yaml"
  - "contracts/parent-capability-metrics.yaml"
  - "contracts/agent-eval-parent-lane.yaml"
  - "schemas/front-matter.schema.json"
  - "schemas/bottom-matter.schema.json"
  - "schemas/iteration-record.schema.json"
  - "schemas/copilot-ratchet-report.schema.json"
  - "schemas/governed-agent-profile.schema.json"
  - "schemas/compiled-capability-harvest.schema.json"
  - "schemas/compiled-feature-matrix.schema.json"
  - "schemas/gap-placement-map.schema.json"
  - "schemas/source-index.schema.json"
  - "scripts/watchers/inbox_router.py"
  - "scripts/score-parent-wrapper.py"
  - "scripts/run-parent-peer-mesh-local.sh"
  - "evaluation/tool-health/status.json"
  - "evaluation/tool-health/local-runners.json"
  - "evaluation/tool-health/peer-mesh-local.json"
  - "evaluation/research/compiled/capability-harvest.json"
  - "evaluation/research/compiled/feature-matrix.json"
  - "evaluation/research/compiled/gap-placement-map.json"
  - "evaluation/research/compiled/source-index.json"
  - "evaluation/metrics-latest.json"
  - "evaluation/copilot-ratchet-report.json"
  - "promotion/readiness.json"
  - "runs/iterations.jsonl"
  - "infranodus-phase-tool-map.json"
  - "inbox/consuming-layer.plan.md"
  - "inbox/consuming-layer.plan.json"
  - "inbox/consuming-layer.plan.review.checkpoint.md"
  - "inbox/FRE-META-HARNESS_PLAN.plan.md"
  - "inbox/fre-meta-harness_plus_inbox.plan.md"
  - "inbox/transcribe.consume/file-system-consume.md"
  - "inbox/transcribe.consume/prompt-candidate-consumption.md"
  - "inbox/file-system-structure-research.consume/2603.16021v2.pdf"
  - "inbox/prompting-tools.consume/"
  - "outbox/2026-05-21-pipeline-ideas-and-implementation.handoff.md"
  - "outbox/2026-05-21-operational-capability-matrix-and-schemas.handoff.md"
tasks:
  - id: T1
    name: "preflight_repo_state_audit"
    description: >
      Walk every directory under repo_root (excluding external/), inventorying
      every file with: relative_path, kind (scaffold | contract | schema |
      example | expected_failure | test | evaluation | promotion | source |
      prompt | protocol | script | doc | other), git_status (committed | dirty
      | untracked | staged), front_matter_present (bool), bottom_matter_present
      (bool), schema_ref (if any), conformance (pass | fail | n/a). Emit as
      structured artifact.
    blocked_by: []
  - id: T2
    name: "inbox_consumption_inventory"
    description: >
      For every artifact in inbox/ (recursing into .consume/ subdirectories),
      emit: artifact_id, packet_class (.plan.md | .checkpoint.md | .brainstorm.md
      | .handoff.md | .spec.md | .analysis.md | .prompt.md | raw_consume),
      producer_role_claimed, routing_status (unrouted | routing_emitted |
      delegated | promoted | blocked), evidence_strength, parent_lane_intent.
      Capture sidecar pairings (.plan.md + .plan.json etc.) explicitly.
    blocked_by: [T1]
  - id: T3
    name: "council_candidate_review_status"
    description: >
      For each existing council candidate (currently only
      inbox/consuming-layer.plan.md @ candidate A), report: candidate_id,
      candidate_name, confidence_self_reported, review_packets_against_it,
      truth_correction_count_pending, missing_concepts_count_pending,
      structural_distinctions_count_pending, council_decision (pending |
      accepted | rejected | merged_with_X), next_iteration_owner.
    blocked_by: [T2]
  - id: T4
    name: "research_gaps_and_undefined_surfaces"
    description: >
      Enumerate (a) every surface referenced by upstream artifacts that does
      not yet exist on disk, (b) every concept named in the inbox .consume
      directories without a contract/schema home, (c) every gate referenced
      with no validator-backed proof, (d) every capability claim in
      capability-harvest.json without evidence. Output as a research_backlog
      with researchId, question, whyItMatters, method, successCriteria,
      deliverable, timebox per item.
    blocked_by: [T2]
  - id: T5
    name: "icm_filesystem_topology_proposal"
    description: >
      Propose the canonical fractal filesystem organization following ICM's
      five-layer hierarchy (Layer 0 identity / Layer 1 routing /
      Layer 2 stage-contract / Layer 3 reference factory / Layer 4 working
      product), explicitly mapped to the FRE Meta-Harness vocabulary
      (six-file scaffold + seven-part proof package + seven-gate lifecycle).
      Identify each section of the meta-harness and sub-harnesses, name its
      root, name its scaffold filenames, name its proof-package directory
      family, and show how subdivisions nest fractally. The proposal must
      stay project-agnostic and must preserve the three framings
      (system / subsystem / wrapper) at every level.
    blocked_by: [T1, T4]
  - id: T6
    name: "promotion_pipeline_RED_to_main_design"
    description: >
      Design the predefined feature-worktree promotion pipeline:
      RED (Capabilities / Tools / Feature worktrees, stages from Consumption
      to Green) -> DEVELOPMENT (green capabilities composed into workflows,
      ETL, multi-stage scripts; single-file-agents composed into
      pipeline-agents) -> PRODUCTION (loops, self-improvement, evaluation,
      manifest registration, library binding, schema validation, role
      assignment) -> main. For each transition emit: promotion_criteria,
      validator_commands, required_evidence_artifacts, required_role,
      blocker_classes_supported, rollback_protocol. Use Pixeltable as the
      durable substrate and InfraNodus as the comparison engine at every
      gate.
    blocked_by: [T5]
  - id: T7
    name: "prerequisites_before_RED"
    description: >
      Enumerate every prerequisite that must be green (or explicitly blocked
      with exact dependency) BEFORE any feature is promoted into RED.
      Include: (a) agent-to-agent communication protocol with Raspberry Pi
      peer mesh (Pi-to-Pi), (b) single-file-agent harness (IndieDevDan
      pattern) installed and validated, (c) inbox watcher running and emitting
      routing decisions, (d) Pixeltable substrate adapter at least at
      filesystem-mirror level, (e) InfraNodus phase-tool-map present and
      tool-health refresh completed, (f) governed prompt contract bound, (g)
      iteration ledger initialized, (h) triad role contracts complete, (i)
      front-door role contracts complete, (j) policy gates active for
      sensitive-content handling. Per item: status, exact_blocker_if_any,
      evidence_artifact, owner.
    blocked_by: [T1, T6]
  - id: T8
    name: "capability_harvest_and_matrix_with_phase_priority"
    description: >
      Harvest every capability claim in the repo (library.yaml capabilities,
      contracts/capability-matrix.yaml, evaluation/research/compiled/
      capability-harvest.json, distribution_units in library.yaml, plus
      operational rows proposed in outbox/2026-05-21-operational-capability-
      matrix-and-schemas.handoff.md). Reconcile duplicates. For each
      capability emit: capability_id, parent_surface_type, native_support
      (native | partial | composed | planned), evidence_refs,
      parent_lane_classification, exact_blocker_if_any, assigned_phase
      (0..12+), assigned_priority (P0 | P1 | P2 | P3), promotion_target
      (capability | tool | pipeline | workflow | ETL), upstream_dependencies,
      downstream_consumers. Output as schemas/operational-feature-matrix
      conformant artifact.
    blocked_by: [T5, T7]
  - id: T9
    name: "feature_worktree_definitions"
    description: >
      Define the predefined feature worktree scaffolds. Each worktree is a
      branch-like surface that a candidate feature enters as RED and traverses
      to GREEN. Per worktree definition emit: worktree_id, scope_definition,
      RED_entry_criteria, GREEN_exit_criteria, intermediate_stage_gates,
      required_artifacts_at_each_stage, validator_commands_per_stage,
      escalation_protocol, abandon_protocol. Define enough worktree templates
      to cover the capability classes surfaced in T8.
    blocked_by: [T8]
  - id: T10
    name: "step_0_artifact_bundle_emission"
    description: >
      Emit the governed Step-0 artifact bundle into inbox/ as paired
      packets. The bundle MUST include:
        - inbox/preflight-state-audit.analysis.md (+ .json sidecar)
        - inbox/inbox-consumption-inventory.analysis.md (+ .json sidecar)
        - inbox/council-candidate-status.checkpoint.md (+ .json sidecar)
        - inbox/research-gaps.spec.md (+ .json sidecar)
        - inbox/filesystem-topology-proposal.plan.md (+ .plan.json sidecar)
        - inbox/promotion-pipeline-design.plan.md (+ .plan.json sidecar)
        - inbox/prerequisites-before-red.spec.md (+ .json sidecar)
        - inbox/capability-harvest-matrix.analysis.md (+ .json sidecar conforming to schemas/operational-feature-matrix.schema.json)
        - inbox/feature-worktree-definitions.spec.md (+ .json sidecar)
      Every packet must carry front matter + body + bottom matter, route
      through inbox_router.py, and emit at least one routing decision per
      packet. Do not author files outside inbox/ in this run.
    blocked_by: [T1, T2, T3, T4, T5, T6, T7, T8, T9]
  - id: T11
    name: "validator_loop_run"
    description: >
      Run the parent validator loop end-to-end, capturing real outputs (no
      dry-run). Commands: (1) uv run python scripts/watchers/inbox_router.py
      (2) uv run --isolated --with jsonschema --with pyyaml python tests/
      validate_parent_wrapper_contract.py (3) uv run --isolated --with
      jsonschema --with pyyaml python scripts/score-parent-wrapper.py --json
      (4) git --no-pager diff --check. Append at least two non-dry iteration
      ledger rows to runs/iterations.jsonl. Refresh evaluation/metrics-
      latest.json, evaluation/copilot-ratchet-report.json, and
      promotion/readiness.json.
    blocked_by: [T10]
  - id: T12
    name: "final_report"
    description: >
      Emit the run report conforming to report_contract below. Do not declare
      Step-0 GREEN unless every preceding task succeeded with validator-backed
      proof. If any subtask is blocked, declare the run BLOCKED with the
      exact_blocker string.
    blocked_by: [T11]
validation_loop:
  loop_id: "preflight_step_0_loop"
  commands:
    - "uv run python scripts/watchers/inbox_router.py"
    - "uv run --isolated --with jsonschema --with pyyaml python tests/validate_parent_wrapper_contract.py"
    - "uv run --isolated --with jsonschema --with pyyaml python scripts/score-parent-wrapper.py --json"
    - "git --no-pager diff --check"
  required_non_dry_cycles: 2
  instrument_repair_on_saturation: true
  fail_loud: true
success_criteria:
  - "Every Task T1..T12 reports status=completed or status=blocked with exact_blocker."
  - "Every Step-0 artifact in T10 exists, is YAML-valid, conforms to its schema, and has been routed by inbox_router.py with a structured routing decision emitted to evaluation/tool-health/inbox-protocol/."
  - "validate_parent_wrapper_contract.py exits 0."
  - "score-parent-wrapper.py reports non-decreasing score vs. previous baseline OR provides instrument-repair evidence per program.md hard rules."
  - "runs/iterations.jsonl has at least 2 new non-dry iteration rows for this run."
  - "promotion/readiness.json status == pass OR status == blocked with exact_blocker[]."
  - "No file outside /Volumes/PixelTable/VW_iTWIN_Bridge/meta has been touched."
  - "No file under external/ has been edited."
  - "The Capability Harvest Matrix in T8 covers every capability surface (library.yaml + contracts/capability-matrix.yaml + evaluation/research/compiled/capability-harvest.json + handoff operational rows) with no orphans."
  - "Prerequisites-before-RED list in T7 marks each item green OR blocked-with-exact-dependency."
  - "Feature worktree definitions in T9 cover every capability class in T8."
report_contract:
  required_fields:
    - "status"
    - "preflight_audit_summary"
    - "inbox_inventory_summary"
    - "council_candidate_status_summary"
    - "research_backlog_summary"
    - "filesystem_topology_proposal_summary"
    - "promotion_pipeline_summary"
    - "prerequisites_before_red_status"
    - "capability_harvest_matrix_summary"
    - "feature_worktree_definitions_summary"
    - "artifacts_emitted"
    - "routing_decisions_emitted"
    - "delegation_bundles_emitted"
    - "validator_result"
    - "scorer_result"
    - "iterations_appended"
    - "metrics_latest_path"
    - "readiness_status"
    - "files_changed"
    - "exact_blocker_if_any"
    - "next_iteration_owner"
    - "next_iteration_objective"
upstream_refs:
  - "inbox/consuming-layer.plan.md"
  - "inbox/consuming-layer.plan.review.checkpoint.md"
  - "inbox/FRE-META-HARNESS_PLAN.plan.md"
  - "inbox/fre-meta-harness_plus_inbox.plan.md"
  - "outbox/2026-05-21-pipeline-ideas-and-implementation.handoff.md"
  - "outbox/2026-05-21-operational-capability-matrix-and-schemas.handoff.md"
external_authority_refs:
  - "https://arxiv.org/abs/2603.16021 (Interpreted Context Methodology — Van Clief & McDermott)"
  - "external/goal-md/"
  - "external/meta-harness/"
  - "external/autoresearch-mlx/"
routing_tags:
  - "preflight"
  - "step-0"
  - "filesystem-topology"
  - "promotion-pipeline"
  - "capability-harvest"
  - "feature-worktrees"
  - "prerequisites-before-red"
  - "council-stage-candidate"
required_consumers:
  - "user-facing-agent"
  - "filesystem-router"
  - "orchestrator-validator"
  - "architect"
  - "research"
created_at: "2026-05-21T00:00:00Z"
updated_at: "2026-05-21T00:00:00Z"
---

# Preflight + Step-0 — FRE Meta-Harness / Super Agentic Meta-Harness

## 0. What this prompt is and what it is not

This is a **council-stage prompt candidate**, labelled `Preflight-Step-0`,
emitted into `inbox/` as a `.prompt.md` artifact. It is **not** the first
major triad prompt; the triad emits that artifact downstream of this one,
after the council picks (or merges) the prompt candidates on the table.

This prompt drives the **Preflight + Step-0 pass** for the wrapper layer at
`/Volumes/PixelTable/VW_iTWIN_Bridge/meta`. Preflight + Step-0 covers
**organization and readiness only** — no Phase 1+ implementation work happens
in this run.

When fed into a fresh session, the receiving agent (`user-facing-agent`) must
behave exactly as described by the structured fields above and the prose
below. Structured fields are machine truth; this prose is the operator-facing
companion (dual-artifact rule).

## 1. The system you are operating inside

You are the front door of the **FRE Meta-Harness** — Fractal Research
Engineering — a **Super Agentic Meta-Harness** wrapper. The wrapper is
**project-agnostic**. It can be attached to any sub-harness as a host AND
as a guest at the same boundary. Three framings must never collapse:

- It **is** a self-governed system.
- It **is** a subsystem of `github.com/JeromyJSmith/fre-meta-harness`.
- It **wraps** an FRE sub-harness (attaches via `body-registry.yaml`).

The substrate vocabulary is **Interpreted Context Methodology (ICM)** —
Van Clief & McDermott, arxiv 2603.16021. Five-layer hierarchy:
**Layer 0 identity / Layer 1 routing / Layer 2 stage-contract /
Layer 3 reference (the factory) / Layer 4 working artifact (the product)**.
ICM is the grammar; the FRE seven-gate lifecycle + seven-part proof package +
six-file scaffold are the enforcement.

## 2. The downstream pipeline you are organizing for

Information flows up the wrapper like sap up a tree. The root sucks
nutrients (research, applications, builds, design documentation). Each
layer prepares the next layer to receive (prompts flow upstream first via
`upstream-prepare-to-consume`; only after `upstream-readiness-ack` does
payload move). Every consume cycle refactors the schemas, registers new
modular tools, and recursively pushes refactored building blocks upward.

The promotion ladder is:

```
DOWNSTREAM  -->  RED  -->  DEVELOPMENT  -->  PRODUCTION  -->  main
```

- **DOWNSTREAM:** raw consumption — `.consume/` directories, transcript
  intake, repo ingestion, web capture, design-doc ingestion. Output:
  packets routed through `inbox/`.

- **RED:** capabilities, tools, and feature worktrees in early-stage
  development. Every capability traverses sub-stages from raw consumption
  toward GREEN. RED is where building blocks live in their unproven form.
  Promotion criteria from DOWNSTREAM to RED include the prerequisites
  enumerated in Task T7.

- **DEVELOPMENT:** GREEN capabilities get linked together to form a
  workflow, perform a full operation; once an operation completes
  successfully, the matrix entries become building blocks. This is where
  workflow composition happens — single-file-agents call other single-file-
  agents call tools. This is the **fractal** layer. **InfraNodus is used
  heavily here** to inspect how capabilities connect and where the graph
  is weak. Capabilities that turn GREEN get promoted to tools; tools get
  linked into pipelines, ETL chains, multi-stage scripts.

- **PRODUCTION:** the manifest layer. Self-improvement loops, evaluation,
  schema registration, library binding (`library.yaml`), role assignment,
  manifest verification, library entry, and final test. Only after all
  PRODUCTION criteria pass does an artifact push to `main`.

## 3. Prerequisites BEFORE RED (the "below the root" check)

Nothing promotes from DOWNSTREAM to RED until each item below is GREEN
or explicitly blocked-with-exact-dependency:

1. **Agent-to-agent communication protocol with Pi peer mesh.** Pi-to-Pi
   communication contracts (`contracts/peer-mesh.yaml`,
   `contracts/peer-message.yaml`, `contracts/peer-lifecycle.yaml`,
   `contracts/peer-mesh-runtime.yaml`) bound; same-host slice active per
   `scripts/run-parent-peer-mesh-local.sh` and
   `evaluation/tool-health/peer-mesh-local.json`; cross-device slice green
   OR explicitly blocked.

2. **IndieDevDan single-file-agent harness.** The single-file-agent
   pattern installed, validated, registered in `library.yaml`
   distribution_units as `unit_type: agent`. Single-file-agents are the
   atomic shippable unit; they compose into pipeline-agents which compose
   into workflows which compose into ETL chains. Fractal.

3. **Inbox watcher running and emitting routing decisions.**
   `scripts/watchers/inbox_router.py` running; every inbox packet produces
   an `inbox-routing-decision.yaml` and `delegation-bundle.yaml` artifact.

4. **Pixeltable substrate adapter at filesystem-mirror level.** Even if
   live Pixeltable tables are not yet bound, the filesystem layout must be
   shaped for later Arrow/Parquet export into Pixeltable, and from
   Pixeltable into DuckDB WASM browser-side analytical surface.

5. **InfraNodus phase-tool-map present and refreshed.**
   `infranodus-phase-tool-map.json` resolved per gate; tool-health refresh
   completed; bounded local InfraNodus substitute available when live MCP
   is not configured.

6. **Governed prompt contract bound.** Every heavy/bounded prompt the
   wrapper emits conforms to `agent-heavy-run-prompt.schema.json` —
   including this very prompt.

7. **Iteration ledger initialized.** `runs/iterations.jsonl` exists,
   schema-valid per `schemas/iteration-record.schema.json`.

8. **Triad role contracts complete.** `orchestrator-validator`, `research`,
   `architect` role contracts authored and validated against
   `schemas/governed-agent-profile.schema.json`.

9. **Front-door role contracts complete.** `user-facing-agent`,
   `spec-interpreter`, `intake-mapper`, `semantic-cartographer`,
   `filesystem-router`, `wrapper-synthesizer` role contracts present.

10. **Policy gates active for sensitive-content handling.** Trauma-safe
    intake, redaction policy, sensitive-content classifier present and
    referenced by front-door stages that touch raw transcripts or PII.

T7 must enumerate each of these items with: status, exact_blocker_if_any,
evidence_artifact, owner.

## 4. The capability-harvest matrix you must produce in T8

Reconcile every capability source in the repo into a single matrix.
Sources to harvest from:

- `library.yaml` — `library.capabilities` section
- `contracts/capability-matrix.yaml`
- `evaluation/research/compiled/capability-harvest.json`
- `evaluation/research/compiled/feature-matrix.json`
- `evaluation/research/compiled/gap-placement-map.json`
- `library.yaml` — `distribution_units` (each unit is a capability claim)
- `outbox/2026-05-21-operational-capability-matrix-and-schemas.handoff.md`
  §1 (8 operational rows)
- `inbox/prompting-tools.consume/` — Tool Catalog, Capability Harvesting
  Matrix, Schema Set, Spec Compiler, Pixeltable/DuckDB, Policy+Gates,
  Observability+Evaluation, Artifact Registry

Per capability row, emit:

```yaml
capability_id: "<kebab-case-id>"
parent_surface_type: "<one of: communication_plane | distribution_plane | policy_plane | observability_plane | browser_validation | sandbox_execution | device_sidecar | arbitration_lane | substrate_plane | governance_plane>"
native_support: "<native | partial | composed | planned>"
evidence_refs: ["<paths>"]
parent_lane_classification: "<core | gated | deployment_specific | reference | blocked_with_exact_dependency>"
exact_blocker_if_any: "<string or null>"
assigned_phase: "<0..12+>"
assigned_priority: "<P0 | P1 | P2 | P3>"
promotion_target: "<capability | tool | pipeline | workflow | ETL>"
upstream_dependencies: ["<capability_id>"]
downstream_consumers: ["<capability_id>"]
evidence_strength: "<transcript_only | transcript_plus_context_summary | task_capture_without_terminal_frames | task_stub_without_terminal_frames | terminal_or_frame_verified>"
```

Output: `inbox/capability-harvest-matrix.analysis.md` paired with a
`.json` sidecar conforming to
`schemas/operational-feature-matrix.schema.json`.

The matrix is the source of truth for which capabilities enter RED in
which phase and at which priority. The council uses this matrix to make
the cut.

## 5. Feature worktree definitions (T9)

Feature worktrees are predefined branch-like surfaces that a candidate
feature enters as RED and traverses to GREEN. Each worktree carries:

- `worktree_id`
- `scope_definition` (what classes of feature it accepts)
- `RED_entry_criteria` (capability matrix row + prerequisites check)
- `intermediate_stage_gates` (per-stage exit criteria)
- `GREEN_exit_criteria` (validator-backed proof)
- `required_artifacts_at_each_stage`
- `validator_commands_per_stage`
- `escalation_protocol` (how to escalate a stuck worktree to triad)
- `abandon_protocol` (how to declare a worktree dead and capture
  learnings)

Define enough worktree templates to cover the capability classes in T8.
Typical templates:

- `feature-worktree.single-file-agent`
- `feature-worktree.pipeline-composition`
- `feature-worktree.tool-promotion`
- `feature-worktree.contract-authoring`
- `feature-worktree.schema-evolution`
- `feature-worktree.substrate-adapter`
- `feature-worktree.policy-bundle`
- `feature-worktree.observability-integration`

## 6. ICM filesystem topology you must propose in T5

Use ICM's five-layer hierarchy as the substrate. At every fractal level
the FRE six-file scaffold must be present. Identify every meta-harness
section and every sub-harness section the wrapper must host. Name root,
scaffold filenames, proof-package directory family, and how subdivisions
nest. Propose explicit homes for:

- inbox / outbox / cache / evidence / graph / memory / relationships /
  runs (already exist as `.gitkeep` placeholders — define their shape)
- contracts/ and contracts/roles/ and contracts/role-families/
- schemas/ and examples/ and expected-failures/
- stages/ (front-door 12-stage lifecycle) and pipelines/ (internal
  consume pipeline) — these are TWO DIFFERENT pipelines that must not be
  collapsed
- tools/ (or `library.tools:` section in `library.yaml` — pick one
  spine; do NOT fork)
- skills/, hooks/, agents/ (single-file-agents)
- capabilities/ (taxonomy + matrix)
- policies/ and gates/
- observability/
- substrate/ (Pixeltable, Arrow/Parquet, DuckDB WASM)
- compiler/
- protocols/ (upstream flow, recursive refactor, three-framings
  non-collapse)
- prompts/ (governed templates)
- evaluation/, promotion/, source/
- worktrees/RED/, worktrees/DEVELOPMENT/, worktrees/PRODUCTION/

The proposal must stay project-agnostic — name no specific consumer.

## 7. What you write and where (T10)

All Step-0 artifacts go into `inbox/` as paired packets. Do NOT author
files outside `inbox/` in this run. Each packet has a Markdown form and a
structured sidecar. Every packet conforms to `contracts/inbox-packet.yaml`
and routes through `scripts/watchers/inbox_router.py`.

The bundle:

```
inbox/preflight-state-audit.analysis.md           + .analysis.json
inbox/inbox-consumption-inventory.analysis.md     + .analysis.json
inbox/council-candidate-status.checkpoint.md      + .checkpoint.json
inbox/research-gaps.spec.md                       + .spec.json
inbox/filesystem-topology-proposal.plan.md        + .plan.json
inbox/promotion-pipeline-design.plan.md           + .plan.json
inbox/prerequisites-before-red.spec.md            + .spec.json
inbox/capability-harvest-matrix.analysis.md       + .analysis.json
inbox/feature-worktree-definitions.spec.md        + .spec.json
```

Every packet must carry full front matter, body, and bottom matter
(seven `gate_progress` entries, `status_summary`, `promotion_criteria`,
`blocked_by`, `next_iteration`).

## 8. Hard NO's

- Do not write code yet. Contracts, schemas, plans, registries, matrices,
  and analyses only.
- Do not edit anything under `external/`.
- Do not edit anything outside `/Volumes/PixelTable/VW_iTWIN_Bridge/meta`.
- Do not author files outside `inbox/` during this run.
- Do not promote any artifact. Only `orchestrator-validator` may promote.
- Do not call this run GREEN unless every success criterion above is met
  with validator-backed proof.
- Do not collapse triad, front-door, and peer-mesh role families.
- Do not collapse system, subsystem, and wrapper framings.
- Do not refer to this wrapper by any specific consumer project name.
- Do not use "IFC" or any synonym. The substrate is **ICM**.

## 9. Reporting

Emit a final report following `report_contract` above. If any task is
blocked, declare the run BLOCKED with an exact_blocker string. Do not
inflate completeness. Trust the validator output literally. Append the
iteration ledger row with `cycle_kind: real_non_dry`.

## 10. Why this prompt exists

The previous run produced two council candidates already in inbox/:

- `consuming-layer.plan.md` (Candidate A, "Roots-First Consuming Lattice
  v2", confidence 0.92 council-stage seed)
- `consuming-layer.plan.review.checkpoint.md` (Candidate A audit with 19
  truth-correction tags pending)

But the wrapper has never had a unified Preflight + Step-0 pass. Without
one, the council is voting on candidates that may be misaligned with the
actual current state of disk. This prompt fixes that: it produces the
ground-truth Step-0 bundle so the next council round has facts, not
narration.

After this prompt completes, the triad will have:

1. A real preflight audit of every file.
2. A real inbox inventory.
3. A real council candidate review status.
4. A research backlog with exact gaps.
5. A canonical ICM filesystem topology proposal.
6. A RED-through-main promotion pipeline design.
7. A prerequisites-before-RED status list.
8. A reconciled capability harvest matrix with phase + priority
   assignments.
9. Predefined feature worktree templates.
10. Validator-backed proof of the run.

Only then is the council ready to pick (or merge) the prompt candidates
and emit the first major triad prompt.

---bottom-matter---
validation_status: "pending_council_routing"
status_summary:
  completeness: 0.90
  confidence: high
  doc_state: "governed_prompt_candidate"
gate_progress:
  - gate_id: harvest_gate
    status: green
    notes: "All required reads enumerated; upstream and external authority refs explicit."
  - gate_id: registry_gate
    status: amber
    notes: "Prompt registry entry pending — promotion to prompts/ awaits council acceptance."
  - gate_id: manifest_gate
    status: amber
    notes: "Tasks T1..T12 declared but not yet executed; manifest of emitted artifacts will populate on T10/T12."
  - gate_id: verification_gate
    status: amber
    notes: "Validator loop declared; not yet run."
  - gate_id: state_gate
    status: amber
    notes: "Iteration ledger row pending; metrics refresh pending."
  - gate_id: health_gate
    status: green
    notes: "Self-contained; cites all sources; no external dependencies beyond declared authorities."
  - gate_id: promotion_gate
    status: red
    notes: "Prompt is candidate stage. Promotion to prompts/ requires explicit council acceptance and inbox routing decision."
open_questions:
  - "Council: accept this prompt as the Preflight-Step-0 driver, request amendments, or replace with a sibling candidate?"
  - "Should the prompt also bind the previously-unbuilt schemas/operational-feature-matrix.schema.json explicitly as a prerequisite of T8, or accept that T8 emits the artifact even when the schema is still drafty?"
  - "Cross-device Pi peer mesh — accept the current 'blocked_explicitly' state as a prerequisite-met-via-exact-blocker, or require it to be GREEN before any feature enters RED?"
  - "Single-file-agent harness (IndieDevDan pattern) — confirm canonical reference doc and pin to a specific commit for reproducibility?"
pending_validations:
  - "Validate this prompt against agent-heavy-run-prompt.schema.json."
  - "Route this prompt through inbox_router.py; confirm a routing decision is emitted."
  - "Confirm every path under required_reads exists and is readable."
promotion_criteria:
  - "Council accepts the prompt as the Preflight-Step-0 driver."
  - "Inbox watcher emits routing decision."
  - "First execution against this prompt completes with all 12 tasks reporting status."
  - "Validator and scorer pass on the resulting Step-0 bundle."
blocked_by:
  - "Council acceptance pending."
next_iteration:
  owner: "orchestrator-validator"
  objective: "Classify this prompt candidate, route it via inbox_router.py, and if accepted, dispatch to user-facing-agent for execution. If amendments are requested, emit a .checkpoint.md against this prompt rather than rewriting it in place."
