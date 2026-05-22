#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.8"
# ///

import json
import re
import sys
from pathlib import Path


def is_dangerous_rm(command):
    normalized = " ".join(command.lower().split())
    patterns = [
        r"\brm\s+.*-[a-z]*r[a-z]*f",
        r"\brm\s+.*-[a-z]*f[a-z]*r",
        r"\brm\s+--recursive\s+--force",
        r"\brm\s+--force\s+--recursive",
    ]
    for pattern in patterns:
        if re.search(pattern, normalized):
            return True
    dangerous_paths = [r"/\s*$", r"/\*", r"~", r"\$HOME", r"\.\.$"]
    if re.search(r"\brm\s+.*-[a-z]*r", normalized):
        for path in dangerous_paths:
            if re.search(path, normalized):
                return True
    return False


def is_env_access(tool_name, tool_input):
    if tool_name in ["Read", "Edit", "Write"]:
        fp = tool_input.get("file_path", "")
        if ".env" in fp and not fp.endswith(".env.sample"):
            return True
    if tool_name == "Bash":
        cmd = tool_input.get("command", "")
        if re.search(r"\.env\b(?!\.sample)", cmd):
            return True
    return False


def main():
    try:
        data = json.load(sys.stdin)
        tool_name = data.get("tool_name", "")
        tool_input = data.get("tool_input", {})

        if is_env_access(tool_name, tool_input):
            print("BLOCKED: .env access prohibited — use .env.sample", file=sys.stderr)
            sys.exit(2)

        if tool_name == "Bash":
            cmd = tool_input.get("command", "")
            if is_dangerous_rm(cmd):
                print("BLOCKED: dangerous rm command", file=sys.stderr)
                sys.exit(2)

        log_dir = Path(__file__).parent.parent.parent / "logs"
        log_dir.mkdir(parents=True, exist_ok=True)
        log_path = log_dir / "pre_tool_use.jsonl"
        with log_path.open("a") as f:
            f.write(json.dumps(data) + "\n")

        sys.exit(0)
    except Exception:
        sys.exit(0)


if __name__ == "__main__":
    main()
