# EvoAgent Failure and Evidence: Two Bounded Lessons

This lesson studies two different ways a system description can fail. It is limited to the EvoAgent snapshot and historical records named below. It does **not** claim production frequency, production impact, or a general law about all agent systems.

## Beginner definitions

- **Trigger**: the input or condition that starts a failure chain.
- **Local fault**: the first incorrect or insufficient behavior at one component.
- **Propagation**: how that local problem affects later steps.
- **Invariant**: a rule that must remain true at the point where it applies.
- **Checkpoint**: a durable record of a completed step and its output.
- **Resume semantics**: the precise promise about what a later run restores or reuses. Reusing completed outputs is narrower than restoring an interrupted process.
- **Static evidence**: evidence obtained by reading code without executing the path.
- **Runtime evidence**: evidence obtained by executing a path and recording what happened.

The architectural case uses `EA-SLICE-001`. The epistemic case uses `EA-SLICE-006` and the historical repair record `EA-PDF-FIX`.

## Case A — Architectural claim/contract failure scenario: overreading checkpoint reuse

No current runtime failure caused by a broad resume promise is established here. The supplied evidence also does not identify a current source document or caller that promises full in-flight restoration. Therefore the overbroad interpretation below is a **hypothetical claim/contract failure scenario**, while the narrow implementation behavior is confirmed.

### Fixed failure chain

**Trigger**  
A review task stops after the planning node completed, then `ReviewHarness.resume` is called; a caller or learner hypothetically interprets “resume” as full restoration.

**→ Local fault**  
The local problem is an overbroad claim or unstated contract, not a confirmed component runtime fault. Current static reading shows that `ReviewHarness.resume` delegates to `ReviewHarness.run`, which reconstructs the initial input and lets `ReviewHarness._completed` reuse completed node outputs. No evidence here establishes that current source promises restoration of the entire interrupted runtime state.

**→ Propagation path**  
If that hypothetical broad interpretation is adopted, a caller or learner may assume that in-flight Python/graph state, partially completed external calls, and external side effects were restored or reconciled. The checkpoint evidence establishes none of those broader properties.

**→ User-visible consequence**  
The confirmed consequence is only that completed planning can be skipped/reused after restart. Repeated work, ambiguous external outcomes, and duplicate side effects are possible concerns under additional conditions, but no such current runtime failure or duplication is established: `UNVERIFIED`.

**→ Why tests/review missed it**  
The bounded test `tests/test_production_features.py::test_failed_graph_resumes_after_last_completed_checkpoint` supports only that completed planning is reused/skipped. Historical R2 also proposed a `KeyError` mechanism, but current source behavior `result.update(node(result))` contradicts that mechanism; it is withdrawn and not carried forward. The surviving confirmed fact in `EA-SLICE-001` is narrow completed-output reuse, not full restoration or duplication.

**→ Violated/at-risk claim boundary**  
This is a required claim/contract boundary, not a sourced EvoAgent runtime invariant: documentation and callers may claim only the state that the durable record can reconstruct. For this snapshot, the supported contract is that a completed node output may be reused instead of re-executing that node. Full in-flight restoration and exactly-once external effects remain outside the established contract.

**→ Minimum repair**  
Documentation or API-contract wording should say “rebuild initial input and reuse completed node outputs.” It should explicitly state that current evidence does not establish arbitrary in-flight runtime-state restoration or exactly-once external effects. This is the minimum claim/contract repair for `EA-SLICE-001`.

**→ Systemic repair**  
Optional hardening belongs to the separate retry/idempotency gap `EA-SLICE-004`: retried external actions could use a durable operation identity, atomic completion record, and ambiguous-outcome reconciliation. That proposal is `UNVERIFIED`, and its inclusion does not imply that duplication occurred or that it is required to correct the narrower `EA-SLICE-001` documentation boundary.

**→ Verification needed**  
To strengthen `EA-SLICE-001`, run interruption tests at each node boundary and record exactly which completed outputs are reused versus recomputed. Separately, to evaluate `EA-SLICE-004`, run an ambiguous external-call test using an operation ID and reconciliation record. No current full-restoration failure, external duplication, or passing hardening test is claimed here.

### Evidence boundary

- **Established:** current code shape supports reconstruction plus completed-output reuse: `STATIC-CONFIRMED`.
- **Established:** the named bounded test supports skipping/reusing completed planning: `TEST-CONFIRMED` as registered by `EA-SLICE-001`.
- **Established withdrawal:** the historical R2 `KeyError` mechanism is contradicted by current source and is not carried forward.
- **Did not establish:** that any current source promises full Python/graph-state restoration.
- **Did not establish:** a current runtime failure caused by an overbroad resume claim.
- **Did not establish:** exactly-once reviewer calls, billing, messages, duplicate effects, or production impact; no evidence here is `PRODUCTION-VALIDATED`.

## Case B — Epistemic failure: static audit predicted the wrong first failure

An **epistemic failure** is a failure in what the available evidence lets us know. Here the static audit identified a real missing-document problem, but it did not establish which failure the WSL run would encounter first.

### Fixed failure chain

**Trigger**  
Run `scripts/render_knowledge_base_pdf.py` under WSL while the expected Markdown source is absent and the old Windows-font fallback is used.

**→ Local fault**  
Before the repair, font registration built a path from the Windows-style fallback `C:\Windows`, which was not a valid WSL font path for that run.

**→ Propagation path**  
Execution reached font registration before reading the missing Markdown source. Font loading therefore raised `Can't open file "C:\Windows/Fonts/msyh.ttc"` before the missing-documents path emphasized by static audit could execute.

**→ User-visible consequence**  
The user received a font-file failure rather than the predicted missing-source failure. After repair, the historical run reached the friendly missing-source exit, but real Markdown-to-PDF generation and Chinese-glyph inspection remain `UNVERIFIED`.

**→ Why tests/review missed it**  
The audit read code and correctly noticed that the source file was absent, but static plausibility did not establish runtime ordering in the WSL environment. No recorded end-to-end environment test had established the first failing stack position before execution.

**→ Violated invariant**  
A statement about the **first observed failure** requires execution evidence from the relevant environment; static evidence alone may identify candidate faults but must not be promoted to observed order.

**→ Minimum repair**  
Check source existence before font registration and return a friendly missing-source message. For font lookup, probe explicit WSL-compatible candidates such as `/mnt/c/Windows/Fonts` and report all attempted paths when none works.

**→ Systemic repair**  
Add an environment matrix that separately tests: missing source, missing fonts, successful font registration, non-empty Markdown rendering, output creation, and Chinese glyph inspection. Keep each result separate so one passing branch is not summarized as full PDF success.

**→ Verification needed**  
Provide a real non-empty Markdown source, run the current renderer with the intended interpreter, confirm a non-empty PDF at the intended path, and inspect Chinese text. Until then, current end-to-end rendering is `UNVERIFIED`.

## Evidence ladder for the PDF case

| Level | Established | Did not establish |
|---|---|---|
| `DOC-CLAIM` | The script is intended to render an existing Markdown knowledge base into PDF. | That dependencies, paths, fonts, input, and output work in WSL. |
| `STATIC-CONFIRMED` | The old font-path logic and missing-source path were visible in code; current source checks source existence before font registration and includes a WSL font candidate. | Which fault a historical run encountered first; successful current PDF generation; correct Chinese rendering. |
| `TEST-CONFIRMED` | No bounded automated test is cited here for the current WSL PDF path. | Current WSL behavior, first-failure order, or end-to-end rendering. |
| `RUNTIME-CONFIRMED` | `EA-PDF-FIX` records that WSL font loading failed first in the historical run, then records the repaired friendly missing-source exit. | Portability to another machine; current successful Markdown-to-PDF generation; Chinese glyph correctness. |
| `PRODUCTION-VALIDATED` | Not available. | Production portability, reliability, frequency, and impact all remain unclaimed. |

### Established versus Did-not-establish

**Established**

1. The historical WSL execution encountered font registration before the missing-source failure: `RUNTIME-CONFIRMED` for that recorded run.
2. Current source ordering places the source-existence guard before font registration: `STATIC-CONFIRMED`.
3. A friendly missing-source exit was observed after repair: `RUNTIME-CONFIRMED` for that branch.

**Did not establish**

1. That a real Markdown document currently renders into a PDF.
2. That Chinese glyphs render correctly.
3. That every WSL or Windows environment uses the same font paths or failure order.
4. That the PDF path is `PRODUCTION-VALIDATED`.

## Counterexample exercise

Invent one concrete environment where the repaired reasoning could still fail. Do not answer only “another error may happen.” Use all three fields below.

**Concrete example to test:**

- **Trigger:** a real non-empty Markdown source exists and `/mnt/c/Windows/Fonts` exists, but ReportLab cannot register the selected TTC font file or the font is unreadable.
- **Expected stack position:** after the source-existence guard and during `register_fonts`, before Markdown rendering and PDF output inspection.
- **Evidence needed:** the exact command, interpreter and ReportLab version, resolved font path, full exception/stack trace, exit code, and whether an output PDF was created. If a PDF exists, inspect whether it is non-empty and whether Chinese glyphs render.

**Acceptance rule:** the learner's own counterexample passes only if it names (1) a concrete trigger, (2) where it should appear in the current call order, and (3) the runtime evidence needed to decide whether it occurred. A static guess alone does not pass.

## Transfer check

For both cases, ask two separate questions:

1. What behavior does the current evidence actually establish?
2. What stronger claim is tempting but unsupported?

For checkpoint/resume, the established behavior is completed-output reuse; the historical `KeyError` mechanism is withdrawn, and full runtime restoration or duplication remains unsupported and `UNVERIFIED`. For the PDF case, the historical first failure and friendly missing-source branch were observed; successful current end-to-end rendering is unsupported.
