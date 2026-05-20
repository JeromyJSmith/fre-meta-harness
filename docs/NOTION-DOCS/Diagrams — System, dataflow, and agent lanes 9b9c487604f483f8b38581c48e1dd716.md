# Diagrams — System, dataflow, and agent lanes

## Purpose

Keep a small set of diagrams that make the harness understandable at a glance.

## Required diagrams

1. **System-as-filesystem** (root folders + contracts)
2. **Agent team lanes** (who owns what)
3. **Outer loop (meta-harness)** (propose → evaluate → keep/revert)
4. **Artifact flow** (inputs → transformations → outputs)

## Diagram formats

- Mermaid (preferred for portability)
- PNG/SVG exports (optional)

## Mermaid: System-as-filesystem (draft)

```mermaid
graph TD
	A[Repo Root] --> B[CLAUDE.md]
	A --> C[docs/harness]
	A --> D[.claude]
	A --> E[schemas]
	A --> F[reports]
	A --> G[compiler]
	C --> C1[goal.md]
	C --> C2[memory.md]
	C --> C3[golden-path.md]
	C --> C4[sources.md]
	D --> D1[settings.json]
	D --> D2[rules/]
	D --> D3[skills/]
	D --> D4[agents/]
```

## Mermaid: Outer loop (draft)

```mermaid
flowchart LR
	P[Propose change] --> R[Run golden path]
	R --> S[Score vs goal]
	S --> K{Better?}
	K -->|yes| M[Merge/promote]
	K -->|no| V[Revert]
	M --> L[Log + pin provenance]
	V --> L
	L --> P
```