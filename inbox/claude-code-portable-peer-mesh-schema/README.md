# Claude Code Portable Peer Mesh Schema

Portable YAML schema package for **Claude Code** multi-agent peer-mesh workflows.

## Included

- `claude-code-portable-peer-mesh.schema.yaml`
- `portable-peer-mesh.example.yaml`

## What it covers

- peer-to-peer agent mesh doctrine
- same-host and cross-device runtime modes
- explicit completion tokens
- agent roles
- hooks and fail-loud guardrails
- capability-to-trigger mapping

## Quick validation

Use any Draft 2020-12 validator that can load YAML. Example with Python:

```bash
python - <<'PY'
import yaml, jsonschema

with open("claude-code-portable-peer-mesh.schema.yaml") as f:
    schema = yaml.safe_load(f)
with open("portable-peer-mesh.example.yaml") as f:
    data = yaml.safe_load(f)

jsonschema.Draft202012Validator.check_schema(schema)
jsonschema.Draft202012Validator(schema).validate(data)
print("valid")
PY
```

## Intent

This package is designed for projects that do **not** already have FRE installed.
It gives you a portable starting contract for Pi-to-Pi style agent communication,
verification, hooks, and capability mapping in Claude Code.
