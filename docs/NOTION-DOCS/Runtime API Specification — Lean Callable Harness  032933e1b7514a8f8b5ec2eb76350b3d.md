# Runtime API Specification — Lean Callable Harness Contract

<aside>
⚙️

**Purpose**: Define the lean runtime/API layer for the FRE Harness: the callable functions, endpoints, contracts, events, and validation rules generated from schemas, comments, docstrings, and markdown specs.

</aside>

## Verdict

Yes — this is the right next step.

The harness now has enough **specification mass**: principles, schemas, examples, lifecycle rules, folders, agents, skills, hooks, CSV database rules, and capability-harvest concepts.

The next productive stage is to compile that into a **runtime API specification**: a small, non-bloated set of callable operations that tells an agent or implementation exactly:

- what functions exist,
- what inputs they accept,
- what outputs they return,
- what artifacts they read/write,
- what validation gates they trigger,
- what hooks fire,
- what state changes,
- what errors mean,
- and how the system proves the action was valid.

This is the layer where the harness stops being only documentation and becomes an executable operating system.

## Important distinction

This “API” does **not** have to start as a network API.

It should begin as a **runtime contract API**.

That means every function can later be implemented as:

- a Claude Code skill,
- a hook,
- a local script,
- a Notion operation,
- a CSV/file operation,
- an MCP tool,
- a web endpoint,
- or an interactive/manual procedure.

The runtime API spec should be transport-agnostic first, then mapped to transports later.

## Runtime docs vs full docs

### Full docs

Full docs explain everything:

- philosophy,
- background,
- principles,
- examples,
- diagrams,
- design rationale,
- public website docs,
- contributor guides.

### Runtime docs

Runtime docs explain only what is needed to operate:

- function name,
- purpose,
- input schema,
- output schema,
- side effects,
- validation,
- failure modes,
- hook triggers,
- artifact paths,
- examples.

Runtime docs should be lean enough that a fresh agent can load them without burning context.

## Proposed folder target

Add this runtime layer to the portable package:

```
runtime/
  README.md
  api.md
  manifest.yaml
  lifecycle.md
  errors.md
  validation.md
  transports.md
  endpoints/
    bootstrap-project.endpoint.md
    validate-package.endpoint.md
    run-capability-harvest.endpoint.md
    register-tool.endpoint.md
    register-skill.endpoint.md
    register-agent.endpoint.md
    register-hook.endpoint.md
    create-run-log.endpoint.md
    score-run.endpoint.md
    promote-improvement.endpoint.md
    export-package.endpoint.md
  schemas/
    runtime-api.schema.json
    endpoint.schema.json
    request.schema.json
    response.schema.json
    error.schema.json
    event.schema.json
    lifecycle.schema.json
```

## API surface: first required endpoints

### 1) `bootstrap.project`

Creates a new project from the harness template.

```yaml
id: bootstrap.project
type: endpoint
purpose: "Generate a new project folder from the portable harness template."
reads:
  - "BOOTSTRAP.md"
  - "CLAUDE.md"
  - "docs/harness/goal.md"
  - "docs/harness/golden-path.md"
  - "docs/harness/sources.md"
  - "docs/harness/memory.md"
  - "schemas/*"
writes:
  - "projects/<project-name>/"
  - "projects/<project-name>/runs/0001.md"
inputs:
  project_name: "kebab-case string"
  purpose: "single sentence"
  green_definition: "acceptance criteria"
  constraints: "array of strings"
outputs:
  project_path: "string"
  run_log_path: "string"
  status: "created|failed"
validation:
  - "required nucleus docs exist"
  - "project folder created"
  - "run log created"
  - "no absolute paths"
hooks:
  before:
    - "validate.template"
  after:
    - "validate.project"
    - "log.action"
failure_modes:
  - "missing template"
  - "invalid project name"
  - "missing acceptance criteria"
```

### 2) `validate.package`

Validates the portable harness package.

```yaml
id: validate.package
type: endpoint
purpose: "Run the full package validation sequence and produce compiler outputs."
reads:
  - "BOOTSTRAP.md"
  - "FS/"
  - "schemas/"
  - "examples/"
  - "compiler/"
writes:
  - "compiler/compliance.md"
  - "compiler/missing.md"
  - "compiler/audit.md"
  - "compiler/drift-report.md"
inputs:
  mode: "baseline|strict|release"
outputs:
  compliance_status: "green|yellow|red"
  missing_items: "array"
  audit_path: "string"
validation:
  - "schema/example 1:1 coverage"
  - "settings hook shape"
  - "agent/skill mapping"
  - "runtime endpoint coverage"
hooks:
  after:
    - "log.action"
    - "score.run"
failure_modes:
  - "schemas without examples"
  - "invalid hook configuration"
  - "missing runtime endpoint"
```

### 3) `capability.harvest`

Turns an imported library, skill archive, or tool docs into governed harness capabilities.

```yaml
id: capability.harvest
type: endpoint
purpose: "Parse an acquired repository/library/skill archive into governed capabilities."
reads:
  - "incoming/<source>/"
  - "tools/"
  - "skills/"
  - "capabilities/"
  - "schemas/"
writes:
  - "capabilities/capability-matrix.yaml"
  - "tools/<tool-id>/tool.yaml"
  - "tools/<tool-id>/abilities/*.yaml"
  - "skills/<skill-id>/skill.yaml"
inputs:
  source_path: "string"
  source_type: "repo|archive|docs|skill|tool"
  promotion_mode: "candidate|promote"
outputs:
  harvested_capabilities: "array"
  missing_contracts: "array"
  promotion_status: "candidate|promoted|rejected"
validation:
  - "source provenance recorded"
  - "tool abilities extracted"
  - "examples exist"
  - "failure modes declared"
hooks:
  before:
    - "validate.source"
  after:
    - "validate.capability"
    - "log.action"
failure_modes:
  - "unknown source type"
  - "missing provenance"
  - "no callable ability found"
```

### 4) `runtime.register_tool`

Registers a tool as a governed runtime capability.

```yaml
id: runtime.register_tool
type: endpoint
purpose: "Add a new tool and its abilities to the runtime capability registry."
reads:
  - "schemas/tool.schema.json"
  - "schemas/tool-ability.schema.json"
writes:
  - "tools/<tool-id>/tool.yaml"
  - "tools/<tool-id>/abilities/*.yaml"
  - "tools/manifest.yaml"
inputs:
  tool_id: "kebab-case string"
  provider: "string"
  abilities: "array"
outputs:
  manifest_entry: "object"
  status: "registered|failed"
validation:
  - "tool schema validates"
  - "each ability has schema + example"
hooks:
  after:
    - "validate.package"
    - "log.action"
failure_modes:
  - "duplicate tool id"
  - "ability missing input/output contract"
```

### 5) `runtime.register_skill`

Registers a skill/instruction package.

```yaml
id: runtime.register_skill
type: endpoint
purpose: "Register a skill as a governed instruction artifact."
reads:
  - "schemas/skill.schema.json"
writes:
  - "skills/<skill-id>/skill.yaml"
  - ".claude/skills/<skill-id>/SKILL.md"
inputs:
  skill_id: "kebab-case string"
  description: "single-line description"
  primary_agent: "agent id"
outputs:
  skill_path: "string"
  runtime_skill_path: "string"
  status: "registered|failed"
validation:
  - "description is single-line"
  - "one primary agent assigned"
  - "frontmatter present"
hooks:
  after:
    - "validate.skill"
    - "log.action"
failure_modes:
  - "missing description"
  - "scope overlaps existing skill"
```

### 6) `runtime.register_agent`

Registers an agent lane.

```yaml
id: runtime.register_agent
type: endpoint
purpose: "Create a narrow-scope agent definition with one primary skill."
reads:
  - "schemas/agent.schema.json"
writes:
  - ".claude/agents/<agent-id>.md"
  - "runs/tasks/<agent-id>.md"
inputs:
  agent_id: "kebab-case string"
  scope: "string"
  primary_skill: "skill id"
outputs:
  agent_path: "string"
  task_list_path: "string"
  status: "registered|failed"
validation:
  - "scope does not overlap"
  - "primary skill exists"
  - "task list exists"
hooks:
  after:
    - "validate.agent"
    - "log.action"
failure_modes:
  - "scope collision"
  - "missing primary skill"
```

### 7) `runtime.log_action`

Appends a runtime action record.

```yaml
id: runtime.log_action
type: endpoint
purpose: "Record every meaningful action in append-only run/action history."
reads:
  - "runs/"
writes:
  - "runs/<run-id>.md"
  - ".claude/logs/actions.jsonl"
inputs:
  run_id: "string"
  action_type: "prompt|file_edit|tool_call|decision|validation|hook"
  summary: "string"
  artifacts: "array"
outputs:
  log_entry_id: "string"
  status: "logged|failed"
validation:
  - "run id exists"
  - "no secrets"
  - "artifact pointers exist"
hooks:
  after:
    - "validate.log"
failure_modes:
  - "missing run id"
  - "secret detected"
```

### 8) `runtime.score_run`

Scores a run against `goal.md`.

```yaml
id: runtime.score_run
type: endpoint
purpose: "Evaluate a run against the current goal contract."
reads:
  - "docs/harness/goal.md"
  - "runs/<run-id>.md"
  - "compiler/compliance.md"
  - "compiler/missing.md"
writes:
  - "reports/scorecard.<run-id>.json"
  - "reports/evaluation-summary.<run-id>.md"
inputs:
  run_id: "string"
outputs:
  primary_score: "number"
  secondary_scores: "object"
  decision: "keep|revert|investigate"
validation:
  - "goal metrics present"
  - "compiler outputs present"
hooks:
  after:
    - "log.action"
failure_modes:
  - "missing goal contract"
  - "missing compiler outputs"
```

### 9) `runtime.promote_improvement`

Promotes a project-level improvement back into the harness template.

```yaml
id: runtime.promote_improvement
type: endpoint
purpose: "Upstream reusable improvements into the meta-harness template."
reads:
  - "projects/<project-name>/runs/"
  - "_harness_template/"
writes:
  - "_harness_template/"
  - "BOOTSTRAP.md"
  - "docs/harness/memory.md"
inputs:
  source_project: "string"
  improvement_summary: "string"
  affected_artifacts: "array"
outputs:
  promotion_status: "kept|reverted|investigate"
  updated_artifacts: "array"
validation:
  - "run evidence exists"
  - "goal score does not regress"
  - "memory updated if invariant changed"
hooks:
  before:
    - "score.run"
  after:
    - "validate.package"
    - "log.action"
failure_modes:
  - "no evidence"
  - "score regression"
  - "template drift"
```

## Runtime API design rules

1. **Every endpoint has one job.**
2. **Every endpoint reads and writes declared artifacts only.**
3. **Every endpoint has an input schema and output schema.**
4. **Every endpoint declares hooks.**
5. **Every endpoint declares validation.**
6. **Every endpoint declares failure modes.**
7. **Every endpoint creates or updates a run/action record.**
8. **Every endpoint is transport-agnostic.**
9. **Every endpoint can be implemented later as CLI, MCP, HTTP, Notion, or manual workflow.**
10. **Every endpoint must be derivable from schema comments, docstrings, and markdown contracts.**

## What may be missing before implementation

Before implementing this runtime API, confirm these decisions:

### 1) Transport priority

Which runtime transport comes first?

Recommended order:

1. Markdown contract API
2. Claude Code skill/hook API
3. Local file API
4. MCP API
5. HTTP/OpenAPI API

### 2) Runtime state model

Decide where runtime state lives:

```
runs/
.claude/logs/
compiler/
reports/
capabilities/
```

### 3) Error model

Define a shared error object:

```yaml
error:
  code: "MISSING_SCHEMA"
  message: "Artifact has no schema."
  severity: "warning|blocking"
  artifact: "schemas/example.schema.json"
  remediation: "Create matching schema and example."
```

### 4) Versioning model

Every endpoint needs:

```yaml
apiVersion: "fre.runtime.v0.1"
endpointVersion: "0.1.0"
breakingChangePolicy: "major version bump"
```

### 5) Idempotency

Every endpoint should say whether it is safe to run twice.

Examples:

```yaml
idempotency:
  mode: "safe"
  key: "project_name"
  behavior: "If project exists, validate instead of overwrite."
```

### 6) Permission model

The runtime API must know whether it can:

- read only,
- write files,
- run hooks,
- call tools,
- edit template,
- promote improvements,
- publish docs.

### 7) Public docs boundary

Separate:

```
runtime/        # what agents need to operate
docs/site/      # what humans need to understand
docs/spec/      # full rationale/specification
schemas/        # machine contracts
examples/       # canonical examples
```

## Recommended next step

Create the runtime/API page and then implement the folder in the portable package.

The page should be called:

**Runtime API Specification — Lean Callable Harness Contract**

Then add it to:

```
docs/spec/runtime-api.md
runtime/README.md
runtime/api.md
```

## Definition of done

This stage is complete when:

- `runtime/api.md` exists.
- Every endpoint has an input/output contract.
- Every endpoint maps to schemas.
- Every endpoint maps to artifacts.
- Every endpoint maps to hooks.
- Every endpoint maps to validation.
- Every endpoint maps to failure modes.
- Every endpoint logs actions.
- The compiler can report missing endpoints.
- Agents can use runtime docs without reading the full design docs.
- The API can later be compiled into OpenAPI, MCP tools, Claude Code skills, or hook workflows.