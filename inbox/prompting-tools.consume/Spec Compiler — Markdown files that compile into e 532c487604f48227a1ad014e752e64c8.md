# Spec Compiler — Markdown files that compile into enforcement

## Purpose

Define a set of markdown-first “compiler specs” that convert human intent into enforceable checks.

## Compiler concept

- Inputs: `docs/harness/*`, registry, schemas, output styles
- Outputs: checklists, validators, hook configs, lint rules, and a minimal test plan

## Compiler must enforce the proof kernel

The compiler must treat the following as **durable contract** requirements, not “nice-to-have docs”:

- Seven Lifecycle Gates (governance model)
- Seven-part Proof Package (evidence model)

And it must be able to answer: for any governed layer, which proof-package parts are missing, and which lifecycle-gate checks are therefore not satisfiable.

## Folder layout (proposed)

- `compiler/`
    - `COMPILER.md` (how the compiler works)
    - `artifact-registry.compiler.md`
    - `schemas.compiler.md`
    - `output-styles.compiler.md`
    - `reports.compiler.md`
    - `plans.compiler.md`
    - `tools.compiler.md`
    - `skills.compiler.md`
    - `capabilities.compiler.md`
    - `hooks.compiler.md`

## Example: `schemas.compiler.md`

- Ensure every artifact has a schema
- Ensure every schema has an example
- Ensure every example validates

## Definition of done

The compiler can answer:

- “What artifacts are missing?”
- “What schemas are missing?”
- “What changed without a run note?”
- “Is the golden path still valid?”
- “What tools are missing from the manifest?”
- “Which tool abilities are undocumented?”
- “Which skills lack instruction specs?”
- “Which hooks lack outputs or validation gates?”
- “Was InfraNodus run or explicitly skipped for every required stage?”

## Minimum compiler outputs (portable)

- `compiler/missing.md`: missing artifacts and missing proof-package parts (by layer)
- `compiler/compliance.md`: pass/fail checklist including lifecycle-gate regressions
- `compiler/drift.md`: cross-surface drift findings (IDs, status, deps, proofs)