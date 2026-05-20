# settings.json

```json
{
  "permissions": {},
  "hooks": {
    "PostToolUse": [
      {
        "name": "self-validate",
        "description": "After every tool use, validate required files, schemas/examples, and log compliance. This is the harness self-validation gate.",
        "command": "echo \"[self-validate] Run your validation procedure here (no-op placeholder).\""
      }
    ],
    "Stop": [
      {
        "name": "self-validate-stop",
        "description": "On stop, run a final self-validation sweep and ensure a run log entry exists.",
        "command": "echo \"[self-validate-stop] Final validation sweep (no-op placeholder).\""
      }
    ]
  },
  "env": {
    "HARNESS_VALIDATE_MODE": "baseline"
  }
}
```

<aside>
📎

**Purpose**: Project-scoped Claude runtime control surface (hooks, env, permissions). This is where “inevitability” becomes executable behavior.

**Inputs**: Harness validation sequence + required artifacts; environment command runner availability.

**Outputs**: Enforced hooks (PostToolUse / Stop) and runtime defaults for validation + logging.

**Validation tie-in**: Static checks (settings present + parseable), Observability checks (hooks produce logs), Replay tests (consistent enforcement).

**Failure modes**: Hooks are no-ops → validation becomes optional; invalid JSON breaks Claude startup.

**Update / upstream path**: Changes here must be mirrored into the template + recorded in an Update Artifact and validated via a fresh export.

</aside>

```yaml
page_contract:
  purpose: "Claude runtime control surface (project-scoped settings + hooks)."
  inputs:
    - "Validation sequence + required artifacts"
    - "Command runner environment"
  outputs:
    - "Enforced hooks (PostToolUse/Stop)"
    - "Runtime defaults (env)"
  validation_tie_in:
    gates: ["Static checks", "Observability checks", "Replay tests"]
    checks:
      - "Valid JSON"
      - "Hooks exist and are non-empty"
  failure_modes:
    - "No-op hooks -> validation not enforced"
    - "Malformed JSON -> runtime fails"
  upstream:
    update_artifact: "Settings/hook update artifact"
    proposal_path: "Patch template + rerun golden path"
```

This file is the project-scoped Claude Code settings stub. Replace the `command` bodies with your real validation runner when available in the environment.