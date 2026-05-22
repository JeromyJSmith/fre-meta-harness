#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.8"
# ///

import datetime
import json
import sqlite3
import sys
from pathlib import Path


def _iso() -> str:
    return datetime.datetime.utcnow().isoformat() + "Z"


def _write_sqlite(log_dir: Path, data: dict) -> None:
    db_path = log_dir / "observability.db"
    con = sqlite3.connect(db_path)
    con.execute(
        """CREATE TABLE IF NOT EXISTS tool_events (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            observed_at TEXT NOT NULL,
            session_id TEXT,
            tool_name TEXT,
            tool_use_id TEXT,
            payload TEXT NOT NULL
        )"""
    )
    con.execute(
        "INSERT INTO tool_events (observed_at, session_id, tool_name, tool_use_id, payload) VALUES (?,?,?,?,?)",
        (
            _iso(),
            data.get("session_id", ""),
            data.get("tool_name", ""),
            data.get("tool_use_id", ""),
            json.dumps(data),
        ),
    )
    con.commit()
    con.close()


def main():
    try:
        data = json.load(sys.stdin)

        log_dir = Path(__file__).parent.parent.parent / "logs"
        log_dir.mkdir(parents=True, exist_ok=True)

        # JSONL log (append-only, fast)
        with (log_dir / "post_tool_use.jsonl").open("a") as f:
            f.write(json.dumps(data) + "\n")

        # SQLite event store — bounded observability proof (no server required)
        _write_sqlite(log_dir, data)

        sys.exit(0)
    except Exception:
        sys.exit(0)


if __name__ == "__main__":
    main()
