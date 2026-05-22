# Prompt Tools — Tool Catalog (Prompt → Tool)

<aside>
🎯

**Purpose**: Convert prompts into **harness-consumable tools** with explicit contracts, schemas, endpoints, policies, tests, and deliverables.

</aside>

## 0) Before → After (what changes when a prompt becomes a tool)

- **Before (prompt)**: a text instruction used ad hoc in a chat/run.
- **After (tool)**: a versioned module with:
    - **Discovery** (Agent Card)
    - **API endpoint(s)** (task lifecycle)
    - **Typed inputs/outputs** (JSON Schemas)
    - **Policies + gates** (allow/block/ask, loop budgets, completion criteria)
    - **Golden tests + replay**
    - **Artifacts** (machine-readable + human-readable)
    - **Pixeltable persistence** (runs, artifacts, scores) backed by DuckDB SQL

## 1) Non-negotiables (contract)

1. Every tool has an API endpoint.
2. Every tool produces at least one **Artifact** with a declared schema.
3. Every tool has a minimal test suite (golden + policy violations).
4. Every tool emits observability events with correlation IDs.
5. Every tool writes its outputs to Pixeltable tables (artifact lake) and supports DuckDB queries.

## 2) ToolSpec template (authoring checklist)

### Identity

- toolId:
- name:
- owner:
- version:
- status: draft | active | deprecated

### Capability claims

- capabilities: CAP-xxxx…
- constraints:
- evidence links (tests / examples):

### Inputs

- Input schema (JSON Schema):
- Required fields:
- Validation rules:

### Outputs (Artifacts)

- Artifact list:
- Each artifact:
    - artifactType
    - schemaRef
    - contentType (application/json, text/markdown, …)
    - storage table (Pixeltable)

### API surface (endpoint-first)

- Discovery: GET /.well-known/agent.json
- Invoke: POST /v1/tools/{toolId}/tasks
- Status: GET /v1/tasks/{taskId}
- Artifacts: GET /v1/tasks/{taskId}/artifacts

### Policies + gates

- allow/block/ask rules:
- message-boundary policies:
- completion criteria:
- loop budgets:

### Observability

- required events:
- correlation rules:
- cost fields:

### Tests

- golden tests:
- replay tests:
- negative tests:

## 3) Pixeltable / DuckDB storage plan (minimum)

Define (at minimum):

- tools table (ToolSpec rows)
- tasks table (task lifecycle)
- artifacts table (artifact metadata)
- events table (observability envelope)
- scores table (eval + regression)

## 4) Tasklist (first vertical slice)

- [ ]  Define ToolSpec JSON Schema
- [ ]  Define Agent Card JSON Schema
- [ ]  Define Task + Artifact schemas
- [ ]  Define OpenAPI skeleton for tool endpoints
- [ ]  Define Pixeltable tables + DuckDB queries
- [ ]  Implement 1 tool end-to-end (Capability Harvester recommended)
- [ ]  Add golden tests + policy tests
- [ ]  Emit events and render a minimal timeline view