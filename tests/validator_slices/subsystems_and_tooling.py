from __future__ import annotations


def build_subsystems_and_tooling_checks(core) -> list[dict]:
    tool_packaging_details = core.validate_tool_packaging_slice()
    subsystem_runner_proof_details = core.validate_subsystem_runner_proof_slice()

    return [
        {
            "name": "subsystem_harness_architecture_slice",
            "status": "pass",
            "details": core.validate_subsystem_architecture_slice(),
        },
        {
            "name": "tool_packaging_contract_family",
            "status": "pass" if not tool_packaging_details["errors"] else "fail",
            "details": tool_packaging_details,
        },
        {
            "name": "subsystem_runner_proof_family",
            "status": "pass" if not subsystem_runner_proof_details["errors"] else "fail",
            "details": subsystem_runner_proof_details,
        },
        {
            "name": "parent_native_orchestration_contracts",
            "status": "pass",
            "details": core.validate_parent_native_contracts(),
        },
    ]
