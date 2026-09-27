# Study 1 — "Ready, Green, Waiting"

**Status (2026-09-27): DESIGN ONLY.** No study data has been collected. These files are the
instructions for future agents that will build and run the study on the founder's own computer or a
VM with open internet (not in a Claude Code cloud session — see `06-what-will-not-work.md` §A2).
Items marked UNVERIFIED / BLOCKED in these files must be checked first (implementation Step 0).

## One-page summary

**Question.** Skylayer's belief 2 (`../../thesis.md`): *the blocker on remediation is impact
uncertainty — not speed, prioritization or tooling.* It has no evidence yet. Study 1 tests it with
public behavioural data and is built so that it can lose.

**Setting.** Security fixes that Dependabot or Renovate already wrote as pull requests, that pass the
repository's own CI, but stay unmerged — **only in company-owned repositories that are deployed
services**. The fix is identical across repositories; what varies is the safety evidence shown: a
peer "safe to merge" score (Dependabot compatibility score, Mend Merge Confidence) that can appear or
change while the PR is open.

**Co-primary results.**
- **P1 "Proven safe, still stuck":** share of fixes with own CI green and a displayed peer score ≥90%
  (or High) that are still unfixed after 30 days. **≥35% falsifies belief 2** in this domain; <15% is
  consistent with it.
- **P2 "Silent proof":** does the merge hazard rise when the score appears silently, at moments when a
  human is merging in that repo — versus the same score change when the badge is not displayed
  (placebo)?

**Secondary.** D1 count of green fixes waiting; H2 dose-response/sign test; H3 "hollow green" lab
(tests never touch the changed dependency code); H4 census of written bot-merge rules; H5 breakage vs
severity at the moment of attention; H6 do the scores predict real breakage (reverts, downgrades,
pins)?; H7 companies vs individuals (optional); H8 72-hour Mend cutoff (demoted).

**Company filter.** Tier A = GitHub-verified domain + a registry link to a business (Wikidata
P2037/P856, GLEIF); Tier B = most recent human committers use one corporate email domain. Headline on
Tier A, A+B as robustness; ~300 owners hand-labelled for precision/recall; deployed-service rule
(deployments/CD workflow/container/IaC, not a published library). All frozen in the OSF
pre-registration before any outcome is computed.

**Honest outlook.** Prior work (He et al. 2023; Rombaut et al. 2024: 83% of Dependabot updates have
no score) predicts few score flips and a small effect. In the company-only sample, **P1 looks
feasible (~200–650 proven-safe PRs in 16 weeks, central assumption) but P2 is likely underpowered
(~40–210 flip events vs 631 needed for HR 1.25)**. The founder must choose the fallback (D1/D2 below)
before registration.

**Budget.** ~$250–$700 of the $1,000 cap (BigQuery scans once per month of data, a small always-on
machine for 5–7 months, a small lab). Rules out paid company databases, big labs, commercial IRB if
expensive (06 §F).

**Legal.** Public data only, zero interaction with any repository, usernames hashed at ingestion,
aggregate and open-access publication (GitHub AUP §7), never name repos/companies with unmerged
security fixes, ≤1 req/s with identified User-Agent, **written OK from GitHub before polling badges
at scale, Mend arm off without Mend's written permission**, IRB exemption determination, GDPR LIA and
privacy notice (07).

## Reading order

1. `README.md` — this page.
2. `01-background.md` — thesis link, prior art with statuses, skeptics' objections and fixes.
3. `04-analysis-design.md` — hypotheses, estimands, models, power, gates, pre-registration draft.
4. `03-population-and-company-filter.md` — discovery pipeline, company tiers, service rule, validation, expected counts.
5. `02-data-sources.md` — every source: fields, endpoints, auth, limits, cost, terms, sample queries.
6. `07-legal-ethics.md` — checklist, policy texts, draft letters, data-management plan.
7. `06-what-will-not-work.md` — blocked domains, data limits, rate limits, unverified items, risks, budget exclusions.
8. `05-implementation-plan.md` — the step-by-step task list to execute.

## Execution order for future agents

(Details, schemas, commands, costs and report templates: `05-implementation-plan.md`.)

| step | what | gate / output |
|---|---|---|
| 0 | Set up GCP (quota + budget alerts), token, tools; **verify every UNVERIFIED item** on the open network; re-read prior art full texts | `verification.md`; stop if P2 already published |
| 1 | Send letters to GitHub, Mend, IRB; publish privacy notice (in parallel, day 1) | **G0** legal |
| 2 | Build advisory table (GitHub Advisory DB, OSV, KEV, EPSS) | `advisories.parquet` |
| 3 | GH Archive materialization; bot-PR skeleton; owner tiers; deployed-service filter; **measure supply, outcome-blind** | **G1** supply |
| 4 | Hand-label ~300 owners + 150 repos; precision/recall | **G3** classifier |
| 5 | Freeze code/rules on synthetic data; **file OSF pre-registration** | OSF link |
| 6 | Badge logger on an always-on machine, 16 weeks (only after G0) | **G2** pilot at week 2 |
| 7 | Daily GraphQL hydration; outcomes written masked | |
| 8 | Bot-merge policy census (H4) | POST 1 |
| 9–11 | Retrospective D1/H5/H6, escaped-breakage labels, hollow-green lab | POST 2 |
| 12 | Unmask on the registered date; P1/P2 and the rest; open-access paper | verdict |

## Decisions the founder must make (before Step 5 unless noted)

- **D1 — Primary sample if Tier A is small.** F1 (recommended): headline on Tier A; P2's causal test
  on A+B with Tier A as a consistency check. F2: all Tier A, P2 exploratory. F3: extend logging to
  26+ weeks. (04 §8)
- **D2 — Accept that P2 may only detect large effects** (MDE HR ≈1.5–2.0 in Tier A) and that a null
  there will be reported as "inconclusive", not as a falsification.
- **D3 — Comparison group of individuals and non-company orgs** (H7): include (adds polling load and
  analysis) or drop.
- **D4 — Who labels** the ~300 owners and 150 repos (~20 h): founder + second person, or founder
  confirming LLM pre-labels.
- **D5 — IRB route:** academic co-author's IRB (free, recommended) or an independent IRB (fee may
  exceed budget). Also whether to add an academic co-author at all (helps OA venue and credibility).
- **D6 — Commit to publishing either outcome**, including "proven safe, still stuck ≥35%" which would
  falsify belief 2 in this domain, under Skylayer's name, open access.
- **D7 — Who signs and sends** the GitHub/Mend letters; what to do if GitHub does not reply within
  3 weeks (recommended: run the retrospective parts only; no prospective logging).
- **D8 — Where the logger runs** (own always-on machine vs small VM) and the hard budget cap per
  category (05 Budget).
- **D9 — Retrospective window**: recommended 2025-01-01..2025-10-06 (rich pre-trim payloads).
- **D10 — Data retention** period and who holds the hashing salt.
- **D11 — Whether any Claude/LLM API usage** (e.g. pre-labelling) counts toward the $1,000.

## Later phase (out of scope here)

C3 v2's factorial randomized trial (breakage proof × relevance × matched placebo × no card, then a
tested-rollback arm) on real OS patch approvals with an RMM/patch vendor or design partners — only
if Study 1 does not return an equivalence null, and only with consent, IRB review, a DPA, truthful
cards and stop rules. A cheaper upgrade path for Study 1 itself: run the same code on a design
partner's **private** GitHub organisation with written consent (a read-only GitHub App), which puts
the study directly on a buyer's production services.

## Provenance

Designed 2026-09-27 in a Claude Code cloud session from the tournament output (finalists X1 and C3
v2, field entries X1/C3, final ranking and conditions) plus new checks listed as VERIFIED in the
files. The tournament JSON lives in that session's scratchpad, not in this repo.
