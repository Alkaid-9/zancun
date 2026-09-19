# Process-Risk Pilot Specification v0 (Non-Executable)

This is a bounded, **non-executable** pilot specification. It consumes the vertical-slice material in [01_VERTICAL_SLICE.md](../01_VERTICAL_SLICE.md), the pattern cards in [02_PATTERN_CARDS.md](../02_PATTERN_CARDS.md), and the failure/evidence lessons in [03_FAILURE_AND_EVIDENCE.md](../03_FAILURE_AND_EVIDENCE.md). No PM4Py run, no code experiment, and no EvoAgent repository execution happened for this file. Where a current source symbol is cited, the snapshot is git `ef768b5` (`source_snapshot: ef768b5`). Every schema instance and every fusion verdict in this file is `RESEARCH-HYPOTHESIS` unless a narrower label is stated, and **no timestamp in this file was captured at runtime**.

## 1. ProcessEventSchema-v0

```yaml
case_id: string
activity: string
agent: string
timestamp: ISO-8601 string
state_before: string
state_after: string
result: success | failure | cancelled | partial
correlation_id: string
```

Row-identity convention: example tables in this file add an `event_id` column as a log-row key, following the `E-003` precedent in 01_VERTICAL_SLICE.md §5. `event_id` is **not** one of the eight schema fields; it exists so the same event identity can be referenced from the interaction view in §2 without inventing links. Whether it becomes a formal field is deferred to a future schema v1.

### 1.1 One example derived from the vertical slice

- evidence_status: RESEARCH-HYPOTHESIS

| event_id | case_id | activity | agent | timestamp | state_before | state_after | result | correlation_id |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| E-003 | task-42 | verification_completed | verifier | 2026-08-10T12:00:03Z | REVIEWING | REVIEWING | success | fix-3 |

Declared limits of this row:

1. **The timestamp is a fictional illustrative value.** 01_VERTICAL_SLICE.md §5 deliberately wrote `required-but-missing` for this same fictional event; this pilot supplies an ISO-8601-shaped placeholder only so the row type-checks against the schema. **No real runtime capture of this event exists**, so temporal ordering and PM4Py ingestion remain `UNVERIFIED`. This continues the E-003 discipline: the event was written for teaching and was not observed at runtime.
2. The 01 chapter illustrative row wrote `result=passed`. `passed` is not in the closed enumeration of this schema, so the row normalizes to `success`; the original `passed` value remains visible in the illustrative log line in 01_VERTICAL_SLICE.md §5. The activity name `verification_completed` records completion only — it does not encode the pass/fail result.
3. `REVIEWING` reuses the process-state vocabulary guarded by `evoagent/harness.py::ALLOWED` (`source_snapshot: ef768b5`) as naming only; this row does not claim that transition was executed.

## 2. InteractionRiskSchema-v0

```yaml
source_agent: string
target_agent: string
interaction_type: message | artifact | shared_state | tool_result
precondition: string
risk_state_before: clean | exposed | suspect | compromised | contained | recovered
risk_state_after: clean | exposed | suspect | compromised | contained | recovered
evidence_event_ids: list[string]
```

Proposed row semantics, all `RESEARCH-HYPOTHESIS`:

1. `risk_state_before` / `risk_state_after` describe the **target_agent** of the row, immediately before and after the interaction.
2. An initial contamination arriving from outside the agent set is written as a self-edge (`source_agent = target_agent`) with `interaction_type: tool_result`, because the contaminated content enters through tool-mediated input rather than from another agent.
3. The six-value risk enumeration replaces the two teaching labels used in 01_VERTICAL_SLICE.md §5 (`awaiting_verified_evidence`, `eligible_for_gate_review`). Both vocabularies obey the same discipline: risk labels are proposed semantics, not observed EvoAgent behavior.

## 3. Three-agent toy

The toy is **fictional**. Agents: `reviewer`, `fixer`, `verifier`. The names borrow the node-role vocabulary of the vertical slice, but every event below is invented; the `STATIC-CONFIRMED` symbol evidence in 01/02 does **not** transfer to this toy through shared naming. Case: `task-77`.

- evidence_status: RESEARCH-HYPOTHESIS

### 3.1 Process-event view (fictional log)

| event_id | case_id | activity | agent | timestamp | state_before | state_after | result | correlation_id |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| T-101 | task-77 | contaminated_diff_ingested | reviewer | 2026-08-12T10:00:01Z | EXECUTING | EXECUTING | success | review-77 |
| T-102 | task-77 | finding_message_sent | reviewer | 2026-08-12T10:00:02Z | EXECUTING | EXECUTING | success | review-77 |
| T-103 | task-77 | fix_candidate_published | fixer | 2026-08-12T10:00:03Z | EXECUTING | REVIEWING | success | fix-77-1 |
| T-104 | task-77 | verification_failed | verifier | 2026-08-12T10:00:04Z | REVIEWING | REVIEWING | failure | fix-77-1 |
| T-105 | task-77 | isolation_applied | verifier | 2026-08-12T10:00:05Z | REVIEWING | REVIEWING | success | fix-77-1 |

All timestamps are fictional illustrative values; no runtime capture exists. The toy covers only the middle of a case (`EXECUTING` onward); the `EXECUTING → REVIEWING` edge in T-103 reuses an edge listed in `evoagent/harness.py::ALLOWED` (`source_snapshot: ef768b5`) as naming only.

### 3.2 Interaction-risk view (fictional)

| row | source_agent | target_agent | interaction_type | precondition | risk_state_before | risk_state_after | evidence_event_ids |
| --- | --- | --- | --- | --- | --- | --- | --- |
| R-1 | reviewer | reviewer | tool_result | external diff content reaches the reviewer through tool-mediated ingestion | clean | compromised | T-101 |
| R-2 | reviewer | fixer | message | reviewer is compromised and fixer consumes the finding message | clean | exposed | T-102 |
| R-3 | fixer | verifier | artifact | fixer is exposed and verifier consumes the published candidate artifact | clean | suspect | T-103 |
| R-4 | verifier | fixer | message | verification failed on the suspect candidate, triggering isolation of the fixer output channel | exposed | contained | T-104; T-105 |

Requirements check: one initial contamination event (R-1), exactly two propagation edge types between distinct agents (`message` in R-2, `artifact` in R-3), and one isolation intervention (R-4). The `tool_result` type in R-1 is the ingestion channel of the initial contamination, not a third propagation edge.

### 3.3 Risk marking before and after the intervention

| agent | before R-4 | after R-4 |
| --- | --- | --- |
| reviewer | compromised | compromised |
| fixer | exposed | contained |
| verifier | suspect | suspect |

Honest boundary: the isolation intervention limits further propagation from the fixer output channel only. It does not clean the reviewer's contamination and does not resolve the verifier's suspect state. A "recovered" claim would need separate recovery events and is deliberately absent.

## 4. Fusion-0 acceptance

Acceptance criterion (from the approved plan): **Fusion-0 passes only if the same event IDs can support both a process event log view and an interaction graph edge view. If identifiers cannot be shared without invented links, Fusion-0 fails.**

Shared-identifier check on the toy material:

| interaction row | evidence_event_ids | present in §3.1 log? | shared case_id | shared correlation_id |
| --- | --- | --- | --- | --- |
| R-1 | T-101 | yes | task-77 | review-77 |
| R-2 | T-102 | yes | task-77 | review-77 |
| R-3 | T-103 | yes | task-77 | fix-77-1 |
| R-4 | T-104; T-105 | yes | task-77 | fix-77-1 |

No identifier outside {task-77; T-101..T-105; review-77; fix-77-1} was needed, and no link was invented. The slice-derived example in §1.1 satisfies the same check through the 01_VERTICAL_SLICE.md §5 walkthrough, where E-003 / task-42 / fix-3 appear unchanged in both the event row and the risk transition.

Verdict: **Fusion-0 acceptance holds on this fictional material.** This is a `RESEARCH-HYPOTHESIS`-level specification verdict: it demonstrates that the two schemas can share identifiers, nothing more. Fusion-0 on real captured EvoAgent runtime events remains `UNVERIFIED`; if a real capture cannot share identifiers without invented links, Fusion-0 fails at that point regardless of this toy.

## 5. Fusion-1: one PM4Py-derived feature and its kill criterion

Chosen feature (exactly one of the five allowed candidates): **handover frequency**.

Definition without metaphor: for one case, order events by timestamp; for each adjacent pair where the `agent` field changes from `a` to `b` with `a ≠ b`, count one handover `a→b`. `handover_frequency(a→b)` is that count per case, or per log window when aggregating cases.

Illustrative hand computation on the §3.1 fictional log (this is arithmetic on invented rows, **not** a PM4Py run): ordering T-101..T-105 by timestamp yields `handover_frequency(reviewer→fixer) = 1` (T-102→T-103) and `handover_frequency(fixer→verifier) = 1` (T-103→T-104).

Role in the risk model (exactly one of structure / parameter / constraint / prior): **parameter**. `handover_frequency(a→b)` enters the risk model as the numeric exposure parameter attached to the existing InteractionRiskSchema edge `a→b`: the count of transmission opportunities per case along that edge, bounding how many times per case a propagation rule on that edge may fire. It is a number attached to an existing edge — it does not create or remove edges (so it is not structure), it does not by itself permit or forbid a model step (so it is not a constraint), and it is not a belief held before the current case supplies evidence (so it is not a prior).

Kill criterion, stated without metaphor — Fusion-1 fails if **any** of the following holds:

1. **Derivability failure:** `handover_frequency` cannot be computed by PM4Py from a real captured event log with valid case/activity/agent/timestamp fields.
2. **Role-statement failure:** its use in the risk model cannot be written as the numeric per-edge transmission-opportunity count defined above and requires analogy language instead.
3. **No observable relation:** across real captured cases, the feature shows no observable relation to failure outcomes (for example `verification_failed` or rollback events).

On failure, the fusion is judged tool concatenation per the approved design's kill criteria, and Fusion-2 must not be entered.

Explicit verdict: **Fusion-1 is NOT ESTABLISHED.** The role statement passes the no-metaphor test at specification level (condition 2 is currently satisfied in the negative sense that the role was stated without metaphor above). Conditions 1 and 3 cannot be evaluated because no real captured event log exists. The kill criterion is therefore not yet triggered — nothing is disproved — and the establish/kill decision is deferred to the first real captured log. This verdict deliberately does not claim success.

- evidence_status: RESEARCH-HYPOTHESIS

## 6. Baselines and ablation (B0-B4)

The matrix below reproduces the ablation design approved in the learning-system design decision (registered as EA-LEARNING-DESIGN; the four-level fusion ladder and the ablation matrix are the authoritative definitions there). B2-B4 are **future experiments** outside this pilot's authorization. **No comparative results are claimed for any row**; the matrix only records which increment a future experiment must attribute its contribution to.

| version | process | interaction | risk | intervention | status in this pilot |
| --- | --- | --- | --- | --- | --- |
| B0 | none | static graph | simple rules | none | specified baseline; not executed; no result claimed |
| B1 | PM4Py | static graph | simple rules | none | specified baseline; not executed; no result claimed |
| B2 | PM4Py | dynamic interaction graph | SBPN/SBTPN | none | future experiment; out of scope here |
| B3 | PM4Py | dynamic interaction graph | SBPN/SBTPN | with intervention | future experiment; out of scope here |
| B4 | full closed loop | dynamic | full | Canary/Shadow verification | future experiment; out of scope here |

Fusion-0 (§4) and Fusion-1 (§5) correspond to the B0→B1 increment: shared event data plus one process-derived feature. B2-B4 additionally require a dynamic interaction graph, an SBPN/SBTPN risk model, interventions, and a Canary/Shadow closed loop, none of which is specified or claimed here.

## 7. What this pilot does not establish

- No PM4Py execution, no SBPN/SBTPN construction, no intervention experiment, and no EvoAgent runtime capture happened.
- The toy's risk labels and propagation semantics are proposed, not observed; the schema row semantics in §2 are proposals.
- Fusion-0 holding on fictional material does not imply it holds on real captured logs.
- Fusion-1 is not established; its decision is deferred as stated in §5.
- Nothing in this file is `TEST-CONFIRMED`, `RUNTIME-CONFIRMED`, or `PRODUCTION-VALIDATED`.
