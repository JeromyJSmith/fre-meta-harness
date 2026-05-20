# 🤖 Copilot CLI Session

> [!NOTE]
> - **Session ID:** `58404b62-b6fb-4eb9-a30f-8cf0ce2415f0`  
> - **Started:** 5/18/2026, 9:32:07 AM  
> - **Duration:** 37s  
> - **Exported:** 5/18/2026, 9:32:44 AM  

---

<sub>⏱️ 3s</sub>

### 👤 User

# Parent Wrapper Copilot Ratchet Prompt

Treat this as one continuous autonomous heavy run on the parent Meta-Harness
wrapper only.

Mission:

- run a real non-dry parent-wrapper ratchet
- validate everything
- challenge the metric if it is saturated or too binary
- keep looping until genuine plateau or an exact blocker

Current verified state:

- parent wrapper root: `/Volumes/PixelTable/VW_iTwin_Bridge/meta`
- scaffold exists: `README.md`, `AGENTS.md`, `CLAUDE.md`, `GOAL.md`,
  `GOLDENPATH.md`, `MEMORY.md`
- governed prompt contract exists
- InfraNodus phase-tool map exists
- parent validator currently passes
- current scorer reports `total_score=100.0`
- that `100.0` may be suspiciously saturated and must not be trusted blindly
- a dry-run iteration row exists, but no real non-dry ratchet has been proven

Hard rules:

- use `uv` for all Python execution
- do not broaden beyond `/Volumes/PixelTable/VW_iTwin_Bridge/meta`
- do not use a dry run as proof
- do not stop after one real cycle unless an exact blocker is proven
- if the score is saturated or gameable, treat that as an instrument problem
  and repair the scorer first
- no fake green states

Read first:

- `/Volumes/PixelTable/VW_iTwin_Bridge/meta/GOAL.md`
- `/Volumes/PixelTable/VW_iTwin_Bridge/meta/domain_spec.md`
- `/Volumes/PixelTable/VW_iTwin_Bridge/meta/library.yaml`
- `/Volumes/PixelTable/VW_iTwin_Bridge/meta/agent-heavy-run-prompt-schema.md`
- `/Volumes/PixelTable/VW_iTwin_Bridge/meta/infranodus-phase-tool-map.json`
- `/Volumes/PixelTable/VW_iTwin_Bridge/meta/tests/validate_parent_wrapper_contract.py`
- `/Volumes/PixelTable/VW_iTwin_Bridge/meta/scripts/score-parent-wrapper.py`
- `/Volumes/PixelTable/VW_iTwin_Bridge/meta/scripts/run-parent-ratchet.sh`

Tasks:

1. Capture the true baseline by running the validator and scorer.
2. Decide whether `total_score=100.0` is trustworthy. If not, improve the
   metric first.
3. Run a real non-dry ratchet cycle.
4. If the metric was repaired or the score improved, run additional non-dry
   cycles.
5. Stop only after 2 consecutive non-improving real cycles with a trustworthy
   metric, or after proving an exact blocker.
6. Refresh:
   - validation report
   - metrics artifact
   - promotion readiness artifact
   - iteration ledger

Validation loop:

- `uv run --isolated --with jsonschema --with pyyaml python /Volumes/PixelTable/VW_iTwin_Bridge/meta/tests/validate_parent_wrapper_contract.py`
- `uv run --isolated --with jsonschema --with pyyaml python /Volumes/PixelTable/VW_iTwin_Bridge/meta/scripts/score-parent-wrapper.py --json`
- `bash /Volumes/PixelTable/VW_iTwin_Bridge/meta/scripts/run-parent-ratchet.sh`
- `bash scripts/pre-commit-docs-check.sh` from `/Volumes/PixelTable/VW_iTWIN_Bridge/VW_iTwin_Bridge` if needed

Report at end:

1. pass or blocked
2. whether the original metric was accepted or repaired
3. number of real non-dry cycles executed
4. before and after scores
5. files changed
6. fresh artifact paths
7. iteration ledger entries appended

---

<sub>⏱️ 8s</sub>

### ✅ `view`

**view the file at /Volumes/PixelTable/VW_iTwin_Bridge/meta.**

/Volumes/PixelTable/VW_iTwin_Bridge/meta

<details>
<summary>43 lines</summary>

```
.DS_Store
AGENTS.md
CLAUDE.md
FEATURE_BACKLOG.md
GOAL.md
GOLDENPATH.md
MEMORY.md
README.md
agent-heavy-run-prompt-index.md
agent-heavy-run-prompt-schema.md
agent-heavy-run-prompt.schema.json
agent-heavy-run-prompt.template.yaml
agentics-library.md
body-registry.yaml
bootstrap.md
cache
config.yaml
contracts
copilot-prompting-playbook.md
docs
domain_spec.md
evaluation
evidence
examples
expected-failures
gold-goals.md
graph
inbox
infranodus-phase-tool-map.json
library.yaml
memory
meta-repomix.xml
metaharness.lock.yaml
outbox
pixeltable-operational-substrate.md
promotion
prompts
relationships
runs
schemas
scripts
source
tests
```

</details>


---

<sub>⏱️ 8s</sub>

### ✅ `view`

**view the file at /Volumes/PixelTable/VW_iTwin_Bridge/meta/GOAL.md.**

/Volumes/PixelTable/VW_iTwin_Bridge/meta/GOAL.md

<details>
<summary>292 lines</summary>

````
1. ---
2. id: "parent-meta-goal"
3. slug: "parent-meta-goal"
4. doctype: "goal"
5. status: "active"
6. version: "1.1.0"
7. owner: "meta-harness"
8. scope: "portable_parent_wrapper"
9. library_refs:
10.   - "library.yaml"
11. prompt_contract_refs:
12.   - "agent-heavy-run-prompt-index.md"
13.   - "agent-heavy-run-prompt-schema.md"
14.   - "agent-heavy-run-prompt.schema.json"
15.   - "agent-heavy-run-prompt.template.yaml"
16.   - "copilot-prompting-playbook.md"
17. comparison_refs:
18.   - "infranodus-phase-tool-map.json"
19. substrate_refs:
20.   - "pixeltable-operational-substrate.md"
21. upstream_refs:
22.   - "https://github.com/jmilinovich/goal-md"
23.   - "https://github.com/stanford-iris-lab/meta-harness"
24.   - "https://github.com/trevin-creator/autoresearch-mlx"
25. ---
26. 
27. # GOAL.md
28. 
29. ## Goal
30. 
31. Improve the parent Meta-Harness wrapper until it becomes a portable,
32. evidence-backed outer loop that can:
33. 
34. 1. identify and govern child body cells
35. 2. carry the reusable contract scaffold
36. 3. carry the governed prompt contract
37. 4. use InfraNodus for diagnosis at every lifecycle gate
38. 5. bind durable evidence to Pixeltable-facing substrate surfaces
39. 6. emit measurable improvement artifacts over repeated iterations
40. 
41. ## Fitness Function
42. 
43. Run this to get the current parent-wrapper score:
44. 
45. ```bash
46. uv run --isolated --with jsonschema --with pyyaml python /Volumes/PixelTable/VW_iTwin_Bridge/meta/scripts/score-parent-wrapper.py --json
47. ```
48. 
49. ### Metric Definition
50. 
51. This is a **split** score:
52. 
53. ```text
54. outcome_score =
55.   scaffold_contract
56. + prompt_contract
57. + proof_package
58. + substrate_and_comparison
59. + iteration_layer
60. 
61. instrument_score =
62.   validator_health
63. + example_truth
64. + gap_analysis_freshness
65. 
66. total_score = 0.75 * outcome_score + 0.25 * instrument_score
67. ```
68. 
69. | Component | Weight | What it measures |
70. |---|---:|---|
71. | `scaffold_contract` | 20 | Required root Markdown scaffold exists and is contract-shaped |
72. | `prompt_contract` | 15 | Governed prompt-schema/playbook set exists and is wired |
73. | `proof_package` | 20 | `source/schema/examples/expected-failures/tests/evaluation/promotion` all exist |
74. | `substrate_and_comparison` | 20 | Pixeltable substrate and InfraNodus phase-map are present and referenced |
75. | `iteration_layer` | 25 | Goal loop, scoring script, domain spec, iteration log, and ratchet runner exist |
76. | `validator_health` | 40 | Parent validator passes end-to-end |
77. | `example_truth` | 30 | Valid examples pass and invalid examples fail for the right reason |
78. | `gap_analysis_freshness` | 30 | InfraNodus gap artifact exists and the missing joins are reflected in the wrapper |
79. 
80. ### Metric Mutability
81. 
82. - [ ] **Locked**
83. - [x] **Split**
84. - [ ] **Open**
85. 
86. The agent may improve the measuring instrument, but it may not silently loosen
87. the definition of "portable parent wrapper readiness."
88. 
89. ## Operating Mode
90. 
91. - [x] **Converge**
92. - [ ] **Continuous**
93. - [ ] **Supervised**
94. 
95. ### Stopping Conditions
96. 
97. Stop and report when ANY of:
98. 
99. - `total_score >= 95`
100. - `instrument_score < 80` after a proposal attempt
101. - `3` consecutive iterations show no improvement
102. - InfraNodus comparison, validator, or substrate references become unavailable
103. 
104. ## Bootstrap
105. 
106. 1. Confirm the active child body in `body-registry.yaml`.
107. 2. Read `domain_spec.md`.
108. 3. Read `library.yaml`, `agent-heavy-run-prompt-schema.md`, and
109.    `infranodus-phase-tool-map.json`.
110. 4. Run the parent validator:
111.    ```bash
112.    uv run --isolated --with jsonschema --with pyyaml python /Volumes/PixelTable/VW_iTwin_Bridge/meta/tests/validate_parent_wrapper_contract.py
113.    ```
114. 5. Record the baseline:
115.    ```bash
116.    uv run --isolated --with jsonschema --with pyyaml python /Volumes/PixelTable/VW_iTwin_Bridge/meta/scripts/score-parent-wrapper.py --json
117.    ```
118. 
119. ## Improvement Loop
120. 
121. The loop follows the Stanford Meta-Harness requirement that a new domain first
122. has a concrete `domain_spec.md`, and the Apple Silicon autoresearch-mlx rule
123. that the loop should hold a fixed artifact, fixed metric, fixed budget, and
124. keep-or-revert discipline.
125. 
126. ```text
127. repeat:
128.   0. Read runs/iterations.jsonl if it exists
129.   1. Run score-parent-wrapper.py --json > /tmp/parent-before.json
130.   2. Read total_score, outcome_score, instrument_score, and weakest component
131.   3. If instrument_score < 80, repair the measuring instrument first
132.   4. Use InfraNodus phase tools to diagnose the active weakest gate/component
133.   5. Pick the highest-impact action from the Action Catalog
134.   6. Make one bounded change
135.   7. Run validate_parent_wrapper_contract.py
136.   8. Run score-parent-wrapper.py --json > /tmp/parent-after.json
137.   9. If improved without regression, keep; otherwise revert
138.   10. Append iteration evidence to runs/iterations.jsonl
139.   11. Continue until stopping condition triggers
140. ```
141. 
142. Commit messages, when this becomes its own repo:
143. 
144. ```text
145. [PARENT:S:NN.N->NN.N] <component>: <bounded change>
146. ```
147. 
148. ## Fixed Search Boundary
149. 
150. For the first parent-wrapper ratchet:
151. 
152. - fixed artifact family: parent wrapper contracts and proof-package surfaces
153. - fixed metric: `score-parent-wrapper.py`
154. - fixed budget: one bounded proposal per cycle
155. - preferred fixed proposer on this Apple Silicon machine:
156.   - `HARNESS_BACKEND=mlx-lm:prism-ml/Ternary-Bonsai-8B-mlx-2bit`
157. - allowed alternative proposer surfaces:
158.   - Claude CLI
159.   - Codex
160.   - Copilot
161. 
162. The first loop must not change model, task, metric, and harness shape all at
163. once.
164. 
165. ## Iteration Log
166. 
167. File: `runs/iterations.jsonl`
168. 
169. One JSON object per line:
170. 
171. ```jsonl
172. {"iteration":1,"before":78.5,"after":82.0,"action":"add parent prompt-contract layer","result":"kept","note":"closed missing prompt-schema gap"}
173. {"iteration":2,"before":82.0,"after":82.0,"action":"rewrite scaffold prose only","result":"reverted","note":"no metric improvement"}
174. ```
175. 
176. ## Action Catalog
177. 
178. ### `iteration_layer` (target: 25)
179. 
180. | Action | Impact | How |
181. |---|---:|---|
182. | Add missing runnable scorer or ratchet script | +8 | Create the script, run it, and emit fresh metrics |
183. | Add missing `domain_spec.md` field or loop constraint | +4 | Tighten the parent domain spec and rerun the scorer |
184. | Add missing iteration evidence surface | +4 | Create or refresh `iterations.jsonl` and evaluation outputs |
185. 
186. ### `scaffold_contract` (target: 20)
187. 
188. | Action | Impact | How |
189. |---|---:|---|
190. | Add or repair front matter / bottom matter on a root scaffold file | +5 | Patch one file, run validator, rerun scorer |
191. | Add missing root scaffold file | +6 | Create the file, wire references, rerun validator |
192. 
193. ### `prompt_contract` (target: 15)
194. 
195. | Action | Impact | How |
196. |---|---:|---|
197. | Add missing governed prompt artifact | +5 | Create or mirror the artifact, validate references |
198. | Repair prompt-contract trace linkage | +3 | Update source trace and root references, rerun scorer |
199. 
200. ### `proof_package` (target: 20)
201. 
202. | Action | Impact | How |
203. |---|---:|---|
204. | Add missing proof-package family | +5 | Create the directory and minimum contract artifact |
205. | Add valid/invalid example pair plus expected failure | +4 | Update schema package and rerun validator |
206. 
207. ### `substrate_and_comparison` (target: 20)
208. 
209. | Action | Impact | How |
210. |---|---:|---|
211. | Wire a missing InfraNodus phase artifact | +5 | Add or refresh the phase map or gap artifact |
212. | Wire a missing Pixeltable substrate reference | +4 | Add the substrate-binding file or reference and rerun scorer |
213. 
214. ## Constraints
215. 
216. 1. **Do not fake green** — validator, examples, and gap artifacts must support the score.
217. 2. **Do not widen the search space mid-cycle** — keep one bounded proposal per cycle.
218. 3. **Do not modify the score definition and claim outcome improvement in the same cycle** — split mode means instrument work must stay explicit.
219. 4. **Do not remove InfraNodus, prompt-contract, or substrate authority surfaces** — they are load-bearing.
220. 5. **Keep Apple Silicon runs fixed-budget** — the first loop should remain compatible with MLX-backed bounded iterations.
221. 
222. ## File Map
223. 
224. | File | Role | Editable? |
225. |---|---|---|
226. | `GOAL.md` | Parent fitness function and improvement loop | Yes |
227. | `domain_spec.md` | Parent onboarding/domain boundary | Yes |
228. | `scripts/score-parent-wrapper.py` | Scoring script | Yes |
229. | `scripts/run-parent-ratchet.sh` | Fixed-budget parent ratchet runner | Yes |
230. | `tests/validate_parent_wrapper_contract.py` | Contract validator | Yes |
231. | `evaluation/validation-report.json` | Fresh validator evidence | Written by script only |
232. | `evaluation/infranodus-gap-analysis.json` | Gap-analysis evidence | Yes |
233. | `promotion/readiness.json` | Promotion readiness evidence | Written by script only |
234. | `runs/iterations.jsonl` | Iteration history | Appended by script only |
235. 
236. ## When to Stop
237. 
238. ```text
239. Starting score: NN.N
240. Ending score:   NN.N
241. Iterations:     N
242. Changes made:   (list)
243. Remaining gaps: (list)
244. Next actions:   (what to improve next)
245. ```
246. 
247. ---bottom-matter---
248. status_summary:
249.   completeness: 1.0
250.   confidence: high
251.   doc_state: active_goal
252. 
253. gate_progress:
254.   - gate_id: harvest_gate
255.     status: green
256.     notes: "Parent goal now includes upstream improvement-loop lineage and local score surfaces."
257.   - gate_id: registry_gate
258.     status: green
259.     notes: "Metrics, loop files, and upstream refs are explicit."
260.   - gate_id: manifest_gate
261.     status: green
262.     notes: "Improvement-layer files are placed in the parent wrapper."
263.   - gate_id: verification_gate
264.     status: amber
265.     notes: "New scorer and ratchet runner still need to be executed after creation."
266.   - gate_id: state_gate
267.     status: green
268.     notes: "State is tied to measurable split scores."
269.   - gate_id: health_gate
270.     status: green
271.     notes: "Improvement layer is no longer missing from the parent wrapper contract."
272.   - gate_id: promotion_gate
273.     status: amber
274.     notes: "Standalone parent repo still pending even though the parent seed now has a real goal loop."
275. 
276. open_questions:
277.   - "Which fixed proposer should be default for the first standalone parent repo ratchet: MLX Bonsai, Claude CLI, or Codex?"
278. 
279. pending_validations:
280.   - "Run the parent scorer and ratchet runner."
281. 
282. promotion_criteria:
283.   - "Parent scorer runs and emits a baseline metrics artifact."
284.   - "Parent ratchet runner appends iteration evidence."
285. 
286. blocked_by:
287.   - "Standalone meta-harness repo not yet initialized."
288. 
289. next_iteration:
290.   owner: "codex"
291.   objective: "Execute the new parent score loop and append the first iteration baseline."
292.
````

</details>


---

<sub>⏱️ 13s</sub>

### ✅ `view`

**view the file at /Volumes/PixelTable/VW_iTwin_Bridge/meta/scripts/score-parent-wrapper.py.**

/Volumes/PixelTable/VW_iTwin_Bridge/meta/scripts/score-parent-wrapper.py

<details>
<summary>141 lines</summary>

```
1. from __future__ import annotations
2. 
3. import argparse
4. import json
5. from pathlib import Path
6. 
7. 
8. ROOT = Path(__file__).resolve().parents[1]
9. 
10. 
11. def exists(path: str) -> bool:
12.     return (ROOT / path).exists()
13. 
14. 
15. def scaffold_contract() -> tuple[float, dict]:
16.     required = ["README.md", "AGENTS.md", "CLAUDE.md", "GOAL.md", "GOLDENPATH.md", "MEMORY.md"]
17.     present = sum(1 for item in required if exists(item))
18.     return round(20.0 * present / len(required), 2), {"present": present, "required": len(required)}
19. 
20. 
21. def prompt_contract() -> tuple[float, dict]:
22.     required = [
23.         "agent-heavy-run-prompt-index.md",
24.         "agent-heavy-run-prompt-schema.md",
25.         "agent-heavy-run-prompt.schema.json",
26.         "agent-heavy-run-prompt.template.yaml",
27.         "copilot-prompting-playbook.md",
28.     ]
29.     present = sum(1 for item in required if exists(item))
30.     return round(15.0 * present / len(required), 2), {"present": present, "required": len(required)}
31. 
32. 
33. def proof_package() -> tuple[float, dict]:
34.     required = ["source", "schemas", "examples", "expected-failures", "tests", "evaluation", "promotion"]
35.     present = sum(1 for item in required if exists(item))
36.     return round(20.0 * present / len(required), 2), {"present": present, "required": len(required)}
37. 
38. 
39. def substrate_and_comparison() -> tuple[float, dict]:
40.     required = ["pixeltable-operational-substrate.md", "infranodus-phase-tool-map.json", "library.yaml", "evaluation/infranodus-gap-analysis.json"]
41.     present = sum(1 for item in required if exists(item))
42.     return round(20.0 * present / len(required), 2), {"present": present, "required": len(required)}
43. 
44. 
45. def iteration_layer() -> tuple[float, dict]:
46.     required = ["domain_spec.md", "scripts/score-parent-wrapper.py", "scripts/run-parent-ratchet.sh", "runs/iterations.jsonl", "GOAL.md"]
47.     present = sum(1 for item in required if exists(item))
48.     return round(25.0 * present / len(required), 2), {"present": present, "required": len(required)}
49. 
50. 
51. def validator_health() -> tuple[float, dict]:
52.     path = ROOT / "evaluation/validation-report.json"
53.     if not path.exists():
54.         return 0.0, {"status": "missing"}
55.     report = json.loads(path.read_text())
56.     status = report.get("overall_status")
57.     return (40.0 if status == "pass" else 0.0), {"status": status}
58. 
59. 
60. def example_truth() -> tuple[float, dict]:
61.     path = ROOT / "evaluation/validation-report.json"
62.     if not path.exists():
63.         return 0.0, {"status": "missing"}
64.     report = json.loads(path.read_text())
65.     example_check = next((c for c in report["checks"] if c["name"] == "schema_and_example_validation"), None)
66.     if not example_check:
67.         return 0.0, {"status": "missing_check"}
68.     return (30.0 if example_check["status"] == "pass" else 0.0), {"status": example_check["status"]}
69. 
70. 
71. def gap_analysis_freshness() -> tuple[float, dict]:
72.     path = ROOT / "evaluation/infranodus-gap-analysis.json"
73.     if not path.exists():
74.         return 0.0, {"status": "missing"}
75.     data = json.loads(path.read_text())
76.     resolved = data.get("resolved_by", [])
77.     return (30.0 if len(resolved) >= 6 else 10.0), {"resolved_count": len(resolved)}
78. 
79. 
80. def build_score() -> dict:
81.     outcome_components = {}
82.     for name, fn in [
83.         ("scaffold_contract", scaffold_contract),
84.         ("prompt_contract", prompt_contract),
85.         ("proof_package", proof_package),
86.         ("substrate_and_comparison", substrate_and_comparison),
87.         ("iteration_layer", iteration_layer),
88.     ]:
89.         score, details = fn()
90.         outcome_components[name] = {"score": score, "details": details}
91. 
92.     instrument_components = {}
93.     for name, fn in [
94.         ("validator_health", validator_health),
95.         ("example_truth", example_truth),
96.         ("gap_analysis_freshness", gap_analysis_freshness),
97.     ]:
98.         score, details = fn()
99.         instrument_components[name] = {"score": score, "details": details}
100. 
101.     outcome_score = round(sum(item["score"] for item in outcome_components.values()), 2)
102.     instrument_score = round(sum(item["score"] for item in instrument_components.values()), 2)
103.     total_score = round(0.75 * outcome_score + 0.25 * instrument_score, 2)
104. 
105.     weakest_component = min(
106.         {**outcome_components, **instrument_components}.items(),
107.         key=lambda item: item[1]["score"],
108.     )[0]
109. 
110.     payload = {
111.         "score_id": "PARENT-META-SCORE-0001",
112.         "created_at": "2026-05-18",
113.         "scope": "portable_parent_wrapper",
114.         "metric_mode": "split",
115.         "total_score": total_score,
116.         "outcome_score": outcome_score,
117.         "instrument_score": instrument_score,
118.         "weakest_component": weakest_component,
119.         "outcome_components": outcome_components,
120.         "instrument_components": instrument_components,
121.     }
122.     return payload
123. 
124. 
125. def main() -> int:
126.     parser = argparse.ArgumentParser()
127.     parser.add_argument("--json", action="store_true")
128.     args = parser.parse_args()
129. 
130.     payload = build_score()
131.     (ROOT / "evaluation/metrics-latest.json").write_text(json.dumps(payload, indent=2) + "\n")
132.     if args.json:
133.         print(json.dumps(payload, indent=2))
134.     else:
135.         print(f"total_score={payload['total_score']}")
136.     return 0
137. 
138. 
139. if __name__ == "__main__":
140.     raise SystemExit(main())
141.
```

</details>


---

<sub>⏱️ 13s</sub>

### ✅ `view`

**view the file at /Volumes/PixelTable/VW_iTwin_Bridge/meta/tests/validate_parent_wrapper_contract.py.**

/Volumes/PixelTable/VW_iTwin_Bridge/meta/tests/validate_parent_wrapper_contract.py

<details>
<summary>185 lines</summary>

```
1. from __future__ import annotations
2. 
3. import json
4. from pathlib import Path
5. 
6. import yaml
7. from jsonschema import Draft202012Validator
8. 
9. 
10. ROOT = Path(__file__).resolve().parents[1]
11. REQUIRED_SCAFFOLD = [
12.     "README.md",
13.     "AGENTS.md",
14.     "CLAUDE.md",
15.     "GOAL.md",
16.     "GOLDENPATH.md",
17.     "MEMORY.md",
18. ]
19. REQUIRED_PROMPT_CONTRACT = [
20.     "agent-heavy-run-prompt-index.md",
21.     "agent-heavy-run-prompt-schema.md",
22.     "agent-heavy-run-prompt.schema.json",
23.     "agent-heavy-run-prompt.template.yaml",
24.     "copilot-prompting-playbook.md",
25. ]
26. REQUIRED_DIRECTORIES = [
27.     "source",
28.     "schemas",
29.     "examples",
30.     "expected-failures",
31.     "tests",
32.     "evaluation",
33.     "promotion",
34. ]
35. 
36. 
37. def parse_markdown_contract(path: Path) -> tuple[dict, dict]:
38.     text = path.read_text()
39.     if not text.startswith("---\n"):
40.         raise ValueError(f"{path.name}: missing front matter start")
41.     _, rest = text.split("---\n", 1)
42.     front_raw, body = rest.split("\n---\n", 1)
43.     if "\n---bottom-matter---\n" not in body:
44.         raise ValueError(f"{path.name}: missing bottom matter marker")
45.     _, bottom_raw = body.split("\n---bottom-matter---\n", 1)
46.     front = yaml.safe_load(front_raw) or {}
47.     bottom = yaml.safe_load(bottom_raw) or {}
48.     return front, bottom
49. 
50. 
51. def validate_examples() -> list[dict]:
52.     results = []
53.     front_schema = json.loads((ROOT / "schemas/front-matter.schema.json").read_text())
54.     bottom_schema = json.loads((ROOT / "schemas/bottom-matter.schema.json").read_text())
55.     Draft202012Validator.check_schema(front_schema)
56.     Draft202012Validator.check_schema(bottom_schema)
57. 
58.     valid_examples = [
59.         ("examples/front-matter.valid.json", front_schema),
60.         ("examples/bottom-matter.valid.json", bottom_schema),
61.     ]
62.     for rel, schema in valid_examples:
63.         instance = json.loads((ROOT / rel).read_text())
64.         Draft202012Validator(schema).validate(instance)
65.         results.append({"file": rel, "status": "pass"})
66. 
67.     registry = yaml.safe_load((ROOT / "expected-failures/registry.yaml").read_text())
68.     for item in registry["invalid_examples"]:
69.         schema = json.loads((ROOT / item["schema"]).read_text())
70.         instance = json.loads((ROOT / item["file"]).read_text())
71.         validator = Draft202012Validator(schema)
72.         errors = list(validator.iter_errors(instance))
73.         if not errors:
74.           raise AssertionError(f"{item['file']} unexpectedly passed")
75.         message_blob = " | ".join(error.message for error in errors)
76.         if item["expected_reason_contains"] not in message_blob:
77.             raise AssertionError(
78.                 f"{item['file']} failed for unexpected reason: {message_blob}"
79.             )
80.         results.append({"file": item["file"], "status": "pass", "reason": message_blob})
81.     return results
82. 
83. 
84. def main() -> int:
85.     checks = []
86. 
87.     scaffold_missing = [name for name in REQUIRED_SCAFFOLD if not (ROOT / name).exists()]
88.     checks.append(
89.         {
90.             "name": "required_scaffold_files",
91.             "status": "pass" if not scaffold_missing else "fail",
92.             "details": {"missing": scaffold_missing},
93.         }
94.     )
95. 
96.     prompt_missing = [name for name in REQUIRED_PROMPT_CONTRACT if not (ROOT / name).exists()]
97.     checks.append(
98.         {
99.             "name": "required_prompt_contract_files",
100.             "status": "pass" if not prompt_missing else "fail",
101.             "details": {"missing": prompt_missing},
102.         }
103.     )
104. 
105.     dir_missing = [name for name in REQUIRED_DIRECTORIES if not (ROOT / name).exists()]
106.     checks.append(
107.         {
108.             "name": "required_proof_package_dirs",
109.             "status": "pass" if not dir_missing else "fail",
110.             "details": {"missing": dir_missing},
111.         }
112.     )
113. 
114.     root_missing = [
115.         name
116.         for name in ["library.yaml", "infranodus-phase-tool-map.json", "pixeltable-operational-substrate.md"]
117.         if not (ROOT / name).exists()
118.     ]
119.     checks.append(
120.         {
121.             "name": "required_root_authorities",
122.             "status": "pass" if not root_missing else "fail",
123.             "details": {"missing": root_missing},
124.         }
125.     )
126. 
127.     scaffold_results = []
128.     front_schema = json.loads((ROOT / "schemas/front-matter.schema.json").read_text())
129.     bottom_schema = json.loads((ROOT / "schemas/bottom-matter.schema.json").read_text())
130.     front_validator = Draft202012Validator(front_schema)
131.     bottom_validator = Draft202012Validator(bottom_schema)
132.     scaffold_ok = True
133.     for name in REQUIRED_SCAFFOLD:
134.         front, bottom = parse_markdown_contract(ROOT / name)
135.         front_validator.validate(front)
136.         bottom_validator.validate(bottom)
137.         scaffold_results.append({"file": name, "status": "pass"})
138.     checks.append(
139.         {
140.             "name": "scaffold_markdown_contracts",
141.             "status": "pass" if scaffold_ok else "fail",
142.             "details": scaffold_results,
143.         }
144.     )
145. 
146.     example_results = validate_examples()
147.     checks.append(
148.         {
149.             "name": "schema_and_example_validation",
150.             "status": "pass",
151.             "details": example_results,
152.         }
153.     )
154. 
155.     overall = "pass" if all(item["status"] == "pass" for item in checks) else "fail"
156.     report = {
157.         "report_id": "PARENT-META-VALIDATION-0001",
158.         "created_at": "2026-05-18",
159.         "scope": "portable_parent_wrapper",
160.         "overall_status": overall,
161.         "checks": checks,
162.     }
163.     (ROOT / "evaluation/validation-report.json").write_text(json.dumps(report, indent=2) + "\n")
164. 
165.     readiness = {
166.         "readiness_id": "PARENT-META-PROMOTION-0001",
167.         "created_at": "2026-05-18",
168.         "scope": "portable_parent_wrapper",
169.         "status": "pass" if overall == "pass" else "blocked",
170.         "blockers": [] if overall == "pass" else ["Parent wrapper contract validation failed."],
171.         "evidence": [
172.             "evaluation/validation-report.json",
173.             "infranodus-phase-tool-map.json",
174.             "library.yaml",
175.             "agent-heavy-run-prompt.schema.json",
176.         ],
177.     }
178.     (ROOT / "promotion/readiness.json").write_text(json.dumps(readiness, indent=2) + "\n")
179.     print(json.dumps(report, indent=2))
180.     return 0 if overall == "pass" else 1
181. 
182. 
183. if __name__ == "__main__":
184.     raise SystemExit(main())
185.
```

</details>


---

<sub>⏱️ 13s</sub>

### ✅ `view`

**view the file at /Volumes/PixelTable/VW_iTwin_Bridge/meta/scripts/run-parent-ratchet.sh.**

/Volumes/PixelTable/VW_iTwin_Bridge/meta/scripts/run-parent-ratchet.sh

<details>
<summary>42 lines</summary>

```
1. #!/usr/bin/env bash
2. set -euo pipefail
3. 
4. ROOT="/Volumes/PixelTable/VW_iTwin_Bridge/meta"
5. LOG="$ROOT/runs/iterations.jsonl"
6. 
7. mkdir -p "$ROOT/runs"
8. touch "$LOG"
9. 
10. before_json="$(mktemp)"
11. after_json="$(mktemp)"
12. 
13. uv run --isolated --with jsonschema --with pyyaml python "$ROOT/scripts/score-parent-wrapper.py" --json > "$before_json"
14. 
15. if [[ "${1:-}" == "--dry" ]]; then
16.   jq -n \
17.     --arg before "$(jq -r '.total_score' "$before_json")" \
18.     '{"iteration":"dry-run","before_score":($before|tonumber),"after_score":($before|tonumber),"action":"dry-run baseline","result":"kept","note":"no proposal executed"}' \
19.     >> "$LOG"
20.   cat "$before_json"
21.   exit 0
22. fi
23. 
24. uv run --isolated --with jsonschema --with pyyaml python "$ROOT/tests/validate_parent_wrapper_contract.py" >/dev/null
25. uv run --isolated --with jsonschema --with pyyaml python "$ROOT/scripts/score-parent-wrapper.py" --json > "$after_json"
26. 
27. jq -n \
28.   --argjson before "$(cat "$before_json")" \
29.   --argjson after "$(cat "$after_json")" \
30.   '{
31.     iteration: (now | floor),
32.     before_score: $before.total_score,
33.     after_score: $after.total_score,
34.     weakest_component_before: $before.weakest_component,
35.     weakest_component_after: $after.weakest_component,
36.     action: "validation-and-score-cycle",
37.     result: (if $after.total_score >= $before.total_score then "kept" else "reverted" end),
38.     note: "bounded parent wrapper ratchet cycle"
39.   }' >> "$LOG"
40. 
41. cat "$after_json"
42.
```

</details>


---

<sub>⏱️ 17s</sub>

### ✅ `view`

**view the file at /Volumes/PixelTable/VW_iTwin_Bridge/meta/evaluation.**

/Volumes/PixelTable/VW_iTwin_Bridge/meta/evaluation

```
README.md
infranodus-gap-analysis.json
metrics-latest.json
validation-report.json
```


---

<sub>⏱️ 17s</sub>

### ✅ `view`

**view the file at /Volumes/PixelTable/VW_iTwin_Bridge/meta/runs.**

/Volumes/PixelTable/VW_iTwin_Bridge/meta/runs

```
.gitkeep
iterations.jsonl
```


---

<sub>⏱️ 17s</sub>

### ✅ `view`

**view the file at /Volumes/PixelTable/VW_iTwin_Bridge/meta/domain_spec.md.**

/Volumes/PixelTable/VW_iTwin_Bridge/meta/domain_spec.md

<details>
<summary>105 lines</summary>

````
1. # Domain Spec: Parent Meta-Harness Wrapper
2. 
3. ## Domain Summary
4. 
5. The target domain is the portable parent Meta-Harness wrapper that sits above a
6. child implementation repo and governs:
7. 
8. - scaffold contracts
9. - governed prompt contracts
10. - InfraNodus comparison doctrine
11. - Pixeltable substrate doctrine
12. - proof-package surfaces
13. - promotion readiness
14. 
15. Unit of evaluation: one bounded parent-wrapper improvement cycle.
16. 
17. Fixed for the first pass:
18. 
19. - parent wrapper root at `/Volumes/PixelTable/VW_iTwin_Bridge/meta`
20. - child body registry entry for `body.vw_itwin_bridge`
21. - governed prompt contract shape
22. - seven-gate lifecycle
23. - seven-part proof package
24. 
25. Allowed to change:
26. 
27. - parent wrapper docs and contracts
28. - scoring and ratchet scripts
29. - validation and promotion evidence surfaces
30. 
31. Out of scope:
32. 
33. - broad child-repo feature work
34. - changing the meaning of readiness while claiming improvement
35. - changing model, metric, and harness shape in the same first loop
36. 
37. ## Harness And Search Plan
38. 
39. Candidate harness shape:
40. 
41. ```text
42. meta/
43.   scaffold/
44.   source/
45.   schemas/
46.   examples/
47.   expected-failures/
48.   tests/
49.   evaluation/
50.   promotion/
51.   scripts/
52.   runs/
53. ```
54. 
55. Every candidate cycle must:
56. 
57. - run the parent validator
58. - run the parent scorer
59. - preserve iteration evidence
60. - keep or revert based on score
61. 
62. ## Evaluation Plan
63. 
64. Search-set evaluation:
65. 
66. - parent contract validation pass
67. - parent score calculation
68. - InfraNodus gap-artifact alignment
69. 
70. Held-out evaluation:
71. 
72. - replay inside the future standalone `meta-harness` repo
73. 
74. Primary metric:
75. 
76. - `total_score` from `scripts/score-parent-wrapper.py`
77. 
78. Secondary metrics:
79. 
80. - `outcome_score`
81. - `instrument_score`
82. - changed-file count
83. - unresolved blockers
84. - iteration count without improvement
85. 
86. ## Experience And Logging
87. 
88. Store per cycle:
89. 
90. - before and after scores
91. - weakest component
92. - action taken
93. - keep or revert decision
94. - validator report path
95. - promotion readiness path
96. 
97. Iteration log:
98. 
99. - `runs/iterations.jsonl`
100. 
101. ## Open Questions And Unknowns
102. 
103. - Which fixed proposer should be default for the first standalone parent repo loop?
104. - Should the standalone repo keep root-level contracts exactly or shift some into subdirectories?
105.
````

</details>


---

<sub>⏱️ 21s</sub>

### ✅ `view`

**view the file at /Volumes/PixelTable/VW_iTwin_Bridge/meta/evaluation/metrics-latest.json.**

/Volumes/PixelTable/VW_iTwin_Bridge/meta/evaluation/metrics-latest.json

<details>
<summary>68 lines</summary>

```
1. {
2.   "score_id": "PARENT-META-SCORE-0001",
3.   "created_at": "2026-05-18",
4.   "scope": "portable_parent_wrapper",
5.   "metric_mode": "split",
6.   "total_score": 100.0,
7.   "outcome_score": 100.0,
8.   "instrument_score": 100.0,
9.   "weakest_component": "prompt_contract",
10.   "outcome_components": {
11.     "scaffold_contract": {
12.       "score": 20.0,
13.       "details": {
14.         "present": 6,
15.         "required": 6
16.       }
17.     },
18.     "prompt_contract": {
19.       "score": 15.0,
20.       "details": {
21.         "present": 5,
22.         "required": 5
23.       }
24.     },
25.     "proof_package": {
26.       "score": 20.0,
27.       "details": {
28.         "present": 7,
29.         "required": 7
30.       }
31.     },
32.     "substrate_and_comparison": {
33.       "score": 20.0,
34.       "details": {
35.         "present": 4,
36.         "required": 4
37.       }
38.     },
39.     "iteration_layer": {
40.       "score": 25.0,
41.       "details": {
42.         "present": 5,
43.         "required": 5
44.       }
45.     }
46.   },
47.   "instrument_components": {
48.     "validator_health": {
49.       "score": 40.0,
50.       "details": {
51.         "status": "pass"
52.       }
53.     },
54.     "example_truth": {
55.       "score": 30.0,
56.       "details": {
57.         "status": "pass"
58.       }
59.     },
60.     "gap_analysis_freshness": {
61.       "score": 30.0,
62.       "details": {
63.         "resolved_count": 12
64.       }
65.     }
66.   }
67. }
68.
```

</details>


---

<sub>⏱️ 21s</sub>

### ✅ `view`

**view the file at /Volumes/PixelTable/VW_iTwin_Bridge/meta/evaluation/validation-report.json.**

/Volumes/PixelTable/VW_iTwin_Bridge/meta/evaluation/validation-report.json

<details>
<summary>91 lines</summary>

```
1. {
2.   "report_id": "PARENT-META-VALIDATION-0001",
3.   "created_at": "2026-05-18",
4.   "scope": "portable_parent_wrapper",
5.   "overall_status": "pass",
6.   "checks": [
7.     {
8.       "name": "required_scaffold_files",
9.       "status": "pass",
10.       "details": {
11.         "missing": []
12.       }
13.     },
14.     {
15.       "name": "required_prompt_contract_files",
16.       "status": "pass",
17.       "details": {
18.         "missing": []
19.       }
20.     },
21.     {
22.       "name": "required_proof_package_dirs",
23.       "status": "pass",
24.       "details": {
25.         "missing": []
26.       }
27.     },
28.     {
29.       "name": "required_root_authorities",
30.       "status": "pass",
31.       "details": {
32.         "missing": []
33.       }
34.     },
35.     {
36.       "name": "scaffold_markdown_contracts",
37.       "status": "pass",
38.       "details": [
39.         {
40.           "file": "README.md",
41.           "status": "pass"
42.         },
43.         {
44.           "file": "AGENTS.md",
45.           "status": "pass"
46.         },
47.         {
48.           "file": "CLAUDE.md",
49.           "status": "pass"
50.         },
51.         {
52.           "file": "GOAL.md",
53.           "status": "pass"
54.         },
55.         {
56.           "file": "GOLDENPATH.md",
57.           "status": "pass"
58.         },
59.         {
60.           "file": "MEMORY.md",
61.           "status": "pass"
62.         }
63.       ]
64.     },
65.     {
66.       "name": "schema_and_example_validation",
67.       "status": "pass",
68.       "details": [
69.         {
70.           "file": "examples/front-matter.valid.json",
71.           "status": "pass"
72.         },
73.         {
74.           "file": "examples/bottom-matter.valid.json",
75.           "status": "pass"
76.         },
77.         {
78.           "file": "examples/front-matter.invalid.missing-id.json",
79.           "status": "pass",
80.           "reason": "'id' is a required property"
81.         },
82.         {
83.           "file": "examples/bottom-matter.invalid.missing-gate-progress.json",
84.           "status": "pass",
85.           "reason": "'gate_progress' is a required property"
86.         }
87.       ]
88.     }
89.   ]
90. }
91.
```

</details>


---

<sub>⏱️ 21s</sub>

### ✅ `view`

**view the file at /Volumes/PixelTable/VW_iTwin_Bridge/meta/evaluation/infranodus-gap-analysis.json.**

/Volumes/PixelTable/VW_iTwin_Bridge/meta/evaluation/infranodus-gap-analysis.json

<details>
<summary>37 lines</summary>

```
1. {
2.   "analysis_id": "PARENT-META-INFRANODUS-GAP-0001",
3.   "created_at": "2026-05-18",
4.   "scope": "portable_parent_wrapper",
5.   "topical_clusters": [
6.     "Memory Goals",
7.     "Active Body",
8.     "Reusable Wrapper",
9.     "Knowledge Substrate",
10.     "Gate Optimization",
11.     "Document Scaffold",
12.     "Data Bridge",
13.     "Skill Verification",
14.     "Runtime Events",
15.     "Infrastructure Geometry"
16.   ],
17.   "content_gaps": [
18.     "Knowledge Substrate -> Gate Optimization",
19.     "Document Scaffold -> Data Bridge",
20.     "Knowledge Substrate -> Document Scaffold"
21.   ],
22.   "resolved_by": [
23.     "README.md",
24.     "library.yaml",
25.     "agent-heavy-run-prompt.schema.json",
26.     "infranodus-phase-tool-map.json",
27.     "pixeltable-operational-substrate.md",
28.     "source/",
29.     "schemas/",
30.     "examples/",
31.     "expected-failures/",
32.     "tests/",
33.     "evaluation/",
34.     "promotion/"
35.   ]
36. }
37.
```

</details>


---

<sub>⏱️ 37s</sub>

### ℹ️ Info

Operation cancelled by user

---

<sub>Generated by [GitHub Copilot CLI](https://github.com/features/copilot/cli)</sub>
