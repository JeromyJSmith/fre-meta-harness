# Finishing Touches — Golden Plan (portable harness package)

<aside>
🧷

This is the **golden plan** to “tie the bow” on the Harness package: make it portable (computer/filesystem/user agnostic), fully specified (schemas/examples/validators), and onboardable.

</aside>

## Plan file (portable): `finishing-touches.plan.md`

```markdown
---
name: Finishing Touches — Portable Harness Package
status: draft
owners:
  - planning-agent
version: 0.1.0
lastUpdated: 2026-05-15
overview: Solidify the harness so it is platform-agnostic, user-agnostic, and self-improving via goal.md + golden-path.md + schemas + spec compiler.
---

# 0) Inputs (confirm once)
- Target portability baseline:
	- macOS + Linux first (Windows later) OR all three now
- Execution runtime assumption:
	- Claude Code (primary) + “works without it” (docs-only mode)
- Artifact storage:
	- repo-only (preferred) vs allow optional `~/.claude` additions

# 1) Lock the nucleus (goal + golden path + sources + memory)
## 1.1 goal.md v1
- Define primary metric: `goal_pass_rate`
- Define secondary metrics: `time_to_green`, `manual_interventions`, `tokens_spent_proxy`
- Define keep/revert rule: no regressions on primary; bounded regressions on secondary

## 1.2 golden-path.md v1
- “Fresh clone to green” steps
- Exact commands
- Known failure modes + fixes

## 1.3 sources.md v1
- Pin Claude Code spec links + version pin fields
- Pin skills provenance policy (skills.sh installs must be recorded)

## 1.4 memory.md v1
- Invariants + decisions
- Drift prevention rule (what must trigger a run note)

# 2) Make the filesystem truly portable
## 2.1 Canonical repo layout
- docs/harness/
- docs/spec/
- schemas/
- examples/
- reports/
- compiler/
- runs/
- .claude/

## 2.2 Path portability rules
- No absolute paths in committed files
- All paths relative to repo root
- Use env vars for local machine differences

## 2.3 Config layering contract
- Committed defaults: `.claude/settings.json`
- Local overrides: `.claude/settings.local.json` (auto-gitignored)
- Secrets: referenced, never committed (documented in sources + golden path)

# 3) Finish the Spec Suite (turn outlines into real contracts)
## 3.1 Artifact Registry → schema + example
- Write `schemas/artifact-registry.schema.json`
- Create `examples/artifact-registry.json`
- Define validator procedure (tool-agnostic)

## 3.2 Action Log first (root dependency)
- Write `schemas/action-log.schema.json`
- Create `examples/action-log/actions.example.jsonl`
- Define redaction policy for logs

## 3.3 Plan schema
- Write `schemas/plan.schema.json` (frontmatter + required sections + bottom-matter block)
- Create `examples/plans/finishing-touches.plan.md`

## 3.4 Run log schema
- `schemas/run-log.schema.json`
- `examples/runs/0001.md`

## 3.5 Report specs
- `schemas/scorecard.schema.json`
- `schemas/report.schema.json`
- Example HTML report skeleton + JSON scorecard

## 3.6 Output style schema
- `schemas/output-style.schema.json`
- Example style definitions (yaml frontmatter, json scorecard, html report)

# 4) Spec Compiler (markdown → enforcement)
## 4.1 Compiler contract
- Define the compiler questions:
	- what’s missing?
	- what’s stale?
	- what broke?
	- did golden path drift?

## 4.2 Compiler outputs
- A single “compliance checklist” artifact:
	- `compiler/compliance.md`
- A single “missing artifacts report” artifact:
	- `compiler/missing.md`

# 5) Agent teams (portable, narrow, no-overlap)
## 5.1 Define the team roster
- planning-agent
- sources-agent
- golden-path-agent
- memory-agent
- evaluation-agent

## 5.2 One skill per agent
- Each agent has a single primary SKILL.md
- Skills must be pinned in sources.md

## 5.3 Tasks are files
- Each agent’s task list is a file (portable):
	- `runs/tasks/<agent>.md`

# 6) Onboarding (minimal but complete)
## 6.1 10-minute onboarding doc
- Where the contracts live
- How to run the golden path
- How to record a run
- How to propose a change safely

## 6.2 First-run walkthrough
- Do the golden path once
- Produce run report + scorecard

# 7) “Tie the bow” release
- Cut a v1 tag of the harness spec
- Freeze v1 schemas + examples
- Start v1 changelog (portable)

# Acceptance criteria
- A new machine can run the golden path to green using only repo files.
- Every artifact type has: schema + example + validator.
- The compiler can produce: compliance + missing report.
- Runs are append-only and reproducible.

```

## Bottom-matter (execution knobs)

```yaml
# plan-config (bottom matter)
run:
  iteration_budget:
    wall_clock_minutes: 20
    max_turns: 80
  quality_gate:
    required_checks:
      - "schema_validate"
      - "golden_path_green"
  logging:
    action_log: ".claude/logs/actions.jsonl"
    run_log_dir: "runs/"
  scoring:
    primary_metric: "goal_pass_rate"
    secondary_metrics:
      - "time_to_green"
      - "manual_interventions"
      - "spec_compliance"
portability:
  forbid_absolute_paths: true
  allow_os_specific_overrides: true
  secrets_policy: "no-secrets-in-repo"
```