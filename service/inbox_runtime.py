from __future__ import annotations

import json
from dataclasses import dataclass
from pathlib import Path
from typing import Any

import yaml


ROOT = Path(__file__).resolve().parents[1]
INBOX_DIR = ROOT / "inbox"
TOOL_HEALTH_DIR = ROOT / "evaluation" / "tool-health"
INBOX_PROTOCOL_DIR = TOOL_HEALTH_DIR / "inbox-protocol"
PACKET_SUFFIXES = (
    ".brainstorm.md",
    ".plan.md",
    ".analysis.md",
    ".test.md",
    ".review.md",
    ".handoff.md",
    ".spec.md",
    ".checkpoint.md",
)
ROLE_IDS = {
    "orchestrator-validator",
    "research",
    "architect",
    "user-facing-agent",
    "spec-interpreter",
    "filesystem-router",
    "intake-mapper",
    "semantic-cartographer",
    "wrapper-synthesizer",
}


@dataclass
class PacketScanResult:
    packet_path: str
    packet_name: str
    front: dict[str, Any]
    bottom: dict[str, Any]
    structured: dict[str, Any] | None
    gate_states: list[dict[str, str]]
    status: str
    errors: list[str]
    resolved_consumers: list[str]


def parse_markdown_packet(path: Path) -> tuple[dict[str, Any], dict[str, Any]]:
    text = path.read_text()
    if not text.startswith("---\n"):
        raise ValueError(f"{path.name}: missing front matter start")
    _, rest = text.split("---\n", 1)
    front_raw, body = rest.split("\n---\n", 1)
    if "\n---bottom-matter---\n" not in body:
        raise ValueError(f"{path.name}: missing bottom matter marker")
    _, bottom_raw = body.split("\n---bottom-matter---\n", 1)
    return yaml.safe_load(front_raw) or {}, yaml.safe_load(bottom_raw) or {}


def evaluate_gate_states(bottom: dict[str, Any]) -> list[dict[str, str]]:
    states = []
    for gate in bottom.get("gate_progress", []):
      if not isinstance(gate, dict):
          continue
      states.append({
          "gate_id": str(gate.get("gate_id", "")),
          "status": str(gate.get("status", "pending")),
      })
    return states


def determine_routing_status(gate_states: list[dict[str, str]], errors: list[str]) -> str:
    if errors:
        return "blocked"
    statuses = {row["status"] for row in gate_states}
    if "red" in statuses or "failed" in statuses:
        return "blocked"
    if "pending" in statuses:
        return "needs_clarification"
    return "routed"


def packet_files() -> list[Path]:
    return sorted(
        path
        for path in INBOX_DIR.iterdir()
        if path.is_file() and any(path.name.endswith(suffix) for suffix in PACKET_SUFFIXES)
    )


def load_structured_ref(front: dict[str, Any]) -> dict[str, Any] | None:
    structured_ref = front.get("structured_artifact_ref")
    if not isinstance(structured_ref, str) or not structured_ref:
        return None
    structured_path = ROOT / structured_ref
    if not structured_path.exists():
        return None
    return json.loads(structured_path.read_text())


def validate_front(front: dict[str, Any]) -> list[str]:
    errors: list[str] = []
    required = {
        "artifact_id",
        "artifact_type",
        "producer_role",
        "target_scope",
        "repo_root",
        "parent_only",
        "structured_contract_ref",
        "structured_artifact_ref",
        "required_consumers",
    }
    for field in sorted(required):
        if field not in front:
            errors.append(f"missing front matter field: {field}")
    role = front.get("producer_role")
    if isinstance(role, str) and role not in ROLE_IDS:
        errors.append(f"unknown producer role: {role}")
    artifact_type = front.get("artifact_type")
    if isinstance(artifact_type, str) and artifact_type not in PACKET_SUFFIXES:
        errors.append(f"unknown artifact_type: {artifact_type}")
    consumers = front.get("required_consumers", [])
    if not isinstance(consumers, list) or not consumers:
        errors.append("required_consumers must be a non-empty list")
    structured_contract_ref = front.get("structured_contract_ref")
    if isinstance(structured_contract_ref, str):
        if not (ROOT / structured_contract_ref).exists():
            errors.append("structured_contract_ref does not resolve to a file")
    else:
        errors.append("structured_contract_ref must be a non-empty string")
    return errors


def validate_bottom(bottom: dict[str, Any]) -> list[str]:
    errors: list[str] = []
    if "gate_progress" not in bottom:
        errors.append("missing bottom matter field: gate_progress")
    if "validation_status" not in bottom:
        errors.append("missing bottom matter field: validation_status")
    return errors


def scan_inbox_packets() -> list[PacketScanResult]:
    results: list[PacketScanResult] = []
    for packet_path in packet_files():
        errors: list[str] = []
        try:
            front, bottom = parse_markdown_packet(packet_path)
        except Exception as exc:  # noqa: BLE001
            results.append(
                PacketScanResult(
                    packet_path=str(packet_path.relative_to(ROOT)),
                    packet_name=packet_path.name,
                    front={},
                    bottom={},
                    structured=None,
                    gate_states=[],
                    status="blocked",
                    errors=[str(exc)],
                    resolved_consumers=[],
                )
            )
            continue
        errors.extend(validate_front(front))
        errors.extend(validate_bottom(bottom))
        structured = load_structured_ref(front)
        if structured is None:
            errors.append("missing or unreadable structured_artifact_ref")
        gate_states = evaluate_gate_states(bottom)
        resolved_consumers = [
            consumer
            for consumer in front.get("required_consumers", [])
            if isinstance(consumer, str)
        ]
        results.append(
            PacketScanResult(
                packet_path=str(packet_path.relative_to(ROOT)),
                packet_name=packet_path.name,
                front=front,
                bottom=bottom,
                structured=structured,
                gate_states=gate_states,
                status=determine_routing_status(gate_states, errors),
                errors=errors,
                resolved_consumers=resolved_consumers,
            )
        )
    return results


def build_routing_artifacts(results: list[PacketScanResult]) -> dict[str, Any]:
    decisions = []
    bundles = []
    for result in results:
        artifact_id = result.front.get("artifact_id", "PACKET-UNKNOWN")
        decision_id = f"ROUTE-{artifact_id.split('-', 1)[-1]}"
        status = result.status
        routing_mode = "fanout" if len(result.resolved_consumers) > 1 else "single_target"
        if status == "needs_clarification":
            routing_mode = "return_to_sender"
        elif status == "blocked":
            routing_mode = "triad_escalation"
        decisions.append(
            {
                "decision_id": decision_id,
                "artifact_type": "inbox_routing_decision",
                "source_packet_ref": result.packet_path,
                "source_artifact_id": artifact_id,
                "status": status,
                "routing_mode": routing_mode,
                "resolved_consumers": result.resolved_consumers or ["filesystem-router"],
                "routing_reason": (
                    "Packet satisfied gatekeeping and can advance."
                    if status == "routed"
                    else "Packet requires clarification or was blocked by gatekeeping."
                ),
                "blocked_reason": "; ".join(result.errors) if result.errors else "",
                "gate_status_summary": result.gate_states,
                "delegation_bundle_ref": "evaluation/tool-health/inbox-protocol/delegations/all.json",
            }
        )
        bundles.append(
            {
                "bundle_id": f"DELEGATE-{artifact_id.split('-', 1)[-1]}",
                "artifact_type": "delegation_bundle",
                "source_packet_ref": result.packet_path,
                "routing_decision_ref": "evaluation/tool-health/inbox-protocol/routing/all.json",
                "delegation_mode": (
                    "fanout"
                    if status == "routed" and len(result.resolved_consumers) > 1
                    else "single_target"
                    if status == "routed"
                    else "return_for_clarification"
                    if status == "needs_clarification"
                    else "triad_escalation"
                ),
                "targets": [
                    {
                        "role": consumer,
                        "why": "Declared required consumer for the inbox packet.",
                        "required_artifacts": [result.packet_path],
                    }
                    for consumer in (result.resolved_consumers or ["filesystem-router"])
                ],
                "dispatch_artifacts": [
                    "evaluation/tool-health/inbox-protocol/routing/all.json",
                    "evaluation/tool-health/inbox-protocol/delegations/all.json",
                ],
            }
        )
    return {"decisions": decisions, "bundles": bundles}


def write_router_outputs(results: list[PacketScanResult], artifacts: dict[str, Any]) -> None:
    INBOX_PROTOCOL_DIR.mkdir(parents=True, exist_ok=True)
    (INBOX_PROTOCOL_DIR / "packets").mkdir(parents=True, exist_ok=True)
    (INBOX_PROTOCOL_DIR / "routing").mkdir(parents=True, exist_ok=True)
    (INBOX_PROTOCOL_DIR / "delegations").mkdir(parents=True, exist_ok=True)
    latest_scan = {
        "status": "pass" if results and all(result.status == "routed" for result in results) else "bounded_pass",
        "packet_count": len(results),
        "routed_count": sum(result.status == "routed" for result in results),
        "blocked_count": sum(result.status == "blocked" for result in results),
        "clarification_count": sum(result.status == "needs_clarification" for result in results),
    }
    (INBOX_PROTOCOL_DIR / "latest-scan.json").write_text(
        json.dumps(
            latest_scan,
            indent=2,
        )
    )
    (INBOX_PROTOCOL_DIR / "gate-status.json").write_text(
        json.dumps(
            {
                "status": latest_scan["status"],
                "packets": [
                    {
                        "packet_path": result.packet_path,
                        "status": result.status,
                        "gate_states": result.gate_states,
                        "errors": result.errors,
                    }
                    for result in results
                ],
            },
            indent=2,
        )
    )
    (INBOX_PROTOCOL_DIR / "routing" / "all.json").write_text(json.dumps(artifacts["decisions"], indent=2))
    (INBOX_PROTOCOL_DIR / "delegations" / "all.json").write_text(json.dumps(artifacts["bundles"], indent=2))
    for result, decision, bundle in zip(results, artifacts["decisions"], artifacts["bundles"], strict=False):
        slug = result.packet_path.replace("/", "-").replace(".", "-").strip("-")
        (INBOX_PROTOCOL_DIR / "packets" / f"{slug}.json").write_text(
            json.dumps(
                {
                    "packet_path": result.packet_path,
                    "artifact_id": result.front.get("artifact_id", ""),
                    "artifact_type": result.front.get("artifact_type", ""),
                    "producer_role": result.front.get("producer_role", ""),
                    "status": result.status,
                    "resolved_consumers": result.resolved_consumers,
                    "gate_states": result.gate_states,
                    "errors": result.errors,
                },
                indent=2,
            )
        )
        (INBOX_PROTOCOL_DIR / "routing" / f"{slug}.json").write_text(json.dumps(decision, indent=2))
        (INBOX_PROTOCOL_DIR / "delegations" / f"{slug}.json").write_text(json.dumps(bundle, indent=2))


def inbox_snapshot() -> dict[str, Any]:
    results = scan_inbox_packets()
    artifacts = build_routing_artifacts(results)
    return {
        "packets": [
            {
                "packet_path": result.packet_path,
                "packet_name": result.packet_name,
                "artifact_id": result.front.get("artifact_id", ""),
                "artifact_type": result.front.get("artifact_type", ""),
                "producer_role": result.front.get("producer_role", ""),
                "status": result.status,
                "resolved_consumers": result.resolved_consumers,
                "gate_states": result.gate_states,
                "errors": result.errors,
            }
            for result in results
        ],
        "routing_decisions": artifacts["decisions"],
        "delegation_bundles": artifacts["bundles"],
    }
