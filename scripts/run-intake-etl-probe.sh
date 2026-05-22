#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
OUTPUT_DIR="$ROOT/evaluation/subsystem-runner-probes/intake_etl"

mkdir -p "$OUTPUT_DIR"

uv run --isolated --with pyyaml python "$ROOT/scripts/run_intake_etl_probe.py" \
  --output-dir "$OUTPUT_DIR"
