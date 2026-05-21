from __future__ import annotations

import json
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
        if not item["ref"].startswith(f"{item['unit_type']}:"):
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
            "evaluation/tool-health/peer-mesh-local.json",
            "evaluation/tool-health/peer-mesh-local.log",
            "evaluation/tool-health/peer-mesh-local-events.jsonl",
            "evaluation/tool-health/peer-mesh-local-benchmarks.json",
            "evaluation/research/compiled/capability-harvest.json",
            "evaluation/research/compiled/feature-matrix.json",
            "evaluation/research/compiled/gap-placement-map.json",
            "evaluation/research/compiled/source-index.json",
        ],
    }
    (ROOT / "promotion/readiness.json").write_text(json.dumps(readiness, indent=2) + "\n")
    print(json.dumps(report, indent=2))
    return 0 if overall == "pass" else 1


if __name__ == "__main__":
    raise SystemExit(main())
