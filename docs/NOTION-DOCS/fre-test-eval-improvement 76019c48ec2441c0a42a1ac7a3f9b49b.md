# fre-test-eval-improvement

<aside>
🧪

**Purpose**: This is the current launch packet for the isolated LATTICE evaluation of FRE as a candidate proof kernel. It reflects the hardened branch/worktree plan and supersedes the earlier standalone `fre-test-eval-improvement` scaffold.

</aside>

## Current evaluation state

- **Branch**: `feat/fre-meta-harness-eval`
- **Worktree**: `/Volumes/PixelTable/VW_iTWIN_Bridge/lattice-worktrees/feat-fre-meta-harness-eval`
- **Base**: `origin/main` at `d02328e`
- **Durable plan**: `meta/harness/docs/specs/fre-method-evaluation-plan-2026-05-16.md`
- **Allowed write scope**: `meta/harness/fre/**`
- **Bootstrap exception**: `meta/harness/docs/specs/fre-method-evaluation-plan-2026-05-16.md`

## Source bundle

Use these as source context, but translate them into repo-local artifacts before executing:

- FRE method source: [FRE — Fractal Research Engineering (Method v0.1)](FRE%20%E2%80%94%20Fractal%20Research%20Engineering%20(Method%20v0%201)%20301c487604f4820b83e601f9ddcf6771.md)
- FRE entry loop: [FRE Harness — Agent Entry Point (Read First)](https://www.notion.so/FRE-Harness-Agent-Entry-Point-Read-First-080928b13e4749c4b292ad74c57b2bdb?pvs=21)
- Human-readable minimal schema: [FRE Minimal Framework — Human-Readable Schema Spec](FRE%20Minimal%20Framework%20%E2%80%94%20Human-Readable%20Schema%20Spec%207a76812e054e4ef192753c494f4aa86e.md)
- Machine-readable minimal schema: [FRE Minimal Framework — Machine-Readable JSON Schema](FRE%20Minimal%20Framework%20%E2%80%94%20Machine-Readable%20JSON%20Sche%205d3be170679a4b0ab9b75094464825d7.md)
- Meta-harness metrics registry: [](Meta-Harness%20Metrics%20Registry%20f2fc487604f48284976d01c7ea649186.md)
- Governed artifact registry: [](Governed%20Artifacts%20Registry%201d5d61bd11cb46608ef72120e7c2f4e8.md)

<aside>
🚫

**Scope guard**: This is not a doctrine branch and not the full FRE universe. This is a bounded evaluation branch to prove, amend, or reject FRE as a minimal proof kernel for LATTICE and future projects.

</aside>

---

# 1. Evaluation hypothesis

This branch evaluates FRE as a **candidate proof kernel**, not as doctrine and not as a replacement framework.

## Bounded claim

> A schema-driven loop of source → schema → examples → validation → metrics → repair task → promotion decision can serve as the smallest repeatable proof kernel for future LATTICE and non-LATTICE projects.
> 

The evaluation must produce one of:

- `ADOPT`
- `ADOPT WITH AMENDMENTS`
- `REJECT`

---

# 2. Production safety constraints

## Allowed writes

```
meta/harness/fre/**
meta/harness/docs/specs/fre-method-evaluation-plan-2026-05-16.md
```

## Forbidden writes

```
pixeltable/**
src/**
public/**
scripts/**
meta/SCHEMA.md
meta/ARCHITECTURE.md
meta/API.md
pixeltable/migrations/**
deployment config
production runtime config
production data
```

## Rule

Any change outside `meta/harness/fre/**` requires explicit justification in both:

1. the session report, and
2. the adoption memo.

Do **not** add Pixeltable migration `0017`.  

Do **not** wire FRE into production runtime.  

Do **not** build UI, Notion sync, InfraNodus, MCP, sidecar integration, or multi-agent orchestration in this evaluation pass.

---

# 3. Updated repository shape

```
meta/harness/fre/
  README.md
  CLAUDE.md
  docs/
    goal.md
    sources.md
    source-normalization.md
    evaluation-questions.md
    fre-to-lattice-map.md
    adoption-rubric.md
    gaps.md
    decisions/
    sessions/
  schemas/
    fre-loop.schema.json
    gate-result.schema.json
    repair-task.schema.json
    promotion-decision.schema.json
  examples/
    fre-loop.valid.json
    fre-loop.invalid.missing-promotion.json
    fre-loop.invalid.green-terminology.json
    expected-failures.yaml
    gate-result.valid.json
    repair-task.valid.json
    promotion-decision.valid.json
  tests/
    test_schema_validity.py
    test_examples_validate.py
    test_failure_examples_fail.py
    test_no_green_terminology.py
    test_required_metrics.py
    test_repair_tasks.py
    test_lattice_mapping.py
  harness/
    validate_schema.py
    validate_examples.py
    evaluate.py
    report.py
    propose_repairs.py
  runs/
    README.md
```

---

# 4. Phase 0 — Normalize source packet first

## Goal

Convert the Notion-derived FRE source packet into clean repo-local source references and executable artifacts.

## Required Phase 0 files

```
meta/harness/fre/README.md
meta/harness/fre/CLAUDE.md
meta/harness/fre/docs/goal.md
meta/harness/fre/docs/sources.md
meta/harness/fre/docs/source-normalization.md
meta/harness/fre/docs/evaluation-questions.md
meta/harness/fre/docs/fre-to-lattice-map.md
meta/harness/fre/docs/adoption-rubric.md
meta/harness/fre/docs/gaps.md
meta/harness/fre/examples/expected-failures.yaml
```

## Source normalization checklist

Before creating executable files:

- [ ]  Remove Notion-created markdown links inside code blocks.
- [ ]  Correct malformed command strings such as `validate_[schema.py](http://schema.py)`.
- [ ]  Correct malformed command strings such as `harness/[evaluate.py](http://evaluate.py)`.
- [ ]  Convert Notion page mentions into provenance/source records.
- [ ]  Validate YAML blocks before treating them as source.
- [ ]  Validate JSON blocks before treating them as source.
- [ ]  Ensure code fences are closed correctly.
- [ ]  Preserve the terminology decision:
    - forbidden canonical field: `definition_of_green`
    - required canonical field: `validation_pass_criteria`
- [ ]  Keep `definition_of_green` only in intentional invalid fixtures, terminology tests, or notes explaining the rejection.

## Phase 0 exit check

One repo-local source bundle summary exists and can be read without the external source packet or Notion page.

---

# 5. Phase 1 — Build minimal executable loop

## Goal

Create a runnable FRE loop under `meta/harness/fre/`.

## Deterministic commands

Use these command shapes from the worktree root:

```
uv run python meta/harness/fre/harness/validate_schema.py
uv run python meta/harness/fre/harness/validate_examples.py
uv run python meta/harness/fre/harness/evaluate.py
uv run python meta/harness/fre/harness/propose_repairs.py
uv run python meta/harness/fre/harness/report.py
uv run pytest meta/harness/fre/tests
```

## Required immutable run output

Every run must write to an immutable run directory:

```
meta/harness/fre/runs/RUN-YYYY-MM-DD-0001/
  input-manifest.yaml
  normalized-source-summary.md
  schema-validation.json
  example-validation.json
  gate-results.json
  scorecard.yaml
  repair-tasks.yaml
  report.md
  promotion-decision.md
```

Optional convenience pointer:

```
meta/harness/fre/runs/latest -> RUN-YYYY-MM-DD-0001
```

Do not treat `latest` as canonical.

## Required run manifest

```yaml
run_id: RUN-YYYY-MM-DD-0001
branch: feat/fre-meta-harness-eval
base_commit: d02328e
worktree: /Volumes/PixelTable/VW_iTWIN_Bridge/lattice-worktrees/feat-fre-meta-harness-eval
source_packet: /Volumes/PixelTable/VW_iTWIN_Bridge/fre-test-eval-improvement 76019c48ec2441c0a42a1ac7a3f9b49b.md
commands:
  - uv run python meta/harness/fre/harness/validate_schema.py
  - uv run python meta/harness/fre/harness/validate_examples.py
  - uv run python meta/harness/fre/harness/evaluate.py
  - uv run python meta/harness/fre/harness/propose_repairs.py
  - uv run python meta/harness/fre/harness/report.py
  - uv run pytest meta/harness/fre/tests
```

## Phase 1 exit check

The loop runs locally from source packet to scorecard/report with deterministic outputs.

---

# 6. Expected failure contracts

Invalid examples must fail for the intended reason, not accidentally.

Required file:

```
meta/harness/fre/examples/expected-failures.yaml
```

Minimum structure:

```yaml
expected_failures:
  - example: examples/fre-loop.invalid.green-terminology.json
    expected_failure_classes:
      - REQUIRED_FIELD_MISSING
      - ADDITIONAL_PROPERTY_NOT_ALLOWED
    expected_field:
      - validation_pass_criteria
      - definition_of_green

  - example: examples/fre-loop.invalid.missing-promotion.json
    expected_failure_classes:
      - AUTHORITY_CHAIN_MISSING_REQUIRED_VALUE
    expected_field:
      - authority_chain
    expected_missing_value:
      - promotion_decision
```

The invalid-example tests must assert:

```
invalid example fails for expected failure class and expected field
```

not merely:

```
invalid example fails
```

---

# 7. FRE → LATTICE anti-corruption layer

FRE vocabulary must not overwrite working LATTICE vocabulary by default.

Required file:

```
meta/harness/fre/docs/fre-to-lattice-map.md
```

Minimum transfer statuses:

```
clean
partial
conflict
reject
needs_extension
```

Minimum mapping:

| FRE field | LATTICE concept | Transfer status | Notes |
| --- | --- | --- | --- |
| `repair_task` | proposal / bounded implementation task | clean | Requires owner and acceptance criteria |
| `promotion_decision` | ratchet decision / capability promotion gate | partial | Needs stronger evidence fields |
| `scorecard` | benchmark / evidence artifact | clean | Should include command output hashes |
| `validation_pass_criteria` | ratchet acceptance rule | clean | Rename accepted; do not use `definition_of_green` |
| `source_record` | provenance evidence | partial | Needs richer source typing |
| `artifact` | capability/proof artifact | partial | Needs artifact lineage |

---

# 8. Phase 2 — Map FRE to LATTICE semantics

## Goal

Prove whether FRE outputs map cleanly to existing LATTICE proof surfaces.

## Deliverables

```
meta/harness/fre/docs/fre-to-lattice-map.md
meta/harness/fre/docs/sessions/RUN-YYYY-MM-DD-0001.md
meta/harness/fre/docs/gaps.md
```

## Phase 2 exit check

The team can point to exact fields that transfer cleanly and exact fields that do not.

---

# 9. Phase 3 — Pressure test with real LATTICE fixtures

## Goal

Test FRE against real artifacts, not just toy examples.

## Candidate fixtures

Use at least two:

- a capability contract document
- a harness proof report
- a route or schema change proposal
- a research-derived adoption packet
- a restart-ready handoff doc

## Test questions

1. Does FRE clarify provenance and evidence?
2. Does it produce better repair tasks?
3. Does it capture ratchet and promotion decisions?
4. Does it stay small?
5. Does it conflict with existing LATTICE proof language?

## Phase 3 exit check

At least two real LATTICE artifacts have gone through the loop and produced reports.

---

# 10. Phase 4 — Adoption decision

## Decision options

```
ADOPT
ADOPT WITH AMENDMENTS
REJECT
```

## Adoption scoring rubric

Score each category from `0` to `2`.

- `0` = failed or not useful
- `1` = partially useful or needs amendment
- `2` = strong fit

| Category | Score |
| --- | --- |
| Deterministic execution | 0–2 |
| Schema clarity | 0–2 |
| Repair task usefulness | 0–2 |
| LATTICE vocabulary compatibility | 0–2 |
| Real artifact usefulness | 0–2 |
| Integration restraint | 0–2 |
| Evidence quality | 0–2 |
| Restart readiness | 0–2 |

Decision rule:

```
14–16 = ADOPT
9–13  = ADOPT WITH AMENDMENTS
0–8   = REJECT
```

## Memo must include

- what FRE proved
- what FRE failed to prove
- where FRE conflicted with LATTICE
- minimal amendments needed
- whether FRE should become the cross-project baseline
- what remains LATTICE-specific

---

# 11. Updated immediate next tasks

1. Create `meta/harness/fre/README.md` and `meta/harness/fre/CLAUDE.md` as the bounded experiment charter.
2. Translate the source packet into local:
    - `docs/sources.md`
    - `docs/source-normalization.md`
    - `docs/goal.md`
3. Add:
    - `docs/fre-to-lattice-map.md`
    - `docs/adoption-rubric.md`
    - `docs/evaluation-questions.md`
    - `docs/gaps.md`
4. Implement the four core schemas plus valid/invalid example set.
5. Add `examples/expected-failures.yaml`.
6. Add the first seven tests, including `test_lattice_mapping.py`.
7. Add `evaluate.py`, `report.py`, and `propose_repairs.py` so every failure emits a repair task.
8. Run one end-to-end session and record it under an immutable run directory.
9. Write the FRE-to-LATTICE mapping memo before expanding scope.

---

# 12. Final directive for Claude Code

```markdown
You are not building the full FRE harness.

You are evaluating FRE as a candidate proof kernel inside LATTICE.

Build only inside `meta/harness/fre/**`.

Your job is to make the FRE candidate loop executable, falsifiable, and repair-producing.

If an invalid example fails for the wrong reason, the harness failed.

If a blocking failure has no repair task, the harness failed.

If a schema change has no test and no promotion decision, the harness failed.

If this work requires migrations, UI, sidecar integration, Notion sync, or runtime wiring before the adoption memo, the evaluation failed.

The first successful milestone is boring:

- source packet normalized
- schemas created
- examples created
- expected failures declared
- tests pass
- scorecard written
- repair tasks written when needed
- promotion decision written
```

---bottom-matter---

status_summary:

completeness: 0.92

confidence: high

doc_state: active-evaluation-packet

implementation_alignment: branch-created

test_alignment: pending

source_alignment: linked-and-needs-normalization

open_questions:

- Should the first run preserve the reduced schema from this page or import the full schema from the machine-readable schema page?
- Should the human terminology correction be formalized as a separate `human_decision` source record?
- What two real LATTICE fixtures should be selected for Phase 3?

pending_validations:

- Create Phase 0 files in `meta/harness/fre/`
- Normalize source packet
- Implement schemas and examples
- Add expected failure contracts
- Run first pytest cycle
- Emit first immutable run directory

promotion_criteria:

- Phase 0 source packet can stand alone inside repo
- Minimal schema validates
- Valid example passes
- Invalid examples fail for expected reasons
- Metrics scorecard is emitted
- Repair tasks are emitted for blocking failures
- Promotion decision is recorded

blocked_by:

- Phase 0/1 scaffolding has not been created yet

next_iteration:

owner: evaluation-agent

objective: Scaffold `meta/harness/fre/` and run the first schema validation/evaluation cycle.

[FRE Schema Evaluation Plan for LATTICE Meta-Harness](FRE%20Schema%20Evaluation%20Plan%20for%20LATTICE%20Meta-Harnes%2053cbd773de08490caf831088b4afc94c.md)