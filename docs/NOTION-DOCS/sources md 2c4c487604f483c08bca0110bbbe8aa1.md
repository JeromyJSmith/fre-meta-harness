# sources.md

## Sources + provenance (pins)

<aside>
📎

**Purpose**: Single source of truth for authoritative specs, version pins, and provenance rules (what can be trusted vs must be verified).

**Inputs**: External canonical docs; tool versions; any imported skills/templates.

**Outputs**: Auditable provenance + reproducibility pins for every run/export.

**Validation tie-in**: Drift detection (version changes), Replay tests (same inputs), Publish decision (sendable package).

**Failure modes**: Without pins, identical-looking packages behave differently; supply-chain risk becomes invisible.

**Update / upstream path**: Any new dependency/skill must be recorded here with evidence + evaluation outcome.

</aside>

```yaml
page_contract:
  purpose: "Authoritative sources + version pins + provenance rules."
  inputs: ["Canonical docs URLs", "claude --version", "Imported skills/templates metadata"]
  outputs: ["Pinned sources list", "Version pins", "Supply chain records"]
  validation_tie_in:
    gates: ["Drift detection", "Replay tests", "Publish decision"]
    checks:
      - "Pins filled for each run/export"
  failure_modes:
    - "Untracked dependency drift"
    - "Unverifiable skill provenance"
  upstream:
    update_artifact: "Sources/provenance update artifact"
    proposal_path: "Update pins + rerun validate + record in run log"
```

### Canonical Claude Code docs

- .claude directory spec: [https://code.claude.com/docs/en/claude-directory](https://code.claude.com/docs/en/claude-directory)
- skills spec: [https://code.claude.com/docs/en/skills](https://code.claude.com/docs/en/skills)
- subagents spec: [https://code.claude.com/docs/en/sub-agents](https://code.claude.com/docs/en/sub-agents)
- changelog: [https://code.claude.com/docs/en/changelog](https://code.claude.com/docs/en/changelog)

### Version pins (fill during each run)

- Claude Code version: `claude --version` →
- Export date/time:

### Skills supply chain

- Any skill installed from [skills.sh](http://skills.sh) must be recorded here with:
    - source URL
    - version/commit/date
    - evaluation result (kept/reverted)