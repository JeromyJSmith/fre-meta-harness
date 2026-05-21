#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"

uv run --isolated --with pyyaml python "$ROOT/scripts/parent_peer_mesh_runtime.py" smoke \
  --output-json "$ROOT/evaluation/tool-health/peer-mesh-local.json" \
  --log-file "$ROOT/evaluation/tool-health/peer-mesh-local.log" \
  --events-file "$ROOT/evaluation/tool-health/peer-mesh-local-events.jsonl" \
  --benchmarks-file "$ROOT/evaluation/tool-health/peer-mesh-local-benchmarks.json"
