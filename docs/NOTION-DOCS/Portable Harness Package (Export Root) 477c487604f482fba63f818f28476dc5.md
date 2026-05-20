# Portable Harness Package (Export Root)

<aside>
📤

Export this page with **“Create folders for subpages”** enabled to generate a portable, filesystem-shaped package.

</aside>

<aside>
📎

**Purpose**: This page is the **export root** that generates the Portable Harness Package as a filesystem-shaped artifact (Markdown + CSV export).

**Inputs**: Harness Lab standards; child pages that represent the package tree.

**Outputs**: An exported folder tree whose root is this page; all subpages become folders/files.

**Validation tie-in**: Contract validation (required files exist); Golden path step 1–2 (fresh export → green).

**Failure modes**: Export without “Create folders for subpages” breaks portability; missing required child pages breaks bootstrapping order.

**Update / upstream path**: If the portable structure changes, update this page’s folder map and add an Update Artifact describing the diff.

</aside>

```yaml
page_contract:
  purpose: "Export root for the Portable Harness Package."
  inputs:
    - "Harness Lab standards"
    - "Child pages (package tree)"
  outputs:
    - "Portable Harness Package export (Markdown + CSV with folder tree)"
  validation_tie_in:
    gates: ["Contract validation", "Golden path"]
    checks:
      - "Export produces required paths + correct casing"
  failure_modes:
    - "Folder tree not created (export toggle off)"
    - "Missing required entrypoint pages"
  upstream:
    update_artifact: "Portable package structure update artifact"
    proposal_path: "Document diff + update folder map + validate fresh export"
```

## Export instructions

- Export format: **Markdown & CSV**
- Toggle on: **Create folders for subpages**
- Result: each subpage becomes a folder; this page is the root.

## Folder map (subpages)

- `CLAUDE.md`
- `docs/harness/goal.md`
- `docs/harness/memory.md`
- `docs/harness/golden-path.md`
- `docs/harness/sources.md`
- `.claude/settings.json`
- `.claude/rules/README.md`
- `.claude/agents/README.md`
- `.claude/skills/README.md`
- `schemas/README.md` + initial schemas
- `examples/README.md` + initial examples
- `expected-failures/README.md` + expected failures registry
- `evals/README.md` + evaluation artifacts + scorecards
- `promotion/README.md` + promotion decisions + carry-forward blockers
- `tools/README.md` + tool manifest + InfraNodus tool specs
- `skills/README.md` + governed skill/instruction registry
- `capabilities/README.md` + capability matrix + harvest schema
- `hooks/README.md` + hook manifest + InfraNodus required hooks
- `reports/README.md` + report skeleton
- `compiler/README.md` + compiler outputs
- `runs/README.md` + run log template

## Proof kernel hard requirement

The portable package is not “done” until it contains the **seven-part proof package directories**:

- `source/` (or `sources/`)
- `schemas/`
- `examples/`
- `expected-failures/`
- `tests/`
- `evals/`
- `promotion/`

These are required so evaluation and promotion remain explicit artifact layers, not implied outcomes.

<aside>
✅

**Goal**: exporting this one root page produces a complete portable package with the intended folder structure.

</aside>

<aside>
🎀

**Tie-the-bow (Sendable Checklist)**

A package is “sendable” only when all items below are true.

1) **Every page** in the Portable Harness Package includes a `page_contract` YAML block at the top.

2) A **fresh export** (Markdown & CSV + Create folders) contains all required entrypoints with correct casing (`CLAUDE.md`).

3) `schemas/` contains required schemas and `examples/` contains matching examples (1:1 pairing).

4) `compiler/` has `compliance.md` + `missing.md` (or an explicit v1 no-op + rationale).

5) `runs/0001.md` exists and links: plan, scorecard, report, action log pointer.

6) `tools/manifest.yaml`, `skills/manifest.yaml`, `capabilities/capability-matrix.yaml`, and `hooks/hook-manifest.yaml` exist and validate.

7) InfraNodus is documented as the always-on graph intelligence layer, with required abilities mapped to FRE stages.

8) `.claude/settings.json` hooks are **not** placeholders in the target environment (or clearly marked as placeholders + next step).

**Definition of done**: A stranger can export this root page and reach “green” using only the files in the export.

</aside>

[[BOOTSTRAP.md](http://BOOTSTRAP.md)](BOOTSTRAP%20md%2085ac487604f4832d919901b78a6d90d4.md)

[FS (do not read by default)](FS%20(do%20not%20read%20by%20default)%20edcc487604f483b98401019b7ad26115.md)