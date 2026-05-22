# Stage 05: Wrapper Synthesis

**GATED** — Only runs when `../04_triad_review/output/promotion-or-blocker.json` contains `"decision": "promote"`.

Assemble governed handoff bundles from all prior stage outputs.

## Inputs

| Source | File/Location | Section/Scope | Why |
|--------|--------------|---------------|-----|
| Gate check | `../04_triad_review/output/promotion-or-blocker.json` | `decision` field | STOP if not "promote" |
| Stage 04 | `../04_triad_review/output/dispatch-message.md` | Full file | Scope and target for the bundle |
| Stage 02 | `../02_research_harvest/output/` | All artifacts | Capability evidence to bundle |
| Stage 03 | `../03_semantic_cartography/output/` | All artifacts | Semantic context to bundle |
| Reference | `references/delegation-bundle.yaml` | Full file | Bundle schema |
| Config | `../../_config/agent-roles.md` | Runtime roles section | Target roles for bundle routing |

## Process

1. **Read** `../04_triad_review/output/promotion-or-blocker.json` — if `decision != "promote"`, STOP and return the blocker
2. Read dispatch-message.md for project ID and target runtime roles
3. Collect all evidence artifacts from stages 01–04
4. Assemble bundle following `references/delegation-bundle.yaml` schema
5. Validate bundle: all required fields present, no missing artifacts referenced
6. Write bundle to `output/handoff-bundles/<project-id>.bundle.json`

## Audit

| Check | Pass Condition |
|-------|---------------|
| Gate cleared | promotion-or-blocker.json shows "promote" |
| All stages represented | Bundle contains artifacts from all four prior stages |
| Schema valid | Bundle passes delegation-bundle.yaml required fields |
| No overclaim | Bundle does not imply Pixeltable sync or child-runtime activation |

## Outputs

| Artifact | Path | Description |
|----------|------|-------------|
| Handoff bundle | `output/handoff-bundles/<project-id>.bundle.json` | Governed bundle ready for runtime handoff |
