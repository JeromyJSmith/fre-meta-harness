from __future__ import annotations

from fastapi import FastAPI

from service.inbox_runtime import build_routing_artifacts, inbox_snapshot, scan_inbox_packets, write_router_outputs


app = FastAPI(title="fre-meta-harness inbox protocol service", version="0.1.0")


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}


@app.get("/api/inbox/queue")
def inbox_queue() -> dict:
    return inbox_snapshot()


@app.get("/api/dashboard")
def dashboard() -> dict:
    return inbox_snapshot()


@app.get("/api/inbox/packets")
def inbox_packets() -> list[dict]:
    return inbox_snapshot()["packets"]


@app.get("/api/routing/results")
def routing_results() -> list[dict]:
    return inbox_snapshot()["routing_decisions"]


@app.get("/api/delegations")
def delegations() -> list[dict]:
    return inbox_snapshot()["delegation_bundles"]


@app.post("/api/inbox/scan")
def inbox_scan() -> dict:
    results = scan_inbox_packets()
    artifacts = build_routing_artifacts(results)
    write_router_outputs(results, artifacts)
    return {
        "status": "ok",
        "packet_count": len(results),
        "routing_decision_path": "evaluation/tool-health/inbox-protocol/routing/all.json",
        "delegation_bundle_path": "evaluation/tool-health/inbox-protocol/delegations/all.json",
    }
