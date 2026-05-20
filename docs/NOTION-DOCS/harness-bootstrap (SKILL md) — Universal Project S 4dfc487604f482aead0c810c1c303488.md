# harness-bootstrap (SKILL.md) — Universal Project Setup Skill

<aside>
🎯

Use this as a universal [**SKILL.md**](http://SKILL.md) to scaffold a new project/work system with the Harness nucleus ([CLAUDE.md](http://CLAUDE.md) + goal/memory/golden-path/sources), `.claude` structure, agent team lanes, and evaluation loop.

</aside>

## Copy/paste: `SKILL.md`

```markdown
---
description: Bootstraps a repo/work system into the Harness standard (CLAUDE.md + docs/harness + .claude + agent team + plans). Use when starting any new project.
# Optional (house spec; some fields are Claude Code–specific)
# allowed-tools: [Read, Write, Edit, Bash, Glob, Grep]
# context: fork
# model: sonnet
---

## Mission
Set up a new project so it is immediately runnable, verifiable, and self-improving.

## Inputs required (ask if missing)
- Project name
- Repo/workspace root path
- Primary objective (1–2 sentences)
- Initial validation command(s) (or what “green” means)
- Constraints (time/budget/tools)

## Outputs (artifacts to create)
### A) Nucleus docs
1) `CLAUDE.md` (root)
- Link to the four nucleus docs below
- Hard rules (short)
- How to run/validate

2) `docs/harness/goal.md`
- “Done means…” acceptance criteria
- Primary metric + secondary metrics
- Iteration budget (time/turns/cost)
- Keep/revert rules

3) `docs/harness/memory.md`
- Stable facts + invariants
- Decisions that must not drift
- Rolling learnings section

4) `docs/harness/golden-path.md`
- Fresh clone → setup → run → validate → ship/handoff
- Exact commands
- Top failure modes + recovery

5) `docs/harness/sources.md`
- Authoritative specs (Claude Code docs)
- Version pins (`claude --version`, key deps)
- Skill provenance (source + version)

### B) Claude Code project config
- `.claude/settings.json` (permissions + hooks + env defaults)
- `.claude/rules/` (topic/path scoped rules)
- `.claude/agents/` (agent team definitions)
- `.claude/skills/` (one primary skill per agent)
- `.mcp.json` (if MCP servers are required)

### C) Plans
- Create `bootstrap.plan.md` (or `<project>.plan.md`) with:
  - YAML frontmatter (name, overview, status)
  - Narrative plan sections
  - Bottom-matter YAML config block (iteration budget, logging, scoring)

### D) Run history (self-improving loop)
- `runs/` folder with append-only run notes (e.g. `runs/0001.md`)
- Append-only action log location documented (recommended: `.claude/logs/actions.jsonl`)

## Agentic team lanes (default roster)
- planning-agent
- sources-agent
- golden-path-agent
- memory-agent
- evaluation-agent

## Procedure
1. Create the directory/file skeleton.
2. Write nucleus docs with minimal but complete content.
3. Create `.claude` structure + stub agent/team files.
4. Define the initial golden path and the first validation gate.
5. Create the first plan file and link it from `CLAUDE.md`.
6. Record everything in `sources.md` (pins + provenance).

## Completion criteria
- A new collaborator can follow `docs/harness/golden-path.md` end-to-end and reach a green validation.
- `goal.md` defines measurable pass/fail criteria.
- The action log location and run log convention are defined.
```

## What else to add (recommended upgrades)

1. **“Definition of Done” linter**: a checklist (or script) that verifies the nucleus files exist + required sections present.
2. **Schema for logs**: a JSON schema for `actions.jsonl` entries so downstream tooling can parse it.
3. **Security policy**: explicit rules for secrets (what must never be logged, how to redact).
4. **Skill provenance + pinning rule**: all installed skills must be pinned (source + version/date) in `sources.md`.
5. **Evaluation rubric**: a small table mapping metrics → acceptable thresholds.
6. **Drift detector**: a rule that flags when `CLAUDE.md` or nucleus docs change without a corresponding run note.