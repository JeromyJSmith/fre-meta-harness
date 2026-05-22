window.__META_HARNESS_DASHBOARD__ = {
  "dashboard": {
    "generated_at": "2026-05-18",
    "scope": "portable_parent_wrapper",
    "current_score": {
      "total_score": 97.56,
      "outcome_score": 96.75,
      "instrument_score": 100.0,
      "weakest_component": "artifact_refresh"
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
      },
      {
        "label": "cycle-4-before",
        "cycle": 4,
        "phase": "before",
        "total_score": 90.62,
        "outcome_score": 87.5,
        "instrument_score": 100.0
      },
      {
        "label": "cycle-4-after",
        "cycle": 4,
        "phase": "after",
        "total_score": 100.0,
        "outcome_score": 100.0,
        "instrument_score": 100.0
      },
      {
        "label": "cycle-5-before",
        "cycle": 5,
        "phase": "before",
        "total_score": 100.0,
        "outcome_score": 100.0,
        "instrument_score": 100.0
      },
      {
        "label": "cycle-5-after",
        "cycle": 5,
        "phase": "after",
        "total_score": 100.0,
        "outcome_score": 100.0,
        "instrument_score": 100.0
      },
      {
        "label": "cycle-6-before",
        "cycle": 6,
        "phase": "before",
        "total_score": 86.09,
        "outcome_score": 81.45,
        "instrument_score": 100.0
      },
      {
        "label": "cycle-6-after",
        "cycle": 6,
        "phase": "after",
        "total_score": 92.84,
        "outcome_score": 90.45,
        "instrument_score": 100.0
      },
      {
        "label": "cycle-7-before",
        "cycle": 7,
        "phase": "before",
        "total_score": 92.84,
        "outcome_score": 90.45,
        "instrument_score": 100.0
      },
      {
        "label": "cycle-7-after",
        "cycle": 7,
        "phase": "after",
        "total_score": 92.84,
        "outcome_score": 90.45,
        "instrument_score": 100.0
      },
      {
        "label": "cycle-8-before",
        "cycle": 8,
        "phase": "before",
        "total_score": 89.84,
        "outcome_score": 86.45,
        "instrument_score": 100.0
      },
      {
        "label": "cycle-8-after",
        "cycle": 8,
        "phase": "after",
        "total_score": 91.3,
        "outcome_score": 88.4,
        "instrument_score": 100.0
      },
      {
        "label": "cycle-9-before",
        "cycle": 9,
        "phase": "before",
        "total_score": 91.3,
        "outcome_score": 88.4,
        "instrument_score": 100.0
      },
      {
        "label": "cycle-9-after",
        "cycle": 9,
        "phase": "after",
        "total_score": 91.3,
        "outcome_score": 88.4,
        "instrument_score": 100.0
      },
      {
        "label": "cycle-10-before",
        "cycle": 10,
        "phase": "before",
        "total_score": 95.05,
        "outcome_score": 93.4,
        "instrument_score": 100.0
      },
      {
        "label": "cycle-10-after",
        "cycle": 10,
        "phase": "after",
        "total_score": 97.56,
        "outcome_score": 96.75,
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
          "history_rows": 10,
          "detailed_rows": 10,
          "ledger_rows": 10,
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
        "name": "artifact_refresh",
        "family": "outcome",
        "score": 21.75,
        "details": {
          "report_artifacts_complete": true,
          "latest_cycle_artifacts_complete": true,
          "required": 4,
          "freshness_span_seconds": 11.505916118621826,
          "tool_statuses": [
            "bounded_pass",
            "bounded_pass",
            "bounded_pass",
            "dry_pass",
            "pass"
          ],
          "tool_health_score": 9.75,
          "schema_errors": [],
          "parse_errors": []
        }
      },
      {
        "name": "ratchet_execution",
        "family": "outcome",
        "score": 25.0,
        "details": {
          "status": "blocked",
          "schema_errors": [],
          "real_rows": 10,
          "kept_rows": 5,
          "substantive_kept_rows": 4,
          "parse_errors": []
        }
      },
      {
        "name": "non_dry_cycle_depth",
        "family": "outcome",
        "score": 25.0,
        "details": {
          "count": 10,
          "substantive_kept_rows": 4,
          "rejected_or_reverted_rows": 5,
          "history_rows": 10,
          "real_rows": 10,
          "parse_errors": [],
          "schema_errors": []
        }
      },
      {
        "name": "plateau_or_blocker_truth",
        "family": "outcome",
        "score": 25.0,
        "details": {
          "kind": "blocker",
          "stop_reason": "exact blocker: live InfraNodus MCP escalation remains blocked because no local runtime credential or session configuration was present, so the bounded local substitute stayed as the strongest honest parent analysis path",
          "cycles": 10,
          "actual_consecutive_non_improving": 0,
          "schema_errors": []
        }
      }
    ],
    "validation_summary": {
      "overall_status": "pass",
      "pass_count": 13,
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
              "file": "examples/capability-harvest-metrics.valid.json",
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
            },
            {
              "file": "examples/capability-harvest-metrics.invalid.docs-only.json",
              "status": "pass",
              "reason": "['docs', 'docs'] has non-unique elements | ['docs', 'docs'] does not contain items matching the given schema"
            }
          ]
        },
        {
          "name": "capability_metrics_contract",
          "status": "pass",
          "details": {
            "path": "contracts/parent-capability-metrics.yaml",
            "metric_family_count": 11,
            "metric_ids": [
              "blocker_precision",
              "cost_local_resource_use",
              "documentation_quality",
              "evidence_freshness",
              "execution_success",
              "latency_runtime",
              "operator_usability",
              "regression_resistance",
              "reproducibility",
              "tool_health_availability",
              "validation_pass_rate"
            ]
          }
        },
        {
          "name": "tool_health_truth_boundaries",
          "status": "pass",
          "details": {
            "path": "evaluation/tool-health/status.json",
            "gitnexus_status": "bounded_pass",
            "graphify_status": "bounded_pass",
            "infranodus_status": "bounded_pass",
            "live_infranodus_status": "blocked"
          }
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
            "row_count": 10,
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
        "label": "evaluation",
        "cluster_id": 1,
        "size_pct": 13,
        "influence_pct": 99
      },
      {
        "label": "meta_loop",
        "cluster_id": 2,
        "size_pct": 34,
        "influence_pct": 99
      },
      {
        "label": "autoresearch",
        "cluster_id": 3,
        "size_pct": 20,
        "influence_pct": 99
      },
      {
        "label": "meta_harness",
        "cluster_id": 4,
        "size_pct": 12,
        "influence_pct": 99
      },
      {
        "label": "agent_eval",
        "cluster_id": 5,
        "size_pct": 5,
        "influence_pct": 99
      },
      {
        "label": "tool_health",
        "cluster_id": 6,
        "size_pct": 16,
        "influence_pct": 99
      }
    ],
    "infranodus_live_summary": {
      "generated_at": "2026-05-20",
      "source": "bounded_local_cli_substitute",
      "scope": "portable_parent_wrapper",
      "statistics": {
        "clusterCount": 6,
        "nodeCount": 523,
        "edgeCount": 15,
        "diversity_score": "bounded_local",
        "modularity_score": "approximate"
      },
      "contentGaps": [
        "Gap 1: meta_harness -> agent_eval",
        "Gap 2: evaluation -> meta_harness",
        "Gap 3: autoresearch -> agent_eval"
      ],
      "mainTopicalClusters": [
        "1. evaluation: evaluation tool_health agent_eval readme scripts cycle (1 | 13% | 99%)",
        "2. meta_loop: evaluation tool_health status iterations external jsonl (2 | 34% | 99%)",
        "3. autoresearch: source external name description status evaluation (3 | 20% | 99%)",
        "4. meta_harness: status external gate_id notes doctrine green (4 | 12% | 99%)",
        "5. agent_eval: smoke agent_eval evaluation dry docker tool_health (5 | 5% | 99%)",
        "6. tool_health: status evaluation summary tool_health command_path duration_ms (6 | 16% | 99%)"
      ],
      "mainConcepts": [
        "evaluation",
        "status",
        "tool_health",
        "external",
        "agent_eval",
        "evidence",
        "readme",
        "scripts",
        "bounded",
        "gate_id",
        "notes",
        "program"
      ],
      "conceptualGateways": [
        "evaluation",
        "status",
        "tool_health",
        "external",
        "agent_eval",
        "evidence",
        "readme",
        "scripts"
      ],
      "topRelations": [
        "1) evaluation <-> meta_loop",
        "2) meta_loop <-> autoresearch",
        "3) autoresearch <-> meta_harness",
        "4) meta_loop <-> tool_health",
        "5) evaluation <-> agent_eval",
        "6) evaluation <-> autoresearch",
        "7) evaluation <-> tool_health",
        "8) agent_eval <-> tool_health",
        "9) autoresearch <-> tool_health",
        "10) meta_loop <-> agent_eval"
      ],
      "topInfluentialNodes": [
        {
          "node": "evaluation",
          "bc": 0.833,
          "degree": 5
        },
        {
          "node": "status",
          "bc": 0.833,
          "degree": 5
        },
        {
          "node": "tool_health",
          "bc": 0.833,
          "degree": 5
        },
        {
          "node": "external",
          "bc": 0.5,
          "degree": 3
        },
        {
          "node": "agent_eval",
          "bc": 0.667,
          "degree": 4
        },
        {
          "node": "evidence",
          "bc": 0.333,
          "degree": 2
        },
        {
          "node": "readme",
          "bc": 0.333,
          "degree": 2
        },
        {
          "node": "scripts",
          "bc": 0.333,
          "degree": 2
        }
      ],
      "limitations": [
        "Live InfraNodus MCP analysis remains API/OAuth-bound and no local runtime credential or session configuration was present in this run.",
        "This bounded substitute reports graph structure honestly but does not claim live InfraNodus MCP output."
      ]
    },
    "infranodus_conceptual_bridges": {
      "analysis_id": "PARENT-META-INFRANODUS-BRIDGES-0001",
      "created_at": "2026-05-20",
      "scope": "portable_parent_wrapper",
      "mode": "bounded_local_cli_substitute",
      "bridges": [
        {
          "bridge_id": "meta_harness-to-agent_eval",
          "from_layer": "meta_harness",
          "to_layer": "agent_eval",
          "through_layer": "tool_health",
          "bridge_terms": [
            "evaluation",
            "status",
            "tool_health"
          ],
          "reason": "Low-overlap layers need a shared operational vocabulary to stay comparable.",
          "evidence": [
            "evaluation/tool-health/status.json",
            "evaluation/tool-health/local-runners.json",
            "contracts/parent-capability-metrics.yaml"
          ]
        },
        {
          "bridge_id": "evaluation-to-meta_harness",
          "from_layer": "evaluation",
          "to_layer": "meta_harness",
          "through_layer": "tool_health",
          "bridge_terms": [
            "status"
          ],
          "reason": "Low-overlap layers need a shared operational vocabulary to stay comparable.",
          "evidence": [
            "evaluation/tool-health/status.json",
            "evaluation/tool-health/local-runners.json",
            "contracts/parent-capability-metrics.yaml"
          ]
        },
        {
          "bridge_id": "autoresearch-to-agent_eval",
          "from_layer": "autoresearch",
          "to_layer": "agent_eval",
          "through_layer": "tool_health",
          "bridge_terms": [
            "evaluation",
            "tool_health"
          ],
          "reason": "Low-overlap layers need a shared operational vocabulary to stay comparable.",
          "evidence": [
            "evaluation/tool-health/status.json",
            "evaluation/tool-health/local-runners.json",
            "contracts/parent-capability-metrics.yaml"
          ]
        }
      ],
      "limitations": [
        "Live InfraNodus MCP analysis remains API/OAuth-bound and no local runtime credential or session configuration was present in this run.",
        "This bounded substitute reports graph structure honestly but does not claim live InfraNodus MCP output."
      ]
    },
    "infranodus_research_topics": {
      "analysis_id": "PARENT-META-INFRANODUS-RESEARCH-0001",
      "created_at": "2026-05-20",
      "scope": "portable_parent_wrapper",
      "mode": "bounded_local_cli_substitute",
      "topics": [
        {
          "topic_id": "topic-1",
          "title": "Bridge meta_harness and agent_eval through observable local evidence",
          "priority": 1,
          "driven_by_gaps": [
            "meta_harness -> agent_eval"
          ],
          "bridge_terms": [
            "evaluation",
            "status",
            "tool_health",
            "external"
          ],
          "questions": [
            "Which bounded commands connect meta_harness outputs to agent_eval decisions?",
            "Which artifact should become the canonical bridge between meta_harness and agent_eval?"
          ],
          "recommended_artifacts": [
            "contracts/parent-capability-metrics.yaml",
            "evaluation/tool-health/status.json",
            "evaluation/infranodus-gap-analysis.json"
          ]
        },
        {
          "topic_id": "topic-2",
          "title": "Bridge evaluation and meta_harness through observable local evidence",
          "priority": 2,
          "driven_by_gaps": [
            "evaluation -> meta_harness"
          ],
          "bridge_terms": [
            "status"
          ],
          "questions": [
            "Which bounded commands connect evaluation outputs to meta_harness decisions?",
            "Which artifact should become the canonical bridge between evaluation and meta_harness?"
          ],
          "recommended_artifacts": [
            "contracts/parent-capability-metrics.yaml",
            "evaluation/tool-health/status.json",
            "evaluation/infranodus-gap-analysis.json"
          ]
        },
        {
          "topic_id": "topic-3",
          "title": "Bridge autoresearch and agent_eval through observable local evidence",
          "priority": 3,
          "driven_by_gaps": [
            "autoresearch -> agent_eval"
          ],
          "bridge_terms": [
            "evaluation",
            "tool_health"
          ],
          "questions": [
            "Which bounded commands connect autoresearch outputs to agent_eval decisions?",
            "Which artifact should become the canonical bridge between autoresearch and agent_eval?"
          ],
          "recommended_artifacts": [
            "contracts/parent-capability-metrics.yaml",
            "evaluation/tool-health/status.json",
            "evaluation/infranodus-gap-analysis.json"
          ]
        },
        {
          "topic_id": "topic-4",
          "title": "Bridge meta_loop and meta_harness through observable local evidence",
          "priority": 4,
          "driven_by_gaps": [
            "meta_loop -> meta_harness"
          ],
          "bridge_terms": [
            "external",
            "status"
          ],
          "questions": [
            "Which bounded commands connect meta_loop outputs to meta_harness decisions?",
            "Which artifact should become the canonical bridge between meta_loop and meta_harness?"
          ],
          "recommended_artifacts": [
            "contracts/parent-capability-metrics.yaml",
            "evaluation/tool-health/status.json",
            "evaluation/infranodus-gap-analysis.json"
          ]
        }
      ],
      "limitations": [
        "Live InfraNodus MCP analysis remains API/OAuth-bound and no local runtime credential or session configuration was present in this run.",
        "This bounded substitute reports graph structure honestly but does not claim live InfraNodus MCP output."
      ]
    },
    "local_runner_capabilities": {
      "harvest_id": "PARENT-LOCAL-RUNNERS-0001",
      "created_at": "2026-05-20",
      "scope": "portable_parent_wrapper",
      "doctrine": "cli_first_local_runners",
      "metrics_contract": "contracts/parent-capability-metrics.yaml",
      "families": [
        {
          "id": "claude_code",
          "label": "Claude Code",
          "status": "available",
          "matched_probe": "claude --version",
          "command_path": "/Users/ojeromyo/.local/bin/claude",
          "summary": "2.1.144 (Claude Code)",
          "duration_ms": 46.56,
          "probes": [
            {
              "command": "claude --version",
              "command_path": "/Users/ojeromyo/.local/bin/claude",
              "status": "pass",
              "exit_code": 0,
              "duration_ms": 46.56,
              "summary": "2.1.144 (Claude Code)"
            }
          ]
        },
        {
          "id": "copilot",
          "label": "Copilot",
          "status": "available",
          "matched_probe": "gh copilot --help",
          "command_path": "/opt/homebrew/bin/gh",
          "summary": "gh version 2.92.0 (2026-04-28)",
          "duration_ms": 26.36,
          "probes": [
            {
              "command": "gh copilot --help",
              "command_path": "/opt/homebrew/bin/gh",
              "status": "pass",
              "exit_code": 0,
              "duration_ms": 26.36,
              "summary": "Runs the GitHub Copilot CLI."
            }
          ]
        },
        {
          "id": "codex",
          "label": "Codex",
          "status": "available",
          "matched_probe": "codex --version",
          "command_path": "/opt/homebrew/bin/codex",
          "summary": "codex-cli 0.130.0",
          "duration_ms": 11.55,
          "probes": [
            {
              "command": "codex --version",
              "command_path": "/opt/homebrew/bin/codex",
              "status": "pass",
              "exit_code": 0,
              "duration_ms": 11.55,
              "summary": "codex-cli 0.130.0"
            }
          ]
        },
        {
          "id": "pi",
          "label": "PI",
          "status": "available",
          "matched_probe": "pi --version",
          "command_path": "/Users/ojeromyo/.bun/bin/pi",
          "summary": "0.72.1",
          "duration_ms": 437.53,
          "probes": [
            {
              "command": "pi --version",
              "command_path": "/Users/ojeromyo/.bun/bin/pi",
              "status": "pass",
              "exit_code": 0,
              "duration_ms": 437.53,
              "summary": "0.72.1"
            }
          ]
        },
        {
          "id": "hermes_agent",
          "label": "Hermes agent",
          "status": "available",
          "matched_probe": "hermes --version",
          "command_path": "/Users/ojeromyo/.local/bin/hermes",
          "summary": "Hermes Agent v0.14.0 (2026.5.16)",
          "duration_ms": 243.38,
          "probes": [
            {
              "command": "hermes --version",
              "command_path": "/Users/ojeromyo/.local/bin/hermes",
              "status": "pass",
              "exit_code": 0,
              "duration_ms": 243.38,
              "summary": "Hermes Agent v0.14.0 (2026.5.16)"
            }
          ]
        },
        {
          "id": "llama",
          "label": "Llama",
          "status": "available",
          "matched_probe": "ollama --version",
          "command_path": "/usr/local/bin/ollama",
          "summary": "ollama version is 0.24.0",
          "duration_ms": 17.17,
          "probes": [
            {
              "command": "llama --version",
              "command_path": null,
              "status": "missing",
              "exit_code": null,
              "duration_ms": 0,
              "summary": "llama is not installed"
            },
            {
              "command": "ollama --version",
              "command_path": "/usr/local/bin/ollama",
              "status": "pass",
              "exit_code": 0,
              "duration_ms": 17.17,
              "summary": "ollama version is 0.24.0"
            },
            {
              "command": "llama-server --version",
              "command_path": "/opt/homebrew/bin/llama-server",
              "status": "pass",
              "exit_code": 0,
              "duration_ms": 8698.67,
              "summary": "load_backend: loaded BLAS backend from /opt/homebrew/Cellar/ggml/0.12.0/libexec/libggml-blas.so"
            }
          ]
        },
        {
          "id": "mlx",
          "label": "MLX",
          "status": "available",
          "matched_probe": "mlx_lm --help",
          "command_path": "/Users/ojeromyo/.local/bin/mlx_lm",
          "summary": "The supported subcommands are ('benchmark', 'cache_prompt', 'chat', 'convert', 'evaluate', 'fuse', 'generate', 'lora', 'manage', 'perplexity', 'awq', 'dwq', 'dynamic_quant', 'gptq', 'server', 'upload', 'share')",
          "duration_ms": 1307.72,
          "probes": [
            {
              "command": "mlx_lm --help",
              "command_path": "/Users/ojeromyo/.local/bin/mlx_lm",
              "status": "pass",
              "exit_code": 0,
              "duration_ms": 1307.72,
              "summary": "The supported subcommands are ('benchmark', 'cache_prompt', 'chat', 'convert', 'evaluate', 'fuse', 'generate', 'lora', 'manage', 'perplexity', 'awq', 'dwq', 'dynamic_quant', 'gptq', 'server', 'upload', 'share')"
            },
            {
              "command": "mlx --help",
              "command_path": null,
              "status": "missing",
              "exit_code": null,
              "duration_ms": 0,
              "summary": "mlx is not installed"
            }
          ]
        },
        {
          "id": "mlx_vlm",
          "label": "MLX VLM",
          "status": "missing",
          "matched_probe": null,
          "command_path": null,
          "summary": "mlx_vlm is not installed",
          "duration_ms": 0,
          "probes": [
            {
              "command": "mlx_vlm --help",
              "command_path": null,
              "status": "missing",
              "exit_code": null,
              "duration_ms": 0,
              "summary": "mlx_vlm is not installed"
            }
          ]
        }
      ],
      "summary": {
        "available_count": 7,
        "missing_count": 1,
        "available": [
          "Claude Code",
          "Copilot",
          "Codex",
          "PI",
          "Hermes agent",
          "Llama",
          "MLX"
        ],
        "missing": [
          "MLX VLM"
        ],
        "baseline_rule": "CLI-first local runner harvests are the default parent evaluation path. Remote-provider lanes are explicit exceptions."
      },
      "remote_exception_lanes": [
        {
          "lane": "vercel-agent-eval",
          "baseline_local_state": "dry plus local runner harvest",
          "remote_exception_requirement": "OPENAI_API_KEY for smoke/live"
        }
      ]
    },
    "readiness": {
      "readiness_id": "PARENT-META-PROMOTION-0001",
      "created_at": "2026-05-20",
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
      "analysis_id": "PARENT-META-INFRANODUS-GAP-0002",
      "created_at": "2026-05-20",
      "scope": "portable_parent_wrapper",
      "method": {
        "mode": "bounded_local_cli_substitute",
        "summary": "Used the governed parent corpus, layer token overlap, and gateway terms as the strongest honest local substitute while live MCP analysis stayed blocked.",
        "limitation": "Live InfraNodus MCP analysis remains API/OAuth-bound and no local runtime credential or session configuration was present in this run."
      },
      "analyzed_layers": [
        {
          "id": "evaluation",
          "label": "evaluation",
          "source_files": [
            "evaluation/README.md",
            "evaluation/metrics-latest.json",
            "evaluation/copilot-ratchet-report.json"
          ],
          "top_terms": [
            "evaluation",
            "tool_health",
            "agent_eval",
            "readme",
            "scripts",
            "cycle",
            "status",
            "true"
          ]
        },
        {
          "id": "meta_loop",
          "label": "meta_loop",
          "source_files": [
            "GOAL.md",
            "program.md",
            "runs/iterations.jsonl"
          ],
          "top_terms": [
            "evaluation",
            "tool_health",
            "status",
            "iterations",
            "external",
            "jsonl",
            "evidence",
            "agent_eval"
          ]
        },
        {
          "id": "autoresearch",
          "label": "autoresearch",
          "source_files": [
            "README.md",
            "program.md",
            "library.yaml"
          ],
          "top_terms": [
            "source",
            "external",
            "name",
            "description",
            "status",
            "evaluation",
            "bounded",
            "tool_health"
          ]
        },
        {
          "id": "meta_harness",
          "label": "meta_harness",
          "source_files": [
            "domain_spec.md",
            "AGENTS.md",
            "MEMORY.md"
          ],
          "top_terms": [
            "status",
            "external",
            "gate_id",
            "notes",
            "doctrine",
            "green",
            "memory",
            "prompt"
          ]
        },
        {
          "id": "agent_eval",
          "label": "agent_eval",
          "source_files": [
            "contracts/agent-eval-parent-lane.yaml",
            "evaluation/agent-eval/README.md",
            "scripts/run-parent-agent-eval.sh"
          ],
          "top_terms": [
            "smoke",
            "agent_eval",
            "evaluation",
            "dry",
            "docker",
            "tool_health",
            "scripts",
            "run-parent-agent_eval"
          ]
        },
        {
          "id": "tool_health",
          "label": "tool_health",
          "source_files": [
            "README.md",
            "evaluation/tool-health/status.json",
            "evaluation/tool-health/local-runners.json"
          ],
          "top_terms": [
            "status",
            "evaluation",
            "summary",
            "tool_health",
            "command_path",
            "duration_ms",
            "command",
            "version"
          ]
        }
      ],
      "likely_missing_adjacent_layer": {
        "id": "tool_health",
        "label": "tool_health",
        "reason": "This layer is present in parent doctrine and evidence, overlaps multiple named layers, and should stay explicit in the improvement map.",
        "evidence": [
          "README.md",
          "evaluation/tool-health/status.json",
          "evaluation/tool-health/local-runners.json"
        ]
      },
      "topical_clusters": [
        "evaluation",
        "meta_loop",
        "autoresearch",
        "meta_harness",
        "agent_eval",
        "tool_health"
      ],
      "content_gaps": [
        "meta_harness -> agent_eval",
        "evaluation -> meta_harness",
        "autoresearch -> agent_eval"
      ],
      "resolved_by": [
        "contracts/parent-capability-metrics.yaml",
        "evaluation/tool-health/local-runners.json",
        "evaluation/tool-health/status.json",
        "scripts/build-parent-infranodus-artifacts.py"
      ],
      "limitations": [
        "Live InfraNodus MCP analysis remains API/OAuth-bound and no local runtime credential or session configuration was present in this run.",
        "This bounded substitute reports graph structure honestly but does not claim live InfraNodus MCP output."
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
        },
        {
          "iteration": 4,
          "cycle_kind": "real_non_dry",
          "before_total_score": 90.62,
          "after_total_score": 100.0,
          "before_outcome_score": 87.5,
          "after_outcome_score": 100.0,
          "before_instrument_score": 100.0,
          "after_instrument_score": 100.0,
          "action": "repair the plateau-weight cap and keep the parent tool-health plus agent-eval documentation wave",
          "result": "kept",
          "validator_status": "pass",
          "changed_files": [
            "AGENTS.md",
            "CLAUDE.md",
            "GOAL.md",
            "GOLDENPATH.md",
            "MEMORY.md",
            "README.md",
            "agentics-library.md",
            "domain_spec.md",
            "evaluation/tool-health/status.json",
            "library.yaml",
            "program.md",
            "scripts/score-parent-wrapper.py",
            "source/README.md"
          ],
          "artifacts": [
            "evaluation/validation-report.json",
            "evaluation/metrics-latest.json",
            "promotion/readiness.json",
            "runs/iterations.jsonl",
            "evaluation/tool-health/status.json"
          ],
          "note": "Fixed the plateau_or_blocker_truth cap to its documented weight, removed stale standalone-state drift, and recorded bounded GitNexus, Graphify, InfraNodus, and agent-eval evidence."
        },
        {
          "iteration": 5,
          "cycle_kind": "real_non_dry",
          "before_total_score": 100.0,
          "after_total_score": 100.0,
          "before_outcome_score": 100.0,
          "after_outcome_score": 100.0,
          "before_instrument_score": 100.0,
          "after_instrument_score": 100.0,
          "action": "test a README-only wording probe and revert it when the repaired metric stays saturated",
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
            "runs/iterations.jsonl",
            "evaluation/tool-health/status.json"
          ],
          "note": "The README-only probe was reverted after the repaired metric stayed at 100.0, proving a bounded saturation blocker for further score-based improvement in this run."
        },
        {
          "iteration": 6,
          "cycle_kind": "real_non_dry",
          "before_total_score": 86.09,
          "after_total_score": 92.84,
          "before_outcome_score": 81.45,
          "after_outcome_score": 90.45,
          "before_instrument_score": 100.0,
          "after_instrument_score": 100.0,
          "action": "add a parent-scoped agent-eval fixture, direct Codex plus Docker smoke contract, and exact dry plus blocker evidence",
          "result": "kept",
          "validator_status": "pass",
          "changed_files": [
            "README.md",
            "GOAL.md",
            "program.md",
            "library.yaml",
            "agentics-library.md",
            "domain_spec.md",
            "contracts/agent-eval-parent-lane.yaml",
            "evaluation/agent-eval/.env.example",
            "evaluation/agent-eval/.gitignore",
            "evaluation/agent-eval/README.md",
            "evaluation/agent-eval/package.json",
            "evaluation/agent-eval/tsconfig.json",
            "evaluation/agent-eval/experiments/parent-wrapper-codex-docker.ts",
            "evaluation/agent-eval/evals/parent-wrapper-agent-eval-boundary/PROMPT.md",
            "evaluation/agent-eval/evals/parent-wrapper-agent-eval-boundary/EVAL.ts",
            "evaluation/agent-eval/evals/parent-wrapper-agent-eval-boundary/package.json",
            "evaluation/agent-eval/evals/parent-wrapper-agent-eval-boundary/README.md",
            "evaluation/agent-eval/evals/parent-wrapper-agent-eval-boundary/GOAL.md",
            "evaluation/agent-eval/evals/parent-wrapper-agent-eval-boundary/program.md",
            "evaluation/agent-eval/evals/parent-wrapper-agent-eval-boundary/library.yaml",
            "evaluation/agent-eval/evals/parent-wrapper-agent-eval-boundary/agentics-library.md",
            "scripts/run-parent-agent-eval.sh",
            "evaluation/tool-health/agent-eval-dry.log",
            "evaluation/tool-health/agent-eval-smoke.log",
            "evaluation/tool-health/status.json",
            "evaluation/copilot-ratchet-report.json",
            "runs/iterations.jsonl"
          ],
          "artifacts": [
            "evaluation/validation-report.json",
            "evaluation/metrics-latest.json",
            "promotion/readiness.json",
            "runs/iterations.jsonl",
            "evaluation/tool-health/status.json"
          ],
          "note": "The parent wrapper now carries a real agent-eval project and the next stronger smoke step is blocked only by OPENAI_API_KEY, not by missing Vercel sandbox credentials."
        },
        {
          "iteration": 7,
          "cycle_kind": "real_non_dry",
          "before_total_score": 92.84,
          "after_total_score": 92.84,
          "before_outcome_score": 90.45,
          "after_outcome_score": 90.45,
          "before_instrument_score": 100.0,
          "after_instrument_score": 100.0,
          "action": "test whether the parent agent-eval lane can honestly rise above dry without OPENAI_API_KEY and reject that promotion when the smoke blocker is real",
          "result": "rejected",
          "validator_status": "pass",
          "changed_files": [
            "evaluation/tool-health/agent-eval-smoke.log",
            "evaluation/tool-health/status.json",
            "evaluation/copilot-ratchet-report.json",
            "runs/iterations.jsonl"
          ],
          "artifacts": [
            "evaluation/validation-report.json",
            "evaluation/metrics-latest.json",
            "promotion/readiness.json",
            "runs/iterations.jsonl",
            "evaluation/tool-health/status.json"
          ],
          "note": "The smoke lane stayed blocked because Docker was present but OPENAI_API_KEY was not configured, so the run kept the stronger claim rejected instead of faking smoke success."
        },
        {
          "iteration": 8,
          "cycle_kind": "real_non_dry",
          "before_total_score": 89.84,
          "after_total_score": 91.3,
          "before_outcome_score": 86.45,
          "after_outcome_score": 88.4,
          "before_instrument_score": 100.0,
          "after_instrument_score": 100.0,
          "action": "replace paid-key-first doctrine with CLI-first local runner harvests, add the reusable parent metrics contract, and keep a bounded InfraNodus substitute with durable gap, bridge, and research artifacts",
          "result": "kept",
          "validator_status": "pass",
          "changed_files": [
            "AGENTS.md",
            "CLAUDE.md",
            "GOAL.md",
            "GOLDENPATH.md",
            "MEMORY.md",
            "README.md",
            "agentics-library.md",
            "contracts/README.md",
            "contracts/agent-eval-parent-lane.yaml",
            "contracts/parent-capability-metrics.yaml",
            "domain_spec.md",
            "evaluation/README.md",
            "evaluation/agent-eval/README.md",
            "evaluation/dashboard-data.js",
            "evaluation/dashboard-data.json",
            "evaluation/infranodus-conceptual-bridges.json",
            "evaluation/infranodus-entity-graph.json",
            "evaluation/infranodus-gap-analysis.json",
            "evaluation/infranodus-live-summary.json",
            "evaluation/infranodus-parent-corpus.txt",
            "evaluation/infranodus-research-topics.json",
            "evaluation/metrics-latest.json",
            "evaluation/tool-health/infranodus-live-probe.json",
            "evaluation/tool-health/local-runners.json",
            "evaluation/tool-health/status.json",
            "evaluation/validation-report.json",
            "examples/capability-harvest-metrics.invalid.docs-only.json",
            "examples/capability-harvest-metrics.valid.json",
            "expected-failures/registry.yaml",
            "library.yaml",
            "program.md",
            "schemas/README.md",
            "schemas/capability-harvest-metrics.schema.json",
            "scripts/build-parent-infranodus-artifacts.py",
            "scripts/build-visualization-artifacts.py",
            "scripts/harvest-local-runner-capabilities.py",
            "scripts/refresh-parent-tool-health.py",
            "scripts/run-parent-agent-eval.sh",
            "scripts/score-parent-wrapper.py",
            "tests/validate_parent_wrapper_contract.py"
          ],
          "artifacts": [
            "evaluation/validation-report.json",
            "evaluation/metrics-latest.json",
            "promotion/readiness.json",
            "runs/iterations.jsonl",
            "evaluation/tool-health/status.json",
            "evaluation/tool-health/local-runners.json",
            "evaluation/infranodus-gap-analysis.json",
            "evaluation/infranodus-conceptual-bridges.json",
            "evaluation/infranodus-research-topics.json"
          ],
          "note": "The parent wrapper now defaults to CLI-first local runner evidence, carries a reusable anti-gaming metrics contract, and emits bounded InfraNodus substitute artifacts without claiming live MCP output."
        },
        {
          "iteration": 9,
          "cycle_kind": "real_non_dry",
          "before_total_score": 91.3,
          "after_total_score": 91.3,
          "before_outcome_score": 88.4,
          "after_outcome_score": 88.4,
          "before_instrument_score": 100.0,
          "after_instrument_score": 100.0,
          "action": "probe live InfraNodus MCP escalation and reject the promotion when runtime credential or session configuration is absent",
          "result": "rejected",
          "validator_status": "pass",
          "changed_files": [
            "evaluation/tool-health/infranodus-live-probe.json",
            "evaluation/tool-health/status.json",
            "evaluation/copilot-ratchet-report.json",
            "runs/iterations.jsonl"
          ],
          "artifacts": [
            "evaluation/validation-report.json",
            "evaluation/metrics-latest.json",
            "promotion/readiness.json",
            "runs/iterations.jsonl",
            "evaluation/tool-health/status.json",
            "evaluation/tool-health/infranodus-live-probe.json"
          ],
          "note": "The run kept the bounded local substitute and rejected a fake live claim because no InfraNodus MCP runtime credential or session configuration was present."
        },
        {
          "iteration": 10,
          "cycle_kind": "real_non_dry",
          "before_total_score": 95.05,
          "after_total_score": 97.56,
          "before_outcome_score": 93.4,
          "after_outcome_score": 96.75,
          "before_instrument_score": 100.0,
          "after_instrument_score": 100.0,
          "action": "demote Graphify to bounded_pass, add validator-backed tool-health truth boundaries, and refresh bounded GitNexus, Graphify, and InfraNodus evidence",
          "result": "kept",
          "validator_status": "pass",
          "changed_files": [
            "scripts/refresh-parent-tool-health.py",
            "tests/validate_parent_wrapper_contract.py",
            "evaluation/tool-health/gitnexus-smoke.log",
            "evaluation/tool-health/gitnexus-parent-fixture/gitnexus-clean-smoke.log",
            "evaluation/tool-health/graphify-smoke.log",
            "evaluation/tool-health/infranodus-live-probe.json",
            "evaluation/tool-health/status.json",
            "evaluation/infranodus-gap-analysis.json",
            "evaluation/infranodus-conceptual-bridges.json",
            "evaluation/infranodus-research-topics.json",
            "evaluation/infranodus-live-summary.json",
            "evaluation/infranodus-parent-corpus.txt",
            "evaluation/infranodus-entity-graph.json",
            "evaluation/dashboard-data.json",
            "evaluation/dashboard-data.js",
            "evaluation/validation-report.json",
            "evaluation/metrics-latest.json",
            "promotion/readiness.json",
            "evaluation/copilot-ratchet-report.json",
            "runs/iterations.jsonl"
          ],
          "artifacts": [
            "evaluation/validation-report.json",
            "evaluation/metrics-latest.json",
            "promotion/readiness.json",
            "runs/iterations.jsonl",
            "evaluation/tool-health/status.json",
            "evaluation/tool-health/infranodus-live-probe.json",
            "evaluation/infranodus-gap-analysis.json",
            "evaluation/infranodus-conceptual-bridges.json",
            "evaluation/infranodus-research-topics.json",
            "evaluation/dashboard-data.json",
            "evaluation/dashboard-data.js",
            "evaluation/infranodus-entity-graph.json"
          ],
          "note": "Graphify now reports only bounded fixture truth, GitNexus and InfraNodus expose explicit truth_boundary fields, and the live InfraNodus lane remains visibly blocked."
        }
      ],
      "legacy_rows": [],
      "real_count": 10,
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
        "id": "cluster_evaluation",
        "name": "evaluation",
        "group": "cluster",
        "color": "#f59e0b",
        "val": 10,
        "meta": {}
      },
      {
        "id": "cluster_meta_loop",
        "name": "meta_loop",
        "group": "cluster",
        "color": "#f59e0b",
        "val": 10,
        "meta": {}
      },
      {
        "id": "cluster_autoresearch",
        "name": "autoresearch",
        "group": "cluster",
        "color": "#f59e0b",
        "val": 10,
        "meta": {}
      },
      {
        "id": "cluster_meta_harness",
        "name": "meta_harness",
        "group": "cluster",
        "color": "#f59e0b",
        "val": 10,
        "meta": {}
      },
      {
        "id": "cluster_agent_eval",
        "name": "agent_eval",
        "group": "cluster",
        "color": "#f59e0b",
        "val": 10,
        "meta": {}
      },
      {
        "id": "cluster_tool_health",
        "name": "tool_health",
        "group": "cluster",
        "color": "#f59e0b",
        "val": 10,
        "meta": {}
      },
      {
        "id": "resolver_contracts_parent_capability_metrics_yaml",
        "name": "contracts/parent-capability-metrics.yaml",
        "group": "resolver",
        "color": "#16a34a",
        "val": 7,
        "meta": {}
      },
      {
        "id": "resolver_evaluation_tool_health_local_runners_json",
        "name": "evaluation/tool-health/local-runners.json",
        "group": "resolver",
        "color": "#16a34a",
        "val": 7,
        "meta": {}
      },
      {
        "id": "resolver_evaluation_tool_health_status_json",
        "name": "evaluation/tool-health/status.json",
        "group": "resolver",
        "color": "#16a34a",
        "val": 7,
        "meta": {}
      },
      {
        "id": "resolver_scripts_build_parent_infranodus_artifacts_py",
        "name": "scripts/build-parent-infranodus-artifacts.py",
        "group": "resolver",
        "color": "#16a34a",
        "val": 7,
        "meta": {}
      },
      {
        "id": "live_cluster_1",
        "name": "evaluation",
        "group": "live_cluster",
        "color": "#f97316",
        "val": 32.75,
        "meta": {
          "size_pct": 13,
          "influence_pct": 99
        }
      },
      {
        "id": "live_cluster_2",
        "name": "meta_loop",
        "group": "live_cluster",
        "color": "#f97316",
        "val": 32.75,
        "meta": {
          "size_pct": 34,
          "influence_pct": 99
        }
      },
      {
        "id": "live_cluster_3",
        "name": "autoresearch",
        "group": "live_cluster",
        "color": "#f97316",
        "val": 32.75,
        "meta": {
          "size_pct": 20,
          "influence_pct": 99
        }
      },
      {
        "id": "live_cluster_4",
        "name": "meta_harness",
        "group": "live_cluster",
        "color": "#f97316",
        "val": 32.75,
        "meta": {
          "size_pct": 12,
          "influence_pct": 99
        }
      },
      {
        "id": "live_cluster_5",
        "name": "agent_eval",
        "group": "live_cluster",
        "color": "#f97316",
        "val": 32.75,
        "meta": {
          "size_pct": 5,
          "influence_pct": 99
        }
      },
      {
        "id": "live_cluster_6",
        "name": "tool_health",
        "group": "live_cluster",
        "color": "#f97316",
        "val": 32.75,
        "meta": {
          "size_pct": 16,
          "influence_pct": 99
        }
      },
      {
        "id": "live_concept_evaluation",
        "name": "evaluation",
        "group": "live_concept",
        "color": "#a855f7",
        "val": 7,
        "meta": {}
      },
      {
        "id": "live_concept_status",
        "name": "status",
        "group": "live_concept",
        "color": "#a855f7",
        "val": 7,
        "meta": {}
      },
      {
        "id": "live_concept_tool_health",
        "name": "tool_health",
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
        "id": "live_concept_agent_eval",
        "name": "agent_eval",
        "group": "live_concept",
        "color": "#a855f7",
        "val": 7,
        "meta": {}
      },
      {
        "id": "live_concept_evidence",
        "name": "evidence",
        "group": "live_concept",
        "color": "#a855f7",
        "val": 7,
        "meta": {}
      },
      {
        "id": "live_concept_readme",
        "name": "readme",
        "group": "live_concept",
        "color": "#a855f7",
        "val": 7,
        "meta": {}
      },
      {
        "id": "live_concept_scripts",
        "name": "scripts",
        "group": "live_concept",
        "color": "#a855f7",
        "val": 7,
        "meta": {}
      },
      {
        "id": "live_concept_bounded",
        "name": "bounded",
        "group": "live_concept",
        "color": "#a855f7",
        "val": 7,
        "meta": {}
      },
      {
        "id": "live_concept_gate_id",
        "name": "gate_id",
        "group": "live_concept",
        "color": "#a855f7",
        "val": 7,
        "meta": {}
      },
      {
        "id": "live_concept_notes",
        "name": "notes",
        "group": "live_concept",
        "color": "#a855f7",
        "val": 7,
        "meta": {}
      },
      {
        "id": "live_concept_program",
        "name": "program",
        "group": "live_concept",
        "color": "#a855f7",
        "val": 7,
        "meta": {}
      },
      {
        "id": "live_gateway_evaluation",
        "name": "evaluation",
        "group": "gateway",
        "color": "#ec4899",
        "val": 8,
        "meta": {}
      },
      {
        "id": "live_gateway_status",
        "name": "status",
        "group": "gateway",
        "color": "#ec4899",
        "val": 8,
        "meta": {}
      },
      {
        "id": "live_gateway_tool_health",
        "name": "tool_health",
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
        "id": "live_gateway_agent_eval",
        "name": "agent_eval",
        "group": "gateway",
        "color": "#ec4899",
        "val": 8,
        "meta": {}
      },
      {
        "id": "live_gateway_evidence",
        "name": "evidence",
        "group": "gateway",
        "color": "#ec4899",
        "val": 8,
        "meta": {}
      },
      {
        "id": "live_gateway_readme",
        "name": "readme",
        "group": "gateway",
        "color": "#ec4899",
        "val": 8,
        "meta": {}
      },
      {
        "id": "live_gateway_scripts",
        "name": "scripts",
        "group": "gateway",
        "color": "#ec4899",
        "val": 8,
        "meta": {}
      },
      {
        "id": "influential_evaluation",
        "name": "evaluation",
        "group": "influential_node",
        "color": "#ef4444",
        "val": 12.5,
        "meta": {
          "bc": 0.833,
          "degree": 5
        }
      },
      {
        "id": "influential_status",
        "name": "status",
        "group": "influential_node",
        "color": "#ef4444",
        "val": 12.5,
        "meta": {
          "bc": 0.833,
          "degree": 5
        }
      },
      {
        "id": "influential_tool_health",
        "name": "tool_health",
        "group": "influential_node",
        "color": "#ef4444",
        "val": 12.5,
        "meta": {
          "bc": 0.833,
          "degree": 5
        }
      },
      {
        "id": "influential_external",
        "name": "external",
        "group": "influential_node",
        "color": "#ef4444",
        "val": 11.5,
        "meta": {
          "bc": 0.5,
          "degree": 3
        }
      },
      {
        "id": "influential_agent_eval",
        "name": "agent_eval",
        "group": "influential_node",
        "color": "#ef4444",
        "val": 12.0,
        "meta": {
          "bc": 0.667,
          "degree": 4
        }
      },
      {
        "id": "influential_evidence",
        "name": "evidence",
        "group": "influential_node",
        "color": "#ef4444",
        "val": 11.0,
        "meta": {
          "bc": 0.333,
          "degree": 2
        }
      },
      {
        "id": "influential_readme",
        "name": "readme",
        "group": "influential_node",
        "color": "#ef4444",
        "val": 11.0,
        "meta": {
          "bc": 0.333,
          "degree": 2
        }
      },
      {
        "id": "influential_scripts",
        "name": "scripts",
        "group": "influential_node",
        "color": "#ef4444",
        "val": 11.0,
        "meta": {
          "bc": 0.333,
          "degree": 2
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
        "id": "weakest_artifact_refresh",
        "name": "artifact_refresh",
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
        "id": "check_capability_metrics_contract",
        "name": "capability_metrics_contract",
        "group": "validation_check",
        "color": "#16a34a",
        "val": 6,
        "meta": {}
      },
      {
        "id": "check_tool_health_truth_boundaries",
        "name": "tool_health_truth_boundaries",
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
        "target": "cluster_evaluation",
        "relation": "cluster",
        "color": "#f59e0b",
        "width": 1.5
      },
      {
        "source": "parent_meta_wrapper",
        "target": "cluster_meta_loop",
        "relation": "cluster",
        "color": "#f59e0b",
        "width": 1.5
      },
      {
        "source": "parent_meta_wrapper",
        "target": "cluster_autoresearch",
        "relation": "cluster",
        "color": "#f59e0b",
        "width": 1.5
      },
      {
        "source": "parent_meta_wrapper",
        "target": "cluster_meta_harness",
        "relation": "cluster",
        "color": "#f59e0b",
        "width": 1.5
      },
      {
        "source": "parent_meta_wrapper",
        "target": "cluster_agent_eval",
        "relation": "cluster",
        "color": "#f59e0b",
        "width": 1.5
      },
      {
        "source": "parent_meta_wrapper",
        "target": "cluster_tool_health",
        "relation": "cluster",
        "color": "#f59e0b",
        "width": 1.5
      },
      {
        "source": "cluster_meta_harness",
        "target": "cluster_agent_eval",
        "relation": "content_gap",
        "color": "#dc2626",
        "width": 4
      },
      {
        "source": "cluster_evaluation",
        "target": "cluster_meta_harness",
        "relation": "content_gap",
        "color": "#dc2626",
        "width": 4
      },
      {
        "source": "cluster_autoresearch",
        "target": "cluster_agent_eval",
        "relation": "content_gap",
        "color": "#dc2626",
        "width": 4
      },
      {
        "source": "parent_meta_wrapper",
        "target": "resolver_contracts_parent_capability_metrics_yaml",
        "relation": "resolved_by",
        "color": "#16a34a",
        "width": 1
      },
      {
        "source": "parent_meta_wrapper",
        "target": "resolver_evaluation_tool_health_local_runners_json",
        "relation": "resolved_by",
        "color": "#16a34a",
        "width": 1
      },
      {
        "source": "parent_meta_wrapper",
        "target": "resolver_evaluation_tool_health_status_json",
        "relation": "resolved_by",
        "color": "#16a34a",
        "width": 1
      },
      {
        "source": "parent_meta_wrapper",
        "target": "resolver_scripts_build_parent_infranodus_artifacts_py",
        "relation": "resolved_by",
        "color": "#16a34a",
        "width": 1
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
        "target": "live_cluster_2",
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
        "target": "live_cluster_4",
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
        "target": "live_cluster_6",
        "relation": "infranodus_cluster",
        "color": "#f97316",
        "width": 1.5
      },
      {
        "source": "parent_meta_wrapper",
        "target": "live_concept_evaluation",
        "relation": "main_concept",
        "color": "#a855f7",
        "width": 1
      },
      {
        "source": "parent_meta_wrapper",
        "target": "live_concept_status",
        "relation": "main_concept",
        "color": "#a855f7",
        "width": 1
      },
      {
        "source": "parent_meta_wrapper",
        "target": "live_concept_tool_health",
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
        "target": "live_concept_agent_eval",
        "relation": "main_concept",
        "color": "#a855f7",
        "width": 1
      },
      {
        "source": "parent_meta_wrapper",
        "target": "live_concept_evidence",
        "relation": "main_concept",
        "color": "#a855f7",
        "width": 1
      },
      {
        "source": "parent_meta_wrapper",
        "target": "live_concept_readme",
        "relation": "main_concept",
        "color": "#a855f7",
        "width": 1
      },
      {
        "source": "parent_meta_wrapper",
        "target": "live_concept_scripts",
        "relation": "main_concept",
        "color": "#a855f7",
        "width": 1
      },
      {
        "source": "parent_meta_wrapper",
        "target": "live_concept_bounded",
        "relation": "main_concept",
        "color": "#a855f7",
        "width": 1
      },
      {
        "source": "parent_meta_wrapper",
        "target": "live_concept_gate_id",
        "relation": "main_concept",
        "color": "#a855f7",
        "width": 1
      },
      {
        "source": "parent_meta_wrapper",
        "target": "live_concept_notes",
        "relation": "main_concept",
        "color": "#a855f7",
        "width": 1
      },
      {
        "source": "parent_meta_wrapper",
        "target": "live_concept_program",
        "relation": "main_concept",
        "color": "#a855f7",
        "width": 1
      },
      {
        "source": "parent_meta_wrapper",
        "target": "live_gateway_evaluation",
        "relation": "gateway",
        "color": "#ec4899",
        "width": 1.2
      },
      {
        "source": "parent_meta_wrapper",
        "target": "live_gateway_status",
        "relation": "gateway",
        "color": "#ec4899",
        "width": 1.2
      },
      {
        "source": "parent_meta_wrapper",
        "target": "live_gateway_tool_health",
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
        "source": "parent_meta_wrapper",
        "target": "live_gateway_agent_eval",
        "relation": "gateway",
        "color": "#ec4899",
        "width": 1.2
      },
      {
        "source": "parent_meta_wrapper",
        "target": "live_gateway_evidence",
        "relation": "gateway",
        "color": "#ec4899",
        "width": 1.2
      },
      {
        "source": "parent_meta_wrapper",
        "target": "live_gateway_readme",
        "relation": "gateway",
        "color": "#ec4899",
        "width": 1.2
      },
      {
        "source": "parent_meta_wrapper",
        "target": "live_gateway_scripts",
        "relation": "gateway",
        "color": "#ec4899",
        "width": 1.2
      },
      {
        "source": "metrics_latest",
        "target": "influential_evaluation",
        "relation": "influential_node",
        "color": "#ef4444",
        "width": 2
      },
      {
        "source": "metrics_latest",
        "target": "influential_status",
        "relation": "influential_node",
        "color": "#ef4444",
        "width": 2
      },
      {
        "source": "metrics_latest",
        "target": "influential_tool_health",
        "relation": "influential_node",
        "color": "#ef4444",
        "width": 2
      },
      {
        "source": "metrics_latest",
        "target": "influential_external",
        "relation": "influential_node",
        "color": "#ef4444",
        "width": 2
      },
      {
        "source": "metrics_latest",
        "target": "influential_agent_eval",
        "relation": "influential_node",
        "color": "#ef4444",
        "width": 2
      },
      {
        "source": "metrics_latest",
        "target": "influential_evidence",
        "relation": "influential_node",
        "color": "#ef4444",
        "width": 2
      },
      {
        "source": "metrics_latest",
        "target": "influential_readme",
        "relation": "influential_node",
        "color": "#ef4444",
        "width": 2
      },
      {
        "source": "metrics_latest",
        "target": "influential_scripts",
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
        "target": "weakest_artifact_refresh",
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
        "target": "check_capability_metrics_contract",
        "relation": "pass",
        "color": "#16a34a",
        "width": 1
      },
      {
        "source": "validation_report",
        "target": "check_tool_health_truth_boundaries",
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
