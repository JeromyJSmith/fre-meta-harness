---
id: "packet-consuming-layer-phased-implementation"
slug: "consuming-layer-phased-implementation"
doctype: "inbox_packet"
status: "ready_for_routing"
version: "0.1.0"
owner: "fre-meta-harness"
artifact_id: "PACKET-20260521-CONSUMINGLAYER"
artifact_type: ".plan.md"
producer_role: "architect"
target_scope: "portable_parent_wrapper"
repo_root: "/Volumes/PixelTable/VW_iTWIN_Bridge/meta"
parent_only: true
structured_contract_ref: "contracts/inbox-packet.yaml"
structured_artifact_ref: "inbox/consuming-layer.plan.json"
prompt_candidate_class: "council_stage_candidate_A"
routing_tags:
  - "inbox-first"
  - "front-door"
  - "consuming-layer"
  - "recursive-documentation"
  - "phased-plan"
  - "blocking-graph"
  - "schema-evolution"
  - "upstream-handshake"
required_consumers:
  - "filesystem-router"
  - "architect"
  - "orchestrator-validator"
  - "research"
upstream_refs:
  - "inbox/FRE-META-HARNESS_PLAN.plan.md"
  - "inbox/fre-meta-harness_plus_inbox.plan.md"
  - "inbox/transcribe.consume/file-system-consume.md"
  - "inbox/transcribe.consume/prompt-candidate-consumption.md"
  - "inbox/file-system-structure-research.consume/2603.16021v2.pdf"
  - "inbox/prompting-tools.consume/"
evidence_refs:
  - "CLAUDE.md"
  - "AGENTS.md"
  - "README.md"
  - "GOAL.md"
  - "GOLDENPATH.md"
  - "MEMORY.md"
  - "program.md"
  - "library.yaml"
  - "agentics-library.md"
  - "body-registry.yaml"
  - "contracts/inbox-packet.yaml"
  - "contracts/inbox-routing-decision.yaml"
  - "contracts/delegation-bundle.yaml"
  - "contracts/front-door-runtime-topology.yaml"
  - "contracts/recursive-documentation-bundle.yaml"
  - "contracts/capability-matrix.yaml"
  - "contracts/three-agent-topology.yaml"
  - "scripts/watchers/inbox_router.py"
  - "schemas/front-matter.schema.json"
  - "schemas/bottom-matter.schema.json"
  - "schemas/iteration-record.schema.json"
  - "schemas/copilot-ratchet-report.schema.json"
  - "agent-heavy-run-prompt.schema.json"
external_authority_refs:
  - "external/goal-md/"
  - "external/meta-harness/"
  - "external/autoresearch-mlx/"
  - "https://arxiv.org/abs/2603.16021"
  - "https://github.com/JeromyJSmith/fre-meta-harness"
created_at: "2026-05-21T00:00:00Z"
updated_at: "2026-05-21T00:00:00Z"
---

# Plan: Consuming Layer for fre-meta-harness — Phased Implementation

## 0. How this file is meant to be consumed

This packet is **not** the first major prompt to the triad. It is a council-stage
candidate that, once approved, becomes the routing source for the triad to emit
their own governed prompts against. The consumption order is:

```yaml
consumption_order:
  - step: 1
    actor: orchestrator-validator
    action: classify_packet_against_contract
    expected_output: contracts/inbox-routing-decision.yaml instance
  - step: 2
    actor: filesystem-router
    action: emit_delegation_bundles_per_phase
    expected_output: contracts/delegation-bundle.yaml instances under runs/
  - step: 3
    actor: architect
    action: review_blocking_graph_for_cycles_and_realism
    expected_output: review note appended to evaluation/architect-review.md
  - step: 4
    actor: research
    action: confirm_evidence_refs_are_real_and_current
    expected_output: evaluation/research-evidence-audit.md
  - step: 5
    actor: triad
    action: keep_or_block
    expected_output: promotion/readiness.json refreshed
```

Each phase below declares its own `blocked_by` and `blocks` arrays. A phase may
only enter `in_progress` when every `blocked_by` phase reads `completed`. Within
a phase, individual files declare their own `blocked_by` / `blocks` against
sibling files. The whole structure is a DAG; cycles are a validator failure.

The prompt candidate that produced this plan is quoted in §1. The first major
triad prompt is **not** in this file — it is the artifact the triad emits
after consuming this packet through the inbox router.

## 1. Prompt Candidate A (council stage, refined v2)

> Role: You are the architect of a consuming connector layer sitting at
> `/Volumes/PixelTable/VW_iTWIN_Bridge/meta/`, downstream of fre-meta-harness.
> Your layer is a root system, not a leaf. Research, applications, builds, and
> design docs enter at the tips, get analyzed (relationship + entity + semantic),
> get schematized, get refactored into modular tools, then offered upstream
> only after the upstream tier signals readiness.
>
> Three non-collapsible framings: this layer **is** a self-governed system, **is**
> a subsystem of fre-meta-harness, and **wraps** an FRE sub-harness — host-shaped
> and guest-shaped at the same boundary.
>
> Communication invariant: prompts flow upstream first
> (`upstream-prepare-to-consume`). Upstream acknowledges
> (`upstream-readiness-ack`). Only then does payload flow. Each tier consumes →
> analyzes → schematizes → refactors → re-advertises readiness.
>
> Inbox-first protocol: every artifact enters via `inbox/` as a governed packet
> (front matter + body + bottom matter). `scripts/watchers/inbox_router.py` emits
> routing decisions and delegation bundles. No chat-only proof.
>
> Governance separation: triad (`orchestrator-validator`, `research`, `architect`)
> governs; front-door runtime (`user-facing-agent`, `spec-interpreter`,
> `filesystem-router`, `intake-mapper`, `semantic-cartographer`,
> `wrapper-synthesizer`) executes intake; peer-mesh runtime executes downstream
> consume cycles. Never collapse the three.
>
> Substrate doctrine: Pixeltable is the durable artifact lake; DuckDB is the
> query surface. Every artifact carries `runId`, `correlationId`, `provenance`,
> `schemaRef`. Filesystem and Pixeltable are dual-written.
>
> Compliance with fre-meta-harness: six-file fractal scaffold at every level;
> seven-gate lifecycle; seven-part proof package; governed prompt contract;
> `library.yaml` spine; `body-registry.yaml` attachment; iteration ledger;
> strict naming.
>
> Scope: NOT a tech stack. Filesystem topology, contract family, schema-evolution
> loop, tool-modularity registry — that is all.

## 2. Phase graph at a glance

```yaml
phases:
  - id: 0
    name: conformance_baseline
    blocked_by: []
    blocks: [1, 2]
    gate: harvest_gate
  - id: 1
    name: inbox_first_contract_family
    blocked_by: [0]
    blocks: [3, 4, 5, 6, 11]
    gate: registry_gate
  - id: 2
    name: schemas_artifact_registry
    blocked_by: [0]
    blocks: [3, 6, 7, 8, 9, 10]
    gate: registry_gate
  - id: 3
    name: front_door_runtime_role_contracts
    blocked_by: [1, 2]
    blocks: [4, 11]
    gate: manifest_gate
  - id: 4
    name: consuming_lifecycle_stages
    blocked_by: [1, 3]
    blocks: [5, 12]
    gate: manifest_gate
  - id: 5
    name: upstream_prompt_flow_protocol
    blocked_by: [1, 4]
    blocks: [11, 12]
    gate: verification_gate
  - id: 6
    name: tool_catalog_capability_matrix
    blocked_by: [1, 2]
    blocks: [7, 8, 10, 11]
    gate: registry_gate
  - id: 7
    name: pixeltable_duckdb_substrate
    blocked_by: [2, 6]
    blocks: [9, 12]
    gate: state_gate
  - id: 8
    name: policy_gates_trust_plane
    blocked_by: [2, 6]
    blocks: [10, 12]
    gate: verification_gate
  - id: 9
    name: observability_evaluation_measure_plane
    blocked_by: [2, 7]
    blocks: [10, 12]
    gate: health_gate
  - id: 10
    name: spec_compiler
    blocked_by: [2, 6, 8, 9]
    blocks: [12]
    gate: verification_gate
  - id: 11
    name: recursive_upstream_refactor_protocol
    blocked_by: [1, 3, 5, 6]
    blocks: [12]
    gate: state_gate
  - id: 12
    name: integration_proof_and_promotion
    blocked_by: [4, 5, 7, 8, 9, 10, 11]
    blocks: []
    gate: promotion_gate
```

Gates align to fre-meta-harness seven-gate lifecycle. Each phase must satisfy
its gate before the validator will mark `gate_progress[*].status: green`.

## 3. Phase 0 — Conformance baseline

Rationale: nothing else may begin until the six-file fractal scaffold, the
front/bottom matter, the seven gates, the seven-part proof package, and the
validator are all already green at the wrapper root. Most of this is already
done at `meta/`; this phase is *audit*, not creation, with creation only for
gaps surfaced by the audit.

```yaml
phase_0:
  id: 0
  name: conformance_baseline
  status: pending
  blocked_by: []
  blocks: [1, 2]
  gate: harvest_gate
  rationale: >
    The wrapper must conform to fre-meta-harness before extending it.
    Audit-first; create only what audit shows missing.
  files:
    - path: README.md
      kind: scaffold_six_file
      rule: front_matter_and_bottom_matter_required
      blocked_by: []
      blocks: [AGENTS.md, CLAUDE.md, GOAL.md, GOLDENPATH.md, MEMORY.md]
    - path: AGENTS.md
      kind: scaffold_six_file
      rule: front_matter_and_bottom_matter_required
      blocked_by: [README.md]
      blocks: []
    - path: CLAUDE.md
      kind: scaffold_six_file
      rule: front_matter_and_bottom_matter_required
      blocked_by: [README.md]
      blocks: []
    - path: GOAL.md
      kind: scaffold_six_file
      rule: includes_metric_mutability_block
      blocked_by: [README.md]
      blocks: []
    - path: GOLDENPATH.md
      kind: scaffold_six_file
      rule: includes_parent_child_flow_section
      blocked_by: [README.md]
      blocks: []
    - path: MEMORY.md
      kind: scaffold_six_file
      rule: includes_fractal_levels_clause
      blocked_by: [README.md]
      blocks: []
    - path: program.md
      kind: ratchet_protocol
      rule: setup_then_mutable_surface_then_loop_then_report
      blocked_by: []
      blocks: []
    - path: library.yaml
      kind: spine_catalog
      rule: prompts_capabilities_references_jobs_keys_present
      blocked_by: []
      blocks: []
    - path: body-registry.yaml
      kind: attachment_surface
      rule: this_wrapper_registered_as_body_or_parent
      blocked_by: []
      blocks: []
    - path: source/
      kind: proof_package_part
      rule: directory_exists_with_provenance_json
      blocked_by: []
      blocks: []
    - path: schemas/
      kind: proof_package_part
      rule: directory_exists_with_existing_four_schemas
      blocked_by: []
      blocks: []
    - path: examples/
      kind: proof_package_part
      rule: directory_exists_with_valid_and_invalid_pairs
      blocked_by: []
      blocks: []
    - path: expected-failures/
      kind: proof_package_part
      rule: directory_exists_with_registry_yaml
      blocked_by: []
      blocks: []
    - path: tests/
      kind: proof_package_part
      rule: directory_exists_with_validate_parent_wrapper_contract_py
      blocked_by: []
      blocks: []
    - path: evaluation/
      kind: proof_package_part
      rule: directory_exists_with_validation_report_json
      blocked_by: []
      blocks: []
    - path: promotion/
      kind: proof_package_part
      rule: directory_exists_with_readiness_json
      blocked_by: []
      blocks: []
  validator_commands:
    - "uv run --isolated --with jsonschema --with pyyaml python tests/validate_parent_wrapper_contract.py"
    - "uv run --isolated --with jsonschema --with pyyaml python scripts/score-parent-wrapper.py --json"
    - "git --no-pager diff --check"
  acceptance:
    - "validator emits pass with all seven gates green"
    - "scorer emits non-decreasing score vs. previous baseline"
    - "no uncommitted whitespace dirt"
    - "promotion/readiness.json status == pass"
```

## 4. Phase 1 — Inbox-first contract family

Rationale: the inbox-first protocol is the load-bearing front door. Several
contracts already exist (`inbox-packet.yaml`, `inbox-routing-decision.yaml`,
`delegation-bundle.yaml`, `front-door-runtime-topology.yaml`,
`recursive-documentation-bundle.yaml`, `capability-matrix.yaml`,
`three-agent-topology.yaml`). The remainder need to be authored. The
`upstream-handshake.yaml` and `schema-evolution-loop.yaml` are NEW and are the
heart of the tree-roots-drinking-water metaphor.

```yaml
phase_1:
  id: 1
  name: inbox_first_contract_family
  status: pending
  blocked_by: [0]
  blocks: [3, 4, 5, 6, 11]
  gate: registry_gate
  files:
    - path: contracts/inbox-packet.yaml
      kind: contract
      status: exists_finalize
      rule: declares_required_fields_for_packet_envelope
      blocked_by: []
      blocks: [contracts/inbox-routing-decision.yaml, contracts/delegation-bundle.yaml]
    - path: contracts/inbox-routing-decision.yaml
      kind: contract
      status: exists_finalize
      rule: declares_routing_modes_single_fanout_chain_blocked_escalation
      blocked_by: [contracts/inbox-packet.yaml]
      blocks: [contracts/delegation-bundle.yaml]
    - path: contracts/delegation-bundle.yaml
      kind: contract
      status: exists_finalize
      rule: declares_consumer_role_evidence_refs_and_payload_pointer
      blocked_by: [contracts/inbox-routing-decision.yaml]
      blocks: []
    - path: contracts/front-door-runtime-topology.yaml
      kind: contract
      status: exists_finalize
      rule: enumerates_six_front_door_roles_and_boundaries
      blocked_by: []
      blocks: [contracts/roles/]
    - path: contracts/recursive-documentation-bundle.yaml
      kind: contract
      status: exists_finalize
      rule: declares_per_subdivision_doc_pairing_rule
      blocked_by: []
      blocks: []
    - path: contracts/capability-matrix.yaml
      kind: contract
      status: exists_finalize
      rule: declares_capability_planes_communication_distribution_policy_observability_browser_sandbox_device
      blocked_by: []
      blocks: [capabilities/]
    - path: contracts/three-agent-topology.yaml
      kind: contract
      status: exists_finalize
      rule: declares_triad_role_boundaries
      blocked_by: []
      blocks: []
    - path: contracts/agent-role-contract.yaml
      kind: contract
      status: new
      rule: declares_role_purpose_inputs_outputs_permissions_tools_skills_hooks_escalation_handoff
      blocked_by: [contracts/three-agent-topology.yaml, contracts/front-door-runtime-topology.yaml]
      blocks: [contracts/roles/]
    - path: contracts/agent-extension-request.yaml
      kind: contract
      status: new
      rule: declares_governed_self_extension_request_envelope
      blocked_by: [contracts/agent-role-contract.yaml]
      blocks: []
    - path: contracts/upstream-handshake.yaml
      kind: contract
      status: new
      rule: declares_prepare_to_consume_then_readiness_ack_then_payload_push
      blocked_by: [contracts/inbox-packet.yaml]
      blocks: [protocols/upstream-flow.md, schemas/upstream-handshake.schema.json]
    - path: contracts/schema-evolution-loop.yaml
      kind: contract
      status: new
      rule: declares_consume_analyze_schematize_refactor_offer_upstream_loop
      blocked_by: [contracts/upstream-handshake.yaml]
      blocks: [protocols/recursive-upstream-refactor.md]
    - path: contracts/consume-request.yaml
      kind: contract
      status: new
      rule: declares_downstream_payload_envelope_with_provenance_and_schema_ref
      blocked_by: [contracts/inbox-packet.yaml]
      blocks: []
    - path: contracts/promotion-decision.yaml
      kind: contract
      status: new
      rule: declares_keep_revert_promote_with_evidence_chain
      blocked_by: [contracts/inbox-packet.yaml]
      blocks: []
    - path: contracts/action-log.yaml
      kind: contract
      status: new
      rule: declares_event_envelope_for_every_action
      blocked_by: []
      blocks: [schemas/action-log.schema.json]
  validator_commands:
    - "uv run python scripts/watchers/inbox_router.py --dry-run --packet inbox/consuming-layer.plan.md"
    - "uv run --isolated --with pyyaml python tests/validate_contract_family.py"
  acceptance:
    - "every contract file present and YAML-valid"
    - "no cycle in contract blocks-graph"
    - "every contract referenced has at least one consumer named"
```

## 5. Phase 2 — Schemas, the artifact registry

Rationale: action-log is foundational — everything else depends on it. The
schemas implement the contracts authored in Phase 1, plus the artifact registry
from the prompting-tools.consume directory.

```yaml
phase_2:
  id: 2
  name: schemas_artifact_registry
  status: pending
  blocked_by: [0]
  blocks: [3, 6, 7, 8, 9, 10, 12]
  gate: registry_gate
  files:
    - path: schemas/action-log.schema.json
      kind: schema
      status: new
      rule: foundational_event_envelope
      blocked_by: []
      blocks: [schemas/run-log.schema.json, observability/event-envelope.schema.json]
    - path: schemas/artifact-registry.schema.json
      kind: schema
      status: new
      rule: enumerates_every_artifact_kind_with_owner_and_validator
      blocked_by: [schemas/action-log.schema.json]
      blocks: [tools/REGISTRY.md]
    - path: schemas/inbox-packet.schema.json
      kind: schema
      status: new
      rule: machine_validates_inbox_packet_yaml
      blocked_by: [contracts/inbox-packet.yaml]
      blocks: []
    - path: schemas/inbox-routing-decision.schema.json
      kind: schema
      status: new
      rule: machine_validates_routing_decision_yaml
      blocked_by: [contracts/inbox-routing-decision.yaml]
      blocks: []
    - path: schemas/delegation-bundle.schema.json
      kind: schema
      status: new
      rule: machine_validates_delegation_bundle_yaml
      blocked_by: [contracts/delegation-bundle.yaml]
      blocks: []
    - path: schemas/upstream-handshake.schema.json
      kind: schema
      status: new
      rule: machine_validates_prepare_to_consume_and_readiness_ack
      blocked_by: [contracts/upstream-handshake.yaml]
      blocks: []
    - path: schemas/consume-request.schema.json
      kind: schema
      status: new
      rule: machine_validates_payload_envelope
      blocked_by: [contracts/consume-request.yaml]
      blocks: []
    - path: schemas/run-log.schema.json
      kind: schema
      status: new
      rule: machine_validates_per_run_summary
      blocked_by: [schemas/action-log.schema.json]
      blocks: []
    - path: schemas/plan.schema.json
      kind: schema
      status: new
      rule: machine_validates_packet_plan_md_class
      blocked_by: []
      blocks: []
    - path: schemas/report.schema.json
      kind: schema
      status: new
      rule: machine_validates_governed_report_artifact
      blocked_by: []
      blocks: []
    - path: schemas/tool.schema.json
      kind: schema
      status: new
      rule: ToolSpec_machine_contract
      blocked_by: [schemas/artifact-registry.schema.json]
      blocks: [tools/manifest.yaml]
    - path: schemas/tool-ability.schema.json
      kind: schema
      status: new
      blocked_by: [schemas/tool.schema.json]
      blocks: []
    - path: schemas/skill.schema.json
      kind: schema
      status: new
      blocked_by: [schemas/tool.schema.json]
      blocks: [skills/REGISTRY.md]
    - path: schemas/agent.schema.json
      kind: schema
      status: new
      blocked_by: [contracts/agent-role-contract.yaml]
      blocks: [agents/REGISTRY.md]
    - path: schemas/single-file-agent.schema.json
      kind: schema
      status: new
      blocked_by: [schemas/agent.schema.json]
      blocks: []
    - path: schemas/hook.schema.json
      kind: schema
      status: new
      blocked_by: [schemas/tool.schema.json]
      blocks: [hooks/REGISTRY.md]
    - path: schemas/capability.schema.json
      kind: schema
      status: new
      blocked_by: []
      blocks: [capabilities/taxonomy.yaml]
    - path: schemas/capability-manifest.schema.json
      kind: schema
      status: new
      blocked_by: [schemas/capability.schema.json]
      blocks: []
    - path: schemas/capability-matrix.schema.json
      kind: schema
      status: new
      blocked_by: [schemas/capability.schema.json, contracts/capability-matrix.yaml]
      blocks: [capabilities/matrix.yaml]
    - path: schemas/capability-harvest.schema.json
      kind: schema
      status: new
      blocked_by: [schemas/capability-matrix.schema.json]
      blocks: []
    - path: schemas/lifecycle-gates.schema.json
      kind: schema
      status: new
      rule: enforces_seven_gate_ids_and_red_amber_green_enum
      blocked_by: []
      blocks: []
    - path: schemas/proof-package.schema.json
      kind: schema
      status: new
      rule: enforces_seven_part_directory_family
      blocked_by: []
      blocks: []
    - path: schemas/infranodus-tool.schema.json
      kind: schema
      status: new
      blocked_by: [schemas/tool.schema.json]
      blocks: []
    - path: schemas/promotion-decision.schema.json
      kind: schema
      status: new
      blocked_by: [contracts/promotion-decision.yaml]
      blocks: []
  validator_commands:
    - "uv run --isolated --with jsonschema python -c 'import json,jsonschema,glob; [jsonschema.Draft202012Validator.check_schema(json.load(open(f))) for f in glob.glob(\"schemas/*.schema.json\")]'"
    - "uv run --isolated --with jsonschema --with pyyaml python tests/validate_schema_set.py"
  acceptance:
    - "every schema is valid JSON Schema 2020-12"
    - "every schema has at least one valid example under examples/"
    - "every schema has at least one invalid example under expected-failures/"
    - "schemas/artifact-registry.schema.json lists every other schema as an artifact kind"
```

## 6. Phase 3 — Front-door runtime role contracts

Rationale: the six front-door roles are named in
`contracts/front-door-runtime-topology.yaml` but each needs its own role contract
following the `agent-role-contract.yaml` shape (purpose, inputs, outputs,
permissions, tools, skills, hooks, escalation, handoff).

```yaml
phase_3:
  id: 3
  name: front_door_runtime_role_contracts
  status: pending
  blocked_by: [1, 2]
  blocks: [4, 11]
  gate: manifest_gate
  files:
    - path: contracts/roles/user-facing-agent.yaml
      kind: role_contract
      status: new
      rule: conversational_intake_and_clarification_only_no_self_certification
      blocked_by: [contracts/agent-role-contract.yaml]
      blocks: [stages/01-project_attach/CONTEXT.md, stages/02-conversation_capture/CONTEXT.md, stages/04-user_confirmation/CONTEXT.md]
    - path: contracts/roles/spec-interpreter.yaml
      kind: role_contract
      status: new
      rule: structures_meaning_from_conversation_no_approval
      blocked_by: [contracts/agent-role-contract.yaml]
      blocks: [stages/03-spec_interpretation/CONTEXT.md]
    - path: contracts/roles/intake-mapper.yaml
      kind: role_contract
      status: new
      rule: maps_content_to_artifact_kinds_and_consumers
      blocked_by: [contracts/agent-role-contract.yaml]
      blocks: [stages/05-drop_ingest/CONTEXT.md, stages/06-content_inventory/CONTEXT.md]
    - path: contracts/roles/semantic-cartographer.yaml
      kind: role_contract
      status: new
      rule: performs_entity_relationship_and_semantic_analysis
      blocked_by: [contracts/agent-role-contract.yaml]
      blocks: [stages/07-semantic_map/CONTEXT.md]
    - path: contracts/roles/filesystem-router.yaml
      kind: role_contract
      status: new
      rule: watches_inbox_validates_envelopes_emits_routing_decisions
      blocked_by: [contracts/agent-role-contract.yaml, contracts/inbox-routing-decision.yaml]
      blocks: []
    - path: contracts/roles/wrapper-synthesizer.yaml
      kind: role_contract
      status: new
      rule: late_bound_consumer_synthesizes_wrapper_from_subsystem_registry
      blocked_by: [contracts/agent-role-contract.yaml]
      blocks: [stages/09-wrapper_binding/CONTEXT.md]
    - path: contracts/roles/triad-orchestrator-validator.yaml
      kind: role_contract
      status: new
      rule: governs_keep_or_block_decisions_not_intake
      blocked_by: [contracts/agent-role-contract.yaml, contracts/three-agent-topology.yaml]
      blocks: [stages/11-triad_review/CONTEXT.md, stages/12-promotion_or_block/CONTEXT.md]
    - path: contracts/roles/triad-architect.yaml
      kind: role_contract
      status: new
      rule: shapes_contracts_prompts_and_handoff_artifacts
      blocked_by: [contracts/agent-role-contract.yaml, contracts/three-agent-topology.yaml]
      blocks: []
    - path: contracts/roles/triad-research.yaml
      kind: role_contract
      status: new
      rule: gathers_bounded_evidence_and_dependency_truth
      blocked_by: [contracts/agent-role-contract.yaml, contracts/three-agent-topology.yaml]
      blocks: []
  validator_commands:
    - "uv run --isolated --with jsonschema --with pyyaml python tests/validate_role_contracts.py"
  acceptance:
    - "every role contract conforms to schemas/agent.schema.json"
    - "no role contract grants both governance and runtime permissions"
    - "every front-door role explicitly forbids self-promotion"
    - "every triad role explicitly forbids conversational intake"
```

## 7. Phase 4 — Consuming lifecycle stages

Rationale: the 12-stage lifecycle from `FRE-META-HARNESS_PLAN.plan.md`
materializes as twelve numbered stage directories, each with its own
CONTEXT.md (ICM-style three-section: Inputs / Process / Outputs). This is the
concrete consume-cycle.

```yaml
phase_4:
  id: 4
  name: consuming_lifecycle_stages
  status: pending
  blocked_by: [1, 3]
  blocks: [5, 12]
  gate: manifest_gate
  files:
    - path: stages/01-project_attach/CONTEXT.md
      kind: stage_contract
      status: new
      rule: inputs_process_outputs_three_section
      blocked_by: [contracts/roles/user-facing-agent.yaml]
      blocks: [stages/02-conversation_capture/CONTEXT.md]
      owner: user-facing-agent
    - path: stages/02-conversation_capture/CONTEXT.md
      kind: stage_contract
      status: new
      blocked_by: [stages/01-project_attach/CONTEXT.md]
      blocks: [stages/03-spec_interpretation/CONTEXT.md]
      owner: user-facing-agent
    - path: stages/03-spec_interpretation/CONTEXT.md
      kind: stage_contract
      status: new
      blocked_by: [stages/02-conversation_capture/CONTEXT.md, contracts/roles/spec-interpreter.yaml]
      blocks: [stages/04-user_confirmation/CONTEXT.md]
      owner: spec-interpreter
    - path: stages/04-user_confirmation/CONTEXT.md
      kind: stage_contract
      status: new
      rule: human_review_gate_required
      blocked_by: [stages/03-spec_interpretation/CONTEXT.md]
      blocks: [stages/05-drop_ingest/CONTEXT.md]
      owner: user-facing-agent
    - path: stages/05-drop_ingest/CONTEXT.md
      kind: stage_contract
      status: new
      blocked_by: [stages/04-user_confirmation/CONTEXT.md, contracts/roles/intake-mapper.yaml]
      blocks: [stages/06-content_inventory/CONTEXT.md]
      owner: intake-mapper
    - path: stages/06-content_inventory/CONTEXT.md
      kind: stage_contract
      status: new
      blocked_by: [stages/05-drop_ingest/CONTEXT.md]
      blocks: [stages/07-semantic_map/CONTEXT.md]
      owner: intake-mapper
    - path: stages/07-semantic_map/CONTEXT.md
      kind: stage_contract
      status: new
      rule: emits_entity_graph_relationship_graph_and_semantic_clusters
      blocked_by: [stages/06-content_inventory/CONTEXT.md, contracts/roles/semantic-cartographer.yaml]
      blocks: [stages/08-subsystem_registry/CONTEXT.md]
      owner: semantic-cartographer
    - path: stages/08-subsystem_registry/CONTEXT.md
      kind: stage_contract
      status: new
      rule: registers_modular_blocks_for_wrapping
      blocked_by: [stages/07-semantic_map/CONTEXT.md]
      blocks: [stages/09-wrapper_binding/CONTEXT.md]
      owner: semantic-cartographer
    - path: stages/09-wrapper_binding/CONTEXT.md
      kind: stage_contract
      status: new
      blocked_by: [stages/08-subsystem_registry/CONTEXT.md, contracts/roles/wrapper-synthesizer.yaml]
      blocks: [stages/10-improvement_queue/CONTEXT.md]
      owner: wrapper-synthesizer
    - path: stages/10-improvement_queue/CONTEXT.md
      kind: stage_contract
      status: new
      blocked_by: [stages/09-wrapper_binding/CONTEXT.md]
      blocks: [stages/11-triad_review/CONTEXT.md]
      owner: filesystem-router
    - path: stages/11-triad_review/CONTEXT.md
      kind: stage_contract
      status: new
      rule: triad_keep_or_block_decision_required
      blocked_by: [stages/10-improvement_queue/CONTEXT.md, contracts/roles/triad-orchestrator-validator.yaml]
      blocks: [stages/12-promotion_or_block/CONTEXT.md]
      owner: orchestrator-validator
    - path: stages/12-promotion_or_block/CONTEXT.md
      kind: stage_contract
      status: new
      blocked_by: [stages/11-triad_review/CONTEXT.md, contracts/promotion-decision.yaml]
      blocks: []
      owner: orchestrator-validator
  validator_commands:
    - "uv run --isolated --with pyyaml python tests/validate_stage_contracts.py"
  acceptance:
    - "every stage CONTEXT.md has exactly three sections: ## Inputs / ## Process / ## Outputs"
    - "every stage names exactly one owner role"
    - "stages form a linear DAG (n blocks n+1, no skipping)"
    - "stages reference inbox protocol at every cross-stage handoff"
```

## 8. Phase 5 — Upstream prompt-flow protocol

Rationale: this is the load-bearing addition the user described — prompts flow
upstream first ("prepare to consume"), upstream restructures and acknowledges,
then payload flows. This phase makes that machine-readable.

```yaml
phase_5:
  id: 5
  name: upstream_prompt_flow_protocol
  status: pending
  blocked_by: [1, 4]
  blocks: [11, 12]
  gate: verification_gate
  files:
    - path: protocols/upstream-flow.md
      kind: protocol
      status: new
      rule: defines_prepare_then_ack_then_payload_state_machine
      blocked_by: [contracts/upstream-handshake.yaml]
      blocks: [prompts/upstream-prepare-to-consume.template.md]
    - path: prompts/upstream-prepare-to-consume.template.md
      kind: prompt_template
      status: new
      rule: governed_prompt_contract_compliant
      blocked_by: [protocols/upstream-flow.md, agent-heavy-run-prompt.schema.json]
      blocks: []
    - path: prompts/upstream-readiness-ack.template.md
      kind: prompt_template
      status: new
      rule: governed_prompt_contract_compliant
      blocked_by: [prompts/upstream-prepare-to-consume.template.md]
      blocks: []
    - path: prompts/upstream-schema-refactor-request.template.md
      kind: prompt_template
      status: new
      rule: requests_upstream_to_restructure_schemas_for_incoming_payload
      blocked_by: [prompts/upstream-readiness-ack.template.md]
      blocks: []
    - path: prompts/downstream-payload-push.template.md
      kind: prompt_template
      status: new
      rule: emitted_only_after_readiness_ack
      blocked_by: [prompts/upstream-schema-refactor-request.template.md]
      blocks: []
    - path: protocols/upstream-flow-state-machine.yaml
      kind: protocol
      status: new
      rule: enumerates_states_idle_preparing_ready_consuming_refactoring_offering_promoted_blocked
      blocked_by: [protocols/upstream-flow.md]
      blocks: []
    - path: examples/upstream-handshake/prepare-to-consume.valid.json
      kind: example
      status: new
      blocked_by: [schemas/upstream-handshake.schema.json]
      blocks: []
    - path: examples/upstream-handshake/readiness-ack.valid.json
      kind: example
      status: new
      blocked_by: [schemas/upstream-handshake.schema.json]
      blocks: []
    - path: expected-failures/upstream-handshake/payload-before-ack.invalid.json
      kind: expected_failure
      status: new
      blocked_by: [schemas/upstream-handshake.schema.json]
      blocks: []
  validator_commands:
    - "uv run --isolated --with jsonschema --with pyyaml python tests/validate_upstream_flow.py"
  acceptance:
    - "no payload-push template references a destination not first acknowledged"
    - "state machine has no unreachable states"
    - "every prompt template passes agent-heavy-run-prompt.schema.json"
```

## 9. Phase 6 — Tool catalog and capability matrix

Rationale: the registry that turns prompts into versioned tools. Every tool
declares endpoint, schemas, policies, tests, artifacts, Pixeltable persistence.

```yaml
phase_6:
  id: 6
  name: tool_catalog_capability_matrix
  status: pending
  blocked_by: [1, 2]
  blocks: [7, 8, 10, 11]
  gate: registry_gate
  files:
    - path: tools/REGISTRY.md
      kind: registry_index
      status: new
      rule: lists_every_tool_with_id_owner_version_status
      blocked_by: [schemas/tool.schema.json]
      blocks: [tools/manifest.yaml]
    - path: tools/manifest.yaml
      kind: manifest
      status: new
      blocked_by: [tools/REGISTRY.md, schemas/tool.schema.json]
      blocks: []
    - path: capabilities/taxonomy.yaml
      kind: capability_catalog
      status: new
      rule: assigns_stable_ids_CAP_0001_through_CAP_NNNN
      blocked_by: [schemas/capability.schema.json]
      blocks: [capabilities/matrix.yaml]
    - path: capabilities/matrix.yaml
      kind: capability_matrix
      status: new
      rule: maps_tool_or_module_to_capability_claims_with_support_level
      blocked_by: [capabilities/taxonomy.yaml, schemas/capability-matrix.schema.json]
      blocks: [capabilities/gap-report.md]
    - path: capabilities/gap-report.md
      kind: gap_report
      status: new
      rule: lists_capabilities_with_no_native_tool
      blocked_by: [capabilities/matrix.yaml]
      blocks: []
    - path: skills/REGISTRY.md
      kind: registry_index
      status: new
      blocked_by: [schemas/skill.schema.json]
      blocks: []
    - path: hooks/REGISTRY.md
      kind: registry_index
      status: new
      blocked_by: [schemas/hook.schema.json]
      blocks: []
    - path: agents/REGISTRY.md
      kind: registry_index
      status: new
      rule: catalogues_single_file_agents
      blocked_by: [schemas/single-file-agent.schema.json]
      blocks: []
    - path: tools/_template/SKILL.md
      kind: skill_skeleton
      status: new
      rule: drop_in_shippable_skill_unit
      blocked_by: [skills/REGISTRY.md]
      blocks: []
  validator_commands:
    - "uv run --isolated --with jsonschema --with pyyaml python tests/validate_tool_catalog.py"
    - "uv run --isolated --with jsonschema --with pyyaml python tests/validate_capability_matrix.py"
  acceptance:
    - "every tool in manifest declares schemaRef, endpoint, tests, Pixeltable table"
    - "every CAP id is referenced by at least one tool or marked as planned"
    - "gap report flags every CAP with zero native support"
```

## 10. Phase 7 — Pixeltable + DuckDB substrate

Rationale: durable artifact lake with queryable surface. Dual-write filesystem
and Pixeltable; every artifact carries `runId`, `correlationId`, `provenance`,
`schemaRef`.

```yaml
phase_7:
  id: 7
  name: pixeltable_duckdb_substrate
  status: pending
  blocked_by: [2, 6]
  blocks: [9, 12]
  gate: state_gate
  files:
    - path: substrate/pixeltable/tables/tool_specs.yaml
      kind: table_schema
      status: new
      blocked_by: [schemas/tool.schema.json]
      blocks: []
    - path: substrate/pixeltable/tables/agent_cards.yaml
      kind: table_schema
      status: new
      blocked_by: [schemas/agent.schema.json]
      blocks: []
    - path: substrate/pixeltable/tables/tasks.yaml
      kind: table_schema
      status: new
      blocked_by: []
      blocks: []
    - path: substrate/pixeltable/tables/artifacts.yaml
      kind: table_schema
      status: new
      rule: includes_runId_correlationId_provenance_schemaRef
      blocked_by: [schemas/artifact-registry.schema.json]
      blocks: []
    - path: substrate/pixeltable/tables/events.yaml
      kind: table_schema
      status: new
      blocked_by: [schemas/action-log.schema.json]
      blocks: []
    - path: substrate/pixeltable/tables/policies.yaml
      kind: table_schema
      status: new
      blocked_by: []
      blocks: []
    - path: substrate/pixeltable/tables/tests.yaml
      kind: table_schema
      status: new
      blocked_by: []
      blocks: []
    - path: substrate/pixeltable/tables/scorecards.yaml
      kind: table_schema
      status: new
      blocked_by: []
      blocks: []
    - path: substrate/pixeltable/tables/baselines.yaml
      kind: table_schema
      status: new
      blocked_by: []
      blocks: []
    - path: substrate/pixeltable/tables/capability_matrix.yaml
      kind: table_schema
      status: new
      blocked_by: [schemas/capability-matrix.schema.json]
      blocks: []
    - path: substrate/duckdb/queries/run_summary.sql
      kind: query_recipe
      status: new
      blocked_by: [substrate/pixeltable/tables/tasks.yaml]
      blocks: []
    - path: substrate/duckdb/queries/artifact_inventory.sql
      kind: query_recipe
      status: new
      blocked_by: [substrate/pixeltable/tables/artifacts.yaml]
      blocks: []
    - path: substrate/duckdb/queries/policy_violations.sql
      kind: query_recipe
      status: new
      blocked_by: [substrate/pixeltable/tables/policies.yaml]
      blocks: []
    - path: substrate/duckdb/queries/regression_deltas.sql
      kind: query_recipe
      status: new
      blocked_by: [substrate/pixeltable/tables/scorecards.yaml, substrate/pixeltable/tables/baselines.yaml]
      blocks: []
    - path: substrate/adapters/filesystem-to-pixeltable.md
      kind: adapter_spec
      status: new
      rule: dual_write_rule
      blocked_by: []
      blocks: []
    - path: substrate/adapters/pixeltable-export-pack.md
      kind: adapter_spec
      status: new
      blocked_by: [substrate/adapters/filesystem-to-pixeltable.md]
      blocks: []
  validator_commands:
    - "uv run --isolated --with pyyaml python tests/validate_substrate_tables.py"
  acceptance:
    - "every Pixeltable table declares column names matching its schema"
    - "every DuckDB query references only tables that exist"
    - "every artifact-producing workflow names which table it dual-writes to"
```

## 11. Phase 8 — Policy + gates (trust plane)

Rationale: deterministic allow/block/ask, message boundaries, tool boundaries,
completion criteria, loop budgets, plus the 8-gate tool-promotion sequence.

```yaml
phase_8:
  id: 8
  name: policy_gates_trust_plane
  status: pending
  blocked_by: [2, 6]
  blocks: [10, 12]
  gate: verification_gate
  files:
    - path: policies/allow-block-ask.yaml
      kind: policy_bundle
      status: new
      blocked_by: []
      blocks: []
    - path: policies/message-boundary.yaml
      kind: policy_bundle
      status: new
      blocked_by: []
      blocks: []
    - path: policies/tool-boundary.yaml
      kind: policy_bundle
      status: new
      rule: file_access_shell_network_rules
      blocked_by: []
      blocks: []
    - path: policies/completion.yaml
      kind: policy_bundle
      status: new
      rule: done_token_max_turns_max_outbound
      blocked_by: []
      blocks: []
    - path: gates/tool-promotion.yaml
      kind: gate_sequence
      status: new
      rule: enforces_eight_step_sequence_schema_openapi_golden_policy_obs_pixeltable_duckdb_docparity
      blocked_by: [policies/allow-block-ask.yaml]
      blocks: []
    - path: schemas/policy.schema.json
      kind: schema
      status: new
      blocked_by: []
      blocks: []
    - path: schemas/gate-result.schema.json
      kind: schema
      status: new
      blocked_by: []
      blocks: []
  validator_commands:
    - "uv run --isolated --with jsonschema --with pyyaml python tests/validate_policy_bundles.py"
    - "uv run --isolated --with jsonschema --with pyyaml python tests/validate_gate_sequence.py"
  acceptance:
    - "every policy bundle references its enforcing role"
    - "gate sequence has no unreachable step"
    - "no tool can claim active status without passing all 8 gates"
```

## 12. Phase 9 — Observability + evaluation (measure plane)

Rationale: structured event stream, benchmarks, baselines, regressions. No
hidden work; every action emits a typed event.

```yaml
phase_9:
  id: 9
  name: observability_evaluation_measure_plane
  status: pending
  blocked_by: [2, 7]
  blocks: [10, 12]
  gate: health_gate
  files:
    - path: observability/event-envelope.schema.json
      kind: schema
      status: new
      rule: includes_eventId_runId_toolId_correlationId_parentEventId
      blocked_by: [schemas/action-log.schema.json]
      blocks: []
    - path: observability/benchmark-point.schema.json
      kind: schema
      status: new
      blocked_by: [observability/event-envelope.schema.json]
      blocks: []
    - path: observability/scorecard.schema.json
      kind: schema
      status: new
      blocked_by: [observability/benchmark-point.schema.json]
      blocks: []
    - path: observability/correlations.md
      kind: doc
      status: new
      rule: defines_parent_event_id_chain_rules
      blocked_by: [observability/event-envelope.schema.json]
      blocks: []
    - path: evaluation/baselines.md
      kind: doc
      status: new
      blocked_by: [observability/scorecard.schema.json]
      blocks: []
    - path: evaluation/benchmark-groups.yaml
      kind: config
      status: new
      rule: declares_mesh_latency_tool_latency_success_rate_blocks_asks_token_cost_artifact_counts
      blocked_by: [observability/benchmark-point.schema.json]
      blocks: []
  validator_commands:
    - "uv run --isolated --with jsonschema --with pyyaml python tests/validate_observability_schemas.py"
  acceptance:
    - "every governed workflow declares which events it emits"
    - "every benchmark has a target value or explicit 'baseline-only'"
    - "scorecard schema supports regression vs baseline comparison"
```

## 13. Phase 10 — Spec compiler

Rationale: turns the markdown corpus and the registry into enforceable checks.
Outputs `missing.md`, `compliance.md`, `drift.md`.

```yaml
phase_10:
  id: 10
  name: spec_compiler
  status: pending
  blocked_by: [2, 6, 8, 9]
  blocks: [12]
  gate: verification_gate
  files:
    - path: compiler/COMPILER.md
      kind: doc
      status: new
      rule: explains_inputs_and_outputs
      blocked_by: []
      blocks: [compiler/artifact-registry.compiler.md]
    - path: compiler/artifact-registry.compiler.md
      kind: compiler_spec
      status: new
      blocked_by: [compiler/COMPILER.md, schemas/artifact-registry.schema.json]
      blocks: []
    - path: compiler/schemas.compiler.md
      kind: compiler_spec
      status: new
      rule: every_artifact_has_schema_every_schema_has_example_every_example_validates
      blocked_by: [compiler/COMPILER.md]
      blocks: []
    - path: compiler/tools.compiler.md
      kind: compiler_spec
      status: new
      blocked_by: [compiler/COMPILER.md, tools/REGISTRY.md]
      blocks: []
    - path: compiler/skills.compiler.md
      kind: compiler_spec
      status: new
      blocked_by: [compiler/COMPILER.md, skills/REGISTRY.md]
      blocks: []
    - path: compiler/capabilities.compiler.md
      kind: compiler_spec
      status: new
      blocked_by: [compiler/COMPILER.md, capabilities/matrix.yaml]
      blocks: []
    - path: compiler/hooks.compiler.md
      kind: compiler_spec
      status: new
      blocked_by: [compiler/COMPILER.md, hooks/REGISTRY.md]
      blocks: []
    - path: compiler/reports.compiler.md
      kind: compiler_spec
      status: new
      blocked_by: [compiler/COMPILER.md]
      blocks: []
    - path: compiler/plans.compiler.md
      kind: compiler_spec
      status: new
      blocked_by: [compiler/COMPILER.md, schemas/plan.schema.json]
      blocks: []
    - path: compiler/output-styles.compiler.md
      kind: compiler_spec
      status: new
      blocked_by: [compiler/COMPILER.md]
      blocks: []
    - path: compiler/missing.md
      kind: compiler_output_template
      status: new
      blocked_by: [compiler/COMPILER.md]
      blocks: []
    - path: compiler/compliance.md
      kind: compiler_output_template
      status: new
      blocked_by: [compiler/COMPILER.md]
      blocks: []
    - path: compiler/drift.md
      kind: compiler_output_template
      status: new
      blocked_by: [compiler/COMPILER.md]
      blocks: []
  validator_commands:
    - "uv run --isolated --with pyyaml python tests/validate_compiler_specs.py"
  acceptance:
    - "compiler can answer: what artifacts are missing, what schemas are missing, what tools are missing, what changed without a run note, is the golden path still valid, was InfraNodus run or explicitly skipped"
    - "every compiler spec declares its inputs and outputs"
    - "missing.md, compliance.md, drift.md are emitted on every run"
```

## 14. Phase 11 — Recursive upstream refactor protocol

Rationale: the constant-consume-and-refactor-upward loop the user described.
Every consume cycle that produces a new schema or a modular tool triggers a
governed refactor request upstream.

```yaml
phase_11:
  id: 11
  name: recursive_upstream_refactor_protocol
  status: pending
  blocked_by: [1, 3, 5, 6]
  blocks: [12]
  gate: state_gate
  files:
    - path: protocols/recursive-upstream-refactor.md
      kind: protocol
      status: new
      rule: defines_full_consume_analyze_schematize_refactor_offer_loop
      blocked_by: [contracts/schema-evolution-loop.yaml, protocols/upstream-flow.md]
      blocks: [protocols/schema-version-bump-policy.md]
    - path: protocols/schema-version-bump-policy.md
      kind: protocol
      status: new
      rule: declares_when_minor_vs_major_bump_is_required
      blocked_by: [protocols/recursive-upstream-refactor.md]
      blocks: []
    - path: protocols/branches/consuming-branch.md
      kind: protocol
      status: new
      rule: describes_per_consume_cycle_branch_creation
      blocked_by: [protocols/recursive-upstream-refactor.md]
      blocks: [protocols/branches/merge-to-main.md]
    - path: protocols/branches/merge-to-main.md
      kind: protocol
      status: new
      rule: declares_what_must_be_green_before_merge_is_proposed
      blocked_by: [protocols/branches/consuming-branch.md]
      blocks: []
    - path: protocols/tool-database-refactor.md
      kind: protocol
      status: new
      rule: every_repeated_pattern_becomes_a_promoted_tool
      blocked_by: [protocols/recursive-upstream-refactor.md, tools/REGISTRY.md]
      blocks: []
    - path: protocols/three-framings-non-collapse.md
      kind: protocol
      status: new
      rule: declares_system_subsystem_wrapper_must_never_be_collapsed_in_any_artifact
      blocked_by: []
      blocks: []
  validator_commands:
    - "uv run --isolated --with pyyaml python tests/validate_recursive_refactor_protocol.py"
  acceptance:
    - "every consume cycle produces an upstream refactor request artifact"
    - "no merge-to-main happens without all seven gates green"
    - "every promoted tool can be traced to the consume cycle that produced it"
    - "three-framings rule is referenced by every protocol that touches the wrapper boundary"
```

## 15. Phase 12 — Integration proof and promotion

Rationale: the final phase. Runs the full validator, runs the watcher, scores,
emits readiness.json, and produces the integration report. Only when this phase
reads `completed` may the wrapper claim a green operational state.

```yaml
phase_12:
  id: 12
  name: integration_proof_and_promotion
  status: pending
  blocked_by: [4, 5, 7, 8, 9, 10, 11]
  blocks: []
  gate: promotion_gate
  files:
    - path: tests/test_inbox_packet_validates.py
      kind: test
      status: new
      blocked_by: [schemas/inbox-packet.schema.json]
      blocks: []
    - path: tests/test_routing_decision_emits.py
      kind: test
      status: new
      blocked_by: [schemas/inbox-routing-decision.schema.json]
      blocks: []
    - path: tests/test_six_file_scaffold_present.py
      kind: test
      status: new
      blocked_by: []
      blocks: []
    - path: tests/test_seven_gates_resolve.py
      kind: test
      status: new
      blocked_by: [schemas/lifecycle-gates.schema.json]
      blocks: []
    - path: tests/test_upstream_handshake.py
      kind: test
      status: new
      blocked_by: [schemas/upstream-handshake.schema.json]
      blocks: []
    - path: tests/test_consuming_lifecycle_runs.py
      kind: test
      status: new
      blocked_by: [stages/12-promotion_or_block/CONTEXT.md]
      blocks: []
    - path: tests/test_tool_catalog_consistent_with_pixeltable.py
      kind: test
      status: new
      blocked_by: [tools/manifest.yaml, substrate/pixeltable/tables/tool_specs.yaml]
      blocks: []
    - path: tests/test_no_governance_runtime_collapse.py
      kind: test
      status: new
      rule: scans_every_role_contract_for_forbidden_permission_combos
      blocked_by: []
      blocks: []
    - path: tests/test_three_framings_preserved.py
      kind: test
      status: new
      rule: scans_for_any_artifact_that_collapses_system_subsystem_wrapper
      blocked_by: []
      blocks: []
    - path: evaluation/integration-report.md
      kind: report
      status: new
      blocked_by: [tests/test_consuming_lifecycle_runs.py]
      blocks: []
    - path: evaluation/metrics-latest.json
      kind: report
      status: refresh
      blocked_by: [evaluation/integration-report.md]
      blocks: []
    - path: evaluation/copilot-ratchet-report.json
      kind: report
      status: refresh
      blocked_by: [evaluation/metrics-latest.json]
      blocks: []
    - path: promotion/readiness.json
      kind: report
      status: refresh
      rule: final_keep_or_block_decision_with_evidence_chain
      blocked_by: [evaluation/copilot-ratchet-report.json]
      blocks: []
    - path: runs/iterations.jsonl
      kind: ledger
      status: append
      rule: at_least_two_non_dry_cycles_required
      blocked_by: [promotion/readiness.json]
      blocks: []
  validator_commands:
    - "uv run python scripts/watchers/inbox_router.py"
    - "uv run --isolated --with jsonschema --with pyyaml python tests/validate_parent_wrapper_contract.py"
    - "uv run --isolated --with jsonschema --with pyyaml python scripts/score-parent-wrapper.py --json"
    - "git --no-pager diff --check"
  acceptance:
    - "validator passes with all seven gates green"
    - "scorer reports non-decreasing score with at least two real non-dry cycles"
    - "readiness.json status == pass"
    - "every previous phase reads 'completed' in the phase graph"
    - "no role contract grants both governance and runtime permissions"
    - "every artifact in the wrapper resolves to a producer role, a consumer role, and a Pixeltable table"
    - "three-framings rule is preserved in every cross-boundary artifact"
```

## 16. Council review checklist (for human + triad pre-acceptance)

```yaml
council_review:
  candidates_on_table:
    - id: A
      name: roots_first_consuming_lattice_v2
      status: present_in_section_1
      confidence: 0.92
    - id: B
      name: capillary_xylem_split
      status: not_yet_drafted
      note: "separates readiness-prompt path from payload path as different pipelines"
    - id: C
      name: membrane_osmosis
      status: not_yet_drafted
      note: "every tier is a selectively-permeable boundary that rejects unprepared payloads"
  council_questions:
    - "Does Candidate A name the three framings clearly enough that no future artifact can accidentally collapse them?"
    - "Does the upstream-handshake protocol preserve the prompt-before-payload invariant under concurrency?"
    - "Is the recursive-refactor loop bounded so it cannot rewrite upstream beyond the merge-to-main criteria?"
    - "Does the tool-catalog phase produce real shippable units (SKILL.md folders), not just registry entries?"
    - "Is the substrate dual-write rule auditable (every artifact appears in both filesystem and Pixeltable)?"
    - "Are evidence_refs in this packet all current and resolvable?"
  council_actions_required_before_triad_consumption:
    - "name the winning candidate explicitly (A, B, C, or merged)"
    - "rewrite §1 with the winning candidate verbatim"
    - "trigger inbox watcher to emit routing decision"
    - "produce the first major triad prompt as a separate inbox packet of artifact_type .handoff.md"
```

## 17. What this packet does NOT contain (deliberately)

```yaml
explicit_non_goals:
  - "tech stack choice (no language, framework, runtime declared)"
  - "first major triad prompt (that artifact is downstream of this one)"
  - "implementation code (this is contracts, schemas, protocols, registries only)"
  - "ICM workspace builder (separate artifact under skills/)"
  - "child runtime adoption claims (parent-only scope)"
  - "InfraNodus live MCP wiring (optional, bounded local substitute is default)"
```

## 18. Gaps surfaced during research (open questions for the council)

```yaml
open_questions:
  - id: OQ-001
    question: "Should later front-door lifecycle packets live at inbox/ root or in inbox/packets/ once the watcher is active?"
    impact: medium
    proposed_default: "inbox/packets/ to avoid root clutter once volume grows"
  - id: OQ-002
    question: "How are body cells registered when this wrapper itself wraps a sub-harness? Is there a body-registry-of-body-registries pattern?"
    impact: high
    proposed_default: "nested body-registry.yaml at each wrapped layer, with a top-level body-registry.index.yaml at the wrapper root"
  - id: OQ-003
    question: "Does the codewiki.google source add anything load-bearing, or is it a noise source?"
    impact: low
    proposed_default: "skip unless the council names a specific gap it would fill"
  - id: OQ-004
    question: "What is the substrate-swap policy if Pixeltable is unavailable in a downstream consumer environment?"
    impact: high
    proposed_default: "filesystem is the source of truth; Pixeltable mirror is best-effort and may be queued for later replay"
  - id: OQ-005
    question: "Should the upstream-handshake support multi-tier propagation (root through ancestors), or is it always one-hop?"
    impact: high
    proposed_default: "one-hop per cycle; multi-tier emerges from repeated one-hop cycles up the chain"
  - id: OQ-006
    question: "How do we ensure recursive refactor does not destabilize already-promoted upstream contracts?"
    impact: high
    proposed_default: "every upstream refactor request must include a backward-compatibility statement and a migration plan; otherwise it is rejected at upstream readiness-ack"
```

## 19. Traceability map

```yaml
trace:
  - phase: 0
    sources:
      - "fre-meta-harness AGENTS.md:43-49 (seven-part proof package + imported authorities)"
      - "fre-meta-harness MEMORY.md:19-22 (fractal six-file scaffold)"
      - "fre-meta-harness program.md:48-72 (mutable surface allowlist)"
  - phase: 1
    sources:
      - "user CLAUDE.md (parent operational note: inbox packets, routing decision, delegation bundle)"
      - "inbox/fre-meta-harness_plus_inbox.plan.md (contract family listing)"
      - "inbox/FRE-META-HARNESS_PLAN.plan.md (front-door lifecycle)"
  - phase: 2
    sources:
      - "inbox/prompting-tools.consume/Schema Set — Contracts for every artifact .md"
      - "inbox/prompting-tools.consume/Artifact Registry — What the harness can produce .md"
  - phase: 3
    sources:
      - "inbox/fre-meta-harness_plus_inbox.plan.md §3 (runtime role family + separation rules)"
      - "docs/NOTION-DOCS/agent-role-contract schema json .md (desired role contract shape)"
  - phase: 4
    sources:
      - "inbox/FRE-META-HARNESS_PLAN.plan.md (first executable lifecycle, 12 stages)"
      - "arxiv 2603.16021 §3.3 (stage contract three-section pattern)"
  - phase: 5
    sources:
      - "user message (tree roots drinking water; prompts upstream first)"
      - "arxiv 2603.16021 §6.1 (edit-source principle as upstream feedback)"
      - "arxiv 2603.16021 §3.3 (Inputs declaration as prompt-before-payload)"
  - phase: 6
    sources:
      - "inbox/prompting-tools.consume/Prompt Tools — Tool Catalog .md"
      - "inbox/prompting-tools.consume/Prompt Tools — Capability Harvesting Matrix .md"
      - "arxiv 2603.16021 §3.2 (skills as Layer 3 bundled reference)"
  - phase: 7
    sources:
      - "inbox/prompting-tools.consume/Prompt Tools — Pixeltable DuckDB Artifact Store .md"
      - "user CLAUDE.md (Pixeltable as durable substrate)"
  - phase: 8
    sources:
      - "inbox/prompting-tools.consume/Prompt Tools — Policy + Gates (Trust Plane) .md"
  - phase: 9
    sources:
      - "inbox/prompting-tools.consume/Prompt Tools — Observability + Evaluation (Measure Plane) .md"
  - phase: 10
    sources:
      - "inbox/prompting-tools.consume/Spec Compiler — Markdown files that compile into enforcement .md"
  - phase: 11
    sources:
      - "user message (recursive consume → analyze → schematize → refactor → push upstream)"
      - "user message (consuming branch; merge to main only after green)"
  - phase: 12
    sources:
      - "fre-meta-harness tests/validate_parent_wrapper_contract.py"
      - "fre-meta-harness scripts/score-parent-wrapper.py"
      - "user CLAUDE.md (no-fake-green; structured routing decision and delegation bundle required)"
```

---bottom-matter---
validation_status: "pending_council_review"
status_summary:
  completeness: 0.88
  confidence: high
  doc_state: "governed_inbox_packet_council_candidate"
gate_progress:
  - gate_id: harvest_gate
    status: green
    notes: "Inputs (transcribe.consume, file-system-structure-research.consume, prompting-tools.consume, fre-meta-harness research) consumed and traceability map emitted."
  - gate_id: registry_gate
    status: amber
    notes: "Contract and schema families enumerated with blocking edges; not yet authored."
  - gate_id: manifest_gate
    status: amber
    notes: "Role contracts and stage contracts enumerated; not yet authored."
  - gate_id: verification_gate
    status: amber
    notes: "Validator command set declared per phase; not yet executed."
  - gate_id: state_gate
    status: amber
    notes: "Pixeltable/DuckDB substrate enumerated; not yet bound."
  - gate_id: health_gate
    status: amber
    notes: "Observability schemas enumerated; not yet emitting events."
  - gate_id: promotion_gate
    status: red
    notes: "Promotion blocked until all prior phases land. This is intentional."
open_questions:
  - "Which candidate (A, B, C, or merge) does the council pick? §16 lists the questions."
  - "Are Phase 1 contract names canonical or do they need renaming to match an upstream convention not yet surfaced?"
  - "Does the three-framings rule need its own JSON Schema or is the protocol doc sufficient?"
pending_validations:
  - "Validate this packet against contracts/inbox-packet.yaml when the inbox watcher consumes it."
  - "Confirm every evidence_ref path resolves from repo_root."
  - "Confirm no cycle in the cross-phase blocks graph."
promotion_criteria:
  - "Council names a winning candidate explicitly."
  - "Inbox watcher emits a routing decision for this packet."
  - "Triad produces a follow-on .handoff.md as the first major triad prompt."
  - "Phase 0 audit returns all green before any Phase ≥1 file is created."
blocked_by:
  - "Council review of Candidate A vs. unstated siblings B and C."
  - "Confirmation that codewiki.google is not load-bearing (or unblocking the codewiki research agent)."
next_iteration:
  owner: "orchestrator-validator"
  objective: "Classify this packet against contracts/inbox-packet.yaml, name the winning candidate, and trigger the inbox watcher to emit the first routing decision."
