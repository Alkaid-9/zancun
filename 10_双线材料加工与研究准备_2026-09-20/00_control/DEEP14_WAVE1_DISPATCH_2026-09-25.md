# Deep14 wave 1 dispatch receipt · 2026-09-25

The controller froze HEAD/worktree and three PDF hashes in `DEEP14_SCOPE_2026-09-25.md` and `R2_C0_2026-09-25.md` before dispatch. Spawned agents were required to be read-only, independent, and terminal-once; the environment fixed their model at `gpt-5.6-sol / xhigh` (not the user's suggested `gpt-6-sol / xhigh`).

| task | frozen paper | result | accepted research claims |
|---|---|---|---|
| deep_pnulock | PNULock, SHA-256 `a6cb64b424d61346448ee5ea567f551c931ca844758fe8081f2b4013251413ac` | TRANSPORT_ERROR: stream disconnected / response-body decode error | 0 |
| deep_sbpn | SBPN, SHA-256 `14d8ed2bb54bc0e554c7d34f2922a0e8944d7d43a7fbd4916671ca806e4c8ecd` | same TRANSPORT_ERROR | 0 |
| deep_contragent | ContrAgent, SHA-256 `b338efa71c6ae3843200345024967b60ef2d3cc40a806b52c77b41e1864269e3` | same TRANSPORT_ERROR | 0 |

All three returned no usable paper report. No worker-authored files were accepted and no model usage amount was available from these errors. Do not retry the same oversized full-paper prompt blindly. Fallback: controller reads one frozen PDF at a time, creates only source-checked scoped deliverables, then resumes agents only with smaller bounded independent checks if the route recovers. None of these failures modifies learner work, closes the original P1 gates, or counts as a completed deep dissection.
