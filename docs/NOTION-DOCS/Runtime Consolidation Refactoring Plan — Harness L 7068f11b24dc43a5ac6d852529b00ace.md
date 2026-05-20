# Runtime Consolidation Refactoring Plan — Harness Lab Migration

---

artifact_id: runtime-consolidation-refactor-plan

artifact_type: plan

schema_version: 0.1.0

status: draft-ready

owner: planning-agent

primary_skill: planning

purpose: Consolidate the expanded FRE Harness documentation into a lean runtime/API layer and inject that runtime back into the original Harness Laboratory and foundational documents.

created_at: 2026-05-16

---

<aside>
🧭

**Purpose**: This plan refactors the current expanded Harness Laboratory documentation into a concise runtime layer while preserving the full specification corpus as source documentation.

</aside>

## 1) Executive summary

The FRE Harness has reached the point where it has enough design material to become a **runtime system**.

The current documentation now includes:

- FRE method and loop
- Harness Lab principles
- Portable Harness Package
- nucleus docs: `CLAUDE.md`, `goal.md`, `golden-path.md`, `sources.md`, `memory.md`
- `.claude/` control surface
- task rules
- schema set
- examples
- compiler concepts
- reports
- CSV database baseline
- capability/tool registry reboot
- InfraNodus always-on graph layer
- Runtime API Specification

The refactor should now separate the ecosystem into two layers:

1. **Source specification layer** — the full, rich, explanatory documentation.
2. **Runtime layer** — concise, callable, schema-derived operating contracts for agents.

The runtime layer becomes the small thing agents read every time. The full docs remain available for audit, contribution, and design evolution.

## 2) Core refactoring principle

> **Full docs explain the harness. Runtime docs operate the harness.**
> 

The system should not force every agent to reread philosophy, history, and design rationale during execution.

Instead:

- schemas define structure,
- comments/docstrings explain why fields exist,
- runtime endpoints define callable behavior,
- hooks enforce validation,
- run logs preserve evidence,
- full docs remain the source of truth for humans and deep audits.

## 3) Target architecture

```
FRE Harness
├── BOOTSTRAP.md
├── CLAUDE.md
├── docs/
│   ├── harness/
│   ├── spec/
│   └── site/
├── runtime/
│   ├── README.md
│   ├── api.md
│   ├── manifest.yaml
│   ├── lifecycle.md
│   ├── validation.md
│   ├── errors.md
│   ├── transports.md
│   └── endpoints/
├── schemas/
├── examples/
├── tools/
├── skills/
├── capabilities/
├── hooks/
├── .claude/
├── backend/data/
├── compiler/
├── reports/
└── runs/
```

## 4) Migration rule

Do not delete the source docs.

Instead:

1. **Extract** runtime-relevant contracts from the full docs.
2. **Condense** them into runtime files.
3. **Link back** to the full source specification.
4. **Validate** that every runtime operation maps to a schema, example, hook, and run-log behavior.

## 5) Refactoring phases

## Phase 0 — Freeze and inventory

### Goal

Create a stable baseline before refactoring.

### Tasks

- [ ]  List every current Harness Laboratory page.
    - Owner: `planning-agent`
    - Outputs: `compiler/audit.md`
    - Validation: all source pages are listed with role + destination.
- [ ]  Classify each page as one of:
    - source spec
    - runtime contract
    - schema
    - example
    - public docs
    - run/report artifact
    - archive/reference
    - Owner: `planning-agent`
    - Outputs: `compiler/audit.md`
    - Validation: every page has one classification.
- [ ]  Record current baseline in `runs/0001.md`.
    - Owner: `evaluation-agent`
    - Outputs: `runs/0001.md`
    - Validation: run log links this plan and audit output.

### Output

```
compiler/audit.md
runs/0001.md
```

## Phase 1 — Define the runtime kernel

### Goal

Create the smallest set of files an agent needs at runtime.

### Runtime kernel files

```
BOOTSTRAP.md
CLAUDE.md
docs/harness/goal.md
docs/harness/golden-path.md
docs/harness/sources.md
docs/harness/memory.md
TASKS.md
runtime/README.md
runtime/api.md
runtime/manifest.yaml
runtime/lifecycle.md
runtime/validation.md
runtime/errors.md
```

### Tasks

- [ ]  Mark these files as the **runtime kernel**.
    - Owner: `planning-agent`
    - Outputs: `runtime/manifest.yaml`
    - Validation: manifest lists every kernel file.
- [ ]  Ensure each kernel file has:
    - purpose
    - inputs
    - outputs
    - validation tie-in
    - failure modes
    - upstream path
    - Owner: `evaluation-agent`
    - Outputs: `compiler/compliance.md`
    - Validation: all kernel files pass envelope check.
- [ ]  Remove runtime bloat from kernel files.
    - Owner: `memory-agent`
    - Outputs: patched kernel docs
    - Validation: kernel docs contain operating instructions, not long design essays.

### Output

```
runtime/manifest.yaml
compiler/compliance.md
```

## Phase 2 — Inject runtime references into the original Harness Laboratory

### Goal

Make the original Harness Laboratory point to the new runtime layer instead of forcing agents through the full documentation corpus.

### Pages to update

- FRE-AGENTIC ENGINEERING front door
- FRE Harness — Agent Entry Point
- Portable Harness Package
- Harness Spec Suite
- Schema Set
- Artifact Registry
- Spec Compiler
- Capability Registry Reboot
- Runtime API Specification

### Tasks

- [ ]  Add `Runtime API Specification` to the canonical entrypoints.
    - Owner: `planning-agent`
    - Outputs: updated front door
    - Validation: front door read order includes runtime.
- [ ]  Update the FRE entrypoint so runtime API validation becomes a mandatory gate.
    - Owner: `golden-path-agent`
    - Outputs: updated FRE entrypoint
    - Validation: runtime gate appears in mandatory gates.
- [ ]  Update Portable Harness Package folder map to include:
    - `runtime/`
    - `tools/`
    - `capabilities/`
    - `hooks/`
    - `backend/data/`
    - Owner: `sources-agent`
    - Outputs: updated package map
    - Validation: export checklist includes runtime folder.
- [ ]  Update Harness Spec Suite so `runtime/` is the compiled output of the full docs.
    - Owner: `memory-agent`
    - Outputs: updated spec suite index
    - Validation: source docs and runtime docs are clearly separated.

### Output

```
updated front door
updated FRE entrypoint
updated Portable Harness Package
updated Harness Spec Suite
```

## Phase 3 — Convert verbose docs into runtime API contracts

### Goal

Turn design documentation into callable runtime endpoints.

### Runtime endpoints to define first

```
bootstrap.project
validate.package
capability.harvest
runtime.register_tool
runtime.register_skill
runtime.register_agent
runtime.register_hook
runtime.log_action
runtime.score_run
runtime.promote_improvement
runtime.export_package
```

### Per-endpoint required fields

```yaml
id:
apiVersion:
endpointVersion:
purpose:
reads:
writes:
inputs:
outputs:
sideEffects:
validation:
hooks:
errors:
idempotency:
permissions:
examples:
sourceDocs:
```

### Tasks

- [ ]  Create `runtime/endpoints/*.endpoint.md` for every endpoint.
    - Owner: `planning-agent`
    - Outputs: endpoint docs
    - Validation: every endpoint has required fields.
- [ ]  Create matching endpoint schemas.
    - Owner: `sources-agent`
    - Outputs: `runtime/schemas/endpoint.schema.json`
    - Validation: endpoint examples validate.
- [ ]  Add endpoint examples.
    - Owner: `evaluation-agent`
    - Outputs: `examples/runtime/*.example.yaml`
    - Validation: one human + one machine example per endpoint.
- [ ]  Link each endpoint to its source docs.
    - Owner: `memory-agent`
    - Outputs: endpoint `sourceDocs` fields
    - Validation: no endpoint exists without source provenance.

### Output

```
runtime/endpoints/*.endpoint.md
runtime/schemas/*.schema.json
examples/runtime/*.example.yaml
```

## Phase 4 — Refactor foundational docs into concise runtime form

### Goal

Make the nucleus docs usable by a fresh agent without loading excess design rationale.

### Refactor targets

#### `CLAUDE.md`

Keep only:

- what this repo is
- read order
- hard rules
- runtime API pointer
- validation pointer
- log requirement

Move long rationale to:

```
docs/spec/claude-runtime-rationale.md
```

#### `goal.md`

Keep only:

- primary metric
- secondary metrics
- keep/revert rule
- operating mode
- acceptance criteria

Move examples/rationale to:

```
docs/spec/goal-rationale.md
```

#### `golden-path.md`

Keep only:

- fresh export → green steps
- validation sequence
- failure recovery
- done means

Move broader explanation to:

```
docs/spec/golden-path-rationale.md
```

#### `sources.md`

Keep only:

- authoritative links
- version pins
- provenance policy
- skill/tool supply-chain requirements

Move historical notes to:

```
docs/spec/source-policy-rationale.md
```

#### `memory.md`

Keep only:

- invariants
- decisions
- rolling learnings

Move old design discussion to:

```
docs/spec/memory-rationale.md
```

### Tasks

- [ ]  Trim nucleus docs to runtime size.
    - Owner: `memory-agent`
    - Outputs: concise nucleus docs
    - Validation: each nucleus doc is readable in one pass.
- [ ]  Move rationale into `docs/spec/`.
    - Owner: `sources-agent`
    - Outputs: rationale docs
    - Validation: every moved section has a destination.
- [ ]  Add links from runtime docs to source specs.
    - Owner: `planning-agent`
    - Outputs: cross-links
    - Validation: no orphaned rationale.

### Output

```
concise nucleus docs
docs/spec/*-rationale.md
```

## Phase 5 — Implement runtime validation as the main gate

### Goal

The runtime must self-validate after every meaningful action.

### Validation artifacts

```
compiler/compliance.md
compiler/missing.md
compiler/audit.md
compiler/drift-report.md
reports/scorecard.<run-id>.json
reports/evaluation-summary.<run-id>.md
runs/<run-id>.md
.claude/logs/actions.jsonl
```

### Tasks

- [ ]  Define `runtime.validation` endpoint behavior.
    - Owner: `evaluation-agent`
    - Outputs: `runtime/endpoints/validate-package.endpoint.md`
    - Validation: endpoint maps to compiler outputs.
- [ ]  Correct `.claude/settings.json` hook shape to match Claude Code schema.
    - Owner: `planning-agent`
    - Outputs: `.claude/settings.json`
    - Validation: hook schema check passes.
- [ ]  Add prompt-based validation fallback for no-CLI environments.
    - Owner: `golden-path-agent`
    - Outputs: runtime validation docs
    - Validation: corporate Mac path remains valid.
- [ ]  Add CSV validation rules for `backend/data/*.csv`.
    - Owner: `sources-agent`
    - Outputs: CSV schemas + examples
    - Validation: CRM/tasks CSVs have headers and example rows.

### Output

```
valid .claude/settings.json
runtime/validation.md
compiler/compliance.md
compiler/missing.md
```

## Phase 6 — Consolidate capability/tool registry into runtime

### Goal

Make tools, skills, hooks, and capabilities callable and discoverable by the runtime API.

### Tasks

- [ ]  Move capability reboot concepts into:
    - `tools/`
    - `skills/`
    - `capabilities/`
    - `hooks/`
    - `runtime/endpoints/`
    - Owner: `capability-harvest-agent`
    - Outputs: governed capability substrate
    - Validation: capability matrix is complete.
- [ ]  Register InfraNodus as the first always-on runtime tool.
    - Owner: `capability-harvest-agent`
    - Outputs: `tools/infranodus/tool.yaml`
    - Validation: every ability has a spec.
- [ ]  Add InfraNodus graph gate to runtime validation.
    - Owner: `evaluation-agent`
    - Outputs: `runtime/validation.md`
    - Validation: every meaningful action logs graph use or explains why skipped.
- [ ]  Register skills as governed instruction artifacts.
    - Owner: `sources-agent`
    - Outputs: `skills/manifest.yaml`
    - Validation: each skill has provenance and evaluation status.

### Output

```
tools/
skills/
capabilities/
hooks/
runtime/endpoints/capability-harvest.endpoint.md
```

## Phase 7 — Create the concise runtime packet

### Goal

Create the minimum packet that a fresh agent can read to operate the harness.

### Runtime packet

```
BOOTSTRAP.md
CLAUDE.md
TASKS.md
docs/harness/goal.md
docs/harness/golden-path.md
docs/harness/sources.md
docs/harness/memory.md
runtime/README.md
runtime/api.md
runtime/manifest.yaml
runtime/validation.md
runtime/errors.md
```

### Tasks

- [ ]  Create `runtime/README.md` as the runtime entrypoint.
    - Owner: `planning-agent`
    - Outputs: `runtime/README.md`
    - Validation: points to every runtime file.
- [ ]  Create `runtime/manifest.yaml`.
    - Owner: `sources-agent`
    - Outputs: runtime manifest
    - Validation: every runtime file listed with purpose.
- [ ]  Create `runtime/api.md`.
    - Owner: `planning-agent`
    - Outputs: endpoint index
    - Validation: every endpoint is discoverable.
- [ ]  Create `runtime/errors.md`.
    - Owner: `evaluation-agent`
    - Outputs: canonical error model
    - Validation: every endpoint uses shared error codes.
- [ ]  Create `runtime/validation.md`.
    - Owner: `golden-path-agent`
    - Outputs: runtime validation protocol
    - Validation: validation maps to hooks + compiler outputs.

### Output

```
runtime packet complete
```

## Phase 8 — Publish docs boundary

### Goal

Separate runtime docs from public/living docs.

### Public docs structure

```
docs/site/
  index.md
  principles.md
  getting-started.md
  runtime-api.md
  capability-harvest.md
  tools.md
  skills.md
  hooks.md
  validation.md
  contributing.md
  glossary.md
```

### Tasks

- [ ]  Create public docs table of contents.
    - Owner: `sources-agent`
    - Outputs: `docs/site/index.md`
    - Validation: site docs do not replace runtime docs.
- [ ]  Link source specs to public docs.
    - Owner: `memory-agent`
    - Outputs: doc cross-links
    - Validation: no duplicated source of truth.
- [ ]  Add contributor path for extending the runtime.
    - Owner: `planning-agent`
    - Outputs: `docs/site/contributing.md`
    - Validation: contributor path uses runtime endpoints.

### Output

```
docs/site/
```

## Phase 9 — Final migration audit

### Goal

Prove the refactor worked.

### Required checks

```
[ ] Runtime packet exists.
[ ] Full source docs are preserved.
[ ] Runtime docs are concise.
[ ] Runtime endpoints exist.
[ ] Every endpoint maps to schemas.
[ ] Every endpoint maps to examples.
[ ] Every endpoint maps to hooks.
[ ] Every endpoint logs actions.
[ ] Every endpoint declares errors.
[ ] Runtime manifest exists.
[ ] Compiler outputs exist.
[ ] Capability/tool substrate exists.
[ ] InfraNodus is registered.
[ ] CSV database source-of-truth exists.
[ ] Public docs boundary exists.
[ ] Fresh agent can operate from runtime docs without reading full source docs.
```

### Output

```
compiler/audit.md
compiler/compliance.md
compiler/missing.md
reports/runtime-consolidation-report.md
runs/0002.md
```

## 6) Refactor decision matrix

| Source area | Runtime destination | Source/spec destination | Public docs destination |
| --- | --- | --- | --- |
| FRE loop | `runtime/lifecycle.md` | `docs/spec/fre-method.md` | `docs/site/principles.md` |
| Harness Lab principles | `runtime/README.md` | `docs/spec/harness-lab.md` | `docs/site/index.md` |
| Nucleus docs | `docs/harness/*` | `docs/spec/*-rationale.md` | `docs/site/getting-started.md` |
| Capability reboot | `runtime/endpoints/capability-harvest.endpoint.md` | `docs/spec/capability-registry.md` | `docs/site/capability-harvest.md` |
| Runtime API spec | `runtime/api.md` | `docs/spec/runtime-api.md` | `docs/site/runtime-api.md` |
| Schema set | `schemas/*` | `docs/spec/schema-system.md` | `docs/site/schemas.md` |
| Examples | `examples/*` | `docs/spec/example-policy.md` | `docs/site/examples.md` |
| Hooks | `runtime/validation.md`  • `hooks/*` | `docs/spec/hook-system.md` | `docs/site/hooks.md` |
| CSV databases | `backend/data/*` | `docs/spec/database-policy.md` | `docs/site/data.md` |
| Reports/compiler | `compiler/*`  • `reports/*` | `docs/spec/compiler-system.md` | `docs/site/validation.md` |

## 7) Definition of done

This refactor is complete when:

1. The original Harness Laboratory points to the runtime API as the operating layer.
2. The foundational docs are concise enough for repeated runtime use.
3. The full explanatory docs are preserved under `docs/spec/`.
4. Runtime endpoints are defined and schema-bound.
5. Runtime validation produces compiler outputs.
6. Capability/tool/skill/hook registries are part of the runtime.
7. InfraNodus is registered as an always-on runtime capability.
8. CSV data rules are represented as runtime contracts.
9. Public docs are separated from runtime docs.
10. A fresh agent can operate the harness by reading only:
    - `BOOTSTRAP.md`
    - `CLAUDE.md`
    - `TASKS.md`
    - `docs/harness/*`
    - `runtime/*`

## 8) Immediate next action

Start with **Phase 0 and Phase 1**:

1. Create `compiler/audit.md`.
2. Create `runtime/README.md`.
3. Create `runtime/manifest.yaml`.
4. Create `runtime/api.md`.
5. Patch the main Harness Laboratory front door to include Runtime as a canonical entrypoint.
6. Patch `BOOTSTRAP.md` so it reads `runtime/README.md` immediately after `CLAUDE.md`.

---

```yaml
# plan-config (bottom matter)
run:
  plan_id: runtime-consolidation-refactor-plan
  iteration_budget:
    max_turns: 12
    max_major_edits: 8
  quality_gate:
    required_checks:
      - "runtime packet exists"
      - "front door points to runtime"
      - "nucleus docs remain concise"
      - "source docs preserved"
      - "compiler audit produced"
  logging:
    run_log: "runs/0002.md"
    action_log: ".claude/logs/actions.jsonl"
  scoring:
    primary_metric: "runtime_readiness_score"
    secondary_metrics:
      - "schema_endpoint_coverage"
      - "runtime_doc_size"
      - "fresh_agent_operability"
      - "source_doc_preservation"
  keep_revert_rule:
    keep_if:
      - "runtime_readiness_score improves or remains stable"
      - "no source documentation is lost"
      - "fresh agent read path is shorter"
    revert_if:
      - "runtime docs become bloated"
      - "source docs are overwritten without migration"
      - "endpoint contracts lose schema mappings"
```