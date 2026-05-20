# DATABASES.md (Corporate Mac: CSV only)

## Constraint

This environment is a corporate-managed Mac where we **cannot**:

- install Xcode
- install Xcode Command Line Tools
- use Terminal / shell commands
- run developer tooling

Therefore, “local SQLite via CLI” is **not a valid assumption**.

## What to use instead (baseline-first)

### 1) CSV files (canonical database)

This environment cannot run local databases and cannot rely on Notion, so the canonical “database” is **CSV**.

#### Canonical folder

- `backend/data/`

#### Canonical files

- `backend/data/crm.csv`
- `backend/data/tasks.csv`

#### CSV rules (portable + Salesforce-adjacent)

- **One header row** (stable column names).
- **One record per row**.
- Use `id` as the primary key (string).
- Use ISO-8601 timestamps for `created_at` / `updated_at` when present.
- Never embed secrets in CSV.

#### crm.csv (v0) — Salesforce-ish shape

```
id,record_type,lead_status,account_name,contact_first_name,contact_last_name,email,phone,website,owner,source,notes,created_at,updated_at
crm_0001,Lead,New,,,,,,,,,,,
```

Field notes:

- `record_type`: `Lead|Contact|Account|Opportunity` (start with Lead/Contact/Account)
- `lead_status`: mirrors “New/Qualified/Contacted/In progress/Won/Lost” style stages

#### tasks.csv (v0)

```json
id,task,status,priority,owner,project,due_date,blocked_reason,notes,created_at,updated_at
task_0001,,Backlog,P2,,,,,,,
```

### 2) JSON as a secondary format (only for nested structures)

If a record truly needs nested fields (rare), store a parallel JSON file:

- `backend/data/crm.json` or `backend/data/tasks.json`

But CSV remains the canonical source of truth unless explicitly overridden in `goal.md` for that project.

## Rules

- Do not reference Terminal commands in golden path steps for this environment.
- Any “database” step must be achievable via simple file creation/editing in the corporate environment.
- If a project needs multiple databases, create additional CSV files under `backend/data/` and document their schemas under `schemas/`.