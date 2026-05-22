#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
OUTPUT_DIR="$ROOT/evaluation/subsystem-runner-probes/semantic_cartography"

mkdir -p "$OUTPUT_DIR"

uv run --isolated --with pyyaml python "$ROOT/scripts/run_semantic_cartography_probe.py" \
  --output-dir "$OUTPUT_DIR"
