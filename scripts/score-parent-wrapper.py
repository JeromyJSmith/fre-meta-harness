from __future__ import annotations

import argparse
import json
from datetime import date
from pathlib import Path

from jsonschema import Draft202012Validator
import yaml


ROOT = Path(__file__).resolve().parents[1]
EDITABLE_FILES = {
    "GOAL.md",
    "domain_spec.md",
    "program.md",
    "library.yaml",
    "agentics-library.md",
    "README.md",
    "AGENTS.md",
    "CLAUDE.md",
    "MEMORY.md",
    "GOLDENPATH.md",
}
EDITABLE_PREFIXES = (
    "source/",
    "schemas/",
    "examples/",
    "expected-failures/",
    "tests/",
    "evaluation/",
    "promotion/",
    "prompts/",
    "runs/",
    "scripts/",
)
DOC_ONLY_FILES = {
    "GOAL.md",
    "domain_spec.md",
    "program.md",
    "library.yaml",
    "agentics-library.md",
    "README.md",
    "AGENTS.md",
    "CLAUDE.md",
    "MEMORY.md",
    "GOLDENPATH.md",
    "source/README.md",
}
DOC_ONLY_PREFIXES = ("docs/",)
SUBSTANTIVE_PREFIXES = (
    "contracts/",
    "schemas/",
    "examples/",
    "expected-failures/",
    "tests/",
    "scripts/",
    "evaluation/tool-health/",
)
REQUIRED_ARTIFACTS = [
    "evaluation/validation-report.json",
    "evaluation/metrics-latest.json",
    "promotion/readiness.json",
    "runs/iterations.jsonl",
]
TOOL_HEALTH_PATH = "evaluation/tool-health/status.json"
TOOL_STATUS_WEIGHTS = {
    "pass": 1.0,
    "bounded_pass": 0.75,
    "dry_pass": 0.5,
    "bounded": 0.35,
    "blocked": 0.25,
    "warn": 0.25,
    "fail": 0.0,
    "missing": 0.0,
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
PARENT_NATIVE_VALID_EXAMPLES = {
    "examples/peer-mesh.valid.json": "schemas/peer-mesh.schema.json",
    "examples/peer-message.valid.json": "schemas/peer-message.schema.json",
    "examples/peer-lifecycle.valid.json": "schemas/peer-lifecycle.schema.json",
    "examples/observability-event.valid.json": "schemas/observability-event.schema.json",
    "examples/observability-ingest.valid.json": "schemas/observability-ingest.schema.json",
    "examples/policy-decision.valid.json": "schemas/policy-decision.schema.json",
    "examples/library-distribution.valid.json": "schemas/library-distribution.schema.json",
    "examples/benchmark-emission.valid.json": "schemas/benchmark-emission.schema.json",
    "examples/peer-mesh-runtime.valid.json": "schemas/peer-mesh-runtime.schema.json",
    "examples/agent-role-contract.valid.json": "schemas/agent-role-contract.schema.json",
    "examples/hook-manifest.valid.json": "schemas/hook-manifest.schema.json",
    "examples/capability-matrix.valid.json": "schemas/capability-matrix.schema.json",
}
INBOX_PROTOCOL_CONTRACTS = {
    "contracts/inbox-packet.yaml": "schemas/inbox-packet.schema.json",
    "contracts/inbox-routing-decision.yaml": "schemas/inbox-routing-decision.schema.json",
    "contracts/delegation-bundle.yaml": "schemas/delegation-bundle.schema.json",
}
FRONT_DOOR_LIFECYCLE_CONTRACTS = {
    "contracts/front-door-runtime-topology.yaml": "schemas/front-door-runtime-topology.schema.json",
    "contracts/recursive-documentation-bundle.yaml": "schemas/recursive-documentation-bundle.schema.json",
}
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
GOVERNED_MARKDOWN_TEMPLATE_GATES = {
    "triad_handoff_consumed",
    "structured_prompt_emitted",
    "markdown_companion_emitted",
}
INBOX_ACTIVATION_CHECK_TOKENS = {
    "inbox",
    "front_door",
    "filesystem_router",
    "routing",
    "confirmed_spec",
}
REQUIRED_PARENT_CAPABILITIES = {
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
REQUIRED_PARENT_ROLES = {"mesh_bootstrap", "prod_boundary", "execution_driver", "verification_guard"}
REQUIRED_PARENT_HOOKS = {
    "session_bootstrap",
    "membership_refresh",
    "message_guard",
    "completion_guard",
}
REQUIRED_PARENT_RUNTIME_MODES = {"same_host", "cross_device"}
REQUIRED_PARENT_OPERATIONS = {"list_agents", "send_command", "send_prompt", "await_response"}
REQUIRED_COMPLETION_TOKENS = {"done", "failed", "needs-human"}
REQUIRED_INGEST_SESSION_MARKERS = {"session_start", "session_end"}
REQUIRED_OBSERVABILITY_EVENTS = {
    "peer_session_started",
    "peer_session_ended",
    "peer_joined",
    "peer_message_sent",
    "peer_message_received",
    "peer_response_completed",
    "policy_decision_emitted",
}
REQUIRED_DISTRIBUTION_UNIT_TYPES = {
    "skill",
    "prompt",
    "agent",
    "policy",
    "validator",
    "benchmark_recipe",
}
REQUIRED_BENCHMARK_GROUPS = {
    "peer_mesh_regression",
    "observability_ingest",
    "library_distribution",
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
ALLOWED_CAPABILITY_CLASSIFICATIONS = {
    "core",
    "gated",
    "deployment_specific",
    "reference",
    "blocked_with_exact_dependency",
}
REQUIRED_RESEARCH_CORE_CAPABILITIES = {
    "pi-vs-claude-code",
    "the-library",
    "claude-code-hooks-mastery",
    "claude-code-hooks-multi-agent-observability",
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


def require_subset_score(required: set[str], actual: set[str]) -> float:
    if not required:
        return 1.0
    return len(required & actual) / len(required)


def load_json(path: Path) -> dict | None:
    if not path.exists():
        return None
    return json.loads(path.read_text())


def parse_markdown_contract(path: Path) -> tuple[dict, dict]:
    text = path.read_text()
    if not text.startswith("---\n"):
        raise ValueError(f"{path.name}: missing front matter start")
    _, rest = text.split("---\n", 1)
    front_raw, body = rest.split("\n---\n", 1)
    if "\n---bottom-matter---\n" not in body:
        raise ValueError(f"{path.name}: missing bottom matter marker")
    _, bottom_raw = body.split("\n---bottom-matter---\n", 1)
    return yaml.safe_load(front_raw) or {}, yaml.safe_load(bottom_raw) or {}


def normalize_identifier(value: str) -> str:
    return "".join(char if char.isalnum() else "_" for char in value.lower()).strip("_")


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


def normalize_tool_status(status: str | None) -> str:
    if not status:
        return "missing"
    normalized = status.lower().strip().replace("-", "_")
    if normalized in TOOL_STATUS_WEIGHTS:
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
    return "warn"


def is_pinned_github_blob(ref: str) -> bool:
    if not ref.startswith("https://github.com/") or "/blob/" not in ref:
        return False
    _, blob_tail = ref.split("/blob/", 1)
    commit, *_ = blob_tail.split("/", 1)
    return len(commit) == 40 and all(char in "0123456789abcdef" for char in commit)


def load_iterations() -> tuple[list[dict], list[str]]:
    path = ROOT / "runs/iterations.jsonl"
    if not path.exists():
        return [], []
    rows = []
    errors = []
    validator = Draft202012Validator(load_iteration_schema())
    for line_number, line in enumerate(path.read_text().splitlines(), start=1):
        if not line.strip():
            continue
        try:
            row = json.loads(line)
        except json.JSONDecodeError as exc:
            errors.append(f"line {line_number}: {exc.msg}")
            continue
        row_errors = [error.message for error in validator.iter_errors(row)]
        if row_errors:
            errors.append(f"line {line_number}: {' | '.join(row_errors)}")
            continue
        rows.append(row)
    return rows, errors


def load_report_schema() -> dict:
    return json.loads((ROOT / "schemas/copilot-ratchet-report.schema.json").read_text())


def load_iteration_schema() -> dict:
    return json.loads((ROOT / "schemas/iteration-record.schema.json").read_text())


def validate_report() -> tuple[dict | None, list[str]]:
    report = load_json(ROOT / "evaluation/copilot-ratchet-report.json")
    if not report:
        return None, ["missing"]
    schema = load_report_schema()
    errors = [error.message for error in Draft202012Validator(schema).iter_errors(report)]
    return report, errors


def is_mutable_path(path: str) -> bool:
    normalized = path.lstrip("./")
    return normalized in EDITABLE_FILES or any(normalized.startswith(prefix) for prefix in EDITABLE_PREFIXES)


def is_doc_only_path(path: str) -> bool:
    normalized = path.lstrip("./")
    return normalized in DOC_ONLY_FILES or any(normalized.startswith(prefix) for prefix in DOC_ONLY_PREFIXES)


def is_substantive_path(path: str) -> bool:
    normalized = path.lstrip("./")
    if is_doc_only_path(normalized):
        return False
    if normalized.startswith(("evaluation/", "promotion/", "runs/")) and not normalized.startswith("evaluation/tool-health/"):
        return False
    if normalized.startswith(SUBSTANTIVE_PREFIXES):
        return True
    if normalized.startswith("source/") and normalized != "source/README.md":
        return True
    return False


def row_has_substantive_change(row: dict) -> bool:
    return any(is_substantive_path(path) for path in row.get("changed_files", []))


def load_tool_health() -> dict | None:
    return load_json(ROOT / TOOL_HEALTH_PATH)


def validate_surface_triad(
    contract_rel: str,
    schema_rel: str,
    example_rel: str,
) -> tuple[dict | None, dict | None, dict | None, list[str]]:
    contract_path = ROOT / contract_rel
    schema_path = ROOT / schema_rel
    example_path = ROOT / example_rel
    errors: list[str] = []
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
        contract = yaml.safe_load(contract_path.read_text())
        Draft202012Validator(schema).validate(contract)
        example = json.loads(example_path.read_text())
        Draft202012Validator(schema).validate(example)
    except Exception as exc:  # noqa: BLE001
        errors.append(f"{contract_rel}:{exc}")
    return contract, schema, example, errors


def parent_native_surface_refresh() -> tuple[float, dict]:
    contracts_validated = 0
    examples_validated = 0
    errors = []
    role_ids = set()
    hook_ids = set()
    hook_classes = set()
    capability_surface_types = set()
    capability_operation_ids = set()
    runtime_modes = set()
    operation_ids = set()
    ingest_session_markers = set()
    distribution_unit_types = set()
    benchmark_groups = set()

    for contract_rel, schema_rel in PARENT_NATIVE_CONTRACTS.items():
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
        contracts_validated += 1
        if contract_rel == "contracts/agent-role-contract.yaml":
            role_ids = {role["role_class"] for role in contract["roles"]}
        elif contract_rel == "contracts/hook-manifest.yaml":
            hook_ids = {hook["hook_id"] for hook in contract["hooks"]}
            hook_classes = {hook["hook_class"] for hook in contract["hooks"]}
        elif contract_rel == "contracts/capability-matrix.yaml":
            capability_surface_types = {item["parent_surface_type"] for item in contract["capabilities"]}
            capability_operation_ids = {
                operation
                for item in contract["capabilities"]
                for operation in item["governed_operations"]
            }
        elif contract_rel == "contracts/peer-mesh-runtime.yaml":
            runtime_modes = {mode["mode_id"] for mode in contract["runtime_modes"]}
        elif contract_rel == "contracts/peer-mesh.yaml":
            operation_ids = set(contract["protocol"]["required_operations"])
        elif contract_rel == "contracts/observability-ingest.yaml":
            ingest_session_markers = set(contract["session_visibility"]["required_session_markers"])
        elif contract_rel == "contracts/library-distribution.yaml":
            distribution_unit_types = set(contract["typed_units"]["required_unit_types"])
        elif contract_rel == "contracts/benchmark-emission.yaml":
            benchmark_groups = set(contract["required_groups"]["minimum_groups"])

    for example_rel, schema_rel in PARENT_NATIVE_VALID_EXAMPLES.items():
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
        examples_validated += 1

    score = 0.0
    if contracts_validated == len(PARENT_NATIVE_CONTRACTS):
        score += 2.5
    if examples_validated == len(PARENT_NATIVE_VALID_EXAMPLES):
        score += 1.25
    subset_score = (
        require_subset_score(REQUIRED_PARENT_ROLES, role_ids)
        + require_subset_score(REQUIRED_PARENT_HOOKS, hook_classes)
        + require_subset_score(REQUIRED_PARENT_CAPABILITIES, capability_surface_types)
        + require_subset_score(REQUIRED_PARENT_RUNTIME_MODES, runtime_modes)
        + require_subset_score(REQUIRED_PARENT_OPERATIONS, operation_ids)
        + require_subset_score(REQUIRED_PARENT_OPERATIONS, capability_operation_ids)
        + require_subset_score(REQUIRED_INGEST_SESSION_MARKERS, ingest_session_markers)
        + require_subset_score(REQUIRED_DISTRIBUTION_UNIT_TYPES, distribution_unit_types)
        + require_subset_score(REQUIRED_BENCHMARK_GROUPS, benchmark_groups)
    ) / 9
    score += round(0.75 * subset_score, 2)

    return score, {
        "contracts_validated": contracts_validated,
        "examples_validated": examples_validated,
        "role_classes": sorted(role_ids),
        "hook_ids": sorted(hook_ids),
        "hook_classes": sorted(hook_classes),
        "capability_surface_types": sorted(capability_surface_types),
        "capability_operation_ids": sorted(capability_operation_ids),
        "runtime_modes": sorted(runtime_modes),
        "operation_ids": sorted(operation_ids),
        "ingest_session_markers": sorted(ingest_session_markers),
        "distribution_unit_types": sorted(distribution_unit_types),
        "benchmark_groups": sorted(benchmark_groups),
        "errors": errors,
    }


def research_governance_refresh() -> tuple[float, dict]:
    errors = []
    score = 0.0

    try:
        contract_schema = json.loads((ROOT / RESEARCH_SCHEMA_PATHS["research_manifest_contract"]).read_text())
        contract = yaml.safe_load((ROOT / "contracts/research-packet-manifest.yaml").read_text())
        Draft202012Validator(contract_schema).validate(contract)
        score += 0.5
    except Exception as exc:  # noqa: BLE001
        return 0.0, {"errors": [f"contract:{exc}"]}

    try:
        compiled_schemas = {
            key: json.loads((ROOT / rel).read_text())
            for key, rel in RESEARCH_SCHEMA_PATHS.items()
            if key != "research_manifest_contract"
        }
        feature_matrix = json.loads((ROOT / contract["authority"]["compiled_outputs"]["feature_matrix"]).read_text())
        capability_harvest = json.loads((ROOT / contract["authority"]["compiled_outputs"]["capability_harvest"]).read_text())
        gap_map = json.loads((ROOT / contract["authority"]["compiled_outputs"]["gap_placement_map"]).read_text())
        source_index = json.loads((ROOT / contract["authority"]["compiled_outputs"]["source_index"]).read_text())
        Draft202012Validator(compiled_schemas["compiled_feature_matrix"]).validate(feature_matrix)
        Draft202012Validator(compiled_schemas["compiled_capability_harvest"]).validate(capability_harvest)
        Draft202012Validator(compiled_schemas["gap_placement_map"]).validate(gap_map)
        Draft202012Validator(compiled_schemas["source_index"]).validate(source_index)
        score += 1.0
    except Exception as exc:  # noqa: BLE001
        return 0.0, {"errors": [f"compiled:{exc}"]}

    try:
        harvest_manifest = json.loads((ROOT / "evaluation/research/harvest-manifest.json").read_text())
        manifest_paths = (
            harvest_manifest["repo_packets"]
            + harvest_manifest["topic_packets"]
            + harvest_manifest["compiled_outputs"]
        )
        missing_paths = [path for path in manifest_paths if not (ROOT / path).exists()]
        if missing_paths:
            raise AssertionError(f"missing manifest paths: {missing_paths}")

        capability_matrix = yaml.safe_load((ROOT / "contracts/capability-matrix.yaml").read_text())
        matrix_rows = capability_matrix["capabilities"]
        feature_rows = feature_matrix["rows"]
        matrix_by_id = {row["capability_id"]: row for row in matrix_rows}
        feature_by_id = {row["capability_id"]: row for row in feature_rows}
        if set(matrix_by_id) != set(feature_by_id):
            raise AssertionError("capability_matrix_ids_mismatch")
        required_fields = set(contract["alignment"]["required_feature_fields"])
        for capability_id, feature_row in feature_by_id.items():
            matrix_row = matrix_by_id[capability_id]
            for field in required_fields:
                if matrix_row[field] != feature_row[field]:
                    raise AssertionError(f"drift:{capability_id}:{field}")
        score += 1.0
    except Exception as exc:  # noqa: BLE001
        errors.append(f"alignment:{exc}")

    try:
        classifications = (
            [row["parent_lane_classification"] for row in feature_matrix["rows"]]
            + [lane["classification"] for lane in gap_map["lanes"]]
        )
        if any(classification == "optional" for classification in classifications):
            raise AssertionError("optional classification present")
        if not set(classifications).issubset(ALLOWED_CAPABILITY_CLASSIFICATIONS):
            raise AssertionError("classification drift")
        for capability_id in REQUIRED_RESEARCH_CORE_CAPABILITIES:
            if feature_by_id[capability_id]["parent_lane_classification"] != "core":
                raise AssertionError(f"core drift:{capability_id}")
        score += 0.5
    except Exception as exc:  # noqa: BLE001
        errors.append(f"classification:{exc}")

    try:
        repo_packets = [json.loads((ROOT / path).read_text()) for path in harvest_manifest["repo_packets"]]
        github_refs = []
        for packet in repo_packets:
            verified_commit = packet.get("github_verification", {}).get("verified_commit", "")
            if len(verified_commit) != 40 or not all(char in "0123456789abcdef" for char in verified_commit):
                raise AssertionError("unpinned verified_commit")
            for source_ref in packet.get("source_refs", []):
                ref = source_ref["ref"]
                if ref.startswith("https://github.com/"):
                    github_refs.append(ref)
        github_refs.extend(
            source["ref"]
            for source in source_index["sources"]
            if source["ref"].startswith("https://github.com/")
        )
        if not github_refs or any(not is_pinned_github_blob(ref) for ref in github_refs):
            raise AssertionError("unpinned github refs")
        score += 0.5
    except Exception as exc:  # noqa: BLE001
        errors.append(f"pins:{exc}")

    try:
        video_sources = 0
        for source in source_index["sources"]:
            evidence_type = source["evidence_type"]
            if evidence_type in VIDEO_EVIDENCE_STRENGTH_BY_TYPE:
                expected_strength = VIDEO_EVIDENCE_STRENGTH_BY_TYPE[evidence_type]
                if source.get("video_evidence_strength") != expected_strength:
                    raise AssertionError(f"video strength drift:{source['ref']}")
                video_sources += 1
        if video_sources == 0:
            raise AssertionError("no explicit video evidence boundaries")
        score += 0.5
    except Exception as exc:  # noqa: BLE001
        errors.append(f"video:{exc}")

    return round(score, 2), {
        "errors": errors,
        "aligned_capability_count": len(feature_matrix["rows"]),
        "compiled_outputs": list(contract["authority"]["compiled_outputs"].values()),
    }


def same_host_runtime_truth() -> tuple[float, dict]:
    summary_path = ROOT / "evaluation" / "tool-health" / "peer-mesh-local.json"
    events_path = ROOT / "evaluation" / "tool-health" / "peer-mesh-local-events.jsonl"
    benchmarks_path = ROOT / "evaluation" / "tool-health" / "peer-mesh-local-benchmarks.json"
    validation = load_json(ROOT / "evaluation/validation-report.json") or {}
    if not summary_path.exists():
        return 0.0, {"status": "missing", "errors": ["summary missing"]}
    summary = load_json(summary_path) or {}
    errors: list[str] = []
    score = 0.0

    if (
        TOOL_STATUS_WEIGHTS.get(normalize_tool_status(summary.get("status")), 0.0)
        >= TOOL_STATUS_WEIGHTS["bounded_pass"]
        and summary.get("activation_result") == "active"
        and summary.get("runtime_mode") == "same_host"
        and summary.get("capability_id") == "pi-vs-claude-code"
    ):
        score += 1.0
    else:
        errors.append("activation")

    mismatch_ids = {item["mismatch_id"] for item in summary.get("runtime_mismatch_list", [])}
    operations = summary.get("operations", {})
    completion = summary.get("completion_tokens", {})
    if (
        REQUIRED_RUNTIME_MISMATCH_IDS.issubset(mismatch_ids)
        and REQUIRED_RUNTIME_OPERATIONS.issubset(set(operations))
        and REQUIRED_COMPLETION_TOKENS.issubset(set(completion.get("required", [])))
        and REQUIRED_COMPLETION_TOKENS.issubset(set(completion.get("observed", [])))
        and completion.get("enforced") is True
    ):
        score += 1.25
    else:
        errors.append("operations_or_completion")

    events = []
    if events_path.exists():
        for line in events_path.read_text().splitlines():
            if line.strip():
                events.append(json.loads(line))
    event_types = {event["event_type"] for event in events}
    session_markers = {event["session_marker"] for event in events if event.get("session_marker")}
    observability = summary.get("observability", {})
    if (
        REQUIRED_OBSERVABILITY_EVENTS.issubset(event_types)
        and observability.get("event_count") == len(events)
        and REQUIRED_INGEST_SESSION_MARKERS.issubset(session_markers)
    ):
        score += 1.25
    else:
        errors.append("observability")

    benchmarks = load_json(benchmarks_path) if benchmarks_path.exists() else {}
    benchmark_groups = {item["benchmark_group"] for item in benchmarks.get("tuples", [])} if benchmarks else set()
    if REQUIRED_BENCHMARK_GROUPS.issubset(set(benchmarks.get("groups", []))) and REQUIRED_BENCHMARK_GROUPS.issubset(benchmark_groups):
        score += 0.75
    else:
        errors.append("benchmarks")

    truth_boundary = summary.get("truth_boundary", {})
    cross_device_entries = [item for item in truth_boundary.get("blocked_runtime_modes", []) if item.get("mode_id") == "cross_device"]
    follow_on = summary.get("blocked_follow_on_lanes", {})
    follow_on_ok = all(
        follow_on.get(capability_id, {}).get("status") == expected
        and follow_on.get(capability_id, {}).get("expected_status") == expected
        for capability_id, expected in REQUIRED_FOLLOW_ON_LANE_STATUS.items()
    )
    if (
        validation.get("overall_status") == "pass"
        and "same_host" in truth_boundary.get("active_runtime_modes", [])
        and cross_device_entries
        and normalize_tool_status(cross_device_entries[0].get("status")) == "blocked"
        and follow_on_ok
    ):
        score += 0.75
    else:
        errors.append("truth_boundary")

    return round(score, 2), {
        "status": summary.get("status"),
        "errors": errors,
        "event_count": len(events),
        "benchmark_groups": sorted(benchmark_groups),
        "observed_completion_tokens": sorted(set(completion.get("observed", []))),
    }


def inbox_front_door_surface_refresh() -> tuple[float, dict]:
    required_triads = {
        **INBOX_PROTOCOL_CONTRACTS,
        **FRONT_DOOR_LIFECYCLE_CONTRACTS,
    }
    total_triads = len(required_triads)
    present_triads = 0
    validated_triads = 0
    errors: list[str] = []
    inbox_key_unions: list[set[str]] = []
    lifecycle_key_unions: list[set[str]] = []

    for contract_rel, schema_rel in required_triads.items():
        example_rel = {
            "contracts/inbox-routing-decision.yaml": "examples/inbox-routing-decision-contract.valid.json",
            "contracts/delegation-bundle.yaml": "examples/delegation-bundle-contract.valid.json",
            "contracts/front-door-runtime-topology.yaml": "examples/front-door-runtime-topology-contract.valid.json",
            "contracts/recursive-documentation-bundle.yaml": "examples/recursive-documentation-bundle.valid.json",
        }.get(contract_rel, f"examples/{Path(contract_rel).stem}.valid.json")
        if contract_rel == "contracts/inbox-packet.yaml":
            triad_paths = [
                ROOT / contract_rel,
                ROOT / schema_rel,
                ROOT / "examples/governed-inbox-packet.protocol.valid.md",
            ]
            if all(path.exists() for path in triad_paths):
                present_triads += 1
            try:
                contract = yaml.safe_load((ROOT / contract_rel).read_text())
                schema = json.loads((ROOT / schema_rel).read_text())
                Draft202012Validator.check_schema(schema)
                Draft202012Validator(schema).validate(contract)
                front, bottom = parse_markdown_contract(ROOT / "examples/governed-inbox-packet.protocol.valid.md")
                key_union = (
                    collect_normalized_keys(contract)
                    | collect_normalized_keys(schema)
                    | collect_normalized_keys(front)
                    | collect_normalized_keys(bottom)
                )
                validated_triads += 1
                inbox_key_unions.append(key_union)
                continue
            except Exception as exc:  # noqa: BLE001
                errors.append(f"{contract_rel}:{exc}")
                continue
        triad_paths = [ROOT / contract_rel, ROOT / schema_rel, ROOT / example_rel]
        if all(path.exists() for path in triad_paths):
            present_triads += 1
        contract, schema, example, triad_errors = validate_surface_triad(contract_rel, schema_rel, example_rel)
        if triad_errors:
            errors.extend(triad_errors)
            continue
        validated_triads += 1
        key_union = (
            collect_normalized_keys(contract)
            | collect_normalized_keys(schema)
            | collect_normalized_keys(example)
        )
        if contract_rel in INBOX_PROTOCOL_CONTRACTS:
            inbox_key_unions.append(key_union)
        else:
            lifecycle_key_unions.append(key_union)

    score = 0.0
    if total_triads:
        score += round(0.5 * (present_triads / total_triads), 2)
        score += round(0.5 * (validated_triads / total_triads), 2)

    inbox_fields = set().union(*inbox_key_unions) if inbox_key_unions else set()
    lifecycle_fields = set().union(*lifecycle_key_unions) if lifecycle_key_unions else set()
    if inbox_fields:
        missing_packet_fields = INBOX_PACKET_REQUIRED_FIELDS - inbox_fields
        if not missing_packet_fields and INBOX_PACKET_SCOPE_FIELDS & inbox_fields:
            score += 0.35
        else:
            errors.append("inbox_fields_incomplete")
    if lifecycle_fields:
        missing_recursive_fields = RECURSIVE_DOCUMENTATION_FIELDS - lifecycle_fields
        if not missing_recursive_fields:
            score += 0.35
        else:
            errors.append("recursive_documentation_incomplete")

    try:
        heavy_schema = json.loads((ROOT / "agent-heavy-run-prompt.schema.json").read_text())
        heavy_template = yaml.safe_load((ROOT / "agent-heavy-run-prompt.template.yaml").read_text())
        handoff_schema = json.loads((ROOT / "architect-review-handoff-prompt.schema.json").read_text())
        handoff_template = yaml.safe_load((ROOT / "architect-review-handoff-prompt.template.yaml").read_text())
        handoff_example = json.loads((ROOT / "examples/architect-review-handoff-prompt.valid.json").read_text())
        prompt_front, prompt_bottom = parse_markdown_contract(
            ROOT / "prompts/governed-triad-follow-up-prompt.template.md"
        )

        runtime_roles = set(heavy_schema["$defs"]["runtime_role_id"]["enum"])
        packet_types = set(heavy_schema["$defs"]["packet_artifact_type"]["enum"])
        handoff_packet_types = set(handoff_schema["$defs"]["packet_artifact_type"]["enum"])
        existing_runtime_roles = {
            role["role_id"]
            for role in yaml.safe_load((ROOT / "contracts/agent-role-contract.yaml").read_text())["roles"]
        }
        gate_names = {
            item.get("gate")
            for item in prompt_bottom.get("gate_progress", [])
            if isinstance(item, dict) and item.get("gate")
        }
        if (
            runtime_roles == FRONT_DOOR_RUNTIME_ROLES
            and packet_types == INBOX_PACKET_ARTIFACT_TYPES
            and handoff_packet_types == INBOX_PACKET_ARTIFACT_TYPES
            and not (runtime_roles & existing_runtime_roles)
            and "triad_context" in heavy_template
            and "inbox_context" in handoff_template
            and "inbox_context" in handoff_example
            and {
                "upstream_inbox_packet_ref",
                "packet_artifact_type",
                "required_gate_state",
                "required_consumers",
                "bottom_matter_ref",
                "structured_contract_ref",
            }.issubset(collect_normalized_keys(handoff_example["inbox_context"]))
            and handoff_example["inbox_context"].get("packet_artifact_type") in INBOX_PACKET_ARTIFACT_TYPES
            and GOVERNED_MARKDOWN_TEMPLATE_GATES.issubset(gate_names)
            and str(prompt_front.get("machine_truth_source")) == "structured_contract_family"
        ):
            score += 0.55
        else:
            errors.append("prompt_handoff_alignment_incomplete")
    except Exception as exc:  # noqa: BLE001
        errors.append(f"prompt_handoff_alignment:{exc}")

    tool_health = load_tool_health() or {}
    activation_candidates = []
    for check_name, check_details in (tool_health.get("checks") or {}).items():
        normalized = normalize_identifier(check_name)
        if any(token in normalized for token in INBOX_ACTIVATION_CHECK_TOKENS):
            activation_candidates.append((check_name, check_details))

    activation_score = 0.0
    activation_details = []
    for check_name, check_details in activation_candidates:
        status = normalize_tool_status(check_details.get("status"))
        probe = check_details.get("activation_probe") or check_details.get("probe") or {}
        evidence = probe.get("evidence", [])
        command = probe.get("command", "")
        evidence_paths_exist = bool(evidence) and all((ROOT / rel).exists() for rel in evidence)
        if TOOL_STATUS_WEIGHTS.get(status, 0.0) >= TOOL_STATUS_WEIGHTS["bounded"] and evidence_paths_exist and command:
            activation_score = max(activation_score, 0.75)
        elif TOOL_STATUS_WEIGHTS.get(status, 0.0) >= TOOL_STATUS_WEIGHTS["warn"] and evidence_paths_exist:
            activation_score = max(activation_score, 0.35)
        activation_details.append(
            {
                "check": check_name,
                "status": status,
                "has_command": bool(command),
                "evidence_count": len(evidence),
                "evidence_paths_exist": evidence_paths_exist,
            }
        )
    score += activation_score

    return round(score, 2), {
        "required_triads": total_triads,
        "present_triads": present_triads,
        "validated_triads": validated_triads,
        "activation_score": activation_score,
        "activation_candidates": activation_details,
        "errors": errors,
    }


def real_iterations(rows: list[dict]) -> list[dict]:
    return sorted(rows, key=lambda row: int(row["iteration"]))


def consecutive_non_improving_cycles(score_history: list[dict]) -> int:
    count = 0
    for item in reversed(score_history):
        result = item.get("result")
        kept = item.get("kept")
        if result in {"reverted", "rejected"} or kept is False:
            count += 1
        else:
            break
    return count


def artifact_span_seconds(paths: list[str]) -> float | None:
    timestamps = []
    for rel in paths:
        path = ROOT / rel
        if not path.exists():
            return None
        timestamps.append(path.stat().st_mtime)
    if not timestamps:
        return None
    return max(timestamps) - min(timestamps)


def validator_health() -> tuple[float, dict]:
    report = load_json(ROOT / "evaluation/validation-report.json")
    if not report:
        return 0.0, {"status": "missing"}
    status = report.get("overall_status")
    return (40.0 if status == "pass" else 0.0), {"status": status}


def report_completeness() -> tuple[float, dict]:
    report, schema_errors = validate_report()
    rows, parse_errors = load_iterations()
    if not report:
        return 0.0, {"status": "missing"}
    score = 0.0
    runtime_truth = report.get("runtime_truth", {})
    score_saturation = report.get("score_saturation", {})
    if not schema_errors:
        score += 10.0
    required_top_level = [
        "status",
        "metric_decision",
        "metric_reason",
        "metric_review",
        "real_non_dry_cycles_executed",
        "stop_reason",
        "stop_evidence",
        "score_history",
        "runtime_truth",
        "score_saturation",
        "files_changed",
        "artifacts",
        "iteration_ledger_entries_appended",
    ]
    present = sum(1 for key in required_top_level if key in report)
    score += round(6.0 * present / len(required_top_level), 2)
    history = report.get("score_history", [])
    detailed_rows = sum(
        1
        for item in history
        if {
            "cycle",
            "before_total_score",
            "after_total_score",
            "before_outcome_score",
            "after_outcome_score",
            "before_instrument_score",
            "after_instrument_score",
            "changed_files",
            "kept",
            "summary",
        }.issubset(item.keys())
    )
    score += round(4.0 * (detailed_rows / len(history)), 2) if history else 0.0
    ledger_aligned = len(rows) == int(report.get("real_non_dry_cycles_executed", 0)) == len(history)
    runtime_truth_fields = {
        "truth_level",
        "runtime_modes_blocked",
        "activation_artifacts",
        "observability_artifacts",
        "tool_health_evidence",
        "completion_tokens_required",
        "completion_tokens_observed",
        "policy_outcomes_observed",
        "mismatch_list",
        "blocked_lanes",
        "command_evidence",
        "freshness",
    }
    runtime_truth_score = 0.0
    if runtime_truth.get("truth_level") in ALLOWED_RUNTIME_TRUTH_LEVELS:
        runtime_truth_score += 2.0
    if runtime_truth_fields.issubset(runtime_truth.keys()):
        runtime_truth_score += 2.0
    command_evidence = runtime_truth.get("command_evidence", {})
    if {
        "activation_commands",
        "validation_commands",
        "tool_health_commands",
    }.issubset(command_evidence.keys()):
        runtime_truth_score += 1.0
    freshness = runtime_truth.get("freshness", {})
    freshness_paths = {item.get("path") for item in freshness.get("artifact_records", [])}
    required_freshness_paths = {
        "evaluation/copilot-ratchet-report.json",
        "evaluation/validation-report.json",
        "evaluation/metrics-latest.json",
        "promotion/readiness.json",
        "runs/iterations.jsonl",
    }
    if required_freshness_paths.issubset(freshness_paths):
        runtime_truth_score += 1.0

    saturation_fields = {
        "baseline_total_score",
        "final_total_score",
        "baseline_outcome_score",
        "final_outcome_score",
        "baseline_instrument_score",
        "final_instrument_score",
        "score_changed",
        "new_truth_added",
        "why_this_slice_counts",
    }
    saturation_score = 0.0
    if saturation_fields.issubset(score_saturation.keys()):
        saturation_score += 2.0
    if (
        score_saturation.get("baseline_total_score") == score_saturation.get("final_total_score")
        and bool(score_saturation.get("flat_score_explanation"))
    ):
        saturation_score += 2.0
    elif score_saturation.get("score_changed") is True:
        saturation_score += 2.0

    score += runtime_truth_score + saturation_score
    return round(score, 2), {
        "schema_errors": schema_errors,
        "history_rows": len(history),
        "detailed_rows": detailed_rows,
        "ledger_rows": len(rows),
        "ledger_aligned": ledger_aligned,
        "runtime_truth_score": runtime_truth_score,
        "score_saturation_score": saturation_score,
        "parse_errors": parse_errors,
    }


def metric_decision_truth() -> tuple[float, dict]:
    report, schema_errors = validate_report()
    if not report:
        return 0.0, {"status": "missing"}
    decision = report.get("metric_decision")
    reason = report.get("metric_reason", "")
    review = report.get("metric_review", {})
    score = 0.0
    if decision in {"accepted", "repaired"} and bool(reason):
        score += 5.0
    if review.get("trustworthy") is True:
        score += 10.0
    if review.get("trust_signals"):
        score += 5.0
    if decision == "repaired" and review.get("problems_found") and review.get("repair_actions"):
        score += 10.0
    if decision == "accepted" and not review.get("problems_found") and review.get("repair_actions") == []:
        score += 10.0
    return round(score, 2), {
        "decision": decision,
        "has_reason": bool(reason),
        "schema_errors": schema_errors,
        "trustworthy": review.get("trustworthy"),
    }


def ratchet_execution() -> tuple[float, dict]:
    report, schema_errors = validate_report()
    rows, parse_errors = load_iterations()
    real_rows = real_iterations(rows)
    if not real_rows:
        return 0.0, {"status": "missing", "parse_errors": parse_errors}
    kept_rows = [row for row in real_rows if row.get("result") == "kept"]
    substantive_kept_rows = [row for row in kept_rows if row_has_substantive_change(row)]
    score = 0.0
    if real_rows:
        score += 10.0
    if all(row.get("validator_status") == "pass" for row in real_rows):
        score += 5.0
    if substantive_kept_rows:
        score += 5.0
    if report and not schema_errors and len(report.get("score_history", [])) == len(real_rows):
        score += 5.0
    elif report and report.get("score_history"):
        score += 3.0
    return round(min(score, 25.0), 2), {
        "status": None if not report else report.get("status"),
        "schema_errors": schema_errors,
        "real_rows": len(real_rows),
        "kept_rows": len(kept_rows),
        "substantive_kept_rows": len(substantive_kept_rows),
        "parse_errors": parse_errors,
    }


def non_dry_cycle_depth() -> tuple[float, dict]:
    report, schema_errors = validate_report()
    rows, parse_errors = load_iterations()
    real_rows = real_iterations(rows)
    if not real_rows:
        return 0.0, {"status": "missing", "parse_errors": parse_errors}
    substantive_kept_rows = [row for row in real_rows if row.get("result") == "kept" and row_has_substantive_change(row)]
    rejected_rows = [row for row in real_rows if row.get("result") in {"rejected", "reverted"}]
    history = [] if not report else report.get("score_history", [])
    score = 0.0
    if substantive_kept_rows:
        score += 10.0
    if len(substantive_kept_rows) >= 2:
        score += 5.0
    if len(substantive_kept_rows) >= 3:
        score += 5.0
    if substantive_kept_rows and rejected_rows:
        score += 5.0
    return round(min(score, 25.0), 2), {
        "count": len(real_rows),
        "substantive_kept_rows": len(substantive_kept_rows),
        "rejected_or_reverted_rows": len(rejected_rows),
        "history_rows": len(history),
        "real_rows": len(real_rows),
        "parse_errors": parse_errors,
        "schema_errors": schema_errors,
    }


def plateau_or_blocker_truth() -> tuple[float, dict]:
    report, schema_errors = validate_report()
    rows, parse_errors = load_iterations()
    history = real_iterations(rows)
    if not history or not report:
        return 0.0, {"status": "missing", "parse_errors": parse_errors}
    stop_reason = report.get("stop_reason", "")
    cycles = len(history)
    actual_consecutive = consecutive_non_improving_cycles(history)
    stop_evidence = report.get("stop_evidence", {})
    kind = stop_evidence.get("kind")
    score = 0.0
    if kind == "continuing":
        valid = report.get("status") == "running" and actual_consecutive < 2
        score = 25.0 if valid else 0.0
    elif kind == "plateau":
        valid = (
            report.get("status") == "pass"
            and cycles >= 2
            and int(report.get("real_non_dry_cycles_executed", 0)) == cycles
            and int(stop_evidence.get("consecutive_non_improving_cycles", 0)) >= 2
            and actual_consecutive >= 2
        )
        score = 25.0 if valid else 0.0
    elif kind == "blocker":
        valid = report.get("status") == "blocked" and bool(stop_evidence.get("blocker_details"))
        score = 25.0 if valid else 0.0
    return round(min(score, 25.0), 2), {
        "kind": kind,
        "stop_reason": stop_reason,
        "cycles": cycles,
        "actual_consecutive_non_improving": actual_consecutive,
        "schema_errors": schema_errors,
    }


def artifact_refresh() -> tuple[float, dict]:
    report, schema_errors = validate_report()
    rows, parse_errors = load_iterations()
    if not report and not rows:
        return 0.0, {"status": "missing"}
    history = real_iterations(rows)
    latest_row = history[-1] if history else None
    report_artifacts = set([] if not report else report.get("artifacts", []))
    latest_artifacts = set([] if not latest_row else latest_row.get("artifacts", []))
    score = 0.0
    if set(REQUIRED_ARTIFACTS).issubset(report_artifacts):
        score += 3.0
    if latest_row and set(REQUIRED_ARTIFACTS).issubset(latest_artifacts):
        score += 3.0
    span_seconds = artifact_span_seconds(
        [
            "evaluation/copilot-ratchet-report.json",
            "evaluation/validation-report.json",
            "promotion/readiness.json",
            "runs/iterations.jsonl",
        ]
    )
    if span_seconds is not None and span_seconds <= 600:
        score += 3.0
    tool_health = load_tool_health() or {}
    checks = tool_health.get("checks", {})
    tracked_statuses = [
        checks.get("gitnexus", {}).get("status", "missing"),
        checks.get("graphify", {}).get("status", "missing"),
        checks.get("infranodus", {}).get("status", "missing"),
        checks.get("agent_eval", {}).get("status", "missing"),
        checks.get("local_runners", {}).get("status", "missing"),
        checks.get("peer_mesh_local", {}).get("status", "missing"),
    ]
    tool_health_score = 0.0
    if tracked_statuses:
        tool_health_score = round(
            8.0
            * (
            sum(TOOL_STATUS_WEIGHTS.get(normalize_tool_status(status), 0.0) for status in tracked_statuses)
               / len(tracked_statuses)
            ),
            2,
        )
        score += tool_health_score
    parent_native_score, parent_native_details = parent_native_surface_refresh()
    score += min(parent_native_score, 4.0)
    inbox_front_door_score, inbox_front_door_details = inbox_front_door_surface_refresh()
    score += min(inbox_front_door_score, 1.5)
    research_governance_score, research_governance_details = research_governance_refresh()
    score += min(research_governance_score, 2.0)
    same_host_runtime_score, same_host_runtime_details = same_host_runtime_truth()
    score += same_host_runtime_score
    return round(min(score, 25.0), 2), {
        "report_artifacts_complete": set(REQUIRED_ARTIFACTS).issubset(report_artifacts),
        "latest_cycle_artifacts_complete": bool(latest_row) and set(REQUIRED_ARTIFACTS).issubset(latest_artifacts),
        "required": len(REQUIRED_ARTIFACTS),
        "freshness_span_seconds": span_seconds,
        "tool_statuses": tracked_statuses,
        "tool_health_score": tool_health_score,
        "parent_native_surface_score": min(parent_native_score, 4.0),
        "parent_native_surface_details": parent_native_details,
        "inbox_front_door_score": min(inbox_front_door_score, 1.5),
        "inbox_front_door_details": inbox_front_door_details,
        "research_governance_score": min(research_governance_score, 2.0),
        "research_governance_details": research_governance_details,
        "same_host_runtime_score": same_host_runtime_score,
        "same_host_runtime_details": same_host_runtime_details,
        "schema_errors": schema_errors,
        "parse_errors": parse_errors,
    }


def build_score() -> dict:
    iterations, iteration_parse_errors = load_iterations()
    outcome_components = {}
    for name, fn in [
        ("ratchet_execution", ratchet_execution),
        ("non_dry_cycle_depth", non_dry_cycle_depth),
        ("plateau_or_blocker_truth", plateau_or_blocker_truth),
        ("artifact_refresh", artifact_refresh),
    ]:
        score, details = fn()
        outcome_components[name] = {"score": score, "details": details}

    instrument_components = {}
    for name, fn in [
        ("validator_health", validator_health),
        ("report_completeness", report_completeness),
        ("metric_decision_truth", metric_decision_truth),
    ]:
        score, details = fn()
        instrument_components[name] = {"score": score, "details": details}

    outcome_score = round(sum(item["score"] for item in outcome_components.values()), 2)
    instrument_score = round(sum(item["score"] for item in instrument_components.values()), 2)
    total_score = round(0.75 * outcome_score + 0.25 * instrument_score, 2)

    weakest_component = min(
        {**outcome_components, **instrument_components}.items(),
        key=lambda item: item[1]["score"],
    )[0]

    payload = {
        "score_id": "PARENT-META-SCORE-0003",
        "created_at": date.today().isoformat(),
        "scope": "portable_parent_wrapper",
        "metric_mode": "split-ledger-validated-substantive",
        "total_score": total_score,
        "outcome_score": outcome_score,
        "instrument_score": instrument_score,
        "weakest_component": weakest_component,
        "outcome_components": outcome_components,
        "instrument_components": instrument_components,
        "iteration_count": len(real_iterations(iterations)),
        "iteration_parse_errors": iteration_parse_errors,
    }
    return payload


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()

    payload = build_score()
    (ROOT / "evaluation/metrics-latest.json").write_text(json.dumps(payload, indent=2) + "\n")
    if args.json:
        print(json.dumps(payload, indent=2))
    else:
        print(f"total_score={payload['total_score']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
