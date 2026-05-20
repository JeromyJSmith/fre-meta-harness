# FRE — Fractal Research Engineering (Method v0.1)

<aside>
🧬

**Purpose**: FRE (Fractal Research Engineering) is a **research-first, spec-governed, test-gated, self-improving** engineering method. It treats documentation, schemas, tests, evaluators, and promotion decisions as one ecosystem that must remain synchronized.

</aside>

<aside>
📎

**Page contract (human + machine readable)**

**Purpose**: Define the FRE method so it can be applied consistently to new projects and audited by validators.

**Inputs**: Existing harness principles; validation sequence; traceability and envelope findings (front matter + bottom matter).

**Outputs**: A portable method spec + templates (document envelope, gates, roles, artifacts).

**Validation tie-in**: Contract validation (required artifacts exist), Drift detection (method changes are versioned), Publish decision (projects may only ship when gates pass).

**Failure modes**: “Docs as prose” causes drift; missing envelopes prevent machine governance; unsourced rules become hallucination vectors.

**Update / upstream path**: Update via an Update Artifact + run log; rerun method compliance checks before promotion.

</aside>

```yaml
page_contract:
  purpose: "Define FRE as an auditable, portable engineering method."
  inputs:
    - "Harness Lab + Portable Harness Package"
    - "Traceability audit findings"
  outputs:
    - "Method spec"
    - "Envelope templates"
    - "Gate definitions"
  validation_tie_in:
    gates: ["Contract validation", "Drift detection", "Publish decision"]
    checks:
      - "Method is versioned"
      - "Templates are present"
  failure_modes:
    - "Method drifts without versioning"
    - "No machine-readable governance"
  upstream:
    update_artifact: "FRE method update artifact"
    proposal_path: "Patch + validate + record keep/revert"
```

---

## 1) Definition

**FRE = RDD + SDD + TDD + META-HARNESS + AUTORESEARCH + Agent Teams + Living Documents**.

In practice:

- **Research** precedes implementation when authoritative sources exist.
- **Specifications & schemas** are the authority surface.
- **Tests & evaluators** are promotion gates.
- **Docs are executable memory** (not optional narrative).
- The **harness** (rules, validators, routing, logs) is part of the product.

## 2) Core loop (the canonical iteration)

1. **Research intake** (sources + conflicts + pins)
2. **Spec update** (contracts first)
3. **Task generation** (small, measurable)
4. **Bounded execution** (limited write targets)
5. **Evaluation** (tests + scorecards)
6. **Promotion decision** (keep / revert / investigate)
7. **Repair + upstream** (failures become durable artifacts)

## 3) Authority chain (non-negotiable)

```
sources
  -> research docs
  -> specs + schemas
  -> tests + evaluators
  -> implementation
  -> evaluation results
  -> promotion decision
```

Models/agents are execution resources, not authority.

## 4) Required artifact families (minimum)

- `docs/research/` (source-map, version matrix, open questions)
- `docs/specs/` (architecture + schemas + policies)
- `docs/golden-paths/` (validated procedures)
- `docs/evals/` (scorecards, benchmarks, sprint reviews)
- `docs/diagrams/` (system context + validation flow)
- `tests/` (contracts, scenarios, regression, fixtures)
- `harness/` (manifests, evaluators, promotion/repair logs)

## 5) Roles (agent teams / human teams)

Each role must have a contract: mission, IO, prohibited actions, gates, escalation triggers.

- Research
- Spec
- Builder
- Test
- Eval
- Repair
- Librarian
- Promotion controller

## 6) The governed document envelope (portable contract)

To be machine-governed, every **governed markdown document** must be “envelope-compliant”:

### 6.1 Required structure

1. **YAML front matter** at the top
2. **Markdown body**
3. `---bottom-matter---` sentinel
4. **YAML bottom matter** at the end

### 6.2 Minimal front matter (template)

```yaml
---
id: <UNIQUE-ID>
slug: <kebab-case>
title: <title>
doctype: <proposal|spec|golden-path|eval|task|diagram|policy>
status: <draft|active|validated|governing|stale|superseded>
version: <semver>
owner: <role/team>
created_at: YYYY-MM-DD
updated_at: YYYY-MM-DD
validated_at: YYYY-MM-DD
depends_on: []
related_tests: []
sources: []
---
```

### 6.3 Minimal bottom matter (template)

```yaml
---bottom-matter---
status_summary:
  completeness: 0.0
  confidence: low
  doc_state: draft
open_questions: []
improvement_targets: []
missing_sections: []
pending_validations: []
todo: []
checklist: []
promotion_criteria: []
blocked_by: []
next_iteration:
  owner: <role>
  target_date: YYYY-MM-DD
  objective: <one line>
change_triggers: []
source_refresh_needed: false
retire_when: []
```

## 7) FRE validation gates (minimum set)

These gates must run before promotion:

1. **Envelope gate**: every governed markdown file has front matter + bottom matter.
2. **Source gate**: material claims have source records; freshness pins exist.
3. **Spec authority gate**: changes trace to a governing spec section.
4. **Schema/example gate**: every artifact type has schema + example.
5. **Test gate**: required tests/scenarios pass OR explicit waiver exists.
6. **Doc parity gate**: docs/diagrams/golden paths updated in same iteration.
7. **Promotion gate**: scorecard thresholds pass + decision recorded.

## 8) How this integrates with the Harness Lab

FRE is the “method layer” that the Harness Lab uses to:

- bootstrap projects from the Portable Harness Package,
- enforce machine-readable governance (contracts + envelopes),
- run evaluation gates and record keep/revert decisions,
- upstream improvements back into the template/harness.

---

## 9) Agent prompt contracts (governed execution layer)

Prompting for agent execution is itself a governed artifact inside FRE. Agent prompts are not ad hoc instructions; they are executable contracts that sit between specs and bounded execution.

### 9.1 Purpose

- Standardize heavy-run prompting across Copilot, Codex, Claude, and other capable agents.
- Keep execution aligned with FRE authority order: sources -> research -> specs -> tests -> evaluation -> promotion.
- Prevent environment drift, tool drift, and fake-green execution paths.

### 9.2 Required prompt schema fields

Every governed heavy-run prompt should define at minimum:

- mode
- mission
- current_verified_state
- hard_rules
- allowed_paths
- disallowed_paths
- tasks
- validation_loop
- success_criteria
- report_contract

### 9.3 Execution policy

- Heavy autonomous runs are preferred when the task boundary is clear.
- Prompts should instruct the agent to complete the full bounded loop in one run when feasible: inspect -> patch -> test -> proof -> fix -> rerun -> artifact refresh -> docs sync -> commit.
- Prompt contracts must explicitly separate acceptable fallback from success.
- Blocked states must remain honest and evidence-backed.

### 9.4 Environment rules

- Python environment and package management must default to `uv`.
- Prefer `uv run`, `uv run --project <project>`, `uv sync`, `uv add`, and `uvx`.
- Do not default to `pip`, `python -m pip`, `venv`, or `virtualenv` unless `uv` is first proven insufficient.
- Execution prompts should include explicit runtime/tooling rules when repo boundaries are sensitive.

### 9.5 Provider/runtime policy

- Do not use paid-model API keys as the default execution path when subscribed agent surfaces already exist.
- Prefer subscribed execution surfaces such as `gh copilot -p` when the task is being delegated to Copilot.
- If a capability truly requires a paid runtime key and no approved subscribed path exists, the result should remain blocked rather than silently introducing a new dependency.

### 9.6 FRE integration

Prompt contracts belong to the FRE governed stack because they affect:

- reproducibility
- evaluation integrity
- repair quality
- promotion decisions
- cross-agent portability

They should be versioned, templated, and validated just like schemas, scorecards, and governed markdown envelopes.

### 9.7 Meta-Harness implication

The Meta-Harness should treat prompt schemas and heavy-run prompt templates as first-class governed artifacts. A prompt schema is part of the execution harness, not just operator convenience.

### 9.8 Repo-local canonical artifacts

These Notion definitions should stay aligned with the repo-local source artifacts:

- `/Volumes/PixelTable/VW_iTwin_Bridge/VW_iTwin_Bridge/meta/harness/docs/specs/agent-heavy-run-prompt-index.md`
- `/Volumes/PixelTable/VW_iTwin_Bridge/VW_iTwin_Bridge/meta/harness/docs/specs/agent-heavy-run-prompt-schema.md`
- `/Volumes/PixelTable/VW_iTwin_Bridge/VW_iTwin_Bridge/meta/harness/docs/specs/agent-heavy-run-prompt.schema.json`
- `/Volumes/PixelTable/VW_iTwin_Bridge/VW_iTwin_Bridge/meta/harness/docs/specs/agent-heavy-run-prompt.template.yaml`

Use the index file as the single repo-local entrypoint. The repo-local artifacts are the executable reference set for Meta-Harness use, while this Notion page is the governed method explanation layer.

## 10) Next actions to finish FRE (promotion-ready)

- Normalize key method docs into envelope-compliant governed markdown templates.
- Add a `source-map` registry + schema.
- Add a `scorecard` schema + first scorecard instance.
- Add an “envelope linter” check to the validation sequence.
- Add governed prompt-schema validation and template examples to the Meta-Harness reference set.
- Run one pilot: promote 1 spec from draft → active using full gates.

[fre-meta-harness-reference-dashboard](fre-meta-harness-reference-dashboard%201dec487604f48309b1008199e55dae4b.md)

[FRE Harness — Agent Entry Point (Read First)](FRE%20Harness%20%E2%80%94%20Agent%20Entry%20Point%20(Read%20First)%20925c487604f482f6903601dfc8ac948e.md)