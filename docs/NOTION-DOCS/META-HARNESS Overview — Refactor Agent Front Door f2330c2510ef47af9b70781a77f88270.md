# META-HARNESS Overview — Refactor Agent Front Door

<aside>
🧬

**Purpose**: This is the refactoring-agent front door for the META-HARNESS governed artifact system. Start here before editing runtime schemas, capability records, tools, skills, hooks, or promotion rules.

</aside>

## Start here

1. Open the [](Governed%20Artifacts%20Registry%201d5d61bd11cb46608ef72120e7c2f4e8.md).
2. Use the **Refactoring Agent Intake** view first.
3. Resolve **Missing source traces** before promoting runtime/schema work.
4. Use **Runtime API contract surface** when editing endpoints.
5. Use **Promotion readiness board** before marking any artifact validated or canonical.

## What this page controls

- Governed specs
- Runtime API contracts
- Capability matrix records
- Tool / skill / hook manifests
- Source trace requirements
- Bottom-matter requirements
- Runtime validation gates
- Promotion readiness
- Refactor-agent intake

## Refactoring agent operating rules

- Every artifact must have a stable **Artifact ID**.
- Every capability or endpoint must have a **source trace**.
- Every runtime endpoint must link to related specs and tests.
- Every governed markdown artifact must declare bottom-matter status.
- Every promotion decision must be blocked until traces, tests, docs parity, and validation gates are present.
- InfraNodus graph mapping is required for tool/capability/runtime-memory artifacts.

## First-pass intake queue

Refactoring agents should prioritize artifacts where:

- **Refactor intake** is checked.
- **Promotion readiness** is `Blocked`, `Needs trace`, `Needs test`, or `Needs docs parity`.
- **Source trace status** is `Missing` or `Partial`.
- **Bottom matter status** is `Missing`, `Partial`, or `Invalid`.

## Required views in the registry

- **All artifacts** — complete governed artifact list.
- **Refactoring Agent Intake** — first-pass queue for schema/runtime refactor agents.
- **Missing source traces** — required provenance cleanup.
- **Promotion readiness board** — promotion/lifecycle control.
- **Runtime API contract surface** — endpoint/schema/test linkage.
- **By directory** — repository-style navigation.
- **Vectorworks → iTwin** — spatial data lineage view.

## Runtime schema refinement focus

The next refactoring agents should harden:

1. `runtime_endpoint.schema.yaml`
2. `runtime_request.schema.yaml`
3. `runtime_response.schema.yaml`
4. `runtime_error.schema.yaml`
5. `capability_matrix.schema.json`
6. `capability_matrix_starter.yaml`
7. source trace block ID convention
8. HTML navigation export convention
9. CXML/code-understanding adapter convention

## Backlinks

- Project root: [FRE-AGENTIC ENGINEERING:](FRE-AGENTIC%20ENGINEERING%20111c487604f48221a914015210b84501.md)
- Capability reboot: [Capability Registry Reboot — Tools, Skills, Hooks, and InfraNodus](Capability%20Registry%20Reboot%20%E2%80%94%20Tools,%20Skills,%20Hooks,%20b29ab5c1ac7a4534a94bbe0c288ff0b9.md)
- Runtime API spec: [Runtime API Specification — Lean Callable Harness Contract](Runtime%20API%20Specification%20%E2%80%94%20Lean%20Callable%20Harness%20%20032933e1b7514a8f8b5ec2eb76350b3d.md)
- Runtime consolidation plan: [Runtime Consolidation Refactoring Plan — Harness Lab Migration](Runtime%20Consolidation%20Refactoring%20Plan%20%E2%80%94%20Harness%20L%207068f11b24dc43a5ac6d852529b00ace.md)
- Governed artifacts: [](Governed%20Artifacts%20Registry%201d5d61bd11cb46608ef72120e7c2f4e8.md)

---bottom-matter---

status_summary:

completeness: 0.68

confidence: medium

doc_state: active-intake

implementation_alignment: partial

test_alignment: pending

source_alignment: partial

next_iteration:

owner: planning-agent

objective: Convert the registry into the full governed-artifacts control database with typed source traces, runtime endpoint coverage, validation surface links, and promotion-decision records.

promotion_criteria:

- Refactor intake view is populated.
- Source trace records are backlinked.
- Runtime endpoints have related specs and tests.
- Capability records have source traces and runtime endpoint mappings.
- Missing trace/test/doc parity gaps are converted into repair events or implementation tasks.

blocked_by:

- Source trace database not yet split into typed relational table.
- Runtime endpoint schema files not yet extracted.
- Capability matrix schema not yet converted into machine-readable JSON Schema.