# Bridge Scheme Evaluation Framework - SOL Pause Handoff

**Date**: 2026-09-02 22:30 Asia/Taipei  
**Task**: `TASK-20260830-004`  
**Window / author marker**: `SOL` (Codex independent review window)  
**Type**: architecture evaluation framework / discussion pause handoff  
**Status**: `ARCHIVED / RECOVERABLE / SOL-LABELED / FABLE-SEPARATE / DISCUSSION-ONLY / UNAPPROVED / NO-EXECUTION-AUTHORITY`  
**Write owner**: `SOL` window only

## Section 0 - TL;DR

The user asked for a detailed explanation of how to analyze and evaluate the proposed
`EvoAgent A-min + T2 replication-plus` structure, then explicitly requested an archive
before answering the remaining priority question.

This file preserves the evaluation method, provisional findings, assumptions, costs,
failure conditions, current cursor, and the one pending question. It does not approve the
proposal, assign a final score, authorize downloads, or authorize implementation.

## Section 1 - Provenance And Isolation

### 1.1 Immediate conversation input

The user asked:

> 先详细给我讲讲？我应该从哪些方面去分析和评估这个方案？

SOL explained the scheme through hard gates, weighted dimensions, teacher/research/time
views, horizontal positioning, and rejection conditions. The final unresolved question was:

> 如果时间发生冲突，是否同意始终保住 T2 研究工件，把 EvoAgent A-min 缩到
> 8-12 小时甚至降级，而不是反过来？

Before answering, the user said:

> 先存档。

Therefore the question remains `PENDING`; no preference is inferred.

### 1.2 Relationship to earlier archives

This file advances only the SOL discussion cursor from:

- `progress/handoff/2026-09-02__bridge-requirements-realignment__sol-review-pause-handoff.md`.

It does not overwrite, edit, supersede, or silently merge the parallel Fable/Claude files,
including:

- `progress/handoff/2026-09-02__bridge-requirements-realignment-pause__handoff.md`;
- `progress/decisions/2026-09-02__research__bridge-requirements-realignment-and-edgeim-slice-proposal.md`;
- the Fable-owned scratch files, planning log, shared task log, handoff index, or
  `/mnt/d/MyResearch/CROSSWINDOW.md`.

The earlier Fable proposal and the SOL recommendation remain separate, unapproved inputs.
Any later reconciliation must preserve both provenance labels.

## Section 2 - Decision Being Evaluated

The current SOL discussion base is a `1+1` structure, not two equally sized projects:

```text
EvoAgent A-min
  -> independently rebuild one bounded engineering micro-slice
  -> produce contribution and live-explanation evidence

T2 replication-plus
  -> PN / DFG / IM / alignment foundation checkpoint
  -> bounded clean-room reimplementation of public EdgeIM stages
  -> synthetic-ground-truth sampling robustness experiment
  -> secondary real-log stress check without ground-truth claims
  -> delayed cold replay and unseen perturbation
```

The two parts answer different admission questions:

| Part | Primary signal | Question it answers | Must not claim |
|---|---|---|---|
| `EvoAgent A-min` | engineering ownership | Can the user independently build, debug, modify, and explain a relevant system slice? | research novelty or ownership of the existing AI-assisted full repository |
| `T2 replication-plus` | research readiness | Can the user learn foundations, reconstruct a published method within public detail, test a falsifiable question, and judge evidence? | full official EdgeIM reproduction, new method paper, or blank-slate discovery |

The parts inside T2 also have distinct duties:

| Layer | Duty |
|---|---|
| foundation | establish DFG, Petri-net, Inductive Miner, alignment, fitness, and precision understanding |
| bounded reenactment | independently implement only the EdgeIM behavior recoverable from public descriptions |
| research experiment | evaluate one preregistered sampling-robustness question using known synthetic truth |
| external stress evidence | check behavior on Sepsis or another real log without pretending to know ground truth |
| ownership | delayed cold replay, unseen perturbation, contribution ledger, and failure diagnosis |

## Section 3 - Evaluation Method

Use three layers in order:

1. hard gates: a failed gate forces scope reduction or rejection;
2. weighted dimensions: compare viable alternatives after all hard gates pass;
3. failure simulation: verify that a negative result or blocked dependency still leaves a
   credible deliverable.

### 3.1 Five hard gates

| Gate | Evaluation question | Evidence required before PASS |
|---|---|---|
| target relevance | Can Lu-group readers see the connection within about 30 seconds? | one direct, factual sentence connecting the artifact to EdgeIM/process mining/PN-IM work |
| minimum research loop | Are input, method, baseline, metric, and verdict all present? | repeatable run plus explicit support/reject/inconclusive rule |
| user ownership | Can the user rebuild, explain, predict, modify, and diagnose it without AI or the old toy? | delayed cold start, live explanation, and unseen change |
| honest claim ceiling | Does the result avoid depending on unavailable official code or undisclosed AI priors? | `bounded reimplementation` wording, prior disclosure, and unresolved-detail list |
| schedule robustness | Can one failure occur while still leaving time to close the package? | explicit downgrade path and at least 20 percent protected buffer |

No weighted score can compensate for a failed hard gate.

### 3.2 Weighted scorecard after the gates

Proposed weights are a discussion aid, not an approved formula:

| Dimension | Weight | What to inspect | Current provisional state |
|---|---:|---|---|
| direct Lu-group relevance | 20 | paper, vocabulary, method family, and one-sentence fit | high for EdgeIM anchor |
| genuine user ownership | 20 | independent decisions, code, explanation, and replay | not yet established |
| research closure | 15 | falsifiable hypothesis, controls, counterevidence, verdict | structurally plausible, unexecuted |
| foundational skill signal | 15 | PN semantics, IM logic, alignment/model/log moves, metric interpretation | must be retained explicitly |
| reproducibility | 10 | data/version/identity/timestamps/missingness/transformation/seed/scope | designable, not yet frozen |
| schedule feasibility | 10 | dependency risk, context switching, buffer, downgrade | plausible only under strict scope |
| presentation friction | 5 | how much unfamiliar context the reader must learn first | low for T2; medium for A-min |
| residual value after failure | 5 | useful artifact if the main empirical claim fails | potentially high |

Do not assign a final numeric score until the user decides the priority between T2 and
A-min and the newest direct sources are locally checked.

## Section 4 - Four Evaluation Viewpoints

### 4.1 Intended supervisor viewpoint

Test whether the package answers four likely questions with little interpretation cost:

1. Is it directly related to the group's work?
2. What technical layer does the student actually understand?
3. Which decisions and implementation are genuinely the student's?
4. Is the next mentoring step concrete and inexpensive?

The preferred evidence order is:

```text
foundation understood and hand-worked
-> public method independently reconstructed within stated limits
-> mismatch or missing detail diagnosed honestly
-> one narrow question tested with controls
-> positive, negative, or inconclusive result defended
```

### 4.2 Research-validity viewpoint

A viable `replication-plus` experiment must specify:

- the exact falsifiable hypothesis;
- independent and dependent variables;
- the source and independence of ground truth;
- matched-budget baseline rules, especially retained-trace count;
- random ordering and seed policy;
- separation of sampling, discovery, and metric effects;
- separate perturbation families rather than one undifferentiated noise rate;
- support, reject, and inconclusive thresholds.

Synthetic logs generated from a known process model are the proposed primary evidence.
Sepsis is secondary stress evidence because it does not expose clean process ground truth.

### 4.3 Learning and ownership viewpoint

The work is not user-owned merely because the user reruns generated code. Ownership needs
evidence that the user can:

- explain why each representation and baseline was chosen;
- predict outputs before execution;
- reconstruct the core after a delay;
- modify one assumption or perturbation without copying;
- diagnose a failure and compare an alternative;
- identify AI-authored scaffolding and prior ideas explicitly.

The existing EdgeIM toy remains a disclosed prior and quarantined reference. Quarantine can
reduce copying, but it cannot turn an already supplied hypothesis into a blank-slate idea.

### 4.4 Delivery and audience viewpoint

The public package should be judged by whether a reader can verify it without first learning
the entire EvoAgent architecture. T2 should therefore stand alone. A-min is separate
engineering evidence and should not become a prerequisite for understanding the research
artifact.

## Section 5 - Current Technical Risks And Corrections

1. EdgeIM is primarily process discovery and data engineering, not the complete original
   reference-model-to-alignment-to-deviation T2 loop. A thin but real PN/IM/alignment
   checkpoint must remain.
2. The old local receipt calls the artifact a behavior reenactment toy and says absolute
   Table II/III values are not directly comparable. Missing custom fall-through behavior is
   an unresolved dependency.
3. The sampling-noise weakness already appears in AI-authored local analysis. The legitimate
   ownership claim is independent derivation, implementation, preregistration, evaluation,
   interpretation, and diagnosis under a disclosed prior.
4. Direct experimental neighbors should come from process discovery and event-log sampling.
   Agent-runtime assurance systems belong only in long-term motivation.
5. The newly located 2026 `sigRank` work means matched-retention comparisons and a current
   neighbor review are required before freezing baselines.
6. A minimal data/reproducibility contract remains necessary even after T3/T4 leave the
   external deliverable.

## Section 6 - Capacity And Scope Test

The discussion used the following provisional effort ranges:

| Work block | Provisional effort |
|---|---:|
| EvoAgent A-min | 12-16 h |
| PN / IM / alignment foundation | 12-16 h |
| bounded EdgeIM reimplementation | 18-24 h |
| synthetic experiment and controls | 18-24 h |
| delayed replay and unseen perturbation | 12-16 h |
| README, brief, email, and repository closeout | 8-12 h |

Raw total: about 80-108 hours. With a 20 percent failure reserve: about 96-130 hours.
This is only conditionally feasible before a mid-to-late September checkpoint. It assumes:

- one A-min slice only;
- no attempt to recreate the entire EvoAgent repository;
- no full nine-dataset EdgeIM reproduction;
- no full processing of all 255 archived material rows;
- no T3/T4 implementation;
- no expansion from an interesting result into a new method during this cycle;
- normal academic obligations are preserved rather than treated as expendable capacity.

## Section 7 - Horizontal Positioning

| Level | Typical evidence | Relation to this proposal |
|---|---|---|
| course/notebook project | code runs, screenshots, limited interpretation | target must exceed this |
| strong pre-group artifact | independent implementation, controls, discrepancy analysis, replay, live defense | minimum acceptable level |
| replication-plus study | the above plus a narrow hypothesis, ground truth, counterevidence, and verdict | intended target, at entry scale |
| method paper | new method, strong baselines, broad evaluation, statistics, peer review | explicitly not promised |

The proposed public ceiling is therefore an entry-scale `replication-plus learning study`,
not an official EdgeIM reproduction and not a new method paper.

## Section 8 - Rejection And Downgrade Triggers

Re-scope or reject the scheme if any of the following occurs:

- the user can only rewrite the old toy by imitation and cannot defend design choices;
- unavailable EdgeIM details make the primary conclusion unjudgeable;
- current literature already contains a materially equivalent experiment and no honest
  learning contribution remains;
- context switching leaves both A-min and T2 incomplete;
- no minimal synthetic-ground-truth experiment exists by the internal midpoint;
- the public artifact depends on substantial AI-generated code for its credibility;
- explaining relevance to the group requires several paragraphs of unfamiliar background.

The downgrade order is intentionally unresolved until the user answers the priority question.

## Section 9 - Done, Not Done, And Current Cursor

### Done in this discussion

- separated the jobs of A-min and T2;
- defined five hard gates and an eight-dimension scorecard;
- evaluated supervisor, research, ownership, delivery, capacity, and horizontal-position views;
- documented the main technical risks, claim ceiling, and rejection triggers;
- preserved the discussion in this SOL-specific file.

### Not done

- no user priority between T2 and A-min has been recorded;
- no final score has been assigned;
- neither the Fable proposal nor SOL structure has been approved;
- no newest-source acquisition or local source-level review has started;
- no architecture specification, schedule, repository, code, experiment, or public package
  has been created;
- no shared Fable-owned or controller-owned file has been changed;
- no staging, commit, push, reset, clean, or merge has occurred.

Current cursor:

```text
SOL evaluation framework explained
-> user requested archive before answering priority question
-> framework archived separately
-> next action is exactly one priority question
```

## Section 10 - Recovery Reading Order

1. this file;
2. `progress/handoff/2026-09-02__bridge-requirements-realignment__sol-review-pause-handoff.md`;
3. `progress/handoff/2026-09-02__bridge-requirements-realignment-pause__handoff.md` for the
   separate Fable proposal;
4. `progress/handoff/2026-08-31__bridge-current-state-and-reference-assets__handoff.md` for
   the previous project authority;
5. `research/papers_lu/teardown-joint-20260813/07_EDGEIM.md` and
   `research/papers_lu/teardown-joint-20260813/repro/edgeim/README.md` for technical claim
   boundaries;
6. `research/tracebridge_full_spectrum_20260830/08_materials/DOWNLOAD_RECEIPT.md` for
   acquisition boundaries.

## Section 11 - Next Action And Explicit Boundaries

The only next question is:

> If time conflicts, should T2 remain the protected primary artifact while EvoAgent A-min is
> reduced to 8-12 hours or downgraded?

Do not ask about incremental downloads until this priority is settled. After it is settled,
downloads still require separate user approval and a non-colliding SOL destination policy.

Until then:

- do not edit Fable/Claude archives or shared controller files;
- do not treat this framework as an approved decision;
- do not download sources, install dependencies, or run third-party code;
- do not create the public repository, research code, experiments, or final schedule;
- do not use the old AI toy as user-owned evidence;
- do not stage, commit, push, reset, clean, or merge.

## Section -1 - Archive Self-Review

| Check | Result |
|---|---|
| unique SOL-labeled path, absent before creation | PASS |
| separate from Fable files and shared indexes/logs | PASS |
| proposal, evidence, and user decisions kept distinct | PASS |
| evaluation dimensions and tradeoffs recoverable | PASS |
| costs, risks, counterevidence, and failure conditions included | PASS |
| one pending question and next action explicit | PASS |
| no temporary persistence path | PASS |
| no implementation or download authority inferred | PASS |
