from __future__ import annotations

import json
import re
from datetime import date
from pathlib import Path

import yaml
from jsonschema import Draft202012Validator


ROOT = Path(__file__).resolve().parents[1]
REQUIRED_SCAFFOLD = [
    "README.md",
    "AGENTS.md",
    "CLAUDE.md",
    "GOAL.md",
    "GOLDENPATH.md",
    "MEMORY.md",
]
REQUIRED_PROMPT_CONTRACT = [
    "agent-heavy-run-prompt-index.md",
    "agent-heavy-run-prompt-schema.md",
    "agent-heavy-run-prompt.schema.json",
    "agent-heavy-run-prompt.template.yaml",
    "architect-review-handoff-prompt-schema.md",
    "architect-review-handoff-prompt.schema.json",
    "architect-review-handoff-prompt.template.yaml",
    "copilot-prompting-playbook.md",
]
REQUIRED_PROGRAM_FILES = [
    "program.md",
]
REQUIRED_DIRECTORIES = [
    "source",
    "schemas",
    "examples",
    "expected-failures",
    "tests",
    "evaluation",
    "promotion",
]
REQUIRED_EXTERNAL_REPOS = {
    "goal-md": [
        "README.md",
        "template/GOAL.md",
    ],
    "meta-harness": [
        "README.md",
        "ONBOARDING.md",
    ],
    "autoresearch-mlx": [
        "README.md",
        "program.md",
    ],
}
PARENT_NATIVE_CONTRACTS = {
    "contracts/peer-mesh.yaml": "schemas/peer-mesh.schema.json",
    "contracts/peer-message.yaml": "schemas/peer-message.schema.json",
    "contracts/peer-lifecycle.yaml": "schemas/peer-lifecycle.schema.json",
    "contracts/observability-event.yaml": "schemas/observability-event.schema.json",
    "contracts/observability-ingest.yaml": "schemas/observability-ingest.schema.json",
    "contracts/policy-decision.yaml": "schemas/policy-decision.schema.json",
    "contracts/library-distribution.yaml": "schemas/library-distribution.schema.json",
    "contracts/benchmark-emission.yaml": "schemas/benchmark-emission.schema.json",
    "contracts/peer-mesh-runtime.yaml": "schemas/peer-mesh-runtime.schema.json",
    "contracts/agent-role-contract.yaml": "schemas/agent-role-contract.schema.json",
    "contracts/hook-manifest.yaml": "schemas/hook-manifest.schema.json",
    "contracts/capability-matrix.yaml": "schemas/capability-matrix.schema.json",
}
PARENT_NATIVE_VALID_EXAMPLES = [
    ("examples/peer-mesh.valid.json", "schemas/peer-mesh.schema.json"),
    ("examples/peer-message.valid.json", "schemas/peer-message.schema.json"),
    ("examples/peer-lifecycle.valid.json", "schemas/peer-lifecycle.schema.json"),
    ("examples/observability-event.valid.json", "schemas/observability-event.schema.json"),
    ("examples/observability-ingest.valid.json", "schemas/observability-ingest.schema.json"),
    ("examples/policy-decision.valid.json", "schemas/policy-decision.schema.json"),
    ("examples/library-distribution.valid.json", "schemas/library-distribution.schema.json"),
    ("examples/benchmark-emission.valid.json", "schemas/benchmark-emission.schema.json"),
    ("examples/peer-mesh-runtime.valid.json", "schemas/peer-mesh-runtime.schema.json"),
    ("examples/agent-role-contract.valid.json", "schemas/agent-role-contract.schema.json"),
    ("examples/hook-manifest.valid.json", "schemas/hook-manifest.schema.json"),
    ("examples/capability-matrix.valid.json", "schemas/capability-matrix.schema.json"),
]
TRIAD_GOVERNANCE_CONTRACTS = {
    "contracts/three-agent-topology.yaml": "schemas/three-agent-topology.schema.json",
    "contracts/agent-extension-request.yaml": "schemas/agent-extension-request.schema.json",
}
TRIAD_GOVERNANCE_VALID_EXAMPLES = [
    ("examples/three-agent-topology.valid.json", "schemas/three-agent-topology.schema.json"),
    ("examples/agent-extension-request.valid.json", "schemas/agent-extension-request.schema.json"),
]
TRIAD_GOVERNANCE_SCHEMA_ONLY = [
    "schemas/governed-agent-profile.schema.json",
]
INBOX_PROTOCOL_CONTRACTS = {
    "contracts/inbox-packet.yaml": "schemas/inbox-packet.schema.json",
    "contracts/inbox-routing-decision.yaml": "schemas/inbox-routing-decision.schema.json",
    "contracts/delegation-bundle.yaml": "schemas/delegation-bundle.schema.json",
}
INBOX_PROTOCOL_VALID_EXAMPLES = [
    ("examples/inbox-routing-decision-contract.valid.json", "schemas/inbox-routing-decision.schema.json"),
    ("examples/delegation-bundle-contract.valid.json", "schemas/delegation-bundle.schema.json"),
]
FRONT_DOOR_LIFECYCLE_CONTRACTS = {
    "contracts/front-door-runtime-topology.yaml": "schemas/front-door-runtime-topology.schema.json",
    "contracts/recursive-documentation-bundle.yaml": "schemas/recursive-documentation-bundle.schema.json",
}
FRONT_DOOR_LIFECYCLE_VALID_EXAMPLES = [
    ("examples/front-door-runtime-topology-contract.valid.json", "schemas/front-door-runtime-topology.schema.json"),
    ("examples/recursive-documentation-bundle.valid.json", "schemas/recursive-documentation-bundle.schema.json"),
]
SUBSYSTEM_ARCHITECTURE_CONTRACTS = {
    "contracts/subsystem-harness-topology.yaml": "schemas/subsystem-harness-topology.schema.json",
    "contracts/subsystem-registry.yaml": "schemas/subsystem-registry.schema.json",
}
SUBSYSTEM_ARCHITECTURE_VALID_EXAMPLES = [
    ("examples/subsystem-harness-topology.valid.json", "schemas/subsystem-harness-topology.schema.json"),
    ("examples/subsystem-registry.valid.json", "schemas/subsystem-registry.schema.json"),
    ("examples/subsystem-registry-record.valid.json", "schemas/subsystem-registry-record.schema.json"),
]
GAP_MAP_STRENGTH_CONTRACTS = {
    "contracts/gap-map-strength.yaml": "schemas/gap-map-strength.schema.json",
}
GAP_MAP_STRENGTH_VALID_EXAMPLES = [
    ("examples/gap-map-strength-report.valid.json", "schemas/gap-map-strength-report.schema.json"),
]
TOOL_PACKAGING_CONTRACTS = {
    "contracts/tool-packaging-family.yaml": "schemas/tool-packaging-family.schema.json",
}
TOOL_PACKAGING_VALID_EXAMPLES = [
    ("examples/tool-packaging-family.valid.json", "schemas/tool-packaging-family.schema.json"),
    ("examples/tool-spec.valid.json", "schemas/tool-spec.schema.json"),
    ("examples/agent-card.valid.json", "schemas/agent-card.schema.json"),
    ("examples/tool-task.valid.json", "schemas/tool-task.schema.json"),
    ("examples/tool-artifact.valid.json", "schemas/tool-artifact.schema.json"),
]
SUBSYSTEM_RUNNER_PROOF_CONTRACTS = {
    "contracts/subsystem-runner-proof-family.yaml": "schemas/subsystem-runner-proof-family.schema.json",
    "contracts/contract-to-runner-map.yaml": "schemas/contract-to-runner-map.schema.json",
    "contracts/subsystem-bounded-probe.yaml": "schemas/subsystem-bounded-probe.schema.json",
    "contracts/subsystem-observability-handshake.yaml": "schemas/subsystem-observability-handshake.schema.json",
}
SUBSYSTEM_RUNNER_PROOF_VALID_EXAMPLES = [
    ("examples/subsystem-runner-proof-family.valid.json", "schemas/subsystem-runner-proof-family.schema.json"),
    ("examples/contract-to-runner-map.valid.json", "schemas/contract-to-runner-map.schema.json"),
    ("examples/subsystem-bounded-probe.valid.json", "schemas/subsystem-bounded-probe.schema.json"),
    ("examples/subsystem-observability-handshake.valid.json", "schemas/subsystem-observability-handshake.schema.json"),
]
TRIAD_DOC_FILES = [
    "AGENTS.md",
    "CLAUDE.md",
]
PROMPT_HANDOFF_FAMILY = [
    "agent-heavy-run-prompt-schema.md",
    "agent-heavy-run-prompt.schema.json",
    "agent-heavy-run-prompt.template.yaml",
    "architect-review-handoff-prompt-schema.md",
    "architect-review-handoff-prompt.schema.json",
    "architect-review-handoff-prompt.template.yaml",
]
TRIAD_TEXT_MARKERS = {"triad", "three-agent", "three agent"}
DECISION_SPACE_MINIMUM = 3
DECISION_SPACE_HINTS = {
    "3+",
    "three or more",
    "at least three",
    '"minitems": 3',
    "minimum_options",
    "minimum_option_count",
    "minimum_decision_options",
    "three_option",
}
MARKDOWN_PROMPT_HINT = "markdown"
PIXTABLE_EVIDENCE_MARKERS = {"pixeltable", "evidence", "validation_gate"}
TRUTH_BOUNDARY_MARKERS = {"bounded", "truth"}
INBOX_PACKET_ARTIFACT_TYPES = {
    ".brainstorm.md",
    ".plan.md",
    ".analysis.md",
    ".test.md",
    ".review.md",
    ".handoff.md",
    ".spec.md",
    ".checkpoint.md",
}
INBOX_PACKET_REQUIRED_FIELDS = {
    "artifact_id",
    "artifact_type",
    "producer_role",
    "required_consumers",
    "routing_tags",
    "evidence_refs",
    "structured_contract_ref",
}
INBOX_PACKET_SCOPE_FIELDS = {
    "target_scope",
    "repo_root",
}
INBOX_PACKET_FRESHNESS_FIELDS = {"created_at", "updated_at"}
INBOX_GATE_FIELDS = {
    "gate_progress",
    "validation_status",
    "promotion_criteria",
    "blocked_by",
    "next_iteration",
}
FRONT_DOOR_RUNTIME_ROLES = {
    "user-facing-agent",
    "spec-interpreter",
    "intake-mapper",
    "semantic-cartographer",
    "filesystem-router",
    "wrapper-synthesizer",
}
RECURSIVE_DOCUMENTATION_FIELDS = {
    "purpose",
    "boundaries",
    "inputs",
    "outputs",
    "dependencies",
    "governing_artifacts",
}
GOVERNED_MARKDOWN_TEMPLATE_FIELDS = {
    "artifact_type",
    "prompt_id",
    "handoff_id",
    "structured_prompt_artifact",
    "acting_role",
    "recommended_option_id",
    "repo_root",
    "parent_only",
    "machine_truth_source",
}
GOVERNED_MARKDOWN_TEMPLATE_GATES = {
    "triad_handoff_consumed",
    "structured_prompt_emitted",
    "markdown_companion_emitted",
}
REQUIRED_PEER_MESH_OPERATIONS = {"list_agents", "send_command", "send_prompt", "await_response"}
REQUIRED_COMPLETION_TOKENS = {"done", "failed", "needs-human"}
REQUIRED_ROLE_CLASSES = {
    "mesh_bootstrap",
    "prod_boundary",
    "execution_driver",
    "verification_guard",
}
REQUIRED_HOOK_CLASSES = {
    "session_bootstrap",
    "membership_refresh",
    "message_guard",
    "completion_guard",
}
REQUIRED_CAPABILITY_SURFACE_TYPES = {
    "communication_plane",
    "distribution_plane",
    "policy_plane",
    "observability_plane",
    "arbitration_lane",
    "sandbox_execution",
    "browser_validation",
    "device_sidecar",
    "parallel_branching_reference",
    "loop_pattern_reference",
}
ALLOWED_CAPABILITY_CLASSIFICATIONS = {
    "core",
    "gated",
    "deployment_specific",
    "reference",
    "blocked_with_exact_dependency",
}
SUBSYSTEM_IDS = {
    "intake_etl",
    "research_harvest",
    "semantic_cartography",
    "wrapper_synthesizer",
}
SUBSYSTEM_FIT_AREAS = {
    "intake_etl",
    "research_harvest",
    "semantic_cartography",
    "wrapper_synthesizer",
    "observability",
    "durable_execution",
    "spec_compiler",
    "substrate_sync",
}
REQUIRED_RESEARCH_CORE_CAPABILITIES = {
    "pi-vs-claude-code",
    "the-library",
    "claude-code-hooks-mastery",
    "claude-code-hooks-multi-agent-observability",
}
ALLOWED_CAPABILITY_TARGET_SURFACES = {
    "program.md",
}
RESEARCH_SCHEMA_PATHS = {
    "research_manifest_contract": "schemas/research-packet-manifest.schema.json",
    "compiled_capability_harvest": "schemas/compiled-capability-harvest.schema.json",
    "compiled_feature_matrix": "schemas/compiled-feature-matrix.schema.json",
    "gap_placement_map": "schemas/gap-placement-map.schema.json",
    "source_index": "schemas/source-index.schema.json",
}
VIDEO_EVIDENCE_STRENGTH_BY_TYPE = {
    "transcript_context_summary": "transcript_plus_context_summary",
    "task_capture": "task_capture_without_terminal_frames",
    "task_stub": "task_stub_without_terminal_frames",
}
REQUIRED_MESSAGE_FIELDS = {
    "message_id",
    "correlation_id",
    "scenario_id",
    "sender_role",
    "recipient_role",
    "operation",
    "payload",
    "response_to_message_id",
}
REQUIRED_MESSAGE_TERMINAL_FIELDS = {"completion_token", "policy_decision_id", "evidence_refs"}
REQUIRED_LIFECYCLE_STATES = {
    "bootstrapping",
    "ready",
    "awaiting_response",
    "verifying_completion",
    "completed",
    "blocked",
}
REQUIRED_LIFECYCLE_EVENTS = {
    "session_start",
    "peer_join",
    "message_dispatch",
    "response_received",
    "verification_passed",
    "verification_failed",
    "retry_requested",
    "needs_human",
}
REQUIRED_OBSERVABILITY_EVENTS = {
    "peer_session_started",
    "peer_session_ended",
    "peer_joined",
    "peer_message_sent",
    "peer_message_received",
    "peer_response_completed",
    "policy_decision_emitted",
}
REQUIRED_INGEST_SESSION_MARKERS = {"session_start", "session_end"}
REQUIRED_INGEST_CORRELATION_FIELDS = {
    "message_id",
    "correlation_id",
    "scenario_id",
    "policy_decision_id",
    "completion_token",
}
REQUIRED_SWIMLANE_DIMENSIONS = {
    "runtime_actor",
    "sender_role",
    "recipient_role",
    "runtime_mode",
}
REQUIRED_POLICY_OUTCOMES = {"allow", "block", "ask"}
REQUIRED_POLICY_RECORD_FIELDS = {
    "decision_id",
    "message_id",
    "correlation_id",
    "scenario_id",
    "outcome",
    "reason",
    "actor_role",
}
REQUIRED_RUNTIME_MODES = {"same_host", "cross_device"}
REQUIRED_DISTRIBUTION_UNIT_TYPES = {
    "skill",
    "prompt",
    "agent",
    "policy",
    "validator",
    "benchmark_recipe",
}
REQUIRED_DISTRIBUTION_TRIGGERS = {"session_start", "peer_join"}
REQUIRED_BENCHMARK_TUPLE_FIELDS = {
    "benchmark_id",
    "benchmark_group",
    "contract_surface",
    "scenario_id",
    "run_ref",
    "status",
    "measurement_ref",
}
REQUIRED_BENCHMARK_COMPARISON_FIELDS = {
    "baseline_run_ref",
    "candidate_run_ref",
    "delta_summary",
    "regression_detected",
}
REQUIRED_BENCHMARK_GROUPS = {
    "peer_mesh_regression",
    "observability_ingest",
    "library_distribution",
}
REQUIRED_BENCHMARK_ARTIFACTS = {
    "evaluation/metrics-latest.json",
    "evaluation/validation-report.json",
    "promotion/readiness.json",
    "runs/iterations.jsonl",
}
REQUIRED_RUNTIME_MISMATCH_IDS = {
    "missing_same_host_bootstrap_entrypoint",
    "missing_local_peer_registration",
    "missing_same_host_message_dispatch",
    "missing_await_response_implementation",
    "missing_completion_token_enforcement",
    "missing_fail_loud_blocker_reporting",
    "missing_same_host_observability_emission",
    "missing_tool_health_runtime_truth",
    "missing_validator_scorer_runtime_credit",
}
REQUIRED_RUNTIME_OPERATIONS = {"bootstrap", "list_agents", "send_prompt", "send_command", "await_response"}
REQUIRED_FOLLOW_ON_LANE_STATUS = {
    "just-prompt": "gated",
    "agent-sandbox-skill": "blocked_with_exact_dependency",
    "bowser": "gated",
    "mac-mini-agent": "deployment_specific",
    "fork-repository-skill": "reference",
    "infinite-agentic-loop": "reference",
}
ALLOWED_RUNTIME_TRUTH_LEVELS = {"contract_only", "bounded_runtime", "active_runtime"}
STATUS_LEVELS = {
    "missing": 0,
    "fail": 1,
    "blocked": 1,
    "warn": 2,
    "bounded": 3,
    "dry_pass": 4,
    "bounded_pass": 5,
    "pass": 6,
}


def parse_markdown_contract(path: Path) -> tuple[dict, dict]:
    text = path.read_text()
    if not text.startswith("---\n"):
        raise ValueError(f"{path.name}: missing front matter start")
    _, rest = text.split("---\n", 1)
    front_raw, body = rest.split("\n---\n", 1)
    if "\n---bottom-matter---\n" not in body:
        raise ValueError(f"{path.name}: missing bottom matter marker")
    _, bottom_raw = body.split("\n---bottom-matter---\n", 1)
    front = yaml.safe_load(front_raw) or {}
    bottom = yaml.safe_load(bottom_raw) or {}
    return front, bottom


def load_jsonl(path: Path) -> tuple[list[dict], list[str]]:
    rows = []
    errors = []
    if not path.exists():
        return rows, errors
    for line_number, line in enumerate(path.read_text().splitlines(), start=1):
        if not line.strip():
            continue
        try:
            rows.append(json.loads(line))
        except json.JSONDecodeError as exc:
            errors.append(f"line {line_number}: {exc.msg}")
    return rows, errors


def require_subset(label: str, required: set[str], actual: set[str]) -> None:
    missing = sorted(required - actual)
    if missing:
        raise AssertionError(f"{label} are missing required values: {missing}")


def is_pinned_github_blob(ref: str) -> bool:
    if not ref.startswith("https://github.com/") or "/blob/" not in ref:
        return False
    _, blob_tail = ref.split("/blob/", 1)
    commit, *_ = blob_tail.split("/", 1)
    return len(commit) == 40 and all(char in "0123456789abcdef" for char in commit)


def status_at_least(status: str | None, minimum: str) -> bool:
    normalized_status = normalize_status(status)
    normalized_minimum = normalize_status(minimum)
    if normalized_status is None or normalized_minimum is None:
        return False
    actual_level = STATUS_LEVELS[normalized_status]
    minimum_level = STATUS_LEVELS[normalized_minimum]
    return actual_level >= minimum_level


def normalize_status(status: str | None) -> str | None:
    if status is None:
        return None
    normalized = status.lower().strip().replace("-", "_")
    if normalized in STATUS_LEVELS:
        return normalized
    if "bounded" in normalized and "pass" in normalized:
        return "bounded_pass"
    if "dry" in normalized and "pass" in normalized:
        return "dry_pass"
    if normalized.endswith("_pass") or normalized.endswith("pass"):
        return "pass"
    if "block" in normalized:
        return "blocked"
    if "warn" in normalized or "partial" in normalized or "degrad" in normalized:
        return "warn"
    if "miss" in normalized or "absent" in normalized:
        return "missing"
    if "fail" in normalized or "error" in normalized:
        return "fail"
    return None


def load_structured(path: Path) -> dict:
    if path.suffix == ".json":
        return json.loads(path.read_text())
    return yaml.safe_load(path.read_text())


def collect_normalized_keys(node: object) -> set[str]:
    keys: set[str] = set()

    def visit(value: object) -> None:
        if isinstance(value, dict):
            for key, child in value.items():
                keys.add(normalize_identifier(str(key)))
                visit(child)
        elif isinstance(value, list):
            for item in value:
                visit(item)

    visit(node)
    return {key for key in keys if key}


def collect_string_values(node: object) -> set[str]:
    values: set[str] = set()

    def visit(value: object) -> None:
        if isinstance(value, str):
            values.add(value.strip())
        elif isinstance(value, dict):
            for child in value.values():
                visit(child)
        elif isinstance(value, list):
            for item in value:
                visit(item)

    visit(node)
    return {value for value in values if value}


def normalize_identifier(value: str) -> str:
    return re.sub(r"[^a-z0-9]+", "_", value.lower()).strip("_")


def text_mentions_role(text: str, role: str) -> bool:
    normalized_role = normalize_identifier(role)
    variants = {
        normalized_role,
        normalized_role.replace("_", "-"),
        normalized_role.replace("_", " "),
    }
    lowered_text = text.lower()
    return any(
        re.search(rf"(?<![a-z0-9]){re.escape(variant)}(?![a-z0-9])", lowered_text)
        for variant in variants
        if variant
    )


def extract_governance_roles(node: object) -> set[str]:
    roles: set[str] = set()

    def visit(value: object, path: tuple[str, ...] = ()) -> None:
        if isinstance(value, dict):
            for key, child in value.items():
                key_norm = normalize_identifier(key)
                if key_norm in {"roles", "triad_roles", "governance_roles"} and isinstance(child, list):
                    for item in child:
                        if isinstance(item, str):
                            roles.add(normalize_identifier(item))
                        elif isinstance(item, dict):
                            for field in ("role_id", "role", "name", "id"):
                                raw = item.get(field)
                                if isinstance(raw, str):
                                    roles.add(normalize_identifier(raw))
                                    break
                elif key_norm in {"agent_profiles", "profiles"} and isinstance(child, dict):
                    for role_key, role_value in child.items():
                        if isinstance(role_value, dict):
                            roles.add(normalize_identifier(role_key))
                elif key_norm in {"governance_triad", "triad", "three_agent_topology"} and isinstance(child, dict):
                    for role_key, role_value in child.items():
                        if isinstance(role_value, (dict, list, str)):
                            roles.add(normalize_identifier(role_key))
                visit(child, path + (key_norm,))
        elif isinstance(value, list):
            for item in value:
                visit(item, path)

    visit(node)
    return {role for role in roles if role}


def extract_option_space_minimum(node: object) -> int:
    minimums: list[int] = []

    def visit(value: object, path: tuple[str, ...] = ()) -> None:
        if isinstance(value, dict):
            context_tokens = [normalize_identifier(part) for part in path]
            context_tokens.extend(normalize_identifier(key) for key in value)
            context = " ".join(token for token in context_tokens if token)
            if "option" in context or "decision" in context:
                min_items = value.get("minItems")
                if isinstance(min_items, int):
                    minimums.append(min_items)
                for key in (
                    "minimum_options",
                    "minimum_option_count",
                    "minimum_decision_options",
                    "min_options",
                    "min_option_count",
                ):
                    raw = value.get(key)
                    if isinstance(raw, int):
                        minimums.append(raw)
            for key, child in value.items():
                key_norm = normalize_identifier(key)
                if ("option" in key_norm or "decision" in key_norm) and isinstance(child, list):
                    minimums.append(len(child))
                visit(child, path + (key_norm,))
        elif isinstance(value, list):
            for item in value:
                visit(item, path)

    visit(node)
    return max(minimums, default=0)


def validate_required_surface_triad(
    contract_rel: str,
    schema_rel: str,
    example_rel: str,
) -> tuple[dict | None, dict | None, dict | None, list[str]]:
    errors: list[str] = []
    contract_path = ROOT / contract_rel
    schema_path = ROOT / schema_rel
    example_path = ROOT / example_rel
    contract = None
    schema = None
    example = None

    if not contract_path.exists():
        errors.append(f"missing:{contract_rel}")
    if not schema_path.exists():
        errors.append(f"missing:{schema_rel}")
    if not example_path.exists():
        errors.append(f"missing:{example_rel}")
    if errors:
        return contract, schema, example, errors

    try:
        schema = json.loads(schema_path.read_text())
        Draft202012Validator.check_schema(schema)
    except Exception as exc:  # noqa: BLE001
        errors.append(f"{schema_rel}:{exc}")
        return contract, schema, example, errors

    try:
        contract = yaml.safe_load(contract_path.read_text())
        Draft202012Validator(schema).validate(contract)
    except Exception as exc:  # noqa: BLE001
        errors.append(f"{contract_rel}:{exc}")

    try:
        example = json.loads(example_path.read_text())
        Draft202012Validator(schema).validate(example)
    except Exception as exc:  # noqa: BLE001
        errors.append(f"{example_rel}:{exc}")

    return contract, schema, example, errors


def validate_examples() -> list[dict]:
    results = []
    schema_paths = {
        "front": "schemas/front-matter.schema.json",
        "bottom": "schemas/bottom-matter.schema.json",
        "ratchet": "schemas/copilot-ratchet-report.schema.json",
        "iteration": "schemas/iteration-record.schema.json",
        "metrics": "schemas/capability-harvest-metrics.schema.json",
        "research_manifest_contract": "schemas/research-packet-manifest.schema.json",
        "architect_handoff_prompt": "architect-review-handoff-prompt.schema.json",
        "peer_mesh": "schemas/peer-mesh.schema.json",
        "peer_message": "schemas/peer-message.schema.json",
        "peer_lifecycle": "schemas/peer-lifecycle.schema.json",
        "observability_event": "schemas/observability-event.schema.json",
        "observability_ingest": "schemas/observability-ingest.schema.json",
        "policy_decision": "schemas/policy-decision.schema.json",
        "library_distribution": "schemas/library-distribution.schema.json",
        "benchmark_emission": "schemas/benchmark-emission.schema.json",
        "peer_mesh_runtime": "schemas/peer-mesh-runtime.schema.json",
        "agent_role": "schemas/agent-role-contract.schema.json",
        "hook_manifest": "schemas/hook-manifest.schema.json",
        "capability_matrix": "schemas/capability-matrix.schema.json",
        "three_agent_topology": "schemas/three-agent-topology.schema.json",
        "agent_extension_request": "schemas/agent-extension-request.schema.json",
        "governed_agent_profile": "schemas/governed-agent-profile.schema.json",
        "inbox_routing_decision": "schemas/inbox-routing-decision.schema.json",
        "delegation_bundle": "schemas/delegation-bundle.schema.json",
        "front_door_runtime_topology": "schemas/front-door-runtime-topology.schema.json",
        "recursive_documentation_bundle": "schemas/recursive-documentation-bundle.schema.json",
        "tool_packaging_family": "schemas/tool-packaging-family.schema.json",
        "tool_spec": "schemas/tool-spec.schema.json",
        "agent_card": "schemas/agent-card.schema.json",
        "tool_task": "schemas/tool-task.schema.json",
        "tool_artifact": "schemas/tool-artifact.schema.json",
        "tool_packaging_report": "schemas/tool-packaging-strengthening-report.schema.json",
        "subsystem_runner_proof_family": "schemas/subsystem-runner-proof-family.schema.json",
        "contract_to_runner_map": "schemas/contract-to-runner-map.schema.json",
        "subsystem_bounded_probe": "schemas/subsystem-bounded-probe.schema.json",
        "subsystem_observability_handshake": "schemas/subsystem-observability-handshake.schema.json",
        "subsystem_runner_proof_report": "schemas/subsystem-runner-proof-strengthening-report.schema.json",
        "evidence_strength": "schemas/evidence-strength.schema.json",
        "operational_feature_matrix": "schemas/operational-feature-matrix.schema.json",
        "consume_source_quality_report": "schemas/consume-source-quality-strengthening-report.schema.json",
    }
    schemas = {name: json.loads((ROOT / rel).read_text()) for name, rel in schema_paths.items()}
    for schema in schemas.values():
        Draft202012Validator.check_schema(schema)

    valid_examples = [
        ("examples/front-matter.valid.json", schemas["front"]),
        ("examples/bottom-matter.valid.json", schemas["bottom"]),
        ("examples/copilot-ratchet-report.valid.json", schemas["ratchet"]),
        ("examples/iteration-record.valid.json", schemas["iteration"]),
        ("examples/capability-harvest-metrics.valid.json", schemas["metrics"]),
        ("examples/research-packet-manifest.valid.json", schemas["research_manifest_contract"]),
        ("examples/architect-review-handoff-prompt.valid.json", schemas["architect_handoff_prompt"]),
        ("examples/peer-mesh.valid.json", schemas["peer_mesh"]),
        ("examples/peer-message.valid.json", schemas["peer_message"]),
        ("examples/peer-lifecycle.valid.json", schemas["peer_lifecycle"]),
        ("examples/observability-event.valid.json", schemas["observability_event"]),
        ("examples/observability-ingest.valid.json", schemas["observability_ingest"]),
        ("examples/policy-decision.valid.json", schemas["policy_decision"]),
        ("examples/library-distribution.valid.json", schemas["library_distribution"]),
        ("examples/benchmark-emission.valid.json", schemas["benchmark_emission"]),
        ("examples/peer-mesh-runtime.valid.json", schemas["peer_mesh_runtime"]),
        ("examples/agent-role-contract.valid.json", schemas["agent_role"]),
        ("examples/hook-manifest.valid.json", schemas["hook_manifest"]),
        ("examples/capability-matrix.valid.json", schemas["capability_matrix"]),
        ("examples/three-agent-topology.valid.json", schemas["three_agent_topology"]),
        ("examples/agent-extension-request.valid.json", schemas["agent_extension_request"]),
        ("examples/inbox-routing-decision-contract.valid.json", schemas["inbox_routing_decision"]),
        ("examples/delegation-bundle-contract.valid.json", schemas["delegation_bundle"]),
        ("examples/front-door-runtime-topology-contract.valid.json", schemas["front_door_runtime_topology"]),
        ("examples/recursive-documentation-bundle.valid.json", schemas["recursive_documentation_bundle"]),
        ("examples/tool-packaging-family.valid.json", schemas["tool_packaging_family"]),
        ("examples/tool-spec.valid.json", schemas["tool_spec"]),
        ("examples/agent-card.valid.json", schemas["agent_card"]),
        ("examples/tool-task.valid.json", schemas["tool_task"]),
        ("examples/tool-artifact.valid.json", schemas["tool_artifact"]),
        ("examples/tool-packaging-strengthening-report.valid.json", schemas["tool_packaging_report"]),
        ("examples/subsystem-runner-proof-family.valid.json", schemas["subsystem_runner_proof_family"]),
        ("examples/contract-to-runner-map.valid.json", schemas["contract_to_runner_map"]),
        ("examples/subsystem-bounded-probe.valid.json", schemas["subsystem_bounded_probe"]),
        ("examples/subsystem-observability-handshake.valid.json", schemas["subsystem_observability_handshake"]),
        ("examples/subsystem-runner-proof-strengthening-report.valid.json", schemas["subsystem_runner_proof_report"]),
        ("examples/evidence-strength.valid.json", schemas["evidence_strength"]),
        ("examples/operational-feature-matrix.valid.json", schemas["operational_feature_matrix"]),
        ("examples/consume-source-quality-strengthening-report.valid.json", schemas["consume_source_quality_report"]),
    ]
    for rel, schema in valid_examples:
        instance = json.loads((ROOT / rel).read_text())
        Draft202012Validator(schema).validate(instance)
        results.append({"file": rel, "status": "pass"})

    registry = yaml.safe_load((ROOT / "expected-failures/registry.yaml").read_text())
    for item in registry["invalid_examples"]:
        schema = json.loads((ROOT / item["schema"]).read_text())
        instance = json.loads((ROOT / item["file"]).read_text())
        validator = Draft202012Validator(schema)
        errors = list(validator.iter_errors(instance))
        if not errors:
            raise AssertionError(f"{item['file']} unexpectedly passed")
        message_blob = " | ".join(error.message for error in errors)
        if item["expected_reason_contains"] not in message_blob:
            raise AssertionError(
                f"{item['file']} failed for unexpected reason: {message_blob}"
            )
        results.append({"file": item["file"], "status": "pass", "reason": message_blob})
    return results


def validate_governance_triad_slice() -> dict:
    loaded_contracts: dict[str, dict] = {}
    loaded_schemas: dict[str, dict] = {}
    loaded_examples: dict[str, dict] = {}

    for contract_rel, schema_rel in TRIAD_GOVERNANCE_CONTRACTS.items():
        contract_path = ROOT / contract_rel
        schema_path = ROOT / schema_rel
        schema = json.loads(schema_path.read_text())
        contract = yaml.safe_load(contract_path.read_text())
        Draft202012Validator.check_schema(schema)
        Draft202012Validator(schema).validate(contract)
        loaded_contracts[contract_rel] = contract
        loaded_schemas[schema_rel] = schema

    for schema_rel in TRIAD_GOVERNANCE_SCHEMA_ONLY:
        schema = json.loads((ROOT / schema_rel).read_text())
        Draft202012Validator.check_schema(schema)
        loaded_schemas[schema_rel] = schema

    for example_rel, schema_rel in TRIAD_GOVERNANCE_VALID_EXAMPLES:
        schema = loaded_schemas.get(schema_rel) or json.loads((ROOT / schema_rel).read_text())
        instance = json.loads((ROOT / example_rel).read_text())
        Draft202012Validator(schema).validate(instance)
        loaded_examples[example_rel] = instance

    topology_contract = loaded_contracts["contracts/three-agent-topology.yaml"]
    topology_example = loaded_examples["examples/three-agent-topology.valid.json"]
    triad_roles = extract_governance_roles(topology_contract)
    example_roles = extract_governance_roles(topology_example)
    if len(triad_roles) < 3:
        raise AssertionError("three-agent-topology must expose at least three explicit governance roles.")
    if not any(role.startswith("orchestrator") for role in triad_roles):
        raise AssertionError("three-agent-topology must keep an explicit orchestrator role.")
    if triad_roles != example_roles:
        raise AssertionError(
            f"three-agent-topology valid example roles drift from the contract. Contract={sorted(triad_roles)} Example={sorted(example_roles)}"
        )

    role_contract = yaml.safe_load((ROOT / "contracts/agent-role-contract.yaml").read_text())
    runtime_role_ids = {normalize_identifier(role["role_id"]) for role in role_contract["roles"]}
    runtime_role_classes = {normalize_identifier(role["role_class"]) for role in role_contract["roles"]}
    overlap = sorted((triad_roles & runtime_role_ids) | (triad_roles & runtime_role_classes))
    if overlap:
        raise AssertionError(
            f"Governance triad roles must stay separate from runtime roles in contracts/agent-role-contract.yaml: {overlap}"
        )

    doc_mentions = {}
    for rel in TRIAD_DOC_FILES:
        text = (ROOT / rel).read_text().lower()
        if not any(marker in text for marker in TRIAD_TEXT_MARKERS):
            raise AssertionError(f"{rel} must explicitly expose the governance triad.")
        missing_roles = sorted(role for role in triad_roles if not text_mentions_role(text, role))
        if missing_roles:
            raise AssertionError(f"{rel} is missing governance triad role coverage: {missing_roles}")
        doc_mentions[rel] = sorted(triad_roles)

    family_texts = {rel: (ROOT / rel).read_text().lower() for rel in PROMPT_HANDOFF_FAMILY}
    family_text = "\n".join(family_texts.values())
    if not any(marker in family_text for marker in TRIAD_TEXT_MARKERS):
        raise AssertionError("Prompt/handoff family must explicitly recognize triad targeting.")
    missing_family_roles = sorted(role for role in triad_roles if not text_mentions_role(family_text, role))
    if missing_family_roles:
        raise AssertionError(f"Prompt/handoff family is missing triad role targeting markers: {missing_family_roles}")

    extension_schema = loaded_schemas["schemas/agent-extension-request.schema.json"]
    extension_contract = loaded_contracts["contracts/agent-extension-request.yaml"]
    extension_example = loaded_examples["examples/agent-extension-request.valid.json"]
    decision_floor = max(
        extract_option_space_minimum(extension_schema),
        extract_option_space_minimum(extension_contract),
        extract_option_space_minimum(extension_example),
    )
    if decision_floor < DECISION_SPACE_MINIMUM:
        raise AssertionError("agent-extension-request must preserve 3+ option decision spaces.")
    if "option" not in family_text or not any(hint in family_text for hint in DECISION_SPACE_HINTS):
        raise AssertionError("Prompt/handoff family must explicitly recognize 3+ option decision spaces.")

    governed_profile_refs = [
        rel for rel, schema in loaded_schemas.items()
        if rel != "schemas/governed-agent-profile.schema.json"
        and "governed-agent-profile" in json.dumps(schema).lower()
    ]
    if not governed_profile_refs:
        raise AssertionError("Triad schemas must wire through schemas/governed-agent-profile.schema.json.")

    handoff_example = load_structured(ROOT / "examples/architect-review-handoff-prompt.valid.json")
    artifact_path = (
        handoff_example.get("expected_outputs", {})
        .get("follow_up_prompt_artifact", {})
        .get("artifact_path", "")
    )
    if not artifact_path.lower().endswith(".md"):
        raise AssertionError("Handoff prompt artifacts must point to Markdown prompt artifacts.")
    if MARKDOWN_PROMPT_HINT not in family_text:
        raise AssertionError("Prompt/handoff family must explicitly require Markdown prompt artifacts.")

    extension_text = "\n".join(
        [
            yaml.safe_dump(extension_contract, sort_keys=False),
            json.dumps(extension_schema, sort_keys=True),
            json.dumps(extension_example, sort_keys=True),
        ]
    ).lower()
    missing_evidence_markers = sorted(marker for marker in PIXTABLE_EVIDENCE_MARKERS if marker not in extension_text)
    if missing_evidence_markers:
        raise AssertionError(
            f"agent-extension-request must keep Pixeltable/evidence/validation-gate doctrine explicit: {missing_evidence_markers}"
        )
    missing_truth_markers = sorted(marker for marker in TRUTH_BOUNDARY_MARKERS if marker not in extension_text)
    if missing_truth_markers:
        raise AssertionError(
            f"agent-extension-request must keep truthful bounded-output doctrine explicit: {missing_truth_markers}"
        )

    return {
        "contracts": sorted(TRIAD_GOVERNANCE_CONTRACTS.keys()),
        "examples": [item[0] for item in TRIAD_GOVERNANCE_VALID_EXAMPLES],
        "schema_only": TRIAD_GOVERNANCE_SCHEMA_ONLY,
        "triad_roles": sorted(triad_roles),
        "runtime_role_ids": sorted(runtime_role_ids),
        "runtime_role_classes": sorted(runtime_role_classes),
        "docs_checked": doc_mentions,
        "prompt_handoff_files": PROMPT_HANDOFF_FAMILY,
        "minimum_decision_options": decision_floor,
        "governed_agent_profile_refs": sorted(governed_profile_refs),
        "handoff_markdown_artifact_path": artifact_path,
    }


def validate_inbox_front_door_slice() -> dict:
    details: dict[str, object] = {
        "required_inbox_contracts": sorted(INBOX_PROTOCOL_CONTRACTS.keys()),
        "required_front_door_contracts": sorted(FRONT_DOOR_LIFECYCLE_CONTRACTS.keys()),
    }
    missing_inventory: list[str] = []
    validation_errors: list[str] = []
    validated_contracts: list[str] = []
    validated_examples: list[str] = []
    inbox_key_unions: list[set[str]] = []
    lifecycle_key_unions: list[set[str]] = []
    front_validator = Draft202012Validator(json.loads((ROOT / "schemas/front-matter.schema.json").read_text()))
    bottom_validator = Draft202012Validator(json.loads((ROOT / "schemas/bottom-matter.schema.json").read_text()))

    for contract_rel, schema_rel in INBOX_PROTOCOL_CONTRACTS.items():
        if contract_rel == "contracts/inbox-packet.yaml":
            contract_path = ROOT / contract_rel
            schema_path = ROOT / schema_rel
            example_path = ROOT / "examples/governed-inbox-packet.protocol.valid.md"
            missing = [
                f"missing:{rel}"
                for rel, path in (
                    (contract_rel, contract_path),
                    (schema_rel, schema_path),
                    ("examples/governed-inbox-packet.protocol.valid.md", example_path),
                )
                if not path.exists()
            ]
            if missing:
                missing_inventory.extend(missing)
                continue
            schema = json.loads(schema_path.read_text())
            Draft202012Validator.check_schema(schema)
            contract = yaml.safe_load(contract_path.read_text())
            Draft202012Validator(schema).validate(contract)
            front, bottom = parse_markdown_contract(example_path)
            front_validator.validate(front)
            bottom_validator.validate(bottom)
            validated_contracts.append(contract_rel)
            validated_examples.append("examples/governed-inbox-packet.protocol.valid.md")
            inbox_key_unions.append(
                collect_normalized_keys(contract)
                | collect_normalized_keys(schema)
                | collect_normalized_keys(front)
                | collect_normalized_keys(bottom)
            )
            continue

        example_rel = {
            "contracts/inbox-routing-decision.yaml": "examples/inbox-routing-decision-contract.valid.json",
            "contracts/delegation-bundle.yaml": "examples/delegation-bundle-contract.valid.json",
        }.get(contract_rel, f"examples/{Path(contract_rel).stem}.valid.json")
        contract, schema, example, errors = validate_required_surface_triad(contract_rel, schema_rel, example_rel)
        if errors:
            missing_inventory.extend(error for error in errors if error.startswith("missing:"))
            validation_errors.extend(error for error in errors if not error.startswith("missing:"))
            continue
        validated_contracts.append(contract_rel)
        validated_examples.append(example_rel)
        inbox_key_unions.append(
            collect_normalized_keys(contract)
            | collect_normalized_keys(schema)
            | collect_normalized_keys(example)
        )

    for contract_rel, schema_rel in FRONT_DOOR_LIFECYCLE_CONTRACTS.items():
        example_rel = {
            "contracts/front-door-runtime-topology.yaml": "examples/front-door-runtime-topology-contract.valid.json",
        }.get(contract_rel, f"examples/{Path(contract_rel).stem}.valid.json")
        contract, schema, example, errors = validate_required_surface_triad(contract_rel, schema_rel, example_rel)
        if errors:
            missing_inventory.extend(error for error in errors if error.startswith("missing:"))
            validation_errors.extend(error for error in errors if not error.startswith("missing:"))
            continue
        validated_contracts.append(contract_rel)
        validated_examples.append(example_rel)
        lifecycle_key_unions.append(
            collect_normalized_keys(contract)
            | collect_normalized_keys(schema)
            | collect_normalized_keys(example)
        )

    if validation_errors:
        raise AssertionError(f"Inbox/front-door triad validation errors: {validation_errors}")

    if missing_inventory:
        raise AssertionError(f"Inbox/front-door surfaces are missing: {sorted(set(missing_inventory))}")

    if not inbox_key_unions:
        raise AssertionError("Inbox protocol surfaces must validate at least one governed packet contract triad.")

    inbox_fields = set().union(*inbox_key_unions)
    missing_packet_fields = sorted(
        field for field in INBOX_PACKET_REQUIRED_FIELDS if field not in inbox_fields
    )
    if missing_packet_fields:
        raise AssertionError(
            f"Inbox protocol surfaces must keep required packet fields explicit: {missing_packet_fields}"
        )
    if not (INBOX_PACKET_SCOPE_FIELDS & inbox_fields):
        raise AssertionError("Inbox protocol surfaces must carry project or target scope fields.")

    lifecycle_fields = set().union(*lifecycle_key_unions) if lifecycle_key_unions else set()
    missing_recursive_fields = sorted(
        field for field in RECURSIVE_DOCUMENTATION_FIELDS if field not in lifecycle_fields
    )
    if missing_recursive_fields:
        raise AssertionError(
            f"Front-door lifecycle surfaces must preserve recursive documentation fields: {missing_recursive_fields}"
        )

    heavy_schema = json.loads((ROOT / "agent-heavy-run-prompt.schema.json").read_text())
    heavy_template = yaml.safe_load((ROOT / "agent-heavy-run-prompt.template.yaml").read_text())
    handoff_schema = json.loads((ROOT / "architect-review-handoff-prompt.schema.json").read_text())
    handoff_template = yaml.safe_load((ROOT / "architect-review-handoff-prompt.template.yaml").read_text())
    handoff_example = load_structured(ROOT / "examples/architect-review-handoff-prompt.valid.json")

    heavy_runtime_roles = set(heavy_schema["$defs"]["runtime_role_id"]["enum"])
    if heavy_runtime_roles != FRONT_DOOR_RUNTIME_ROLES:
        raise AssertionError(
            f"Heavy-run schema runtime roles drifted from the inbox/front-door role family. Expected={sorted(FRONT_DOOR_RUNTIME_ROLES)} Actual={sorted(heavy_runtime_roles)}"
        )
    governed_roles = set(heavy_schema["$defs"]["governed_role_id"]["enum"])
    union_roles = set(heavy_schema["$defs"]["governed_or_runtime_role_id"]["enum"])
    if governed_roles & heavy_runtime_roles:
        raise AssertionError("Governance roles and front-door runtime roles must stay disjoint in prompt schemas.")
    if union_roles != governed_roles | heavy_runtime_roles:
        raise AssertionError("governed_or_runtime_role_id must be the exact union of governance and front-door runtime roles.")

    role_contract = yaml.safe_load((ROOT / "contracts/agent-role-contract.yaml").read_text())
    existing_runtime_roles = {role["role_id"] for role in role_contract["roles"]}
    overlap = sorted(existing_runtime_roles & heavy_runtime_roles)
    if overlap:
        raise AssertionError(f"Front-door runtime roles must stay separate from peer-mesh runtime roles: {overlap}")

    packet_types = set(heavy_schema["$defs"]["packet_artifact_type"]["enum"])
    handoff_packet_types = set(handoff_schema["$defs"]["packet_artifact_type"]["enum"])
    if packet_types != INBOX_PACKET_ARTIFACT_TYPES or handoff_packet_types != INBOX_PACKET_ARTIFACT_TYPES:
        raise AssertionError("Prompt/handoff packet artifact types must cover the governed inbox packet protocol exactly.")

    triad_context = heavy_template["triad_context"]
    required_triad_fields = {
        "acting_role",
        "upstream_handoff_ref",
        "upstream_inbox_packet_ref",
        "packet_artifact_type",
        "required_gate_state",
        "required_consumers",
        "bottom_matter_ref",
        "structured_contract_ref",
        "decision_space_required",
        "runtime_truth_requirements",
        "command_evidence_requirements",
    }
    missing_triad_fields = sorted(required_triad_fields - set(triad_context))
    if missing_triad_fields:
        raise AssertionError(f"Heavy-run prompt template is missing inbox-aware triad fields: {missing_triad_fields}")
    if triad_context["packet_artifact_type"] not in INBOX_PACKET_ARTIFACT_TYPES:
        raise AssertionError("Heavy-run prompt template must point at a governed inbox packet artifact type.")
    if not str(triad_context["upstream_inbox_packet_ref"]).startswith("inbox/"):
        raise AssertionError("Heavy-run prompt template must point at an inbox packet path.")
    if not str(triad_context["bottom_matter_ref"]).startswith("inbox/"):
        raise AssertionError("Heavy-run prompt template bottom_matter_ref must stay inbox-scoped.")
    if not str(triad_context["structured_contract_ref"]).startswith("inbox/"):
        raise AssertionError("Heavy-run prompt template structured_contract_ref must stay inbox-scoped.")

    inbox_context = handoff_template["inbox_context"]
    missing_handoff_fields = sorted(
        {
            "upstream_inbox_packet_ref",
            "packet_artifact_type",
            "required_gate_state",
            "required_consumers",
            "bottom_matter_ref",
            "structured_contract_ref",
        }
        - set(inbox_context)
    )
    if missing_handoff_fields:
        raise AssertionError(f"Architect handoff template is missing inbox context fields: {missing_handoff_fields}")
    if handoff_example.get("inbox_context") is None:
        raise AssertionError("Architect handoff valid example must now include inbox_context.")

    packet_ref = handoff_example["inbox_context"].get("upstream_inbox_packet_ref", "")
    if not packet_ref.startswith("inbox/"):
        raise AssertionError("Architect handoff valid example must reference an inbox packet artifact.")
    if handoff_example["inbox_context"].get("packet_artifact_type") not in INBOX_PACKET_ARTIFACT_TYPES:
        raise AssertionError("Architect handoff valid example must use a governed inbox packet artifact type.")

    prompt_front, prompt_bottom = parse_markdown_contract(
        ROOT / "prompts/governed-triad-follow-up-prompt.template.md"
    )
    missing_front_fields = sorted(GOVERNED_MARKDOWN_TEMPLATE_FIELDS - set(prompt_front))
    if missing_front_fields:
        raise AssertionError(
            f"Governed markdown companion template is missing front-matter fields: {missing_front_fields}"
        )
    gate_names = {
        item.get("gate")
        for item in prompt_bottom.get("gate_progress", [])
        if isinstance(item, dict) and item.get("gate")
    }
    missing_markdown_gates = sorted(GOVERNED_MARKDOWN_TEMPLATE_GATES - gate_names)
    if missing_markdown_gates:
        raise AssertionError(
            f"Governed markdown companion template is missing gate_progress entries: {missing_markdown_gates}"
        )
    prompt_text = (ROOT / "prompts/governed-triad-follow-up-prompt.template.md").read_text().lower()
    required_markdown_markers = {
        "upstream inbox packet",
        "upstream inbox packet bottom matter",
        "structured handoff artifact",
        "structured heavy-run prompt artifact",
    }
    missing_markers = sorted(marker for marker in required_markdown_markers if marker not in prompt_text)
    if missing_markers:
        raise AssertionError(
            f"Governed markdown companion template is missing inbox packet parsing markers: {missing_markers}"
        )

    governed_packets = []
    inbox_root = ROOT / "inbox"
    if inbox_root.exists():
        for path in sorted(inbox_root.rglob("*.md")):
            text = path.read_text()
            if text.startswith("---\n") and "\n---bottom-matter---\n" in text:
                front, bottom = parse_markdown_contract(path)
                key_union = collect_normalized_keys(front) | collect_normalized_keys(bottom)
                governed_packets.append(
                    {
                        "path": str(path.relative_to(ROOT)),
                        "artifact_type": front.get("artifact_type"),
                        "keys": sorted(key_union),
                    }
                )
                is_governed_packet = (
                    front.get("doctype") == "inbox_packet"
                    or front.get("structured_contract_ref") == "contracts/inbox-packet.yaml"
                )
                if is_governed_packet and "artifact_type" in front and front["artifact_type"] not in INBOX_PACKET_ARTIFACT_TYPES:
                    raise AssertionError(f"{path.relative_to(ROOT)} declares an unknown inbox packet artifact type.")
                if is_governed_packet and front.get("artifact_type") in INBOX_PACKET_ARTIFACT_TYPES:
                    missing_keys = sorted(
                        field
                        for field in INBOX_PACKET_REQUIRED_FIELDS
                        if field not in key_union
                    )
                    if missing_keys:
                        raise AssertionError(
                            f"{path.relative_to(ROOT)} is missing governed inbox packet keys: {missing_keys}"
                        )
                    if not (INBOX_PACKET_SCOPE_FIELDS & key_union):
                        raise AssertionError(f"{path.relative_to(ROOT)} must carry project or target scope keys.")
                    if not (INBOX_PACKET_FRESHNESS_FIELDS & key_union):
                        raise AssertionError(f"{path.relative_to(ROOT)} must carry freshness metadata keys.")
                    missing_packet_gates = sorted(
                        field for field in INBOX_GATE_FIELDS if field not in key_union
                    )
                    if missing_packet_gates:
                        raise AssertionError(
                            f"{path.relative_to(ROOT)} is missing governed inbox gate keys: {missing_packet_gates}"
                        )

    details.update(
        {
            "validated_contracts": validated_contracts,
            "validated_examples": validated_examples,
            "front_door_runtime_roles": sorted(heavy_runtime_roles),
            "governance_roles": sorted(governed_roles),
            "packet_artifact_types": sorted(packet_types),
            "governed_markdown_packets_found": governed_packets,
            "markdown_template_path": "prompts/governed-triad-follow-up-prompt.template.md",
        }
    )
    return details

def validate_subsystem_architecture_slice() -> dict:
    validated_contracts = 0
    validated_examples = 0
    errors: list[str] = []
    topology_first_subsystems: set[str] = set()
    topology_focus_areas: set[str] = set()

    for contract_rel, schema_rel in SUBSYSTEM_ARCHITECTURE_CONTRACTS.items():
        contract_path = ROOT / contract_rel
        schema_path = ROOT / schema_rel
        if not contract_path.exists() or not schema_path.exists():
            errors.append(f"missing:{contract_rel}")
            continue
        schema = json.loads(schema_path.read_text())
        contract = yaml.safe_load(contract_path.read_text())
        try:
            Draft202012Validator(schema).validate(contract)
        except Exception as exc:  # noqa: BLE001
            errors.append(f"{contract_rel}:{exc}")
            continue
        validated_contracts += 1
        if contract_rel == "contracts/subsystem-harness-topology.yaml":
            topology_first_subsystems = {item["subsystem_id"] for item in contract["first_subsystems"]}
            topology_focus_areas = set(contract["repo_catalog_lens"]["focus_areas"])

    if validated_contracts == len(SUBSYSTEM_ARCHITECTURE_CONTRACTS):
        try:
            require_subset("Subsystem topology first_subsystems", SUBSYSTEM_IDS, topology_first_subsystems)
            require_subset("Subsystem topology focus areas", SUBSYSTEM_FIT_AREAS, topology_focus_areas)
        except AssertionError as exc:
            errors.append(str(exc))

    for example_rel, schema_rel in SUBSYSTEM_ARCHITECTURE_VALID_EXAMPLES:
        example_path = ROOT / example_rel
        schema_path = ROOT / schema_rel
        if not example_path.exists() or not schema_path.exists():
            errors.append(f"missing:{example_rel}")
            continue
        schema = json.loads(schema_path.read_text())
        instance = json.loads(example_path.read_text())
        try:
            Draft202012Validator(schema).validate(instance)
        except Exception as exc:  # noqa: BLE001
            errors.append(f"{example_rel}:{exc}")
            continue
        validated_examples += 1

    record_path = ROOT / "source/subsystems/registry.json"
    record_schema_path = ROOT / "schemas/subsystem-registry-record.schema.json"
    scaffold_paths = [
        "source/subsystems/README.md",
        "source/subsystems/intake-etl.md",
        "source/subsystems/research-harvest.md",
        "source/subsystems/semantic-cartography.md",
        "source/subsystems/wrapper-synthesizer.md",
    ]
    missing_scaffolds = [path for path in scaffold_paths if not (ROOT / path).exists()]
    if missing_scaffolds:
        errors.append(f"missing scaffold files: {missing_scaffolds}")

    repo_count = 0
    shortlist_count = 0
    if not record_path.exists():
        errors.append("missing:source/subsystems/registry.json")
    elif not record_schema_path.exists():
        errors.append("missing:schemas/subsystem-registry-record.schema.json")
    else:
        record_schema = json.loads(record_schema_path.read_text())
        record = json.loads(record_path.read_text())
        try:
            Draft202012Validator(record_schema).validate(record)
        except Exception as exc:  # noqa: BLE001
            errors.append(f"source/subsystems/registry.json:{exc}")
        else:
            repo_catalog = record["repo_catalog"]
            repo_count = len(repo_catalog)
            shortlist_count = len(record["reusable_infrastructure_shortlist"])
            repo_ids = {item["repo_id"] for item in repo_catalog}
            repo_classifications = {item["classification"] for item in repo_catalog}
            fit_areas = {
                fit_area
                for item in repo_catalog
                for fit_area in item["best_fit_subsystems"]
            }
            active_lanes = set(record["runtime_truth"]["active_parent_runtime_lanes"])
            blocked_lanes = {item["lane_id"] for item in record["runtime_truth"]["blocked_parent_runtime_lanes"]}
            non_activated_lanes = set(record["runtime_truth"]["non_activated_subsystem_lanes"])
            subsystem_ids = {item["subsystem_id"] for item in record["subsystems"]}
            try:
                require_subset("Subsystem registry subsystem ids", SUBSYSTEM_IDS, subsystem_ids)
                require_subset("Subsystem registry fit areas", SUBSYSTEM_FIT_AREAS, fit_areas)
                require_subset(
                    "Subsystem registry active parent runtime lanes",
                    {"peer_mesh_local.same_host", "inbox_protocol.same_host"},
                    active_lanes,
                )
                require_subset(
                    "Subsystem registry blocked runtime lanes",
                    {"peer_mesh_local.cross_device", "inbox_protocol.cross_device"},
                    blocked_lanes,
                )
                require_subset("Subsystem registry non-activated subsystem lanes", SUBSYSTEM_IDS, non_activated_lanes)
                require_subset("Subsystem registry classifications", ALLOWED_CAPABILITY_CLASSIFICATIONS, repo_classifications)
            except AssertionError as exc:
                errors.append(str(exc))
            if len(repo_ids) != 20:
                errors.append("Subsystem registry must classify exactly 20 unique repos.")
            if shortlist_count < 5:
                errors.append("Subsystem registry must keep at least 5 reusable-now shortlist entries.")

    if errors:
        raise AssertionError(" | ".join(errors))

    return {
        "validated_contracts": validated_contracts,
        "validated_examples": validated_examples,
        "registry_record": "source/subsystems/registry.json",
        "repo_count": repo_count,
        "shortlist_count": shortlist_count,
        "scaffold_paths": scaffold_paths,
    }


def validate_report_runtime_truth(report_instance: dict, iteration_rows: list[dict]) -> dict:
    errors: list[str] = []
    runtime_truth = report_instance.get("runtime_truth", {})
    score_saturation = report_instance.get("score_saturation", {})
    summary = json.loads((ROOT / "evaluation/tool-health/peer-mesh-local.json").read_text())
    status_report = json.loads((ROOT / "evaluation/tool-health/status.json").read_text())

    truth_level = runtime_truth.get("truth_level")
    if truth_level not in ALLOWED_RUNTIME_TRUTH_LEVELS:
        errors.append("runtime_truth.truth_level is missing or invalid.")

    runtime_mode = runtime_truth.get("runtime_mode_activated")
    if truth_level in {"bounded_runtime", "active_runtime"} and runtime_mode != "same_host":
        errors.append("runtime_truth.runtime_mode_activated must be same_host for the kept peer-mesh lane.")

    activation_artifacts = set(runtime_truth.get("activation_artifacts", []))
    observability_artifacts = set(runtime_truth.get("observability_artifacts", []))
    tool_health_evidence = set(runtime_truth.get("tool_health_evidence", []))
    expected_activation_artifacts = {
        "evaluation/tool-health/peer-mesh-local.json",
        "evaluation/tool-health/peer-mesh-local.log",
    }
    expected_observability_artifacts = {
        "evaluation/tool-health/peer-mesh-local-events.jsonl",
        "evaluation/tool-health/peer-mesh-local-benchmarks.json",
    }
    if truth_level in {"bounded_runtime", "active_runtime"}:
        if not expected_activation_artifacts.issubset(activation_artifacts):
            errors.append("runtime_truth.activation_artifacts is missing same-host activation proof.")
        if not expected_observability_artifacts.issubset(observability_artifacts):
            errors.append("runtime_truth.observability_artifacts is missing same-host observability proof.")
        if "evaluation/tool-health/status.json" not in tool_health_evidence:
            errors.append("runtime_truth.tool_health_evidence must include evaluation/tool-health/status.json.")

    completion_required = set(runtime_truth.get("completion_tokens_required", []))
    completion_observed = set(runtime_truth.get("completion_tokens_observed", []))
    summary_completion = summary.get("completion_tokens", {})
    if truth_level in {"bounded_runtime", "active_runtime"}:
        if completion_required != set(summary_completion.get("required", [])):
            errors.append("runtime_truth.completion_tokens_required does not match peer-mesh-local proof.")
        if completion_observed != set(summary_completion.get("observed", [])):
            errors.append("runtime_truth.completion_tokens_observed does not match peer-mesh-local proof.")

    summary_policy = set(summary.get("policy", {}).get("outcomes_observed", []))
    report_policy = set(runtime_truth.get("policy_outcomes_observed", []))
    if truth_level in {"bounded_runtime", "active_runtime"} and report_policy != summary_policy:
        errors.append("runtime_truth.policy_outcomes_observed does not match peer-mesh-local proof.")

    blocked_modes = runtime_truth.get("runtime_modes_blocked", [])
    cross_device = [item for item in blocked_modes if item.get("mode_id") == "cross_device"]
    if truth_level in {"bounded_runtime", "active_runtime"}:
        if not cross_device:
            errors.append("runtime_truth.runtime_modes_blocked must include cross_device.")
        elif normalize_status(cross_device[0].get("status")) != "blocked":
            errors.append("runtime_truth.runtime_modes_blocked cross_device entry must stay blocked.")

    blocked_lanes = {item.get("lane_id"): item for item in runtime_truth.get("blocked_lanes", [])}
    for lane_id, expected_status in REQUIRED_FOLLOW_ON_LANE_STATUS.items():
        lane = blocked_lanes.get(lane_id)
        if lane is None:
            errors.append(f"runtime_truth.blocked_lanes is missing {lane_id}.")
            continue
        if lane.get("status") != expected_status:
            errors.append(f"runtime_truth.blocked_lanes {lane_id} must stay {expected_status}.")

    mismatch_list = runtime_truth.get("mismatch_list", [])
    if truth_level in {"bounded_runtime", "active_runtime"} and not mismatch_list:
        errors.append("runtime_truth.mismatch_list must name the schema gaps closed by the kept slice.")

    command_evidence = runtime_truth.get("command_evidence", {})
    for key in ("activation_commands", "validation_commands", "tool_health_commands"):
        commands = command_evidence.get(key, [])
        if truth_level in {"bounded_runtime", "active_runtime"} and not commands:
            errors.append(f"runtime_truth.command_evidence.{key} must not be empty.")
        for command in commands:
            if not command.get("evidence_refs"):
                errors.append(f"runtime_truth.command_evidence.{key} contains a command without evidence_refs.")

    freshness = runtime_truth.get("freshness", {})
    freshness_paths = {item.get("path") for item in freshness.get("artifact_records", [])}
    required_freshness_paths = {
        "evaluation/copilot-ratchet-report.json",
        "evaluation/validation-report.json",
        "evaluation/metrics-latest.json",
        "promotion/readiness.json",
        "runs/iterations.jsonl",
        "evaluation/tool-health/status.json",
    }
    if truth_level in {"bounded_runtime", "active_runtime"} and not required_freshness_paths.issubset(freshness_paths):
        errors.append("runtime_truth.freshness.artifact_records is missing refreshed proof artifacts.")
    for path_str in freshness_paths:
        if path_str and not (ROOT / path_str).exists():
            errors.append(f"runtime_truth.freshness references missing artifact {path_str}.")

    latest_row = iteration_rows[-1] if iteration_rows else {}
    if latest_row:
        row_truth_level = latest_row.get("runtime_truth_level")
        if row_truth_level and row_truth_level != truth_level:
            errors.append("Latest iteration row runtime_truth_level does not match report.runtime_truth.truth_level.")

    if metric_review := report_instance.get("metric_review"):
        saturation_baseline = score_saturation.get("baseline_total_score")
        saturation_final = score_saturation.get("final_total_score")
        if saturation_baseline != metric_review.get("baseline_total_score"):
            errors.append("score_saturation.baseline_total_score must match metric_review.baseline_total_score.")
        if saturation_final != metric_review.get("final_total_score"):
            errors.append("score_saturation.final_total_score must match metric_review.final_total_score.")

    if score_saturation.get("baseline_total_score") == score_saturation.get("final_total_score"):
        if score_saturation.get("score_changed") is not False:
            errors.append("score_saturation.score_changed must be false when baseline and final total scores match.")
        if not score_saturation.get("flat_score_explanation"):
            errors.append("score_saturation.flat_score_explanation is required when the score stays flat.")

    peer_mesh_status = status_report.get("checks", {}).get("peer_mesh_local", {}).get("status")
    if truth_level in {"bounded_runtime", "active_runtime"} and not status_at_least(peer_mesh_status, "bounded_pass"):
        errors.append("tool-health/status.json no longer proves the bounded same-host peer-mesh lane.")

    return {
        "truth_level": truth_level,
        "runtime_mode_activated": runtime_mode,
        "latest_iteration": latest_row.get("iteration"),
        "errors": errors,
    }


def validate_gap_map_strength_slice() -> dict:
    errors: list[str] = []
    validated_contracts = 0
    validated_examples = 0

    for contract_rel, schema_rel in GAP_MAP_STRENGTH_CONTRACTS.items():
        contract_path = ROOT / contract_rel
        schema_path = ROOT / schema_rel
        if not contract_path.exists() or not schema_path.exists():
            errors.append(f"missing:{contract_rel}")
            continue
        schema = json.loads(schema_path.read_text())
        contract = yaml.safe_load(contract_path.read_text())
        try:
            Draft202012Validator.check_schema(schema)
            Draft202012Validator(schema).validate(contract)
        except Exception as exc:  # noqa: BLE001
            errors.append(f"{contract_rel}:{exc}")
            continue
        validated_contracts += 1

    report_path = ROOT / "evaluation/gap-map-strength-report.json"
    report_schema_path = ROOT / "schemas/gap-map-strength-report.schema.json"
    source_synthesis_path = ROOT / "source/gap-map-strength.md"
    if not report_path.exists():
        errors.append("missing:evaluation/gap-map-strength-report.json")
    if not source_synthesis_path.exists():
        errors.append("missing:source/gap-map-strength.md")

    report = {}
    contract = {}
    if validated_contracts == len(GAP_MAP_STRENGTH_CONTRACTS):
        contract = yaml.safe_load((ROOT / "contracts/gap-map-strength.yaml").read_text())
    if report_path.exists() and report_schema_path.exists():
        report_schema = json.loads(report_schema_path.read_text())
        report = json.loads(report_path.read_text())
        try:
            Draft202012Validator.check_schema(report_schema)
            Draft202012Validator(report_schema).validate(report)
        except Exception as exc:  # noqa: BLE001
            errors.append(f"evaluation/gap-map-strength-report.json:{exc}")

    for example_rel, schema_rel in GAP_MAP_STRENGTH_VALID_EXAMPLES:
        example_path = ROOT / example_rel
        schema_path = ROOT / schema_rel
        if not example_path.exists() or not schema_path.exists():
            errors.append(f"missing:{example_rel}")
            continue
        schema = json.loads(schema_path.read_text())
        instance = json.loads(example_path.read_text())
        try:
            Draft202012Validator(schema).validate(instance)
        except Exception as exc:  # noqa: BLE001
            errors.append(f"{example_rel}:{exc}")
            continue
        validated_examples += 1

    strong_area_ids: set[str] = set()
    missing_classes: set[str] = set()
    map_types: set[str] = set()
    underspecified_surfaces: set[str] = set()
    tool_focuses: set[str] = set()
    tool_ids: set[str] = set()
    blocker_lane_ids: set[str] = set()

    if report and contract:
        try:
            strong_area_ids = {item["area_id"] for item in report["strong_content"]}
            require_subset(
                "Gap map strong content areas",
                set(contract["strong_content_rules"]["required_areas"]),
                strong_area_ids,
            )
            for area in report["weak_content"]:
                for item in area["missing_items"]:
                    missing_classes.add(item["class"])
            require_subset(
                "Gap map missing-item classes",
                set(contract["weak_content_rules"]["required_missing_classes"]),
                missing_classes,
            )
            map_types = {item["map_type"] for item in report["workflow_structure"]["missing_maps"]}
            require_subset(
                "Gap map missing-map types",
                set(contract["workflow_rules"]["required_missing_map_types"]),
                map_types,
            )
            underspecified_surfaces = {
                item["surface_id"] for item in report["workflow_structure"]["underspecified_contracts"]
            }
            require_subset(
                "Gap map underspecified surfaces",
                set(contract["workflow_rules"]["required_underspecified_contract_surfaces"]),
                underspecified_surfaces,
            )
            for item in report["runnable_tools"]:
                tool_ids.add(item["tool_id"])
                tool_focuses.update(item["helping_areas"])
            if len(report["runnable_tools"]) < int(contract["tool_shortlist_rules"]["minimum_tools"]):
                raise AssertionError("Gap map runnable tool shortlist is shorter than the contract minimum.")
            require_subset(
                "Gap map runnable tool focus areas",
                set(contract["tool_shortlist_rules"]["required_focus_areas"]),
                tool_focuses,
            )

            topology = yaml.safe_load((ROOT / "contracts/subsystem-harness-topology.yaml").read_text())
            runtime_truth = report["runtime_truth"]
            if runtime_truth["runtime_truth_level"] != "bounded_runtime":
                raise AssertionError("Gap map runtime_truth_level must stay bounded_runtime.")
            if set(runtime_truth["active_parent_runtime_lanes"]) != set(
                topology["parent_kernel"]["active_parent_runtime_lanes"]
            ):
                raise AssertionError("Gap map active_parent_runtime_lanes must match subsystem topology truth.")
            blocker_lane_ids = {
                item["lane_id"] for item in runtime_truth["blocked_parent_runtime_lanes"]
            }
            expected_blocked_lane_ids = {
                item["lane_id"] for item in topology["parent_kernel"]["blocked_parent_runtime_lanes"]
            }
            if blocker_lane_ids != expected_blocked_lane_ids:
                raise AssertionError("Gap map blocked_parent_runtime_lanes must match subsystem topology truth.")
            if set(runtime_truth["non_activated_subsystem_lanes"]) != set(
                topology["parent_kernel"]["non_activated_subsystem_lanes"]
            ):
                raise AssertionError("Gap map non_activated_subsystem_lanes must match subsystem topology truth.")

            tool_health = json.loads((ROOT / "evaluation/tool-health/status.json").read_text())
            infranodus_live_status = (
                tool_health.get("checks", {})
                .get("infranodus", {})
                .get("truth_boundary", {})
                .get("live_status")
            )
            if infranodus_live_status != report["infranodus_path"]["live_status"]:
                raise AssertionError("Gap map InfraNodus live_status must match tool-health status.")
            if infranodus_live_status != "pass" and report["infranodus_path"]["mode"] != "bounded_local_cli_substitute":
                raise AssertionError("Gap map must stay on the bounded InfraNodus path while live remains blocked.")
            if report["follow_up_prompt"]["target_schema_ref"] != contract["follow_up_prompt_requirements"]["structured_prompt_schema_ref"]:
                raise AssertionError("Gap map follow-up prompt must point at the governed heavy-run prompt schema.")
        except AssertionError as exc:
            errors.append(str(exc))

    return {
        "validated_contracts": validated_contracts,
        "validated_examples": validated_examples,
        "strong_content_area_ids": sorted(strong_area_ids),
        "missing_item_classes": sorted(missing_classes),
        "missing_map_types": sorted(map_types),
        "underspecified_surfaces": sorted(underspecified_surfaces),
        "tool_ids": sorted(tool_ids),
        "tool_focus_areas": sorted(tool_focuses),
        "blocker_lane_ids": sorted(blocker_lane_ids),
        "source_synthesis_ref": "source/gap-map-strength.md",
        "errors": errors,
    }


def validate_tool_packaging_slice() -> dict:
    errors: list[str] = []
    validated_contracts = 0
    validated_examples = 0
    source_guidance_path = ROOT / "source/tool-packaging-contract-family.md"

    contract = {}
    for contract_rel, schema_rel in TOOL_PACKAGING_CONTRACTS.items():
        contract_path = ROOT / contract_rel
        schema_path = ROOT / schema_rel
        if not contract_path.exists() or not schema_path.exists():
            errors.append(f"missing:{contract_rel}")
            continue
        schema = json.loads(schema_path.read_text())
        contract = yaml.safe_load(contract_path.read_text())
        try:
            Draft202012Validator.check_schema(schema)
            Draft202012Validator(schema).validate(contract)
        except Exception as exc:  # noqa: BLE001
            errors.append(f"{contract_rel}:{exc}")
            continue
        validated_contracts += 1

    for example_rel, schema_rel in TOOL_PACKAGING_VALID_EXAMPLES:
        example_path = ROOT / example_rel
        schema_path = ROOT / schema_rel
        if not example_path.exists() or not schema_path.exists():
            errors.append(f"missing:{example_rel}")
            continue
        schema = json.loads(schema_path.read_text())
        instance = json.loads(example_path.read_text())
        try:
            Draft202012Validator.check_schema(schema)
            Draft202012Validator(schema).validate(instance)
        except Exception as exc:  # noqa: BLE001
            errors.append(f"{example_rel}:{exc}")
            continue
        validated_examples += 1

    if not source_guidance_path.exists():
        errors.append("missing:source/tool-packaging-contract-family.md")

    boundary = contract.get("packaging_boundary", {})
    surfaces = contract.get("contract_surfaces", {})
    storage_truth = contract.get("storage_truth", {})
    validation = contract.get("validation", {})

    if validated_contracts == len(TOOL_PACKAGING_CONTRACTS):
        expected_surface_refs = {
            "schemas/tool-packaging-family.schema.json",
            "schemas/tool-spec.schema.json",
            "schemas/agent-card.schema.json",
            "schemas/tool-task.schema.json",
            "schemas/tool-artifact.schema.json",
        }
        actual_surface_refs = set(surfaces.values())
        if actual_surface_refs != expected_surface_refs:
            errors.append("tool-packaging contract_surfaces do not point at the full schema family.")
        if not boundary.get("endpoint_first"):
            errors.append("tool-packaging packaging_boundary.endpoint_first must stay true.")
        if not boundary.get("artifact_registry_linkage_required"):
            errors.append("tool-packaging packaging_boundary.artifact_registry_linkage_required must stay true.")
        if storage_truth.get("pixeltable_sync_status") != "blocked_not_activated":
            errors.append("tool-packaging storage truth must keep pixeltable blocked_not_activated.")
        if storage_truth.get("duckdb_query_surface_status") != "planned_not_activated":
            errors.append("tool-packaging storage truth must keep duckdb planned_not_activated.")
        if len(validation.get("valid_examples", [])) < len(TOOL_PACKAGING_VALID_EXAMPLES):
            errors.append("tool-packaging validation.valid_examples is incomplete.")

    return {
        "validated_contracts": validated_contracts,
        "validated_examples": validated_examples,
        "source_guidance_present": source_guidance_path.exists(),
        "endpoint_first": boundary.get("endpoint_first"),
        "artifact_registry_linkage_required": boundary.get("artifact_registry_linkage_required"),
        "pixeltable_sync_status": storage_truth.get("pixeltable_sync_status"),
        "duckdb_query_surface_status": storage_truth.get("duckdb_query_surface_status"),
        "schema_refs": sorted(set(surfaces.values())),
        "errors": errors,
    }


def validate_subsystem_runner_proof_slice() -> dict:
    errors: list[str] = []
    validated_contracts = 0
    validated_examples = 0
    source_guidance_path = ROOT / "source/subsystem-runner-proof-family.md"

    loaded_contracts: dict[str, dict] = {}
    for contract_rel, schema_rel in SUBSYSTEM_RUNNER_PROOF_CONTRACTS.items():
        contract_path = ROOT / contract_rel
        schema_path = ROOT / schema_rel
        if not contract_path.exists() or not schema_path.exists():
            errors.append(f"missing:{contract_rel}")
            continue
        schema = json.loads(schema_path.read_text())
        contract = yaml.safe_load(contract_path.read_text())
        try:
            Draft202012Validator.check_schema(schema)
            Draft202012Validator(schema).validate(contract)
        except Exception as exc:  # noqa: BLE001
            errors.append(f"{contract_rel}:{exc}")
            continue
        loaded_contracts[contract_rel] = contract
        validated_contracts += 1

    for example_rel, schema_rel in SUBSYSTEM_RUNNER_PROOF_VALID_EXAMPLES:
        example_path = ROOT / example_rel
        schema_path = ROOT / schema_rel
        if not example_path.exists() or not schema_path.exists():
            errors.append(f"missing:{example_rel}")
            continue
        schema = json.loads(schema_path.read_text())
        instance = json.loads(example_path.read_text())
        try:
            Draft202012Validator.check_schema(schema)
            Draft202012Validator(schema).validate(instance)
        except Exception as exc:  # noqa: BLE001
            errors.append(f"{example_rel}:{exc}")
            continue
        validated_examples += 1

    if not source_guidance_path.exists():
        errors.append("missing:source/subsystem-runner-proof-family.md")

    family_contract = loaded_contracts.get("contracts/subsystem-runner-proof-family.yaml", {})
    map_contract = loaded_contracts.get("contracts/contract-to-runner-map.yaml", {})
    probe_contract = loaded_contracts.get("contracts/subsystem-bounded-probe.yaml", {})
    handshake_contract = loaded_contracts.get("contracts/subsystem-observability-handshake.yaml", {})
    report_schema_path = ROOT / "schemas/subsystem-runner-proof-strengthening-report.schema.json"
    report_path = ROOT / "evaluation/subsystem-runner-proof-strengthening-report.json"
    report_markdown_path = ROOT / "evaluation/subsystem-runner-proof-strengthening-report.md"

    family_states = set(family_contract.get("proof_state_vocabulary", {}).get("required_states", []))
    required_states = {
        "designed_not_activated",
        "bounded_probe_blocked",
        "bounded_probe_pass",
        "activation_proven_same_host",
    }
    if family_states and family_states != required_states:
        errors.append("subsystem-runner-proof family required_states must match the governed proof-state vocabulary.")

    boundary_rows = map_contract.get("runner_boundaries", [])
    boundary_ids = {row.get("subsystem_id") for row in boundary_rows}
    if boundary_ids and boundary_ids != SUBSYSTEM_IDS:
        errors.append("contract-to-runner map must cover the four governed subsystem ids exactly.")
    if any(row.get("current_proof_state") != "designed_not_activated" for row in boundary_rows):
        errors.append("current subsystem runner proof states must remain designed_not_activated in this slice.")

    truth_boundary = probe_contract.get("truth_boundary", {})
    if truth_boundary.get("allowed_parent_runtime_lanes") != [
        "peer_mesh_local.same_host",
        "inbox_protocol.same_host",
    ]:
        errors.append("subsystem-bounded-probe truth boundary must stay on same-host parent runtime lanes.")
    if not truth_boundary.get("no_child_runtime_adoption_claims"):
        errors.append("subsystem-bounded-probe must keep child runtime adoption blocked.")
    if not truth_boundary.get("no_pixeltable_or_duckdb_activation_claims"):
        errors.append("subsystem-bounded-probe must keep Pixeltable and DuckDB activation blocked.")

    handshake_requirements = handshake_contract.get("handshake_requirements", {})
    if handshake_requirements.get("failure_mode") != "fail_loud":
        errors.append("subsystem observability handshake must stay fail_loud.")
    if "validation_refreshed" not in handshake_requirements.get("required_event_types", []):
        errors.append("subsystem observability handshake must require validation_refreshed events.")
    if not report_schema_path.exists():
        errors.append("missing:schemas/subsystem-runner-proof-strengthening-report.schema.json")
    if report_schema_path.exists() and report_path.exists():
        try:
            report_schema = json.loads(report_schema_path.read_text())
            report_instance = json.loads(report_path.read_text())
            Draft202012Validator.check_schema(report_schema)
            Draft202012Validator(report_schema).validate(report_instance)
            follow_up = report_instance.get("follow_up_prompt", {})
            if not (ROOT / follow_up.get("artifact_path", "")).exists():
                errors.append("subsystem runner proof report follow-up prompt artifact is missing.")
            if not (ROOT / follow_up.get("markdown_companion_artifact_path", "")).exists():
                errors.append("subsystem runner proof report follow-up markdown companion is missing.")
        except Exception as exc:  # noqa: BLE001
            errors.append(f"evaluation/subsystem-runner-proof-strengthening-report.json:{exc}")
    else:
        errors.append("missing:evaluation/subsystem-runner-proof-strengthening-report.json")
    if not report_markdown_path.exists():
        errors.append("missing:evaluation/subsystem-runner-proof-strengthening-report.md")

    return {
        "validated_contracts": validated_contracts,
        "validated_examples": validated_examples,
        "source_guidance_present": source_guidance_path.exists(),
        "report_schema_present": report_schema_path.exists(),
        "report_present": report_path.exists(),
        "report_markdown_present": report_markdown_path.exists(),
        "proof_states": sorted(family_states),
        "runner_boundary_ids": sorted(boundary_ids),
        "handshake_failure_mode": handshake_requirements.get("failure_mode"),
        "errors": errors,
    }


def validate_capability_metrics_contract() -> dict:
    schema = json.loads((ROOT / "schemas/capability-harvest-metrics.schema.json").read_text())
    contract = yaml.safe_load((ROOT / "contracts/parent-capability-metrics.yaml").read_text())
    Draft202012Validator(schema).validate(contract)
    expected_ids = {
        "documentation_quality",
        "execution_success",
        "validation_pass_rate",
        "tool_health_availability",
        "latency_runtime",
        "cost_local_resource_use",
        "reproducibility",
        "blocker_precision",
        "evidence_freshness",
        "operator_usability",
        "regression_resistance",
    }
    actual_ids = {item["id"] for item in contract["metric_families"]}
    missing = sorted(expected_ids - actual_ids)
    extra = sorted(actual_ids - expected_ids)
    if missing or extra:
        raise AssertionError(
            f"Capability metrics contract IDs do not match expected set. Missing={missing} Extra={extra}"
        )
    return {
        "path": "contracts/parent-capability-metrics.yaml",
        "metric_family_count": len(contract["metric_families"]),
        "metric_ids": sorted(actual_ids),
    }


def validate_research_governance() -> dict:
    contract_schema = json.loads((ROOT / RESEARCH_SCHEMA_PATHS["research_manifest_contract"]).read_text())
    contract = yaml.safe_load((ROOT / "contracts/research-packet-manifest.yaml").read_text())
    Draft202012Validator(contract_schema).validate(contract)
    evidence_strength_schema = json.loads((ROOT / "schemas/evidence-strength.schema.json").read_text())

    compiled_schemas = {
        key: json.loads((ROOT / rel).read_text())
        for key, rel in RESEARCH_SCHEMA_PATHS.items()
        if key != "research_manifest_contract"
    }
    for schema in compiled_schemas.values():
        Draft202012Validator.check_schema(schema)

    current_understanding = json.loads((ROOT / "evaluation/research/current-understanding.json").read_text())
    harvest_manifest = json.loads((ROOT / "evaluation/research/harvest-manifest.json").read_text())
    capability_harvest = json.loads((ROOT / contract["authority"]["compiled_outputs"]["capability_harvest"]).read_text())
    feature_matrix = json.loads((ROOT / contract["authority"]["compiled_outputs"]["feature_matrix"]).read_text())
    gap_map = json.loads((ROOT / contract["authority"]["compiled_outputs"]["gap_placement_map"]).read_text())
    source_index = json.loads((ROOT / contract["authority"]["compiled_outputs"]["source_index"]).read_text())

    Draft202012Validator(compiled_schemas["compiled_capability_harvest"]).validate(capability_harvest)
    Draft202012Validator(compiled_schemas["compiled_feature_matrix"]).validate(feature_matrix)
    Draft202012Validator(compiled_schemas["gap_placement_map"]).validate(gap_map)
    Draft202012Validator(compiled_schemas["source_index"]).validate(source_index)

    manifest_paths = (
        harvest_manifest["repo_packets"]
        + harvest_manifest["topic_packets"]
        + harvest_manifest["compiled_outputs"]
    )
    missing_manifest_paths = [path for path in manifest_paths if not (ROOT / path).exists()]
    if missing_manifest_paths:
        raise AssertionError(f"Harvest manifest paths are missing: {missing_manifest_paths}")

    compiled_paths = list(contract["authority"]["compiled_outputs"].values())
    if set(compiled_paths) != set(harvest_manifest["compiled_outputs"]):
        raise AssertionError("Research packet manifest compiled outputs must match harvest-manifest compiled outputs.")
    if set(current_understanding["compiler_targets"]) != set(compiled_paths):
        raise AssertionError("current-understanding compiler_targets must match the governed compiled outputs.")

    capability_matrix = yaml.safe_load((ROOT / "contracts/capability-matrix.yaml").read_text())
    matrix_rows = capability_matrix["capabilities"]
    feature_rows = feature_matrix["rows"]
    harvest_rows = capability_harvest["capabilities"]
    matrix_by_id = {row["capability_id"]: row for row in matrix_rows}
    feature_by_id = {row["capability_id"]: row for row in feature_rows}
    harvest_by_id = {row["capability_id"]: row for row in harvest_rows}

    if set(matrix_by_id) != set(feature_by_id):
        raise AssertionError(
            f"Capability matrix rows must align exactly with the compiled feature matrix. Missing={sorted(set(feature_by_id) - set(matrix_by_id))} Extra={sorted(set(matrix_by_id) - set(feature_by_id))}"
        )
    if set(harvest_by_id) != set(feature_by_id):
        raise AssertionError("Compiled capability harvest rows must align exactly with the compiled feature matrix.")

    required_feature_fields = set(contract["alignment"]["required_feature_fields"])
    for capability_id, feature_row in feature_by_id.items():
        matrix_row = matrix_by_id[capability_id]
        harvest_row = harvest_by_id[capability_id]
        for field in required_feature_fields:
            if matrix_row[field] != feature_row[field]:
                raise AssertionError(
                    f"Capability matrix drift for {capability_id} field {field}: {matrix_row[field]!r} != {feature_row[field]!r}"
                )
            if harvest_row[field] != feature_row[field]:
                raise AssertionError(
                    f"Capability harvest drift for {capability_id} field {field}: {harvest_row[field]!r} != {feature_row[field]!r}"
                )

    allowed_classifications = set(contract["classification_governance"]["allowed_values"])
    if allowed_classifications != ALLOWED_CAPABILITY_CLASSIFICATIONS:
        raise AssertionError("Research packet manifest classification language must match the governed lane vocabulary.")

    all_classifications = (
        [row["parent_lane_classification"] for row in feature_rows]
        + [row["parent_lane_classification"] for row in matrix_rows]
        + [lane["classification"] for lane in gap_map["lanes"]]
    )
    if any(classification == "optional" for classification in all_classifications):
        raise AssertionError("Useful governed lanes must not be labeled optional.")
    if not set(all_classifications).issubset(ALLOWED_CAPABILITY_CLASSIFICATIONS):
        raise AssertionError("Research classifications must stay inside the governed lane vocabulary.")

    core_capabilities = set(contract["classification_governance"]["required_core_capability_ids"])
    if core_capabilities != REQUIRED_RESEARCH_CORE_CAPABILITIES:
        raise AssertionError("Research packet manifest must keep the required core capability IDs explicit.")
    for capability_id in core_capabilities:
        if feature_by_id[capability_id]["parent_lane_classification"] != "core":
            raise AssertionError(f"{capability_id} must stay core in the compiled feature matrix.")
        if matrix_by_id[capability_id]["parent_lane_classification"] != "core":
            raise AssertionError(f"{capability_id} must stay core in the capability matrix.")
    if feature_by_id["pi-vs-claude-code"]["parent_lane_classification"] != "core":
        raise AssertionError("pi-vs-claude-code must stay core.")

    blocked_rows = [
        row["capability_id"]
        for row in feature_rows
        if row["parent_lane_classification"] == "blocked_with_exact_dependency"
    ]
    harvest_blockers = [item["capability_id"] for item in capability_harvest["exact_blockers"]]
    if sorted(blocked_rows) != sorted(harvest_blockers):
        raise AssertionError("Blocked lanes must stay explicit in both the feature matrix and compiled capability harvest.")
    if "agent-sandbox-skill" not in blocked_rows:
        raise AssertionError("The exact blocked sandbox lane must remain visible.")

    repo_packets = []
    for rel in harvest_manifest["repo_packets"]:
        repo_packet = json.loads((ROOT / rel).read_text())
        repo_packets.append(repo_packet)
        github_verification = repo_packet.get("github_verification", {})
        verified_commit = github_verification.get("verified_commit", "")
        if len(verified_commit) != 40 or not all(char in "0123456789abcdef" for char in verified_commit):
            raise AssertionError(f"{rel} must keep a 40-character pinned verified_commit.")

    all_github_refs = []
    for repo_packet in repo_packets:
        for source_ref in repo_packet.get("source_refs", []):
            ref = source_ref["ref"]
            if ref.startswith("https://github.com/"):
                all_github_refs.append(ref)
    for ref in all_github_refs:
        if not is_pinned_github_blob(ref):
            raise AssertionError(f"GitHub source refs must stay pinned to blob SHAs: {ref}")
    for source in source_index["sources"]:
        Draft202012Validator(evidence_strength_schema).validate(source["evidence_strength"])
        ref = source["ref"]
        if ref.startswith("https://github.com/") and not is_pinned_github_blob(ref):
            raise AssertionError(f"Compiled source index must keep pinned GitHub blob refs: {ref}")

    video_sources = []
    for source in source_index["sources"]:
        evidence_type = source["evidence_type"]
        if evidence_type in VIDEO_EVIDENCE_STRENGTH_BY_TYPE:
            expected_strength = VIDEO_EVIDENCE_STRENGTH_BY_TYPE[evidence_type]
            actual_strength = source.get("video_evidence_strength")
            if actual_strength != expected_strength:
                raise AssertionError(
                    f"Video evidence strength drift for {source['ref']}: expected {expected_strength!r}, got {actual_strength!r}"
                )
            if actual_strength == "terminal_or_frame_verified":
                raise AssertionError("Transcript or task-derived sources must not be promoted to terminal_or_frame_verified.")
            video_sources.append({"ref": source["ref"], "strength": actual_strength})
    if not video_sources:
        raise AssertionError("Research source index must preserve explicit video evidence-strength boundaries.")

    return {
        "manifest_path": "contracts/research-packet-manifest.yaml",
        "repo_packet_count": len(harvest_manifest["repo_packets"]),
        "topic_packet_count": len(harvest_manifest["topic_packets"]),
        "compiled_output_count": len(harvest_manifest["compiled_outputs"]),
        "capability_count": len(feature_rows),
        "core_capabilities": sorted(core_capabilities),
        "blocked_capabilities": sorted(blocked_rows),
        "video_sources": video_sources,
    }


def validate_consume_source_quality_outputs() -> dict:
    errors = []
    evidence_strength_schema = json.loads((ROOT / "schemas/evidence-strength.schema.json").read_text())
    operational_matrix_schema = json.loads((ROOT / "schemas/operational-feature-matrix.schema.json").read_text())
    source_index_schema = json.loads((ROOT / "schemas/source-index.schema.json").read_text())

    source_guidance_path = ROOT / "source/consume-source-quality-pipeline.md"
    source_index_path = ROOT / "evaluation/research/compiled/source-index.json"
    operational_matrix_path = ROOT / "evaluation/research/compiled/operational-feature-matrix.json"
    handoff_paths = [
        ROOT / "outbox/2026-05-22-operational-feature-matrix.handoff.md",
        ROOT / "outbox/2026-05-22-capability-matrix-extension.handoff.md",
        ROOT / "outbox/2026-05-22-consume-folder-extraction-map.handoff.md",
        ROOT / "outbox/2026-05-22-compiled-output-ingestion-map.handoff.md",
    ]

    if not source_guidance_path.exists():
        errors.append("missing:source/consume-source-quality-pipeline.md")
    if not source_index_path.exists():
        errors.append("missing:evaluation/research/compiled/source-index.json")
    if not operational_matrix_path.exists():
        errors.append("missing:evaluation/research/compiled/operational-feature-matrix.json")

    consume_source_count = 0
    transcript_blocked_count = 0
    operational_row_count = 0
    if source_index_path.exists():
        try:
            source_index = json.loads(source_index_path.read_text())
            Draft202012Validator(source_index_schema).validate(source_index)
            for source in source_index["sources"]:
                Draft202012Validator(evidence_strength_schema).validate(source["evidence_strength"])
                if source["kind"] == "consume_packet":
                    consume_source_count += 1
                if source["evidence_strength"]["transcript_derived"]:
                    if source["evidence_strength"]["workflow_claim_promotion"] != "blocked":
                        errors.append("Transcript-derived workflow claims must stay blocked in source-index evidence strength.")
                    transcript_blocked_count += 1
            if consume_source_count < 4:
                errors.append("source-index must contain at least four first-party consume_packet sources.")
        except Exception as exc:  # noqa: BLE001
            errors.append(f"evaluation/research/compiled/source-index.json:{exc}")

    if operational_matrix_path.exists():
        try:
            operational_matrix = json.loads(operational_matrix_path.read_text())
            Draft202012Validator(operational_matrix_schema).validate(operational_matrix)
            operational_row_count = len(operational_matrix["rows"])
        except Exception as exc:  # noqa: BLE001
            errors.append(f"evaluation/research/compiled/operational-feature-matrix.json:{exc}")

    missing_handoffs = [str(path.relative_to(ROOT)) for path in handoff_paths if not path.exists()]
    if missing_handoffs:
        errors.append(f"missing_handoffs:{missing_handoffs}")

    return {
        "source_guidance_present": source_guidance_path.exists(),
        "source_index_present": source_index_path.exists(),
        "operational_matrix_present": operational_matrix_path.exists(),
        "handoff_paths": [str(path.relative_to(ROOT)) for path in handoff_paths],
        "consume_source_count": consume_source_count,
        "transcript_blocked_count": transcript_blocked_count,
        "operational_row_count": operational_row_count,
        "errors": errors,
    }


def validate_consume_source_quality_report() -> dict:
    errors = []
    report_schema_path = ROOT / "schemas/consume-source-quality-strengthening-report.schema.json"
    report_path = ROOT / "evaluation/consume-source-quality-strengthening-report.json"
    report_markdown_path = ROOT / "evaluation/consume-source-quality-strengthening-report.md"
    prompt_path = ROOT / "prompts/PROMPT-20260522-CSQ3.yaml"
    prompt_markdown_path = ROOT / "prompts/PROMPT-20260522-CSQ3.md"

    if not report_schema_path.exists():
        errors.append("missing:schemas/consume-source-quality-strengthening-report.schema.json")
    if not report_path.exists():
        errors.append("missing:evaluation/consume-source-quality-strengthening-report.json")
    if not report_markdown_path.exists():
        errors.append("missing:evaluation/consume-source-quality-strengthening-report.md")
    if not prompt_path.exists():
        errors.append("missing:prompts/PROMPT-20260522-CSQ3.yaml")
    if not prompt_markdown_path.exists():
        errors.append("missing:prompts/PROMPT-20260522-CSQ3.md")

    if report_schema_path.exists() and report_path.exists():
        try:
            report_schema = json.loads(report_schema_path.read_text())
            report_instance = json.loads(report_path.read_text())
            Draft202012Validator.check_schema(report_schema)
            Draft202012Validator(report_schema).validate(report_instance)
            follow_up = report_instance.get("follow_up_prompt", {})
            if follow_up.get("artifact_path") != "prompts/PROMPT-20260522-CSQ3.yaml":
                errors.append("consume-source-quality report must point to PROMPT-20260522-CSQ3.yaml as the follow-up prompt.")
            if follow_up.get("markdown_companion_artifact_path") != "prompts/PROMPT-20260522-CSQ3.md":
                errors.append("consume-source-quality report must point to PROMPT-20260522-CSQ3.md as the follow-up markdown companion.")
        except Exception as exc:  # noqa: BLE001
            errors.append(f"evaluation/consume-source-quality-strengthening-report.json:{exc}")

    if prompt_path.exists():
        try:
            prompt_schema = json.loads((ROOT / "agent-heavy-run-prompt.schema.json").read_text())
            prompt_instance = yaml.safe_load(prompt_path.read_text())
            Draft202012Validator(prompt_schema).validate(prompt_instance)
        except Exception as exc:  # noqa: BLE001
            errors.append(f"prompts/PROMPT-20260522-CSQ3.yaml:{exc}")

    return {
        "report_schema_present": report_schema_path.exists(),
        "report_present": report_path.exists(),
        "report_markdown_present": report_markdown_path.exists(),
        "follow_up_prompt_present": prompt_path.exists(),
        "follow_up_prompt_markdown_present": prompt_markdown_path.exists(),
        "errors": errors,
    }


def validate_tool_health_truth() -> dict:
    path = ROOT / "evaluation" / "tool-health" / "status.json"
    if not path.exists():
        raise AssertionError("evaluation/tool-health/status.json is missing")

    payload = json.loads(path.read_text())
    checks = payload.get("checks", {})
    failures = []

    gitnexus = checks.get("gitnexus", {})
    gitnexus_boundary = gitnexus.get("truth_boundary", {})
    if not status_at_least(gitnexus.get("status"), "bounded_pass"):
        failures.append("GitNexus strongest honest status must be at least bounded_pass.")
    if not gitnexus.get("strongest_honest_scope"):
        failures.append("GitNexus strongest_honest_scope must be present.")
    if not status_at_least(gitnexus_boundary.get("strongest_honest_status"), "bounded_pass"):
        failures.append("GitNexus truth_boundary strongest_honest_status must be at least bounded_pass.")
    if not gitnexus_boundary.get("bounded_scope"):
        failures.append("GitNexus truth_boundary must declare a bounded_scope.")
    if not gitnexus_boundary.get("bounded_evidence"):
        failures.append("GitNexus truth_boundary must declare bounded_evidence.")
    if not gitnexus_boundary.get("limitation"):
        failures.append("GitNexus truth_boundary must carry an explicit limitation.")
    if not status_at_least(gitnexus.get("fixture_probe", {}).get("status"), "bounded_pass"):
        failures.append("GitNexus fixture_probe must stay at least bounded_pass.")
    if not gitnexus.get("fixture_probe", {}).get("command"):
        failures.append("GitNexus fixture_probe command must be recorded.")
    if not gitnexus.get("fixture_probe", {}).get("evidence"):
        failures.append("GitNexus fixture_probe evidence must be recorded.")
    if not gitnexus.get("full_repo_probe", {}).get("command"):
        failures.append("GitNexus full_repo_probe command must be recorded.")

    graphify = checks.get("graphify", {})
    graphify_boundary = graphify.get("truth_boundary", {})
    if not status_at_least(graphify.get("status"), "bounded_pass"):
        failures.append("Graphify strongest honest status must be at least bounded_pass.")
    if not graphify.get("strongest_honest_scope"):
        failures.append("Graphify strongest_honest_scope must be present.")
    if not status_at_least(graphify_boundary.get("strongest_honest_status"), "bounded_pass"):
        failures.append("Graphify truth_boundary strongest_honest_status must be at least bounded_pass.")
    if not graphify_boundary.get("bounded_scope"):
        failures.append("Graphify truth_boundary must declare a bounded_scope.")
    if not graphify_boundary.get("bounded_evidence"):
        failures.append("Graphify truth_boundary must declare bounded_evidence.")
    if not graphify_boundary.get("limitation"):
        failures.append("Graphify truth_boundary must carry an explicit limitation.")
    if not graphify.get("probe", {}).get("command"):
        failures.append("Graphify probe command must be recorded.")
    if not graphify.get("probe", {}).get("evidence"):
        failures.append("Graphify probe evidence must be recorded.")

    infranodus = checks.get("infranodus", {})
    infranodus_boundary = infranodus.get("truth_boundary", {})
    if not status_at_least(infranodus.get("status"), "bounded_pass"):
        failures.append("InfraNodus strongest honest status must be at least bounded_pass.")
    if not infranodus.get("strongest_honest_scope"):
        failures.append("InfraNodus strongest_honest_scope must be present.")
    if not status_at_least(infranodus_boundary.get("strongest_honest_status"), "bounded_pass"):
        failures.append("InfraNodus truth_boundary strongest_honest_status must be at least bounded_pass.")
    if not infranodus_boundary.get("bounded_scope"):
        failures.append("InfraNodus truth_boundary must declare a bounded_scope.")
    if not infranodus_boundary.get("bounded_evidence"):
        failures.append("InfraNodus truth_boundary must declare bounded_evidence.")
    if not infranodus_boundary.get("live_status"):
        failures.append("InfraNodus truth_boundary must declare a live_status.")
    if not infranodus_boundary.get("live_mode"):
        failures.append("InfraNodus truth_boundary must declare a live_mode.")
    if not status_at_least(infranodus_boundary.get("live_status"), "pass") and not infranodus_boundary.get("live_blocker"):
        failures.append("InfraNodus truth_boundary must carry a live_blocker whenever live_status is not pass.")
    if not infranodus.get("probe", {}).get("evidence"):
        failures.append("InfraNodus bounded evidence must be recorded.")

    peer_mesh_local = checks.get("peer_mesh_local", {})
    peer_mesh_boundary = peer_mesh_local.get("truth_boundary", {})
    blocked_modes = peer_mesh_boundary.get("blocked_runtime_modes", [])
    cross_device_entries = [item for item in blocked_modes if item.get("mode_id") == "cross_device"]
    if not status_at_least(peer_mesh_local.get("status"), "bounded_pass"):
        failures.append("peer_mesh_local strongest honest status must be at least bounded_pass.")
    if peer_mesh_local.get("strongest_honest_scope") != "same_host_runtime":
        failures.append("peer_mesh_local strongest_honest_scope must stay same_host_runtime.")
    if not status_at_least(peer_mesh_boundary.get("strongest_honest_status"), "bounded_pass"):
        failures.append("peer_mesh_local truth_boundary strongest_honest_status must be at least bounded_pass.")
    if "same_host" not in peer_mesh_boundary.get("active_runtime_modes", []):
        failures.append("peer_mesh_local must keep same_host in active_runtime_modes.")
    if not cross_device_entries:
        failures.append("peer_mesh_local must keep an explicit blocked cross_device runtime boundary.")
    elif normalize_status(cross_device_entries[0].get("status")) != "blocked":
        failures.append("peer_mesh_local cross_device boundary must stay blocked.")
    if not peer_mesh_local.get("activation_probe", {}).get("command"):
        failures.append("peer_mesh_local activation_probe command must be recorded.")
    if int(peer_mesh_local.get("activation_probe", {}).get("exit_code", 1)) != 0:
        failures.append("peer_mesh_local activation_probe must exit cleanly.")
    if not peer_mesh_local.get("activation_probe", {}).get("evidence"):
        failures.append("peer_mesh_local activation_probe evidence must be recorded.")

    if failures:
        raise AssertionError(" | ".join(failures))

    return {
        "path": "evaluation/tool-health/status.json",
        "gitnexus_status": gitnexus.get("status"),
        "graphify_status": graphify.get("status"),
        "infranodus_status": infranodus.get("status"),
        "live_infranodus_status": infranodus_boundary.get("live_status"),
        "peer_mesh_local_status": peer_mesh_local.get("status"),
    }


def validate_same_host_runtime_activation() -> dict:
    summary_path = ROOT / "evaluation" / "tool-health" / "peer-mesh-local.json"
    events_path = ROOT / "evaluation" / "tool-health" / "peer-mesh-local-events.jsonl"
    benchmarks_path = ROOT / "evaluation" / "tool-health" / "peer-mesh-local-benchmarks.json"
    log_path = ROOT / "evaluation" / "tool-health" / "peer-mesh-local.log"

    if not summary_path.exists():
        raise AssertionError("evaluation/tool-health/peer-mesh-local.json is missing")
    if not events_path.exists():
        raise AssertionError("evaluation/tool-health/peer-mesh-local-events.jsonl is missing")
    if not benchmarks_path.exists():
        raise AssertionError("evaluation/tool-health/peer-mesh-local-benchmarks.json is missing")
    if not log_path.exists():
        raise AssertionError("evaluation/tool-health/peer-mesh-local.log is missing")

    summary = json.loads(summary_path.read_text())
    events, parse_errors = load_jsonl(events_path)
    if parse_errors:
        raise AssertionError(f"peer-mesh-local-events.jsonl parse errors: {parse_errors}")
    benchmarks = json.loads(benchmarks_path.read_text())

    if summary.get("capability_id") != "pi-vs-claude-code":
        raise AssertionError("Same-host runtime proof must stay centered on pi-vs-claude-code.")
    if not status_at_least(summary.get("status"), "bounded_pass"):
        raise AssertionError("Same-host runtime proof must be at least bounded_pass.")
    if summary.get("activation_result") != "active":
        raise AssertionError("Same-host runtime proof must mark activation_result active.")
    if summary.get("runtime_mode") != "same_host":
        raise AssertionError("Same-host runtime proof must declare runtime_mode same_host.")

    mismatch_ids = {item["mismatch_id"] for item in summary.get("runtime_mismatch_list", [])}
    require_subset("Same-host runtime mismatch IDs", REQUIRED_RUNTIME_MISMATCH_IDS, mismatch_ids)

    operations = summary.get("operations", {})
    require_subset("Same-host runtime operations", REQUIRED_RUNTIME_OPERATIONS, set(operations))
    if operations["bootstrap"].get("peer_count", 0) < 4:
        raise AssertionError("Same-host bootstrap must register all governed peers.")
    if operations["list_agents"].get("peer_count", 0) < 4:
        raise AssertionError("list_agents must return the governed same-host peer registry.")
    if operations["send_prompt"].get("policy_outcome") != "allow":
        raise AssertionError("The kept send_prompt path must include an allowed same-host exchange.")
    if operations["send_command"].get("status") != "done":
        raise AssertionError("The kept send_command path must complete with done.")
    if operations["send_command"].get("exit_code") != 0:
        raise AssertionError("The kept send_command path must capture a zero-exit successful command.")
    if len(operations["await_response"].get("verified_correlations", [])) < 5:
        raise AssertionError("await_response must verify the kept success, failed, and needs-human exchanges.")

    completion = summary.get("completion_tokens", {})
    require_subset("Same-host runtime required completion tokens", REQUIRED_COMPLETION_TOKENS, set(completion.get("required", [])))
    require_subset("Same-host runtime observed completion tokens", REQUIRED_COMPLETION_TOKENS, set(completion.get("observed", [])))
    if completion.get("enforced") is not True:
        raise AssertionError("Same-host runtime must mark completion tokens enforced.")
    if completion.get("failed_case", {}).get("completion_token") != "failed":
        raise AssertionError("Same-host runtime must preserve an explicit failed completion case.")
    if completion.get("needs_human_case", {}).get("completion_token") != "needs-human":
        raise AssertionError("Same-host runtime must preserve an explicit needs-human completion case.")

    policy = summary.get("policy", {})
    require_subset("Same-host runtime policy outcomes", {"allow", "ask"}, set(policy.get("outcomes_observed", [])))
    require_subset(
        "Same-host runtime hook IDs",
        {
            "peer-session-start",
            "peer-membership-refresh",
            "peer-prompt-guard",
            "peer-command-guard",
            "completion-verification",
        },
        set(policy.get("hook_ids_triggered", [])),
    )

    observability = summary.get("observability", {})
    if observability.get("event_count") != len(events):
        raise AssertionError("Same-host runtime observability event_count must match emitted JSONL rows.")
    require_subset(
        "Same-host runtime observability event types",
        REQUIRED_OBSERVABILITY_EVENTS,
        set(observability.get("required_event_types_observed", [])),
    )
    require_subset(
        "Same-host runtime session markers",
        REQUIRED_INGEST_SESSION_MARKERS,
        set(observability.get("session_markers_observed", [])),
    )
    event_types = {event["event_type"] for event in events}
    require_subset("Emitted observability event types", REQUIRED_OBSERVABILITY_EVENTS, event_types)

    library_distribution = summary.get("library_distribution", {})
    distribution_units = library_distribution.get("distribution_units", [])
    unit_types = {item["unit_type"] for item in distribution_units}
    require_subset("Same-host distributed unit types", REQUIRED_DISTRIBUTION_UNIT_TYPES, unit_types)
    refs = {item["ref"] for item in distribution_units}
    for item in distribution_units:
        allowed_prefixes = {f"{item['unit_type']}:"}
        if str(item.get("source", "")).startswith("contracts/"):
            allowed_prefixes.add("contract:")
        if not any(item["ref"].startswith(prefix) for prefix in allowed_prefixes):
            raise AssertionError(f"Distribution unit ref prefix drift: {item['ref']}")
        if not (ROOT / item["source"]).exists():
            raise AssertionError(f"Same-host runtime distribution unit source is missing: {item['source']}")
    if set(library_distribution.get("resolved_refs", [])) != refs:
        raise AssertionError("Same-host runtime resolved_refs must match distribution_units.")

    require_subset("Same-host runtime benchmark groups", REQUIRED_BENCHMARK_GROUPS, set(benchmarks.get("groups", [])))
    benchmark_groups = {item["benchmark_group"] for item in benchmarks.get("tuples", [])}
    require_subset("Emitted benchmark groups", REQUIRED_BENCHMARK_GROUPS, benchmark_groups)

    truth_boundary = summary.get("truth_boundary", {})
    if "same_host" not in truth_boundary.get("active_runtime_modes", []):
        raise AssertionError("Same-host runtime truth boundary must keep same_host active.")
    cross_device_entries = [item for item in truth_boundary.get("blocked_runtime_modes", []) if item.get("mode_id") == "cross_device"]
    if not cross_device_entries:
        raise AssertionError("Same-host runtime truth boundary must keep cross_device explicitly blocked.")
    if normalize_status(cross_device_entries[0].get("status")) != "blocked":
        raise AssertionError("Same-host runtime cross_device expansion must remain blocked.")
    if not truth_boundary.get("limitation"):
        raise AssertionError("Same-host runtime truth boundary must carry an explicit limitation.")

    blocked_follow_on = summary.get("blocked_follow_on_lanes", {})
    for capability_id, expected_status in REQUIRED_FOLLOW_ON_LANE_STATUS.items():
        lane = blocked_follow_on.get(capability_id)
        if not lane:
            raise AssertionError(f"Blocked follow-on lane is missing from runtime proof: {capability_id}")
        if lane.get("status") != expected_status or lane.get("expected_status") != expected_status:
            raise AssertionError(f"Follow-on lane classification drift for {capability_id}.")
        if not lane.get("blocker_or_dependency"):
            raise AssertionError(f"Follow-on lane must preserve an explicit blocker/dependency: {capability_id}")

    return {
        "summary_path": str(summary_path.relative_to(ROOT)),
        "events_path": str(events_path.relative_to(ROOT)),
        "benchmarks_path": str(benchmarks_path.relative_to(ROOT)),
        "log_path": str(log_path.relative_to(ROOT)),
        "event_count": len(events),
        "benchmark_groups": sorted(benchmark_groups),
        "observed_completion_tokens": sorted(set(completion.get("observed", []))),
    }


def validate_parent_native_contracts() -> dict:
    loaded_contracts = {}
    details = {
        "contracts": [],
        "role_ids": [],
        "role_classes": [],
        "hook_ids": [],
        "hook_classes": [],
        "capability_ids": [],
        "capability_surface_types": [],
        "distribution_unit_types": [],
        "benchmark_groups": [],
        "ingest_session_markers": [],
        "runtime_modes": [],
    }
    for contract_rel, schema_rel in PARENT_NATIVE_CONTRACTS.items():
        schema = json.loads((ROOT / schema_rel).read_text())
        contract = yaml.safe_load((ROOT / contract_rel).read_text())
        Draft202012Validator(schema).validate(contract)
        loaded_contracts[contract_rel] = contract
        details["contracts"].append(contract_rel)

    contract_surface_ids = set(PARENT_NATIVE_CONTRACTS.keys())

    peer_mesh = loaded_contracts["contracts/peer-mesh.yaml"]
    require_subset("Peer mesh contract surfaces", contract_surface_ids - {"contracts/peer-mesh.yaml"}, set(peer_mesh["contract_surfaces"]))
    require_subset("Peer mesh operations", REQUIRED_PEER_MESH_OPERATIONS, set(peer_mesh["protocol"]["required_operations"]))
    require_subset(
        "Peer mesh completion tokens",
        REQUIRED_COMPLETION_TOKENS,
        set(peer_mesh["protocol"]["required_completion_tokens"]),
    )
    require_subset("Peer mesh runtime modes", REQUIRED_RUNTIME_MODES, set(peer_mesh["runtime_boundary"]["mode_refs"]))

    role_contract = loaded_contracts["contracts/agent-role-contract.yaml"]
    role_ids = [role["role_id"] for role in role_contract["roles"]]
    role_classes = [role["role_class"] for role in role_contract["roles"]]
    if len(role_ids) != len(set(role_ids)):
        raise AssertionError("Agent role IDs must stay unique.")
    require_subset("Agent role classes", REQUIRED_ROLE_CLASSES, set(role_classes))
    owned_lanes = [role["owned_lane"] for role in role_contract["roles"]]
    if len(owned_lanes) != len(set(owned_lanes)):
        raise AssertionError("Agent roles must keep one-lane ownership without scope overlap.")
    require_subset(
        "Agent governing contracts",
        {
            "contracts/peer-mesh.yaml",
            "contracts/peer-message.yaml",
            "contracts/observability-ingest.yaml",
            "contracts/policy-decision.yaml",
            "contracts/library-distribution.yaml",
            "contracts/benchmark-emission.yaml",
            "contracts/hook-manifest.yaml",
        },
        set(role_contract["governing_contracts"]),
    )
    if not any(
        role["role_class"] == "prod_boundary"
        and role["permissions"]["can_access_prod"]
        and role["permissions"]["requires_pii_redaction"]
        for role in role_contract["roles"]
    ):
        raise AssertionError("At least one governed role must own the production redaction boundary.")
    if not any(
        role["role_class"] == "mesh_bootstrap" and "list_agents" in role["message_operations"]
        for role in role_contract["roles"]
    ):
        raise AssertionError("At least one governed role must own mesh bootstrap and list_agents discovery.")
    if not any(
        role["role_class"] == "execution_driver"
        and role["permissions"]["can_send_command"]
        and role["permissions"]["can_send_prompt"]
        for role in role_contract["roles"]
    ):
        raise AssertionError("At least one governed role must own delegated prompt and command execution.")
    if not any(
        role["role_class"] == "verification_guard"
        and role["verification_boundary"]["observability_event_required"]
        for role in role_contract["roles"]
    ):
        raise AssertionError("At least one governed role must own observability-backed completion verification.")
    details["role_ids"] = sorted(role_ids)
    details["role_classes"] = sorted(set(role_classes))

    hook_manifest = loaded_contracts["contracts/hook-manifest.yaml"]
    hook_ids = [hook["hook_id"] for hook in hook_manifest["hooks"]]
    hook_classes = [hook["hook_class"] for hook in hook_manifest["hooks"]]
    if len(hook_ids) != len(set(hook_ids)):
        raise AssertionError("Hook IDs must stay unique.")
    require_subset("Hook classes", REQUIRED_HOOK_CLASSES, set(hook_classes))
    require_subset(
        "Hook policy contracts",
        {"contracts/policy-decision.yaml", "contracts/observability-event.yaml"},
        set(hook_manifest["policy_contracts"]),
    )
    hook_ids_set = set(hook_ids)
    role_ids_set = set(role_ids)
    governed_hook_operations = set()
    targeted_contracts = set()
    for hook in hook_manifest["hooks"]:
        if hook["runtime_actor"] not in role_ids_set:
            raise AssertionError(f"{hook['hook_id']} references an unknown runtime actor: {hook['runtime_actor']}")
        if not set(hook["target_contract_surfaces"]).issubset(contract_surface_ids):
            raise AssertionError(f"{hook['hook_id']} targets an unknown contract surface.")
        if not set(hook["policy_outcomes"]).issubset(REQUIRED_POLICY_OUTCOMES):
            raise AssertionError(f"{hook['hook_id']} declares an unknown policy outcome.")
        governed_hook_operations |= set(hook["governed_operations"])
        targeted_contracts |= set(hook["target_contract_surfaces"])
    require_subset("Hook governed operations", {"send_prompt", "send_command", "await_response", "list_agents"}, governed_hook_operations)
    require_subset(
        "Hook target contract coverage",
        {
            "contracts/observability-ingest.yaml",
            "contracts/library-distribution.yaml",
            "contracts/benchmark-emission.yaml",
        },
        targeted_contracts,
    )
    details["hook_ids"] = sorted(hook_ids)
    details["hook_classes"] = sorted(set(hook_classes))

    capability_matrix = loaded_contracts["contracts/capability-matrix.yaml"]
    capability_ids = [item["capability_id"] for item in capability_matrix["capabilities"]]
    capability_surface_types = [item["parent_surface_type"] for item in capability_matrix["capabilities"]]
    capability_operations = set()
    allowed_target_surfaces = contract_surface_ids | ALLOWED_CAPABILITY_TARGET_SURFACES
    if len(capability_ids) != len(set(capability_ids)):
        raise AssertionError("Capability matrix rows must stay unique.")
    require_subset("Capability surface types", REQUIRED_CAPABILITY_SURFACE_TYPES, set(capability_surface_types))
    distribution_targeted = False
    observability_targeted = False
    for item in capability_matrix["capabilities"]:
        if item["runtime_actor"] not in role_ids_set:
            raise AssertionError(f"{item['capability_id']} references an unknown runtime actor: {item['runtime_actor']}")
        if item["target_contract_surface"] not in allowed_target_surfaces:
            raise AssertionError(f"{item['capability_id']} points at an unknown contract surface.")
        capability_operations |= set(item["governed_operations"])
        evidence_path = ROOT / item["evidence_artifact"]
        if not evidence_path.exists():
            raise AssertionError(f"{item['capability_id']} evidence artifact is missing: {item['evidence_artifact']}")
        if item["parent_lane_classification"] not in ALLOWED_CAPABILITY_CLASSIFICATIONS:
            raise AssertionError(f"{item['capability_id']} declares an unknown parent_lane_classification.")
        distribution_targeted = distribution_targeted or (
            item["parent_surface_type"] == "distribution_plane"
            and item["target_contract_surface"] == "contracts/library-distribution.yaml"
        )
        observability_targeted = observability_targeted or (
            item["parent_surface_type"] == "observability_plane"
            and item["target_contract_surface"] == "contracts/observability-ingest.yaml"
        )
    require_subset("Capability governed operations", REQUIRED_PEER_MESH_OPERATIONS, capability_operations)
    if not distribution_targeted:
        raise AssertionError("Capability matrix must route at least one distribution-plane row through the library-distribution contract.")
    if not observability_targeted:
        raise AssertionError("Capability matrix must route at least one observability-plane row through the observability-ingest contract.")
    details["capability_ids"] = sorted(capability_ids)
    details["capability_surface_types"] = sorted(set(capability_surface_types))

    peer_message = loaded_contracts["contracts/peer-message.yaml"]
    require_subset("Peer message required fields", REQUIRED_MESSAGE_FIELDS, set(peer_message["envelope"]["required_fields"]))
    require_subset("Peer message correlation keys", {"message_id", "correlation_id", "scenario_id"}, set(peer_message["correlation"]["required_keys"]))
    require_subset("Peer message completion tokens", REQUIRED_COMPLETION_TOKENS, set(peer_message["completion"]["required_tokens"]))
    require_subset(
        "Peer message terminal response fields",
        REQUIRED_MESSAGE_TERMINAL_FIELDS,
        set(peer_message["completion"]["terminal_response_required_fields"]),
    )
    message_operations = (
        set(peer_message["operations"]["discovery_operations"])
        | set(peer_message["operations"]["command_operations"])
        | set(peer_message["operations"]["prompt_operations"])
        | set(peer_message["operations"]["await_operations"])
    )
    require_subset("Peer message operations", REQUIRED_PEER_MESH_OPERATIONS, message_operations)
    require_subset(
        "Peer message retryable operations",
        {"send_command", "send_prompt", "await_response"},
        set(peer_message["retry_boundary"]["retryable_operations"]),
    )
    if peer_message["retry_boundary"]["escalation_role"] not in role_ids_set:
        raise AssertionError("Peer message escalation_role must reference a known runtime role.")

    peer_lifecycle = loaded_contracts["contracts/peer-lifecycle.yaml"]
    state_ids = {state["state_id"] for state in peer_lifecycle["states"]}
    require_subset("Peer lifecycle states", REQUIRED_LIFECYCLE_STATES, state_ids)
    completion_boundary = peer_lifecycle["completion_boundary"]
    require_subset("Peer lifecycle events", REQUIRED_LIFECYCLE_EVENTS, set(completion_boundary["required_event_types"]))
    require_subset("Peer lifecycle terminal states", {"completed", "blocked"}, set(completion_boundary["terminal_states"]))
    require_subset(
        "Peer lifecycle verification role classes",
        {"verification_guard"},
        set(completion_boundary["verification_role_classes"]),
    )
    if not set(completion_boundary["terminal_states"]).issubset(state_ids):
        raise AssertionError("Peer lifecycle terminal states must exist in the lifecycle state registry.")
    if not set(completion_boundary["retryable_states"]).issubset(state_ids):
        raise AssertionError("Peer lifecycle retryable states must exist in the lifecycle state registry.")
    for transition in peer_lifecycle["transitions"]:
        if transition["from_state"] not in state_ids or transition["to_state"] not in state_ids:
            raise AssertionError("Peer lifecycle transitions must reference declared states.")

    observability = loaded_contracts["contracts/observability-event.yaml"]
    require_subset(
        "Observability event types",
        REQUIRED_OBSERVABILITY_EVENTS,
        set(observability["event_taxonomy"]["required_event_types"]),
    )
    require_subset(
        "Observability governed operations",
        REQUIRED_PEER_MESH_OPERATIONS,
        set(observability["operation_event_requirements"]["required_operations"]),
    )
    require_subset(
        "Observability correlation keys",
        {"message_id", "correlation_id", "scenario_id"},
        set(observability["ingestion"]["correlation_keys"]),
    )
    if observability["ingestion"]["ingest_contract"] != "contracts/observability-ingest.yaml":
        raise AssertionError("Observability events must point at the decoupled observability-ingest contract.")
    require_subset(
        "Observability swimlane role classes",
        REQUIRED_ROLE_CLASSES,
        set(observability["swimlanes"]["required_role_classes"]),
    )

    observability_ingest = loaded_contracts["contracts/observability-ingest.yaml"]
    if not observability_ingest["ingest_plane"]["endpoint_path"].startswith("/"):
        raise AssertionError("Observability ingest endpoint_path must stay rooted.")
    require_subset(
        "Observability ingest session markers",
        REQUIRED_INGEST_SESSION_MARKERS,
        set(observability_ingest["session_visibility"]["required_session_markers"]),
    )
    require_subset(
        "Observability ingest source contracts",
        {"contracts/peer-lifecycle.yaml", "contracts/observability-event.yaml"},
        set(observability_ingest["session_visibility"]["source_contracts"]),
    )
    require_subset(
        "Observability ingest correlation fields",
        REQUIRED_INGEST_CORRELATION_FIELDS,
        set(observability_ingest["correlation_visibility"]["required_correlation_fields"]),
    )
    require_subset(
        "Observability ingest swimlane roles",
        set(role_ids),
        set(observability_ingest["swimlane_visibility"]["required_roles"]),
    )
    require_subset(
        "Observability ingest swimlane dimensions",
        REQUIRED_SWIMLANE_DIMENSIONS,
        set(observability_ingest["swimlane_visibility"]["required_dimensions"]),
    )

    policy = loaded_contracts["contracts/policy-decision.yaml"]
    require_subset("Policy decision outcomes", REQUIRED_POLICY_OUTCOMES, set(policy["decision_outcomes"]["required_outcomes"]))
    require_subset(
        "Policy record fields",
        REQUIRED_POLICY_RECORD_FIELDS,
        set(policy["decision_records"]["required_fields"]),
    )
    require_subset(
        "Policy governed operations",
        {"send_prompt", "send_command"},
        set(policy["decision_records"]["governed_operations"]),
    )
    if policy["escalation"]["ask_routes_to"] not in role_ids_set:
        raise AssertionError("Policy ask_routes_to must reference a known runtime role.")

    library_distribution = loaded_contracts["contracts/library-distribution.yaml"]
    require_subset(
        "Library distribution unit types",
        REQUIRED_DISTRIBUTION_UNIT_TYPES,
        set(library_distribution["typed_units"]["required_unit_types"]),
    )
    reference_prefixes = {
        item["unit_type"]: item["reference_prefix"]
        for item in library_distribution["typed_units"]["reference_prefixes"]
    }
    missing_prefixes = sorted(
        unit_type
        for unit_type in REQUIRED_DISTRIBUTION_UNIT_TYPES
        if reference_prefixes.get(unit_type) != f"{unit_type}:"
    )
    if missing_prefixes:
        raise AssertionError(f"Library distribution must provide typed reference prefixes for: {missing_prefixes}")
    require_subset(
        "Library distribution source contracts",
        {
            "contracts/agent-role-contract.yaml",
            "contracts/hook-manifest.yaml",
            "contracts/benchmark-emission.yaml",
        },
        set(library_distribution["typed_units"]["source_contracts"]),
    )
    require_subset(
        "Library distribution propagation triggers",
        REQUIRED_DISTRIBUTION_TRIGGERS,
        set(library_distribution["propagation"]["propagation_triggers"]),
    )
    require_subset(
        "Library distribution runtime modes",
        REQUIRED_RUNTIME_MODES,
        set(library_distribution["propagation"]["runtime_modes"]),
    )
    require_subset(
        "Library distribution governance surfaces",
        {
            "contracts/agent-role-contract.yaml",
            "contracts/hook-manifest.yaml",
            "contracts/benchmark-emission.yaml",
        },
        set(library_distribution["governance"]["required_contract_surfaces"]),
    )
    details["distribution_unit_types"] = sorted(set(library_distribution["typed_units"]["required_unit_types"]))

    benchmark_emission = loaded_contracts["contracts/benchmark-emission.yaml"]
    require_subset(
        "Benchmark emission artifacts",
        REQUIRED_BENCHMARK_ARTIFACTS,
        set(benchmark_emission["emission_plane"]["emitted_artifacts"]),
    )
    require_subset(
        "Benchmark tuple fields",
        REQUIRED_BENCHMARK_TUPLE_FIELDS,
        set(benchmark_emission["benchmark_tuple"]["required_fields"]),
    )
    require_subset(
        "Benchmark comparison fields",
        REQUIRED_BENCHMARK_COMPARISON_FIELDS,
        set(benchmark_emission["benchmark_tuple"]["comparison_fields"]),
    )
    require_subset(
        "Benchmark required groups",
        REQUIRED_BENCHMARK_GROUPS,
        set(benchmark_emission["required_groups"]["minimum_groups"]),
    )
    require_subset(
        "Benchmark regression signal fields",
        REQUIRED_BENCHMARK_COMPARISON_FIELDS,
        set(benchmark_emission["regression_policy"]["regression_signal_fields"]),
    )
    details["benchmark_groups"] = sorted(set(benchmark_emission["required_groups"]["minimum_groups"]))
    details["ingest_session_markers"] = sorted(set(observability_ingest["session_visibility"]["required_session_markers"]))

    runtime = loaded_contracts["contracts/peer-mesh-runtime.yaml"]
    mode_ids = [mode["mode_id"] for mode in runtime["runtime_modes"]]
    if len(mode_ids) != len(set(mode_ids)):
        raise AssertionError("Peer mesh runtime mode IDs must stay unique.")
    require_subset("Peer mesh runtime modes", REQUIRED_RUNTIME_MODES, set(mode_ids))
    for mode in runtime["runtime_modes"]:
        require_subset(
            f"Peer mesh runtime operations for {mode['mode_id']}",
            REQUIRED_PEER_MESH_OPERATIONS,
            set(mode["supports_operations"]),
        )
        require_subset(
            f"Peer mesh runtime actor roles for {mode['mode_id']}",
            set(role_ids),
            set(mode["actor_roles"]),
        )
        require_subset(
            f"Peer mesh runtime actor role classes for {mode['mode_id']}",
            REQUIRED_ROLE_CLASSES,
            set(mode["actor_role_classes"]),
        )
    require_subset("Peer mesh runtime actors", set(role_ids), set(runtime["actors"]["required_roles"]))
    require_subset(
        "Peer mesh runtime actor classes",
        REQUIRED_ROLE_CLASSES,
        set(runtime["actors"]["required_role_classes"]),
    )
    require_subset(
        "Peer mesh runtime completion tokens",
        REQUIRED_COMPLETION_TOKENS,
        set(runtime["completion_boundary"]["required_completion_tokens"]),
    )
    if runtime["completion_boundary"]["benchmark_contract"] != "contracts/benchmark-emission.yaml":
        raise AssertionError("Peer mesh runtime must point at the benchmark-emission contract.")
    if runtime["actors"]["prod_boundary_role"] not in role_ids_set:
        raise AssertionError("Peer mesh runtime prod_boundary_role must reference a known runtime role.")
    if runtime["actors"]["verification_role"] not in role_ids_set:
        raise AssertionError("Peer mesh runtime verification_role must reference a known runtime role.")
    details["runtime_modes"] = sorted(mode_ids)

    for role in role_contract["roles"]:
        unknown_hooks = sorted(set(role["hook_refs"]) - hook_ids_set)
        if unknown_hooks:
            raise AssertionError(f"{role['role_id']} references unknown hook_refs: {unknown_hooks}")
        unknown_handoffs = sorted(set(role["handoff_targets"]) - role_ids_set)
        if unknown_handoffs:
            raise AssertionError(f"{role['role_id']} references unknown handoff targets: {unknown_handoffs}")
        unknown_modes = sorted(set(role["runtime_modes"]) - set(mode_ids))
        if unknown_modes:
            raise AssertionError(f"{role['role_id']} references unknown runtime modes: {unknown_modes}")
        unknown_operations = sorted(set(role["message_operations"]) - REQUIRED_PEER_MESH_OPERATIONS)
        if unknown_operations:
            raise AssertionError(f"{role['role_id']} references unknown message operations: {unknown_operations}")

    return details


def main() -> int:
    checks = []

    scaffold_missing = [name for name in REQUIRED_SCAFFOLD if not (ROOT / name).exists()]
    checks.append(
        {
            "name": "required_scaffold_files",
            "status": "pass" if not scaffold_missing else "fail",
            "details": {"missing": scaffold_missing},
        }
    )

    prompt_missing = [name for name in REQUIRED_PROMPT_CONTRACT if not (ROOT / name).exists()]
    checks.append(
        {
            "name": "required_prompt_contract_files",
            "status": "pass" if not prompt_missing else "fail",
            "details": {"missing": prompt_missing},
        }
    )

    dir_missing = [name for name in REQUIRED_DIRECTORIES if not (ROOT / name).exists()]
    checks.append(
        {
            "name": "required_proof_package_dirs",
            "status": "pass" if not dir_missing else "fail",
            "details": {"missing": dir_missing},
        }
    )

    program_missing = [name for name in REQUIRED_PROGRAM_FILES if not (ROOT / name).exists()]
    checks.append(
        {
            "name": "required_program_files",
            "status": "pass" if not program_missing else "fail",
            "details": {"missing": program_missing},
        }
    )

    root_missing = [
        name
        for name in ["library.yaml", "infranodus-phase-tool-map.json", "pixeltable-operational-substrate.md"]
        if not (ROOT / name).exists()
    ]
    checks.append(
        {
            "name": "required_root_authorities",
            "status": "pass" if not root_missing else "fail",
            "details": {"missing": root_missing},
        }
    )

    external_missing = []
    for repo, files in REQUIRED_EXTERNAL_REPOS.items():
        for rel in files:
            path = ROOT / "external" / repo / rel
            if not path.exists():
                external_missing.append(str(path.relative_to(ROOT)))
    checks.append(
        {
            "name": "required_local_upstream_clones",
            "status": "pass" if not external_missing else "fail",
            "details": {"missing": external_missing},
        }
    )

    scaffold_results = []
    front_schema = json.loads((ROOT / "schemas/front-matter.schema.json").read_text())
    bottom_schema = json.loads((ROOT / "schemas/bottom-matter.schema.json").read_text())
    front_validator = Draft202012Validator(front_schema)
    bottom_validator = Draft202012Validator(bottom_schema)
    for name in REQUIRED_SCAFFOLD:
        front, bottom = parse_markdown_contract(ROOT / name)
        front_validator.validate(front)
        bottom_validator.validate(bottom)
        scaffold_results.append({"file": name, "status": "pass"})
    checks.append(
        {
            "name": "scaffold_markdown_contracts",
            "status": "pass",
            "details": scaffold_results,
        }
    )

    checks.append(
        {
            "name": "schema_and_example_validation",
            "status": "pass",
            "details": validate_examples(),
        }
    )

    checks.append(
        {
            "name": "governance_triad_slice",
            "status": "pass",
            "details": validate_governance_triad_slice(),
        }
    )

    checks.append(
        {
            "name": "inbox_front_door_protocol_slice",
            "status": "pass",
            "details": validate_inbox_front_door_slice(),
        }
    )

    checks.append(
        {
            "name": "capability_metrics_contract",
            "status": "pass",
            "details": validate_capability_metrics_contract(),
        }
    )

    checks.append(
        {
            "name": "research_governance_alignment",
            "status": "pass",
            "details": validate_research_governance(),
        }
    )

    consume_source_quality_details = validate_consume_source_quality_outputs()
    checks.append(
        {
            "name": "consume_source_quality_outputs",
            "status": "pass" if not consume_source_quality_details["errors"] else "fail",
            "details": consume_source_quality_details,
        }
    )

    consume_source_quality_report_details = validate_consume_source_quality_report()
    checks.append(
        {
            "name": "consume_source_quality_report",
            "status": "pass" if not consume_source_quality_report_details["errors"] else "fail",
            "details": consume_source_quality_report_details,
        }
    )

    checks.append(
        {
            "name": "subsystem_harness_architecture_slice",
            "status": "pass",
            "details": validate_subsystem_architecture_slice(),
        }
    )

    gap_map_strength_details = validate_gap_map_strength_slice()
    checks.append(
        {
            "name": "gap_map_strength_slice",
            "status": "pass" if not gap_map_strength_details["errors"] else "fail",
            "details": gap_map_strength_details,
        }
    )

    tool_packaging_details = validate_tool_packaging_slice()
    checks.append(
        {
            "name": "tool_packaging_contract_family",
            "status": "pass" if not tool_packaging_details["errors"] else "fail",
            "details": tool_packaging_details,
        }
    )

    subsystem_runner_proof_details = validate_subsystem_runner_proof_slice()
    checks.append(
        {
            "name": "subsystem_runner_proof_family",
            "status": "pass" if not subsystem_runner_proof_details["errors"] else "fail",
            "details": subsystem_runner_proof_details,
        }
    )

    checks.append(
        {
            "name": "tool_health_truth_boundaries",
            "status": "pass",
            "details": validate_tool_health_truth(),
        }
    )

    checks.append(
        {
            "name": "same_host_runtime_activation",
            "status": "pass",
            "details": validate_same_host_runtime_activation(),
        }
    )

    checks.append(
        {
            "name": "parent_native_orchestration_contracts",
            "status": "pass",
            "details": validate_parent_native_contracts(),
        }
    )

    program_front, program_bottom = parse_markdown_contract(ROOT / "program.md")
    front_validator.validate(program_front)
    bottom_validator.validate(program_bottom)
    checks.append(
        {
            "name": "program_markdown_contract",
            "status": "pass",
            "details": [{"file": "program.md", "status": "pass"}],
        }
    )

    iterations_path = ROOT / "runs/iterations.jsonl"
    iteration_rows, iteration_errors = load_jsonl(iterations_path)
    iteration_schema = json.loads((ROOT / "schemas/iteration-record.schema.json").read_text())
    iteration_validator = Draft202012Validator(iteration_schema)
    invalid_rows = []
    for index, row in enumerate(iteration_rows, start=1):
        row_errors = sorted(iteration_validator.iter_errors(row), key=lambda error: list(error.path))
        if row_errors:
            invalid_rows.append({"row": index, "errors": [error.message for error in row_errors]})
    checks.append(
        {
            "name": "iteration_ledger_contract",
            "status": "pass" if not iteration_errors and not invalid_rows else "fail",
            "details": {
                "path": str(iterations_path.relative_to(ROOT)),
                "row_count": len(iteration_rows),
                "parse_errors": iteration_errors,
                "invalid_rows": invalid_rows,
            },
        }
    )

    ratchet_report_path = ROOT / "evaluation/copilot-ratchet-report.json"
    ratchet_schema = json.loads((ROOT / "schemas/copilot-ratchet-report.schema.json").read_text())
    ratchet_check = {
        "name": "copilot_ratchet_report_contract",
        "status": "pass",
        "details": {"status": "missing"},
    }
    if ratchet_report_path.exists():
        report_instance = json.loads(ratchet_report_path.read_text())
        errors = sorted(Draft202012Validator(ratchet_schema).iter_errors(report_instance), key=lambda error: error.path)
        ratchet_check = {
            "name": "copilot_ratchet_report_contract",
            "status": "pass" if not errors else "fail",
            "details": {
                "path": str(ratchet_report_path.relative_to(ROOT)),
                "errors": [error.message for error in errors],
            },
        }
    checks.append(ratchet_check)

    runtime_truth_check = {
        "name": "runtime_truth_reporting_contract",
        "status": "fail",
        "details": {"errors": ["evaluation/copilot-ratchet-report.json is missing."]},
    }
    if ratchet_report_path.exists():
        report_instance = json.loads(ratchet_report_path.read_text())
        details = validate_report_runtime_truth(report_instance, iteration_rows)
        runtime_truth_check = {
            "name": "runtime_truth_reporting_contract",
            "status": "pass" if not details["errors"] else "fail",
            "details": details,
        }
    checks.append(runtime_truth_check)

    overall = "pass" if all(item["status"] == "pass" for item in checks) else "fail"
    report = {
        "report_id": "PARENT-META-VALIDATION-0001",
        "created_at": date.today().isoformat(),
        "scope": "portable_parent_wrapper",
        "overall_status": overall,
        "checks": checks,
    }
    (ROOT / "evaluation/validation-report.json").write_text(json.dumps(report, indent=2) + "\n")

    ratchet_blockers = []
    report_path = ROOT / "evaluation/copilot-ratchet-report.json"
    if iteration_errors or invalid_rows:
        ratchet_blockers.append("Iteration ledger does not satisfy the iteration record contract.")
    if not report_path.exists():
        ratchet_blockers.append("Real copilot-ratchet-report.json is missing.")
    else:
        report_instance = json.loads(report_path.read_text())
        schema_errors = list(Draft202012Validator(ratchet_schema).iter_errors(report_instance))
        if schema_errors:
            ratchet_blockers.append("Real copilot-ratchet-report.json does not satisfy the report schema.")
        runtime_truth_details = validate_report_runtime_truth(report_instance, iteration_rows)
        if runtime_truth_details["errors"]:
            ratchet_blockers.append("Real copilot-ratchet-report.json does not satisfy the runtime-truth reporting contract.")
        if int(report_instance.get("real_non_dry_cycles_executed", 0)) < 2:
            ratchet_blockers.append("Real copilot ratchet executed fewer than 2 non-dry cycles.")

    readiness = {
        "readiness_id": "PARENT-META-PROMOTION-0001",
        "created_at": date.today().isoformat(),
        "scope": "portable_parent_wrapper",
        "status": "pass" if overall == "pass" and not ratchet_blockers else "blocked",
        "blockers": ([] if overall == "pass" else ["Parent wrapper contract validation failed."]) + ratchet_blockers,
        "evidence": [
            "evaluation/validation-report.json",
            "evaluation/copilot-ratchet-report.json",
            "infranodus-phase-tool-map.json",
            "library.yaml",
            "agent-heavy-run-prompt.schema.json",
            "program.md",
            "runs/iterations.jsonl",
            "contracts/research-packet-manifest.yaml",
            "contracts/peer-mesh.yaml",
            "contracts/peer-message.yaml",
            "contracts/peer-lifecycle.yaml",
            "contracts/observability-event.yaml",
            "contracts/policy-decision.yaml",
            "contracts/peer-mesh-runtime.yaml",
            "contracts/agent-role-contract.yaml",
            "contracts/hook-manifest.yaml",
            "contracts/capability-matrix.yaml",
            "contracts/three-agent-topology.yaml",
            "contracts/agent-extension-request.yaml",
            "contracts/subsystem-harness-topology.yaml",
            "contracts/subsystem-registry.yaml",
            "contracts/subsystem-runner-proof-family.yaml",
            "contracts/contract-to-runner-map.yaml",
            "contracts/subsystem-bounded-probe.yaml",
            "contracts/subsystem-observability-handshake.yaml",
            "contracts/tool-packaging-family.yaml",
            "prompts/governed-triad-follow-up-prompt.template.md",
            "schemas/governed-agent-profile.schema.json",
            "schemas/subsystem-harness-topology.schema.json",
            "schemas/subsystem-registry.schema.json",
            "schemas/subsystem-registry-record.schema.json",
            "schemas/subsystem-runner-proof-family.schema.json",
            "schemas/contract-to-runner-map.schema.json",
            "schemas/subsystem-bounded-probe.schema.json",
            "schemas/subsystem-observability-handshake.schema.json",
            "schemas/subsystem-runner-proof-strengthening-report.schema.json",
            "schemas/evidence-strength.schema.json",
            "schemas/operational-feature-matrix.schema.json",
            "schemas/consume-source-quality-strengthening-report.schema.json",
            "schemas/tool-packaging-family.schema.json",
            "schemas/tool-spec.schema.json",
            "schemas/agent-card.schema.json",
            "schemas/tool-task.schema.json",
            "schemas/tool-artifact.schema.json",
            "examples/three-agent-topology.valid.json",
            "examples/agent-extension-request.valid.json",
            "examples/subsystem-harness-topology.valid.json",
            "examples/subsystem-registry.valid.json",
            "examples/subsystem-registry-record.valid.json",
            "examples/subsystem-runner-proof-family.valid.json",
            "examples/contract-to-runner-map.valid.json",
            "examples/subsystem-bounded-probe.valid.json",
            "examples/subsystem-observability-handshake.valid.json",
            "examples/subsystem-runner-proof-strengthening-report.valid.json",
            "examples/evidence-strength.valid.json",
            "examples/operational-feature-matrix.valid.json",
            "examples/consume-source-quality-strengthening-report.valid.json",
            "examples/tool-packaging-family.valid.json",
            "examples/tool-spec.valid.json",
            "examples/agent-card.valid.json",
            "examples/tool-task.valid.json",
            "examples/tool-artifact.valid.json",
            "source/subsystems/registry.json",
            "source/subsystems/intake-etl.md",
            "source/subsystems/research-harvest.md",
            "source/subsystems/semantic-cartography.md",
            "source/subsystems/wrapper-synthesizer.md",
            "source/subsystem-runner-proof-family.md",
            "source/tool-packaging-contract-family.md",
            "source/consume-source-quality-pipeline.md",
            "evaluation/subsystem-runner-proof-strengthening-report.json",
            "evaluation/subsystem-runner-proof-strengthening-report.md",
            "evaluation/tool-health/peer-mesh-local.json",
            "evaluation/tool-health/peer-mesh-local.log",
            "evaluation/tool-health/peer-mesh-local-events.jsonl",
            "evaluation/tool-health/peer-mesh-local-benchmarks.json",
            "evaluation/research/compiled/capability-harvest.json",
            "evaluation/research/compiled/feature-matrix.json",
            "evaluation/research/compiled/gap-placement-map.json",
            "evaluation/research/compiled/source-index.json",
            "evaluation/research/compiled/operational-feature-matrix.json",
            "evaluation/consume-source-quality-strengthening-report.json",
            "evaluation/consume-source-quality-strengthening-report.md",
            "outbox/2026-05-22-operational-feature-matrix.handoff.md",
            "outbox/2026-05-22-capability-matrix-extension.handoff.md",
            "outbox/2026-05-22-consume-folder-extraction-map.handoff.md",
            "outbox/2026-05-22-compiled-output-ingestion-map.handoff.md",
            "prompts/PROMPT-20260522-CONSUME-SOURCE-QUALITY.yaml",
            "prompts/PROMPT-20260522-CONSUME-SOURCE-QUALITY.md",
            "prompts/PROMPT-20260522-CSQ3.yaml",
            "prompts/PROMPT-20260522-CSQ3.md",
        ]
        + sorted(INBOX_PROTOCOL_CONTRACTS.keys())
        + [schema for schema in INBOX_PROTOCOL_CONTRACTS.values()]
        + [item[0] for item in INBOX_PROTOCOL_VALID_EXAMPLES]
        + sorted(FRONT_DOOR_LIFECYCLE_CONTRACTS.keys())
        + [schema for schema in FRONT_DOOR_LIFECYCLE_CONTRACTS.values()]
        + [item[0] for item in FRONT_DOOR_LIFECYCLE_VALID_EXAMPLES],
    }
    (ROOT / "promotion/readiness.json").write_text(json.dumps(readiness, indent=2) + "\n")
    print(json.dumps(report, indent=2))
    return 0 if overall == "pass" else 1


if __name__ == "__main__":
    raise SystemExit(main())
