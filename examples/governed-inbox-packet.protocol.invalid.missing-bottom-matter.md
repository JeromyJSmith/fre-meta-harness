---
id: "PACKET-PROTOCOL-20260521-INVALID"
slug: "governed-inbox-plan-packet-invalid"
doctype: "inbox_packet"
status: "proposed"
version: "1.0.0"
owner: "fre-meta-harness"
artifact_id: "PACKET-20260521-PROTOCOL-INVALID"
artifact_type: ".plan.md"
producer_role: "architect"
target_scope: "portable_parent_wrapper"
repo_root: "/Volumes/PixelTable/VW_iTWIN_Bridge/meta"
parent_only: true
structured_contract_ref: "contracts/inbox-packet.yaml"
structured_artifact_ref: "inbox/fre-meta-harness_plus_inbox.plan.json"
routing_tags:
  - "inbox-first"
required_consumers:
  - "filesystem-router"
upstream_refs:
  - "inbox/fre-meta-harness_plus_inbox.plan.md"
evidence_refs:
  - "agent-heavy-run-prompt.schema.json"
created_at: "2026-05-21T00:00:00Z"
updated_at: "2026-05-21T00:00:00Z"
---

# Summary

This invalid example omits bottom matter so the validator can prove that
governed inbox packets cannot advance without explicit gatekeeping state.
