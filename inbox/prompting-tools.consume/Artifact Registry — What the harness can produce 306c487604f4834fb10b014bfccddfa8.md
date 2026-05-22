# Artifact Registry — What the harness can produce

## Purpose

A canonical registry of every artifact the harness can create or update.

## Registry record template (one per artifact)

- **Artifact ID** (kebab-case)
- **Type** (doc | schema | report | config | log | plan | agent | skill | rule | style)
- **Type** (doc | schema | report | config | log | plan | agent | skill | rule | style | tool | tool-ability | capability | capability-manifest | capability-matrix | hook | single-file-agent)
- **Owner agent** (single lane owner)
- **File path(s)** (canonical locations)
- **Schema** (JSON schema file)
- **Example** (golden example file)
- **Validator** (command or procedure)
- **Versioning** (semver + changelog)
- **Provenance** (sources, pins)

## Initial artifact list (seed)

### Nucleus docs

- `claude-md`
- `goal-md`
- `memory-md`
- `golden-path-md`
- `sources-md`

### Claude Code control surface

- `claude-settings-json`
- `claude-rules-md`
- `claude-skill-md`
- `claude-agent-md`
- `mcp-json`

### Capability + tool substrate

- `tool-manifest-yaml`
- `tool-ability-yaml`
- `skill-manifest-yaml`
- `capability-matrix-yaml`
- `capability-harvest-schema`
- `hook-manifest-yaml`
- `single-file-agent-spec`
- `infranodus-tool`
- `infranodus-required-hooks`

### Planning + execution

- `plan-md`
- `action-log-jsonl`
- `run-log-md`

### Reports

- `interactive-html-report`
- `scorecard-json`
- `evaluation-summary-md`

### Wrapper governance + proof kernel (portable contract)

- `lifecycle-gates.schema.json` (Seven Lifecycle Gates schema)
- `proof-package.schema.json` (Seven-part Proof Package schema)
- `expected-failures-registry` (portable anticipated failures inventory)
- `promotion-decision` (explicit keep/revert/promote record, never implied)