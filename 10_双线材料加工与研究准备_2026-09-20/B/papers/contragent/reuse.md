# Scoped reuse proposal · not an implemented monitor

## Source-derived interface (CA-05–17,26)

```text
Input: immutable tool-call/return event sequence Σ*; explicit context-key update rule κ;
       numeric counters ρ; frozen predicate vocabulary V and parameter values;
       reviewed A/G contracts; event/return timing and host-side effect contract.
State: recorded prefix τ; κ; ρ; one assumption and one guarantee monitor per contract;
       per-contract and aggregate verdicts.
Grounding: P(s,a,c) -> Boolean for each observed event and selected predicate.
Output: before-call online pass/block (+ contract attribution and response),
        and offline pair (venv,vag) for a fixed recorded trace.
Invariants to check: same input trace + same grounding + same library => same prefix verdict;
        blocked event is not appended to *monitored* prefix; assumption and guarantee
        failures have distinct attribution.
Exceptions / UNKNOWN: missing or duplicated call/return, stale context, counter drift,
        ambiguous NL contract, unverifiable content predicate, external effect before return,
        unmatched asynchronous event, unexpected agent/environment control boundary.
```

The paper describes this interface but does not deliver a verified host implementation for our target domain. The two local fixture pairs are intentionally synthetic and test information sufficiency/side effects; they are **not** benchmarks in the original PDF. The strongest simple comparator for the first pair is a version-aware object-ID keyed FSM, not an LLM-only grader. All comparators must receive the **same declared visible fields** before any superiority claim.

## Consumer and guardrails

- Potential consumer: a future T3-lite observable-interface specification or training card after a controller accepts the source claims; no course PASS or live runtime gate follows.
- A per-call checker that ignores order/history/count is not an adequate baseline for temporal claims (PDF p.11 Table 5). Conversely, an object-aware FSM may already solve a chosen order-approval task: test it before claiming ALTLf is needed.
- Performance comparisons must retain four benchmark populations, paired tasks/metrics and hardware. SOPBench p.6 Table 2 reports **seconds added per task**; Appendix E Table 8 p.13 reports **milliseconds per hot-path event**. AgentDojo Table 3 is replay of recorded traces; prospective live-intervention utility requires a separate experiment.
- Future runtime run: freeze fixtures+independent expected outcomes before code; capture actual command/cwd/Python and dependencies/input+code hash/exit/raw stdout+stderr/output hash. This paper package has **no such run**.
- Do not use this interface to infer semantic intent safety, complete information-flow protection, atomic rollback, unchanged external business state, whole-MAS safety, novelty, or author-code reproduction.
