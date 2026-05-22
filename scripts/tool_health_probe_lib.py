from __future__ import annotations

import json
import os
import shutil
import subprocess
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
TOOL_HEALTH_DIR = ROOT / "evaluation" / "tool-health"


@dataclass
class ProbeResult:
    command: str
    status: str
    summary: str
    evidence: list[str]
    exit_code: int | None = None
    stdout_tail: list[str] | None = None
    stderr_tail: list[str] | None = None
    missing_prerequisites: list[str] | None = None
    satisfied_prerequisites: list[str] | None = None
    observed_at: str | None = None

    def as_dict(self) -> dict:
        payload = {
            "command": self.command,
            "status": self.status,
            "summary": self.summary,
            "evidence": self.evidence,
            "observed_at": self.observed_at or now_iso(),
        }
        if self.exit_code is not None:
            payload["exit_code"] = self.exit_code
        if self.stdout_tail:
            payload["stdout_tail"] = self.stdout_tail
        if self.stderr_tail:
            payload["stderr_tail"] = self.stderr_tail
        if self.missing_prerequisites:
            payload["missing_prerequisites"] = self.missing_prerequisites
        if self.satisfied_prerequisites:
            payload["satisfied_prerequisites"] = self.satisfied_prerequisites
        return payload


def now_iso() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def load_json(path: Path) -> dict | None:
    if not path.exists():
        return None
    return json.loads(path.read_text())


def write_json(path: Path, payload: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2) + "\n")


def command_path(name: str) -> str | None:
    return shutil.which(name)


def run_command(
    command: list[str],
    *,
    log_path: Path | None = None,
    env: dict[str, str] | None = None,
    cwd: Path = ROOT,
) -> subprocess.CompletedProcess[str]:
    merged_env = os.environ.copy()
    if env:
        merged_env.update(env)
    completed = subprocess.run(
        command,
        cwd=cwd,
        env=merged_env,
        capture_output=True,
        text=True,
        check=False,
    )
    if log_path is not None:
        log_path.parent.mkdir(parents=True, exist_ok=True)
        log_path.write_text((completed.stdout or "") + (("\n" + completed.stderr) if completed.stderr else ""))
    return completed


def result_from_completed(
    command: list[str],
    completed: subprocess.CompletedProcess[str],
    *,
    evidence: list[str],
    summary: str,
    status: str | None = None,
    missing_prerequisites: list[str] | None = None,
    satisfied_prerequisites: list[str] | None = None,
) -> ProbeResult:
    derived_status = status
    if derived_status is None:
        derived_status = "pass" if completed.returncode == 0 else "fail"
    return ProbeResult(
        command=" ".join(command),
        status=derived_status,
        summary=summary,
        evidence=evidence,
        exit_code=completed.returncode,
        stdout_tail=completed.stdout.strip().splitlines()[-5:] if completed.stdout.strip() else [],
        stderr_tail=completed.stderr.strip().splitlines()[-5:] if completed.stderr.strip() else [],
        missing_prerequisites=missing_prerequisites or [],
        satisfied_prerequisites=satisfied_prerequisites or [],
    )
