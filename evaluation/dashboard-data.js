window.__META_HARNESS_DASHBOARD__ = {
  "dashboard": {
    "generated_at": "2026-05-18",
    "scope": "portable_parent_wrapper",
    "current_score": {
      "total_score": 90.62,
      "outcome_score": 87.5,
      "instrument_score": 100.0,
      "weakest_component": "plateau_or_blocker_truth"
    },
    "score_timeline": [
      {
        "label": "cycle-1-before",
        "cycle": 1,
        "phase": "before",
        "total_score": 10.0,
        "outcome_score": 0.0,
        "instrument_score": 40.0
      },
      {
        "label": "cycle-1-after",
        "cycle": 1,
        "phase": "after",
        "total_score": 83.12,
        "outcome_score": 77.5,
        "instrument_score": 100.0
      },
      {
        "label": "cycle-2-before",
        "cycle": 2,
        "phase": "before",
        "total_score": 83.12,
        "outcome_score": 77.5,
        "instrument_score": 100.0
      },
      {
        "label": "cycle-2-after",
        "cycle": 2,
        "phase": "after",
        "total_score": 90.62,
        "outcome_score": 87.5,
        "instrument_score": 100.0
      },
      {
        "label": "cycle-3-before",
        "cycle": 3,
        "phase": "before",
        "total_score": 90.62,
        "outcome_score": 87.5,
        "instrument_score": 100.0
      },
      {
        "label": "cycle-3-after",
        "cycle": 3,
        "phase": "after",
        "total_score": 90.62,
        "outcome_score": 87.5,
        "instrument_score": 100.0
      }
    ],
    "component_rows": [
      {
        "name": "report_completeness",
        "family": "instrument",
        "score": 30.0,
        "details": {
          "schema_errors": [],
          "history_rows": 3,
          "detailed_rows": 3,
          "ledger_rows": 3,
          "ledger_aligned": true,
          "parse_errors": []
        }
      },
      {
        "name": "metric_decision_truth",
        "family": "instrument",
        "score": 30.0,
        "details": {
          "decision": "repaired",
          "has_reason": true,
          "schema_errors": [],
          "trustworthy": true
        }
      },
      {
        "name": "validator_health",
        "family": "instrument",
        "score": 40.0,
        "details": {
          "status": "pass"
        }
      },
      {
        "name": "plateau_or_blocker_truth",
        "family": "outcome",
        "score": 12.5,
        "details": {
          "kind": "plateau",
          "stop_reason": "plateau after two consecutive non-improving real proposal cycles under the repaired metric",
          "cycles": 3,
          "actual_consecutive_non_improving": 2,
          "schema_errors": []
        }
      },
      {
        "name": "ratchet_execution",
        "family": "outcome",
        "score": 25.0,
        "details": {
          "status": "pass",
          "schema_errors": [],
          "real_rows": 3,
          "parse_errors": [],
          "mutable_files": 8,
          "files_changed": 8
        }
      },
      {
        "name": "non_dry_cycle_depth",
        "family": "outcome",
        "score": 25.0,
        "details": {
          "count": 3,
          "history_rows": 3,
          "real_rows": 3,
          "parse_errors": [],
          "schema_errors": []
        }
      },
      {
        "name": "artifact_refresh",
        "family": "outcome",
        "score": 25.0,
        "details": {
          "listed": 4,
          "ledger_listed": 4,
          "existing": 4,
          "required": 4,
          "freshness_span_seconds": 5.679206132888794,
          "schema_errors": [],
          "parse_errors": []
        }
      }
    ],
    "validation_summary": {
      "overall_status": "pass",
      "pass_count": 11,
      "fail_count": 0,
      "checks": [
        {
          "name": "required_scaffold_files",
          "status": "pass",
          "details": {
            "missing": []
          }
        },
        {
          "name": "required_prompt_contract_files",
          "status": "pass",
          "details": {
            "missing": []
          }
        },
        {
          "name": "required_proof_package_dirs",
          "status": "pass",
          "details": {
            "missing": []
          }
        },
        {
          "name": "required_program_files",
          "status": "pass",
          "details": {
            "missing": []
          }
        },
        {
          "name": "required_root_authorities",
          "status": "pass",
          "details": {
            "missing": []
          }
        },
        {
          "name": "required_local_upstream_clones",
          "status": "pass",
          "details": {
            "missing": []
          }
        },
        {
          "name": "scaffold_markdown_contracts",
          "status": "pass",
          "details": [
            {
              "file": "README.md",
              "status": "pass"
            },
            {
              "file": "AGENTS.md",
              "status": "pass"
            },
            {
              "file": "CLAUDE.md",
              "status": "pass"
            },
            {
              "file": "GOAL.md",
              "status": "pass"
            },
            {
              "file": "GOLDENPATH.md",
              "status": "pass"
            },
            {
              "file": "MEMORY.md",
              "status": "pass"
            }
          ]
        },
        {
          "name": "schema_and_example_validation",
          "status": "pass",
          "details": [
            {
              "file": "examples/front-matter.valid.json",
              "status": "pass"
            },
            {
              "file": "examples/bottom-matter.valid.json",
              "status": "pass"
            },
            {
              "file": "examples/copilot-ratchet-report.valid.json",
              "status": "pass"
            },
            {
              "file": "examples/iteration-record.valid.json",
              "status": "pass"
            },
            {
              "file": "examples/front-matter.invalid.missing-id.json",
              "status": "pass",
              "reason": "'id' is a required property"
            },
            {
              "file": "examples/bottom-matter.invalid.missing-gate-progress.json",
              "status": "pass",
              "reason": "'gate_progress' is a required property"
            },
            {
              "file": "examples/copilot-ratchet-report.invalid.missing-cycles.json",
              "status": "pass",
              "reason": "'metric_review' is a required property | 'real_non_dry_cycles_executed' is a required property | 'stop_evidence' is a required property | 'iteration_ledger_entries_appended' is a required property | [] should be non-empty | [] should be non-empty | [] is too short"
            },
            {
              "file": "examples/iteration-record.invalid.dry-run.json",
              "status": "pass",
              "reason": "Additional properties are not allowed ('after_score', 'before_score' were unexpected) | 'before_total_score' is a required property | 'after_total_score' is a required property | 'before_outcome_score' is a required property | 'after_outcome_score' is a required property | 'before_instrument_score' is a required property | 'after_instrument_score' is a required property | 'validator_status' is a required property | 'changed_files' is a required property | 'artifacts' is a required property | 'dry-run' is not of type 'integer' | 'dry_run' is not one of ['real_non_dry']"
            }
          ]
        },
        {
          "name": "program_markdown_contract",
          "status": "pass",
          "details": [
            {
              "file": "program.md",
              "status": "pass"
            }
          ]
        },
        {
          "name": "iteration_ledger_contract",
          "status": "pass",
          "details": {
            "path": "runs/iterations.jsonl",
            "row_count": 3,
            "parse_errors": [],
            "invalid_rows": []
          }
        },
        {
          "name": "copilot_ratchet_report_contract",
          "status": "pass",
          "details": {
            "path": "evaluation/copilot-ratchet-report.json",
            "errors": []
          }
        }
      ]
    },
    "gate_coverage": [
      {
        "gate_id": "harvest_gate",
        "required_count": 7,
        "supporting_count": 5
      },
      {
        "gate_id": "registry_gate",
        "required_count": 3,
        "supporting_count": 7
      },
      {
        "gate_id": "manifest_gate",
        "required_count": 3,
        "supporting_count": 4
      },
      {
        "gate_id": "verification_gate",
        "required_count": 3,
        "supporting_count": 3
      },
      {
        "gate_id": "state_gate",
        "required_count": 3,
        "supporting_count": 5
      },
      {
        "gate_id": "health_gate",
        "required_count": 3,
        "supporting_count": 7
      },
      {
        "gate_id": "promotion_gate",
        "required_count": 3,
        "supporting_count": 5
      }
    ],
    "cluster_rows": [
      {
        "label": "Prompt Governance",
        "cluster_id": 4,
        "size_pct": 7,
        "influence_pct": 20
      },
      {
        "label": "Goal Onboarding",
        "cluster_id": 0,
        "size_pct": 11,
        "influence_pct": 13
      },
      {
        "label": "Graph Analysis",
        "cluster_id": 10,
        "size_pct": 10,
        "influence_pct": 11
      },
      {
        "label": "Reporting Cycle",
        "cluster_id": 6,
        "size_pct": 7,
        "influence_pct": 10
      },
      {
        "label": "Content Generation",
        "cluster_id": 11,
        "size_pct": 6,
        "influence_pct": 10
      },
      {
        "label": "Tool Mapping",
        "cluster_id": 5,
        "size_pct": 5,
        "influence_pct": 10
      },
      {
        "label": "Meta Structure",
        "cluster_id": 1,
        "size_pct": 7,
        "influence_pct": 8
      },
      {
        "label": "Role Metrics",
        "cluster_id": 7,
        "size_pct": 19,
        "influence_pct": 6
      },
      {
        "label": "Operational Substrate",
        "cluster_id": 3,
        "size_pct": 13,
        "influence_pct": 5
      },
      {
        "label": "Active Identification",
        "cluster_id": 2,
        "size_pct": 9,
        "influence_pct": 3
      },
      {
        "label": "Scoring Validation",
        "cluster_id": 9,
        "size_pct": 5,
        "influence_pct": 3
      },
      {
        "label": "Proof Package",
        "cluster_id": 8,
        "size_pct": 1,
        "influence_pct": 0
      }
    ],
    "infranodus_live_summary": {
      "generated_at": "2026-05-18",
      "source": "mcp__infranodus__.generate_knowledge_graph",
      "scope": "portable_parent_wrapper",
      "statistics": {
        "modularity": 0.6840293674922019,
        "clusterCount": 12,
        "nodeCount": 150,
        "edgeCount": 256,
        "diversity_score": "dispersed",
        "modularity_score": "very_high"
      },
      "contentGaps": [
        "Gap 1: 3. Graph Analysis (knowledge graph exist analyze search text google related) -> 10. Active Identification (child body surface vw active identify standalone itwin)",
        "Gap 2: 3. Graph Analysis (knowledge graph exist analyze search text google related) -> 9. Operational Substrate (substrate ref operational pixeltable template authority upstream carry)",
        "Gap 3: 8. Role Metrics (metric current role blocker evidence durable iteration loop) -> 10. Active Identification (child body surface vw active identify standalone itwin)"
      ],
      "mainTopicalClusters": [
        "1. Prompt Governance: prompt schema run govern contract heavy maintain agent (4 | 7% | 20%)",
        "2. Goal Onboarding: md goal external program onboard domain slice autoresearch (0 | 11% | 13%)",
        "3. Graph Analysis: knowledge graph exist analyze search text google related (10 | 10% | 11%)",
        "4. Reporting Cycle: report ratchet real copilot dry cycle evaluator proposer (6 | 7% | 10%)",
        "5. Content Generation: generate seo topical contextual content cluster hint gap (11 | 6% | 10%)",
        "6. Tool Mapping: json map tool phase infranodus full required supporting (5 | 5% | 10%)",
        "7. Meta Structure: parent meta wrapper portable outer harness id slug (1 | 7% | 8%)",
        "8. Role Metrics: metric current role blocker evidence durable iteration loop (7 | 19% | 6%)",
        "9. Operational Substrate: substrate ref operational pixeltable template authority upstream carry (3 | 13% | 5%)",
        "10. Active Identification: child body surface vw active identify standalone itwin (2 | 9% | 3%)",
        "11. Scoring Validation: score split ledger script instrument runner validate outcome (9 | 5% | 3%)",
        "12. Proof Package: proof (8 | 1% | 0%)"
      ],
      "mainConcepts": [
        "prompt",
        "schema",
        "json",
        "md",
        "report",
        "generate",
        "seo",
        "parent",
        "goal",
        "run",
        "knowledge",
        "graph",
        "meta",
        "external",
        "govern",
        "ratchet"
      ],
      "conceptualGateways": [
        "seo",
        "schema",
        "json",
        "report",
        "generate",
        "exist",
        "knowledge",
        "external"
      ],
      "topRelations": [
        "1) meta <-> harness",
        "2) agent <-> heavy",
        "3) heavy <-> run",
        "4) run <-> prompt",
        "5) goal <-> md",
        "6) parent <-> meta",
        "7) search <-> query",
        "8) program <-> md",
        "9) prompt <-> schema",
        "10) required <-> tool",
        "11) supporting <-> tool",
        "12) readme <-> md"
      ],
      "topInfluentialNodes": [
        {
          "node": "prompt",
          "bc": 0.33992381643388353,
          "degree": 12
        },
        {
          "node": "schema",
          "bc": 0.3012425176854707,
          "degree": 3
        },
        {
          "node": "json",
          "bc": 0.27566660620351896,
          "degree": 5
        }
      ]
    },
    "readiness": {
      "readiness_id": "PARENT-META-PROMOTION-0001",
      "created_at": "2026-05-18",
      "scope": "portable_parent_wrapper",
      "status": "pass",
      "blockers": [],
      "evidence": [
        "evaluation/validation-report.json",
        "evaluation/copilot-ratchet-report.json",
        "infranodus-phase-tool-map.json",
        "library.yaml",
        "agent-heavy-run-prompt.schema.json",
        "program.md",
        "runs/iterations.jsonl"
      ]
    },
    "gap_analysis": {
      "analysis_id": "PARENT-META-INFRANODUS-GAP-0001",
      "created_at": "2026-05-18",
      "scope": "portable_parent_wrapper",
      "topical_clusters": [
        "Memory Goals",
        "Active Body",
        "Reusable Wrapper",
        "Knowledge Substrate",
        "Gate Optimization",
        "Document Scaffold",
        "Data Bridge",
        "Skill Verification",
        "Runtime Events",
        "Infrastructure Geometry"
      ],
      "content_gaps": [
        "Knowledge Substrate -> Gate Optimization",
        "Document Scaffold -> Data Bridge",
        "Knowledge Substrate -> Document Scaffold"
      ],
      "resolved_by": [
        "README.md",
        "library.yaml",
        "agent-heavy-run-prompt.schema.json",
        "infranodus-phase-tool-map.json",
        "pixeltable-operational-substrate.md",
        "source/",
        "schemas/",
        "examples/",
        "expected-failures/",
        "tests/",
        "evaluation/",
        "promotion/"
      ]
    },
    "iteration_summary": {
      "real_rows": [
        {
          "iteration": 1,
          "cycle_kind": "real_non_dry",
          "before_total_score": 10.0,
          "after_total_score": 83.12,
          "before_outcome_score": 0.0,
          "after_outcome_score": 77.5,
          "before_instrument_score": 40.0,
          "after_instrument_score": 100.0,
          "action": "replace dry-run evidence with the first real non-dry ledger row and a running structured report",
          "result": "kept",
          "validator_status": "pass",
          "changed_files": [
            "runs/iterations.jsonl",
            "evaluation/copilot-ratchet-report.json"
          ],
          "artifacts": [
            "evaluation/validation-report.json",
            "evaluation/metrics-latest.json",
            "promotion/readiness.json",
            "runs/iterations.jsonl"
          ],
          "note": "The trustworthy metric now has a real cycle ledger instead of a dry-run placeholder."
        },
        {
          "iteration": 2,
          "cycle_kind": "real_non_dry",
          "before_total_score": 83.12,
          "after_total_score": 90.62,
          "before_outcome_score": 77.5,
          "after_outcome_score": 87.5,
          "before_instrument_score": 100.0,
          "after_instrument_score": 100.0,
          "action": "test a README-only improvement-layer clarification and revert it when it fails to change the trustworthy metric",
          "result": "rejected",
          "validator_status": "pass",
          "changed_files": [
            "README.md",
            "runs/iterations.jsonl",
            "evaluation/copilot-ratchet-report.json"
          ],
          "artifacts": [
            "evaluation/validation-report.json",
            "evaluation/metrics-latest.json",
            "promotion/readiness.json",
            "runs/iterations.jsonl"
          ],
          "note": "The README clarification was reverted; the cycle is kept only as real non-dry evidence."
        },
        {
          "iteration": 3,
          "cycle_kind": "real_non_dry",
          "before_total_score": 90.62,
          "after_total_score": 90.62,
          "before_outcome_score": 87.5,
          "after_outcome_score": 87.5,
          "before_instrument_score": 100.0,
          "after_instrument_score": 100.0,
          "action": "test a prompt-YAML wording probe and revert it when it fails to improve the trustworthy metric",
          "result": "rejected",
          "validator_status": "pass",
          "changed_files": [
            "prompts/parent-wrapper-copilot-ratchet.prompt.yaml",
            "runs/iterations.jsonl",
            "evaluation/copilot-ratchet-report.json"
          ],
          "artifacts": [
            "evaluation/validation-report.json",
            "evaluation/metrics-latest.json",
            "promotion/readiness.json",
            "runs/iterations.jsonl"
          ],
          "note": "The prompt-YAML probe was reverted; this is the second consecutive non-improving proposal cycle."
        }
      ],
      "legacy_rows": [],
      "real_count": 3,
      "legacy_count": 0
    },
    "ratchet_report_present": true,
    "warnings": []
  },
  "graph": {
    "nodes": [
      {
        "id": "parent_meta_wrapper",
        "name": "Parent Meta Wrapper",
        "group": "root",
        "color": "#2563eb",
        "val": 18,
        "meta": {
          "scope": "portable_parent_wrapper"
        }
      },
      {
        "id": "metrics_latest",
        "name": "metrics-latest.json",
        "group": "artifact",
        "color": "#0f766e",
        "val": 12,
        "meta": {}
      },
      {
        "id": "validation_report",
        "name": "validation-report.json",
        "group": "artifact",
        "color": "#0f766e",
        "val": 12,
        "meta": {}
      },
      {
        "id": "promotion_readiness",
        "name": "readiness.json",
        "group": "artifact",
        "color": "#0f766e",
        "val": 12,
        "meta": {}
      },
      {
        "id": "iterations_ledger",
        "name": "iterations.jsonl",
        "group": "artifact",
        "color": "#0f766e",
        "val": 11,
        "meta": {}
      },
      {
        "id": "copilot_ratchet_report",
        "name": "copilot-ratchet-report.json",
        "group": "artifact",
        "color": "#0f766e",
        "val": 11,
        "meta": {}
      },
      {
        "id": "external_goal_md",
        "name": "goal-md",
        "group": "external_repo",
        "color": "#7c3aed",
        "val": 11,
        "meta": {}
      },
      {
        "id": "external_meta_harness",
        "name": "meta-harness",
        "group": "external_repo",
        "color": "#7c3aed",
        "val": 11,
        "meta": {}
      },
      {
        "id": "external_autoresearch_mlx",
        "name": "autoresearch-mlx",
        "group": "external_repo",
        "color": "#7c3aed",
        "val": 11,
        "meta": {}
      },
      {
        "id": "cluster_memory_goals",
        "name": "Memory Goals",
        "group": "cluster",
        "color": "#f59e0b",
        "val": 10,
        "meta": {}
      },
      {
        "id": "cluster_active_body",
        "name": "Active Body",
        "group": "cluster",
        "color": "#f59e0b",
        "val": 10,
        "meta": {}
      },
      {
        "id": "cluster_reusable_wrapper",
        "name": "Reusable Wrapper",
        "group": "cluster",
        "color": "#f59e0b",
        "val": 10,
        "meta": {}
      },
      {
        "id": "cluster_knowledge_substrate",
        "name": "Knowledge Substrate",
        "group": "cluster",
        "color": "#f59e0b",
        "val": 10,
        "meta": {}
      },
      {
        "id": "cluster_gate_optimization",
        "name": "Gate Optimization",
        "group": "cluster",
        "color": "#f59e0b",
        "val": 10,
        "meta": {}
      },
      {
        "id": "cluster_document_scaffold",
        "name": "Document Scaffold",
        "group": "cluster",
        "color": "#f59e0b",
        "val": 10,
        "meta": {}
      },
      {
        "id": "cluster_data_bridge",
        "name": "Data Bridge",
        "group": "cluster",
        "color": "#f59e0b",
        "val": 10,
        "meta": {}
      },
      {
        "id": "cluster_skill_verification",
        "name": "Skill Verification",
        "group": "cluster",
        "color": "#f59e0b",
        "val": 10,
        "meta": {}
      },
      {
        "id": "cluster_runtime_events",
        "name": "Runtime Events",
        "group": "cluster",
        "color": "#f59e0b",
        "val": 10,
        "meta": {}
      },
      {
        "id": "cluster_infrastructure_geometry",
        "name": "Infrastructure Geometry",
        "group": "cluster",
        "color": "#f59e0b",
        "val": 10,
        "meta": {}
      },
      {
        "id": "resolver_readme_md",
        "name": "README.md",
        "group": "resolver",
        "color": "#16a34a",
        "val": 7,
        "meta": {}
      },
      {
        "id": "resolver_library_yaml",
        "name": "library.yaml",
        "group": "resolver",
        "color": "#16a34a",
        "val": 7,
        "meta": {}
      },
      {
        "id": "resolver_agent_heavy_run_prompt_schema_json",
        "name": "agent-heavy-run-prompt.schema.json",
        "group": "resolver",
        "color": "#16a34a",
        "val": 7,
        "meta": {}
      },
      {
        "id": "resolver_infranodus_phase_tool_map_json",
        "name": "infranodus-phase-tool-map.json",
        "group": "resolver",
        "color": "#16a34a",
        "val": 7,
        "meta": {}
      },
      {
        "id": "resolver_pixeltable_operational_substrate_md",
        "name": "pixeltable-operational-substrate.md",
        "group": "resolver",
        "color": "#16a34a",
        "val": 7,
        "meta": {}
      },
      {
        "id": "resolver_source_",
        "name": "source/",
        "group": "resolver",
        "color": "#16a34a",
        "val": 7,
        "meta": {}
      },
      {
        "id": "resolver_schemas_",
        "name": "schemas/",
        "group": "resolver",
        "color": "#16a34a",
        "val": 7,
        "meta": {}
      },
      {
        "id": "resolver_examples_",
        "name": "examples/",
        "group": "resolver",
        "color": "#16a34a",
        "val": 7,
        "meta": {}
      },
      {
        "id": "resolver_expected_failures_",
        "name": "expected-failures/",
        "group": "resolver",
        "color": "#16a34a",
        "val": 7,
        "meta": {}
      },
      {
        "id": "resolver_tests_",
        "name": "tests/",
        "group": "resolver",
        "color": "#16a34a",
        "val": 7,
        "meta": {}
      },
      {
        "id": "resolver_evaluation_",
        "name": "evaluation/",
        "group": "resolver",
        "color": "#16a34a",
        "val": 7,
        "meta": {}
      },
      {
        "id": "resolver_promotion_",
        "name": "promotion/",
        "group": "resolver",
        "color": "#16a34a",
        "val": 7,
        "meta": {}
      },
      {
        "id": "live_cluster_4",
        "name": "Prompt Governance",
        "group": "live_cluster",
        "color": "#f97316",
        "val": 13.0,
        "meta": {
          "size_pct": 7,
          "influence_pct": 20
        }
      },
      {
        "id": "live_cluster_0",
        "name": "Goal Onboarding",
        "group": "live_cluster",
        "color": "#f97316",
        "val": 11.25,
        "meta": {
          "size_pct": 11,
          "influence_pct": 13
        }
      },
      {
        "id": "live_cluster_10",
        "name": "Graph Analysis",
        "group": "live_cluster",
        "color": "#f97316",
        "val": 10.75,
        "meta": {
          "size_pct": 10,
          "influence_pct": 11
        }
      },
      {
        "id": "live_cluster_6",
        "name": "Reporting Cycle",
        "group": "live_cluster",
        "color": "#f97316",
        "val": 10.5,
        "meta": {
          "size_pct": 7,
          "influence_pct": 10
        }
      },
      {
        "id": "live_cluster_11",
        "name": "Content Generation",
        "group": "live_cluster",
        "color": "#f97316",
        "val": 10.5,
        "meta": {
          "size_pct": 6,
          "influence_pct": 10
        }
      },
      {
        "id": "live_cluster_5",
        "name": "Tool Mapping",
        "group": "live_cluster",
        "color": "#f97316",
        "val": 10.5,
        "meta": {
          "size_pct": 5,
          "influence_pct": 10
        }
      },
      {
        "id": "live_cluster_1",
        "name": "Meta Structure",
        "group": "live_cluster",
        "color": "#f97316",
        "val": 10.0,
        "meta": {
          "size_pct": 7,
          "influence_pct": 8
        }
      },
      {
        "id": "live_cluster_7",
        "name": "Role Metrics",
        "group": "live_cluster",
        "color": "#f97316",
        "val": 9.5,
        "meta": {
          "size_pct": 19,
          "influence_pct": 6
        }
      },
      {
        "id": "live_cluster_3",
        "name": "Operational Substrate",
        "group": "live_cluster",
        "color": "#f97316",
        "val": 9.25,
        "meta": {
          "size_pct": 13,
          "influence_pct": 5
        }
      },
      {
        "id": "live_cluster_2",
        "name": "Active Identification",
        "group": "live_cluster",
        "color": "#f97316",
        "val": 8.75,
        "meta": {
          "size_pct": 9,
          "influence_pct": 3
        }
      },
      {
        "id": "live_cluster_9",
        "name": "Scoring Validation",
        "group": "live_cluster",
        "color": "#f97316",
        "val": 8.75,
        "meta": {
          "size_pct": 5,
          "influence_pct": 3
        }
      },
      {
        "id": "live_cluster_8",
        "name": "Proof Package",
        "group": "live_cluster",
        "color": "#f97316",
        "val": 12,
        "meta": {
          "size_pct": 1,
          "influence_pct": 0
        }
      },
      {
        "id": "live_concept_prompt",
        "name": "prompt",
        "group": "live_concept",
        "color": "#a855f7",
        "val": 7,
        "meta": {}
      },
      {
        "id": "live_concept_schema",
        "name": "schema",
        "group": "live_concept",
        "color": "#a855f7",
        "val": 7,
        "meta": {}
      },
      {
        "id": "live_concept_json",
        "name": "json",
        "group": "live_concept",
        "color": "#a855f7",
        "val": 7,
        "meta": {}
      },
      {
        "id": "live_concept_md",
        "name": "md",
        "group": "live_concept",
        "color": "#a855f7",
        "val": 7,
        "meta": {}
      },
      {
        "id": "live_concept_report",
        "name": "report",
        "group": "live_concept",
        "color": "#a855f7",
        "val": 7,
        "meta": {}
      },
      {
        "id": "live_concept_generate",
        "name": "generate",
        "group": "live_concept",
        "color": "#a855f7",
        "val": 7,
        "meta": {}
      },
      {
        "id": "live_concept_seo",
        "name": "seo",
        "group": "live_concept",
        "color": "#a855f7",
        "val": 7,
        "meta": {}
      },
      {
        "id": "live_concept_parent",
        "name": "parent",
        "group": "live_concept",
        "color": "#a855f7",
        "val": 7,
        "meta": {}
      },
      {
        "id": "live_concept_goal",
        "name": "goal",
        "group": "live_concept",
        "color": "#a855f7",
        "val": 7,
        "meta": {}
      },
      {
        "id": "live_concept_run",
        "name": "run",
        "group": "live_concept",
        "color": "#a855f7",
        "val": 7,
        "meta": {}
      },
      {
        "id": "live_concept_knowledge",
        "name": "knowledge",
        "group": "live_concept",
        "color": "#a855f7",
        "val": 7,
        "meta": {}
      },
      {
        "id": "live_concept_graph",
        "name": "graph",
        "group": "live_concept",
        "color": "#a855f7",
        "val": 7,
        "meta": {}
      },
      {
        "id": "live_concept_meta",
        "name": "meta",
        "group": "live_concept",
        "color": "#a855f7",
        "val": 7,
        "meta": {}
      },
      {
        "id": "live_concept_external",
        "name": "external",
        "group": "live_concept",
        "color": "#a855f7",
        "val": 7,
        "meta": {}
      },
      {
        "id": "live_concept_govern",
        "name": "govern",
        "group": "live_concept",
        "color": "#a855f7",
        "val": 7,
        "meta": {}
      },
      {
        "id": "live_concept_ratchet",
        "name": "ratchet",
        "group": "live_concept",
        "color": "#a855f7",
        "val": 7,
        "meta": {}
      },
      {
        "id": "live_gateway_seo",
        "name": "seo",
        "group": "gateway",
        "color": "#ec4899",
        "val": 8,
        "meta": {}
      },
      {
        "id": "live_gateway_schema",
        "name": "schema",
        "group": "gateway",
        "color": "#ec4899",
        "val": 8,
        "meta": {}
      },
      {
        "id": "live_gateway_json",
        "name": "json",
        "group": "gateway",
        "color": "#ec4899",
        "val": 8,
        "meta": {}
      },
      {
        "id": "live_gateway_report",
        "name": "report",
        "group": "gateway",
        "color": "#ec4899",
        "val": 8,
        "meta": {}
      },
      {
        "id": "live_gateway_generate",
        "name": "generate",
        "group": "gateway",
        "color": "#ec4899",
        "val": 8,
        "meta": {}
      },
      {
        "id": "live_gateway_exist",
        "name": "exist",
        "group": "gateway",
        "color": "#ec4899",
        "val": 8,
        "meta": {}
      },
      {
        "id": "live_gateway_knowledge",
        "name": "knowledge",
        "group": "gateway",
        "color": "#ec4899",
        "val": 8,
        "meta": {}
      },
      {
        "id": "live_gateway_external",
        "name": "external",
        "group": "gateway",
        "color": "#ec4899",
        "val": 8,
        "meta": {}
      },
      {
        "id": "influential_prompt",
        "name": "prompt",
        "group": "influential_node",
        "color": "#ef4444",
        "val": 16.0,
        "meta": {
          "bc": 0.33992381643388353,
          "degree": 12
        }
      },
      {
        "id": "influential_schema",
        "name": "schema",
        "group": "influential_node",
        "color": "#ef4444",
        "val": 11.5,
        "meta": {
          "bc": 0.3012425176854707,
          "degree": 3
        }
      },
      {
        "id": "influential_json",
        "name": "json",
        "group": "influential_node",
        "color": "#ef4444",
        "val": 12.5,
        "meta": {
          "bc": 0.27566660620351896,
          "degree": 5
        }
      },
      {
        "id": "gate_harvest_gate",
        "name": "harvest_gate",
        "group": "gate",
        "color": "#0891b2",
        "val": 11,
        "meta": {}
      },
      {
        "id": "tool_analyze_text",
        "name": "analyze_text",
        "group": "tool",
        "color": "#475569",
        "val": 6,
        "meta": {}
      },
      {
        "id": "tool_generate_knowledge_graph",
        "name": "generate_knowledge_graph",
        "group": "tool",
        "color": "#475569",
        "val": 6,
        "meta": {}
      },
      {
        "id": "tool_create_knowledge_graph",
        "name": "create_knowledge_graph",
        "group": "tool",
        "color": "#475569",
        "val": 6,
        "meta": {}
      },
      {
        "id": "tool_analyze_google_search_results",
        "name": "analyze_google_search_results",
        "group": "tool",
        "color": "#475569",
        "val": 6,
        "meta": {}
      },
      {
        "id": "tool_analyze_related_search_queries",
        "name": "analyze_related_search_queries",
        "group": "tool",
        "color": "#475569",
        "val": 6,
        "meta": {}
      },
      {
        "id": "tool_search_queries_vs_search_results",
        "name": "search_queries_vs_search_results",
        "group": "tool",
        "color": "#475569",
        "val": 6,
        "meta": {}
      },
      {
        "id": "tool_generate_seo_report",
        "name": "generate_seo_report",
        "group": "tool",
        "color": "#475569",
        "val": 6,
        "meta": {}
      },
      {
        "id": "tool_generate_topical_clusters",
        "name": "generate_topical_clusters",
        "group": "tool",
        "color": "#475569",
        "val": 6,
        "meta": {}
      },
      {
        "id": "tool_analyze_existing_graph_by_name",
        "name": "analyze_existing_graph_by_name",
        "group": "tool",
        "color": "#475569",
        "val": 6,
        "meta": {}
      },
      {
        "id": "tool_list_graphs",
        "name": "list_graphs",
        "group": "tool",
        "color": "#475569",
        "val": 6,
        "meta": {}
      },
      {
        "id": "tool_search",
        "name": "search",
        "group": "tool",
        "color": "#475569",
        "val": 6,
        "meta": {}
      },
      {
        "id": "tool_fetch",
        "name": "fetch",
        "group": "tool",
        "color": "#475569",
        "val": 6,
        "meta": {}
      },
      {
        "id": "gate_registry_gate",
        "name": "registry_gate",
        "group": "gate",
        "color": "#0891b2",
        "val": 11,
        "meta": {}
      },
      {
        "id": "gate_manifest_gate",
        "name": "manifest_gate",
        "group": "gate",
        "color": "#0891b2",
        "val": 11,
        "meta": {}
      },
      {
        "id": "tool_difference_between_texts",
        "name": "difference_between_texts",
        "group": "tool",
        "color": "#475569",
        "val": 6,
        "meta": {}
      },
      {
        "id": "tool_merged_graph_from_texts",
        "name": "merged_graph_from_texts",
        "group": "tool",
        "color": "#475569",
        "val": 6,
        "meta": {}
      },
      {
        "id": "tool_overlap_between_texts",
        "name": "overlap_between_texts",
        "group": "tool",
        "color": "#475569",
        "val": 6,
        "meta": {}
      },
      {
        "id": "gate_verification_gate",
        "name": "verification_gate",
        "group": "gate",
        "color": "#0891b2",
        "val": 11,
        "meta": {}
      },
      {
        "id": "tool_generate_contextual_hint",
        "name": "generate_contextual_hint",
        "group": "tool",
        "color": "#475569",
        "val": 6,
        "meta": {}
      },
      {
        "id": "tool_retrieve_from_knowledge_base",
        "name": "retrieve_from_knowledge_base",
        "group": "tool",
        "color": "#475569",
        "val": 6,
        "meta": {}
      },
      {
        "id": "gate_state_gate",
        "name": "state_gate",
        "group": "gate",
        "color": "#0891b2",
        "val": 11,
        "meta": {}
      },
      {
        "id": "tool_generate_content_gaps",
        "name": "generate_content_gaps",
        "group": "tool",
        "color": "#475569",
        "val": 6,
        "meta": {}
      },
      {
        "id": "tool_generate_responses_from_graph",
        "name": "generate_responses_from_graph",
        "group": "tool",
        "color": "#475569",
        "val": 6,
        "meta": {}
      },
      {
        "id": "gate_health_gate",
        "name": "health_gate",
        "group": "gate",
        "color": "#0891b2",
        "val": 11,
        "meta": {}
      },
      {
        "id": "gate_promotion_gate",
        "name": "promotion_gate",
        "group": "gate",
        "color": "#0891b2",
        "val": 11,
        "meta": {}
      },
      {
        "id": "tool_memory_get_relations",
        "name": "memory_get_relations",
        "group": "tool",
        "color": "#475569",
        "val": 6,
        "meta": {}
      },
      {
        "id": "part_source",
        "name": "source",
        "group": "proof_part",
        "color": "#14b8a6",
        "val": 9,
        "meta": {}
      },
      {
        "id": "part_schema",
        "name": "schema",
        "group": "proof_part",
        "color": "#14b8a6",
        "val": 9,
        "meta": {}
      },
      {
        "id": "part_examples",
        "name": "examples",
        "group": "proof_part",
        "color": "#14b8a6",
        "val": 9,
        "meta": {}
      },
      {
        "id": "part_expected_failures",
        "name": "expected_failures",
        "group": "proof_part",
        "color": "#14b8a6",
        "val": 9,
        "meta": {}
      },
      {
        "id": "part_tests",
        "name": "tests",
        "group": "proof_part",
        "color": "#14b8a6",
        "val": 9,
        "meta": {}
      },
      {
        "id": "part_evaluation",
        "name": "evaluation",
        "group": "proof_part",
        "color": "#14b8a6",
        "val": 9,
        "meta": {}
      },
      {
        "id": "part_promotion",
        "name": "promotion",
        "group": "proof_part",
        "color": "#14b8a6",
        "val": 9,
        "meta": {}
      },
      {
        "id": "weakest_plateau_or_blocker_truth",
        "name": "plateau_or_blocker_truth",
        "group": "metric",
        "color": "#b91c1c",
        "val": 10,
        "meta": {
          "role": "weakest_component"
        }
      },
      {
        "id": "check_required_scaffold_files",
        "name": "required_scaffold_files",
        "group": "validation_check",
        "color": "#16a34a",
        "val": 6,
        "meta": {}
      },
      {
        "id": "check_required_prompt_contract_files",
        "name": "required_prompt_contract_files",
        "group": "validation_check",
        "color": "#16a34a",
        "val": 6,
        "meta": {}
      },
      {
        "id": "check_required_proof_package_dirs",
        "name": "required_proof_package_dirs",
        "group": "validation_check",
        "color": "#16a34a",
        "val": 6,
        "meta": {}
      },
      {
        "id": "check_required_program_files",
        "name": "required_program_files",
        "group": "validation_check",
        "color": "#16a34a",
        "val": 6,
        "meta": {}
      },
      {
        "id": "check_required_root_authorities",
        "name": "required_root_authorities",
        "group": "validation_check",
        "color": "#16a34a",
        "val": 6,
        "meta": {}
      },
      {
        "id": "check_required_local_upstream_clones",
        "name": "required_local_upstream_clones",
        "group": "validation_check",
        "color": "#16a34a",
        "val": 6,
        "meta": {}
      },
      {
        "id": "check_scaffold_markdown_contracts",
        "name": "scaffold_markdown_contracts",
        "group": "validation_check",
        "color": "#16a34a",
        "val": 6,
        "meta": {}
      },
      {
        "id": "check_schema_and_example_validation",
        "name": "schema_and_example_validation",
        "group": "validation_check",
        "color": "#16a34a",
        "val": 6,
        "meta": {}
      },
      {
        "id": "check_program_markdown_contract",
        "name": "program_markdown_contract",
        "group": "validation_check",
        "color": "#16a34a",
        "val": 6,
        "meta": {}
      },
      {
        "id": "check_iteration_ledger_contract",
        "name": "iteration_ledger_contract",
        "group": "validation_check",
        "color": "#16a34a",
        "val": 6,
        "meta": {}
      },
      {
        "id": "check_copilot_ratchet_report_contract",
        "name": "copilot_ratchet_report_contract",
        "group": "validation_check",
        "color": "#16a34a",
        "val": 6,
        "meta": {}
      }
    ],
    "links": [
      {
        "source": "parent_meta_wrapper",
        "target": "metrics_latest",
        "relation": "emits",
        "color": "#0f766e",
        "width": 2
      },
      {
        "source": "parent_meta_wrapper",
        "target": "validation_report",
        "relation": "emits",
        "color": "#0f766e",
        "width": 2
      },
      {
        "source": "parent_meta_wrapper",
        "target": "promotion_readiness",
        "relation": "emits",
        "color": "#0f766e",
        "width": 2
      },
      {
        "source": "parent_meta_wrapper",
        "target": "iterations_ledger",
        "relation": "emits",
        "color": "#0f766e",
        "width": 2
      },
      {
        "source": "parent_meta_wrapper",
        "target": "copilot_ratchet_report",
        "relation": "emits",
        "color": "#0f766e",
        "width": 2
      },
      {
        "source": "parent_meta_wrapper",
        "target": "external_goal_md",
        "relation": "imports",
        "color": "#7c3aed",
        "width": 2
      },
      {
        "source": "parent_meta_wrapper",
        "target": "external_meta_harness",
        "relation": "imports",
        "color": "#7c3aed",
        "width": 2
      },
      {
        "source": "parent_meta_wrapper",
        "target": "external_autoresearch_mlx",
        "relation": "imports",
        "color": "#7c3aed",
        "width": 2
      },
      {
        "source": "parent_meta_wrapper",
        "target": "cluster_memory_goals",
        "relation": "cluster",
        "color": "#f59e0b",
        "width": 1.5
      },
      {
        "source": "parent_meta_wrapper",
        "target": "cluster_active_body",
        "relation": "cluster",
        "color": "#f59e0b",
        "width": 1.5
      },
      {
        "source": "parent_meta_wrapper",
        "target": "cluster_reusable_wrapper",
        "relation": "cluster",
        "color": "#f59e0b",
        "width": 1.5
      },
      {
        "source": "parent_meta_wrapper",
        "target": "cluster_knowledge_substrate",
        "relation": "cluster",
        "color": "#f59e0b",
        "width": 1.5
      },
      {
        "source": "parent_meta_wrapper",
        "target": "cluster_gate_optimization",
        "relation": "cluster",
        "color": "#f59e0b",
        "width": 1.5
      },
      {
        "source": "parent_meta_wrapper",
        "target": "cluster_document_scaffold",
        "relation": "cluster",
        "color": "#f59e0b",
        "width": 1.5
      },
      {
        "source": "parent_meta_wrapper",
        "target": "cluster_data_bridge",
        "relation": "cluster",
        "color": "#f59e0b",
        "width": 1.5
      },
      {
        "source": "parent_meta_wrapper",
        "target": "cluster_skill_verification",
        "relation": "cluster",
        "color": "#f59e0b",
        "width": 1.5
      },
      {
        "source": "parent_meta_wrapper",
        "target": "cluster_runtime_events",
        "relation": "cluster",
        "color": "#f59e0b",
        "width": 1.5
      },
      {
        "source": "parent_meta_wrapper",
        "target": "cluster_infrastructure_geometry",
        "relation": "cluster",
        "color": "#f59e0b",
        "width": 1.5
      },
      {
        "source": "cluster_knowledge_substrate",
        "target": "cluster_gate_optimization",
        "relation": "content_gap",
        "color": "#dc2626",
        "width": 4
      },
      {
        "source": "cluster_document_scaffold",
        "target": "cluster_data_bridge",
        "relation": "content_gap",
        "color": "#dc2626",
        "width": 4
      },
      {
        "source": "cluster_knowledge_substrate",
        "target": "cluster_document_scaffold",
        "relation": "content_gap",
        "color": "#dc2626",
        "width": 4
      },
      {
        "source": "parent_meta_wrapper",
        "target": "resolver_readme_md",
        "relation": "resolved_by",
        "color": "#16a34a",
        "width": 1
      },
      {
        "source": "parent_meta_wrapper",
        "target": "resolver_library_yaml",
        "relation": "resolved_by",
        "color": "#16a34a",
        "width": 1
      },
      {
        "source": "parent_meta_wrapper",
        "target": "resolver_agent_heavy_run_prompt_schema_json",
        "relation": "resolved_by",
        "color": "#16a34a",
        "width": 1
      },
      {
        "source": "parent_meta_wrapper",
        "target": "resolver_infranodus_phase_tool_map_json",
        "relation": "resolved_by",
        "color": "#16a34a",
        "width": 1
      },
      {
        "source": "parent_meta_wrapper",
        "target": "resolver_pixeltable_operational_substrate_md",
        "relation": "resolved_by",
        "color": "#16a34a",
        "width": 1
      },
      {
        "source": "parent_meta_wrapper",
        "target": "resolver_source_",
        "relation": "resolved_by",
        "color": "#16a34a",
        "width": 1
      },
      {
        "source": "parent_meta_wrapper",
        "target": "resolver_schemas_",
        "relation": "resolved_by",
        "color": "#16a34a",
        "width": 1
      },
      {
        "source": "parent_meta_wrapper",
        "target": "resolver_examples_",
        "relation": "resolved_by",
        "color": "#16a34a",
        "width": 1
      },
      {
        "source": "parent_meta_wrapper",
        "target": "resolver_expected_failures_",
        "relation": "resolved_by",
        "color": "#16a34a",
        "width": 1
      },
      {
        "source": "parent_meta_wrapper",
        "target": "resolver_tests_",
        "relation": "resolved_by",
        "color": "#16a34a",
        "width": 1
      },
      {
        "source": "parent_meta_wrapper",
        "target": "resolver_evaluation_",
        "relation": "resolved_by",
        "color": "#16a34a",
        "width": 1
      },
      {
        "source": "parent_meta_wrapper",
        "target": "resolver_promotion_",
        "relation": "resolved_by",
        "color": "#16a34a",
        "width": 1
      },
      {
        "source": "parent_meta_wrapper",
        "target": "live_cluster_4",
        "relation": "infranodus_cluster",
        "color": "#f97316",
        "width": 1.5
      },
      {
        "source": "parent_meta_wrapper",
        "target": "live_cluster_0",
        "relation": "infranodus_cluster",
        "color": "#f97316",
        "width": 1.5
      },
      {
        "source": "parent_meta_wrapper",
        "target": "live_cluster_10",
        "relation": "infranodus_cluster",
        "color": "#f97316",
        "width": 1.5
      },
      {
        "source": "parent_meta_wrapper",
        "target": "live_cluster_6",
        "relation": "infranodus_cluster",
        "color": "#f97316",
        "width": 1.5
      },
      {
        "source": "parent_meta_wrapper",
        "target": "live_cluster_11",
        "relation": "infranodus_cluster",
        "color": "#f97316",
        "width": 1.5
      },
      {
        "source": "parent_meta_wrapper",
        "target": "live_cluster_5",
        "relation": "infranodus_cluster",
        "color": "#f97316",
        "width": 1.5
      },
      {
        "source": "parent_meta_wrapper",
        "target": "live_cluster_1",
        "relation": "infranodus_cluster",
        "color": "#f97316",
        "width": 1.5
      },
      {
        "source": "parent_meta_wrapper",
        "target": "live_cluster_7",
        "relation": "infranodus_cluster",
        "color": "#f97316",
        "width": 1.5
      },
      {
        "source": "parent_meta_wrapper",
        "target": "live_cluster_3",
        "relation": "infranodus_cluster",
        "color": "#f97316",
        "width": 1.5
      },
      {
        "source": "parent_meta_wrapper",
        "target": "live_cluster_2",
        "relation": "infranodus_cluster",
        "color": "#f97316",
        "width": 1.5
      },
      {
        "source": "parent_meta_wrapper",
        "target": "live_cluster_9",
        "relation": "infranodus_cluster",
        "color": "#f97316",
        "width": 1.5
      },
      {
        "source": "parent_meta_wrapper",
        "target": "live_cluster_8",
        "relation": "infranodus_cluster",
        "color": "#f97316",
        "width": 1.5
      },
      {
        "source": "parent_meta_wrapper",
        "target": "live_concept_prompt",
        "relation": "main_concept",
        "color": "#a855f7",
        "width": 1
      },
      {
        "source": "parent_meta_wrapper",
        "target": "live_concept_schema",
        "relation": "main_concept",
        "color": "#a855f7",
        "width": 1
      },
      {
        "source": "parent_meta_wrapper",
        "target": "live_concept_json",
        "relation": "main_concept",
        "color": "#a855f7",
        "width": 1
      },
      {
        "source": "parent_meta_wrapper",
        "target": "live_concept_md",
        "relation": "main_concept",
        "color": "#a855f7",
        "width": 1
      },
      {
        "source": "parent_meta_wrapper",
        "target": "live_concept_report",
        "relation": "main_concept",
        "color": "#a855f7",
        "width": 1
      },
      {
        "source": "parent_meta_wrapper",
        "target": "live_concept_generate",
        "relation": "main_concept",
        "color": "#a855f7",
        "width": 1
      },
      {
        "source": "parent_meta_wrapper",
        "target": "live_concept_seo",
        "relation": "main_concept",
        "color": "#a855f7",
        "width": 1
      },
      {
        "source": "parent_meta_wrapper",
        "target": "live_concept_parent",
        "relation": "main_concept",
        "color": "#a855f7",
        "width": 1
      },
      {
        "source": "parent_meta_wrapper",
        "target": "live_concept_goal",
        "relation": "main_concept",
        "color": "#a855f7",
        "width": 1
      },
      {
        "source": "parent_meta_wrapper",
        "target": "live_concept_run",
        "relation": "main_concept",
        "color": "#a855f7",
        "width": 1
      },
      {
        "source": "parent_meta_wrapper",
        "target": "live_concept_knowledge",
        "relation": "main_concept",
        "color": "#a855f7",
        "width": 1
      },
      {
        "source": "parent_meta_wrapper",
        "target": "live_concept_graph",
        "relation": "main_concept",
        "color": "#a855f7",
        "width": 1
      },
      {
        "source": "parent_meta_wrapper",
        "target": "live_concept_meta",
        "relation": "main_concept",
        "color": "#a855f7",
        "width": 1
      },
      {
        "source": "parent_meta_wrapper",
        "target": "live_concept_external",
        "relation": "main_concept",
        "color": "#a855f7",
        "width": 1
      },
      {
        "source": "parent_meta_wrapper",
        "target": "live_concept_govern",
        "relation": "main_concept",
        "color": "#a855f7",
        "width": 1
      },
      {
        "source": "parent_meta_wrapper",
        "target": "live_concept_ratchet",
        "relation": "main_concept",
        "color": "#a855f7",
        "width": 1
      },
      {
        "source": "parent_meta_wrapper",
        "target": "live_gateway_seo",
        "relation": "gateway",
        "color": "#ec4899",
        "width": 1.2
      },
      {
        "source": "parent_meta_wrapper",
        "target": "live_gateway_schema",
        "relation": "gateway",
        "color": "#ec4899",
        "width": 1.2
      },
      {
        "source": "parent_meta_wrapper",
        "target": "live_gateway_json",
        "relation": "gateway",
        "color": "#ec4899",
        "width": 1.2
      },
      {
        "source": "parent_meta_wrapper",
        "target": "live_gateway_report",
        "relation": "gateway",
        "color": "#ec4899",
        "width": 1.2
      },
      {
        "source": "parent_meta_wrapper",
        "target": "live_gateway_generate",
        "relation": "gateway",
        "color": "#ec4899",
        "width": 1.2
      },
      {
        "source": "parent_meta_wrapper",
        "target": "live_gateway_exist",
        "relation": "gateway",
        "color": "#ec4899",
        "width": 1.2
      },
      {
        "source": "parent_meta_wrapper",
        "target": "live_gateway_knowledge",
        "relation": "gateway",
        "color": "#ec4899",
        "width": 1.2
      },
      {
        "source": "parent_meta_wrapper",
        "target": "live_gateway_external",
        "relation": "gateway",
        "color": "#ec4899",
        "width": 1.2
      },
      {
        "source": "metrics_latest",
        "target": "influential_prompt",
        "relation": "influential_node",
        "color": "#ef4444",
        "width": 2
      },
      {
        "source": "metrics_latest",
        "target": "influential_schema",
        "relation": "influential_node",
        "color": "#ef4444",
        "width": 2
      },
      {
        "source": "metrics_latest",
        "target": "influential_json",
        "relation": "influential_node",
        "color": "#ef4444",
        "width": 2
      },
      {
        "source": "parent_meta_wrapper",
        "target": "gate_harvest_gate",
        "relation": "gate",
        "color": "#0891b2",
        "width": 1.5
      },
      {
        "source": "gate_harvest_gate",
        "target": "tool_analyze_text",
        "relation": "required",
        "color": "#ef4444",
        "width": 2
      },
      {
        "source": "gate_harvest_gate",
        "target": "tool_generate_knowledge_graph",
        "relation": "required",
        "color": "#ef4444",
        "width": 2
      },
      {
        "source": "gate_harvest_gate",
        "target": "tool_create_knowledge_graph",
        "relation": "required",
        "color": "#ef4444",
        "width": 2
      },
      {
        "source": "gate_harvest_gate",
        "target": "tool_analyze_google_search_results",
        "relation": "required",
        "color": "#ef4444",
        "width": 2
      },
      {
        "source": "gate_harvest_gate",
        "target": "tool_analyze_related_search_queries",
        "relation": "required",
        "color": "#ef4444",
        "width": 2
      },
      {
        "source": "gate_harvest_gate",
        "target": "tool_search_queries_vs_search_results",
        "relation": "required",
        "color": "#ef4444",
        "width": 2
      },
      {
        "source": "gate_harvest_gate",
        "target": "tool_generate_seo_report",
        "relation": "required",
        "color": "#ef4444",
        "width": 2
      },
      {
        "source": "gate_harvest_gate",
        "target": "tool_generate_topical_clusters",
        "relation": "supporting",
        "color": "#94a3b8",
        "width": 1
      },
      {
        "source": "gate_harvest_gate",
        "target": "tool_analyze_existing_graph_by_name",
        "relation": "supporting",
        "color": "#94a3b8",
        "width": 1
      },
      {
        "source": "gate_harvest_gate",
        "target": "tool_list_graphs",
        "relation": "supporting",
        "color": "#94a3b8",
        "width": 1
      },
      {
        "source": "gate_harvest_gate",
        "target": "tool_search",
        "relation": "supporting",
        "color": "#94a3b8",
        "width": 1
      },
      {
        "source": "gate_harvest_gate",
        "target": "tool_fetch",
        "relation": "supporting",
        "color": "#94a3b8",
        "width": 1
      },
      {
        "source": "parent_meta_wrapper",
        "target": "gate_registry_gate",
        "relation": "gate",
        "color": "#0891b2",
        "width": 1.5
      },
      {
        "source": "gate_registry_gate",
        "target": "tool_analyze_existing_graph_by_name",
        "relation": "required",
        "color": "#ef4444",
        "width": 2
      },
      {
        "source": "gate_registry_gate",
        "target": "tool_generate_topical_clusters",
        "relation": "required",
        "color": "#ef4444",
        "width": 2
      },
      {
        "source": "gate_registry_gate",
        "target": "tool_search",
        "relation": "required",
        "color": "#ef4444",
        "width": 2
      },
      {
        "source": "gate_registry_gate",
        "target": "tool_fetch",
        "relation": "supporting",
        "color": "#94a3b8",
        "width": 1
      },
      {
        "source": "gate_registry_gate",
        "target": "tool_list_graphs",
        "relation": "supporting",
        "color": "#94a3b8",
        "width": 1
      },
      {
        "source": "gate_registry_gate",
        "target": "tool_generate_knowledge_graph",
        "relation": "supporting",
        "color": "#94a3b8",
        "width": 1
      },
      {
        "source": "gate_registry_gate",
        "target": "tool_create_knowledge_graph",
        "relation": "supporting",
        "color": "#94a3b8",
        "width": 1
      },
      {
        "source": "gate_registry_gate",
        "target": "tool_analyze_google_search_results",
        "relation": "supporting",
        "color": "#94a3b8",
        "width": 1
      },
      {
        "source": "gate_registry_gate",
        "target": "tool_analyze_related_search_queries",
        "relation": "supporting",
        "color": "#94a3b8",
        "width": 1
      },
      {
        "source": "gate_registry_gate",
        "target": "tool_search_queries_vs_search_results",
        "relation": "supporting",
        "color": "#94a3b8",
        "width": 1
      },
      {
        "source": "parent_meta_wrapper",
        "target": "gate_manifest_gate",
        "relation": "gate",
        "color": "#0891b2",
        "width": 1.5
      },
      {
        "source": "gate_manifest_gate",
        "target": "tool_difference_between_texts",
        "relation": "required",
        "color": "#ef4444",
        "width": 2
      },
      {
        "source": "gate_manifest_gate",
        "target": "tool_generate_topical_clusters",
        "relation": "required",
        "color": "#ef4444",
        "width": 2
      },
      {
        "source": "gate_manifest_gate",
        "target": "tool_merged_graph_from_texts",
        "relation": "required",
        "color": "#ef4444",
        "width": 2
      },
      {
        "source": "gate_manifest_gate",
        "target": "tool_overlap_between_texts",
        "relation": "supporting",
        "color": "#94a3b8",
        "width": 1
      },
      {
        "source": "gate_manifest_gate",
        "target": "tool_analyze_existing_graph_by_name",
        "relation": "supporting",
        "color": "#94a3b8",
        "width": 1
      },
      {
        "source": "gate_manifest_gate",
        "target": "tool_search",
        "relation": "supporting",
        "color": "#94a3b8",
        "width": 1
      },
      {
        "source": "gate_manifest_gate",
        "target": "tool_fetch",
        "relation": "supporting",
        "color": "#94a3b8",
        "width": 1
      },
      {
        "source": "parent_meta_wrapper",
        "target": "gate_verification_gate",
        "relation": "gate",
        "color": "#0891b2",
        "width": 1.5
      },
      {
        "source": "gate_verification_gate",
        "target": "tool_difference_between_texts",
        "relation": "required",
        "color": "#ef4444",
        "width": 2
      },
      {
        "source": "gate_verification_gate",
        "target": "tool_generate_contextual_hint",
        "relation": "required",
        "color": "#ef4444",
        "width": 2
      },
      {
        "source": "gate_verification_gate",
        "target": "tool_retrieve_from_knowledge_base",
        "relation": "required",
        "color": "#ef4444",
        "width": 2
      },
      {
        "source": "gate_verification_gate",
        "target": "tool_overlap_between_texts",
        "relation": "supporting",
        "color": "#94a3b8",
        "width": 1
      },
      {
        "source": "gate_verification_gate",
        "target": "tool_merged_graph_from_texts",
        "relation": "supporting",
        "color": "#94a3b8",
        "width": 1
      },
      {
        "source": "gate_verification_gate",
        "target": "tool_analyze_existing_graph_by_name",
        "relation": "supporting",
        "color": "#94a3b8",
        "width": 1
      },
      {
        "source": "parent_meta_wrapper",
        "target": "gate_state_gate",
        "relation": "gate",
        "color": "#0891b2",
        "width": 1.5
      },
      {
        "source": "gate_state_gate",
        "target": "tool_generate_content_gaps",
        "relation": "required",
        "color": "#ef4444",
        "width": 2
      },
      {
        "source": "gate_state_gate",
        "target": "tool_difference_between_texts",
        "relation": "required",
        "color": "#ef4444",
        "width": 2
      },
      {
        "source": "gate_state_gate",
        "target": "tool_generate_contextual_hint",
        "relation": "required",
        "color": "#ef4444",
        "width": 2
      },
      {
        "source": "gate_state_gate",
        "target": "tool_retrieve_from_knowledge_base",
        "relation": "supporting",
        "color": "#94a3b8",
        "width": 1
      },
      {
        "source": "gate_state_gate",
        "target": "tool_analyze_existing_graph_by_name",
        "relation": "supporting",
        "color": "#94a3b8",
        "width": 1
      },
      {
        "source": "gate_state_gate",
        "target": "tool_generate_responses_from_graph",
        "relation": "supporting",
        "color": "#94a3b8",
        "width": 1
      },
      {
        "source": "gate_state_gate",
        "target": "tool_search_queries_vs_search_results",
        "relation": "supporting",
        "color": "#94a3b8",
        "width": 1
      },
      {
        "source": "gate_state_gate",
        "target": "tool_analyze_related_search_queries",
        "relation": "supporting",
        "color": "#94a3b8",
        "width": 1
      },
      {
        "source": "parent_meta_wrapper",
        "target": "gate_health_gate",
        "relation": "gate",
        "color": "#0891b2",
        "width": 1.5
      },
      {
        "source": "gate_health_gate",
        "target": "tool_difference_between_texts",
        "relation": "required",
        "color": "#ef4444",
        "width": 2
      },
      {
        "source": "gate_health_gate",
        "target": "tool_generate_content_gaps",
        "relation": "required",
        "color": "#ef4444",
        "width": 2
      },
      {
        "source": "gate_health_gate",
        "target": "tool_merged_graph_from_texts",
        "relation": "required",
        "color": "#ef4444",
        "width": 2
      },
      {
        "source": "gate_health_gate",
        "target": "tool_overlap_between_texts",
        "relation": "supporting",
        "color": "#94a3b8",
        "width": 1
      },
      {
        "source": "gate_health_gate",
        "target": "tool_generate_topical_clusters",
        "relation": "supporting",
        "color": "#94a3b8",
        "width": 1
      },
      {
        "source": "gate_health_gate",
        "target": "tool_generate_contextual_hint",
        "relation": "supporting",
        "color": "#94a3b8",
        "width": 1
      },
      {
        "source": "gate_health_gate",
        "target": "tool_retrieve_from_knowledge_base",
        "relation": "supporting",
        "color": "#94a3b8",
        "width": 1
      },
      {
        "source": "gate_health_gate",
        "target": "tool_analyze_google_search_results",
        "relation": "supporting",
        "color": "#94a3b8",
        "width": 1
      },
      {
        "source": "gate_health_gate",
        "target": "tool_search_queries_vs_search_results",
        "relation": "supporting",
        "color": "#94a3b8",
        "width": 1
      },
      {
        "source": "gate_health_gate",
        "target": "tool_generate_seo_report",
        "relation": "supporting",
        "color": "#94a3b8",
        "width": 1
      },
      {
        "source": "parent_meta_wrapper",
        "target": "gate_promotion_gate",
        "relation": "gate",
        "color": "#0891b2",
        "width": 1.5
      },
      {
        "source": "gate_promotion_gate",
        "target": "tool_generate_content_gaps",
        "relation": "required",
        "color": "#ef4444",
        "width": 2
      },
      {
        "source": "gate_promotion_gate",
        "target": "tool_retrieve_from_knowledge_base",
        "relation": "required",
        "color": "#ef4444",
        "width": 2
      },
      {
        "source": "gate_promotion_gate",
        "target": "tool_difference_between_texts",
        "relation": "required",
        "color": "#ef4444",
        "width": 2
      },
      {
        "source": "gate_promotion_gate",
        "target": "tool_generate_contextual_hint",
        "relation": "supporting",
        "color": "#94a3b8",
        "width": 1
      },
      {
        "source": "gate_promotion_gate",
        "target": "tool_generate_responses_from_graph",
        "relation": "supporting",
        "color": "#94a3b8",
        "width": 1
      },
      {
        "source": "gate_promotion_gate",
        "target": "tool_merged_graph_from_texts",
        "relation": "supporting",
        "color": "#94a3b8",
        "width": 1
      },
      {
        "source": "gate_promotion_gate",
        "target": "tool_memory_get_relations",
        "relation": "supporting",
        "color": "#94a3b8",
        "width": 1
      },
      {
        "source": "gate_promotion_gate",
        "target": "tool_generate_seo_report",
        "relation": "supporting",
        "color": "#94a3b8",
        "width": 1
      },
      {
        "source": "parent_meta_wrapper",
        "target": "part_source",
        "relation": "proof_part",
        "color": "#14b8a6",
        "width": 1.5
      },
      {
        "source": "part_source",
        "target": "tool_analyze_text",
        "relation": "supports_part",
        "color": "#22c55e",
        "width": 1
      },
      {
        "source": "part_source",
        "target": "tool_generate_knowledge_graph",
        "relation": "supports_part",
        "color": "#22c55e",
        "width": 1
      },
      {
        "source": "part_source",
        "target": "tool_create_knowledge_graph",
        "relation": "supports_part",
        "color": "#22c55e",
        "width": 1
      },
      {
        "source": "part_source",
        "target": "tool_list_graphs",
        "relation": "supports_part",
        "color": "#22c55e",
        "width": 1
      },
      {
        "source": "part_source",
        "target": "tool_search",
        "relation": "supports_part",
        "color": "#22c55e",
        "width": 1
      },
      {
        "source": "part_source",
        "target": "tool_analyze_google_search_results",
        "relation": "supports_part",
        "color": "#22c55e",
        "width": 1
      },
      {
        "source": "part_source",
        "target": "tool_analyze_related_search_queries",
        "relation": "supports_part",
        "color": "#22c55e",
        "width": 1
      },
      {
        "source": "part_source",
        "target": "tool_search_queries_vs_search_results",
        "relation": "supports_part",
        "color": "#22c55e",
        "width": 1
      },
      {
        "source": "part_source",
        "target": "tool_generate_seo_report",
        "relation": "supports_part",
        "color": "#22c55e",
        "width": 1
      },
      {
        "source": "parent_meta_wrapper",
        "target": "part_schema",
        "relation": "proof_part",
        "color": "#14b8a6",
        "width": 1.5
      },
      {
        "source": "part_schema",
        "target": "tool_difference_between_texts",
        "relation": "supports_part",
        "color": "#22c55e",
        "width": 1
      },
      {
        "source": "part_schema",
        "target": "tool_generate_topical_clusters",
        "relation": "supports_part",
        "color": "#22c55e",
        "width": 1
      },
      {
        "source": "part_schema",
        "target": "tool_analyze_existing_graph_by_name",
        "relation": "supports_part",
        "color": "#22c55e",
        "width": 1
      },
      {
        "source": "part_schema",
        "target": "tool_fetch",
        "relation": "supports_part",
        "color": "#22c55e",
        "width": 1
      },
      {
        "source": "parent_meta_wrapper",
        "target": "part_examples",
        "relation": "proof_part",
        "color": "#14b8a6",
        "width": 1.5
      },
      {
        "source": "part_examples",
        "target": "tool_analyze_existing_graph_by_name",
        "relation": "supports_part",
        "color": "#22c55e",
        "width": 1
      },
      {
        "source": "part_examples",
        "target": "tool_generate_contextual_hint",
        "relation": "supports_part",
        "color": "#22c55e",
        "width": 1
      },
      {
        "source": "part_examples",
        "target": "tool_overlap_between_texts",
        "relation": "supports_part",
        "color": "#22c55e",
        "width": 1
      },
      {
        "source": "part_examples",
        "target": "tool_merged_graph_from_texts",
        "relation": "supports_part",
        "color": "#22c55e",
        "width": 1
      },
      {
        "source": "parent_meta_wrapper",
        "target": "part_expected_failures",
        "relation": "proof_part",
        "color": "#14b8a6",
        "width": 1.5
      },
      {
        "source": "part_expected_failures",
        "target": "tool_generate_content_gaps",
        "relation": "supports_part",
        "color": "#22c55e",
        "width": 1
      },
      {
        "source": "part_expected_failures",
        "target": "tool_difference_between_texts",
        "relation": "supports_part",
        "color": "#22c55e",
        "width": 1
      },
      {
        "source": "part_expected_failures",
        "target": "tool_generate_topical_clusters",
        "relation": "supports_part",
        "color": "#22c55e",
        "width": 1
      },
      {
        "source": "part_expected_failures",
        "target": "tool_search_queries_vs_search_results",
        "relation": "supports_part",
        "color": "#22c55e",
        "width": 1
      },
      {
        "source": "parent_meta_wrapper",
        "target": "part_tests",
        "relation": "proof_part",
        "color": "#14b8a6",
        "width": 1.5
      },
      {
        "source": "part_tests",
        "target": "tool_difference_between_texts",
        "relation": "supports_part",
        "color": "#22c55e",
        "width": 1
      },
      {
        "source": "part_tests",
        "target": "tool_generate_topical_clusters",
        "relation": "supports_part",
        "color": "#22c55e",
        "width": 1
      },
      {
        "source": "part_tests",
        "target": "tool_generate_contextual_hint",
        "relation": "supports_part",
        "color": "#22c55e",
        "width": 1
      },
      {
        "source": "part_tests",
        "target": "tool_retrieve_from_knowledge_base",
        "relation": "supports_part",
        "color": "#22c55e",
        "width": 1
      },
      {
        "source": "parent_meta_wrapper",
        "target": "part_evaluation",
        "relation": "proof_part",
        "color": "#14b8a6",
        "width": 1.5
      },
      {
        "source": "part_evaluation",
        "target": "tool_difference_between_texts",
        "relation": "supports_part",
        "color": "#22c55e",
        "width": 1
      },
      {
        "source": "part_evaluation",
        "target": "tool_generate_content_gaps",
        "relation": "supports_part",
        "color": "#22c55e",
        "width": 1
      },
      {
        "source": "part_evaluation",
        "target": "tool_generate_contextual_hint",
        "relation": "supports_part",
        "color": "#22c55e",
        "width": 1
      },
      {
        "source": "part_evaluation",
        "target": "tool_merged_graph_from_texts",
        "relation": "supports_part",
        "color": "#22c55e",
        "width": 1
      },
      {
        "source": "part_evaluation",
        "target": "tool_overlap_between_texts",
        "relation": "supports_part",
        "color": "#22c55e",
        "width": 1
      },
      {
        "source": "part_evaluation",
        "target": "tool_analyze_google_search_results",
        "relation": "supports_part",
        "color": "#22c55e",
        "width": 1
      },
      {
        "source": "part_evaluation",
        "target": "tool_analyze_related_search_queries",
        "relation": "supports_part",
        "color": "#22c55e",
        "width": 1
      },
      {
        "source": "part_evaluation",
        "target": "tool_search_queries_vs_search_results",
        "relation": "supports_part",
        "color": "#22c55e",
        "width": 1
      },
      {
        "source": "part_evaluation",
        "target": "tool_generate_seo_report",
        "relation": "supports_part",
        "color": "#22c55e",
        "width": 1
      },
      {
        "source": "parent_meta_wrapper",
        "target": "part_promotion",
        "relation": "proof_part",
        "color": "#14b8a6",
        "width": 1.5
      },
      {
        "source": "part_promotion",
        "target": "tool_generate_content_gaps",
        "relation": "supports_part",
        "color": "#22c55e",
        "width": 1
      },
      {
        "source": "part_promotion",
        "target": "tool_retrieve_from_knowledge_base",
        "relation": "supports_part",
        "color": "#22c55e",
        "width": 1
      },
      {
        "source": "part_promotion",
        "target": "tool_difference_between_texts",
        "relation": "supports_part",
        "color": "#22c55e",
        "width": 1
      },
      {
        "source": "part_promotion",
        "target": "tool_generate_responses_from_graph",
        "relation": "supports_part",
        "color": "#22c55e",
        "width": 1
      },
      {
        "source": "part_promotion",
        "target": "tool_memory_get_relations",
        "relation": "supports_part",
        "color": "#22c55e",
        "width": 1
      },
      {
        "source": "part_promotion",
        "target": "tool_generate_seo_report",
        "relation": "supports_part",
        "color": "#22c55e",
        "width": 1
      },
      {
        "source": "metrics_latest",
        "target": "weakest_plateau_or_blocker_truth",
        "relation": "weakest_component",
        "color": "#b91c1c",
        "width": 3
      },
      {
        "source": "validation_report",
        "target": "check_required_scaffold_files",
        "relation": "pass",
        "color": "#16a34a",
        "width": 1
      },
      {
        "source": "validation_report",
        "target": "check_required_prompt_contract_files",
        "relation": "pass",
        "color": "#16a34a",
        "width": 1
      },
      {
        "source": "validation_report",
        "target": "check_required_proof_package_dirs",
        "relation": "pass",
        "color": "#16a34a",
        "width": 1
      },
      {
        "source": "validation_report",
        "target": "check_required_program_files",
        "relation": "pass",
        "color": "#16a34a",
        "width": 1
      },
      {
        "source": "validation_report",
        "target": "check_required_root_authorities",
        "relation": "pass",
        "color": "#16a34a",
        "width": 1
      },
      {
        "source": "validation_report",
        "target": "check_required_local_upstream_clones",
        "relation": "pass",
        "color": "#16a34a",
        "width": 1
      },
      {
        "source": "validation_report",
        "target": "check_scaffold_markdown_contracts",
        "relation": "pass",
        "color": "#16a34a",
        "width": 1
      },
      {
        "source": "validation_report",
        "target": "check_schema_and_example_validation",
        "relation": "pass",
        "color": "#16a34a",
        "width": 1
      },
      {
        "source": "validation_report",
        "target": "check_program_markdown_contract",
        "relation": "pass",
        "color": "#16a34a",
        "width": 1
      },
      {
        "source": "validation_report",
        "target": "check_iteration_ledger_contract",
        "relation": "pass",
        "color": "#16a34a",
        "width": 1
      },
      {
        "source": "validation_report",
        "target": "check_copilot_ratchet_report_contract",
        "relation": "pass",
        "color": "#16a34a",
        "width": 1
      }
    ]
  }
};
