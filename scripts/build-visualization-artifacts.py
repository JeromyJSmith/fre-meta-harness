from __future__ import annotations

import json
import re
from pathlib import Path
from typing import Any


ROOT = Path("/Volumes/PixelTable/VW_iTwin_Bridge/meta")
EVAL_DIR = ROOT / "evaluation"
RUNS_DIR = ROOT / "runs"


def load_json(path: Path) -> dict[str, Any] | None:
    if not path.exists():
        return None
    return json.loads(path.read_text())


def load_jsonl(path: Path) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    if not path.exists():
        return rows
    for line in path.read_text().splitlines():
        if not line.strip():
            continue
        try:
            rows.append(json.loads(line))
        except json.JSONDecodeError:
            continue
    return rows


def slug(value: str) -> str:
    return (
        value.lower()
        .replace(" ", "_")
        .replace("/", "_")
        .replace("-", "_")
        .replace(".", "_")
        .replace(":", "_")
    )


def build_score_timeline(metrics: dict[str, Any], ratchet_report: dict[str, Any] | None) -> tuple[list[dict[str, Any]], list[str]]:
    warnings: list[str] = []
    timeline: list[dict[str, Any]] = []

    if ratchet_report and ratchet_report.get("score_history"):
        for item in ratchet_report["score_history"]:
            cycle = item.get("cycle")
            timeline.append(
                {
                    "label": f"cycle-{cycle}-before",
                    "cycle": cycle,
                    "phase": "before",
                    "total_score": item.get("before_total_score"),
                    "outcome_score": item.get("before_outcome_score"),
                    "instrument_score": item.get("before_instrument_score"),
                }
            )
            timeline.append(
                {
                    "label": f"cycle-{cycle}-after",
                    "cycle": cycle,
                    "phase": "after",
                    "total_score": item.get("after_total_score"),
                    "outcome_score": item.get("after_outcome_score"),
                    "instrument_score": item.get("after_instrument_score"),
                }
            )
    else:
        warnings.append("No real copilot ratchet score history exists yet. Showing current baseline only.")
        timeline.append(
            {
                "label": "current-baseline",
                "cycle": 0,
                "phase": "current",
                "total_score": metrics.get("total_score", 0.0),
                "outcome_score": metrics.get("outcome_score", 0.0),
                "instrument_score": metrics.get("instrument_score", 0.0),
            }
        )

    return timeline, warnings


def build_component_rows(metrics: dict[str, Any]) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    for group_name in ("outcome_components", "instrument_components"):
        for name, payload in metrics.get(group_name, {}).items():
            rows.append(
                {
                    "name": name,
                    "family": "outcome" if group_name == "outcome_components" else "instrument",
                    "score": payload.get("score", 0.0),
                    "details": payload.get("details", {}),
                }
            )
    rows.sort(key=lambda row: (row["family"], row["score"]))
    return rows


def build_validation_summary(validation: dict[str, Any]) -> dict[str, Any]:
    checks = validation.get("checks", [])
    pass_count = sum(1 for item in checks if item.get("status") == "pass")
    fail_count = sum(1 for item in checks if item.get("status") == "fail")
    return {
        "overall_status": validation.get("overall_status", "unknown"),
        "pass_count": pass_count,
        "fail_count": fail_count,
        "checks": checks,
    }


def build_gate_coverage(phase_tool_map: dict[str, Any]) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    for gate_id, payload in phase_tool_map.get("phase_to_tools", {}).items():
        rows.append(
            {
                "gate_id": gate_id,
                "required_count": len(payload.get("required_tools", [])),
                "supporting_count": len(payload.get("supporting_tools", [])),
            }
        )
    return rows


def build_cluster_rows(live_summary: dict[str, Any] | None) -> list[dict[str, Any]]:
    if not live_summary:
        return []
    rows: list[dict[str, Any]] = []
    pattern = re.compile(
        r"^\d+\.\s+(?P<label>.*?):\s+.*\((?P<cluster>\d+)\s+\|\s+(?P<size>\d+)%\s+\|\s+(?P<influence>\d+)%\)$"
    )
    for item in live_summary.get("mainTopicalClusters", []):
        match = pattern.match(item)
        if not match:
            rows.append(
                {
                    "label": item,
                    "cluster_id": None,
                    "size_pct": 0,
                    "influence_pct": 0,
                }
            )
            continue
        rows.append(
            {
                "label": match.group("label"),
                "cluster_id": int(match.group("cluster")),
                "size_pct": int(match.group("size")),
                "influence_pct": int(match.group("influence")),
            }
        )
    return rows


def build_iteration_rows(rows: list[dict[str, Any]]) -> dict[str, Any]:
    real_rows = []
    legacy_rows = []
    for row in rows:
        if row.get("cycle_kind") == "dry_run" or row.get("iteration") == "dry-run":
            legacy_rows.append(row)
        else:
            real_rows.append(row)
    return {
        "real_rows": real_rows,
        "legacy_rows": legacy_rows,
        "real_count": len(real_rows),
        "legacy_count": len(legacy_rows),
    }


def build_graph(
    metrics: dict[str, Any],
    validation: dict[str, Any],
    readiness: dict[str, Any],
    gap_analysis: dict[str, Any],
    phase_tool_map: dict[str, Any],
    live_summary: dict[str, Any] | None,
) -> dict[str, Any]:
    nodes: list[dict[str, Any]] = []
    links: list[dict[str, Any]] = []
    seen_nodes: set[str] = set()

    def add_node(node_id: str, label: str, group: str, color: str, size: float = 8, meta: dict[str, Any] | None = None) -> None:
        if node_id in seen_nodes:
            return
        seen_nodes.add(node_id)
        nodes.append(
            {
                "id": node_id,
                "name": label,
                "group": group,
                "color": color,
                "val": size,
                "meta": meta or {},
            }
        )

    def add_link(source: str, target: str, relation: str, color: str = "#6b7280", width: float = 1.5) -> None:
        links.append(
            {
                "source": source,
                "target": target,
                "relation": relation,
                "color": color,
                "width": width,
            }
        )

    add_node(
        "parent_meta_wrapper",
        "Parent Meta Wrapper",
        "root",
        "#2563eb",
        18,
        {"scope": "portable_parent_wrapper"},
    )

    artifact_nodes = [
        ("metrics_latest", "metrics-latest.json", "artifact", "#0f766e", 12),
        ("validation_report", "validation-report.json", "artifact", "#0f766e", 12),
        ("promotion_readiness", "readiness.json", "artifact", "#0f766e", 12),
        ("iterations_ledger", "iterations.jsonl", "artifact", "#0f766e", 11),
        ("copilot_ratchet_report", "copilot-ratchet-report.json", "artifact", "#0f766e", 11),
    ]
    for node_id, label, group, color, size in artifact_nodes:
        add_node(node_id, label, group, color, size)
        add_link("parent_meta_wrapper", node_id, "emits", "#0f766e", 2)

    for repo in ("goal-md", "meta-harness", "autoresearch-mlx"):
        node_id = f"external_{slug(repo)}"
        add_node(node_id, repo, "external_repo", "#7c3aed", 11)
        add_link("parent_meta_wrapper", node_id, "imports", "#7c3aed", 2)

    for cluster in gap_analysis.get("topical_clusters", []):
        cluster_id = f"cluster_{slug(cluster)}"
        add_node(cluster_id, cluster, "cluster", "#f59e0b", 10)
        add_link("parent_meta_wrapper", cluster_id, "cluster", "#f59e0b", 1.5)

    for gap in gap_analysis.get("content_gaps", []):
        if "->" not in gap:
            continue
        source_label, target_label = [part.strip() for part in gap.split("->", 1)]
        source_id = f"cluster_{slug(source_label)}"
        target_id = f"cluster_{slug(target_label)}"
        add_node(source_id, source_label, "cluster", "#f59e0b", 10)
        add_node(target_id, target_label, "cluster", "#f59e0b", 10)
        add_link(source_id, target_id, "content_gap", "#dc2626", 4)

    for resolver in gap_analysis.get("resolved_by", []):
        resolver_id = f"resolver_{slug(resolver)}"
        add_node(resolver_id, resolver, "resolver", "#16a34a", 7)
        add_link("parent_meta_wrapper", resolver_id, "resolved_by", "#16a34a", 1)

    if live_summary:
        for cluster in build_cluster_rows(live_summary):
            cluster_id = f"live_cluster_{cluster['cluster_id'] if cluster['cluster_id'] is not None else slug(cluster['label'])}"
            add_node(
                cluster_id,
                cluster["label"],
                "live_cluster",
                "#f97316",
                8 + (cluster["influence_pct"] / 4 if cluster["influence_pct"] else 4),
                {
                    "size_pct": cluster["size_pct"],
                    "influence_pct": cluster["influence_pct"],
                },
            )
            add_link("parent_meta_wrapper", cluster_id, "infranodus_cluster", "#f97316", 1.5)

        for concept in live_summary.get("mainConcepts", []):
            concept_id = f"live_concept_{slug(concept)}"
            add_node(concept_id, concept, "live_concept", "#a855f7", 7)
            add_link("parent_meta_wrapper", concept_id, "main_concept", "#a855f7", 1)

        for gateway in live_summary.get("conceptualGateways", []):
            gateway_id = f"live_gateway_{slug(gateway)}"
            add_node(gateway_id, gateway, "gateway", "#ec4899", 8)
            add_link("parent_meta_wrapper", gateway_id, "gateway", "#ec4899", 1.2)

        for node in live_summary.get("topInfluentialNodes", []):
            influential_id = f"influential_{slug(node['node'])}"
            add_node(
                influential_id,
                node["node"],
                "influential_node",
                "#ef4444",
                10 + (node.get("degree", 0) / 2),
                {"bc": node.get("bc"), "degree": node.get("degree")},
            )
            add_link("metrics_latest", influential_id, "influential_node", "#ef4444", 2)

    for gate_id, payload in phase_tool_map.get("phase_to_tools", {}).items():
        gate_node = f"gate_{gate_id}"
        add_node(gate_node, gate_id, "gate", "#0891b2", 11)
        add_link("parent_meta_wrapper", gate_node, "gate", "#0891b2", 1.5)
        for tool in payload.get("required_tools", []):
            tool_id = f"tool_{slug(tool)}"
            add_node(tool_id, tool, "tool", "#475569", 6)
            add_link(gate_node, tool_id, "required", "#ef4444", 2)
        for tool in payload.get("supporting_tools", []):
            tool_id = f"tool_{slug(tool)}"
            add_node(tool_id, tool, "tool", "#475569", 6)
            add_link(gate_node, tool_id, "supporting", "#94a3b8", 1)

    for part_name, tools in phase_tool_map.get("proof_package_to_tools", {}).items():
        part_node = f"part_{slug(part_name)}"
        add_node(part_node, part_name, "proof_part", "#14b8a6", 9)
        add_link("parent_meta_wrapper", part_node, "proof_part", "#14b8a6", 1.5)
        for tool in tools:
            tool_id = f"tool_{slug(tool)}"
            add_node(tool_id, tool, "tool", "#475569", 6)
            add_link(part_node, tool_id, "supports_part", "#22c55e", 1)

    weakest = metrics.get("weakest_component")
    if weakest:
        weak_id = f"weakest_{slug(weakest)}"
        add_node(weak_id, weakest, "metric", "#b91c1c", 10, {"role": "weakest_component"})
        add_link("metrics_latest", weak_id, "weakest_component", "#b91c1c", 3)

    for blocker in readiness.get("blockers", []):
        blocker_id = f"blocker_{slug(blocker)}"
        add_node(blocker_id, blocker, "blocker", "#991b1b", 10)
        add_link("promotion_readiness", blocker_id, "blocked_by", "#991b1b", 3)

    for check in validation.get("checks", []):
        check_id = f"check_{slug(check.get('name', 'unknown'))}"
        status = check.get("status", "unknown")
        color = "#16a34a" if status == "pass" else "#dc2626"
        add_node(check_id, check.get("name", "unknown"), "validation_check", color, 6)
        add_link("validation_report", check_id, status, color, 1)

    return {"nodes": nodes, "links": links}


def main() -> int:
    metrics = load_json(EVAL_DIR / "metrics-latest.json") or {}
    validation = load_json(EVAL_DIR / "validation-report.json") or {}
    readiness = load_json(ROOT / "promotion/readiness.json") or {}
    gap_analysis = load_json(EVAL_DIR / "infranodus-gap-analysis.json") or {}
    live_summary = load_json(EVAL_DIR / "infranodus-live-summary.json")
    phase_tool_map = load_json(ROOT / "infranodus-phase-tool-map.json") or {}
    ratchet_report = load_json(EVAL_DIR / "copilot-ratchet-report.json")
    iteration_rows = load_jsonl(RUNS_DIR / "iterations.jsonl")

    score_timeline, timeline_warnings = build_score_timeline(metrics, ratchet_report)
    iteration_summary = build_iteration_rows(iteration_rows)

    dashboard = {
        "generated_at": "2026-05-18",
        "scope": "portable_parent_wrapper",
        "current_score": {
            "total_score": metrics.get("total_score", 0.0),
            "outcome_score": metrics.get("outcome_score", 0.0),
            "instrument_score": metrics.get("instrument_score", 0.0),
            "weakest_component": metrics.get("weakest_component"),
        },
        "score_timeline": score_timeline,
        "component_rows": build_component_rows(metrics),
        "validation_summary": build_validation_summary(validation),
        "gate_coverage": build_gate_coverage(phase_tool_map),
        "cluster_rows": build_cluster_rows(live_summary),
        "infranodus_live_summary": live_summary or {},
        "readiness": readiness,
        "gap_analysis": gap_analysis,
        "iteration_summary": iteration_summary,
        "ratchet_report_present": ratchet_report is not None,
        "warnings": timeline_warnings,
    }

    graph = build_graph(metrics, validation, readiness, gap_analysis, phase_tool_map, live_summary)

    (EVAL_DIR / "dashboard-data.json").write_text(json.dumps(dashboard, indent=2) + "\n")
    (EVAL_DIR / "infranodus-entity-graph.json").write_text(json.dumps(graph, indent=2) + "\n")

    payload = {
        "dashboard": dashboard,
        "graph": graph,
    }
    (EVAL_DIR / "dashboard-data.js").write_text(
        "window.__META_HARNESS_DASHBOARD__ = " + json.dumps(payload, indent=2) + ";\n"
    )
    print(json.dumps({"status": "ok", "artifacts": ["evaluation/dashboard-data.json", "evaluation/infranodus-entity-graph.json", "evaluation/dashboard-data.js"]}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
