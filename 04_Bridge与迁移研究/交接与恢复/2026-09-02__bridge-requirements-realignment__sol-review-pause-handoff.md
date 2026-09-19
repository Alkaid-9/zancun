# Bridge->Lu Group Requirements Realignment - SOL Independent Review Pause Handoff

**Date**: 2026-09-02 22:10 Asia/Taipei
**Task**: `TASK-20260830-004`
**Window / author marker**: `SOL` (Codex independent review window)
**Type**: independent architecture review / material-status audit / pause handoff
**Status**: `ARCHIVED / RECOVERABLE / SOL-LABELED / FABLE-SEPARATE / REVIEW-ONLY / NO-EXECUTION-AUTHORITY`
**Write owner**: `SOL` window only

## Section 0 - TL;DR

SOL review is archived separately: old materials are local, newly found sources are not downloaded, and the redesign remains unapproved.

## Section 1 - Isolation From The Parallel Fable Archive

The user explicitly stated that a parallel `Fable` window is archiving similar material and required this archive to be separately marked. This file therefore does not overwrite, edit, supersede, or silently merge any of the following files already present in the workspace:

- `progress/handoff/2026-09-02__bridge-requirements-realignment-pause__handoff.md`;
- `progress/decisions/2026-09-02__research__bridge-requirements-realignment-and-edgeim-slice-proposal.md`;
- `research/tracebridge_full_spectrum_20260830/00_control/_scratch/2026-09-02__bridge-direction-provenance__scratch.md`;
- `research/tracebridge_full_spectrum_20260830/00_control/_scratch/2026-09-02__bridge-redesign-edgeim__scratch.md`;
- `research/tracebridge_full_spectrum_20260830/00_control/BRIDGE_LU_PLANNING_LOG.md`;
- `progress/task_logs/2026/08/2026-08-30__research__bridge-lu-two-week-masterplan-alignment.md`;
- `progress/handoff/INDEX.md` and `/mnt/d/MyResearch/CROSSWINDOW.md`.

Those files are referred to below as the parallel Fable/Claude archive because that is the user's explicit cross-window label. Their own headers identify their write owner as `Claude Code`.

This SOL handoff is an independent review supplement, not the new project authority. Any later reconciliation between the two archives must be explicit and must preserve both provenance labels.

## Section 2 - Scope And Authority Reopened By SOL

SOL reopened the documented authority chain before reviewing the proposed redesign:

1. `progress/handoff/2026-08-31__bridge-current-state-and-reference-assets__handoff.md`;
2. `progress/decisions/2026-08-30__research__bridge-lu-two-week-master-goal-checkpoint.md`;
3. `progress/decisions/2026-08-31__research__bridge-lu-section2-deliverables-acceptance-proposal.md`;
4. `progress/decisions/2026-08-31__research__bridge-mainline-reset-c028-deferred.md`;
5. `progress/decisions/2026-08-31__research__current-user-profile-checkpoint.md`;
6. the EdgeIM teardown, old EdgeIM toy receipt, pyBeamline teardown, material manifest, and EvoAgent repository state.

The authority chain still says:

- Sections 1 and 2 are frozen specifications, not completed deliverables;
- Section 3 is an optimization-open working base;
- execution and experiments have not started;
- D1-D5 and A1-A4 have not passed;
- the current task is design review unless the user later grants execution authority.

Repository identity observed by SOL:

- outer repository: `/mnt/d/MyResearch`, branch `main`;
- research repository: `/mnt/d/MyResearch/MAS_Safety_Project`, branch `master`, observed HEAD `3779b81075ba91bfc80d188c410166dde8359f07`;
- EvoAgent repository: `/mnt/d/MyResearch/EvoAgent`, branch `master`, observed HEAD `acc762c7b9c99d389968e2d3280e6e9cc8673aed`.

No repository state in this section authorizes staging, committing, pushing, resetting, cleaning, or merging.

## Section 3 - SOL Review Verdict On The Parallel EdgeIM Proposal

SOL's independent verdict is: do not approve the four proposed decisions as one bundle. The scope reduction is directionally sound, but several claims and comparisons require correction.

### 3.1 What Can Be Retained

- Make T2 the current learning and artifact mainline.
- Remove T4, T3-lite, and T2-to-T4 typed relations from the current external deliverable while retaining them as long-term boundaries.
- Stop treating full processing of 255 archived material rows as a prerequisite; use a question-driven direct-source subset.
- Use EdgeIM as a low-friction paper anchor connected to Lu's process-mining line.
- Retain D3-D5, A2-A4, delayed independent replay, failure records, and a separate public research repository.

### 3.2 What Must Be Corrected

1. Do not call the proposed work a complete independent EdgeIM reproduction. The old receipt states that official code was not available in the checked scope, the implementation was a behavioral reenactment toy, and absolute Table II/III values were not directly comparable. Missing Stage 3 fall-through details remain an unresolved implementation dependency.
2. EdgeIM is process-model discovery, not the original T2 reference-model-to-alignment-to-deviation loop. It can be a T2 foundation slice only if a thin, independently assessed PN/IM/alignment layer is retained.
3. The noise-retention hypothesis is already present in the AI-authored local EdgeIM teardown, and the old toy has already reported feature inconsistency and a reversed precision direction. Code quarantine may prevent copying, but it cannot restore idea-level blank-slate originality.
4. Ownership should therefore be framed as independent derivation, implementation, preregistered evaluation, result interpretation, and failure diagnosis under a disclosed prior, not as independent discovery of the hypothesis.
5. A minimal reproducibility/data contract must remain even if T3/T4 typed relations are removed: dataset version, case/event identity, timestamp semantics, missingness, transformation version, and evaluation scope directly support T2 credibility.
6. The direct comparison set must be process-discovery and event-log-sampling work. Agent-runtime assurance systems such as ProbGuard or VeriGuard are long-term destination context, not experimental baselines for this slice.
7. The user's earlier choice of architecture A cannot be silently replaced by "do not redo EvoAgent." A full rewrite is not feasible, but a separately budgeted, independently rebuilt EvoAgent micro-slice remains a live option.

### 3.3 SOL's Recommended Discussion Base

The recommended replacement is a `1+1` structure, still unapproved:

```text
EvoAgent A-min
  -> one independently rebuilt 12-16 hour engineering micro-slice
  -> separate contribution and live-explanation evidence

T2 research repository
  -> PN / IM / alignment foundation checkpoint
  -> bounded clean-room reimplementation of published EdgeIM stages
  -> synthetic-ground-truth sampling robustness experiment
  -> secondary Sepsis stress check without ground-truth claims
  -> delayed cold replay and unseen perturbation
```

The public claim ceiling would be `replication-plus learning study`, not an EdgeIM method reproduction and not a new method paper.

## Section 4 - Material Download Status At The Pause Point

### 4.1 Previously Archived Material Layer

The existing central download receipt currently records:

- 255 manifest rows;
- 246 rows with local paths and 9 rows without local payload;
- at least 1,144,912,727 bytes of local material;
- 98 repository snapshots, 62 downloaded entities, 82 web snapshots, 12 metadata-only rows, and 1 access-blocked row;
- central manifest SHA-256 `6be9c1fc1b14e8ac96af6b3da6a9e4548ee2afdfd822e57fd477a13a6b113c65`.

This supports `MATERIAL-LAYER-CLOSED` within the recorded boundary. It does not support research saturation, current literature completeness, successful code execution, user learning, or project completion.

Confirmed local examples include:

- EdgeIM teardown, extracted paper text, reproduction plan, toy implementation, and result receipt under `research/papers_lu/teardown-joint-20260813/`;
- the Agent Behavior Mining paper and repository records at central manifest rows `W1A-S043`, `W1A-S045`, and `OSS-REPO-ABM`;
- the ABM repository snapshot at commit `6eaa06bc7eed3fd04d23015dd6a56c58d1b99ef7`;
- the pyBeamline teardown and prior bounded E2 evidence under `research/map/oss_landscape/`.

### 4.2 Sources Found By SOL But Not Downloaded Into The Workspace

The following items were checked through live web access during the SOL review but were not downloaded or added to the central manifest:

1. Xuan Su et al., "Toward Efficient Support for Business Process Event Log Sampling," IEEE Transactions on Services Computing 19(2), 2026, DOI `10.1109/TSC.2026.3665370` (`sigRank`);
2. the public ProM `SoftwareProcessMining` repository path containing the `sampling/sigrank` implementation;
3. Xuan Su et al., "CrossEdgeIM: An Edge-Based Approach for Interactive Robotic Behavior Model Discovery," IEEE Internet of Things Magazine 9(1), 2026, DOI `10.1109/MIOT.2025.3625047`;
4. Dominique Sommers et al., "A ground truth approach for assessing process mining techniques," Process Science 2, 2025, DOI `10.1007/s44311-025-00006-8`;
5. the current 4TU metadata/terms page for the Sepsis Cases event log.

The live check found no discoverable public repository named for the exact EdgeIM paper in the searched GitHub and institutional channels. This is a bounded negative search result, not proof that no official code exists.

Useful source locators retained in this handoff:

- `https://novaresearch.unl.pt/en/publications/edgeim-an-efficient-edge-based-process-model-discovery-technique/`
- `https://run.unl.pt/entities/publication/cfdff734-3844-41a6-952e-74e55e4d092e`
- `https://github.com/promworkbench/SoftwareProcessMining`
- `https://novaresearch.unl.pt/en/publications/crossedgeim-an-edge-based-approach-for-interactive-robotic-behavi/`
- `https://link.springer.com/article/10.1007/s44311-025-00006-8`
- `https://data.4tu.nl/articles/_/12707639/1`

## Section 5 - Why The New Sources Change The Design

- The 2026 sigRank work is a direct, newer sampling neighbor. It evaluates seven sampling techniques plus IMi and points to a public ProM plugin. It must appear in the current-neighbor review; experimental use still needs a bounded feasibility check.
- A fair experiment must compare sampling methods at matched retained-trace counts because EdgeIM coverage filtering has an endogenous output size while sigRank and several baselines use fixed ratios.
- Real-world Sepsis data cannot provide clean injected-noise ground truth. Its official metadata also states that timestamps were randomized while within-trace time differences were preserved. Synthetic data from a known model should be primary; Sepsis should be secondary external stress evidence.
- The synthetic protocol must distinguish behavioral deviations from recording errors and label insertion, deletion, and adjacent-swap perturbations separately.
- Ordering and random seeds are material confounders for greedy feature-coverage sampling and must be preregistered rather than hidden by one deterministic order.

These findings make the parallel proposal valuable as a draft but not yet acceptable as the final Section 3 slice.

## Section 6 - Current Cursor And First Action After Recovery

Current cursor:

```text
requirements re-aligned in conversation
-> parallel Fable proposal archived but unapproved
-> SOL independent review and freshness check archived separately
-> no new source entity downloaded by SOL
-> no architecture decision or implementation authorized
```

First action after recovery:

1. Read this SOL handoff Sections 0, 1, 3, 4, and 6.
2. Read the parallel Fable handoff Sections 0, 3, 4, and 5.
3. Reconcile only factual conflicts first: EdgeIM reproduction ceiling, disclosed AI prior, 2026 sigRank neighbor, ground-truth design, and EvoAgent architecture A.
4. Ask the user whether the revised `EvoAgent A-min + bounded T2 replication-plus` structure should become the next discussion base.
5. Only after that decision, separately ask whether to download the five newly located source entities and agree on a non-colliding destination and manifest policy.

## Section 7 - Explicit Boundaries

- Do not edit or overwrite the parallel Fable/Claude files listed in Section 1.
- Do not register this file in shared `progress/handoff/INDEX.md`, the planning log, the shared TASK-004 log, or `CROSSWINDOW.md` until the primary controller reconciles concurrent ownership.
- Do not download the newly found sources merely because their URLs are recorded here.
- Do not build a public repository, write research code, run an experiment, install dependencies, or execute third-party repositories.
- Do not treat the old material archive as literature saturation or the old EdgeIM toy as user-owned evidence.
- Do not treat either the Fable proposal or the SOL recommendation as approved.

## Section 8 - Recovery Reading Order

1. `progress/handoff/2026-09-02__bridge-requirements-realignment__sol-review-pause-handoff.md` (this SOL supplement);
2. `progress/handoff/2026-09-02__bridge-requirements-realignment-pause__handoff.md` (parallel Fable/Claude pause archive);
3. `progress/handoff/2026-08-31__bridge-current-state-and-reference-assets__handoff.md` (previous project-wide authority);
4. `progress/decisions/2026-08-30__research__bridge-lu-two-week-master-goal-checkpoint.md` and the frozen Section 2 acceptance specification;
5. `research/papers_lu/teardown-joint-20260813/07_EDGEIM.md` and `repro/edgeim/README.md` for EdgeIM claim boundaries;
6. `research/tracebridge_full_spectrum_20260830/08_materials/DOWNLOAD_RECEIPT.md` and `MANIFEST.tsv` for acquisition facts.

## Section -1 - SOL Self-Review Record

| Check | Result | Note |
|---|---|---|
| Unique path / no overwrite | PASS | `sol-review` is present in the filename and the target did not exist before creation |
| SOL/Fable provenance separation | PASS | both labels and all known parallel files are explicit |
| No temporary persistence target | PASS | repository `progress/handoff/` only |
| Done/not-done split | PASS | old acquisition and new web-only sources are separate |
| Decisions vs proposals | PASS | no proposed architecture is marked approved |
| Recovery cursor and first action | PASS | Sections 6 and 8 |
| Boundaries | PASS | Section 7 |
| Shared-file ownership | PASS | no shared index, log, decision, scratch, or cross-window file edited |
| Source locators | PASS | six direct URLs plus local authority paths retained |
| Secrets or large raw output | PASS | none recorded |

## Section -2 - User Approval State

- [x] User explicitly requested an immediate, non-overwriting, SOL-labeled archive.
- [x] SOL archive created as a separate file.
- [ ] User has not approved the Fable proposal, SOL recommendation, new downloads, implementation, experiments, or public release.

