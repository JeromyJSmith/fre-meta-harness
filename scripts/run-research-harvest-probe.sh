#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
OUTPUT_DIR="$ROOT/evaluation/subsystem-runner-probes/research_harvest"

mkdir -p "$OUTPUT_DIR"

uv run --isolated --with pyyaml python "$ROOT/scripts/run_research_harvest_probe.py" \
  --output-dir "$OUTPUT_DIR"
