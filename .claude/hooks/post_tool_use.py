#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.8"
# ///

import json
import sys
from pathlib import Path


def main():
    try:
        data = json.load(sys.stdin)

        log_dir = Path(__file__).parent.parent.parent / "logs"
        log_dir.mkdir(parents=True, exist_ok=True)
        log_path = log_dir / "post_tool_use.jsonl"
        with log_path.open("a") as f:
            f.write(json.dumps(data) + "\n")

        sys.exit(0)
    except Exception:
        sys.exit(0)


if __name__ == "__main__":
    main()
