from __future__ import annotations


def build_governance_and_runtime_checks(core) -> list[dict]:
    consume_source_quality_details = core.validate_consume_source_quality_outputs()
    consume_source_quality_report_details = core.validate_consume_source_quality_report()
    gap_map_strength_details = core.validate_gap_map_strength_slice()

    return [
        {
            "name": "governance_triad_slice",
            "status": "pass",
            "details": core.validate_governance_triad_slice(),
        },
        {
            "name": "inbox_front_door_protocol_slice",
            "status": "pass",
            "details": core.validate_inbox_front_door_slice(),
        },
        {
            "name": "capability_metrics_contract",
            "status": "pass",
            "details": core.validate_capability_metrics_contract(),
        },
        {
            "name": "research_governance_alignment",
            "status": "pass",
            "details": core.validate_research_governance(),
        },
        {
            "name": "consume_source_quality_outputs",
            "status": "pass" if not consume_source_quality_details["errors"] else "fail",
            "details": consume_source_quality_details,
        },
        {
            "name": "consume_source_quality_report",
            "status": "pass" if not consume_source_quality_report_details["errors"] else "fail",
            "details": consume_source_quality_report_details,
        },
        {
            "name": "gap_map_strength_slice",
            "status": "pass" if not gap_map_strength_details["errors"] else "fail",
            "details": gap_map_strength_details,
        },
        {
            "name": "tool_health_truth_boundaries",
            "status": "pass",
            "details": core.validate_tool_health_truth(),
        },
        {
            "name": "same_host_runtime_activation",
            "status": "pass",
            "details": core.validate_same_host_runtime_activation(),
        },
    ]
