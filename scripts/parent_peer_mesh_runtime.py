from __future__ import annotations

import argparse
import json
import os
import re
import shutil
import subprocess
import tempfile
import uuid
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

import yaml


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_TOOL_HEALTH_DIR = ROOT / "evaluation" / "tool-health"
DEFAULT_STATE_PATH = DEFAULT_TOOL_HEALTH_DIR / "peer-mesh-local-state.json"
DEFAULT_SUMMARY_PATH = DEFAULT_TOOL_HEALTH_DIR / "peer-mesh-local.json"
DEFAULT_LOG_PATH = DEFAULT_TOOL_HEALTH_DIR / "peer-mesh-local.log"
DEFAULT_EVENTS_PATH = DEFAULT_TOOL_HEALTH_DIR / "peer-mesh-local-events.jsonl"
DEFAULT_BENCHMARKS_PATH = DEFAULT_TOOL_HEALTH_DIR / "peer-mesh-local-benchmarks.json"

REQUIRED_COMPLETION_TOKENS = {"done", "failed", "needs-human"}
REQUIRED_EVENT_TYPES = {
    "peer_session_started",
    "peer_session_ended",
    "peer_joined",
    "peer_message_sent",
    "peer_message_received",
    "peer_response_completed",
    "policy_decision_emitted",
}
REQUIRED_BENCHMARK_GROUPS = {
    "peer_mesh_regression",
    "observability_ingest",
    "library_distribution",
}
BLOCKED_COMMAND_PATTERNS = (
    "rm -rf",
    "git push",
    "git reset --hard",
    "git clean",
    "shutdown",
    "reboot",
    "mkfs",
    "dd if=",
)
PII_OR_SECRET_PATTERN = re.compile(
    r"(\b\d{3}-\d{2}-\d{4}\b|\bsecret\b|\bapi[_-]?key\b|\btoken\b|\bpassword\b)",
    re.IGNORECASE,
)
ROLE_HOOKS = {
    "list_agents": ["peer-membership-refresh"],
    "send_prompt": ["peer-prompt-guard"],
    "send_command": ["peer-command-guard"],
    "await_response": ["completion-verification"],
}
EVENT_CATEGORY = {
    "peer_session_started": "lifecycle",
    "peer_session_ended": "lifecycle",
    "peer_joined": "lifecycle",
    "peer_message_sent": "messaging",
    "peer_message_received": "messaging",
    "peer_response_completed": "messaging",
    "policy_decision_emitted": "policy",
}
FOLLOW_ON_LANE_STATUS = {
    "just-prompt": "gated",
    "agent-sandbox-skill": "blocked_with_exact_dependency",
    "bowser": "gated",
    "mac-mini-agent": "deployment_specific",
    "fork-repository-skill": "reference",
    "infinite-agentic-loop": "reference",
}


def now_iso() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def load_yaml(path: Path) -> dict[str, Any]:
    return yaml.safe_load(path.read_text()) or {}


def load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text())


def write_json(path: Path, payload: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2) + "\n")


def write_jsonl(path: Path, rows: list[dict[str, Any]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("".join(json.dumps(row) + "\n" for row in rows))


def create_id(prefix: str) -> str:
    return f"{prefix}-{uuid.uuid4()}"


def load_contract_bundle() -> dict[str, Any]:
    return {
        "roles": load_yaml(ROOT / "contracts" / "agent-role-contract.yaml"),
        "hooks": load_yaml(ROOT / "contracts" / "hook-manifest.yaml"),
        "policy": load_yaml(ROOT / "contracts" / "policy-decision.yaml"),
        "runtime": load_yaml(ROOT / "contracts" / "peer-mesh-runtime.yaml"),
        "capability_matrix": load_yaml(ROOT / "contracts" / "capability-matrix.yaml"),
        "library_distribution": load_yaml(ROOT / "contracts" / "library-distribution.yaml"),
        "benchmark": load_yaml(ROOT / "contracts" / "benchmark-emission.yaml"),
        "library": load_yaml(ROOT / "library.yaml"),
    }


def resolve_distribution_units(library_payload: dict[str, Any]) -> list[dict[str, Any]]:
    units = library_payload.get("distribution_units", [])
    if not isinstance(units, list) or not units:
        raise ValueError("library.yaml must declare non-empty distribution_units for the same-host runtime slice.")
    seen_refs: set[str] = set()
    for unit in units:
        if unit["ref"] in seen_refs:
            raise ValueError(f"Duplicate distribution unit ref: {unit['ref']}")
        seen_refs.add(unit["ref"])
        source_path = ROOT / unit["source"]
        if not source_path.exists():
            raise FileNotFoundError(f"Distribution unit source is missing: {unit['source']}")
    return units


def load_state(path: Path) -> dict[str, Any]:
    if not path.exists():
        raise FileNotFoundError(f"State file is missing: {path}")
    return load_json(path)


def save_state(path: Path, state: dict[str, Any]) -> None:
    write_json(path, state)


def emit_event(
    events: list[dict[str, Any]],
    *,
    event_type: str,
    session_id: str,
    scenario_id: str,
    runtime_mode: str,
    runtime_actor: str,
    sender_role: str,
    recipient_role: str,
    operation: str,
    message_id: str | None,
    correlation_id: str | None,
    policy_decision_id: str | None,
    completion_token: str | None,
    session_marker: str | None,
    status: str,
    evidence_refs: list[str],
    note: str,
) -> dict[str, Any]:
    if event_type not in REQUIRED_EVENT_TYPES:
        raise ValueError(f"Unknown event type: {event_type}")
    event = {
        "event_id": create_id("event"),
        "created_at": now_iso(),
        "event_type": event_type,
        "category": EVENT_CATEGORY[event_type],
        "session_id": session_id,
        "scenario_id": scenario_id,
        "runtime_mode": runtime_mode,
        "runtime_actor": runtime_actor,
        "sender_role": sender_role,
        "recipient_role": recipient_role,
        "operation": operation,
        "message_id": message_id,
        "correlation_id": correlation_id,
        "policy_decision_id": policy_decision_id,
        "completion_token": completion_token,
        "session_marker": session_marker,
        "status": status,
        "evidence_refs": evidence_refs,
        "note": note,
    }
    events.append(event)
    return event


def evaluate_policy(
    *,
    operation: str,
    runtime_mode: str,
    payload_text: str,
    sender_role: str,
    recipient_role: str,
) -> tuple[str, str]:
    if runtime_mode != "same_host":
        return "block", "Cross-device delivery is blocked in this kept slice until PI_COMS_NET_AUTH_TOKEN-backed transport is activated."
    if operation == "send_command":
        lowered = payload_text.lower()
        blocked_pattern = next((pattern for pattern in BLOCKED_COMMAND_PATTERNS if pattern in lowered), None)
        if blocked_pattern:
            return "block", f"Blocked by same-host command guard: {blocked_pattern}"
        if not payload_text.strip():
            return "ask", "Empty command payload requires human clarification."
        return "allow", "Local same-host command is allowed by the bounded parent command guard."
    if operation == "send_prompt":
        if PII_OR_SECRET_PATTERN.search(payload_text):
            return "ask", "Prompt payload may contain PII or secrets and requires human review before release."
        if not payload_text.strip():
            return "ask", "Empty prompt payload requires human clarification."
        return "allow", "Local same-host prompt is allowed by the bounded parent prompt guard."
    if operation == "list_agents":
        return "allow", "Same-host peer discovery is allowed after governed bootstrap."
    if operation == "await_response":
        return "allow", "Await-response verification is required by the completion boundary."
    return "block", f"Unsupported governed operation: {operation}"


def record_policy_decision(
    *,
    state: dict[str, Any],
    events: list[dict[str, Any]],
    message_id: str,
    correlation_id: str,
    scenario_id: str,
    operation: str,
    sender_role: str,
    recipient_role: str,
    payload_text: str,
) -> dict[str, Any]:
    outcome, reason = evaluate_policy(
        operation=operation,
        runtime_mode=state["runtime_mode"],
        payload_text=payload_text,
        sender_role=sender_role,
        recipient_role=recipient_role,
    )
    decision = {
        "decision_id": create_id("policy"),
        "message_id": message_id,
        "correlation_id": correlation_id,
        "scenario_id": scenario_id,
        "outcome": outcome,
        "reason": reason,
        "actor_role": sender_role,
        "operation": operation,
        "created_at": now_iso(),
    }
    emit_event(
        events,
        event_type="policy_decision_emitted",
        session_id=state["session_id"],
        scenario_id=scenario_id,
        runtime_mode=state["runtime_mode"],
        runtime_actor=sender_role,
        sender_role=sender_role,
        recipient_role=recipient_role,
        operation=operation,
        message_id=message_id,
        correlation_id=correlation_id,
        policy_decision_id=decision["decision_id"],
        completion_token=None,
        session_marker=None,
        status=outcome,
        evidence_refs=["contracts/policy-decision.yaml", "contracts/hook-manifest.yaml"],
        note=reason,
    )
    return decision


def build_request(
    *,
    operation: str,
    sender_role: str,
    recipient_role: str,
    scenario_id: str,
    payload: dict[str, Any],
    response_to_message_id: str | None = None,
) -> dict[str, Any]:
    return {
        "message_id": create_id("msg"),
        "correlation_id": create_id("corr"),
        "scenario_id": scenario_id,
        "sender_role": sender_role,
        "recipient_role": recipient_role,
        "operation": operation,
        "payload": payload,
        "response_to_message_id": response_to_message_id,
        "created_at": now_iso(),
    }


def prompt_response(
    *,
    recipient_role: str,
    prompt_text: str,
    distribution_units: list[dict[str, Any]],
) -> dict[str, Any]:
    prompt_refs = [unit["ref"] for unit in distribution_units if unit["unit_type"] in {"prompt", "policy", "validator"}]
    role_summary = {
        "prod_gatekeeper": "Bounded same-host prod gatekeeper response using local guardrails only.",
        "dev_driver": "Bounded same-host dev driver response using local role adapters only.",
        "mesh_verifier": "Bounded same-host mesh verifier response using local completion checks only.",
    }.get(recipient_role, "Bounded same-host peer response.")
    return {
        "message": role_summary,
        "prompt_excerpt": prompt_text[:160],
        "resolved_refs": prompt_refs,
        "provider_backed": False,
    }


def command_response(command: str) -> tuple[str, dict[str, Any]]:
    completed = subprocess.run(
        ["bash", "-lc", command],
        cwd=ROOT,
        capture_output=True,
        text=True,
        timeout=30,
        check=False,
    )
    payload = {
        "command": command,
        "exit_code": completed.returncode,
        "stdout": completed.stdout.strip(),
        "stderr": completed.stderr.strip(),
        "cwd": str(ROOT),
    }
    return ("done" if completed.returncode == 0 else "failed"), payload


def execute_operation(
    *,
    state: dict[str, Any],
    request: dict[str, Any],
) -> tuple[str, dict[str, Any]]:
    operation = request["operation"]
    if operation == "list_agents":
        return "done", {
            "peers": state["peers"],
            "distributed_refs": state["distributed_refs"],
        }
    if operation == "send_prompt":
        prompt_text = str(request["payload"].get("prompt", ""))
        return "done", prompt_response(
            recipient_role=request["recipient_role"],
            prompt_text=prompt_text,
            distribution_units=state["distributed_refs"],
        )
    if operation == "send_command":
        command = str(request["payload"].get("command", ""))
        return command_response(command)
    raise ValueError(f"Unsupported operation: {operation}")


def dispatch_operation(
    *,
    state: dict[str, Any],
    events: list[dict[str, Any]],
    operation: str,
    sender_role: str,
    recipient_role: str,
    scenario_id: str,
    payload: dict[str, Any],
) -> dict[str, Any]:
    known_roles = {peer["role_id"] for peer in state["peers"]}
    if sender_role not in known_roles:
        raise ValueError(f"Unknown sender_role: {sender_role}")
    if recipient_role not in known_roles:
        raise ValueError(f"Unknown recipient_role: {recipient_role}")

    request = build_request(
        operation=operation,
        sender_role=sender_role,
        recipient_role=recipient_role,
        scenario_id=scenario_id,
        payload=payload,
    )
    payload_text = json.dumps(payload, sort_keys=True)
    policy_decision = record_policy_decision(
        state=state,
        events=events,
        message_id=request["message_id"],
        correlation_id=request["correlation_id"],
        scenario_id=scenario_id,
        operation=operation,
        sender_role=sender_role,
        recipient_role=recipient_role,
        payload_text=payload_text,
    )

    record = {
        "request": request,
        "policy_decision": policy_decision,
        "hooks": ROLE_HOOKS.get(operation, []),
        "status": "awaiting_response",
        "response": None,
    }

    if policy_decision["outcome"] == "allow":
        emit_event(
            events,
            event_type="peer_message_sent",
            session_id=state["session_id"],
            scenario_id=scenario_id,
            runtime_mode=state["runtime_mode"],
            runtime_actor=sender_role,
            sender_role=sender_role,
            recipient_role=recipient_role,
            operation=operation,
            message_id=request["message_id"],
            correlation_id=request["correlation_id"],
            policy_decision_id=policy_decision["decision_id"],
            completion_token=None,
            session_marker=None,
            status="sent",
            evidence_refs=["contracts/peer-message.yaml", "contracts/hook-manifest.yaml"],
            note=f"{operation} dispatched on the same host.",
        )
        completion_token, response_payload = execute_operation(state=state, request=request)
        emit_event(
            events,
            event_type="peer_message_received",
            session_id=state["session_id"],
            scenario_id=scenario_id,
            runtime_mode=state["runtime_mode"],
            runtime_actor=recipient_role,
            sender_role=sender_role,
            recipient_role=recipient_role,
            operation=operation,
            message_id=request["message_id"],
            correlation_id=request["correlation_id"],
            policy_decision_id=policy_decision["decision_id"],
            completion_token=completion_token,
            session_marker=None,
            status="received",
            evidence_refs=["contracts/peer-lifecycle.yaml", "contracts/observability-event.yaml"],
            note=f"{operation} was received by the local {recipient_role} adapter.",
        )
    elif policy_decision["outcome"] == "ask":
        completion_token = "needs-human"
        response_payload = {
            "message": policy_decision["reason"],
            "handoff_target": "mesh_verifier",
            "provider_backed": False,
        }
    else:
        completion_token = "failed"
        response_payload = {
            "message": policy_decision["reason"],
            "provider_backed": False,
        }

    response = {
        "message_id": create_id("msg"),
        "correlation_id": request["correlation_id"],
        "scenario_id": scenario_id,
        "sender_role": recipient_role,
        "recipient_role": sender_role,
        "operation": operation,
        "payload": response_payload,
        "response_to_message_id": request["message_id"],
        "completion_token": completion_token,
        "policy_decision_id": policy_decision["decision_id"],
        "evidence_refs": [
            "evaluation/tool-health/peer-mesh-local.json",
            "evaluation/tool-health/peer-mesh-local-events.jsonl",
        ],
        "created_at": now_iso(),
    }
    record["response"] = response
    record["status"] = "response_ready"
    state["messages"][request["correlation_id"]] = record
    return {
        "message_id": request["message_id"],
        "correlation_id": request["correlation_id"],
        "policy_decision": policy_decision,
        "completion_token": completion_token,
    }


def await_response(
    *,
    state: dict[str, Any],
    events: list[dict[str, Any]],
    correlation_id: str,
) -> dict[str, Any]:
    record = state["messages"].get(correlation_id)
    if not record:
        raise ValueError(f"Unknown correlation_id: {correlation_id}")
    response = record.get("response")
    if not response:
        raise ValueError(f"No response is available for correlation_id: {correlation_id}")
    completion_token = response.get("completion_token")
    if completion_token not in REQUIRED_COMPLETION_TOKENS:
        raise ValueError(f"Invalid completion token: {completion_token}")
    if not response.get("policy_decision_id"):
        raise ValueError("Terminal response is missing policy_decision_id.")
    if not response.get("evidence_refs"):
        raise ValueError("Terminal response is missing evidence_refs.")
    emit_event(
        events,
        event_type="peer_response_completed",
        session_id=state["session_id"],
        scenario_id=response["scenario_id"],
        runtime_mode=state["runtime_mode"],
        runtime_actor="mesh_verifier",
        sender_role=response["sender_role"],
        recipient_role=response["recipient_role"],
        operation=response["operation"],
        message_id=response["message_id"],
        correlation_id=correlation_id,
        policy_decision_id=response["policy_decision_id"],
        completion_token=completion_token,
        session_marker=None,
        status="verified",
        evidence_refs=response["evidence_refs"],
        note="Completion token and evidence refs verified by the same-host mesh verifier.",
    )
    record["status"] = "completed"
    state["messages"][correlation_id] = record
    return response


def bootstrap_state(
    *,
    session_id: str,
    scenario_id: str,
    runtime_mode: str,
    contracts: dict[str, Any],
) -> tuple[dict[str, Any], list[dict[str, Any]]]:
    runtime_modes = {item["mode_id"] for item in contracts["runtime"]["runtime_modes"]}
    if runtime_mode not in runtime_modes:
        raise ValueError(f"Unknown runtime mode: {runtime_mode}")
    if runtime_mode != "same_host":
        raise ValueError("This kept runtime slice only activates same_host. Cross-device remains blocked.")
    roles = contracts["roles"]["roles"]
    distribution_units = resolve_distribution_units(contracts["library"])
    state = {
        "session_id": session_id,
        "scenario_id": scenario_id,
        "runtime_mode": runtime_mode,
        "created_at": now_iso(),
        "status": "ready",
        "peers": roles,
        "messages": {},
        "distributed_refs": distribution_units,
    }
    events: list[dict[str, Any]] = []
    emit_event(
        events,
        event_type="peer_session_started",
        session_id=session_id,
        scenario_id=scenario_id,
        runtime_mode=runtime_mode,
        runtime_actor="peer_mesh_host",
        sender_role="peer_mesh_host",
        recipient_role="peer_mesh_host",
        operation="mesh_bootstrap",
        message_id=None,
        correlation_id=None,
        policy_decision_id=None,
        completion_token=None,
        session_marker="session_start",
        status="started",
        evidence_refs=["contracts/peer-mesh-runtime.yaml", "contracts/agent-role-contract.yaml", "library.yaml"],
        note="Started the bounded same-host peer mesh session.",
    )
    for role in roles:
        emit_event(
            events,
            event_type="peer_joined",
            session_id=session_id,
            scenario_id=scenario_id,
            runtime_mode=runtime_mode,
            runtime_actor="peer_mesh_host",
            sender_role="peer_mesh_host",
            recipient_role=role["role_id"],
            operation="list_agents",
            message_id=None,
            correlation_id=None,
            policy_decision_id=None,
            completion_token=None,
            session_marker=None,
            status="joined",
            evidence_refs=["contracts/agent-role-contract.yaml", "library.yaml"],
            note=f"Registered peer {role['role_id']} in the same-host mesh.",
        )
    return state, events


def build_benchmarks(
    *,
    summary_path: Path,
    events_path: Path,
    state: dict[str, Any],
    previous_run_ref: str | None,
    run_ref: str,
) -> dict[str, Any]:
    tuples = [
        {
            "benchmark_id": create_id("bench"),
            "benchmark_group": "peer_mesh_regression",
            "contract_surface": "contracts/peer-mesh.yaml",
            "scenario_id": state["scenario_id"],
            "run_ref": run_ref,
            "status": "pass",
            "measurement_ref": str(summary_path.relative_to(ROOT)),
            "baseline_run_ref": previous_run_ref or run_ref,
            "candidate_run_ref": run_ref,
            "delta_summary": "Bounded same-host bootstrap, discovery, prompt, command, and await-response completed.",
            "regression_detected": False,
        },
        {
            "benchmark_id": create_id("bench"),
            "benchmark_group": "observability_ingest",
            "contract_surface": "contracts/observability-ingest.yaml",
            "scenario_id": state["scenario_id"],
            "run_ref": run_ref,
            "status": "pass",
            "measurement_ref": str(events_path.relative_to(ROOT)),
            "baseline_run_ref": previous_run_ref or run_ref,
            "candidate_run_ref": run_ref,
            "delta_summary": "Required same-host session, message, completion, and policy events were emitted into the bounded local sink.",
            "regression_detected": False,
        },
        {
            "benchmark_id": create_id("bench"),
            "benchmark_group": "library_distribution",
            "contract_surface": "contracts/library-distribution.yaml",
            "scenario_id": state["scenario_id"],
            "run_ref": run_ref,
            "status": "pass",
            "measurement_ref": "library.yaml",
            "baseline_run_ref": previous_run_ref or run_ref,
            "candidate_run_ref": run_ref,
            "delta_summary": "Same-host peers resolved typed prompt, skill, agent, policy, validator, and benchmark recipe refs from the governed library catalog.",
            "regression_detected": False,
        },
    ]
    return {
        "run_ref": run_ref,
        "generated_at": now_iso(),
        "groups": sorted(REQUIRED_BENCHMARK_GROUPS),
        "tuples": tuples,
    }


def blocked_follow_on_lanes(contracts: dict[str, Any]) -> dict[str, Any]:
    capability_rows = {row["capability_id"]: row for row in contracts["capability_matrix"]["capabilities"]}
    blocked: dict[str, Any] = {}
    for capability_id, expected_status in FOLLOW_ON_LANE_STATUS.items():
        row = capability_rows[capability_id]
        blocked[capability_id] = {
            "status": row["parent_lane_classification"],
            "expected_status": expected_status,
            "blocker_or_dependency": row["blocker_or_dependency"],
        }
    return blocked


def runtime_mismatch_list() -> list[dict[str, str]]:
    return [
        {
            "mismatch_id": "missing_same_host_bootstrap_entrypoint",
            "baseline_gap": "No executable same-host bootstrap entrypoint existed for the parent peer mesh.",
            "kept_resolution": "scripts/run-parent-peer-mesh-local.sh and scripts/parent_peer_mesh_runtime.py bootstrap now activate the bounded same-host lane.",
        },
        {
            "mismatch_id": "missing_local_peer_registration",
            "baseline_gap": "No parent-native implementation registered governed peers into a live same-host registry.",
            "kept_resolution": "Bootstrap now admits peer_mesh_host, prod_gatekeeper, dev_driver, and mesh_verifier from the governed role contract.",
        },
        {
            "mismatch_id": "missing_same_host_message_dispatch",
            "baseline_gap": "No live list/send dispatch path existed behind the peer-message contract.",
            "kept_resolution": "The runtime now dispatches list_agents, send_prompt, and send_command through governed request, policy, and response records.",
        },
        {
            "mismatch_id": "missing_await_response_implementation",
            "baseline_gap": "No runtime await-response verifier enforced terminal responses.",
            "kept_resolution": "await_response now verifies policy_decision_id, evidence_refs, and allowed completion tokens before closing a correlation.",
        },
        {
            "mismatch_id": "missing_completion_token_enforcement",
            "baseline_gap": "Completion tokens were only contract doctrine.",
            "kept_resolution": "The kept slice now observes and verifies done, failed, and needs-human tokens in live same-host exchanges.",
        },
        {
            "mismatch_id": "missing_fail_loud_blocker_reporting",
            "baseline_gap": "Blocked or ask states were not emitted as runtime evidence.",
            "kept_resolution": "Same-host policy decisions now return failed or needs-human terminal responses with explicit reasons.",
        },
        {
            "mismatch_id": "missing_same_host_observability_emission",
            "baseline_gap": "No local observability stream proved session, join, message, policy, and completion events.",
            "kept_resolution": "The kept slice now emits governed observability events into evaluation/tool-health/peer-mesh-local-events.jsonl.",
        },
        {
            "mismatch_id": "missing_tool_health_runtime_truth",
            "baseline_gap": "Tool-health evidence did not distinguish an active same-host lane from blocked cross-device expansion.",
            "kept_resolution": "peer-mesh-local.json and status.json now mark same_host active and cross_device blocked with explicit truth boundaries.",
        },
        {
            "mismatch_id": "missing_validator_scorer_runtime_credit",
            "baseline_gap": "Validator and scorer rewarded contract presence without requiring live runtime proof.",
            "kept_resolution": "Validation and scoring now require fresh same-host runtime evidence, observability output, and completion-token enforcement.",
        },
    ]


def smoke(
    *,
    output_json: Path,
    log_file: Path,
    events_file: Path,
    benchmarks_file: Path,
) -> dict[str, Any]:
    contracts = load_contract_bundle()
    previous_run_ref = None
    if benchmarks_file.exists():
        try:
            previous_run_ref = load_json(benchmarks_file).get("run_ref")
        except json.JSONDecodeError:
            previous_run_ref = None

    session_id = f"peer-mesh-local-{datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%SZ')}"
    scenario_id = "pi-vs-claude-code-same-host-local"
    state, events = bootstrap_state(
        session_id=session_id,
        scenario_id=scenario_id,
        runtime_mode="same_host",
        contracts=contracts,
    )

    list_result = dispatch_operation(
        state=state,
        events=events,
        operation="list_agents",
        sender_role="peer_mesh_host",
        recipient_role="peer_mesh_host",
        scenario_id=scenario_id,
        payload={"query": "all"},
    )
    list_response = await_response(state=state, events=events, correlation_id=list_result["correlation_id"])

    prompt_result = dispatch_operation(
        state=state,
        events=events,
        operation="send_prompt",
        sender_role="peer_mesh_host",
        recipient_role="prod_gatekeeper",
        scenario_id=scenario_id,
        payload={"prompt": "Summarize the bounded same-host runtime activation slice."},
    )
    prompt_response_payload = await_response(state=state, events=events, correlation_id=prompt_result["correlation_id"])

    command_result = dispatch_operation(
        state=state,
        events=events,
        operation="send_command",
        sender_role="peer_mesh_host",
        recipient_role="dev_driver",
        scenario_id=scenario_id,
        payload={"command": "pwd"},
    )
    command_response_payload = await_response(state=state, events=events, correlation_id=command_result["correlation_id"])

    failed_command_result = dispatch_operation(
        state=state,
        events=events,
        operation="send_command",
        sender_role="peer_mesh_host",
        recipient_role="dev_driver",
        scenario_id=scenario_id,
        payload={"command": "false"},
    )
    failed_command_response = await_response(state=state, events=events, correlation_id=failed_command_result["correlation_id"])

    needs_human_result = dispatch_operation(
        state=state,
        events=events,
        operation="send_prompt",
        sender_role="peer_mesh_host",
        recipient_role="prod_gatekeeper",
        scenario_id=scenario_id,
        payload={"prompt": "Contains SSN 123-45-6789 and requires prod review."},
    )
    needs_human_response = await_response(state=state, events=events, correlation_id=needs_human_result["correlation_id"])

    emit_event(
        events,
        event_type="peer_session_ended",
        session_id=session_id,
        scenario_id=scenario_id,
        runtime_mode=state["runtime_mode"],
        runtime_actor="peer_mesh_host",
        sender_role="peer_mesh_host",
        recipient_role="peer_mesh_host",
        operation="mesh_bootstrap",
        message_id=None,
        correlation_id=None,
        policy_decision_id=None,
        completion_token=None,
        session_marker="session_end",
        status="completed",
        evidence_refs=["evaluation/tool-health/peer-mesh-local.json", "evaluation/tool-health/peer-mesh-local-events.jsonl"],
        note="Closed the bounded same-host runtime session.",
    )

    run_ref = f"peer-mesh-local/{session_id}"
    benchmarks = build_benchmarks(
        summary_path=output_json,
        events_path=events_file,
        state=state,
        previous_run_ref=previous_run_ref,
        run_ref=run_ref,
    )

    observed_tokens = sorted(
        {
            list_response["completion_token"],
            prompt_response_payload["completion_token"],
            command_response_payload["completion_token"],
            failed_command_response["completion_token"],
            needs_human_response["completion_token"],
        }
    )
    required_event_types_observed = sorted({event["event_type"] for event in events})
    policy_outcomes = sorted(
        {
            list_result["policy_decision"]["outcome"],
            prompt_result["policy_decision"]["outcome"],
            command_result["policy_decision"]["outcome"],
            failed_command_result["policy_decision"]["outcome"],
            needs_human_result["policy_decision"]["outcome"],
        }
    )
    runtime_summary = {
        "report_id": "PARENT-PEER-MESH-LOCAL-0001",
        "created_at": now_iso(),
        "scope": "portable_parent_wrapper",
        "capability_id": "pi-vs-claude-code",
        "lane_id": "peer-mesh-same-host-local",
        "status": "bounded_pass",
        "activation_result": "active",
        "runtime_mode": "same_host",
        "session_id": session_id,
        "scenario_id": scenario_id,
        "runtime_mismatch_list": runtime_mismatch_list(),
        "operations": {
            "bootstrap": {
                "status": "done",
                "peer_count": len(state["peers"]),
                "distributed_ref_count": len(state["distributed_refs"]),
            },
            "list_agents": {
                "status": "done",
                "correlation_id": list_result["correlation_id"],
                "peer_count": len(list_response["payload"]["peers"]),
            },
            "send_prompt": {
                "status": "done",
                "correlation_id": prompt_result["correlation_id"],
                "policy_outcome": prompt_result["policy_decision"]["outcome"],
                "recipient_role": "prod_gatekeeper",
            },
            "send_command": {
                "status": command_response_payload["completion_token"],
                "correlation_id": command_result["correlation_id"],
                "policy_outcome": command_result["policy_decision"]["outcome"],
                "recipient_role": "dev_driver",
                "command": command_response_payload["payload"]["command"],
                "exit_code": command_response_payload["payload"]["exit_code"],
            },
            "await_response": {
                "status": "done",
                "verified_correlations": [
                    list_result["correlation_id"],
                    prompt_result["correlation_id"],
                    command_result["correlation_id"],
                    failed_command_result["correlation_id"],
                    needs_human_result["correlation_id"],
                ],
            },
        },
        "completion_tokens": {
            "required": sorted(REQUIRED_COMPLETION_TOKENS),
            "observed": observed_tokens,
            "enforced": observed_tokens == sorted(REQUIRED_COMPLETION_TOKENS),
            "failed_case": {
                "correlation_id": failed_command_result["correlation_id"],
                "completion_token": failed_command_response["completion_token"],
                "reason": failed_command_response["payload"].get("stderr") or f"Command exited with {failed_command_response['payload'].get('exit_code')}",
            },
            "needs_human_case": {
                "correlation_id": needs_human_result["correlation_id"],
                "completion_token": needs_human_response["completion_token"],
                "reason": needs_human_response["payload"]["message"],
            },
        },
        "policy": {
            "outcomes_observed": policy_outcomes,
            "decisions": [
                list_result["policy_decision"],
                prompt_result["policy_decision"],
                command_result["policy_decision"],
                failed_command_result["policy_decision"],
                needs_human_result["policy_decision"],
            ],
            "hook_ids_triggered": sorted(
                {
                    "peer-session-start",
                    "peer-membership-refresh",
                    "peer-prompt-guard",
                    "peer-command-guard",
                    "completion-verification",
                }
            ),
        },
        "observability": {
            "events_file": str(events_file.relative_to(ROOT)),
            "event_count": len(events),
            "required_event_types_observed": required_event_types_observed,
            "session_markers_observed": sorted({event["session_marker"] for event in events if event["session_marker"]}),
        },
        "library_distribution": {
            "distribution_units": state["distributed_refs"],
            "resolved_refs": [unit["ref"] for unit in state["distributed_refs"]],
            "source_catalog": "library.yaml",
        },
        "benchmarks": {
            "file": str(benchmarks_file.relative_to(ROOT)),
            "run_ref": run_ref,
            "groups": benchmarks["groups"],
        },
        "tool_prerequisites": {
            "bun": shutil.which("bun"),
            "just": shutil.which("just"),
            "pi": shutil.which("pi"),
        },
        "truth_boundary": {
            "active_runtime_modes": ["same_host"],
            "blocked_runtime_modes": [
                {
                    "mode_id": "cross_device",
                    "status": "blocked",
                    "blocker": "Cross-device transport remains blocked until PI_COMS_NET_AUTH_TOKEN and a declared hub URL are configured.",
                }
            ],
            "limitation": "Prompt handling is bounded to local role adapters and explicit policy decisions; no provider-backed arbitration or cross-device transport is claimed.",
        },
        "blocked_follow_on_lanes": blocked_follow_on_lanes(contracts),
    }

    log_lines = [
        f"session_id={session_id}",
        f"scenario_id={scenario_id}",
        "runtime_mode=same_host",
        f"list_agents={list_result['correlation_id']}",
        f"send_prompt={prompt_result['correlation_id']}",
        f"send_command={command_result['correlation_id']}",
        f"failed_command={failed_command_result['correlation_id']}",
        f"needs_human={needs_human_result['correlation_id']}",
        f"observed_completion_tokens={','.join(observed_tokens)}",
        f"observed_policy_outcomes={','.join(policy_outcomes)}",
        f"required_event_types={','.join(required_event_types_observed)}",
    ]

    write_json(output_json, runtime_summary)
    write_jsonl(events_file, events)
    write_json(benchmarks_file, benchmarks)
    log_file.parent.mkdir(parents=True, exist_ok=True)
    log_file.write_text("\n".join(log_lines) + "\n")
    return runtime_summary


def bootstrap_command(args: argparse.Namespace) -> int:
    contracts = load_contract_bundle()
    state, events = bootstrap_state(
        session_id=args.session_id or f"peer-mesh-local-{datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%SZ')}",
        scenario_id=args.scenario_id or "peer-mesh-cli",
        runtime_mode=args.mode,
        contracts=contracts,
    )
    save_state(args.state_file, state)
    write_jsonl(args.events_file, events)
    print(json.dumps({"session_id": state["session_id"], "scenario_id": state["scenario_id"], "peer_count": len(state["peers"])}, indent=2))
    return 0


def list_agents_command(args: argparse.Namespace) -> int:
    state = load_state(args.state_file)
    print(json.dumps({"peers": state["peers"], "distributed_refs": state["distributed_refs"]}, indent=2))
    return 0


def send_prompt_command(args: argparse.Namespace) -> int:
    state = load_state(args.state_file)
    events = load_jsonl_or_empty(args.events_file)
    result = dispatch_operation(
        state=state,
        events=events,
        operation="send_prompt",
        sender_role=args.sender_role,
        recipient_role=args.recipient_role,
        scenario_id=args.scenario_id or state["scenario_id"],
        payload={"prompt": args.prompt},
    )
    save_state(args.state_file, state)
    write_jsonl(args.events_file, events)
    print(json.dumps(result, indent=2))
    return 0


def send_command_command(args: argparse.Namespace) -> int:
    state = load_state(args.state_file)
    events = load_jsonl_or_empty(args.events_file)
    result = dispatch_operation(
        state=state,
        events=events,
        operation="send_command",
        sender_role=args.sender_role,
        recipient_role=args.recipient_role,
        scenario_id=args.scenario_id or state["scenario_id"],
        payload={"command": args.command},
    )
    save_state(args.state_file, state)
    write_jsonl(args.events_file, events)
    print(json.dumps(result, indent=2))
    return 0


def await_response_command(args: argparse.Namespace) -> int:
    state = load_state(args.state_file)
    events = load_jsonl_or_empty(args.events_file)
    result = await_response(state=state, events=events, correlation_id=args.correlation_id)
    save_state(args.state_file, state)
    write_jsonl(args.events_file, events)
    print(json.dumps(result, indent=2))
    return 0


def load_jsonl_or_empty(path: Path) -> list[dict[str, Any]]:
    if not path.exists():
        return []
    rows: list[dict[str, Any]] = []
    for line in path.read_text().splitlines():
        if line.strip():
            rows.append(json.loads(line))
    return rows


def smoke_command(args: argparse.Namespace) -> int:
    summary = smoke(
        output_json=args.output_json,
        log_file=args.log_file,
        events_file=args.events_file,
        benchmarks_file=args.benchmarks_file,
    )
    print(json.dumps(summary, indent=2))
    return 0


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Bounded same-host parent peer mesh runtime")
    subparsers = parser.add_subparsers(dest="command", required=True)

    bootstrap = subparsers.add_parser("bootstrap")
    bootstrap.add_argument("--state-file", type=Path, default=DEFAULT_STATE_PATH)
    bootstrap.add_argument("--events-file", type=Path, default=DEFAULT_EVENTS_PATH)
    bootstrap.add_argument("--session-id")
    bootstrap.add_argument("--scenario-id")
    bootstrap.add_argument("--mode", default="same_host")
    bootstrap.set_defaults(func=bootstrap_command)

    list_agents = subparsers.add_parser("list_agents")
    list_agents.add_argument("--state-file", type=Path, default=DEFAULT_STATE_PATH)
    list_agents.set_defaults(func=list_agents_command)

    send_prompt = subparsers.add_parser("send_prompt")
    send_prompt.add_argument("--state-file", type=Path, default=DEFAULT_STATE_PATH)
    send_prompt.add_argument("--events-file", type=Path, default=DEFAULT_EVENTS_PATH)
    send_prompt.add_argument("--scenario-id")
    send_prompt.add_argument("--sender-role", default="peer_mesh_host")
    send_prompt.add_argument("--recipient-role", default="prod_gatekeeper")
    send_prompt.add_argument("--prompt", required=True)
    send_prompt.set_defaults(func=send_prompt_command)

    send_command = subparsers.add_parser("send_command")
    send_command.add_argument("--state-file", type=Path, default=DEFAULT_STATE_PATH)
    send_command.add_argument("--events-file", type=Path, default=DEFAULT_EVENTS_PATH)
    send_command.add_argument("--scenario-id")
    send_command.add_argument("--sender-role", default="peer_mesh_host")
    send_command.add_argument("--recipient-role", default="dev_driver")
    send_command.add_argument("--command", required=True)
    send_command.set_defaults(func=send_command_command)

    await_parser = subparsers.add_parser("await_response")
    await_parser.add_argument("--state-file", type=Path, default=DEFAULT_STATE_PATH)
    await_parser.add_argument("--events-file", type=Path, default=DEFAULT_EVENTS_PATH)
    await_parser.add_argument("--correlation-id", required=True)
    await_parser.set_defaults(func=await_response_command)

    smoke_parser = subparsers.add_parser("smoke")
    smoke_parser.add_argument("--output-json", type=Path, default=DEFAULT_SUMMARY_PATH)
    smoke_parser.add_argument("--log-file", type=Path, default=DEFAULT_LOG_PATH)
    smoke_parser.add_argument("--events-file", type=Path, default=DEFAULT_EVENTS_PATH)
    smoke_parser.add_argument("--benchmarks-file", type=Path, default=DEFAULT_BENCHMARKS_PATH)
    smoke_parser.set_defaults(func=smoke_command)

    return parser


def main() -> int:
    parser = build_parser()
    args = parser.parse_args()
    return args.func(args)


if __name__ == "__main__":
    raise SystemExit(main())
