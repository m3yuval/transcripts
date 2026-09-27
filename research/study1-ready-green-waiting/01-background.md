# 01 — Background

## 1. The thesis and the belief under test

Source: `../../thesis.md` (last updated 2026-09-25) and `../../ledger.md`.

Skylayer's claim: *organizations don't remediate fast enough because nobody can prove a change is
safe (fear of breaking production owns the blast radius), not because they don't know what to fix.*

Belief 2 in thesis.md: **"The blocker is impact uncertainty — not speed, not prioritization, not the
absence of tooling."** The ledger's claim C1 ("fear of breaking production") has eleven unprompted
interview supporters, but interviews cannot separate fear of breakage from attention, prioritization
or ownership, and thesis.md lists "Any number" as unproven. **Belief 2 has zero evidence so far.**
Study 1 is designed to be able to falsify it with public behavioural data.

## 2. Study 1 in one paragraph

Track security fixes that a bot (Dependabot or Renovate) already wrote as a pull request, that pass
the repo's own CI, but stay unmerged — in **company-owned, deployed-service** repos. The fix is
identical across repos. Measure (a) the share of fixes that are *proven safe* (own CI green plus a peer
"safe to merge" score ≥90% / High) and still unfixed after 30 days (co-primary P1; ≥35% falsifies
belief 2 here), and (b) whether a peer score appearing silently on an open PR raises the merge hazard
at moments when a human is merging (co-primary P2), against a placebo (the same score change when
the badge is not displayed), a severity horse race (H5), a hollow-green lab measure (H3), a census of
written bot-merge rules (H4) and a calibration of the scores against real breakage (H6). Headlines
are pre-written for both outcomes. Full hypotheses in `04-analysis-design.md` §2.

Origin: winner of a 131-agent research tournament (48 generators, 132 raw ideas, 26 candidates, 8
challengers). The final judge ranked X1 ("Ready, Green, Waiting: Silent Proof vs Noisy Nudge") first
and C3 v2 ("Proven Safe, Still Stuck") second, and required folding C3's MVP into X1. The
tournament output is in the design session's scratchpad (`tournament.json`), not in this repo; the
relevant content is reproduced below and in 04.

## 3. Prior art

Status: **VERIFIED** (primary text read), **VERIFIED-SNIPPET** (existence and key finding confirmed
only through web-search snippets; the publisher/arXiv pages were blocked), **UNVERIFIED** (from
memory; not confirmed), **BLOCKED** (page could not be reached). Step 0 of the implementation plan
re-reads every item from the full text.

### 3.1 Directly on the mechanism (bot fixes, scores, merging)

| work | what it says (relevance) | link | status |
|---|---|---|---|
| He, He, Zhang, Zhou. "Automating Dependency Updates in Practice: An Exploratory Study on GitHub Dependabot." IEEE TSE 2023 (arXiv 2206.07230) | Dependabot's "compatibility scores are too scarce to be effective in reducing update suspicion"; developers configure Dependabot to reduce notifications; 11.3% of projects deprecated it. Snippets also report a weak Spearman ρ = 0.37 between compatibility score and merge rate (attribution to this paper to be confirmed). **Predicts a small/null P2.** | https://doi.org/10.1109/TSE.2023.3278129 · https://arxiv.org/abs/2206.07230 | VERIFIED-SNIPPET |
| Rombaut, Cogo, Hassan. "Leveraging the Crowd for Dependency Management: An Empirical Study on the Dependabot Compatibility Score." arXiv 2403.09012 (2024; venue unconfirmed) | 579,206 Dependabot PRs and 618,045 score records; **a score cannot be calculated for 83% of updates**; existing scores are mostly >90%. Score = successful updates / candidate updates across client packages. **Closest prior art; limits flips and low scores.** | https://arxiv.org/abs/2403.09012 | VERIFIED-SNIPPET |
| Alfadel, Costa, Shihab, Mkhallalati. "On the Use of Dependabot Security Pull Requests." MSR 2021 | 2,904 JS projects; 65.42% of security PRs accepted, often merged within a day. | https://2021.msrconf.org/details/msr-2021-technical-papers/25/On-the-Use-of-Dependabot-Security-Pull-Requests | VERIFIED-SNIPPET |
| Rebatchi, Bissyandé, Moha. "Dependabot and security pull requests: large empirical study." EMSE 29:128 (2024) | 9.9M PR-related issues in 1.74M projects; security PRs highly accepted, fixes applied in <1 day; project/PR/developer features correlate with acceptance. | https://doi.org/10.1007/s10664-024-10523-y | VERIFIED-SNIPPET |
| Mohayeji Nasrabadi, Agaronian, Constantinou, Zannone, Serebrenik. "Securing dependencies: A comprehensive study of Dependabot's impact on vulnerability mitigation." EMSE 30:89 (2025) | engineered, active JS projects; tests/CI influence acceptance of security updates. | https://doi.org/10.1007/s10664-025-10638-w | VERIFIED-SNIPPET |
| Tanaka, Tsuchida, Shimari, Kula, Matsumoto. "An Exploratory Study of Dependabot Cooldown Adoption in Open-Source GitHub Projects." arXiv 2609.16605 (2026-09-15) | cooldown GA July 2025; 83 of 92 adoptions security-motivated; 64.3% use 7 days. (Context for age gates; cooldown does not apply to security updates.) | https://arxiv.org/abs/2609.16605 | VERIFIED-SNIPPET |
| Hejderup, Gousios. "Can we trust tests to automate dependency updates? A case study of Java projects." JSS 183 (2022) | tests cover 58% of direct and 21% of transitive dependency calls; detect 47% / 35% of injected faults. **Motivates "hollow green" (H3).** | https://www.sciencedirect.com/science/article/pii/S0164121221001941 · https://arxiv.org/abs/2109.11921 | VERIFIED-SNIPPET |
| Cogo, Oliva, Hassan. "An Empirical Study of Dependency Downgrades in the npm Ecosystem." TSE 47 (2019) | downgrades as a signal of unsuitable versions — basis of the escaped-breakage label (H6). | https://doi.org/10.1109/TSE.2019.2952130 | VERIFIED-SNIPPET |
| Reyes, Gamage, Skoglund, Baudry, Monperrus. "BUMP: A Benchmark of Reproducible Breaking Dependency Updates." SANER 2024 | 571 reproducible breaking updates (mostly from bot PRs; Java). Useful for lab validation. | https://arxiv.org/abs/2401.09906 · https://github.com/chains-project/bump | VERIFIED-SNIPPET |
| Rombaut et al. "There's no such thing as a free lunch: ... overhead introduced by the Greenkeeper dependency bot in npm." TOSEM 2023 | bot PR overhead / noise. | — | UNVERIFIED |
| Mirhosseini, Parnin. "Can automated pull requests encourage software developers to upgrade out-of-date dependencies?" ASE 2017 | bot PRs vs badges as nudges. | — | UNVERIFIED |
| Trockman et al. "Adding sparkle to social coding: an empirical study of repository badges in the npm ecosystem." ICSE 2018 | badges as signals. | — | UNVERIFIED |
| "Reducing Alert Fatigue via AI-Assisted Negotiation: A Case for Dependabot." arXiv 2502.06175 | related (alert fatigue); content not read. | https://arxiv.org/abs/2502.06175 | VERIFIED-SNIPPET (existence) |
| "Towards a Benchmark for Dependency Decision-Making." arXiv 2601.00205 | related; content not read. | https://arxiv.org/abs/2601.00205 | VERIFIED-SNIPPET (existence) |

**Novelty check.** No paper found (in snippets) that estimates the *causal* effect of a displayed
score changing on an open PR, uses an invisible-flip placebo, or measures the "proven safe, still
stuck" share. The tournament's skeptic reached the same conclusion from memory. **Must be confirmed
from full texts in Step 0** (tournament condition 5): if someone already did it, P2 becomes a
replication and the headline shifts to P1, D1, H4 and hollow-green.

### 3.2 On the company filter

| work | relevance | link | status |
|---|---|---|---|
| Spinellis, Kotti, Kravvaritis, Theodorou, Louridas. "A Dataset of Enterprise-Driven Open Source Software." MSR 2020 (arXiv 2002.03927) | identified 17,252 enterprise GitHub projects from enterprise email domains of committers (three heuristics); manual evaluation 89% accurate. **Basis for Tier B.** | https://arxiv.org/abs/2002.03927 · https://doi.org/10.1145/3379597.3387495 | VERIFIED-SNIPPET |
| "Rules of engagement: Why and how companies participate in OSS." ICSE 2023 | company participation patterns. | — | VERIFIED-SNIPPET (existence only) |
| "Recipe for Discovery: A Pipeline for Institutional Open Source Activity." arXiv 2506.18359 | pipeline to find institutional (likely academic) GitHub activity — possibly reusable for excluding universities. | https://arxiv.org/abs/2506.18359 | VERIFIED-SNIPPET (existence only) |
| GitHub docs: verifying a domain for an organization | verified badge requires profile website and email to match verified domains; free plans included. | github/docs source (see 02 §S2) | VERIFIED |
| Wikidata P2037 (GitHub username), P1278 (LEI), P1320 (OpenCorporates ID) | registry links for Tier A. | https://www.wikidata.org/wiki/Property:P2037 | VERIFIED-SNIPPET |

### 3.3 On nudges, notifications and fear of change (for interpretation)

| work | relevance | status |
|---|---|---|
| Maddila et al. "Nudge: Accelerating Overdue Pull Requests toward Completion." ACM TOSEM 32(2), 2022 (arXiv 2011.12468) | attention reminders on PRs cut completion time at Microsoft — **the attention rival stated outright**. Whether it was randomized: not confirmed from snippets. | VERIFIED-SNIPPET (paper); design details UNVERIFIED |
| Durumeric et al. IMC 2014 (Heartbleed notifications); Li et al. USENIX Security 2016 ("You've Got Vulnerability"); Stock et al. USENIX Sec 2016 / NDSS 2018; Cetin et al. 2019; Maass et al. USENIX Sec 2021 | randomized vulnerability-notification trials; message-content changes mostly small/null. | UNVERIFIED (memory) |
| Li et al. SOUPS 2019 ("Keepers of the Machines"); Tiefenau et al. SOUPS 2020; Dissanayake et al. CSCW 2022 | self-reported reasons for delayed patching, including fear of breakage and coordination costs. | UNVERIFIED (memory) |

### 3.4 Primary technical sources used by the design (all VERIFIED on 2026-09-27)
- GitHub docs source, `dependabot-security-updates.md` — compatibility-score definition; minimum
  patched version; grouped security updates.
- `dependabot/fetch-metadata` `src/dependabot/verified_commits.ts` — badge URL and SVG `<title>` parse.
- `dependabot/dependabot-core` branch namer — branch format.
- `renovatebot/renovate` `docs/usage/merge-confidence.md` and `lib/config/options/index.ts`
  (`vulnerabilityAlerts` defaults).
- GitHub docs source: Events API payloads, rate limits (REST, GraphQL, secondary), AUP §7, ToS §H,
  domain verification; GitHub OpenAPI description (`is_verified`); GraphQL public schema.
- GitHub docs source: Dependabot default 3-day cooldown for version updates, "does not apply to
  security updates".
- GH Archive repository (`bigquery/schema.js`, READMEs).
- cloud.google.com BigQuery pricing page.

## 4. What the tournament skeptics said (and how the design answers)

### X1 (score 5.03, verdict "wounded")
1. **Treatment varies at the fix level and fix fixed effects absorb it**; within a fix only different
   from-versions vary, which tracks repo diligence; if the backend keys on new-version only, the
   treatment disappears. → G2 (iv) keying test; jump-size and previous-version-popularity controls;
   drop Dependabot from P2 if keyed on to-version.
2. **Flips are rare and early; filters may leave too few events**; low scores rare so H2 weak. →
   G2 (i)(ii); company-only makes this worse (04 §5, §8); H2 reported as estimate.
3. **Nobody observes whether a maintainer saw the badge** → uninterpretable null likely. →
   human-activity (session FE) restriction, invisible-flip placebo, H5, and P1 which does not depend
   on exposure timing.
4. **Noisy-nudge placebo is tied to activity** (rebases happen when main moves). → dropped as a
   placebo; kept as covariate.
5. **72 h discontinuity sits on a crowded focal point** (pnpm/yarn age gates, hidden presets). → H8
   demoted to secondary with placebo cutoffs and negative-control ecosystems.
6. **Hollow-green fingerprint is not clean** (coverage also marks peripheral deps and weak test
   culture). → maturity and relevance controls; still a secondary hypothesis.
7. **Off-wedge; OSS maintainers ≠ enterprise change boards; low revert rate cuts against urgency.**
   → the founder's company-only + deployed-service restriction targets exactly this; interpretation
   of revert rate pre-registered both ways; scope stated honestly.

Skeptic's prior art (X1): arXiv, Scholar, OpenAlex, Crossref, GH Archive, docs.renovatebot.com,
developer.mend.io and dependabot-badges were all blocked; primary facts were verified from raw GitHub
sources; the within-PR event study on a silent score change "looks novel"; H4's novelty unconfirmed.

### C3 (score 4.97, "wounded") — relevant parts
- The RCT bundled reachability (relevance) with breakage proof; controls already contain badges;
  the placebo is not blind; the sign test is underpowered; OSS outcomes are bimodal (merged in hours
  or never); the DIVD venue is unethical; the RMM venue needs a competitor's cooperation; a
  behavioural field experiment strains "technical evidence only". → Only C3's **MVP** is folded in
  (P1 and the sign test); the RCT is a later phase (README).

### Final judge — conditions attached to the win (all adopted)
1. C3's "proven safe, still stuck at 30 days" share as co-primary, human-active no-automerge stratum,
   ≥35% falsifying → **P1**.
2. Recheck badge display in the week-2 gate (the 1-in-5 sample likely understates display) → **G2 (iii)**.
3. Collect via GH Archive/BigQuery plus GraphQL, never Search → **03 §2**.
4. Poll only security-subset badges, identified UA, ≤1 req/s, GitHub's written OK first; Mend off
   without written permission → **07, G0**.
5. Verify the prior art from an unrestricted network in week 1 → **05 Step 0.8**.
6. State scope honestly (application-dependency patching in org-owned deployable services); bridge to
   wedge B later → **04 intro, 06 §E3**.
7. Never name repos with unmerged security fixes; publish open access → **07 §7, §2.7**.

Judge's weaknesses of X1: off-wedge; prior expects a null (He et al.); uncertain badge exposure;
starts from an open PR so it cannot test the unknown-asset rival. Kill list items relevant here: the
72 h discontinuity as a headline; any unconsented intervention (comments/PRs/nudges) on real repos.

## 5. What a result will mean for Skylayer

- **Supported** (P1 < 15%, P2 ≥ 1.25 with placebo null): first public, pre-registered evidence that
  displayed proof moves real security fixes in company services; the hollow-green share sizes the
  product gap ("proof exists but is weak where tests are blind").
- **Falsified** (P1 ≥ 35%, P2 equivalence-null, H5 severity/nothing): in this domain the delay is
  attention/ownership, not fear → reposition toward "act and own" (thesis belief 3/4) rather than
  "prove".
- **Mixed**: "uncertainty is one contributor", with measured shares. Either way the founder updates
  thesis.md and ledger.md by hand.
