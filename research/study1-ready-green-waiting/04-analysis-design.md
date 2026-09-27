# 04 — Analysis design

Hypotheses, estimands, models, placebos, power (recomputed for the company-only sample), gates,
pass/fail rules, headline tables and figures, and a pre-registration draft ready for OSF (§10).
Population definitions are in `03-population-and-company-filter.md`; sources in `02-data-sources.md`.

Scope, stated honestly (tournament condition 6): **application-dependency security fixes in
company-owned, deployed-service GitHub repos.** Not OS patching, not network config, not private
enterprise repos (a later phase with a design partner can run the same code on a private org).

---

## 1. Belief under test

thesis.md, belief 2: *"The blocker is impact uncertainty — not speed, not prioritization, not the
absence of tooling."* ledger.md has **zero** evidence for or against it. Study 1 is designed so that
belief 2 can **lose**.

Prior (recorded before data): published work suggests Dependabot compatibility scores are usually
missing and weakly related to merging — He et al., TSE 2023: "compatibility scores are too scarce
to be effective in reducing update suspicion"; Rombaut et al., arXiv:2403.09012: 83% of updates have
no score and existing scores are mostly >90% (both VERIFIED-SNIPPET; see 01). **Our expected outcome
for H1 is small or null.** The design separates "null because proof doesn't matter" from "null
because nobody looked" (human-activity restriction, placebo, H5).

## 2. Hypotheses and estimands

### Co-primary (headline)

**P1 — "Proven safe, still stuck" share** (from C3 v2, adopted per the tournament's condition 1).
- Population: Tier A × deployed-service, human-active, no automerge at open, single-dependency
  security fix PRs, own CI green at head, and a **displayed** peer score of ≥90% (Dependabot) or
  Confidence High/Very High (Mend) observed by the logger within 7 days of PR open ("proven safe").
- Estimand: share still **not fixed** 30 days after PR open. "Fixed" = PR merged, OR a superseding
  bot PR for the same package merged, OR the default-branch lockfile shows a version ≥ the patched
  version (checked at day 30). Closed-unmerged without a fix = not fixed.
- Pre-registered reading (belief 2, this domain):
  - **≥ 35%** (point estimate ≥0.35 and 95% CI lower bound ≥ 0.25) → **FALSIFIES** belief 2 here:
    proof exists and does not clear the queue.
  - **< 15%** (point estimate <0.15 and CI upper bound < 0.25) → **consistent with** belief 2: when
    proof exists, fixes move.
  - otherwise → MIXED ("uncertainty is at most one contributor").
- Needs prospective badge logging (historical badge values are not observable).

**P2 — Silent proof (H1 from X1).** When the displayed peer score on an open PR changes from
unknown to numeric ≥90% (Dependabot) or Neutral→High (Mend), with no change to the PR's content or
CI and no notification, the merge hazard rises.
- Unit: PR × day (discrete time), restricted to days on which a human is active in the repo
  (merge-session days: a `User` merged ≥1 PR, or reviewed/commented on any PR, that day).
- Model: conditional logit (equivalently discrete-time hazard) of merge on that day, with **session
  (repo-day) fixed effects** (holds attention constant), **fix fixed effects** (package × to-version),
  PR-age baseline (spline), jump size (semver distance from→to), previous-version popularity;
  cluster-robust SEs by repo. Treatment: displayed-score state (unknown / numeric ≥90 / 70–89 / <70),
  time-varying, lagged to the last logger observation before the day starts.
- Estimand: hazard ratio HR(high vs unknown).
- SESOI: HR 1.25 (proof removes ~20% of the waiting hazard).
- SUPPORTS: HR ≥ 1.25 with 95% CI excluding 1; flat pre-trend at fake flip dates 1–3 days earlier;
  invisible-flip placebo (§4) CI includes 1 and differs from the displayed effect (p<0.05).
- FALSIFIES: TOST equivalence within [0.87, 1.15] at adequate power (§5), or HR < 1.
- CONFOUNDED: invisible-flip HR ≈ displayed HR (herding/peer adoption, not proof).
- INCONCLUSIVE: anything else, including an underpowered null. **An underpowered null is never
  reported as a falsification.**

Multiplicity: the two co-primaries are tested at α = 0.025 each (Bonferroni); P1 is an estimation
with pre-set thresholds and CIs are reported at 95%.

### Secondary (pre-registered)

| id | hypothesis | estimand / test | supports / falsifies |
|---|---|---|---|
| D1 | descriptive: N security fix PRs, green at head and unmerged ≥7 days in Tier A deployed services; median wait | counts, KM curves | no causal claim |
| H2 | sign / dose-response: among PRs a human looked at after the value was set, merge hazard ordered low(<70%) < unknown < high(≥90%) | ordered contrasts in the P2 model | supports: monotone and low<unknown significant; falsifies: flat numeric effect (salience) or low ≥ unknown |
| H3 | hollow-green fingerprint: P2 effect ≥1.5× larger where the repo's tests do not exercise the changed dependency code (lab, §6), controlling for overall coverage (maturity) and production import (relevance) | interaction ratio | supports: ≥1.5, CI excl. 1; falsifies: CI includes 1 or <1 |
| H4 | written policy census: among de-duplicated, edited bot-merge policies in the company sample, gates on breakage proxies (update-type, compatibility-score, matchConfidence, release age) outnumber gates on severity/relevance proxies (alert-state, cvss, ghsa-id, dependency-type) | ratio of gate counts | supports: ≥3×; falsifies: ≤1× or <200 edited policies (then "no signal") |
| H5 | horse race at the moment of attention: on merge-session days, choice among open green security bot PRs depends more on breakage signals (semver, displayed score, hollow-green) than on severity (CVSS, EPSS, KEV) | conditional logit with session FE; standardized coefficient difference | supports: breakage > severity (CI of difference excl. 0); falsifies: severity > breakage or breakage null |
| H6 | predictability: escaped breakage (revert, lockfile downgrade, new pin/ignore within 30/90 days of a green security merge) predicted by peer score and hollow-green better than semver alone | PR-AUC ≥ 2× base rate and Brier skill > 0 | falsifies: AUC CI includes 0.5 for both; the escaped-breakage rate is reported whatever it is |
| H7 | companies vs individuals (optional group): for the same fix, time-to-merge is longer in Tier A than Tier U among human-active green no-automerge PRs | Cox with fix strata; HR(Tier A vs U) | thesis predicts HR<1 (slower); reported either way; never pooled into headlines |
| H8 | 72h Merge Confidence discontinuity (npm, Mend) | diff-in-discontinuities vs PyPI/Maven; placebo cutoffs 24/48/96h | **secondary, demoted**: pnpm's 24h default and ~34k visible age-gate configs crowd the cutoff |

Retrospective analyses (D1, H5-retro, H6-retro) use the pre-trim window 2025-01-01..2025-10-06
(03 §2); no badge values exist historically, so H5-retro uses semver, dependency type, CVSS, EPSS.

### Belief-2 verdict rule (this domain only; pre-registered)
- **SUPPORTED** if P1 < 15% AND P2 SUPPORTS AND (H2 or H3 supports) AND H5 not falsified.
- **FALSIFIED** if P1 ≥ 35% AND P2 does not SUPPORT (equivalence-null, or inconclusive — P2 itself
  is still labelled "inconclusive" in that case; the falsification rests on P1) AND H5 shows severity
  or nothing drives choice.
- **Partly falsified**: P1 ≥ 35% alone is reported as "proof exists and does not clear the queue in
  N% of cases" — it is the single most decisive number the study can produce.
- Everything else **MIXED**. No subgroup is promoted to the headline unless pre-registered.

## 3. Key definitions for the models

- **Displayed score state** at time t: the last logged value of the badge **whose URL is present in
  the PR body at t** (body edits from `userContentEdits`; stripped bodies = not displayed).
- **Flip**: first logged change unknown→numeric (Dependabot) or Neutral→High/Very High (Mend). Flip
  time = midpoint between the two logger observations; sensitivity with the later observation.
- **Human present after flip**: ≥1 merge-session day in the repo after the flip while the PR is open.
- **Supersession**: Dependabot/Renovate close a PR when a newer one replaces it; the chain is linked
  by (repo, package) and the fix time is the merge of any PR in the chain.
- **Escaped breakage** (H6): within 30/90 days of the merge commit, any of: `git revert` of the merge
  commit; lockfile/manifest version of the package decreased (Cogo et al. TSE 2019-style downgrade);
  new ignore rule (dependabot.yml `ignore`, Renovate `packageRules` disable/pin, `overrides`/
  `resolutions` pin) for the package; a commit message matching `(?i)(revert|rollback|pin|fix (the )?build).*<pkg>`.
  Precision hand-audited on 300 cases; recall is a lower bound (fixes-forward are missed).

## 4. Placebos and robustness

1. **Invisible-flip placebo** (P2): same score change on PRs whose body does not display the badge
   (stripped/edited bodies; Renovate with badges disabled via `ignorePresets`). Should move nothing.
2. **Fake-flip pre-trends**: flips moved 1–3 days earlier.
3. **Stacked event study**: flipped PRs vs PR-age-matched not-yet-flipped PRs of other (from,to)
   pairs.
4. **Noisy nudge** (rebases/force-pushes) is a covariate only; the tournament judged a placebo claim
   on it invalid (rebases coincide with activity on main).
5. **Other-PR placebo**: a flip on PR X should not change the hazard of an unrelated open PR Y in the
   same repo on the same day beyond session effects.
6. **Tier robustness**: A (main) vs A1+A2 only vs A+B.
7. **Automerge leakage**: re-run excluding repos with any automerge evidence at any time.
8. **Security classification**: re-run with `incidental_fix` PRs added.
9. **Keying**: if the Dependabot score is keyed on to-version only (gate G2 check), the fix FE absorbs
   Dependabot flips — Dependabot is dropped from P2 and Mend alone is used (if permitted).

## 5. Power (recomputed for the company sample)

Schoenfeld approximation, events D = (z₁₋α/₂ + z₁₋β)² / (p(1−p)·(ln HR)²); computed in the design
session:

| HR | exposed share p | α=0.05, 80% | α=0.025, 80% |
|---|---|---|---|
| 1.25 | 0.5 | 631 | 764 |
| 1.25 | 0.3 | 751 | — |
| 1.25 | 0.1 | 1,751 | — |
| 1.5 | 0.5 | 191 | 231 |
| 2.0 | 0.5 | 65 | — |

Minimum detectable HR (α=0.05, 80%, p=0.5): 100 events → 1.75; 200 → 1.49; 300 → 1.38; 500 → 1.28;
1,000 → 1.19.

**Equivalence (TOST) correction.** The tournament said ~1,300 events for TOST within [0.87, 1.15].
Recomputed: with a true HR of 1 and p=0.5, 80% power needs **~1,766 events** (1,300 events give only
~61% power). A wider margin [0.80, 1.25] needs ~688 events.

**Sign test (H2):** HR 0.80 for low vs high with 10% of PRs low needs ~1,751 events — **not reachable
in the company sample**; H2 is reported as an estimate with CI.

**P1 precision:** 95% CI half-width at p=0.25: n=200 → ±0.10 (deff 3); n=400 → ±0.073; n=800 →
±0.052. P1 is decidable at n≈400 unless the truth is near 25%.

**Expected supply** (03 §9, central assumptions): Tier A deployed over 16 weeks → ~200–650
proven-safe PRs (P1: probably adequate) and **~40–210 flip events (P2: underpowered for HR 1.25;
MDE ≈ 1.5–2.0)**. Power will be re-estimated by simulation on the week-2 pilot (resampling repos,
injecting HR 1.25 and 1.5) before the causal arm is kept.

## 6. Provability lab ("hollow green", H3/H6)

For a random sample of merged green security PRs (pilot 200; full 500 within budget, JS and Python):
diff the registry tarballs of old vs new version to list changed functions; run the repo's unmodified
tests in a container (network off after install), once per version, with coverage (c8/nyc;
coverage.py) and diff-scoped mutation (Stryker; mutmut). Label **hollow-green** if tests execute none
of the changed functions (or kill <10% of diff-scoped mutants). Controls: overall line coverage;
whether production code imports the package (static import scan).

## 7. Go/no-go gates (outcome-blind)

| gate | when | continue only if | else |
|---|---|---|---|
| **G0 legal** | before any badge request at scale | GitHub written OK for badge polling (or explicit no-objection); Mend written OK for the Mend arm | no OK from GitHub → no prospective logging: study ships D1, H4, H5-retro, H6 only. No Mend OK → Mend arm off |
| **G1 supply** | end of Step 3 (week 1) | measured Tier A deployed security fix PRs ≥ 300/week (≈4,800 in 16 weeks; at the assumed 70% green × 45% eligible × 20% proven-safe this yields ≈300 P1 PRs) | apply the founder's pre-chosen fallback (§8) before registration |
| **G2 pilot** | end of week 2 of logging | (i) projected flip-with-human events ≥ 630 in the *primary causal sample* (§8); (ii) <70% of flips within 24 h of open; (iii) ≥50% of bodies display the badge; (iv) score keyed on (from,to) (≤50 test requests); (v) projected proven-safe PRs ≥ 300 | (i)–(iv) fail → P2/H2/H3 become exploratory (amendment filed); (v) fails → extend logging to 26 weeks or report P1 as estimation with its CI |
| **G3 classifier** | before registration | Tier A precision ≥0.90 (lower bound ≥0.80); service precision ≥0.80 | tighten once, re-validate, report both |

Gate metrics use only counts of PRs, flips, displays and classification labels — **never merge
outcomes**. Each gate decision is filed as an OSF amendment before the next phase.

## 8. The company-only power problem — pre-registered fallback (founder decision D1/D2)

The founder requires company-owned repos in the headline. P1 is probably feasible in Tier A; P2
probably is not. One of these must be chosen **before registration**:

- **Option F1 (recommended):** headline estimands (P1, D1, H4, H5, H6) on **Tier A**. P2 is
  estimated on Tier A and reported as an estimate with CI and its MDE; the **causal test of P2** is
  run on **A+B** (pre-registered as the P2 test sample) and on Tier A as a pre-registered
  consistency check (same sign, CI overlap). Tier C/U are never used for P2.
- **Option F2:** everything on Tier A; P2 declared exploratory up front. Cleanest, weakest.
- **Option F3:** extend prospective logging from 16 to 26+ weeks (more events; +~2.5 months; small
  extra cost) and keep Tier A as P2's test sample.

## 9. Headline tables and figures (pre-specified)

- **Table 1** Funnel: bot PRs → security → org-owned → Tier A/B → deployed → eligible → green →
  proven safe; weekly counts; classifier precision/recall.
- **Table 2** D1: green-at-head security fixes unmerged ≥7/30/90 days; median wait (Tier A; A+B).
- **Table 3** P1: proven-safe-still-stuck share at 30 days with 95% CI (Tier A; A1+A2; A+B;
  by ecosystem; by bot). The pre-registered reading printed next to it.
- **Table 4** P2/H2: hazard ratios by displayed-score state; placebo; pre-trends; MDE.
- **Table 5** H5: standardized coefficients breakage vs severity at merge sessions.
- **Table 6** H4: policy census — gate types in edited policies; codified security-fix exclusions.
- **Table 7** H6: escaped-breakage rate 30/90 d; AUC/Brier of score, hollow-green, semver.
- **Table 8** (secondary) H7: Tier A vs Tier U for the same fix.
- **Fig. 1** Kaplan–Meier time-to-fix for green security PRs: proven-safe vs unknown score (Tier A).
- **Fig. 2** Event-study plot around flips (displayed vs invisible).
- **Fig. 3** Reliability curve: peer score vs realized escaped breakage.
- **Fig. 4** Hollow-green share by ecosystem.
All cells aggregate ≥10 repos; no repo, package-instance, company or org name for any unmerged fix.

**Pre-written headlines** (numbers filled in only after analysis):
- *If supported:* "Ready, green and still waiting — until proof shows up: in company services, N
  bot-written security fixes passed their own tests and waited a median of D days. Once a peer
  'safe to merge' score appeared, only P% were still unfixed at 30 days; when the same score
  appeared on the identical fix but was hidden, nothing changed."
- *If falsified:* "Proven safe, still stuck: P% of security fixes in company services that passed
  their own tests AND showed ≥90% peer compatibility were still unmerged 30 days later. When
  maintainers sat down to merge, they chose by [severity / recency / nothing], not by breakage
  signals. In this domain the delay is attention and ownership, not fear of breakage."

## 10. Pre-registration draft (OSF, "Preregistration of secondary data analysis" template)

> Paste into the van den Akker et al. template (OSF x4gzt). Replace `<...>`; everything else is the
> proposed final text. File **before** any merge outcome of the company sample is computed.

**Title.** Ready, Green, Waiting: do displayed safety proofs get security fixes merged in company
services? A pre-registered observational study of bot-written dependency fixes on GitHub.

**Authors / affiliation.** <founder>, Skylayer; <academic co-author if any>. Conflict of interest:
Skylayer is building remediation-safety tooling; its thesis predicts P1 < 15% and P2 > 1. Both
outcomes will be published.

**Q1 Hypotheses.** P1, P2 (co-primary) and D1, H2–H8 (secondary) exactly as in §2 of design doc
`04-analysis-design.md` at commit `<hash>`, including thresholds and the belief-2 verdict rule.

**Q2 Data.** GH Archive via BigQuery (`githubarchive.day`, <windows>); GitHub REST/GraphQL for PR
hydration and repo attributes; badge images from dependabot-badges.githubapp.com<, developer.mend.io>
logged at t0, +6h, +1d, +2d, +3d, +7d, +14d, +30d and daily while open; GitHub Advisory Database and
OSV; CISA KEV; EPSS; Wikidata; GLEIF; git history of candidate repos; registry tarballs.

**Q3 Data already accessed.** Before registration we accessed: GH Archive counts of opened bot PRs and
owner/repo attributes (no merge/close outcomes of the company sample); classifier validation labels;
week-2 pilot counts of flips and badge display (no outcomes). Code and logs at <repo, commit>.

**Q4 Prior knowledge.** Prior literature (He et al. 2023; Rombaut et al. 2024; Alfadel et al. 2021;
Rebatchi et al. 2024; Mohayeji et al. 2025) suggests scores are rare, mostly high, weakly associated
with merging; most security PRs merge within a day. We therefore expect a small or null P2.

**Q5 Sampling and exclusions.** Company tiers, deployed-service rule, eligibility rules, security
classification — `03-population-and-company-filter.md` §3–§6 at commit `<hash>`; regex and list files
`<hashes>`. Validation results: Tier A precision <x> [CI], recall <y>; service precision <z>.

**Q6 Variables.** Outcome: merge/fix time; 30-day fix status; escaped breakage. Treatment: displayed
score state (time-varying). Covariates: listed in §2 and §3.

**Q7 Statistical models.** §2 (conditional logit with session and fix FE; Cox for H7; logistic/AUC for
H6), clustered SEs by repo, α = 0.025 per co-primary; TOST margins [0.87, 1.15]; SESOI HR 1.25.

**Q8 Inference criteria.** §2 SUPPORTS/FALSIFIES rules; §7 gates; §8 option <F1|F2|F3>.

**Q9 Missing data.** Logger gaps > 24 h: the PR-days are dropped from P2 and the gap is reported; a PR
whose badge was never observed is excluded from P1 (reported count). No imputation of outcomes.

**Q10 Robustness.** §4.

**Q11 Sample size and stopping.** Fixed calendar windows: retrospective 2025-01-01..2025-10-06;
prospective <start>..<start+16w> (+30 d follow-up for P1, +90 d for H6). No optional stopping.

**Q12 Ethics and data.** Public data only; no intervention on any repository; usernames hashed at
ingestion; email local parts never stored; no repo/company named for any unmerged fix; cells k ≥ 10;
open-access publication (GitHub AUP §7). IRB determination: <reference>.

**Q13 Timeline.** Registration <date>; analysis date <start+16w+30d> for P1/P2; <+90 d> for H6.
