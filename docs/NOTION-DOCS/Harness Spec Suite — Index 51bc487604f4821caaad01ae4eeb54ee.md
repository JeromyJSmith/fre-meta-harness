# Harness Spec Suite — Index

<aside>
🗂️

This is the **single entry point** for the Harness specification suite: docs, schemas, diagrams, artifact contracts, and the “spec compiler” markdown files.

</aside>

## Why this exists

- The harness should spend tokens on **work**, not on re-discovering how it works.
- Every artifact is defined by an explicit **contract** (schema + examples + validation).
- The **file system is the system**: agents are embodied as files (skills, rules, plans, run logs, schemas).

## Spec suite map (top-level)

1. **Artifact Registry** (what can exist)
2. **Schema Set** (machine-validated contracts)
3. **Output Styles** (render contracts for YAML/JSON/Markdown/HTML)
4. **Reports** (interactive HTML report specs)
5. **Diagrams** (system + dataflow + agent team)
6. **Spec Compiler** (markdown files that compile specs into runnable constraints)

## Two canonical “sevens” (do not conflate)

The suite treats these as distinct governed structures:

1. **Seven Lifecycle Gates** (governance checkpoints): harvest, registry, manifest, verification, state, health, promotion.
2. **Seven-part Proof Package** (durable evidence bundle): source, schema, examples, expected-failures, tests, evaluation, promotion.

These two structures are portable contracts that must exist in-repo (Markdown + JSON Schema) and must be kept in sync with any wrapper docs.

## Naming conventions (canonical)

- Specs live in `docs/spec/`
- Schemas live in `schemas/`
- Reports live in `reports/`
- Compiler rules live in `compiler/`

## Portability rule (hard)

- Any structure described here is only “real” when represented as **files in the portable package** (exportable + repo-checkable).
- Notion pages are the design surface; the repo is the enforcement surface.

## Canonical principles

- **One artifact ⇒ one schema ⇒ one example ⇒ one validator**
- **Append-only** for run logs and evaluation history
- **Pinned provenance** for every imported skill/template

## Linked pages (created in this suite)

- notion-198 (Artifact Registry)
- notion-199 (Schema Set)
- notion-200 (Diagrams)
- notion-201 (Output Styles)
- notion-202 (Reports)
- notion-203 (Spec Compiler)

<aside>
✅

**Definition of done**: A new agent can bootstrap a project *without web research* by reading only `CLAUDE.md` + this spec suite, and validating outputs via schemas.

</aside>