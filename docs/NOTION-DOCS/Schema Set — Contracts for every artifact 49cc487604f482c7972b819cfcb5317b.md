# Schema Set — Contracts for every artifact

## Purpose

Define **machine-validated schemas** for every artifact in the registry.

This includes the two canonical portable structures:

- Seven Lifecycle Gates schema
- Seven-part Proof Package schema

## Folder layout (proposed)

- `schemas/`
    - `artifact-registry.schema.json`
    - `goal.schema.json`
    - `golden-path.schema.json`
    - `sources.schema.json`
    - `action-log.schema.json`
    - `run-log.schema.json`
    - `plan.schema.json`
    - `report.schema.json`
    - `output-style.schema.json`
    - `tool.schema.json`
    - `tool-ability.schema.json`
    - `skill.schema.json`
    - `agent.schema.json`
    - `single-file-agent.schema.json`
    - `hook.schema.json`
    - `capability.schema.json`
    - `capability-manifest.schema.json`
    - `capability-matrix.schema.json`
    - `capability-harvest.schema.json`
    - `infranodus-tool.schema.json`
    - `lifecycle-gates.schema.json`
    - `proof-package.schema.json`

## Schema rules

- Schemas must be **small, composable**, and reference each other.
- Every schema ships with:
    - **1 canonical example** (`examples/<artifact>/...`)
    - **1 validator command** (documented)
    - **1 breaking-change rule** (what increments major)

## Proof-package coupling rule (hard)

- Any schema that declares a governed artifact type must also declare:
    - where its valid examples live
    - where its invalid examples / expected failures live
    - what evaluation artifacts are emitted
    - what promotion decision artifact closes the loop
- Tool, ability, skill, hook, and capability schemas must include docstrings/comments that explain what the artifact is, what it is used for, and why it exists in the harness context.

## Minimal required fields (common)

All artifacts should share:

- `schemaVersion`
- `artifactId`
- `createdAt`
- `updatedAt`
- `provenance` (sources, pins)

## Next step

Define the **action log** first (because everything else depends on it).

## Capability reboot addendum

The schema set must now support capability harvest: acquired repositories, tool libraries, and skill archives are parsed into governed tool, ability, skill, hook, and capability records before promotion.