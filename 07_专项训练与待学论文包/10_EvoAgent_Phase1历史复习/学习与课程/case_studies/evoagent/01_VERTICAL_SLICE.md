# EvoAgent Vertical Slice: One Task Through the System

This bounded lesson follows only: task creation → Harness transition → agent coordination/message → Reviewer finding → Fixer candidate → Verifier result → Evolution gate decision → rollout outcome. API catalogues, the full database schema, general security review, and deployment review are excluded. Source snapshot: current working tree at `/mnt/d/MyResearch/EvoAgent`, verified 2026-08-10. Static reading establishes code shape, not runtime or production behavior.

## 1. Pre-test

Before reading the explanations, fill this table from your prediction. Do not score it yet.

| prompt | prediction | evidence you would seek |
| --- | --- | --- |
| Task states and legal transitions |  |  |
| Where checkpointing occurs |  |  |
| What “resume” must guarantee |  |  |
| Which failures may be retried |  |  |
| What Fixer and Verifier must never report silently |  |  |
| Evidence required before Evolution activation |  |  |
| What Canary/Shadow must observe before promotion or rollback |  |  |

## 2. Guided source reading

Each card uses a stable symbol rather than a line number. `source_snapshot` means the working tree read on 2026-08-10; it is not a commit hash.

### Beginner words used in the cards

An **invariant** is a rule that must still be true whenever the system reaches the point where the rule applies. It is not merely a usual pattern or a hoped-for outcome.

- State example: if the current task state is `PENDING`, moving directly to `SUCCESS` is forbidden because that edge is not in `ALLOWED`. The invariant is: every accepted state change must be an edge listed in `ALLOWED`.
- Non-state example: a Fixer candidate must not be published unless verification reports `passed`. This rule concerns publication, not which task state comes next.

When a card below says “invariant,” read it as “the rule this step must not break.”

### 2.1 Task creation

- file: `evoagent/store.py`
- symbol: `TaskStore.create`
- responsibility: persist a task initially as `PENDING`.
- input: task id, repository, pull request, payload, tenant.
- output: durable task row; no domain return value.
- invariant: the new state is `PENDING` and the supplied id identifies one task.
- failure surface: persistence/duplicate-id errors; no runtime behavior was exercised here.
- source_snapshot: current working tree, 2026-08-10
- verified_at: 2026-08-10
- evidence_status: `STATIC-CONFIRMED`

### 2.2 Harness transition and checkpoint reuse

- file: `evoagent/harness.py`
- symbol: `ALLOWED`; `ReviewHarness.run`; `ReviewHarness.resume`; `ReviewHarness._transition`; `ReviewHarness._run_node`; `ReviewHarness._completed`
- responsibility: enforce `PENDING → PLANNING → EXECUTING → REVIEWING → SUCCESS`, allow terminal failure/cancellation edges, checkpoint node outputs, and reuse completed outputs.
- input: task identity, repository/PR, diff, stored task/checkpoints.
- output: report or terminal failure/cancellation plus trace/checkpoints.
- invariant: `_transition` accepts only an edge in `ALLOWED`; a completed node output is returned instead of executing that node again.
- failure surface: `resume` delegates to `run`, which reconstructs initial input state and cached node outputs; it does not restore arbitrary in-flight Python/graph state. A callback exception other than the excluded classes is retried at most `node_retries + 1` attempts, but external reviewer calls carry no explicit operation id.
- source_snapshot: current working tree, 2026-08-10
- verified_at: 2026-08-10
- evidence_status: `STATIC-CONFIRMED`

### 2.3 Agent coordination/message

- file: `evoagent/agents.py`; `evoagent/store.py`
- symbol: `CollaborativeReviewer.review_with_context`; `CollaborativeReviewer._emit`; `TaskStore.record_agent_message`
- responsibility: run planner/specialist/critic/test/synthesizer/fix/verifier nodes and persist typed messages when a store and task id exist.
- input: task id, diff, parsed diff, sender/recipient/kind/content/correlation id.
- output: verified findings and persisted collaboration records.
- invariant: the fallback graph preserves node order; persisted messages retain sender, recipient, kind, content, and correlation id.
- failure surface: specialist exceptions are collected; this lesson does not claim every message is delivered exactly once.
- source_snapshot: current working tree, 2026-08-10
- verified_at: 2026-08-10
- evidence_status: `STATIC-CONFIRMED`

### 2.4 Reviewer finding

- file: `evoagent/models.py`; `evoagent/harness.py`
- symbol: `Finding`; `ReviewHarness._reviewing`
- responsibility: represent and rank a finding, then build a `ReviewReport`.
- input: rule id, severity, title, explanation, path, line, evidence, fix, test, confidence.
- output: serialized findings inside a report with summary and risk.
- invariant: severity is an enum; a finding carries both evidence and a proposed test rather than only prose.
- failure surface: schema presence does not prove evidence truth or test execution.
- source_snapshot: current working tree, 2026-08-10
- verified_at: 2026-08-10
- evidence_status: `STATIC-CONFIRMED`

### 2.5 Fixer candidate

- file: `evoagent/fixer.py`
- symbol: `SafeFixer.apply`; `SafeFixer._apply_python_ast`; `SafeFixer.create_fix_commits`
- responsibility: create conservative deterministic edits, verify them, then publish an atomic candidate only when verification passes.
- input: source content/findings/path or repository/PR/report.
- output: changed content/rules, no-eligible result, blocked result, or candidate commit/draft PR metadata.
- invariant: publication occurs only after `verification["passed"]`.
- failure surface: malformed Python, out-of-range lines, and unsupported rules can collapse to unchanged content plus empty rules; the caller exposes only a generic no-eligible note. It must not silently imply “no defect.”
- source_snapshot: current working tree, 2026-08-10
- verified_at: 2026-08-10
- evidence_status: `STATIC-CONFIRMED`

### 2.6 Verifier result

- file: `evoagent/verifier.py`
- symbol: `RepairVerifier.verify_contents`; `RepairVerifier.verify_worktree`; `RepairVerifier.verify_archive`
- responsibility: compile changed Python and optionally run the configured repository command in an isolated extracted archive.
- input: files, worktree, or archive plus replacements.
- output: `passed`, named checks, details, duration.
- invariant: a failed compile or configured test prevents candidate publication.
- failure surface: with no configured test command, worktree verification returns passed with an explicit note; this is not test evidence and must never be summarized as “tests passed.”
- source_snapshot: current working tree, 2026-08-10
- verified_at: 2026-08-10
- evidence_status: `STATIC-CONFIRMED`

### 2.7 Evolution gate decision

- file: `evoagent/evolution.py`
- symbol: `EvolutionEngine.propose`
- responsibility: save, defer, reject, or activate a prompt candidate using seven gates.
- input: candidate prompt, validation/holdout cases, reviewer factory, thresholds.
- output: version, decision, reason, metrics, seven gate values, run id.
- invariant: activation requires all evaluated conditions: safety, validation dataset readiness, holdout readiness, evaluation success, validation improvement, validation non-regression, and holdout non-regression.
- failure surface: unavailable provider or insufficient datasets defer evaluation; `None` gates must not be reported as passed.
- source_snapshot: current working tree, 2026-08-10
- verified_at: 2026-08-10
- evidence_status: `STATIC-CONFIRMED`

### 2.8 Rollout outcome

- file: `evoagent/rollout.py`
- symbol: `ReleaseManager.configure`; `ReleaseManager.assignment`; `ReleaseManager.observe`; `ReleaseManager.observe_shadow`
- responsibility: assign stable/canary/shadow traffic, record candidate outcomes, rollback on canary error budget, or promote after shadow verification.
- input: deployment configuration, deterministic key, lane, failure/result observations.
- output: assignment or updated deployment/observation and alerts on rollback/promotion.
- invariant: only canary-lane observations enter `observe` accounting; promotion/rollback claims require recorded observations.
- failure surface: zero-percent canary assigns all traffic stable, and stable observations are not recorded as canary results. This is an implicit disabled-protection state, not proof that rollback is broken.
- source_snapshot: current working tree, 2026-08-10
- verified_at: 2026-08-10
- evidence_status: `STATIC-CONFIRMED`

## 3. Evidence check

| layer | what it supports | what it does not support |
| --- | --- | --- |
| Documentation claim | The design says application-owned checkpoints survive worker restarts. `DOC-CLAIM` | Full in-flight runtime-state restoration. |
| Current static implementation | Legal transitions, bounded retries, cached completed-node outputs, message persistence, Fixer/Verifier gates, seven Evolution gates, lane-specific rollout observations. `STATIC-CONFIRMED` | That any path ran successfully in this snapshot. |
| Existing test evidence | Exact bounded anchors: `tests/test_production_features.py::test_failed_graph_resumes_after_last_completed_checkpoint`, recorded in `progress/audits/2026/08/evoagent/SLICE_FINDINGS.csv` row `EA-SLICE-001`, supports only that completed planning is skipped/reused; `tests/test_production_features.py::test_canary_assignment_and_error_budget_rollback`, recorded in row `EA-SLICE-003`, supports only canary assignment and error-budget rollback under its tested nonzero configuration. These assertions are `TEST-CONFIRMED`; the whole chain is not. | Full runtime-state resume, external-call idempotency, zero-percent protection, or production behavior. |
| Recorded runtime evidence | Historical `EA-PDF-FIX` records font loading failing before the predicted missing-docs failure, followed by a friendly missing-source exit. `RUNTIME-CONFIRMED` for that historical ordering only. | Current real Markdown-to-PDF generation or Chinese rendering. |
| Missing production evidence | No evidence used in this lesson is `PRODUCTION-VALIDATED`. | Production impact, frequencies, reliability, or readiness. |

**Epistemic side case — PDF ordering.** Static review predicted a missing-document failure, but the recorded run reached font loading first. Current source now checks source existence before registering fonts. The lesson is not “static review is useless”; it is that static plausibility does not establish runtime order. End-to-end PDF generation remains `UNVERIFIED`.

Finding class and lifecycle are independent: the PDF issue is `CONFIRMED` yet `PARTIALLY_FIXED`; canary-zero and retry/idempotency are `DOWNGRADE` yet `OPEN`. Do not turn either pair into one status.

## 4. Reconstruction

Complete these without reopening source, then compare against §2.

### Exercise A — state transition table

Output all legal normal and terminal edges plus one forbidden edge. **Passes only if** normal order is `PENDING → PLANNING → EXECUTING → REVIEWING → SUCCESS`, failure/cancellation edges originate only where `ALLOWED` permits them, and the forbidden edge is rejected rather than silently coerced.

### Exercise B — idempotent node retry pseudocode

```text
run_node(task_id, node, operation_id):
  if durable_result(operation_id) is completed: return that result
  reserve the same operation_id for every retry
  call dependency with operation_id
  atomically commit result once
  on ambiguous timeout: reconcile by operation_id before another call
```

**Passes only if** the same `operation_id` is reused, completed results are not re-executed, and a partial LLM response cannot be committed twice. Current EvoAgent does not expose this full contract; mapping it to current behavior is `UNVERIFIED`.

### Exercise C — minimal Reviewer finding schema

Output: `{finding_id, rule_id, severity, path, location, claim, evidence, proposed_fix, regression_test, confidence}`. **Passes only if** claim, evidence, and test are separate; absence of a fixer rule cannot erase the finding.

### Exercise D — seven-gate activation truth table

| safety | validation ready | holdout ready | evaluation success | improvement | validation non-regression | holdout non-regression | activation |
| --- | --- | --- | --- | --- | --- | --- | --- |
| T | T | T | T | T | T | T | T |
| F | T | T | T | T | T | T | F |
| T | F | T | — | — | — | — | F/deferred |
| T | T | F | — | — | — | — | F/deferred |
| T | T | T | F | T | T | T | F |
| T | T | T | T | F | T | T | F |
| T | T | T | T | T | F | T | F |
| T | T | T | T | T | T | F | F |

**Passes only if** activation is true solely in the all-true row and unknown/not-run gates are never counted as passes.

### Exercise E — failure propagation chain

Selected chain: external reviewer accepts a retry → no explicit operation id → first response may have succeeded before an ambiguous transport failure → node retries → duplicate bill/side effect may occur → checkpoint stores only the returned attempt → metrics without result/provider/model/lane labels cannot attribute the duplication. Current code shape is `STATIC-CONFIRMED`; actual duplication and production impact are `UNVERIFIED`.

**Passes only if** the answer names trigger, violated invariant, observable consequence, current evidence level, and next test.

### Exercise F — pre-fix failing test

Test `SafeFixer.apply` with malformed Python plus an otherwise eligible finding and assert a structured error status distinct from `no_eligible_rule`. It should fail against current behavior because `SyntaxError` becomes unchanged content plus empty rules.

**Passes only if** the pre-fix assertion fails for the expected reason, a proposed fix makes it pass, and unsupported findings still remain distinguishable from parse failure. This test is designed, not run: `UNVERIFIED`.

## 5. Transfer

Transfer to another Agent/MAS review service by preserving contracts, not class names:

1. give every retried external operation a durable identity;
2. separate “unsupported,” “invalid candidate,” and “verified no-op” outcomes;
3. require activation evidence distinct from rollout observations;
4. correlate state, messages, findings, fixes, verification, and rollout by case/event ids.

### Beginner event-log vocabulary before PM4Py

Use a tiny parcel example first:

- **case**: one journey being followed, such as parcel `parcel-9` from booking to delivery.
- **event**: one recorded thing that happened in that journey, such as event `E-001` saying the parcel was booked.
- **activity**: the short name for what happened, such as `parcel_booked`.
- **timestamp**: when it happened, such as `2026-08-10T09:00:00Z`; without it, event order by time is incomplete.
- **consume**: read a row as input. “PM4Py consumes an event” means PM4Py reads an event-log row with fields such as case, activity, and timestamp; it does not eat, execute, or approve the event.

The EvoAgent illustration below is **not captured runtime data**. Its timestamp is missing, so PM4Py compatibility and temporal ordering remain `UNVERIFIED`.

### Process state and risk state are different

| process state | risk state |
| --- | --- |
| Says where the task is in its workflow, for example `REVIEWING`. | Says our current risk interpretation, for example `awaiting_verified_evidence` or `blocked_by_failed_verification`. |
| Derived from workflow execution and legal transitions. | Requires separately defined risk meaning and transition rules. |
| `REVIEWING → SUCCESS` can be checked against `ALLOWED`. | A change such as `awaiting_verified_evidence → eligible_for_gate_review` is only a proposed interpretation here. |
| Does not by itself say “safe” or “unsafe.” | Must not be inferred merely by renaming a process state. |

### One running example: the same fictional event all the way through

Keep these identities unchanged: case `task-42`, raw event `E-003`, and correlation id `fix-3`.

**Step 1 — raw log line (`RESEARCH-HYPOTHESIS`; illustrative):**

```text
E-003 task-42 verifier verification_completed result=passed correlation_id=fix-3
```

This line has no real timestamp. It was written for teaching and was not observed at runtime.

**Step 2 — proposed `ProcessEventSchema-v0` row (`RESEARCH-HYPOTHESIS`):**

| event_id | case_id | activity | agent | timestamp | state_before | state_after | result | correlation_id |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| E-003 | task-42 | verification_completed | verifier | required-but-missing | REVIEWING | REVIEWING | passed | fix-3 |

**Step 3 — what PM4Py can read:** PM4Py could read `case_id=task-42` as the case identifier and `activity=verification_completed` as the activity. A proper event log also needs a real timestamp for temporal analysis; because this row has `required-but-missing`, actual PM4Py ingestion is `UNVERIFIED`.

**Step 4 — proposed `InteractionRiskSchema-v0` transition (`RESEARCH-HYPOTHESIS`):**

```text
risk_state_before = awaiting_verified_evidence
--[evidence_event_id = E-003; result = passed]-->
risk_state_after = eligible_for_gate_review
```

This does **not** mean `passed` proves safety. The two risk-state labels and their transition semantics are proposed teaching labels, not observed EvoAgent behavior.

**Step 5 — exactly one PM4Py-derived feature enters the risk model (`RESEARCH-HYPOTHESIS`):**

Selected Fusion vocabulary: **constraint**. The derived Boolean input/predicate value is `has_passed_verification_event(task-42)=true`, inferred from illustrative event `E-003`. The **constraint is a separate rule that consumes that value**: if it is not `true`, entry to `eligible_for_gate_review` is forbidden. The predicate value is not itself structure, parameter, constraint, or prior. Whether PM4Py can derive it from a valid captured log, and whether the consuming rule predicts or controls real risk, remain `UNVERIFIED`.

This walkthrough intentionally uses only **constraint**. Do not try to master the other Fusion words at the same time.

### Fusion glossary for later use

- **structure**: which states or components are connected.
- **parameter**: a numeric value used by the model, such as a probability or delay.
- **constraint**: a rule that permits or forbids a model step.
- **prior**: a starting belief before the current case supplies evidence.

A Fusion claim is useful only if a process result becomes a clearly defined model input and adds an observable relation to failure. Otherwise it is tool concatenation. All mappings in this walkthrough remain `RESEARCH-HYPOTHESIS`.

## 6. Reflection

Write three sentences:

1. “I previously treated checkpoint reuse as ___; source reading changed it to ___.”
2. “I previously treated a passed verifier with no configured command as ___; now I require ___.”
3. “The claim I am most tempted to overstate is ___; the missing evidence is ___.”

Human Gate A re-check, answerable from this file alone. Answer in your own words and use the running example where requested:

1. A task stopped after planning. What can its checkpoint let the next run reuse, and what in-flight work or external side effect does that checkpoint **not** prove was restored or performed exactly once?
2. Suppose the task is `PENDING` and code tries to move it directly to `SUCCESS`. Explain what an invariant is, how `ALLOWED` decides this case, and give the non-state publication invariant from §2.
3. For event `E-003`, identify its case, event, activity, and missing timestamp. Then explain “PM4Py consumes this event” without using the word “consume.”
4. Using only illustrative event `E-003`, distinguish its process state from the proposed risk-state change. Which values are merely illustrative event-row fields, which meanings are proposed risk semantics, and what actual runtime capture evidence exists? (Answer for runtime capture: none.)
5. Write the Boolean input/predicate value used in the walkthrough. Then write the separate constraint that consumes it, explain why the value is not itself a constraint, and state what remains unverified.

**Pass rubric:** each answer must reconstruct the mechanism or apply it to `E-003`. If you can only repeat terms such as “checkpoint,” “invariant,” “PM4Py,” “risk state,” or “constraint” without explaining the relationship or boundary, Human Gate A is **not passed**. The prior Human Gate A attempt failed for expansion; this repair requires a new user-run check and does not call the gate passed.

## 7. Four-way research mapping card

### EvoAgent

- responsibility: carry a review task from persisted creation through evidence, candidate repair, verification, activation decision, and rollout observation.
- contract: legal state edges; durable node outputs; explicit finding/fix/verifier outcomes; all-seven-gate activation; observation-backed promotion/rollback.
- invariant: no illegal transition, no publication after failed verification, no activation with a false/unknown gate.
- evidence: current symbols are `STATIC-CONFIRMED`; bounded historical tests are `TEST-CONFIRMED`; production behavior is `UNVERIFIED`.

### PM4Py mapping

- event candidates: task creation, each Harness transition, agent message, finding emission, fixer outcome, verifier outcome, Evolution decision, lane assignment, rollout observation.
- conformance question: does an observed case follow the reference order, or show retry loops, missing verification, rework, or a decision without prerequisite evidence?
- evidence_status: `RESEARCH-HYPOTHESIS`; no PM4Py-compatible runtime log was produced here.

### SBPN/SBTPN mapping

- state interpretation: places may encode task phase plus candidate-risk state; tokens may represent task/candidate evidence state.
- transition interpretation: message handoff, retry, finding acceptance, fix proposal, verification, activation, promotion, rollback.
- evidence gap: probability/timing parameters, causal propagation semantics, and evidence-linked risk-state labels are absent.
- evidence_status: `RESEARCH-HYPOTHESIS`.

### Fusion mapping

- selected bridge for this lesson: the Boolean input/predicate value `has_passed_verification_event(case_id)` is consumed by a **constraint**: if the value is not `true`, entry to the proposed risk state `eligible_for_gate_review` is forbidden. The value does not itself become a constraint.
- vocabulary staging: §5 defines constraint first; structure, parameter, and prior are glossary terms for later lessons, not simultaneous mastery requirements.
- kill criterion: if this feature cannot be derived from a valid captured event log, cannot be given defensible risk semantics, or adds no observable relation to failure, stop; it is tool concatenation.
- evidence_status: `RESEARCH-HYPOTHESIS`; the timestamp, PM4Py run, feature extraction, risk semantics, and predictive/control value are `UNVERIFIED`.

## 8. Mastery check

- **L0:** identify task states, checkpoint, finding, verification, gate, and lane.
- **L1:** explain why checkpoint reuse is narrower than true resume; why no configured tests is not test success; and why process order is not risk causality.
- **L2:** produce all six reconstruction outputs, link each claim to an evidence label, and design one executable failing test.

The previous Human Gate A attempt **failed for expansion**: the learner understood checkpoint versus full resume, but beginner event vocabulary, PM4Py input, process-state versus risk-state mapping, and Fusion staging were not yet usable. This repaired slice passes its usability gate only if the learner answers the five revised questions in §6 by reconstructing the mechanism rather than repeating vocabulary. `validate_learning.py` checks file structure and selected content markers; it does **not** assess Human Gate A. The gate remains user-run and is **not passed** by this edit. Curriculum expansion remains blocked pending a successful re-check.
