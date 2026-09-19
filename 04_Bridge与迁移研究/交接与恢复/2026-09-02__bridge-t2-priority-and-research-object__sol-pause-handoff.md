# Bridge T2 Priority And Research Object - SOL Pause Handoff

**Date**: 2026-09-02 23:05 Asia/Taipei  
**Task**: `TASK-20260830-004`  
**Window / author marker**: `SOL` (Codex independent review window)  
**Type**: user-decision receipt / architecture alternatives / user-stop handoff  
**Status**: `ARCHIVED / RECOVERABLE / SOL-LABELED / FABLE-SEPARATE / USER-STOP / PARTIAL-DECISION / NO-EXECUTION-AUTHORITY`  
**Write owner**: `SOL` window only

## Section 0 - TL;DR

The user selected priority option `A`: the T2 research artifact is the protected primary
deliverable; EvoAgent A-min is auxiliary and may be reduced or downgraded when time conflicts.

SOL then presented three candidate T2 research objects and recommended `R1`, an EdgeIM
sampling-mechanism audit. The user did not approve or reject `R1`; the user requested an
archive and said work will continue tomorrow.

No download, implementation, experiment, public-repository creation, shared-file edit,
commit, or push is authorized by this decision.

## Section 1 - Provenance And Archive Isolation

### 1.1 Immediate user decisions

The previous SOL archive ended with one priority question:

> If time conflicts, should T2 remain the protected primary artifact while EvoAgent A-min is
> reduced to 8-12 hours or downgraded?

The user answered:

> A

SOL interpreted option A exactly as previously offered:

- protect the T2 research artifact;
- permit EvoAgent A-min to shrink to 8-12 hours or downgrade;
- do not allow A-min completion to block T2 completion.

The user later said:

> 先存档，明天继续

This is a stop instruction. The next research-object question remains unanswered.

### 1.2 Relationship to previous SOL files

This file advances the SOL-only cursor from:

1. `progress/handoff/2026-09-02__bridge-requirements-realignment__sol-review-pause-handoff.md`;
2. `progress/handoff/2026-09-02__bridge-scheme-evaluation-framework__sol-pause-handoff.md`.

It does not overwrite, edit, supersede, or merge the separate Fable/Claude archives,
decisions, scratch files, planning log, shared task log, handoff index, or
`/mnt/d/MyResearch/CROSSWINDOW.md`.

The user's option A is recorded here as a SOL discussion decision. Reconciliation into the
shared project decision surface remains a separate controller action.

## Section 2 - Consequences Of Priority A

The decision fixes resource and downgrade order, but not the detailed experimental design.

### 2.1 Protected T2 properties

The following T2 elements take priority over A-min:

- a narrow, falsifiable research question;
- PN / DFG / IM / alignment foundational learning and assessment;
- a fair controlled experiment with explicit baselines;
- known or bounded ground truth;
- result interpretation with support/reject/inconclusive outcomes;
- delayed cold replay and an unseen perturbation;
- a self-contained research repository and honest public claim ceiling.

### 2.2 A-min downgrade policy

EvoAgent A-min remains a candidate engineering-ownership signal, not a co-equal research
mainline.

Provisional policy:

1. cap A-min at 8-12 hours when it conflicts with T2;
2. keep its repository, claim, and acceptance evidence separate from T2;
3. do not make T2 depend on A-min data, code, or completion;
4. downgrade A-min before removing T2 foundations, the primary controlled experiment, or
   ownership acceptance;
5. do not interpret this policy as approval to choose or implement the A-min slice.

### 2.3 Provisional T2 downgrade order

If time is insufficient, the candidate downgrade order is:

```text
second real-world dataset
-> optional newer baseline implementation
-> EvoAgent A-min depth
-> EvoAgent A-min itself
```

The protected T2 core should not be reduced until its exact research object and acceptance
criteria are approved. This order is a SOL proposal, not yet a shared frozen rule.

## Section 3 - Three Candidate T2 Research Objects

### R1 - EdgeIM sampling-mechanism audit (SOL recommendation)

```text
known synthetic process and event log
-> multiple sampling strategies at matched retained size
-> one common PM4Py IM/IMf downstream pipeline
-> DFG, Petri-net, alignment, and quality assessment
```

Scope:

- independently implement EdgeIM's coverage-sampling mechanism and only the public,
  determinate statistics needed to test it;
- compare it with no sampling, matched-size random sampling, and a frequency-aware baseline;
- consider `sigRank` only after a bounded source and feasibility check;
- use a common downstream miner to isolate sampling effects;
- use synthetic ground truth as primary evidence and a real log only as secondary stress
  evidence.

Advantages:

- strongest isolation of the research variable;
- least dependence on unpublished EdgeIM Stage 3 fall-through behavior;
- cleanest link between hypothesis, baselines, metrics, and verdict;
- narrower and more feasible within the protected T2 budget.

Costs and claim ceiling:

- cannot be called a complete EdgeIM reproduction;
- public wording should be an EdgeIM-inspired component audit or bounded replication-plus
  learning study;
- the known AI-authored noise hypothesis remains a disclosed prior.

### R2 - Bounded EdgeIM full-pipeline reenactment

Scope:

- reconstruct sampling, local `(S,E,R)` summaries, aggregation, and process discovery from
  published details;
- then add the sampling-robustness experiment.

Advantages:

- most visibly resembles the Lu-group paper;
- produces a more complete end-to-end demonstration if successful.

Risks:

- unpublished/custom fall-through details may prevent meaningful Table II comparison;
- sampling effects and discovery-implementation effects become confounded;
- substantially higher schedule risk and a greater chance of spending time on an
  unjudgeable mismatch.

### R3 - Agent-trace conformance study

Scope:

- derive a reference process model for a bounded EvoAgent trace slice;
- perform alignment/conformance and deviation analysis directly on agent traces.

Advantages:

- strongest connection to the long-term T2 destination;
- directly exercises reference-model-to-alignment-to-deviation concepts.

Risks:

- higher explanation cost for the intended Lu-group reader;
- weaker immediate continuation from a specific Lu-group paper;
- reference truth and evaluation validity are harder to establish;
- risks coupling the protected T2 artifact back to the AI-assisted EvoAgent asset.

## Section 4 - Why SOL Recommends R1

R1 is recommended because it preserves a direct EdgeIM connection while moving the research
claim to a component that can be isolated and tested fairly.

The key correction is to compare samplers under the same retained-trace or retained-event
budget and pass every sampled log through the same downstream discovery and evaluation
pipeline. This avoids attributing differences caused by missing or custom Stage 3 behavior to
the sampling mechanism.

R1 also leaves room for a separate, thin PN/IM/alignment foundation checkpoint. That is
necessary because EdgeIM itself is primarily a process-discovery and data-engineering work,
not the complete reference-model-to-alignment-to-deviation T2 loop.

The recommendation remains provisional until the user explicitly selects it.

## Section 5 - Decision State

| Item | State | Meaning |
|---|---|---|
| T2 protected over A-min under time conflict | `USER-SELECTED / SOL-RECORDED` | option A was explicitly selected |
| A-min 8-12 hour cap or downgrade | `DIRECTIONALLY ACCEPTED` | follows the exact option A wording; detailed slice still unselected |
| R1 sampling-mechanism audit | `RECOMMENDED / UNAPPROVED` | next user decision |
| R2 bounded full pipeline | `ALTERNATIVE / UNAPPROVED` | retained for comparison |
| R3 agent-trace conformance | `ALTERNATIVE / UNAPPROVED` | retained for comparison |
| exact hypothesis, metrics, thresholds, datasets, baselines | `NOT-FROZEN` | design follows only after research-object choice |
| new source acquisition | `NOT-AUTHORIZED` | separate later approval required |
| implementation or experiment | `NOT-AUTHORIZED` | no execution may begin |

## Section 6 - Current Cursor And Tomorrow's First Action

Current cursor:

```text
evaluation framework archived
-> user selected priority A: protect T2 over A-min
-> SOL presented R1 / R2 / R3 research-object alternatives
-> SOL recommended R1
-> user requested archive and stop until tomorrow
```

Tomorrow's first action is exactly one question:

> 是否同意以 R1“EdgeIM 采样机制审计”作为 T2 的核心研究对象？

Do not skip ahead to detailed metrics, acquisition, code, or schedule before this question is
answered. If the user selects another option, preserve the stated tradeoffs and redesign from
that choice rather than treating R1 as accepted.

## Section 7 - Recovery Reading Order

1. this file;
2. `progress/handoff/2026-09-02__bridge-scheme-evaluation-framework__sol-pause-handoff.md`;
3. `progress/handoff/2026-09-02__bridge-requirements-realignment__sol-review-pause-handoff.md`;
4. `progress/handoff/2026-09-02__bridge-requirements-realignment-pause__handoff.md` for the
   separate Fable proposal;
5. `progress/handoff/2026-08-31__bridge-current-state-and-reference-assets__handoff.md` for
   previous project authority;
6. `research/papers_lu/teardown-joint-20260813/07_EDGEIM.md` and
   `research/papers_lu/teardown-joint-20260813/repro/edgeim/README.md` for technical claim
   boundaries;
7. `research/tracebridge_full_spectrum_20260830/08_materials/DOWNLOAD_RECEIPT.md` for
   acquisition boundaries.

## Section 8 - Explicit Stop Boundaries

Until the user resumes tomorrow:

- do not ask further design questions or continue analysis;
- do not treat R1, R2, or R3 as approved;
- do not edit the Fable/Claude archives or shared controller files;
- do not download sources, clone repositories, install dependencies, or run third-party code;
- do not select datasets, thresholds, exact baselines, or the A-min slice;
- do not create the public repository, implementation plan, research code, or experiments;
- do not use the old AI toy as user-owned evidence;
- do not stage, commit, push, reset, clean, or merge.

## Section -1 - Archive Self-Review

| Check | Result |
|---|---|
| unique SOL-labeled path, absent before creation | PASS |
| user option A recorded without broadening its meaning | PASS |
| R1 recommendation separated from user approval | PASS |
| R1/R2/R3 alternatives and tradeoffs recoverable | PASS |
| Fable and shared controller files left untouched | PASS |
| tomorrow's first action is one explicit question | PASS |
| user stop boundary explicit | PASS |
| no temporary persistence target | PASS |
| no download or execution authority inferred | PASS |
