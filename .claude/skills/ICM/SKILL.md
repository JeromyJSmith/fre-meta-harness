---
name: ICM
description: Interpretable Context Methodology — folder structure as agent architecture. Use when creating new stages, reading stage CONTEXT.md files, or understanding how this workspace routes work across numbered stage folders. Reference lib/ICM/ and lib/ICM-animation-example/ for working implementations.
---

# Interpretable Context Methodology (ICM)

arXiv:2603.16021v2 by Jake Van Clief & David McDermott (Eduba/U. Edinburgh). Folder structure IS the orchestration. Numbered stages with CONTEXT.md contracts replace framework-level orchestration.

## Reference Implementations

- `lib/ICM/` — RinDig reference implementation (`github.com/RinDig/Interpreted-Context-Methdology`)
- `lib/ICM-animation-example/` — Working example: script → spec → build pipeline

## Five-Layer Context Hierarchy

| Layer | File | Tokens | Question Answered |
|-------|------|--------|------------------|
| 0 | `CLAUDE.md` | ~800 | "Where am I?" |
| 1 | `CONTEXT.md` (root) | ~300 | "Where do I go?" |
| 2 | `stages/NN_name/CONTEXT.md` | ~200-500 | "What do I do?" |
| 3 | `stages/NN_name/references/` | varies | "What rules apply?" |
| 4 | `stages/NN_name/output/` | varies | "What am I working with?" |

## Five Principles

1. **One stage, one job** — each stage directory has exactly one clear job
2. **Plain text interface** — CONTEXT.md is markdown; everything human-readable
3. **Layered context loading** — load only what the current stage needs
4. **Every output is an edit surface** — outputs go to `output/` and are directly editable
5. **Configure factory not product** — stages/ is the template; output/ is per-run

## Stage CONTEXT.md Format

```markdown
# Stage NN: Name

One-sentence description of this stage's job.

## Inputs

| Source | File/Location | Section/Scope | Why |
|--------|--------------|---------------|-----|
| Previous stage | ../NN-1_prev/output/artifact.json | Full file | Why needed |
| Reference | references/contract.yaml | Relevant section | Why needed |

## Process

1. Step one
2. Step two
3. ...

## Audit

| Check | Pass Condition |
|-------|---------------|
| Check name | Pass condition |

## Outputs

| Artifact | Path | Description |
|----------|------|-------------|
| artifact | output/artifact.json | What it contains |
```

## This Workspace's Stages

```
stages/
  01_inbox_intake/       ← validate packet, emit routing + delegation
  02_research_harvest/   ← capability evidence + feature matrix
  03_semantic_cartography/ ← codegraph + InfraNodus
  04_triad_review/       ← ≥3 options, promote or block
  05_wrapper_synthesis/  ← GATED: assemble handoff bundles
```

## Creating a New Stage

1. Create `stages/NN_name/CONTEXT.md` following the format above
2. Create `stages/NN_name/references/` and symlink or copy contract files
3. Create `stages/NN_name/output/.gitkeep`
4. Update `CONTEXT.md` (root Layer 1) task routing table
