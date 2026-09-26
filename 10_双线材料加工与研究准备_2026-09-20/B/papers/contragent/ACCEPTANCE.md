# ContrAgent scoped acceptance receipt · 2026-09-25

**Overall: PARTIAL / SOURCE-REVIEWED-BY-CONTROLLER / PEER-REVIEW-OPEN / EXECUTABLE-NOT_RUN.** This is the first 1/14 paper package, not completion of the 14-paper deep-dive. The first dedicated worker failed with a stream/body transport error and delivered **no** report. This receipt must not be relabeled as heterogeneous Agent verification or as reproduced author results.

| Gate | Check performed | Evidence | Result / next action |
|---|---|---|---|
| Identity/source | Local PDF physically exists; cover authors/date/version match frozen SHA-256 | `sources.tsv`; `00_control/R2_C0_2026-09-25.md`; PDF p.1 | `SOURCE-LOCAL-PASS`; external/arXiv/repo availability not checked |
| Claim coverage | Abstract + 3 contribution bullets + §2–§7 + Appendix A–F mapped to 36 claim rows | `claims.tsv`; `analysis.md` §1,§5; PDF pp.1–13 | `CONTROLLER-SCOPED-PASS`; underlying prior-work papers and raw datasets not independently checked |
| Formal semantics | Def.1/3/4, Problem1, Eq.(1)–(3) read; Equation overbars cross-checked visually | PDF rendered p.3; `analysis.md` §2; CA-05–17 | `CONTROLLER-SCOPED-PASS`; independent reviewer still required |
| Four experimental claims | Values/denominators transcribed distinctly; Tables 2,3,7,8,9 visually checked | PDF rendered pp.6,7,13; prose pp.7,8,12 | `AUTHOR-REPORT-SOURCE-CHECKED`; original data/author code not run |
| Limitations | Human-reviewed contracts, observation-channel trust, semantic residuals and non-rollback distinction preserved | PDF p.8 Limitations + pp.2,5 Def1/§5.2; CA-26 | `SOURCE+EXPLICIT-INFERENCE`; return/effect point is our inference, not author theorem |
| P2 falsification candidate | Two fixtures name predicate vocabulary, hidden difference, independent label, and a simple FSM comparator | `fixtures/predicate_blindspot_pairs.json`; `analysis.md` §4 | `SPEC_ONLY`; object-aware checker and host-effect pair not independently executed |
| Executable P3 / reproduction | No code, fixture runner, official repository checkout, benchmark, or LLM evaluated | No `runs/<id>` or executable tests from this package | `NOT_RUN`; do not claim author reproduction or experimental protection |
| External/reviewer verification | Three child workers were dispatched but stream disconnected | `00_control/DEEP14_WAVE1_DISPATCH_2026-09-25.md` | `OPEN`; rerun only bounded, short independent checks if route stabilizes |
| Learner/research claim ceiling | No EX-05 / ledger / G0 / EX-06 / paper-to-JINZU ability changed | `DEEP14_SCOPE_2026-09-25.md`; package only under `B/` | `UNCHANGED`; candidate bridge is not a tested research direction |

## Mandatory independent questions before upgrading this paper

1. Confirm the exact Eq.(1) overbars and Eq.(2)–(3) join/meet from rendered p.3; flat text has lost negation glyphs.
2. Trace the difference between Table 2 task-level `+0.135s`, Table 3 replay `0.16ms/call`, and Table 8 hot-path distributions; check author hardware and denominators.
3. Challenge whether our first fixture's *entire* frozen AP sequence is identical, not just the final visible row. Try adding `Match(order_id,approved_id)` to show the failure is a missing-field choice, not a theorem against the paper.
4. For the second fixture, identify the tool/host's actual effect-commit point; no assertion of rollback or physical side effects is accepted without host evidence.
5. Check author code/version and benchmark raw inputs separately if moving from source-based claims to reproduction. Never infer repository status from the PDF footnote alone.

Pass through 1–4 with recorded evidence for scoped falsification; pass through 5 plus a reproducible run/independent oracle only if claiming any executable or reproduction status. Until then keep this paper `PARTIAL`, even though all 13 PDF pages were reviewed.
