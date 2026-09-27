# Round 2 shortlist (11 research agents, 2026-09-26)

Synthesis of the second round of idea generation: 11 agents, one per angle; the patch-diffing
agent's report was cut off partway through. Superseded by the 131-agent tournament in
`tournament/`, which rejected several of these (see its kill list), but kept here for the record.
Figures and dates were reported by the agents and were not independently checked.

## Four ways to show *why* fixes wait (found independently by several agents)

1. **Same fix, different risk.** Keep the patch identical, vary only its risk or the proof it needs,
   and measure the delay.
2. **Burned once, slower after.** A public breakage raises perceived risk while attack pressure stays
   the same; a slowdown afterwards is fear.
3. **Written excuses checked against what happened.** Formal "we can't patch, it would break"
   records, followed to see whether the patch broke anything when it went in.
4. **What people give up to avoid a change.** Money paid to stay on old versions; fixes left in test
   mode for years.

## Top 7 (round 2)

| # | Idea | What it shows | Cost |
|---|---|---|---|
| 1 | Fear Tax, then The Cliff | Fear in dollars (extended-support fees), then whether it was justified at forced upgrades | 2–4 mo |
| 2 | Qualification Clock | Time to prove a change safe: same Microsoft patch, lag until medical/OT vendors approve it | 2–4 mo |
| 3 | Safe But Stuck | Fixes left in test mode (DMARC p=none, CSP-Report-Only, MTA-STS testing) | 6–9 mo |
| 4 | Burn Effect / Known-Issue Shock | Adoption of the next fix after a public breakage | 3–12 mo |
| 5 | Patch Weather | Public pre-registered forecast of which updates will regress | 6 mo + 1 yr |
| 6 | Breached With the Fix on the Shelf | Aggregate link between ransomware victims and long-available fixes | 6–9 mo |
| 7 | The Deviation Files | FedRAMP "operational requirement" exceptions vs what happened later | 12–24 mo |

## Risks raised

- The evidence could go against belief 2: prior work (Dissanayake et al. 2022) found coordination
  delays mattered most; Equifax and Log4j reviews point to unknown assets.
- Downloads and scans are not deployments; comparisons within one system or repo keep them credible.
- Many sources could not be verified from the cloud environment (proxy blocks).

## What the tournament later said about these

Killed: Fear Tax (upgrade effort, not fear, drives it), Safe But Stuck (safety of enforcing can't be
computed from outside), standalone Patch Weather (too few regressions to score monthly), Breached
With the Fix on the Shelf (re-identifies victims), Deviation Files (FOIA too slow). Kept in some
form: Qualification Clock (as "The Proof Bill"), Burn Effect (as "Same Fix, New Warning").
