# A2 EdgeIM paper note draft

Status: DRAFT / A2-PROVISIONAL / USER-MUST-READ
Owner: A2 agent (SOL)
Scope: Segment 0 only; no implementation or experiment authorization.
Evidence boundary: No local EdgeIM PDF or `07_EDGEIM.md` was found in the current tree during this pass. The notes below distinguish official bibliographic/abstract evidence from inference. Full algorithmic claims require the user to read the paper itself before B1 freezes the measurement contract.

## 1. Paper identity and role

- Title: *An Efficient Edge-Based Process Model Discovery Technique* (EdgeIM).
- Venue/year: IEEE International Conference on Web Services (ICWS), 2025.
- DOI: `10.1109/ICWS67624.2025.00057`.
- Official record: NOVA Research portal (bibliographic record and abstract).
- Authors/relationship: Su Xuan first author; Lu Faming is listed as a co-author/通讯关系 in project records. This relationship must be checked against the paper PDF before outreach wording.
- Role in R1: primary motivating method; R1 is a bounded audit of its sampling component, not a claim of complete replication.
- Access status: official record verified; local full text not located in this pass. Do not claim full-text or code availability.

## 2. Core claim (paper-level, as far as verified)

The paper presents an edge-based process-model discovery technique intended to reduce the cost of process discovery while preserving relevant process features. The official abstract describes a three-stage architecture: (i) feature-preserving sampling, (ii) local edge processing, and (iii) global feature aggregation. It reports evaluation with PM4Py on nine public event logs.

**Claim ceiling for this note:** We may state that the paper proposes this architecture and reports such an evaluation. We may not yet state exact sampling guarantees, exact selection rule, metric values, or superiority claims until the paper text is read and page/section anchored.

## 3. Method / mechanism summary (provisional)

### Stage 1 — Feature-preserving sampling
The event log is reduced before discovery using a sampling procedure intended to preserve process-relevant features. The exact sampling unit (trace/case/event), budget definition, coverage criterion, and tie-breaking rule are **not verified** from the available local evidence.

### Stage 2 — Local edge processing
The sampled data are processed at edge nodes rather than sending the entire log to a central location. The exact local representation, partitioning assumptions, and whether local discovery is performed independently are **not verified**.

### Stage 3 — Global feature aggregation
Local outputs/features are aggregated centrally to produce a global process model. The aggregation object, conflict resolution, and relationship to PM4Py discovery (including IM/IMf) are **not verified**.

These three stages are an abstract architecture summary, not an implementation contract.

## 4. Pre-reading prediction (to be written by user after reading)

Before inspecting reported results, the user should write a prediction for the R1 audit:

- Under equal retained budget, coverage-based sampling will preserve more distinct/rare structural behavior than uniform random sampling.
- If injected recording errors create novel rare structures, coverage selection may retain a higher fraction of marked noise than random sampling (H1; not assumed true).
- If H1 is false, first alternative explanations to test are: (a) the coverage rule is robust to the chosen error type; (b) the downstream miner, rather than sampling, dominates the observed difference.

This prediction is a training prompt, not evidence about what EdgeIM actually does.

## 5. Uncertainty / details not publicly established in this pass

1. Exact pseudocode for the coverage/feature-preserving sampler.
2. Definition of “feature” and the state maintained while selecting traces/events.
3. Sampling unit and stopping/termination condition.
4. Whether the method samples traces, events, variants, or partition-local records.
5. Edge partitioning and global aggregation protocol.
6. Exact PM4Py miner, parameters, preprocessing, and metric implementation.
7. Dataset preprocessing, timestamp treatment, and random seeds.
8. Whether an official implementation is public and reproducible.
9. Which reported tables are directly comparable to a clean-room implementation.

These are open questions, not negative findings.

## 6. Relation to current R1 design

R1 should test the sampling mechanism as an isolated primary object:

> At equal retained budget, how do coverage-based and comparison sampling strategies differ in retaining legitimate rare behaviour versus injected recording noise, and what downstream change appears under one fixed discovery pipeline?

Implications:

- The measurement contract must define retained unit and noise labels before coding.
- The primary downstream miner should be one fixed PM4Py pipeline (recommended IM); IMf is only a sensitivity check if time permits.
- Synthetic logs with explicit ground truth are preferable for the primary experiment; real logs are stress tests, not the source of causal identification.
- “EdgeIM replication” must be described as a bounded, EdgeIM-inspired component audit unless the missing details are recovered and independently implemented.

## 7. Minimum user reading / ownership checkpoint

Before B1 measurement-contract freeze, the user must personally read and annotate at least:

1. Abstract and introduction: exact motivation and paper-level claim.
2. Method section containing the sampling algorithm: every input, state variable, selection rule, termination rule, and output.
3. System/architecture section: what is local versus global and what is actually aggregated.
4. Experimental setup: datasets, preprocessing, miner, parameters, metrics, repetitions/seeds.
5. One results table and its surrounding text: what comparison is genuinely identified.

The user’s note should mark each statement as one of:
`PAPER-TEXT`, `USER-INFERENCE`, `AGENT-SUMMARY`, `UNKNOWN`.

## 8. Seven-field paper note checklist

- Core claim: provisional architecture/cost-preservation claim above; exact wording pending paper read.
- Mechanism: three stages above; algorithm-level details open.
- Pre-result prediction: Section 4, to be rewritten by user after reading.
- Missing/under-specified details: Section 5.
- Paper text vs inference: evidence boundary and labels in Sections 1–3/7.
- Relevance to R1: Section 6.
- Most questionable/verifiable point: whether the feature-preserving rule’s retention advantage survives controlled recording noise at equal retained budget.

## 9. Gate recommendation

A2 should be marked `CONDITIONAL-PASS` only for bibliographic/abstract orientation. It is **not** sufficient to freeze B1 or authorize code. B1 may consume this note only after the user supplies a paper-anchored method note or explicitly accepts the missing-text risk and downgrades R1 to a mechanism audit based on recoverable evidence.
