# Contracts

Reusable parent-wrapper contract artifacts live here once they move beyond the
root scaffold and proof-package seed surfaces.

Current contracts:

- `agent-eval-parent-lane.yaml`
- `parent-capability-metrics.yaml`
- `peer-mesh.yaml`
- `peer-message.yaml`
- `peer-lifecycle.yaml`
- `observability-event.yaml`
- `observability-ingest.yaml`
- `policy-decision.yaml`
- `library-distribution.yaml`
- `benchmark-emission.yaml`
- `peer-mesh-runtime.yaml`
- `agent-role-contract.yaml`
- `hook-manifest.yaml`
- `capability-matrix.yaml`
- `research-packet-manifest.yaml`

The communication slice is now explicit about peer primitives, role classes,
prompt plus command guards, lifecycle completion, policy decisions, and
observability ingestion. The Phase 2 slice adds decoupled ingest, typed
distribution, and benchmark-emission contracts on top of that communication
plane. The research-governance slice makes the packetized harvest and compiled
research views first-class governed surfaces instead of loose artifact files.
