# Research tournament results

Generators 48, raw ideas 132, candidates 26, challengers 8.

## Final ranking

### 1. X1 Ready, Green, Waiting: Silent Proof vs Noisy Nudge

Best overall. X1 compares the same fix at the same cost, with the same green CI and a human merging that day (session fixed effects), and lets only the displayed proof vary. The invisible-flip placebo (the same score change on PRs where the badge isn't shown) separates the effect of proof from herding. H5 races breakage signals against severity at the moment of attention, which tests the prioritization rival head-on. It is the only finalist that checks the proof mechanism against ground truth: escaped breakage (reverts, downgrades, new pins) is used to calibrate the peer scores, and the lab runs the repos' unmodified tests to measure 'hollow green'. Rigor is the strongest in the field: Schoenfeld power, TOST equivalence so a null can count as a falsification, a week-2 kill gate, and a pre-registered verdict rule. The legal basis is the cleanest. The GitHub AUP research clause was checked against the source text, the data is public, there is no scanning, and there is no licence or partner dependency. The first publication comes at week 4 (policy census) and a second at week 6 (the D1 count of green fixes waiting, revert rate, H5, hollow-green share), whether or not the causal arm survives. Weaknesses: (1) It is off-wedge: it covers application dependencies in org-owned repos, not enterprise OS patching. (2) The prior expects a null (He et al. 2023; neither the plan nor this judge could verify it). (3) Exposure to the badge is uncertain. (4) Because it starts from an open PR, the asset is known by construction, so it cannot test the unknown-asset rival.

### 2. C3 v2 Proven Safe, Still Stuck: Badge-Flip natural experiment, then factorial Proof/Relevance/Placebo RCT

C3 has the field's best single falsifying number: the share of provably safe security fixes (own CI green and peer score ≥90%) still unmerged at 30 days, with ≥35% pre-registered as falsifying belief 2. It also has the only randomized, on-wedge test that could settle belief 2 for enterprise OS patching: breakage proof vs relevance vs a matched placebo vs no card, plus a sign test and a reversibility arm. It ranks below X1 because its MVP is weaker on the same data. Its pipeline depends on GitHub Search sliced into 20-minute windows, and X1 hit secondary rate limits after 2 queries. It keeps the 72h Mend discontinuity as a primary test even though pnpm now defaults to a 24h release-age gate and about 34k visible age-gate configs crowd that cutoff. It has no human-present restriction, so a null is ambiguous. The RCT needs about 300 tenants from an RMM vendor that may see Skylayer as a competitor, 9-15 months and $80-200k. It is also a human-behaviour field experiment, which strains the 'technical evidence only' constraint and needs founder sign-off plus IRB review. Recommendation: fold its MVP (the H4 share and the sign test) into X1, and keep its RCT as the phase-3 decisive test.

### 3. X2 Canary Order v2: 'The fix was already on their test box'

X2 is the only finalist that sits on wedge B (OS patching) and puts numbers on the named rivals directly. It splits exposure into four buckets: forgotten hosts, fleets that had not started patching, automatic updates, and hosts that waited after their own fleet's first patch (self-proven delay). The last bucket is the one that answers Equifax/Log4j and Dissanayake. Its blast-radius sign test is well built because prioritization predicts the opposite sign. It has a real uncertainty shock: 74 jammy and 44 noble regression USNs, analysed as a difference-in-differences with an irrelevant-package placebo. It also tests belief 4 through the automation frontier. Its headline would be the most CISO-legible of the five. It ranks third on execution risk: (1) It needs an academic co-lead with Censys research access, whose terms are unverified and non-commercial, which limits Skylayer's reuse. (2) Weekly snapshots will turn many patch orders into ties. (3) Inferring fleets and blast radius from outside is the weakest link. (4) Mature enterprises rarely expose Ubuntu revision banners, so the gate of 300 or more fleets may fail. (5) There is no publication date until data access lands. (6) IPs may be personal data under GDPR.

### 4. X3 Twin Servers v2: the Proof Gap (staging vs production)

X3 has the cleanest counterfactual in the field: the org has already applied the fix to its staging twin. H2 tests dominance on the full population, with an attended-vs-abandoned split that tests the unknown-asset rival directly, and it measures the field rollback rate. But X2 dominates it. X3 uses the same data source and has the same licence dependency, with far fewer events: H3 has only about 10-16 revision clusters and can detect only a doubling of the gap. Name-token pairs of staging and production hosts that both expose revision-bearing SSH will be rare. H4 depends on the PHP revision appearing in X-Powered-By headers, which is unverified. And a positive H1 reads as 'change management working as designed'. It should become a pre-registered subgroup inside X2, not a separate study.

### 5. X5 The Proof Bill: manufacturers' 'safe to install' verdict ledger

X5 is strategically closest to the FDA-regulated design partner. Its 'approved configuration still vulnerable after the KEV due date' number is board-legible, and the cadence test is a clever way to falsify belief 2. It ranks last for three reasons. (1) The data may not exist: only one vendor page (Hologic) is confirmed, through a third-party probe, and many lists may show only current state. (2) It measures the manufacturer's mandatory validation ritual, not organizational delay, so it cannot say anything about belief 2 for organizations without a partner arm that is not signed. (3) Power is low: about 30-45 KB-months carry a mid-spell urgency shock. Anonymised vendor letters blunt the virality, and there is terms-of-service and vendor-relations risk. Even a positive result points at a proof step that Skylayer legally cannot replace in regulated V&V.

## Why the winner

X1 wins because it is the only finalist that can deliver a decisive, reproducible and legal answer within 6 weeks, from public data, with no partner or licence gate.

WHY IT WINS
- It holds constant the four things that make most patching claims unfalsifiable. The fix is already known (the PR is open), it costs nothing (a bot wrote it), it passes the owner's own CI, and the same fix appears across many repos (fix fixed effects). Only the safety evidence shown to the human varies.
- It builds in the placebos critics will ask for. The invisible-flip test gives the same score change with no badge displayed. The dose-response ordering (low < unknown < high) separates information from salience. The hollow-green interaction is something attention and prioritization theories do not predict.
- It races belief 2 against severity (the prioritization rival) at the exact moment a human is merging.
- It is the only finalist that tests the proof mechanism itself. It calibrates the peer scores the industry already ships against escaped breakage (reverts, lockfile downgrades, new pins). It also runs unmodified tests in its own lab to measure whether green CI actually exercised the changed dependency code.
- With TOST at about 1,300 events, a null is a real falsification. It is pre-registered and publishes whichever way the result lands.
- It ships two posts regardless of the causal arm: a week-4 census of hand-written bot-merge rules ('K of M let a bot fix only when it probably won't break'), and a week-6 D1/revert/H5/hollow-green post.

CONDITIONS ATTACHED TO THE WIN
(1) Adopt C3's 'proven safe, still stuck at 30 days' share as a co-primary headline estimand, restricted to the human-active, no-automerge stratum, with ≥35% pre-registered as falsifying. It is the crispest one-number stunt in the field and cannot be gamed by the badge-exposure problem.
(2) Recheck badge display in the week-2 gate. C3 counted 317,204 Dependabot PRs in 7 days whose bodies contain 'Dependabot compatibility score'. That suggests X1's 1-in-5 sample, drawn from a single org, understates display.
(3) Collect data through GH Archive/BigQuery plus GraphQL, never Search.
(4) Poll only security-subset badges, with an identified User-Agent, at ≤1 req/s, and get GitHub's written OK before scaling. Keep the Mend arm off without Mend's written permission.
(5) Verify the prior art (He et al. TSE 2023, Alfadel MSR 2021, Hejderup & Gousios 2022) from an unrestricted network in week 1. This judge could not: arXiv is blocked and the search budget is used up. If a published paper already measured the effect of the compatibility score on merges, H1 becomes a replication and the headline shifts to D1, H4 and hollow-green.
(6) State the scope honestly: application-dependency patching in org-owned deployable services. Bridge to wedge B with Dependabot docker base-image PRs and with X2.
(7) Never name repos with unmerged security fixes. Publish open access, as the GitHub AUP requires.

WHAT A RESULT MEANS
If H1 and H2 or H3 pass, Skylayer gets the first public causal evidence that displayed proof unblocks fixes, plus evidence that existing proof is weak where tests are hollow, which is the product gap.
If the result is 'proven safe, still stuck' with an equivalence null, belief 2 is falsified in this domain early and cheaply, and the founder repositions toward 'act and own' rather than 'prove'.

## Recommended portfolio

Sequence of 4 studies, with decision gates.

1) WEEKS 0-6: X1, merged with C3's MVP. This is the lead and needs no dependencies.
- Pre-register on OSF in week 1, including C3's H4 'proven-safe-still-stuck' share and the sign test (low score slows merges).
- Start the security-subset badge logger.
- Week-2 kill gate on the causal arm.
- Week-4 post: census of bot-merge policies.
- Week-6 post: D1 count of green security fixes waiting, proven-safe-still-stuck share, revert rate, the H5 horse race, and the hollow-green share.
- The prospective panel runs blind to month 4, with the H1-H3 readout at about month 7.
- Cost: about $3-6k, 1-2 people.
- Why first: it is the fastest route to a legal, reproducible number, and it answers belief 2 and the proof mechanism at once.

2) START WEEK 0, RUN WHEN DATA ACCESS LANDS: X2 Canary Order, with X3 folded in.
- Add X3's staging/production twin pairs as a pre-registered subgroup (the cleanest counterfactual).
- Add X3's attended-vs-abandoned split to the H0 exposure decomposition.
- Recruit an academic co-lead with Censys research access now, because the access lead time is the critical path. Run the go/no-go on the count of 300 or more fleets and the tie rate before any analysis.
- Why: it is the on-wedge (OS patching) test and the only one that measures the unknown-asset and not-started rivals against self-proven delay. X1 cannot do this by construction.
- Joint verdict:
  - X1 finds displayed proof moves merges AND X2 finds self-proven delay ≥25% with a positive regression-USN difference-in-differences: belief 2 is supported in two independent venues. That is the pitch.
  - X1 is proven-safe-still-stuck or null AND X2 finds forgotten plus not-started >60%: drop belief 2 and move toward asset ownership and coordination.
  - Mixed results: 'uncertainty is one contributor', with measured shares.

3) MONTHS 3-15, CONDITIONAL: C3's phase-B RCT on real OS patch approvals.
- Arms: breakage proof, relevance, matched placebo, no card; then the reversibility arm (H8, belief 4).
- Use the FDA design partner for a within-org change-ticket pilot, and an RMM/patch-content vendor for the powered venue (about 300 tenants).
- Go only if X1 did not return an equivalence null (otherwise the prior is too low; redesign it as proof plus action/rollback).
- Requires the founder's explicit sign-off that a consented behavioural field experiment fits 'technical evidence only', plus IRB review, a DPA, truthful-only cards, and stop rules.
- This is the one study that can settle belief 2 causally on wedge B.

4) OPTIONAL, WEEK 1 ONLY: X5 feasibility gate as a cheap side bet for the design partner's sector.
- Inventory medical/OT 'validated patches' pages: robots.txt and terms of service, date format, Wayback density.
- Continue the ledger only if 3 or more vendors have 3 or more years of dated per-KB history.
- Merge its partner arm (H8, exposure decomposition in a regulated fleet) into the RCT partner's data agreement rather than running it separately.

## Kill list

1) P6 'Breached With the Fix on the Shelf' (joining ransomware leak-site victims to scan history). It effectively re-identifies victims and builds on data criminals published. From outside it cannot tell 'feared breakage' from 'forgot the box'. The legal and reputational downside is far larger than any headline.

2) P1 'Fear Tax then Cliff' and C17 'Stand-Still Bill' (EKS/GKE/RDS extended-support fees). Paying to avoid a Kubernetes or database major-version upgrade is driven by upgrade effort (API removals, app changes). The thesis explicitly excludes that ('not because the fix is hard'). Per-account payment data is not public, and forced-upgrade outcomes can't be seen without customer data.

3) Generic 'N% of the internet still vulnerable to X' scan counts (round-1 b: edge-device patch decay; any standalone regreSSHion or Citrix count). They look like the MCP post but prove exposure, not cause. Shadowserver, Censys and Shodan already publish them weekly, and they can only feed the unknown-asset story. A count is worth publishing only when it carries a causal contrast, as X2 does.

4) Round-1 d, containers and Helm charts with fixable CVEs. This is a saturated vendor-marketing genre (image CVE-count reports), and most of those CVEs are unreachable. It is the noise this project is meant to cut, not a cut through it.

5) P3 'Safe But Stuck' / Last Blocker (DMARC p=none, CSP-Report-Only, MTA-STS testing). Whether enforcement is safe cannot be computed passively: aggregate reports go only to the domain owner. These are config toggles, not patches (closer to wedge A, which got zero interview support), and they have no exploit clock.

6) X4 'Same Bits, New Badge' and X7 'Firewall Ratchet'. Both sit on wedge A (no support in 40 calls) and need firewall version fingerprinting. X7 is already dead.

7) C12 RPKI. Blast radius is exactly computable, but the domain is routing, off-wedge, and RPKI delay is known to be driven by tooling and ownership.

8) C14 'ransomware shops for scary patches'. It is sensational and cannot be shown causally from public data: attackers choose by how common an edge device is, not by how scary the patch is. It would invite ridicule from the exact audience Skylayer needs.

9) P5 'Patch Weather / Call the Blast' as a standalone public forecast. It tests Skylayer's prediction skill before a product exists, not belief 2. Regressions are too rare for monthly scoring power (74 regression-titled jammy USNs over about 4 years). A public miss is a self-inflicted wound. Fold the calibration idea into X1's H6 instead.

10) The C3/X1 72h Merge Confidence discontinuity as a headline test. pnpm's 24h default and about 34k visible age-gate configs crowd the cutoff. Keep it secondary with placebo cutoffs, or drop it.

11) C7 'Friendly Fire' outage census and C13 '24-Hour' certificate-replacement test. Postmortems are a selected sample and show that breakage happens, not that fear causes delay. Certificate replacement is effort and ownership, not breakage uncertainty.

12) Data that is inaccessible or politically radioactive: P7 Deviation Files (FedRAMP and BOD exception records; FOIA is slow and redacted), FOIA change logs, litigation discovery, the insurance price of fear, pacemaker update uptake (patient-adjacent data), election equipment. None can produce a public, reproducible number on a startup timeline. Some carry ethical or political risk that swamps the message.

13) Any unconsented intervention on real maintainers or organisations: 'noisy nudge' comments or PRs on OSS repos, or CSIRT/DIVD notification arms that vary or withhold urgency. It is unethical, it breaks the zero-intervention legal checklist, and C3 rightly dropped the DIVD venue. Randomization is acceptable only with consenting partners, as in C3's phase B.

## Finalist execution plans

### Ready, Green, Waiting: Silent Proof vs Noisy Nudge (X1, execution plan with skeptic fixes)

**One line:** Track bot-written security fixes in public, actively maintained services that already pass their own CI but stay unmerged. Measure what gets them merged when a maintainer actually sits down to merge: a peer "safe to merge" score that appears silently on the identical fix, a notification carrying no new information, or severity. Score the incumbents' proof against real reverts, and read the written rules for when bots may act.

**Hypotheses:**
- H0 (prior, recorded before any data): published prior work (He et al., TSE 2023, cited from memory and unverified) suggests compatibility scores are often missing and ignored. Our expected outcome for H1 is therefore a small or null effect. The design is powered to tell 'null because proof doesn't matter' apart from 'null because nobody looked' (see H1 exposure restriction and H5).
- D1 (descriptive stunt): in actively maintained, org-owned deployable repos (Dockerfile or deploy workflow; a human merged some other PR in the window; no automerge configured at PR open), a substantial number of single-dependency, patch/minor, bot-written security PRs have green CI at the head SHA and stay unmerged for 7 days or more. Reported as N and median waiting days. No causal claim.
- H1 (silent proof, primary causal): when a PR's displayed peer score changes from unknown to numeric >= 90% (Dependabot) or from Neutral to High (Mend), and a human is shown to be present afterwards, the merge hazard rises. The PR's own content and CI are unchanged and no notification is sent. Unit: (PR, merge-session) panel. Controls: session fixed effects (attention held fixed), fix fixed effects, PR-age baseline, jump size and previous-version popularity. Placebo: the identical flip on PRs whose body no longer shows the badge (stripped or edited bodies, Renovate badges disabled) should move nothing. This separates the effect of displaying proof from herding and peer adoption.
- H2 (dose-response, within an identical badge): among PRs a human looked at, merge probability is monotone in the displayed score, with the pre-registered ordering low (<70%) < unknown < high (>=90%). A flat 'any number' effect means salience, not information. Low >= unknown falsifies the uncertainty reading.
- H3 (provability fingerprint): the H1/H2 effect is at least 1.5x larger where the repo's own tests cannot see the changed dependency code ('hollow green': low coverage and mutation detection of the functions changed between versions, measured in our lab). Controls: overall repo test coverage (maturity) and whether the dependency is imported by production code (relevance). These controls address the skeptic's point that prioritization and maturity also predict an interaction.
- H4 (revealed policy census): among deduplicated, edited (not copied from a template) bot-merge policies, conditions that let the bot act are dominated by breakage-risk proxies (update-type, compatibility-score, matchConfidence, release age) rather than relevance or severity proxies (alert-state, cvss, ghsa-id, dependency-type). Codified exclusions of security fixes (ignore rules, minimumReleaseAge inside vulnerabilityAlerts, apt/dnf holds, unattended-upgrades blacklists) are counted separately.
- H5 (horse race at the moment of attention, highest power): on merge-session days (a human merged at least one bot PR in the repo that day), the choice among the open, green, security bot PRs depends more on breakage-risk signals (update-type, displayed score, hollow-green) than on severity (CVSS, and EPSS/KEV if available). Conditional logit with session fixed effects. If severity dominates and breakage signals are null, the prioritization story beats belief 2.
- H6 (is blast radius predictable?): escaped breakage (a revert, a lockfile downgrade of that package, or a new ignore or pin within 30/90 days of a green-CI security merge) is predicted by the peer score and by our hollow-green measure better than by semver alone (PR-AUC at least 2x the base rate, positive Brier skill). If neither predicts it, the incumbents' proof is weak, and it is unclear whether prediction is possible at all.

**Pass/fail:** Filed on OSF before the prospective analysis starts. The descriptive and retrospective parts (D1, H4, H5-retro, H6-retro) are filed before the historical data is queried.

SESOI: HR 1.25, i.e. proof removes about 20% of the waiting hazard.

POWER (Schoenfeld):
- Detecting HR 1.25 with 50/50 exposure, 80% power and two-sided alpha 0.05 needs about 630 merge events in the exposure-contrast sample. With a 30/70 split it needs about 750.
- Concluding 'no effect' requires TOST equivalence within [0.87, 1.15], which needs about 1,300 merge events. With fewer, a null is reported as INCONCLUSIVE, never as a falsification.

KILL-OR-GO GATE (end of week 2, pilot of about 2,000 new security PRs). The causal arm (H1-H3) continues only if all of these hold:
(i) the extrapolated count of usable flip-while-open events with a human present after the flip is at least 630 over 16 weeks;
(ii) fewer than 70% of flips happen within 24h of PR open;
(iii) at least 50% of PR bodies still show the badge (bodies are sometimes stripped: 4 of the 5 Dependabot PRs we sampled, all from one large org, had no badge);
(iv) the Dependabot score is keyed on the (from, to) version pair, tested by varying previous-version on at most 50 requests. If it is keyed on to-version only, the within-fix Dependabot design is dropped and Mend alone is used;
(v) Mend's terms permit polling, or Mend grants access. Otherwise the Mend arm is off.
If the gate fails, H1-H3 become exploratory and the study ships D1, H4, H5 and H6 only.

SUPPORT / FALSIFY:
- H1 SUPPORTS: session-FE hazard ratio >= 1.25, 95% CI excluding 1; flat pre-trend at fake flip dates 1-3 days early; invisible-flip placebo (same flip, badge not displayed) HR CI includes 1 and differs from displayed HR (p<0.05). FALSIFIES: equivalence within [0.87, 1.15] at adequate power, or HR < 1. CONFOUNDED (neither): invisible-flip HR is about the same as displayed HR (herding or peer adoption, not proof).
- H2 SUPPORTS: monotone slope > 0 AND low < unknown < high, with low vs unknown significant. FALSIFIES: a flat effect across numeric values (salience), or low >= unknown.
- H3 SUPPORTS: hollow-green x flip interaction ratio >= 1.5 with CI excluding 1, after the maturity and relevance controls. FALSIFIES: CI includes 1 or the ratio is < 1.
- H4 SUPPORTS: among edited, deduplicated policies, breakage-proxy gates >= 3x severity/relevance gates. FALSIFIES: ratio <= 1, or fewer than 200 edited policies survive deduplication (then we report that no revealed-policy signal exists).
- H5 SUPPORTS: standardized breakage coefficient > severity coefficient (difference CI excludes 0). FALSIFIES: severity coefficient > breakage coefficient, or breakage signals null.
- H6 SUPPORTS predictability: PR-AUC >= 2x base rate AND Brier skill > 0 for the peer score or hollow-green. FALSIFIES: AUC CI includes 0.5 for both.
- The escaped-breakage rate itself is reported whatever it turns out to be. Interpretation is fixed in advance: >= 2% and concentrated in hollow-green means fear is partly rational and predictable; < 0.5% and unpredictable means fear is not grounded in escaped breakage in this domain.

BELIEF-2 VERDICT (this domain only):
- SUPPORTED if H1 passes, H2 or H3 passes, and H5 is not falsified.
- FALSIFIED if H1 is equivalence-null at power, H2 is flat, and H5 shows severity or nothing drives choice.
- Anything else is MIXED and reported as such.
No subgroup is promoted to the headline unless it was pre-registered. The main stratum is org-owned deployable services.

**Data pipeline:** 1) ADVISORY TABLE
- Clone github/advisory-database (reachable) and pull the OSV bulk export from GCS (osv-vulnerabilities/<eco>/all.zip; npm's is 216 MB, updated 2026-09-26).
- Build rows (ecosystem, package, vulnerable ranges, first patched version, GHSA, CVSS, published_at). Add EPSS/KEV if they can be reached.

2) PR DISCOVERY
- Source: the GH Archive public BigQuery dataset (PullRequestEvent opened/closed/merged for actors dependabot[bot] and renovate[bot]).
- The Events API no longer emits 'synchronize' on github.com (verified in the docs), so rebases, force-pushes, reviews, comments and body edits come from GraphQL timelines (HeadRefForcePushedEvent, userContentEdits) on one research token within its rate limits.
- GitHub search does not scale for this: our pilot hit a secondary rate limit after 2 queries.

3) SECURITY CLASSIFICATION
- Renovate: '[SECURITY]' title plus GHSA/CVE in the body (verified on a sample). Grouped multi-dependency PRs are dropped.
- Dependabot: join (package, from, to) to the advisory table. Per GitHub's docs, a security PR targets the minimum patched version, so the rule is: from-version in a vulnerable range AND to-version = first patched version.
- Validate against repos that label security PRs. Dependabot grouped security updates are dropped.

4) BADGE LOGGER (on an egress host that can reach the endpoints; our sandbox proxy blocks them)
- Parse the badge URL from the PR body: dependabot-badges.githubapp.com/badges/compatibility_score?dependency-name&package-manager&previous-version&new-version, and developer.mend.io/api/mc/badges/{age,confidence,...}/{datasource}/{pkg}/{from}/{to}.
- Fetch at t0, +6h, +1d, +2d, +3d, +7d, +14d and +30d with an identified User-Agent, <= 1 req/s and caching.
- Parse the title 'compatibility: N%' or 'unknown', as fetch-metadata does.
- Measure camo caching so that the value actually shown is known.
- Record whether the badge is displayed at all, via body edits and whether it is present in the body.

5) PR STATE
- Head-SHA check runs and statuses give green-at-head.
- Also record: merged/closed times, supersession, and the human merge-session days in the repo, which define choice sets for H5 and the exposure windows for H1.
- The repo config at t0 is parsed from history: dependabot.yml (ignore rules), renovate.json/json5 and resolved org presets, workflows using fetch-metadata or auto-merge, pnpm-workspace.yaml minimumReleaseAge (pnpm >= 11 defaults to 1440 minutes), .yarnrc.yml npmMinimalAgeGate and bunfig.toml.
- Repo covariates: owner type, Dockerfile or deploy workflow, ecosystem, activity.

6) ESCAPED-BREAKAGE GROUND TRUTH
- Shallow git clones of merged repos; scan 90 days after the merge for: a revert of the merge commit, a lockfile downgrade of the package (Cogo-style), a new ignore rule or override/resolution pinning the package, or a follow-up 'fix build' commit touching the package.
- Precision is hand-audited on 300 cases.

7) PROVABILITY LAB
- Registry tarballs (npm and PyPI reachable) are diffed to find the functions changed between old and new versions.
- The repo's unmodified tests run in a container with networking off after install, once on each version. Measure coverage of the changed functions, and mutation detection on them (Stryker/mutmut restricted to the diff). Label each PR hollow-green or visible.

8) CENSUS
- Code search and BigQuery file contents are used to collect the files. Deduplicate forks and templates by content hash, then diff against the GitHub docs and fetch-metadata README examples to keep edited policies only.
- Classify each gate as a breakage proxy or a relevance proxy. The OS-level IaC (unattended-upgrades blacklist, versionlock, apt-mark hold, GKE/EKS/AKS maintenance exclusions) is classified the same way.

9) PRIVACY AND STORAGE
- Usernames are hashed then dropped at ingestion. Repo IDs are salted-hashed in any released data. Published cells need k >= 10 repos.
- Parquet plus DuckDB. Code is released under an OSI license.

**6-week MVP:** Team: 1-2 people. Budget: about $3-6k (BigQuery scans, one small VM for the logger, lab compute for 200 PRs; cost figures are estimates).

WEEK 1: pre-register and switch on
(1) OSF pre-registration: H0-H6, SESOI, power, the gate, the verdict rule and the expected-null prior.
(2) Legal pack. GitHub AUP research clause (verified): commit to open-access output. Write to GitHub and Mend asking about polling and for historical score or view logs. Request an IRB exemption determination.
(3) Stand up the badge logger on a VM whose egress reaches both badge endpoints, fed by hourly discovery of new Dependabot and Renovate security PRs.
(4) Build the advisory table from github/advisory-database plus OSV GCS.
(5) Verify prior-art citations from a network that can reach the literature.

WEEKS 1-2: kill-or-go pilot (about 2,000 new security PRs)
- Measure: unknown share at open; flip-while-open share (green, active, no automerge); advisory-to-flip time; share of flips in the first 24h; badge-display share (body stripping); pair vs to-version keying (at most 50 extra requests); camo cache TTL; whether GH Archive PR bodies are present.
- End of week 2: GO or NO-GO on the causal arm, published as an OSF amendment.

WEEKS 2-4: census (H4), reproducible
- Collect fetch-metadata workflows, dependabot.yml, renovate.json/json5 plus resolved presets, pnpm/yarn/bun age gates, and OS-level IaC holds and exclusions.
- Deduplicate forks and templates, diff against the docs examples, classify gates.
- Release POST 1 at week 4: 'K of M hand-written rules let a bot fix things only when it probably won't break; J look at how dangerous the bug is', plus counts of codified 'never auto-fix this' holds.

WEEKS 2-5: retrospective 'Ready, Green, Waiting' (D1, H5-retro, H6-retro)
- Security PRs opened 2025-10-01..2026-06-30, followed to 2026-09-26, so at least 90 days of follow-up.
- Stratum: org-owned deployable services, active abstainers, no automerge at t0, single dependency, patch/minor.
- Compute: N green-at-head and unmerged for 7+ days; median waiting days; the share of waiting that happens while humans merge other bot PRs.
- H5 conditional logit on merge-session choice sets, using semver, dependency type, CVSS and PR age. Historical badge values cannot be observed.
- Escaped-breakage rate at 30/90 days, precision-audited on 300 cases.

WEEKS 4-6: provability lab pilot (200 merged PRs, JS and Python)
- Hollow-green rate: the share of green security bumps whose tests never execute the changed dependency code.
- First look at whether hollow-green predicts escaped breakage (H6-retro).

WEEK 6: POST 2
- Contents: D1, the revert rate, the H5 horse race and the hollow-green share.
- The prospective panel keeps running blind: no H1-H3 outcome peeking before the pre-registered analysis date.

MVP deliverables: two reproducible posts; open code; an aggregated dataset with hashed IDs; a decision on whether to invest in the full causal arm.

**Full version:** Months 1-7 (1-2 people, about $15-30k; no partners required):

1) PROSPECTIVE PANEL, weeks 1-16, then a 90-day revert follow-up (ends about month 7). Dependabot and Renovate security PRs with badge trajectories, timelines, CI state, config at t0 and merge-session days.

2) PRIMARY CAUSAL ANALYSIS (H1): a discrete-time hazard over (PR, merge-session) cells.
- Fixed effects and controls: session FE (holds attention: a human was actively merging bot PRs that day), fix FE, a PR-age baseline, jump size, previous-version popularity, repo FE in robustness checks.
- Placebos and robustness:
  - invisible-flip placebo: the same score flips on PRs whose badge is not displayed (stripped or edited bodies, Renovate badges disabled via ignorePresets);
  - fake-flip pre-trends;
  - a secondary stacked event study with PR-age-matched not-yet-flipped controls from other pairs (the skeptic's fix b);
  - rebase and force-push 'noisy nudge' is kept only as a covariate inside sessions, with pushes to main controlled for. The pre-registered placebo claim is dropped unless rebases not triggered by a push to main can be isolated (the skeptic's fix d).

3) DOSE-RESPONSE (H2): only among PRs with a human look after the badge value was set (the first-look design, skeptic's fix c).

4) 72H MERGE-CONFIDENCE DISCONTINUITY: demoted to secondary.
- Placebo cutoffs at 24h (pnpm default), 48h and 96h.
- Negative controls: PyPI and Maven, which have no 3-day rule.
- Repos with visible age gates are excluded (32k pnpm and 2.2k yarn configs seen), and resolved org presets are parsed.
- Only the Confidence badge is used, never Age.

5) LAB AT SCALE (H3): about 2,000 PRs, mutation-scoped to the changed functions, with maturity and relevance controls.

6) PREDICTABILITY (H6): calibration of the peer score, Merge Confidence, semver and hollow-green against 30/90-day escaped breakage (PR-AUC, Brier, reliability curves).

7) WEDGE-B BRIDGE
- Dependabot docker base-image bump PRs, if a score exists for them (pilot check).
- OS-level IaC census: unattended-upgrades blacklists, versionlock, apt-mark hold, k8s maintenance exclusions, auto_upgrade none.

8) OUTPUT: an open-access paper (satisfies the GitHub AUP; target a security or MSR venue plus an arXiv preprint), a replication package, and a public 'escaped-breakage vs. peer-score' calibration dashboard in aggregate.

OPTIONAL ACCELERATORS (need agreements):
- Historical score logs or badge-render/PR-view logs from GitHub or Mend. These turn H1 retrospective and rescue exposure measurement.
- Phase 2 with an RMM or patch-management partner, 6-12 months after the passive result exists: the same design on OS patch rings with ring-pass data shown silently vs not. This is the on-wedge generalization for enterprise buyers and the FDA-regulated design partner.

**Headline if true:** Ready, green, and still waiting: N bot-written security fixes passed their own tests and still sat unmerged a median of D days in actively maintained services. The fix never changed. When a peer 'safe to merge' score quietly appeared, merges rose X%; a low score cut them to W%; the same score change hidden from view moved nothing. Where the tests couldn't see the changed code, the effect doubled. And written rules let bots act on 'will it break?' K times more often than on 'is it dangerous?'

**Headline if false:** Proof isn't the bottleneck. We tracked N security fixes that were green and bot-written. A 'safe to merge' score appearing on the identical fix changed nothing (hazard ratio within about ±15% of no change), and a low score didn't slow merges. When maintainers sat down to merge, they picked by [severity / recency / nothing], not by breakage signals. Only R% of green-CI security merges were ever reverted. In this domain, the delay is attention and coordination, not fear of breakage.

**Legal checklist:** 1) GITHUB AUP RESEARCH CLAUSE (verified)
- Use only public, non-personal information.
- Every publication must be open access (arXiv plus an OA venue). This is a hard requirement.
- Usernames are personal data: hash them at ingestion, then drop them.

2) GITHUB API TERMS
- One identified research token, published rate limits respected, no token rotation to evade limits.
- GraphQL and REST for timelines. Search is not used for bulk collection (we hit secondary limits in the pilot).

3) BADGE IMAGES
- Fetch only badge URLs that appear in public PR bodies, as a normal image load.
- Identified User-Agent with a contact address, <= 1 req/s, fixed schedule, caching, stop on 429/403.
- Ask GitHub to confirm. The pair-keying test is capped at 50 extra requests.

4) MEND BADGE API
- Confirm Mend's terms, or obtain written permission, before polling at scale. Otherwise switch the Mend arm off or use a data agreement.

5) GH ARCHIVE AND BIGQUERY
- CC-BY-4.0 attribution for GH Archive; follow GCP terms.

6) ZERO INTERVENTION
- No comments, PRs, issues, reactions, stars, notifications or maintainer contact. We never delay or influence any fix.

7) CLONING AND LAB
- Public repos, license-respecting, shallow clones.
- Tests run unmodified in isolated containers, network off after dependency install, no credentials.
- No exploits and no vulnerability testing of any third-party system.

8) SECRETS AND SENSITIVE CONFIGS
- If an IaC or config file exposes a secret, do not store or report it; discard it and count it in aggregate only.

9) DISCLOSURE HYGIENE
- Repos with unmerged security fixes are vulnerable targets. Never name repos or orgs, never publish lists.
- Released data uses salted-hashed IDs, cells need k >= 10, and release is delayed 90 days.

10) ETHICS
- IRB exemption determination for public behavioral traces, plus a data-management plan and a retention limit.

11) PRE-REGISTRATION
- OSF, before the analysis date. The expected-null prior and the falsification rules are filed.

12) REGISTRIES
- npm and PyPI public endpoints used within normal-use rate limits.

**Biggest risks:** 1) UNINTERPRETABLE NULL
Maintainers may simply not look at badges (He et al. prior, unverified). Mitigations:
- the session-FE and first-look restriction;
- H5 (a horse race at a moment when a human is present);
- the invisible-flip placebo.
A null is declared only under TOST at about 1,300 events; otherwise it is reported as inconclusive.

2) VOLUME
Filters (green, active, single-dependency, patch/minor, no automerge, flip-while-open, badge displayed) may leave fewer than 630 events. The week-2 gate kills or keeps the causal arm. D1, H4, H5 and H6 ship regardless.

3) PAIR-LEVEL TREATMENT
Within a fix, variation comes from different from-versions, which correlate with how diligent a repo is. Mitigations: session FE, jump-size and previous-version-popularity controls, PR-age matching. If the score is keyed on to-version only, the Dependabot within-fix design is dropped.

4) HERDING
Scores arrive as peers adopt the fix. The invisible-flip placebo tests this directly; if displayed and hidden flips move merges alike, we report 'confounded'.

5) CROWDED 72H FOCAL POINT
pnpm's 24h default, 32k pnpm and 2.2k yarn age-gate configs, and hidden org presets and Mend workflows all sit near the cutoff. The 72h test is demoted to secondary, with placebo cutoffs and negative-control ecosystems.

6) INFRASTRUCTURE BLOCKERS
Our sandbox proxy blocks the badge endpoints, GH Archive, OSV/deps.dev APIs and the literature. The production pipeline needs an unrestricted VM and GCP billing, and the prior-art citations remain unverified until checked.

7) OFF-WEDGE
OSS maintainers are not enterprise change boards. Mitigations: restrict the main stratum to org-owned deployable services, add docker base-image bumps and the OS IaC census, and generalize fully only via the RMM phase.

8) REVERT RATE BACKFIRE
A low escaped-breakage rate reads as 'fear is irrational'. The interpretation is pre-registered both ways; revert detection is a lower bound because silent fixes-forward are missed.

9) CENSUS INFLATION
The docs example gates on semver-patch, so copy-paste inflates the ratio. Only edited policies are counted, and the H4 floor is 200.

10) PROPRIETARY SCORE AND ALGORITHM DRIFT
Mend's algorithm is private and can change mid-study. Only documented rules are used for identification, and algorithm changes are logged.

11) GENUINE FALSIFICATION
This is a feature, not a risk. If belief 2 fails here, the founder learns to reposition toward prioritization and coordination, or toward acting where proof exists.

**Why it cuts the noise:** It works because it holds constant the things that make most claims unfalsifiable:
- the fix is already known (the PR is open);
- it is free (a bot wrote it);
- it passes the owner's own CI;
- the same fix appears everywhere (fix fixed effects).
The only thing that varies is the safety evidence shown. Vendor claims about 'risk-based prioritization' and 'autonomous remediation' rest on surveys and anecdotes. This produces reproducible numbers from public traces: N green security fixes waiting D days; the share of escaped breakage; the ratio of written bot policies that gate on 'will it break' vs 'is it dangerous'. It also puts belief 2 in a head-to-head test against attention and severity at the exact moment a human is merging.

Placebos that critics usually ask for are built in:
- the invisible-flip test (same score change, not displayed);
- the ordering test (low < unknown < high);
- the provability fingerprint, which attention theories do not predict.

It needs no exploits, scanning or subjects, and every number comes out with its falsification rule filed in advance. Whichever way it lands, it is one of the few public results in this space that can say 'we were wrong' and mean it.

**Sources:**
- GitHub docs: Dependabot security updates, compatibility score definition ('percentage of CI runs that passed when updating between specific versions'); PRs target 'minimum version that includes the patch'; grouped security updates exist https://raw.githubusercontent.com/github/docs/main/content/code-security/concepts/supply-chain-security/dependabot-security-updates.md — verified (primary source, fetched from github/docs raw on 2026-09-26)
- dependabot/fetch-metadata source (verified_commits.ts): fetches the SVG badge by (dependency, package-manager, previous-version, new-version) and regex-parses the 'compatibility: N%' title https://raw.githubusercontent.com/dependabot/fetch-metadata/main/src/dependabot/verified_commits.ts — verified (raw source)
- Dependabot badge endpoint dependabot-badges.githubapp.com https://dependabot-badges.githubapp.com/badges/compatibility_score — blocked by our egress proxy (403 CONNECT). Its URL format was verified inside a live Dependabot PR body (2026-09-21). Response format, the 'unknown' rate and the sample threshold must be checked in the week-1 pilot from an unrestricted host.
- Dependabot PR bodies carry the badge https://github.com/search?q=author%3Aapp%2Fdependabot&type=pullrequests — verified, with an important caveat. In a sample of 5 Dependabot PRs opened 2026-09-20..25, only 1 carried the badge URL. The other 4 came from one large org whose bodies were stripped to about 250 characters, so badge display is not universal. That makes exposure measurable and gives the invisible-flip placebo.
- Renovate Merge Confidence docs: algorithm private; Low/Neutral/High/Very High; npm packages <3 days old cannot be High; Adoption/Passing are weighted toward orgs and private repos (not raw); Merge Confidence Workflows for paying and OSS-cloud users https://raw.githubusercontent.com/renovatebot/renovate/main/docs/usage/merge-confidence.md — verified (primary source, renovatebot/renovate docs via raw GitHub)
- Mend Merge Confidence badge API (developer.mend.io/api/mc/badges/{age,confidence}/...) https://developer.mend.io/api/mc/badges/ — blocked by our proxy. URL format verified in 3 live Renovate [SECURITY] PR bodies (age and confidence badges present). Terms for polling at scale are unconfirmed: needs agreement or permission.
- Renovate security PR volume https://github.com/search?q=author%3Aapp%2Frenovate+%22%5BSECURITY%5D%22+in%3Atitle&type=pullrequests — verified: 1,044 PRs by app/renovate with '[SECURITY]' in the title, created 2026-09-18..24 (raw search count, includes grouped PRs). The sampled bodies contain GHSA/CVE IDs.
- GitHub Events API payloads (PullRequestEvent actions on github.com: opened, closed, merged, reopened, assigned, unassigned, labeled, unlabeled; no synchronize) https://raw.githubusercontent.com/github/docs/main/data/reusables/webhooks/pull_request_event_api_properties.md — verified (github/docs reusables). Consequence: rebases and body edits need GraphQL/REST, not GH Archive alone.
- GH Archive (hourly event dumps; BigQuery public dataset; CC-BY-4.0) https://www.gharchive.org/ — README verified. Data host and site are blocked by our proxy. BigQuery access needs a GCP billing account (public dataset, legal). Whether PR bodies are present after the 2025 payload changes still needs a pilot check.
- GitHub search API (MCP) for pilot sampling https://docs.github.com/en/rest/search — works but does not scale: we hit a secondary rate limit after 2 queries; direct api.github.com search is blocked by session scoping. Not used in the production pipeline.
- GitHub Acceptable Use Policies, research clause ('Researchers may use public, non-personal information ... only if any publications resulting from that research are open access'; scraping is distinct from the API) https://raw.githubusercontent.com/github/docs/main/content/site-policy/acceptable-use-policies/github-acceptable-use-policies.md — verified (github/docs site-policy source)
- GitHub Advisory Database (git repository) https://github.com/github/advisory-database — verified reachable
- OSV bulk exports on GCS (e.g. npm/all.zip, 216,651,333 bytes, last-modified 2026-09-26) https://storage.googleapis.com/osv-vulnerabilities/npm/all.zip — verified
- api.osv.dev and api.deps.dev https://api.osv.dev/ — blocked by our proxy. Use the GCS bulk export, or the deps.dev BigQuery dataset (needs GCP).
- npm registry and PyPI JSON (release timestamps for age; tarballs for the lab diff) https://registry.npmjs.org/ — verified reachable
- pnpm minimumReleaseAge (default 1440 minutes since v11) https://raw.githubusercontent.com/pnpm/pnpm.io/main/docs/settings/dependency-resolution.md — verified (pnpm.io docs source). Consequence: a 24h focal point and a CI-green confounder near the 72h test.
- GitHub code search pilot counts, run today (raw, undeduplicated): pnpm-workspace.yaml with minimumReleaseAge = 32,064; .yarnrc.yml with npmMinimalAgeGate = 2,204; 'dependabot-badges.githubapp.com' under .github = 5 https://github.com/search?type=code — verified (raw counts). Earlier round counts (6,288 semver-patch fetch-metadata gates; 102 compatibility-score; 111 alert-state; 37 cvss; 34 matchConfidence; 2,888 unattended-upgrades blacklist) were carried over and not re-run.
- Prior art: He et al. TSE 2023 (Dependabot in practice); Alfadel et al. MSR 2021; Cogo, Oliva & Hassan TSE 2019 (npm downgrades); Hejderup & Gousios JSS 2022 (tests detect about half of dependency changes); Reyes et al. 2024 BUMP; Rombaut et al. TOSEM 2023; Dissanayake et al. CSCW 2022  — not verified: arXiv, Semantic Scholar, dblp, Crossref and Zenodo are all blocked by our proxy and the session web-search budget is used up. Cited from memory; must be checked in week 1.
- GitHub and Mend historical score logs, or badge-render and PR-view logs, under a research agreement  — needs agreement (no public program found or verified). Optional accelerator and exposure rescue.

### Proven Safe, Still Stuck? The Badge-Flip natural experiment, then a factorial Proof/Relevance/Placebo trial (C3 v2, with the skeptic's fixes)

**One line:** GitHub and Mend already put live "is this update safe?" badges on hundreds of thousands of real fix PRs every week, and those badges change value over time. We first log, passively and in public, how human merge behaviour responds when the displayed proof on a fixed security fix flips from "unknown" to "safe", or from "safe" to "risky". Only then do we run a pre-registered on-wedge randomized trial that separates breakage proof from relevance (reachability/exposure), from a matched placebo, and from no card.

**Hypotheses:**
- H1 (belief 2, natural experiment, primary). Scope: OSV-matched security-fix PRs, merged by a human, in repos that do not auto-merge and are not dormant, with the repo's own CI green. When the displayed Dependabot compatibility score for the SAME PR flips from 'unknown' to >=90%, the daily merge hazard rises. Model: Cox with a time-varying covariate, stratified by ecosystem x semver type x repo-activity tercile, SEs clustered by repo.
- H2 (sign test: the proof content is read, not just seen). Same scope, own CI green. A displayed score <70% LOWERS the merge hazard compared with >=90%. If low scores do not slow merges, any positive H1 effect is salience, not resolved uncertainty.
- H3 (discontinuity, Renovate). Mend Merge Confidence cannot be 'High' for npm releases under 3 days old (verified rule). At the 72h mark after the fix release, npm PRs whose badge flips Neutral->High show a jump in merge hazard. PyPI/Maven PRs crossing the same 72h mark with no rule-driven flip show no such jump (difference-in-discontinuities). The Age badge ticking to '3 days' in both ecosystems controls for the age label itself.
- H4 (proven safe, still stuck: the pre-registered falsifier). Among security fixes that are demonstrably safe (own CI green AND displayed peer score >=90% / High confidence), the share still unmerged at 30 days is SMALL (<15%). If it is large (>=35%), proof already exists and does not clear the queue, so in this venue the blocker is attention or prioritization, not impact uncertainty.
- H5 (blast radius is predictable). The peer-derived score (Dependabot compatibility %, Mend passing %) predicts the repo's own CI failure on the same update, and 30-day revert/downgrade, better than base rate. Pre-set bars: AUC >=0.70 and Brier skill >0.
- H6 (RCT, on-wedge, 2x2 + placebo + no card). Setting: real OS/package patch approvals at an RMM/patch vendor or at design partners. Randomized by tenant. Factors: breakage evidence (early-ring install-failure/rollback rates + calibrated P(break)) x relevance evidence (is the vulnerable component present/running/exposed). Empty slots are filled with a length- and numeracy-matched true placebo; a fifth arm gets no card. Belief 2 holds only if the breakage main effect > 0 AND breakage >= relevance AND (placebo - no card) is less than half the breakage effect.
- H7 (sign test in the RCT). Truthful 'elevated risk' breakage cards (oversampled so this has power) slow approval relative to placebo.
- H8 (belief 4, reversibility; phase C). Among changes with P(break) > 5%, a card showing that rollback of this exact patch was tested on N devices in the early ring, with median rollback time T, raises 14-day approval versus the breakage card alone.
- H9 (share of delay). Days of delay removed by breakage proof, as a share of median total days to approval/merge. Pre-registered: >=30% = 'the' blocker; 10-30% = 'a' contributor; <10% or CI including 0 = not the blocker.

**Pass/fail:** Registered on OSF before any outcome data is opened. The analysis code is frozen on 2 weeks of logs with outcomes masked.

MVP (natural experiment, OSS). A PASS on all four points supports belief 2 for this venue:
(1) H1: HR >= 1.25 with 95% CI lower bound > 1.05.
(2) H2: HR(<70% vs >=90%) <= 0.80 with CI upper bound < 1.0.
(3) H3: the npm jump at 72h is >= 1.3x the non-npm jump, CI excluding 1.
(4) H4: <15% of proven-safe security fixes are unmerged at 30 days.

FALSIFY (the result gets published either way):
- H1 is a precise null: HR CI inside [0.90, 1.10], with >= 2,000 flip events.
- OR H2 fails: low scores do not slow merges, so badge content is not processed.
- OR H4 >= 35%: 'proven safe, still stuck', meaning proof is available and not acted on.
- OR the pre-registered placebo flip moves merges as much as the real flip. The placebo flip is the Age badge crossing a round number, or a score flip on a DIFFERENT dependency's PR in the same repo.

Mixed result (e.g. H1 positive but H4 high): report it as 'uncertainty is one contributor', not as the cause.

Predictability (H5): AUC >= 0.70 passes. AUC < 0.60 falsifies 'blast radius is predictable from peers' for dependency updates.

Full RCT (primary, on-wedge):
- SUPPORT: breakage main effect on 14-day approval >= +8pp, or >= 20% cut in median days to approval, with CI excluding 0; AND breakage >= relevance; AND placebo-vs-none < 0.5 x breakage effect; AND the H7 sign test is significant (HR < 0.8).
- FALSIFY:
  - the breakage effect's CI upper bound is < +3pp;
  - OR (proof - placebo) is < 1/3 of (placebo - none), meaning salience;
  - OR relevance exceeds breakage by >= 5pp, meaning prioritization;
  - OR H7 fails.
- Power target: 80% power to detect 10pp at alpha 0.05, assuming ICC 0.1 and ~20 changes per tenant per quarter. That gives design effect ~2.9, so >= 1,150 changes per arm, about 60 tenants per arm, about 300 tenants over 5 arms.
- Stop rule: halt and notify if the breakage-proof arm's post-deploy failure/rollback rate exceeds placebo by >2pp absolute, or if calibration error (ECE) is > 0.10.

**Data pipeline:** PHASE 0 / MVP: passive and observational. No messages to anyone.

1. ENUMERATE bot PRs daily.
- Use the GitHub Search API. Verified: 317,204 Dependabot PRs carrying 'Dependabot compatibility score' were created in about 7 days, and 543 Renovate '[SECURITY]' PRs in 6 days.
- Search caps results at 1,000 per query, so slice queries into 20-minute created: windows.
- GH Archive (BigQuery) is the backfill and cross-check. Check post-2025 Events API payload trimming before relying on its body fields.

2. CLASSIFY security fixes.
- Parse (ecosystem, package, from, to) from the PR title and body.
- Label a PR as a security fix when 'from' is inside an OSV/GHSA affected range and 'to' is >= the fixed version. Use the OSV bulk export, which does not depend on the bot calling it a security update.
- Tag KEV-linked CVEs using CISA KEV.

3. LOG DISPLAYED PROOF, going forward.
- For every open PR, every 3-6h, fetch the badge the maintainer actually sees: body_html from the REST API, then the camo-proxied badge URL. Periodically also fetch the origin URL to measure cache staleness.
- Dependabot: parse the SVG '<title>compatibility: NN%</title>' exactly as GitHub's own dependabot/fetch-metadata action does.
- Renovate: the Mend Confidence/Age/Adoption/Passing badges. Only with Mend's written OK; until then, Dependabot only.
- Record flip timestamps.
- Get npm release timestamps from registry.npmjs.org 'time' (the 72h mark).

4. OUTCOMES.
- REST: merged_at, merged_by, closed_at.
- check-runs conclusion at the head SHA: own CI green/red.
- Exclusion flags:
  - auto-merge (workflow files calling 'gh pr merge --auto' or gating on compatibility-score; 107 such files verified; Renovate automerge config; merged_by a bot);
  - dormant repo (no human push in 90d);
  - minimumReleaseAge / stabilityDays set.

5. REVERT/BREAKAGE LABELS.
At day 30, read the manifest/lockfile on the default branch. Label as reverted if the dependency is back below the fixed version, or if there is a 'Revert' PR/commit naming the package.

6. STORAGE.
- Repo IDs are SHA-256 hashed with a secret salt. No maintainer identities.
- Only aggregate tables leave the pipeline.
- About 6 REST calls per PR, which fits one GitHub App's rate limit.

7. ANALYSIS.
Survival models with time-varying displayed score. Diff-in-discontinuity at 72h. AUC/Brier for H5. Share-of-delay (H9) as a counterfactual median.

FULL VERSION adds:
(a) A data request to GitHub/Mend, under a research agreement, for any internal A/B or staged-rollout data on the compatibility score / Merge Confidence.
(b) RCT telemetry from the RMM/patch vendor or design partners. Per patch x tenant: availability time, card arm, card-detail click (expand event), approval time, ring progression, install failures, rollbacks, post-deploy incidents. Exported as aggregates or pseudonymous rows under a DPA.
(c) Calibrated P(break) for OS patches, built from early-ring outcomes on the same build/KB plus component-presence data, and scored against later-ring failures.
(d) The dependents' test harness for the OSS arm. deps.dev's API gives only dependent COUNTS (verified), so dependent lists come from the deps.dev BigQuery dataset or GitHub's dependency graph. Clone K public dependents and run their tests in Skylayer's own lab.

**6-week MVP:** MVP scope: fully passive, public, technical logs. No messages to anyone, so it complies with 'technical evidence only'.

Week 1: set up and pre-register.
- Write and register the OSF pre-registration: H1-H5, H9, exclusions, models, pass/fail thresholds, placebo flips.
- Freeze the analysis code on synthetic column schemas, with no outcome data.
- Email GitHub (courtesy notice plus request for any internal compatibility-score A/B data) and Mend (permission to poll Merge Confidence badges plus an A/B data request).
- Get an IRB determination (expected: not human-subjects research, or exempt).
- Build the enumerator: Search API in 20-minute slices, Dependabot first.

Week 2: start forward logging.
- Poll camo and origin badges every 3-6h for every new open PR.
- Build the OSV/GHSA security-fix classifier and validate it on 200 hand-checked PRs.
- Add KEV tagging.
- Add exclusion flags: auto-merge workflows, bot merges, dormancy, minimumReleaseAge.
- Measure camo cache staleness.

Week 3: calibration study (H5), retrospective.
- Pull about 20k closed PRs from the last 60 days.
- Score the current peer score against the own-CI result and against the day-30 revert/downgrade.
- Caveat: today's score uses more data than the score shown at the time, so report the bias.
- Add the Renovate/Mend stream if Mend says yes. Otherwise restrict H3 to a Dependabot-only analogue: the 'unknown' -> numeric flip.

Week 4: first descriptive readout, on data already out of the pre-registered masking window.
- H4 'proven safe, still stuck' share at 14 and 30 days for security fixes.
- Flip-event counts, to confirm H1 is powered (target >= 2,000 flips; if the count is lower, extend logging and say so).
- In parallel, start partner outreach for the RCT: the design partner; 2-3 RMM/patch vendors (NinjaOne, plus non-competing patch-content vendors); an MSP.

Week 5: run the frozen analysis on 4 weeks of forward-logged PRs.
- H1, H2, H3 and H9, with clustered SEs.
- The placebo-flip checks.
- The pre-registered robustness checks: own-CI green only; human merges only; patch-level only; KEV subset.

Week 6: publish and plan the RCT.
- Open-access write-up with aggregate numbers only: no repo or package names for unmerged fixes; k >= 20 per cell.
- Release the code and the salted-hash dataset schema.
- Compute the RCT power from the observed ICC and base rates.
- Draft the RCT protocol (arms, placebo text, stop rules) for IRB review.

Deliverables:
- the one-number post (the H4 share, plus the H1/H2 flip effect);
- a calibration curve (H5);
- a go/no-go on the RCT.

Cost: about 1 engineer for 6 weeks, a $100/month VM, and BigQuery under $300. Zero partner dependency for the core result.

**Full version:** Timeline: 9-15 months, $80-200k (plus partner engineering time). Four phases.

A. Scale the natural experiment (months 0-6):
- Six months of forward logging across npm/PyPI/Maven/Go/NuGet, with Renovate badges if permitted.
- The Dependabot 'unknown'->numeric flip analysis, plus the Renovate npm 72h diff-in-discontinuity.
- The KEV subgroup.
- A superior add-on if granted under agreement: GitHub/Mend internal staged-rollout or A/B data on the badges, which would be true randomization at scale.

B. On-wedge RCT (months 3-12; the primary causal test of belief 2). Run with an RMM/patch vendor, or pooled across 3-5 design partners (including the FDA-regulated medical-device CIO+CISO), on real OS/package patch approvals.
Five arms, randomized by tenant/approver:
1. no card;
2. placebo card: true, equal length, equally numeric, non-diagnostic release logistics (KB/package release date, size, supersedence chain, checksum);
3. breakage card: early-ring install-failure and rollback rates on the same build, calibrated P(break), with known issues shown to ALL arms;
4. relevance card: component present/running/exposed on this tenant's fleet;
5. breakage + relevance.
Rules:
- The fix itself is never delayed and urgency/KEV status is never withheld; only the extra card varies.
- Oversample patches with non-trivial predicted risk so the H7 sign test has power.
- Card-detail expand clicks serve as a no-survey manipulation check.
- Outcomes: days to approval and to production-ring deployment, 14-day approval rate, rollbacks, post-deploy failures.
- Report delay removed as a share of total delay (H9).
- Target about 300 tenants / 5,800 changes.
- Within the design partner (small N), randomize at the change-ticket level as a calibration pilot; the pooled vendor venue carries the causal claim.

C. Reversibility RCT (months 9-15): among P(break) > 5% changes, the breakage card vs breakage + tested-rollback card (rollback of this exact patch validated on ring-0 devices, median rollback time) (H8, belief 4).

D. Optional OSS RCT (secondary; calibration and the sign test only):
- An opt-in self-hosted-Renovate GitHub App.
- Merge Confidence badges held constant: disabled in all arms via ignorePresets, or shown in all arms.
- Repo-level randomization.
- Exclude auto-merge and dormant repos.
- Dependents' tests run in Skylayer's lab. deps.dev BigQuery supplies the dependent lists, because the API gives only counts.
- >= 400 PRs per arm, which means about 2,000+ repos.

DIVD is dropped: the case closed on notification day with no rescans, and urgency cannot ethically be removed.

Outputs:
- Skylayer's first calibration dataset (predicted vs realized breakage) for OS patches.
- A pre-registered causal answer to belief 2.
- A demo of the product's proof card, validated in the field.

**Headline if true:** "Same security fix, different badge. When GitHub's bot showed 'compatibility unknown', X% of maintainers whose own tests were green merged within 14 days; when the badge flipped to '>=90% of other projects pass', Y% did. Low scores slowed merges. In a randomized trial on N real OS patches, a blast-radius proof cut approval delay by Z days (P% of all delay), twice what exposure info did, and a same-length placebo did nothing. Fear of breakage is a measurable, removable part of the patch gap."

**Headline if false:** "Proven safe, still unpatched. Of N real security fixes that passed the project's own tests AND showed >=90% passing across other projects, P% were still unmerged 30 days later. Flipping the safety badge from 'unknown' to 'safe' moved merges by under 2 points. In the randomized patch trial, attention and exposure information beat breakage proof. The remediation gap is not fear of breakage; it's attention and prioritization."

**Legal checklist:** MVP (observational):
- [ ] GitHub AUP research clause, verified: public non-personal information only, and publication must be open access. Stay within API rate limits (ToS section H). Use an authenticated GitHub App token. Do no HTML scraping beyond the API.
- [ ] Dependabot badge endpoint: public, and called by GitHub's own Action. Poll politely (<= 1 request per PR per 3h, with backoff). Courtesy notice to GitHub.
- [ ] Mend badge endpoint: terms not verified, so get written permission BEFORE automated polling; exclude the Renovate stream if refused.
- [ ] No comments, PRs, issues, stars or any interaction with non-consenting repos.
- [ ] Unmerged security fixes are live exposures. Never publish repo, package-instance or org names. Aggregate reporting only, with k >= 20 per cell. Hash repo IDs with a salt. Store no maintainer identities.
- [ ] IRB determination (expected: not human-subjects research, or exempt; public behavior, no intervention).
- [ ] OSF pre-registration before outcomes are unmasked.
- [ ] Scratch data outside any repo; delete raw data after 12 months.

RCT (full):
- [ ] Flag to the founder: this is a human-behavior field experiment and strains 'technical evidence only'. Outcomes are behavioral logs, and it is sequenced AFTER the passive study.
- [ ] Full IRB review. Consent via opt-in/partner terms that disclose randomized informational cards. Debrief at the end.
- [ ] Partner DPA and data minimization. Pseudonymous or aggregate exports. No customer identification. Respect the vendor's own customer terms.
- [ ] Truthful content only. No arm withholds urgency, KEV status or known-issue information. The fix is never delayed.
- [ ] Pre-set stop rule on proof-arm harm (> 2pp excess failures/rollbacks) and on calibration error.
- [ ] Click telemetry disclosed in consent.
- [ ] For the medical-device partner: keep the study outside regulated product change control (IT fleet only), or document it under their QMS (21 CFR 820 / IEC 62304) with the partner's QA sign-off.
- [ ] Coordinated disclosure path in case the analysis surfaces a systemic issue (e.g. a mis-scored badge) to GitHub or Mend.

**Biggest risks:** 1. Confounding in the natural experiment: a low displayed score correlates with genuinely harder updates.
- Mitigations: condition on own CI green; use within-PR time-varying flips rather than cross-PR comparisons; use the 72h mechanical rule; use pre-registered placebo flips.
- Residual confounding remains, so the natural experiment is strong but not randomized. That is why phase B exists.

2. Flip timing is endogenous. The Dependabot score appears once enough public repos ran the update, which is itself a sign of popularity/momentum. Mitigate with stratification by package popularity and with the npm-vs-non-npm diff-in-discontinuity.

3. Measurement: whether maintainers actually see the badge, and camo caching staleness. Measure staleness, and treat the flip as an intention-to-treat exposure.

4. Venue mismatch: OSS maintainers are not enterprise blast-radius owners. The on-wedge causal answer depends on an RMM/patch partner that may see Skylayer as a competitor. Mitigate with pooled design partners and non-competing patch-content vendors, and report honestly if no partner signs.

5. Power:
- the npm under-72h security subset may be small;
- the RCT needs about 300 tenants.
Mitigations: use all update types for the mechanism test, with security as the headline subgroup; state MDEs up front.

6. Mend may refuse badge polling, and GH Archive payload changes may limit the backfill; Search API caps need careful slicing.

7. Prior art: GitHub/Mend may already hold A/B data showing a small effect. Ask for it first; a small published effect lowers the prior but is still evidence.

8. Outcome risk: the most likely result may be 'proven safe, still stuck' (H4 high). That falsifies belief 2 for OSS. It is valuable to know, but it forces a pivot in messaging (from 'proof unblocks' to 'proof plus action/ownership').

9. RCT ethics and reputation: a wrong proof could cause an outage. Covered by the stop rule, calibration gates and truthful-only content.

**Why it cuts the noise:** Every vendor claims that 'confidence', 'prioritization' or 'safe auto-remediation' is what unblocks patching, and nobody has shown whether showing breakage evidence changes what humans do. This study uses safety-proof badges the industry already ships (GitHub's compatibility score and Mend's Merge Confidence, live on hundreds of thousands of real PRs a week) as a reproducible public natural experiment. It also produces one blunt number anyone can recompute from public data: the share of security fixes that are provably safe and still unmerged.

It is designed to be able to lose. The sign test, the placebo flips and the proven-safe-still-stuck falsifier mean a null or a negative result is publishable and decisive. The factorial RCT then separates breakage proof from relevance, salience and urgency on real OS patches, the four explanations the market blurs together.

Either outcome replaces a vendor narrative with a counterfactual. It tells Skylayer, and the industry, whether 'proof' is a product, or whether the gap is attention and ownership.

**Sources:**
- GitHub Docs: Dependabot security updates 'compatibility scores' (computed from CI in other public repos with the same update) https://raw.githubusercontent.com/github/docs/main/content/code-security/concepts/supply-chain-security/dependabot-security-updates.md — verified. Text read from github/docs (content/code-security/concepts/supply-chain-security/dependabot-security-updates.md) via raw.githubusercontent.com
- dependabot/fetch-metadata (official Action): compat-lookup -> compatibility-score output, parsed from the badge SVG https://github.com/dependabot/fetch-metadata — verified. README plus source: fetches https://dependabot-badges.githubapp.com/badges/compatibility_score?dependency-name=..&package-manager=..&previous-version=..&new-version=.. and regex-parses '<title>compatibility: NN%</title>'
- Dependabot badge endpoint (dependabot-badges.githubapp.com) https://dependabot-badges.githubapp.com/badges/compatibility_score — URL format verified via official Action source. Direct fetch blocked by this sandbox's egress proxy. It is a public endpoint that GitHub's own Action calls programmatically
- Live volume: Dependabot PRs carrying 'Dependabot compatibility score' created 2026-09-20..26 https://github.com/search?q=author%3Aapp%2Fdependabot+%22Dependabot+compatibility+score%22&type=pullrequests — verified via GitHub Search API: total_count 317,204 (all update types; the security subset is to be classified via OSV)
- Auto-merge gates on compatibility-score in GitHub workflows (the 'gate by confidence' that already exists; used as an exclusion flag) https://github.com/search?q=%22compatibility-score%22+path%3A.github%2Fworkflows&type=code — verified via GitHub code search: 107 workflow files, e.g. 'compatibility-score >= 90' -> gh pr merge --auto
- Renovate docs: Merge Confidence (Age/Adoption/Passing/Confidence badges; Low/Neutral/High/Very High; npm cannot be High before 3 days old; Merge Confidence Workflows; ignorePresets to disable) https://raw.githubusercontent.com/renovatebot/renovate/main/docs/usage/merge-confidence.md — verified. Full doc fetched from renovatebot/renovate docs/usage/merge-confidence.md
- Mend Merge Confidence badge endpoint (developer.mend.io/api/mc/badges/{age|confidence}/{manager}/{pkg}/{from}/{to}) https://developer.mend.io/api/mc/badges/ — URL format verified in a live Renovate [SECURITY] PR body (543 such PRs created 2026-09-20..26 via search). developer.mend.io was blocked from this sandbox, so Mend's terms for automated polling are NOT verified: needs Mend's written permission
- deps.dev API (GetDependents) https://github.com/google/deps.dev/blob/main/api/v3alpha/api.proto — verified via google/deps.dev v3alpha api.proto. Returns only dependent_count/direct/indirect COUNTS, not a list of dependents; api.deps.dev blocked from sandbox. Dependent lists need the deps.dev BigQuery public dataset (not verified this session)
- GH Archive (public GitHub event stream, BigQuery) https://www.gharchive.org/ — verified. README references BigQuery; data host blocked from sandbox. From memory, not verified: GitHub trimmed Events API payloads in 2025, so check PR body availability; the Search/REST API is primary
- GitHub Advisory Database (GHSA) https://github.com/github/advisory-database — verified. Repo README reachable
- OSV (affected ranges and fixed versions; bulk export) https://osv.dev/ — verified. osv.dev README reachable; api.osv.dev blocked from sandbox (public service)
- CISA KEV catalog https://github.com/cisagov/kev-data — verified via cisagov/kev-data mirror: catalogVersion 2026.09.25, 1,726 entries
- npm registry (release 'time' field for the 72h rule) https://registry.npmjs.org/ — verified. registry.npmjs.org reachable and returns package documents
- GitHub Acceptable Use Policies: research clause https://github.com/github/site-policy/blob/main/Policies/acceptable-use-policies/github-acceptable-use-policies.md — verified text: 'Researchers may use public, non-personal information from the Service for research purposes, only if any publications resulting from that research are open access'; API use is governed by ToS section H
- DIVD case DIVD-2025-00039 (Cisco ASA, ips: 40887) https://github.com/DIVD-NL/web-csirt-nl — verified: case opened 2025-09-25, closed 2025-10-03, no rescans or outcome tracking. The DIVD venue is DROPPED
- NinjaOne patch-management API fields (RMM venue) https://www.ninjaone.com/ — not re-verified (ninjaone.com blocked from this sandbox). Relies on the earlier round's verification; the RCT itself needs a partner agreement
- OSF pre-registration https://osf.io/ — not verified (osf.io blocked from sandbox); standard public service
- Prior art: Microsoft Nudge (Maddila et al., FSE 2022 / TSE); randomized notification RCTs (Durumeric IMC 2014; Li et al. USENIX Sec 2016; Stock et al. 2016/2018; Cetin et al. 2019; Maass et al. USENIX Sec 2021); He et al. TOSEM 2023 on Dependabot  — not verified: from memory, scholarly domains blocked. None known to pit a safety proof against a matched placebo on real fixes
- Design partner (FDA-regulated medical-device AI company, CIO+CISO): within-org change-ticket randomization  — needs agreement

### Canary Order v2: "The fix was already on their test box." A pre-registered, passive, within-fleet test of whether servers wait for fixes because of uncertainty about breakage

**One line:** Using existing research scan archives (no scanning), take fleets of Ubuntu and Debian servers managed with the same tooling. After a fleet's own team has installed a security update on one of its hosts, measure how long the update takes to reach the servers that many domains depend on. Test whether that wait grows with the update bundle's history of breakage and shrinks after safety news, and split total exposure into four parts: forgotten hosts, fleets that had not started patching, automatic updates, and hosts delayed after the fleet's own first patch. The design is built so that it can come out against belief 2.

**Hypotheses:**
- Unit of analysis. A 'fleet' is a management domain inferred from behaviour, as the skeptic's fix 1 asks. Its hosts must share an organization link (AS2Org or ASdb org-owned ASN, a registrable domain in certificate SANs, or reverse DNS). They must also share an sshd configuration fingerprint (the KEXINIT kex, cipher, MAC and host-key-algorithm lists, HASSH-server style) and host-key type. And they must have co-patched in the same scan interval on at least 2 earlier USNs. An 'install event' is a change in a host's OpenSSH (or PHP) package revision. That revision is only a marker: the treatment is the whole bundle of pending security updates installed at that moment. t0_fleet is the first MANUALLY patched host in the fleet (see H4 for how auto hosts are classified). Pilot USNs (USN-6560-1, USN-6859-1, USN-7270-1) are exploratory and are never reused in the confirmatory tests.
- H0 (exposure decomposition, pre-registered thresholds). Split all host-days of exposure to a fixable, published USN in the manual-fleet panel into four buckets: (a) FORGOTTEN, no install event within 180 days; (b) FLEET-NOT-STARTED, before t0_fleet, which covers awareness and capability; (c) SELF-PROVEN DELAY, after t0_fleet plus the fleet's first observed install window, on hosts that were eventually patched; (d) AUTO-HOST LAG. Belief 2 can only matter in practice if bucket (c) is at least 25% of exposure host-days.
- H1 (order sign test). Among eventually-patched manual hosts in fleets that have at least 3 same-release, same-role hosts seen before the fix, and a real spread in blast radius (BR), the hazard of installing the fix falls with outside-in BR: a Cox model stratified by fleet × install event gives HR(top vs bottom BR tercile) < 1. Also, the top-BR host is patched strictly last more often than the chance rate. Prioritization and the unknown-asset story both predict HR > 1.
- H1-mag (magnitude, the skeptic's fix 2). For events whose pending bundle contains a CVE that is KEV-listed, has EPSS >= 0.1, or has public PoC code, the median lag of top-BR hosts beyond the fleet's first observed install window is at least 14 days. Staged rollout on its own does not count as support.
- H2 (dose-response on ex-ante bundle uncertainty, the skeptic's fix 3). The BR gradient in the hazard gets steeper as the pending bundle's ex-ante UNCERTAINTY score rises. That score is built from the pending source packages' regression-USN history over the past 24 months, any new upstream version in the bundle, and debdiff size. The model also controls for DOWNTIME/EFFORT covariates entered separately: whether the bundle contains a kernel, glibc, openssl or systemd update (restart or reboot proxies), and the package count. Prediction: the BR × uncertainty interaction is > 0. A fixed soak or change-board policy predicts a flat interaction.
- H3 (reaction to safety news). This uses the 74 regression-titled USNs that affect jammy (2022–2026) and the 44 that affect noble, all counted in this session. H3a: when a regression USN is published for a package pending in a host's bundle, the install hazard of unpatched high-BR hosts drops more than that of low-BR hosts in the same fleet (difference-in-differences). H3b: when the '-N' regression fix is published, high-BR hosts catch up with a surge. H3c (placebo): regression USNs for packages NOT in the server seed produce no BR-differential response. No coordination or prioritization story predicts a response to safety news that depends on BR.
- H4 (automation frontier, belief 4). A host is classified 'security-only unattended-upgrades' if (i) it is never observed on an -updates-only (SRU) revision across the panel, and (ii) it adopts -security revisions within 1 scan interval in at least 80% of USNs. Prediction: within a fleet, P(auto) falls with BR (OR per tercile < 0.8). The pocket-fingerprint rule works because Ubuntu's default Allowed-Origins covers -security and ESM but not -updates, and SRU-only revisions exist: jammy openssh 0.4 and 0.7, noble 13.5, 13.7, 13.9 and 13.12–13.14, php8.1 2.3–2.6, 2.9 and 2.15. A host seen on one of these revisions was upgraded by a human, by config management, or by a non-default u-u setup. This works at weekly cadence.
- H5 (unknown-asset arm, the skeptic's fix 4). P(FORGOTTEN, i.e. no install within 180 days) is modelled as its own outcome. The unknown-asset story predicts it falls with BR and makes up most of the exposure in H0. It is kept apart from H1 so that canaries and forgotten boxes cannot cancel each other out.
- H6 (exploratory, demoted, the skeptic's fix 6). A validated revert upper bound: the same host key on the same IP with the same TLS cert or hostname moves to a lower revision within 30 days, with no multi-revision flapping in the same week. We report ex-ante bundle features vs reverts (PR-AUC, calibration) as exploratory only, and never in the headline.
- Negative controls. NC1: patch order does not follow IP numeric order or hostname lexical order (|HR-1| < 0.05). If it does, scripted inventory order such as Ansible serial is at work, and it is reported separately. NC2: order does not follow host build order (first-seen date). NC3: a placebo 'BR' (a hash of the IP) has HR of about 1.

**Pass/fail:** Everything below is registered on OSF or AsPredicted before any confirmatory data is looked at. Multiplicity: Holm correction across H1–H5. Smallest effect size of interest (SESOI): HR 0.90, and 7 days of lag.

GO/NO-GO (the skeptic's fix 7, judged on the pilot using only pre-fix covariates plus eventual patching). Continue only if at least 300 eligible fleets exist (at least 3 same-release, same-role, eventually-patched manual hosts, with a BR spread where the top host has at least 2x the SAN/domain fan-in of the bottom one), AND the order tie rate at the available cadence is at most 60%, AND the honeypot/banner-rewrite filter removes at most 30% of candidate hosts. Otherwise stop, or buy data with daily cadence before going on. In neither case is a result claimed.

BELIEF 2 SUPPORTED, strong form ('delay is caused by uncertainty about this change'). All of these must hold:
(1) H1 HR < 1, with the upper 95% CI bound < 0.90;
(2) H1-mag median of at least 14 days on KEV, EPSS >= 0.1 or PoC bundles;
(3) either the H2 interaction > 0 with the CI excluding 0 after Holm correction, or H3a DiD in the predicted direction at Holm-corrected p < 0.01 with the H3c placebo null;
(4) H0 bucket (c) is at least 25% of exposure host-days;
(5) NC1–NC3 are null.

WEAK FORM, must be labelled as NOT supporting per-change doubt: (1), (2) and (4) hold, but H2 and H3 are both null, shown by an equivalence test that rules out effects larger than the SESOI. The conclusion is then 'blast radius drives delay through blanket staging or freeze policy', and it has to be stated that way.

BELIEF 2 FALSIFIED for internet-facing Linux fleets if ANY of these holds:
- H1 HR >= 1, with the lower CI bound >= 0.95 (important servers patched first or at the same time);
- H0 bucket (c) is below 10% of exposure host-days, while forgotten plus not-started make up more than 60% (the unknown-asset and awareness stories win);
- the H1-mag median is under 3 days (the wait is trivial).
A falsification is published under the same headline template.

AMBIGUOUS. If NC1 fails (order follows IP or hostname sort), scripted order dominates. H1 then counts as uninterpretable, and only H2, H3 and H4 are reported.

BELIEF 4 / automation frontier. Supported if the H4 OR per BR tercile is < 0.8 with the CI excluding 1. Falsified if the OR is >= 1 (robots are trusted on crown jewels at least as often).

Proof mechanism (can blast radius be predicted?). Only exploratory. PR-AUC on reverts is reported with its CI, and a result below 2x the base rate is stated as 'not predictable from public ex-ante features'.

**Data pipeline:** No scanning. Every host observation comes from existing research archives.

Stage 1: clock library (public, built this session).
- Pull every USN for jammy (2,573), noble (1,507) and focal, from the Ubuntu notices JSON API.
- From Launchpad +publishinghistory, pull per-pocket publish timestamps for openssh, php8.x and every source package in the ubuntu-server seed.
- Flag SRU-only (-updates-only) revisions.
- Flag regression USNs by title (74 affect jammy, 44 affect noble).
- Join EPSS daily scores, CISA KEV dates, and first-public-PoC dates (from GitHub/ExploitDB timestamps) per CVE.
- Compute each bundle's uncertainty score (regression history, new upstream version, debdiff size from Launchpad diffs) and, separately, its downtime score (kernel, glibc, openssl, systemd, package count).
- Debian (DSA/DLA plus point releases, with banners like 'Debian-2+deb12u9') is added in the full version, because the Debian tracker is blocked from here.

Stage 2: host panel.
- Source: the Censys BigQuery research snapshots (censys-io.research_1w and research_1m universal_internet_dataset). The MVP is weekly. The full version uses commercial Censys daily data or a Shadowserver/CERT partnership.
- Fields: ssh banner, ssh.server_host_key.fingerprint_sha256, KEXINIT algorithm lists, the co-located 443 certificate SANs and HTTP X-Powered-By header, rDNS and ASN.
- Key the panel on host key, then track IP and hostname as time-varying attributes.
- Parse banners like 'OpenSSH_8.9p1 Ubuntu-3ubuntu0.10' into release plus revision.
- Pseudonymise IPs at ingestion with a keyed HMAC.

Stage 3: filters.
- Drop honeypots: banners that rotate between scans, and static fake banners.
- Drop banner-rewriting middleboxes with a KEX consistency check. Example: the strict-KEX extension (Terrapin) must be present when the banner is jammy 0.5 or later.
- Drop host keys shared by more than 3 IPs, end-of-life and ESM-only releases, and hosts first seen after the fix shipped.
- Hosting, cloud and MSP ASNs, as labelled by ASdb, go into a separate stratum rather than being dropped.

Stage 4: fleets.
- Organization link: AS2Org/ASdb org-owned ASN, the registrable domain in SANs, or rDNS.
- Behavioural cluster: an identical KEXINIT/config fingerprint plus co-patching in the same interval on at least 2 earlier USNs.
- Store three linkage-confidence tiers for sensitivity analysis.

Stage 5: blast radius, measured from outside. Each measure is pre-registered separately and also as a composite:
- the number of distinct FQDNs and SANs the host serves;
- MX/NS/A/CNAME fan-in, from OpenINTEL public ccTLD and toplist data in the MVP, and from gTLD data under an OpenINTEL agreement plus CZDS NS data in the full version;
- Tranco-weighted reach;
- a hostname tier (prod/www/api/mail versus dev/test/stage/uat/qa);
- role, used as a stratum (mail, DNS, web, bastion).

Stage 6: clocks and classifiers.
- For each host, the install event interval-censored between two scans.
- t0_fleet: the first manual install event in the fleet.
- The fleet's install-window profile (weekday and hour modes, where the cadence allows).
- The H4 pocket-fingerprint auto classifier.
- The H0 bucket assignment for every exposed host-day.

Stage 7: models.
- Interval-censored discrete-time or stratified Cox models (strata: fleet × event).
- A rank test for top-BR-last.
- The H2 interaction.
- H3 difference-in-differences with fleet fixed effects.
- Within-fleet conditional logit for H4.
- Negative controls.
- Sensitivity checks: by linkage tier, cadence, role, and cloud versus on-prem.

Stage 8: outputs.
- k-anonymous aggregate tables (at least 10 fleets per cell).
- Open code.
- No host-level release.
- A standing 'Canary Index' page.

Internal validations built into the pipeline:
- On hosts where both the SSH and PHP markers are visible, check whether they bump together. This tests the assumption that a marker bump means the whole bundle was installed.
- In the full version, compare against partner ring configs.

**6-week MVP:** Precondition, week 0. The academic co-lead already holds Censys research access, or Skylayer buys a 1-month commercial Censys/Shodan historical licence; which one decides the terms under which results can be published. If neither is in hand, the 6 weeks start when access arrives. Weeks 1 and 2 run without scan data either way.

WEEK 1: pre-registration and clock library.
- Draft and lock the pre-registration: H0–H6, thresholds, SESOI, go/no-go, pilot/confirmatory split.
- Build the clock library from the Ubuntu USN API and Launchpad: jammy and noble, openssh plus php8.1/8.3 plus server-seed packages; SRU-only revision table; 74+44 regression USNs.
- Build the bundle uncertainty scorer and the downtime scorer.
- Join EPSS, KEV and PoC dates.
- Deliverable: a clock table open-sourced on GitHub.

WEEK 2: panel extraction.
- Run BigQuery pulls of port-22 Ubuntu jammy/noble banner hosts, Jul 2023 to Sep 2026, with host keys, KEXINIT and co-located 443 certs.
- Pseudonymise IPs.
- Apply the honeypot/rewrite filter (rotating banners, strict-KEX consistency).
- Deliverable: host-key panel stats (hosts, persistence, cadence, share filtered).

WEEK 3: fleets and blast radius.
- Organization linkage (AS2Org, ASdb, SAN, rDNS).
- Behavioural fleet clustering (config fingerprint plus co-patching on pre-pilot USNs).
- BR features from SAN/FQDN count, hostname tier, OpenINTEL public ccTLD and toplist fan-in, and role.
- GO/NO-GO COUNT: the number of eligible fleets and the tie rate at weekly cadence. If there are fewer than 300 fleets or ties exceed 60%, stop and write the kill memo, or move to daily data.

WEEK 4: pilot analyses (exploratory) on USN-6560-1 (Terrapin), USN-6859-1 (regreSSHion) and USN-7270-1.
- H0 exposure decomposition.
- H1 order test and H1-mag.
- H4 pocket-fingerprint automation frontier.
- H5 forgotten arm.
- NC1–NC3.
- Measure effect sizes and variance to run the power analysis for the confirmatory set.

WEEK 5: remaining pilot work and lock.
- H2 bundle interaction and H3 regression-event DiD, on the pilot window only, to check power.
- Run the SSH/PHP co-bump check of the bundle-install assumption.
- Sensitivity by linkage tier.
- Freeze code.
- Update the pre-registration with the pilot-based power analysis before any confirmatory USN is touched.

WEEK 6: confirmatory run and memo.
- Run the confirmatory set: all other jammy/noble OpenSSH and PHP install events, 2023–2026.
- Produce k-anonymous tables.
- Write the internal memo scoring each hypothesis PASS/WEAK/FAIL, and draft the headline, whichever way it came out.
- Seven-day embargo while the co-lead reviews.
- Decide: publish the preprint, or run the full version.

Budget: $2–10k BigQuery. $0 data if an academic holds access; otherwise about $5–20k for one month of commercial historical data. About 1.5 FTE.

**Full version:** Timeline 6–12 months, plus extensions. Paper target: IMC or USENIX Security, plus a standing public 'Canary Index'.

1) Data upgrades.
- Daily-cadence host data from a commercial Censys licence or a Shadowserver/CERT partnership, so canary-to-production lags of a few days can be resolved and ties drop.
- An OpenINTEL gTLD agreement and CZDS for .com/.net/.org fan-in.
- Ten years of history (2016–2026): Ubuntu xenial through noble, and Debian stretch through trixie (DSA and point-release banners).
- PHP replication over HTTP.

2) Full confirmatory battery (H0–H5) over all USN/DSA install events. H3 on every regression USN touching the server seed, which gives hundreds of events across releases.

3) Validation partner under a data agreement (technical data only). The candidates are an MSP or RMM vendor, or the FDA-regulated medical-device company as an inside-out validator. They supply their ring/wave configuration, CMDB criticality and change-freeze calendar for hosts that are also visible from outside. We test whether outside-in BR ranks match the internal criticality and ring order (Spearman correlation, with a pre-registered minimum), and whether our auto-classifier matches their u-u configuration. This addresses the reviewer objection that BR is only a proxy.

4) Extensions, each 2–4 months:
- the same within-fleet order test on KEV edge appliances (FortiGate, NetScaler, Ivanti) from existing fingerprint datasets, HQ vs branch;
- Kubernetes /version build strings, dev vs prod;
- a sector cut on ASdb health care;
- a cloud/hosting stratum using certificate/SAN-based fleets.

5) Proof-mechanism study. Validated reverts and partner-labelled breakages, predicted from ex-ante bundle features (PR-AUC, calibration). This is the seed of Skylayer's confidence gate, but only if a commercial licence covers product use.

6) Quarterly Canary Index. The self-proven delay share, the automation frontier, and exposure days after PoC or KEV. Open code, k-anonymous tables, results published whichever way they come out.

Cost: $10–40k compute, $20–100k a year for commercial data, 1 academic co-lead, and 1–2 FTE.

**Headline if true:** "The fix was already on their test box. Across N server fleets, the same team that had installed a security update on its own low-stakes hosts took a median X more days to put it on the servers that M+ domains depend on. That wait roughly doubled when the update bundle included a package with a recent regression, and Y% of it came after public exploit code existed. Forgotten servers accounted for only W% of the exposure. The rest was deliberate waiting on servers the team already knew about. And Z% of teams let automatic updates touch their throwaway boxes but not their crown jewels."

**Headline if false:** "It isn't fear of breakage. Across N fleets, the most depended-on servers got security fixes first or at the same time as the low-stakes ones (HR = …). A breakage-prone update bundle did not change that order. W% of all exposure came from servers nobody patched for 180 days, and V% from fleets that hadn't started patching at all. The internet's patch gap is forgotten assets and slow starts, not hesitation." Skylayer would publish this anyway, because it was pre-registered. It would then drop belief 2 and move the wedge toward asset discovery and coordination, rather than proof of safety.

**Legal checklist:** - No scanning, probing, login attempts or banner grabs by Skylayer. Only existing research datasets are used, so CFAA and Computer Misuse Act exposure is nil. No system is touched beyond normal public web visits to Ubuntu and Launchpad pages.
- Data licences:
  - Censys research terms: academic, non-commercial. There must be an academic co-lead who is the data controller for the published study.
  - OpenINTEL CC BY-NC-SA 4.0: non-commercial, and ShareAlike applies to derived tables, so any released aggregates carry the same licence.
  - CZDS: a per-TLD agreement, with no redistribution of zone data.
  - CAIDA AS2Org: follow its acceptable-use policy and acknowledgement terms.
  - ASdb, Tranco, EPSS and KEV: attribution.
  - Get written confirmation from Censys and OpenINTEL that a startup-sponsored academic paper plus Skylayer citing its public findings is acceptable. Any product use needs separate commercial licences (Censys or Shodan enterprise).
- GDPR/UK GDPR: IPs and hostnames may be personal data.
  - Run a legitimate-interest assessment and a DPIA, and rely on the Art. 89 research safeguards.
  - Pseudonymise at ingestion (keyed HMAC); keep derived panels only; set a retention limit (e.g. raw data deleted after 12 months).
  - Make no attempt at re-identification beyond the org/fleet linkage the design needs.
- Ethics: review by the co-lead's IRB or ethics board (it analyses organizational behaviour), with Menlo Report principles documented.
- Publication:
  - k-anonymous aggregates only (at least 10 fleets per cell).
  - Never name or expose an organization, IP, hostname or sector cell that could identify one.
  - No exploit details. No new vulnerabilities are found.
- Coordinated disclosure: aggregate counts of high-BR hosts still missing KEV-class fixes go to Shadowserver or national CERTs through their existing notification channels. Organizations are never contacted directly.
- Pre-registration is time-stamped before any confirmatory data is touched, and the code is released so academics with the same access can reproduce it.
- Marketing: any Skylayer claims must match the paper exactly (FTC Act §5, and Lanham Act risk for comparative claims). No customer or competitor is named.
- Partner validation, if any, runs under a data-processing agreement covering only technical data, with no interviews or surveys, in line with the tournament constraint.

**Biggest risks:** 1) Staging-policy confound. H1 and H1-mag may pass while H2 and H3 come out null. The honest conclusion is then 'blanket staging or freeze policy', which is weaker support for belief 2 and practitioners may read it as good hygiene. This outcome is pre-registered and labelled as such.
2) Sample collapse. Requiring at least 3 same-release, same-role manual hosts with a BR spread, after removing honeypots, cloud and hosting, may leave fewer than 300 fleets. Mature enterprises rarely expose SSH. The go/no-go kill switch covers this.
3) Cadence. Weekly research snapshots turn most within-fleet orders into ties. Daily data costs money and pulls against non-commercial terms.
4) The bundle-install assumption may not hold. Hosts can run `apt install openssh-server`, pin packages, or use holds. The SSH/PHP co-bump check measures this, but only on hosts that expose both.
5) Outside-in BR is only a proxy for internal criticality and is tied to host role. Without the partner validation, reviewers may dismiss it.
6) Fleet inference errors. Multiple admin teams inside universities, ISPs and government networks, or MSP-managed estates, can still mix decisions. Sensitivity analysis by linkage tier covers some of this.
7) Scripted order (Ansible serial). NC1 detects it, but it can dominate.
8) Licensing limits Skylayer's product reuse. The public headline must be academic-led.
9) The FDA/medical-device relevance is thin (internet-facing Linux ≠ GxP systems). The design partner fits best as the inside-out validator.
10) Blocked verification. Censys terms, CZDS, crt.sh, Shadowserver, KEV/EPSS and Debian sources could not be re-checked from this sandbox. Web search was also exhausted, so prior art (Gasser NOMS 2014; Tajalizadehkhoob CCS 2017; Li SOUPS 2019; Tiefenau SOUPS 2020; Kotzias NDSS 2019) comes from memory and must be re-checked before any novelty claim.

**Why it cuts the noise:** The industry's story is that remediation fails for lack of visibility and prioritization, which vendors answer with more scanners and scores, or that teams simply need to 'patch faster'. This study measures teams' own behaviour. The key moment is when a team has already installed the fix on one of its hosts, which proves it knew about the fix and could apply it. From there it counts the days until the same apt update reaches the servers that other domains depend on. It then asks whether that wait tracks how risky the update bundle looks. The result is one number: the share of internet exposure that sits on servers whose owners had already installed the fix elsewhere, set against the share on forgotten servers. It is a decomposition nobody can hand-wave away as survey opinion. It needs no exploit and no scanning, and names no one. Anyone with the same academic data access can reproduce it. Because it is pre-registered to be able to falsify Skylayer's own belief 2, and the result will be published either way, it carries credibility that vendor reports cannot. The automation frontier adds a second quotable fact: 'robots are trusted on the throwaway boxes, not the crown jewels'. That fact speaks directly to whether enterprises will let a tool act.

**Sources:**
- Ubuntu Security Notices JSON API (all USNs with fixed versions per release) https://ubuntu.com/security/notices.json — VERIFIED this session. Fetched: 58 OpenSSH notices. USN-6859-1 (2024-07-01) jammy 1:8.9p1-3ubuntu0.10 and noble 1:9.6p1-3ubuntu13.3. USN-7270-1 (2025-02-18) jammy 0.11 and noble 13.8. Jammy has 10 OpenSSH security revisions 2023–2026 (0.3, 0.5, 0.6, 0.10, 0.11, 0.13–0.17, most recently USN-8721-1 on 2026-09-03). 2,573 jammy USNs, 1,507 noble USNs, and 74 regression-titled USNs affecting jammy (2022–2026).
- Launchpad source publishing history (exact per-pocket publish timestamps; SRU-only revisions) https://launchpad.net/ubuntu/+source/openssh/+publishinghistory — VERIFIED this session (web pages). Timestamps are exact, e.g. jammy openssh 0.10 in -security at 2024-07-01 09:16:24 UTC. SRU-only revisions exist: jammy openssh 0.4 and 0.7; noble 13.5, 13.7, 13.9 and 13.12–13.14; php8.1 2.3–2.6, 2.9 and 2.15. The api.launchpad.net endpoint is proxy-blocked from this sandbox but the web pages work.
- OpenSSH banner exposes the Ubuntu/Debian package revision https://github.com/RUB-NDS/Terrapin-Scanner — VERIFIED via GitHub code. RUB-NDS/Terrapin-Scanner README shows 'SSH-2.0-OpenSSH_8.9p1 Ubuntu-3ubuntu0.5' with SupportsStrictKex=true, which is the basis for the KEX consistency check. The fakessh repo shows static fake banners, which is why the honeypot filter is needed.
- PHP X-Powered-By header exposes the Ubuntu revision https://github.com/BUseclab/cve-genie — VERIFIED via GitHub code (e.g. 'X-Powered-By: PHP/8.1.2-1ubuntu2.22', 115 code hits).
- unattended-upgrades default Allowed-Origins (-security and ESM on, -updates commented out) https://github.com/linode/docs — VERIFIED via documentation repos (linode/docs and others showing the default 50unattended-upgrades). The Debian/Ubuntu package source itself was not fetched. The Debian defaults (point-release origin) are still to be verified.
- Censys BigQuery research datasets (research_1w / research_1m universal_internet_dataset) https://github.com/InetIntel/ioda-censys-isi — Dataset existence VERIFIED via the InetIntel/ioda-censys-isi notebook (snapshot_20221206 research_1w, snapshot_20220419 research_1m). Access terms and cadence guarantees NOT checked because the censys.com domains are blocked. NEEDS AGREEMENT (academic co-lead). Daily cadence probably needs a commercial licence.
- Censys host schema: ssh.server_host_key.fingerprint_sha256 and KEXINIT algorithm lists https://github.com/censys/censys-sdk-python — VERIFIED via censys/censys-sdk-python models/ssh.py, the MISP censys_enrich module, and the Sentinel censys table documentation (ssh_kex_init_message_* fields).
- OpenINTEL public DNS data (bucket openintel-public at object.openintel.nl, fdns basis=zonefile|toplist) https://github.com/CAIDA/nids-dns-ecosystem — VERIFIED via third-party code and documentation (CAIDA/nids-dns-ecosystem, InternetHealthReport/internet-yellow-pages, r13i/dodomains research note: about 307 ccTLDs, CC BY-NC-SA 4.0, no commercial licence offered). openintel.nl is proxy-blocked. gTLD (.com/.net/.org) coverage NEEDS AGREEMENT.
- Stanford ASdb (AS industry categories incl. health care, hosting) https://asdb.stanford.edu/ — VERIFIED to exist via the IYP crawler code (monthly CSV asdb.stanford.edu/static-website/data/YYYY-MM_categorized_ases.csv). Site blocked here, so terms are unverified.
- CAIDA AS2Org (as-org2info) https://publicdata.caida.org/datasets/as-organizations/ — Existence VERIFIED via 56 GitHub code references to publicdata.caida.org. The CAIDA site is blocked, so the acceptable-use terms (research vs commercial) are UNVERIFIED.
- ICANN CZDS gTLD zone files https://czds.icann.org/ — NOT VERIFIED (czds.icann.org blocked). Known from memory: per-TLD application with no redistribution, and NS/glue records only (no MX/A/CNAME fan-in). NEEDS AGREEMENT.
- Certificate Transparency (crt.sh) / Censys certificates https://crt.sh/ — crt.sh BLOCKED here, so UNVERIFIED. Fallback: certificate fields inside the Censys dataset.
- Tranco top list https://tranco-list.eu/ — BLOCKED here, so UNVERIFIED directly. OpenINTEL's toplist source=tranco partition is referenced in wangmm001/openintel-dns-analysis.
- CISA KEV catalog, FIRST EPSS https://www.cisa.gov/known-exploited-vulnerabilities-catalog — BLOCKED here, so UNVERIFIED in session. Both are known public feeds.
- Shadowserver daily scan data (daily-cadence alternative) https://www.shadowserver.org/ — BLOCKED here, so UNVERIFIED. NEEDS AGREEMENT (research or CERT data-sharing partnership).
- Shodan historical data (commercial fallback) https://www.shodan.io/ — BLOCKED here, so UNVERIFIED. Commercial licence.
- Rapid7 Project Sonar SSH history https://opendata.rapid7.com/ — BLOCKED here, so UNVERIFIED. From memory, access has been restricted to vetted researchers since 2022.
- Debian security tracker / snapshot.debian.org (DSA timing, Debian banners) https://security-tracker.debian.org/ — BLOCKED here, so UNVERIFIED. Needed for the Debian arm in the full version.
- OSF pre-registration https://osf.io/ — BLOCKED here, so UNVERIFIED. AsPredicted is an alternative.
- Validation partner (MSP/RMM ring configs; hospital or med-device network)  — NOT FOUND / NEEDS AGREEMENT. A data-sharing agreement for technical data only (no interviews).

### The Proof Bill: a pre-registered public ledger of manufacturers' "safe to install" verdicts on Microsoft security fixes (finalist X5, rebuilt with the skeptic's fixes)

**One line:** Collect every dated, public "validated / safe to install" verdict that medical-device and industrial-control manufacturers publish for Microsoft security updates. From those verdicts, measure three things: how many days the only approved configuration stays vulnerable to a CISA-listed exploited flaw, how often the proof finds no problem, and whether the proof clock reacts to breakage signals (impact uncertainty) or runs on a fixed calendar (compliance cadence). The design is built so that the second answer, if true, falsifies belief 2.

**Hypotheses:**
- SCOPE (pre-registered): the confirmatory tests cover only the manufacturer's proof clock in regulated fleets. No claim about organisations in general, or about site-side delay, is made unless the partner arm (H8) lands. Unit of analysis is a spell: vendor x product x OS build x Microsoft KB, running from Microsoft release to the first dated verdict. Spells can end in a verdict, be superseded (the vendor skips the KB and validates the next cumulative update), or be censored.
- E1 (primary estimand, always reported): median approved-vulnerable days (AVD) per product x KEV-listed Windows CVE. AVD runs from Microsoft's fix release to the first date the product has an approved configuration containing the fix. Because updates are cumulative, a later approved update counts. CIs come from a vendor-clustered bootstrap.
- E2 (primary estimand): no-problem share = compatible / (compatible + compatible-with-exception + issue-found + do-not-install). 'Not applicable' and 'pending' are excluded. Products under a blanket 'install unless told otherwise' policy are reported separately, not counted as lag 0.
- E3 (primary estimand, board metric): share of product x KEV-CVE pairs where the manufacturer's approval arrived after the KEV dueDate (the federal remediation deadline).
- E4 (estimand): retraction rate = verdicts reversed, downgraded, or given a new exception within 60 days of issue.
- H1 Breakage-signal response (the confirmatory test that belief 2 lives or dies on). Within a spell, a Microsoft known issue opening whose scope covers the product's documented OS SKU and role slows the verdict hazard: hazard ratio (HR) <= 0.75 with 95% CI upper bound < 1. Model: Cox with time-varying covariates, stratified by vendor x product, KB-month frailty. Irrelevant-scope known issues are also estimated. If irrelevant issues delay almost as much as relevant ones, that means 'cannot prove it does not apply' (a discrimination failure). If they have no effect, vendors discriminate well.
- H2 Urgency elasticity (within-spell, replacing the broken cross-KB comparison): a CVE added to KEV during an open spell. Belief 2 as a hard bottleneck predicts HR <= 1.5. HR >= 2 together with retractions rising >= 3 percentage points means a real speed-vs-safety tradeoff. HR >= 2 with no retraction rise means routine lag was prioritisation.
- H3 Cadence falsifier: if proof is uncertainty resolution, verdict timing depends on content and signals. If it is compliance ritual, verdicts bunch at a fixed offset from Patch Tuesday, or at the MDS2-stated service level, regardless of content.
- H4 Content dependence: the lag differs by update family (OS cumulative update vs .NET vs SQL Server vs Office/Edge) and grows with the number of fixed CVEs in components the product actually uses. Belief 2 predicts families released the same month are not validated as one same-day batch.
- H5 Workload vs breakage: breakage signals (H1 covariates) explain more of the lag variation than capacity proxies do (KB count that month, vendor holiday windows, concurrent out-of-band releases, number of products the vendor validates).
- H6 (secondary) Stated vs realised: realised lag compared with each product's MDS2-stated validation cycle, reporting the share of verdicts beyond the stated service level and whether verdicts bunch exactly at it.
- H7 (secondary, run only if >= 30 issue-found training events and >= 10 test events): 'issue found' is predictable from public features on a time-split holdout. The pre-registered bar is PR-AUC >= 2x base rate and above a 'Microsoft known issue exists' baseline, and the model must be calibrated.
- H8 (full version; required before any claim that belief 2 holds for organisations): in partner fleets, vendor proof lag is at least 50% of total exposure time (fix release to install) at the median.

**Pass/fail:** Everything below is registered on OSF before confirmatory extraction. Only the week-1 feasibility inventory, which records existence and date format but no lag values, precedes it. The 2019-2020 data of one vendor is set aside as a calibration set for the parser and excluded from confirmatory tests. Holm correction is applied across H1, H2, H3 and H5.

SUPPORT for belief 2 (sector-level, manufacturer proof clock only). Requires all three:
(a) H1 passes: relevant known-issue HR <= 0.75, CI upper < 1.
(b) H3 does not falsify.
(c) H2 is not 'prioritisation'.

FALSIFICATION of belief 2 for this sector. Any one is enough:
(1) Cadence (H3): for vendors covering >= 50% of verdicts, >= 70% of each vendor's verdicts fall within +/-2 days of its modal offset from Patch Tuesday, or of its MDS2-stated service level. Adding content and signal covariates to a calendar-only model does not improve fit (likelihood-ratio p > 0.05).
(2) Prioritisation (H2): mid-spell KEV addition HR >= 2.0, and the retraction-rate difference versus non-urgent spells has a 95% CI upper bound below 3 percentage points.
(3) Deaf to breakage (H1): relevant known-issue HR point estimate >= 0.9 with CI including 1.
(4) Capacity (H5): workload covariates add more C-index than breakage covariates, and the difference is >= 0.02.

INCONCLUSIVE: anything else, reported as such, with minimum detectable effects stated.

VERDICT CONTENT (E2):
- E2 < 90% (issue-found >= 10%) falsifies the 'safe but unproven' framing: real incompatibilities are common, so fix cost matters.
- E2 >= 95% is consistent with belief 2 only in combination with H1. On its own it is equally consistent with 'the ritual always passes'. This caveat is pre-registered and stated in the headline.
- 90-95% is ambiguous.

URGENCY-TRADEOFF reading (H2): HR >= 2 with a retraction rise >= 3 percentage points (one-sided p < 0.05) means compressed proof costs safety. This supports the premise that proof, not effort, is binding.

PARTNER ARM (H8, full version only):
- Supports if the median proof-lag share of total exposure is >= 50%.
- Falsifies for operators if <= 30%, with post-proof delay dominated by asset-discovery gaps, maintenance-window waits or change-board waits. This is the Dissanayake/Equifax rival winning.
- 30-50% is mixed.

KILL GATE (end of week 1): fewer than 3 vendors with >= 3 years of per-KB dated verdict history. Dated means in-document dates or revision stamps, or Wayback captures at <= 7-day resolution. If the gate fails, stop the ledger and switch to the fallback: written data-access requests to vendors, plus a one-time MDS2 stated-cycle census. No headline number is published from fewer than 3 vendors.

POWER NOTE (from verified KEV data): 83 of 140 Microsoft KEV entries with CVE year >= 2022 were added on a Patch Tuesday. The other 57 were added a median 10 days after the latest Patch Tuesday (IQR 6-17), which falls inside typical validation windows. After the MSRC join, expect roughly 30-45 KB-months with a genuine mid-spell urgency shock. The minimum detectable HR is computed from gate data and published in the pre-registration. If it exceeds 2.0, H2 is demoted to secondary before any outcome is seen.

**Data pipeline:** NOTE: this sandbox's egress proxy blocks every vendor, Microsoft, FDA and Archive domain. Collection must run from a normal network, as an ordinary visitor.

1) Source inventory and ToS log (week 1). For each candidate list, record: URL, robots.txt, terms-of-service clause on automated access, date format (per-KB 'validated on' date, revision table, or current-state only), earliest entry, and Wayback CDX capture density (captures per month). The skeptic's point 4 is enforced here. Candidates:
- medical: Hologic Validated Patches (existence confirmed), Philips, GE HealthCare, Siemens Healthineers, BD, Elekta, Canon, Fujifilm, Carestream.
- DCS/OT: Siemens SIMATIC PCS 7/WinCC compatibility entries, ABB 800xA, Yokogawa CENTUM, Schneider, AVEVA, Valmet.
- GxP lab software: Agilent OpenLab, Waters Empower, Thermo Chromeleon (unverified; added because they share the same regulated-validation mechanism).
- Gated: Rockwell, Emerson, Honeywell, Varian go only through written research-access requests.
The vendor-selection rule is pre-registered: include every vendor that passes the gate.

2) Retrieval. Polite crawler (identifying user agent with contact email, <= 1 request per 10 s, robots honoured) for pages whose ToS permit it. Manual browser download where ToS are silent or restrictive. Wayback CDX plus snapshot fetches for history. Every raw file is stored with its SHA-256 and capture time in a private evidence store (never in a git repo).

3) Extraction into the ledger. Schema per row:
- vendor_id (anonymised letter), product, product_version, os_sku/build, update_family (OS CU / SSU / .NET / SQL / Office / Edge / Defender / out-of-band), KB
- verdict: compatible / compatible-with-exception / issue-found / do-not-install / not-applicable / pending / blanket-policy
- verdict_date plus date_source (in-document / revision stamp / first Wayback capture) and date_resolution_days
- revision events: retraction, exception added, reversal
LLM-assisted extraction. Double human coding of a stratified 10% sample. Acceptance: Cohen's kappa >= 0.8 on verdict, and exact agreement >= 0.9 on date.

4) Joins.
- MSRC CVRF API (/updates, /cvrf/{yyyy-Mmm}): CVE-to-KB-to-OS-build map, release date, 'Exploited: Yes' flag, out-of-band flag.
- CISA KEV (cisagov/kev-data): dateAdded (mid-spell urgency timing), dueDate (E3), knownRansomwareCampaignUse.
- Microsoft known issues: Windows release health pages and KB 'Known issues' sections via Wayback history; the Graph windowsUpdates knownIssue API in a partner tenant gives startDateTime, resolvedDateTime, and originating/resolving KB. Each issue is coded for scope against the product profile (OS SKU, domain-joined, roles such as SMB/Kerberos/print/RDP/Secure Boot/BitLocker, drawn from MDS2 and product manuals). Two coders; kappa reported.
- MDS2 forms (2019 'CSUP' Cyber Security Product Upgrades section) for the stated validation cycle and whether third-party updates need approval.
- Workload covariates: KB count per month, vendor-HQ holidays, concurrent out-of-band releases.
- openFDA device recall root_cause_description: exploratory only.

5) Spell construction. Time-varying covariate episodes are split at each KEV addition and each known-issue open or resolve date. Supersession (the vendor skips a KB) is a competing risk.

6) Analysis:
- Cox with time-varying covariates, stratified by vendor x product, KB-month frailty; Fine-Gray sensitivity for supersession.
- Bunching estimator and calendar-only vs full-model likelihood-ratio test.
- Update-family same-day batching share.
- MDS2 stated vs realised.
- Vendor-clustered bootstrap for E1-E4.
- Time-split PR-AUC only if the event threshold is met.

7) Outputs. Aggregate tables, anonymised vendor letters, code and data dictionary. The full replication package, which includes URLs and so reveals vendors, goes to credentialed researchers on request.

8) Partner arm (full version). Under a data-use agreement, obtain the design partner's device-validation logs plus install timestamps (Intune/ConfigMgr, or Windows Update for Business reports) and asset inventory. Decompose exposure into four parts: proof lag; asset-not-in-inventory time; maintenance-window wait; change-board wait. Optionally add aggregated OS patch-level telemetry from an asset-visibility vendor (Claroty, Armis, Asimily, Ordr) under a data-use agreement.

**6-week MVP:** Staff: 1 analyst, plus a statistician at about 0.2 FTE, plus a second coder for about 20 hours. Budget $4-8k (LLM extraction about $0.5k, coders $2-3k, statistician $2-4k). Collection runs from a normal network, not this sandbox.

WEEK 1: feasibility gate, no outcome values recorded.
- Inventory 12-15 candidate vendor lists (Hologic first, since its existence is confirmed). Log robots.txt and ToS, date format, earliest entry and Wayback density.
- Pull MDS2 forms for every candidate product.
- Download MSRC CVRF for 2019-2026 and KEV (already verified).
- Gate: >= 3 vendors with >= 3 years of dated per-KB history. If it fails, the fallback deliverable is (a) data-access request letters to 10 vendors, and (b) an MDS2 stated-validation-cycle census across all products found. Stop the ledger.

WEEK 2: pre-registration.
- Write and freeze the OSF pre-registration: estimands E1-E4, tests H1-H5 with thresholds, vendor-selection rule, known-issue relevance codebook, power/MDE computed from gate counts, and the rule that demotes H2 if MDE HR > 2.
- Build the parser on the calibration set (one vendor, 2019-2020, excluded from confirmatory analysis).
- Retrieve raw documents and Wayback snapshots for the gated-in vendors.

WEEK 3: extraction.
- LLM extraction into the ledger.
- Double-code a stratified 10% sample; kappa >= 0.8 on verdict or the codebook is revised and re-coded.
- Build the known-issue table (Wayback of release-health pages and KB articles). Two coders code scope vs product profiles.

WEEK 4: joins and spells.
- Join CVE-KB-KEV, construct spells, split time-varying episodes at KEV and known-issue dates.
- Compute E1-E4 with vendor-clustered bootstrap.

WEEK 5: confirmatory models.
- H1, H2, H3 and H5 exactly as registered. H4 update-family split and H6 MDS2 stated-vs-realised as secondary.
- H7 only if the event threshold is met; otherwise report 'not testable, n = X'.
- Robustness: date-resolution sensitivity (drop Wayback-dated spells whose resolution is > 3 days); blanket-policy products excluded vs included.

WEEK 6: write-up and vendor preview.
- 8-10 page technical note with a one-chart headline (AVD distribution for KEV CVEs, with the KEV dueDate line) and the pre-registered decision table (support / falsify / inconclusive), including whichever headline the data yields.
- Send each vendor its own figures privately with a 14-day reply window, so public release is week 8.
- Deliverables: private ledger, public aggregate tables, code, codebook, OSF link.

What the MVP can honestly claim: the price and behaviour of the manufacturer's proof clock. It cannot claim that belief 2 holds for organisations.

**Full version:** Timeline 9-18 months. Budget $40-120k plus partner time. Four arms.

(1) Ledger at scale:
- Every public vendor list that passes the gate, across medical devices, DCS/OT, GxP lab software (Agilent OpenLab, Waters Empower, Thermo Chromeleon, pending verification) and building automation.
- Written research-access agreements for gated portals (Rockwell, Emerson, Honeywell, Varian) that permit aggregate publication.
- Monthly refresh as a public 'Proof Clock' tracker (anonymised aggregates), scored against the P5 'Patch Weather' forecast.
- Target: >= 10 vendors, >= 150 products, 2016-2027.

(2) Partner arm, required before any claim about belief 2 for operators:
- The FDA-regulated design partner's fleet: its own device-validation logs (it is itself a manufacturer), plus install timestamps from Intune/ConfigMgr or Windows Update for Business reports, plus asset inventory.
- 2-4 operator sites (hospital or plant), or one asset-visibility vendor's aggregated telemetry, under data-use agreements.
- Decompose exposure for each product-CVE into: vendor proof lag, asset-not-inventoried time, maintenance-window wait, and change-board wait. H8 decides whether proof or site-side coordination dominates, which directly tests the Dissanayake and Equifax rivals.

(3) Blast-radius predictability:
- With multi-vendor 'issue found' and retraction events (target >= 50), train on public features: Windows components changed, known-issue text, product OS SKU and roles, prior verdict history.
- Evaluate PR-AUC and calibration on a time-split holdout against the Microsoft known-issue baseline.
- This is the first public benchmark for 'will this fix break this product'. Skylayer's own predictor is scored on it, openly.

(4) Blanket-pre-authorisation contrast:
- Some products let customers install Microsoft updates without manufacturer approval. Compare, for the same KBs, their later 'do not install' notices with the issue-found rate on validate-first products.
- This measures how much information the waiting actually buys.

Demoted to exploratory appendix, per the skeptic:
- the FDA software-change recall event study (non-software recall placebo);
- the IaC/SSM 'approve_after_days' mirror arm.

Outputs: peer-reviewed paper (USENIX Security / IEEE S&P / CSCW, or a medical-informatics venue), the public tracker, the benchmark dataset, and a regulator-facing brief that maps AVD against NERC CIP-007 R2 and FD&C 524B clocks.

**Headline if true:** We read N dated 'safe to install' verdicts that K medical and industrial manufacturers issued on Microsoft security updates since 2019.
- For flaws CISA lists as exploited in the wild, the only configuration the manufacturer had approved stayed vulnerable for a median of W days, and in P% of cases approval came after CISA's own federal patch deadline.
- Q% of verdicts (not-applicable excluded) said 'no problem found'.
- When CISA flagged a flaw as exploited mid-validation, proof didn't speed up (hazard ratio ~H, not significant).
- When Microsoft posted a breakage notice that could touch the product, proof slowed by D days, and it ran on content and warnings, not the calendar.
In regulated fleets the patch is ready long before anyone can prove it is safe to install.

**Headline if false:** Proof isn't the bottleneck, even in the most regulated fleets. Across N verdicts from K medical and industrial manufacturers:
- X% of approvals landed on a fixed calendar day regardless of what the update changed, and Microsoft breakage warnings did not move them.
- When CISA flagged active exploitation, validation ran H times faster with no rise in retractions.
- In partner fleets, the manufacturer's proof was only S% of total exposure time. The rest was site-side: assets not in inventory, maintenance windows, change boards.
Delay here is cadence and coordination, not uncertainty about breakage.

**Legal checklist:** 1. Public pages only, fetched as a normal visitor. Before any retrieval, log robots.txt and the terms-of-service clause for each domain. Automated fetching only where ToS permit, with an identifying user agent and contact email, <= 1 request per 10 s. Otherwise download manually or send a written data request. No login-gated content, no shared or borrowed credentials. Gated portals only under written research access that permits aggregate publication.
2. Wayback Machine through the CDX API within Internet Archive terms and rate limits. Use MSRC CVRF, KEV (CC0; via cisagov GitHub) and openFDA through their public terms.
3. Copyright: extract facts (KB numbers, dates, verdicts); never republish vendor documents verbatim. Raw captures stay in a private evidence store, never in a public repo.
4. No scanning, probing, fingerprinting or exploitation of any system. No exploit details. Name no hospitals, utilities, plants or sites. No product-level exposure tables in public outputs.
5. Vendor fairness: publish anonymised vendor letters (A-K) and sector aggregates. The vendor-selection rule is pre-registered. Each vendor gets its own figures privately with a 14-day right of reply before publication. Name a vendor only with its consent (e.g., the fastest ones). The replication package, which reveals URLs, goes only to credentialed researchers on request.
6. Framing: a systemic proof bottleneck, not negligence. State explicitly that operators must not skip manufacturer validation. Include FDA's position that routine cybersecurity patches generally do not need new clearance, so no reader infers a regulatory violation.
7. Technical evidence only. Vendor data-access requests are procedural correspondence, and none of their content is used as evidence. No interviews or surveys. No human subjects, so no IRB is expected; confirm with an institutional reviewer if publishing academically.
8. Partner arm: a written data-use agreement covering the partner's own data only. Asset and patch metadata only: no patient data or PHI (confirm with the partner's privacy officer that no BAA is triggered). Aggregate reporting, partner anonymised unless it opts in. The same applies to any asset-visibility vendor data partnership.
9. Pre-register on OSF before confirmatory extraction. Publish all pre-registered results, including falsifying ones.
10. Defamation/antitrust hygiene: state only facts reproducible from the vendor's own publications, with capture timestamps. No price or commercial comparisons between vendors.

**Biggest risks:** 1. Data existence and history (highest). Only Hologic's validated-patch page is confirmed to exist, and only through a third-party probe. Every other vendor list, plus Wayback and the Microsoft pages, was blocked or unverified this session. Many lists may show current state only. Mitigation: the week-1 kill gate and the written data-request fallback.

2. The ritual interpretation. For FDA- and IEC 62443-bound makers, validation is mandatory whatever the uncertainty, so a high no-problem share is also consistent with 'the ritual always passes'. Mitigation: H1 (does the clock react to relevant breakage warnings?) and the H3 cadence falsifier. The result may well be 'cadence', which falsifies belief 2 for this sector and must be published.

3. Power. The mid-spell urgency shocks are few: about 57 Microsoft KEV CVEs since 2022 were added off Patch Tuesday, clustering into perhaps 30-45 KB-months. Relevant known issues per product role are rarer still. Mitigation: MDE computed at the gate, pre-registered demotion, pooling across vendors with KB-month frailty.

4. Proof lag may be small next to site delay. Vendor proof likely takes 1-5 weeks, while site exposure can run months or years (unsupported operating systems, unknown assets). Without the partner arm the study cannot say proof is THE bottleneck. The headline is therefore restricted to AVD, E3 and the no-problem share. H8 is required before any organisation-level claim, and its data rest on an n=1-4 partner arm that is not yet signed.

5. Measurement. Posting date is not the date validation finished. Wayback resolution can be similar in size to the effect. 'Not applicable' and blanket policies distort shares. Supersession (skipped KBs) needs competing-risk handling. Mitigations: in-document dates preferred, date-resolution sensitivity, exclusions pre-registered.

6. Selection bias. Public, well-archived vendors are likely the faster ones, and the large gated OT vendors are missing. Report lag as a lower bound, and seek gated access in the full version.

7. Weaker virality. Anonymisation and expected medians of 1-4 weeks give less punch than the MCP-server post. OT and medical practitioners already 'know' OEM approval takes weeks. The novel parts are the per-KB verdict ledger, AVD beyond the KEV deadline, and the reacts-to-signals-or-calendar test.

8. Strategic mismatch. Even a perfect blast-radius predictor cannot legally replace regulated verification and validation. For Skylayer the value is (a) a benchmark and training set for 'will it break', (b) speeding up and targeting the manufacturer's proof, and (c) the post-proof site lag measured in the partner arm. Autonomous action on validated devices remains the hardest sale.

9. Vendor relations and legal pushback. Mitigated by the right of reply, anonymisation and factual framing.

**Why it cuts the noise:** Most security-industry claims about why patching is slow are surveys, vendor telemetry with undisclosed methods, or opinion. This study uses the one place in the industry where 'proof that a change is safe' is a formal, dated, public artifact: the manufacturer's regulated verdict on a Microsoft fix. Joined to CISA's exploited list, it gives a number a board can grasp and anyone can reproduce: the days during which the only approved configuration is one CISA says is being exploited, and how often approval lands after CISA's own deadline. It sets that against the fact that most proofs apparently come back 'no problem'.

It is also built to be able to say no. The cadence falsifier, the within-spell urgency test with a retraction check, and the partner decomposition all have pre-registered thresholds under which belief 2 fails. A published result against the author's own thesis is rare enough in security marketing to be credible, and either way it replaces anecdote with a public ledger other researchers can extend.

The KEV data verified here show why the redesign was needed: 48 of 57 Patch Tuesdays since 2022 carried a Microsoft exploited-in-the-wild addition within a week, so 'urgent vs routine' at the update level is meaningless. The within-spell timing of KEV additions and breakage warnings is the honest test.

**Sources:**
- CISA Known Exploited Vulnerabilities catalog (GitHub mirror cisagov/kev-data) https://raw.githubusercontent.com/cisagov/kev-data/main/known_exploited_vulnerabilities.json — VERIFIED this session: downloaded catalog version 2026.09.25, 1,726 entries. Fields include dateAdded, dueDate, knownRansomwareCampaignUse. 389 Microsoft entries (177 with 'Windows' in the product name). Computed: 48 of 57 Patch Tuesdays from Jan 2022 to Sep 2026 had >= 1 Microsoft KEV addition within 7 days, which confirms that a cross-KB 'exploited at release' flag is nearly constant. 57 of 140 Microsoft KEV entries with CVE year >= 2022 were added off Patch Tuesday (median 10 days after it), which gives the within-spell urgency shocks. cisa.gov itself is blocked by the proxy.
- Microsoft Security Updates API (MSRC CVRF) https://raw.githubusercontent.com/microsoft/MSRC-Microsoft-Security-Updates-API/main/docs/swagger.json — VERIFIED (spec only): the OpenAPI definition in microsoft/MSRC-Microsoft-Security-Updates-API documents the /updates and /cvrf/{id} endpoints ('MSRC CVRF API'). The live endpoint api.msrc.microsoft.com is blocked by this session's proxy. It is a public API; month-1 check needed from a normal network.
- openFDA device recall: root_cause_description (FDA Determined Cause) https://raw.githubusercontent.com/FDA/openfda/master/schemas/devicerecall_schema.json — VERIFIED (schema): the field is present in FDA/openfda schemas/devicerecall_schema.json and pipeline.py. Public notebooks list the values Software Change Control, Software Design Change, Software Manufacturing/Software Deployment and Software In The Use Environment. api.fda.gov is blocked by the proxy. Demoted to exploratory, per the skeptic.
- Microsoft Graph windowsUpdates knownIssue resource (beta) https://raw.githubusercontent.com/microsoftgraph/microsoft-graph-docs-contrib/main/api-reference/beta/resources/windowsupdates-knownissue.md — VERIFIED (docs), NEEDS AGREEMENT: the resource provides startDateTime, resolvedDateTime, status, knownIssueHistories, originating/resolving KnowledgeBaseArticle and safeguardHoldIds (doc dated 2026-01-27, Windows Autopatch subservice). It needs a licensed Entra tenant, so it is accessible through the partner's tenant, not anonymously.
- Windows release health known-issues pages (public, learn.microsoft.com) and their Wayback history https://learn.microsoft.com/en-us/windows/release-health/ — BLOCKED this session (learn.microsoft.com and web.archive.org are egress-blocked). Not verified; week-1 check needed.
- Hologic Validated Patches page (per-product validated Microsoft monthly patches) https://www.hologic.com/support/usa/Breast-Skeletal-Products-Cybersecurity/Validated-Patches — VERIFIED EXISTS (secondary): a third-party probe dated 2026-09-13 recorded HTTP 200 and described it as 'Validated Microsoft monthly critical patch releases, published per product'. Format and history depth are unverified because hologic.com is blocked here. First gate candidate.
- Hologic per-product MDS2 forms page https://raw.githubusercontent.com/api-evangelist/hologic/main/lifecycle/hologic-lifecycle.yml — VERIFIED EXISTS (secondary, same 2026-09-13 probe; api-evangelist/hologic lifecycle and security YAML)
- BD Cybersecurity Trust Center, 'Bulletins and Patches' tab https://www.bd.com/en-us/about-bd/cybersecurity?active-tab=3 — VERIFIED EXISTS (secondary mirror generated 2026-07-11). Whether it contains per-KB Microsoft validation is unverified.
- MDS2 (2019) form, CSUP 'Cyber Security Product Upgrades' section https://github.com/LM-Tech-Solutions/parseMDS2 — PARTLY VERIFIED: the section exists (the open-source parser LM-Tech-Solutions/parseMDS2 builds a 'CYBER SECURITY PRODUCT UPGRADES' section from CSUP- questions). The wording of the questions on third-party patch approval and review cycle was not verified this session.
- Siemens SIMATIC PCS 7 / WinCC compatibility of Microsoft security updates (SIOS) https://support.industry.siemens.com — BLOCKED (support.industry.siemens.com is egress-blocked); no GitHub mirror found. Unverified.
- ABB 800xA third-party security update validation status  — NOT FOUND this session (vendor domain blocked; GitHub code search returned 0 mirrors). Unverified.
- Yokogawa CENTUM, Philips, GE HealthCare, Siemens Healthineers, Elekta Microsoft patch validation lists  — BLOCKED / UNVERIFIED: vendor domains blocked. api-evangelist mirrors exist for Philips, Siemens Healthineers and Siemens disclosure programs but do not document patch-validation lists.
- Rockwell (TechConnect), Emerson (Guardian), Honeywell, Varian (MyVarian) patch qualification  — NEEDS AGREEMENT: login-gated according to prior rounds (not re-verified). Excluded unless written research access permits aggregate publication.
- Internet Archive Wayback CDX API https://web.archive.org/cdx/search/cdx — BLOCKED this session (web.archive.org is egress-blocked). Capture density per vendor URL is a week-1 gate item.
- Partner arm: design partner's device-validation logs, install timestamps (Intune/ConfigMgr/Windows Update for Business reports), and asset inventory  — NEEDS AGREEMENT (written data-use agreement, aggregate-only, no patient data)
- Aggregated medical/OT patch-level telemetry (asset-visibility vendors such as Claroty, Armis, Asimily, Ordr)  — NEEDS AGREEMENT (data partnership). Unverified whether any will share.
- Regulatory clocks: NERC CIP-007-6 R2 (35-day patch evaluation/apply-or-mitigate); FD&C Act 524B (patches 'as soon as possible out of cycle' for critical vulnerabilities)  — NOT RE-VERIFIED this session (web search budget exhausted at 200/200); cited from prior knowledge. Confirm the text before publication.

### Twin Servers v2: the Proof Gap (same org, same OpenSSH fix, staging vs production, plus a fix-risk dose test and a same-host selective-hold test)

**One line:** Using only historical internet scan data, compare when the same company installs the same OpenSSH security fix on its production server and on that server's staging twin. Measure how many days longer production waits, whether the wait grows when the fix is riskier (the uncertainty test the first version lacked), and what share of real exposure this gap explains compared with servers nobody touches at all.

**Hypotheses:**
- H1 Material proof gap (confirmatory; primary sample is manual-manual twin pairs, both upgraded in place, pooled across 8 or more OpenSSH security revisions from 2023 to 2026). Production installs the fix a median of 7 or more days after its own staging twin. P(staging first) is reported only as a descriptive number, per the skeptic's fix (b), and is not used as a falsifier.
- H2 Dominance (confirmatory; computed on the FULL population of Ubuntu/Debian-banner SSH hosts, not only twins, per fix (c)). The proof tax is the number of vulnerable production server-days attributable to production waiting behind staging. It must be at least 25% of production vulnerable-days among hosts that do patch. Its population-scaled total must also exceed the server-days on hosts that were never patched within 180 days. The never-patched group is split in advance into 'attended' hosts (persistent web-layer changes, i.e. deploys, while OpenSSH stays frozen) and 'abandoned' hosts (no change at all). The abandoned group is the unknown-asset rival.
- H3 Uncertainty moves the gate: the key causal test, per fix (a). It varies uncertainty while holding the stakes fixed. Before any outcome is seen, two raters score each revision blind for server-side change risk (behaviour or default changes such as Terrapin strict-KEX or the CVE-2025-32728 forwarding semantics, and patch size touching sshd) and separately for severity (CVSS, KEV status, public exploit). In manual-manual pairs, the production-minus-staging gap increases with change risk, holding severity fixed: beta_risk > 0, with a wild-cluster-bootstrap CI by revision that excludes 0. What the rivals predict: fixed governance, CAB or calendar predicts beta_risk ≈ 0, and prioritization predicts that the gap shrinks with severity.
- H4 Selective hold on the same host: a second uncertainty contrast with stakes, owner, effort and change ticket all identical. Consider Ubuntu hosts that expose both the OpenSSH revision (SSH banner) and a distro PHP revision (X-Powered-By header, excluding PPA builds). When OpenSSH moves past a date D, the PHP security revision that was already available at D is left behind at least 15 percentage points more often than the OpenSSH revision itself, and more often on production-labeled hosts than on non-production hosts. On hosts that otherwise auto-update, leaving PHP behind reveals an explicit exclusion from unattended-upgrades. Prioritization predicts the opposite, because PHP is the web-exposed package. Whether the PHP header carries the revision string is unverified; this is checked in week 1, and H4 is dropped if too few hosts show it.
- H5 Soak, not calendar (confirmatory for timing). Regress the production patch time on the staging twin's patch time with revision fixed effects; the slope is at least 0.5 with a CI excluding 0. Also, fewer than 50% of production flips fall into org-level batches (3 or more production hosts in the same org flipping within one observation interval) or into recurring org-specific weekday windows.
- H6 Fear exceeds realized breakage (belief 4, descriptive with a pre-registered claim rule). Among in-place upgrades, the field rollback rate is below 2% at the upper bound of its 95% CI. A rollback is a downgrade below the fixed revision with the SSH host key unchanged, persisting for 2 or more observations, within 30 days. Also reported: in-place vs replacement share (host-key change) and the 'auto on staging, manual in prod' share. Hosts are classified auto vs manual using verified Ubuntu defaults: unattended-upgrades runs daily with a random delay on -security, and -updates is off. So a host that takes an -updates-only OpenSSH revision is doing manual or full apt sweeps.
- Secondary (reported, not decisive):
(S1) Proof availability. Production hosts in orgs with an observable non-production twin are compared with matched production hosts (same ASN type, distro series and org host count) in orgs with none. Belief 2 predicts the no-twin orgs lag more on high-risk revisions. Caveat: staging environments not visible from the internet add noise.
(S2) Governance proxy. Orgs whose CT-logged names show a trust-center hostname (e.g. trust.<domain>), found from names only with no page visits, are compared with orgs that have none. If the gap is concentrated there and is flat across change risk, that points to governance, not uncertainty.
(S3) Urgency responsiveness. The production-minus-staging gap for critical security revisions is compared with the gap for non-security -updates-only OpenSSH SRUs. Equal gaps mean urgency does not move the production gate. This replaces the discarded certificate placebo; it is not claimed to rule out neglect.
(S4) Strata: hosting ASN vs enterprise ASN; Ubuntu vs Debian.
(S5) Prospective holdout: the first OpenSSH security revision published after the OSF registration date is analysed with the frozen code as an out-of-sample replication.

**Pass/fail:** Everything below is registered on OSF before any outcome is extracted. The frozen items are:
- the environment-token lexicon and the pair rules;
- the revision list and change-risk/severity ratings;
- the thresholds and analysis code, debugged only on a held-out pilot revision (CVE-2023-38408, Jul 2023, excluded from the confirmatory set).

GO/NO-GO (week 1, on one current snapshot): at least 300 projected manual-manual in-place pair-events pooled across 6 or more revisions, drawn from at least 100 distinct registered domains. If this fails, stop, or run the descriptive-only fallback (all within-org non-prod/prod pairs with role fixed effects) and label it non-confirmatory.

HEADLINE RULES:
(1) 'Uncertainty about breakage delays production patching' may be claimed only if H1 AND H3 pass. H4 passing strengthens the claim.
(2) If H1 passes but H3 is null, the headline must be 'the cost of the manual production gate / manual proof', not causation. That is fix (i).
(3) The 'fear exceeds breakage' line may be used only if H6's rollback upper CI is below 2%.

BELIEF 2 IS DECLARED FALSIFIED as the dominant cause if ANY of the following holds:
(a) H1 fails: the median manual-manual gap is under 7 days, or production goes first in 50% or more of pairs.
(b) H2 fails: never-patched server-days exceed the proof tax, or the proof tax is under 25% of production vulnerable-days. If most never-patched days are on 'abandoned' hosts, the verdict is 'unknown assets dominate' (the Equifax/Log4j rival).
(c) H3 is negative, i.e. riskier fixes do NOT widen the gap, or its CI is centred on 0 while H5 shows a slope under 0.2 with 50% or more of flips batched or on fixed windows. The verdict is then coordination/governance (Dissanayake).
(d) H4 shows PHP left behind no more often than OpenSSH (only if H4 had enough data).

INCONCLUSIVE, not support: H3 point estimate positive but CI includes 0. With only about 10 to 16 revision clusters, the design detects roughly a doubling of the gap from the lowest to the highest change-risk tercile, not smaller effects.

PRE-REGISTERED SENSITIVITY CHECKS: exclude the 30 days after the CrowdStrike outage (19 Jul 2024) from the regreSSHion production window; strict vs loose lexicon; twins only vs all env pairs; hosting vs enterprise ASN. Vulnerable-days are stated as an upper bound, because LoginGraceTime=0 workarounds are invisible in the banner.

All results are published whichever way they come out; a falsification is a publishable headline too.

**Data pipeline:** 0. REVISION CLOCK (public, free)
- Pull every openssh source publication for focal, jammy, noble and resolute from the Launchpad publishing history. It gives per-series, per-pocket timestamps (security / updates / proposed) and statuses, including Deleted entries with remarks.
- Mark security-pocket revisions: these are the patch clocks.
- Mark updates-only revisions: these are manual-sweep markers, because default unattended-upgrades skips -updates.
- Map each revision to its USN and CVEs, e.g. USN-6560-1 (19 Dec 2023), USN-6859-1 (1 Jul 2024), USN-7270-1 (18 Feb 2025), plus the 2026 publications on 12–13 Mar, 29 Apr, 13 Jul and 3 Sep.
- Add the Debian bookworm DSAs.
- Build a banner-to-revision map, e.g. 'OpenSSH_8.9p1 Ubuntu-3ubuntu0.10' maps to 1:8.9p1-3ubuntu0.10.
- Two raters pre-score change risk from the changelogs and debdiffs, and severity from CVSS/KEV.

1. POPULATION (third-party scan data only; no scanning by us). Two paths:
- Path A (preferred): an academic PI's Censys research access / BigQuery snapshots from 2023-06 to 2026-09.
- Path B: a commercial Censys Platform licence. Its search and aggregate endpoints cover only CURRENT data, so the candidate set comes from current data plus per-IP history via get_host_timeline(start,end) and get_host(at_time). This adds survivorship bias, which must be disclosed.
- NEVER use Live Rescan or tracked scans.
- Select all hosts whose SSH banner carries an Ubuntu- or Debian- revision.

2. NAMES
Per IP and per time window, collect:
- TLS SANs from certificates served on the same IP;
- the PTR record;
- Censys DNS-resolution history (forward DNS to IP over time; needs a Search/Core plan);
- CT-log names.
Then:
- Reduce each name to eTLD+1 with the Public Suffix List, dropping private-section and shared-hosting domains.
- Tag environments with the pre-registered token lexicon (staging, stage, stg, dev, qa, uat, test, preprod, sandbox; exclude demo and canary).
- Strip the token to get the role stem and match it to exactly one production name in the same eTLD+1.
- Require the same distro series and the same pre-fix revision at the USN date, both observed before the USN.
- Two coders audit 300 random names and report precision and kappa.
- Hash the names with a salt held by the PI; raw names are deleted after pairing.

3. TIMELINES
Per IP, record:
- SSH banner revision;
- host-key SHA-256 fingerprint;
- HTTP Server and X-Powered-By headers (PHP revision, for H4);
- body/title/favicon hashes (the deploy signal for attended vs abandoned);
- certificate serials;
- observation timestamps.
Drop IPs whose host key flaps, since those are load balancers or NAT.

4. REGIME CLASSIFICATION, using verified Ubuntu defaults
- Auto: every prior security revision taken within the first observation interval, and -updates-only revisions ignored.
- Manual sweeper: takes -updates-only revisions.
- Frozen.
- Replaced: host-key change.
- Flapping: excluded.

5. EVENTS
- Patch time: interval-censored between the last pre-fix and the first post-fix observation, with the host key unchanged.
- Rollback: a downgrade with the same key, persisting for 2 or more observations.
- Replacement: a key change.
- PHP left-behind indicator.
- Org batches: 3 or more production hosts flipping in the same interval.

6. MODELS
- Interval-censored AFT/Cox (R icenReg, or Python lifelines) with pair fixed effects and SEs clustered by eTLD+1.
- H3: the gap regressed on change risk and severity, with a wild cluster bootstrap by revision.
- H5: the soak slope, plus batch and weekday concentration.
- H2: an exposure-days decomposition on the full population.

7. OUTPUT
- Aggregate tables with at least 10 orgs per cell.
- Code and the revision clock released publicly.
- Raw data stays with the PI under the licence.
- Still-vulnerable IP lists go only to Shadowserver or national CERTs, via the PI, if they accept them.

**6-week MVP:** WEEK 1: LICENCE, CLOCK, GO/NO-GO
- Licence (fixes g and f). Choose Path A: an academic PI owns and publishes under Censys research terms, confirmed in writing, and Skylayer only cites. Or choose Path B: get a written commercial quote whose licence allows publishing aggregates.
- Submit for an IRB exempt determination through the PI.
- Build the revision clock from Launchpad, the USNs and the DSAs.
- Two raters blind-score change risk and severity for every revision.
- Run the go/no-go count on ONE current snapshot: Ubuntu/Debian-banner hosts with names, twin pairs, and projected manual-manual in-place pair-events.
- Check whether Ubuntu PHP revision strings appear in X-Powered-By (H4 feasibility).
- KILL if under 300 pair-events or under 100 orgs.

WEEK 2: FREEZE AND PRE-REGISTER
- Freeze the lexicon, pair rules, revision list, ratings, hypotheses H1–H6, thresholds and the prospective holdout rule.
- Debug the code ONLY on the held-out pilot revision (CVE-2023-38408).
- Post to OSF before touching any confirmatory outcome.

WEEK 3: EXTRACT
- Build per-IP timelines for 2023-06 to 2026-09: banner, host key, headers, hashes, certificates.
- Classify regimes (auto, manual, frozen, replaced, flapping).
- Two coders audit the precision of 300 name labels.
- Hash the names and delete the raw names.

WEEK 4: CONFIRMATORY ANALYSIS
- H1: gap and materiality.
- H2: full-population dominance, with the attended vs abandoned split.
- H3: the change-risk interaction.
- H4: selective hold.
- H5: soak slope and batching.
- H6: rollback, in-place vs replacement.

WEEK 5: ROBUSTNESS AND RED-TEAM
- Exclude the CrowdStrike window.
- Strict vs loose lexicon.
- Ubuntu vs Debian.
- Hosting vs enterprise ASN (fix h).
- All env pairs vs twins.
- The skeptic and the PI try to break the result.
- Hand still-vulnerable aggregates and IP lists to Shadowserver or CERTs via the PI.

WEEK 6: PUBLISH
- The PI posts a preprint.
- Skylayer writes a post that cites it.
- Release the code, the revision clock and the k≥10 aggregate tables.
- State the scope plainly: small, internet-exposed shops, not regulated enterprises.

DELIVERABLES
- The median production proof gap in days.
- The proof-tax share of exposure.
- The risk-dose slope.
- The auto-on-staging/off-in-prod share.
- The selective-hold rate.
- The field rollback rate.
- The attended vs abandoned never-patched split.

COST
- One analyst for 6 weeks, plus the PI part-time.
- Path A data: $0, plus roughly $0.5–3k of compute (unverified).
- Path B: whatever the written quote says.

**Full version:** Timeline: 6 to 12 months, partner-dependent.

1. Longer history and more revisions. Extend to 2019–2026 with Censys BigQuery snapshots, covering all Ubuntu LTS series and Debian oldstable/stable. This gives about 30 revision clusters, which fixes H3's power problem. Replicate on Shodan or Sonar history where a licence allows.

2. More packages visible from outside, to vary change risk within one host. Add every remotely visible Debian/Ubuntu revision string: PHP, plus any others found in banners or headers during week 1. Package-pairs (low-risk vs high-risk package on the same host) then become a second primary test of belief 2, alongside staging vs production.

3. Prospective live run. Pre-register the next 4 OpenSSH security revisions and publish each result about 60 days after release ('Proof Gap Monitor'). This removes any 'you peeked at history' critique and gives a recurring news hook.

4. Enterprise bridge, closing the external-validity hole. Under data agreements, design partners (starting with the FDA-regulated medical-device AI company) export their own dpkg.log, apt history, change tickets and environment tags for staging and production. That is technical artifacts only, with no interviews. The same code then computes their proof gap, risk-dose slope and rollback rate. Validation-regime orgs (CSV/CSA) are compared with others. This also serves as Skylayer's product demo: 'your proof tax is X days.'

5. Fleet telemetry partnership. Seek aggregated, anonymized data on install timing by environment tag from a fleet-management or hosting provider (e.g. an Ubuntu fleet-management vendor or a VPS host). This needs an agreement; availability is unverified.

6. The blast-radius link, which the MVP cannot test. For orgs in (4), check whether a dependency model of the host predicts which upgrades were later rolled back. That is the first data on whether blast radius can be predicted at all.

7. Peer-reviewed paper with the academic PI (IMC, USENIX Security or CSCW), plus the open 'Twin Gap' reproduction kit.

**Headline if true:** Same company, same fix, same command. Across N companies, production servers waited a median of Y days for OpenSSH security fixes that their own staging twins had already installed, Z times longer. The wait roughly doubled when the fix changed behaviour, though urgency barely moved it. The fear was rarely borne out: only R% of servers ever rolled a fix back. And P% of servers that auto-patch OpenSSH were set to leave PHP behind.

**Headline if false:** Depending on which test fails:

- If unknown assets dominate (H1 fails or H2 fails on abandoned hosts): 'Fear isn't the bottleneck, forgetting is. Across N companies, production patched within D days of staging, but P% of all vulnerable server-days sat on servers nobody had touched in 6 months: no deploys, no patches, no owner.'

- If the gap is real but flat across fix risk (H3 null, H5 calendar-dominant): 'Production waits Y days for the change window, not for proof. The gap is the same whether the fix is trivial or risky.' In this case Skylayer's claim becomes 'the manual gate is the cost', not 'uncertainty is the cause'.

**Legal checklist:** DATA RIGHTS
1. Before any design work, get written confirmation from Censys (and any fallback provider) of the permitted use: research vs commercial, the right to publish aggregates, and the sharing of derived tables.
2. On research terms: the academic PI is data controller, analyst of record and first author. Skylayer staff work under the PI and never hold raw data. Skylayer marketing only cites the published paper.
3. Follow Launchpad/Ubuntu and CT/crt.sh usage policies, with rate limits.

NO ACTIVE MEASUREMENT BY US
4. No scanning, probing, logins, Live Rescan or tracked-scan requests.
5. No DNS or HTTP requests to studied hosts. Trust-center signals come from CT names only, with no page visits.
6. Only third-party passive data that hosts broadcast publicly (banners, certificates, headers). No authentication is bypassed, so there is no CFAA or Computer Misuse Act exposure.

PRIVACY (GDPR/UK GDPR: IPs and hostnames can be personal data for individual VPS owners)
7. Legitimate-interest assessment plus a short DPIA.
8. Data minimization.
9. Salted hashing of names right after pairing.
10. Raw data kept 90 days or less.
11. No publication of any IP, domain, org, ASN-level detail or rare-distro cell that could re-identify anyone.
12. k≥10 orgs per published cell.
13. No rankings and no shame lists.

ETHICS
14. IRB exempt determination through the PI, although there are no human subjects.
15. Pre-registration on OSF.
16. Conflict-of-interest statement disclosing Skylayer's commercial interest.

DISCLOSURE
17. Report hosts still vulnerable to regreSSHion or other CVEs only as aggregate counts.
18. Offer IP lists only to Shadowserver or national CERTs, through their existing channels, via the PI. No direct contact with any org.
19. No exploit details or reachability tips.

CLAIMS
20. Headline wording is bound to the pre-registered rules (the H1+H3 gate), for FTC truth-in-advertising and reputational safety.
21. Legal review of the preprint and the Skylayer post before release.

**Biggest risks:** 1. DATA ACCESS
- Censys research terms are unverified (the domain is blocked here), and the legacy v2 API is being deprecated.
- Commercial pricing is unknown.
- A current-data candidate set (Path B) adds survivorship bias.
- Mitigation: settle the licence in week 1, and the PI owns the study.

2. TOO FEW PAIRS
- Mature orgs set DebianBanner=no, put production behind CDNs or bastions, and don't expose SSH.
- Default unattended-upgrades makes many pairs patch within a day on both sides, which shrinks the manual-manual sample.
- Mitigation: a hard go/no-go at 300 pair-events and 100 orgs.

3. GOVERNANCE CANNOT BE FULLY SEPARATED FROM UNCERTAINTY
- CAB, change windows and ownership splits produce the same timestamps.
- Only H3 (the risk dose) and H4 (selective hold) vary uncertainty with the stakes fixed.
- H3 has only about 10–16 revision clusters and detects only large effects. A CAB may itself scrutinize risky changes more, which counts as 'the cost of manual proof' rather than a clean cause.

4. SELECTION AND EXTERNAL VALIDITY
- The sample is small internet-exposed shops, the opposite of the FDA-scale design partner.
- It must be stated plainly. The enterprise bridge (partner dpkg logs) is the fix, and that fix needs agreements.

5. MEASUREMENT
- Scan cadence for port 22 is unverified, so timing is interval-censored and auto/manual classification may degrade.
- Load balancers and cloned host keys can fake rollbacks (flap filter).
- Name-based environment labels are noisy (biased toward the null; audited).
- LoginGraceTime workarounds are invisible, so exposure is an upper bound.
- The CrowdStrike 19 Jul 2024 window contaminates the regreSSHion production window (sensitivity exclusion).
- The PHP header revision string is unverified.

6. READ AS BEST PRACTICE
- 'Prod waits for staging' reads as change management working as designed.
- The answer is the pre-registered materiality threshold, the risk dose, and the low rollback rate (fear exceeds realized breakage).

7. NOVELTY UNCONFIRMED
- Bitsight and SecurityScorecard patching-cadence work uses the same signal.
- The literature could not be searched here and must be re-checked before release.

8. LIKELY OUTCOME
- H2 may well fail, because never-patched long tails usually dominate internet SSH data.
- Budget for publishing a falsification.

**Why it cuts the noise:** Most industry claims about patching come from vendor surveys or aggregate decay curves that cannot say WHY fixes wait. This design uses a real counterfactual inside the same company: the same CVE, the same package bytes, the same apt command, the same no-reboot restart. The only difference is whether a breakage would hurt, and the org has already shown on the twin server that it knows about the fix and can apply it.

Then it adds what the first version lacked: a test where uncertainty varies while the stakes stay fixed. Riskier fixes should widen the gap. And on the same host, the riskier package should be the one left behind. Rival explanations (prioritization, unknown assets, change calendars) predict different patterns, and the study is pre-registered to publish a falsification.

The evidence is the servers' own public broadcasts (SSH banners and host keys) plus Ubuntu's public release clock and Ubuntu's documented auto-update defaults. It needs no interviews, exploits or scans of our own, and anyone with scan-history access can reproduce it with the released code. It yields crisp numbers practitioners can repeat:
- the proof gap in days;
- the proof tax as a share of exposure;
- the share of servers that auto-patch OpenSSH but have PHP excluded;
- the tiny share of fixes ever rolled back.

**Sources:**
- Ubuntu USN-6859-1 (regreSSHion CVE-2024-6387): published 1 Jul 2024; fixed jammy 1:8.9p1-3ubuntu0.10, noble 1:9.6p1-3ubuntu13.3, mantic 1:9.3p1-1ubuntu3.6 https://ubuntu.com/security/notices/USN-6859-1 — verified (fetched)
- Ubuntu USN-6560-1 (Terrapin CVE-2023-48795 + CVE-2023-28531): 19 Dec 2023; jammy 1:8.9p1-3ubuntu0.5, focal 1:8.2p1-4ubuntu0.10 https://ubuntu.com/security/notices/USN-6560-1 — verified (fetched)
- Ubuntu USN-7270-1 (CVE-2025-26465/26466): 18 Feb 2025; jammy 1:8.9p1-3ubuntu0.11, noble 1:9.6p1-3ubuntu13.8, focal 1:8.2p1-4ubuntu0.12 https://ubuntu.com/security/notices/USN-7270-1 — verified (fetched)
- USN-6560-2 and USN-7270-2: these are ESM (Ubuntu Pro) extensions for 16.04/18.04, NOT regression reissues. This means OpenSSH gives no clean Ubuntu 'burn' events, so the burn-history contrast was demoted and replaced by the change-risk interaction (H3). https://ubuntu.com/security/notices/USN-7270-2 — verified (fetched)
- Launchpad openssh publishing history: per-series, per-pocket (security/updates/proposed) timestamps and statuses, including Deleted entries with remarks. It shows 2026 security publications on 12–13 Mar, 29 Apr, 13 Jul and 3 Sep (latest jammy 1:8.9p1-3ubuntu0.17, noble 1:9.6p1-3ubuntu13.19) and updates-only SRUs. Caveat: the summarizer's full-table extraction was inconsistent, so the exact revision list must be pulled programmatically. https://launchpad.net/ubuntu/+source/openssh/+publishinghistory — verified (web page reachable); api.launchpad.net blocked from this sandbox
- Ubuntu Server docs: unattended-upgrades is installed and enabled by default, runs once a day through systemd timers with a random delay, allows the security pocket (and ESM), and leaves -updates commented out. This grounds the auto vs manual classification and the use of -updates-only revisions as manual-sweep markers. https://ubuntu.com/server/docs/how-to/software/automatic-updates/ — verified (fetched)
- Censys Platform SDK (censys-sdk-python): get_host(host_id, at_time), get_host_timeline(host_id, start_time, end_time), DNS-resolution history endpoints that need a Search or Core plan, and Live Rescan at 10 credits (we will not use it). Search and aggregate cover current data only. https://github.com/censys/censys-sdk-python/blob/main/docs/sdks/globaldata/README.md — verified (docs in GitHub repo)
- censys-python v2 (view at_time, view_host_events, view_host_diff, view_host_certificates). The README says the Search v1/v2 APIs 'will be deprecated soon' in favour of the Censys Platform API, so the pipeline must be built on the Platform API. https://github.com/censys/censys-python — verified (fetched); legacy API being deprecated
- Censys research access / BigQuery historical snapshots (eligibility, non-commercial terms, cadence) https://censys.com/ — blocked by proxy (censys.com, search.censys.io); needs agreement; unverified
- Censys commercial historical licence pricing (the earlier $10–30k estimate) https://censys.com/ — blocked; unverified. Get a written quote in week 1; do not assume the figure.
- Debian DSA-5724 / security tracker for CVE-2024-6387 (bookworm 1:9.2p1-2+deb12u3 per the earlier round) https://security-tracker.debian.org/tracker/CVE-2024-6387 — blocked by proxy; unverified
- OpenSSH DebianBanner default 'yes' (the revision appears in the banner) https://manpages.ubuntu.com/manpages/noble/man5/sshd_config.5.html — verified in the earlier round; my re-check returned HTTP 503
- Shodan host history (fallback longitudinal source) https://developer.shodan.io/api — blocked (developer.shodan.io); unverified; needs a paid or academic plan
- Rapid7 Project Sonar / Open Data (fallback) https://opendata.rapid7.com/ — blocked; access believed restricted to vetted researchers; needs agreement; unverified
- Certificate Transparency via crt.sh (extra env-token names; trust-center hostnames for S2) https://crt.sh/ — blocked by proxy; unverified (CT logs are public by design)
- OpenINTEL forward-DNS measurements (alternative name-to-IP history) https://openintel.nl/data/ — blocked by proxy; needs agreement; unverified
- Shadowserver (disclosure channel for still-vulnerable IPs) https://www.shadowserver.org/ — blocked by proxy; unverified
- Ubuntu PHP revision in the X-Powered-By header (e.g. PHP/x.y.z-Nubuntu…), needed for H4  — not verified; check in week 1 from scan data; drop H4 if too few hosts show it
- Closest prior art: Bitsight / SecurityScorecard 'patching cadence' (same banner signal, org unit, no twin contrast); Gasser 2014; Durumeric IMC 2014; Kotzias NDSS 2019; Dissanayake CSCW 2022  — not re-checked (literature sites blocked; search budget exhausted); must be re-checked before publication

## Full scored field

### X1 — Silent Proof vs Noisy Nudge: same fix, same green CI, only the safety evidence changes (a natural experiment that combines C3, P4 and C2, plus a census of bot-merge policies and a revert ground truth) (score 5.03, wounded)

**Best headline:** Ready, green, and still waiting: N bot-written security fixes passed their own tests and still sat unmerged for a median of D days. When a peer 'safe to merge' score silently appeared on the identical fix, merges within 7 days rose from Y% to X%. A notification with no new information moved nothing, and R% of green-CI security merges were reverted within 30 days anyway.

**Skeptic's flaws:** No single flaw is certainly fatal, but several go to the heart of the causal claim.
(1) The treatment varies at the fix level, and the design's own fixed effects absorb it. The badge value depends only on (package, from, to, time), so every PR with the same version pair flips at the same moment. With fix × calendar-day fixed effects, the only variation left comes from different from-versions. That is the same as the size of the version jump and the repo's upgrade diligence: diligent repos sit on popular previous versions, which reach the sample threshold first. So "flipped vs not-yet-flipped PRs for the same fix" compares diligent small-jump repos with laggard big-jump repos. If the backend aggregates only on new-version (unverified), the treatment disappears into the fixed effects entirely.
(2) Flip timing makes the event rare and confounded. Security PRs for an advisory are opened en masse on the same day, so scores for popular pairs likely form within hours to a day, often before or at PR open. Rare pairs never flip. The PRs that do see a flip while open fall in the first hours, when the merge hazard is falling fastest, or they are already-selected laggards. The candidate's own filters (green CI, single dependency, patch/minor, active abstainer, no automerge, flip while open) may leave too few events. The main stratum (patch/minor with green CI) also leaves little room for low scores, so the dose-response test (H2) will be weak.
(3) Nobody observes whether a maintainer actually saw the badge. A silent flip only matters if a maintainer opens the PR after it. With no view data, a null H1 cannot be told apart from "badge ignored". Prior work and practitioner code suggest the badge is often unknown and often ignored. So the most likely outcome is an uninterpretable null, which is neither a crisp stunt nor a clean falsification.
(4) The noisy-nudge placebo is tied to repo activity. Dependabot rebases and force-pushes happen when main moves or conflicts arise, which is exactly when maintainers are active. They also re-run CI. Merge hazard will jump at rebases for mechanical reasons, which makes "nudge > proof" a probable artifact that would falsely count against belief 2.
(5) The 72h discontinuity sits on a crowded focal point. In late 2025 several npm-side tools added 3-day release-age gates: pnpm's minimumReleaseAge, Yarn's age gate and Renovate presets (from memory; I believe these followed the Sept 2025 npm worm attacks). Some can hold CI or a status check until 72h, which interacts with the green-CI conditioning. Org-level presets and Mend workflows are invisible in the repo's config file, so excluding repos by config is leaky. Treated and control releases also differ, since only popular, well-tested releases flip to High.
(6) The provability "fingerprint" is not clean. Low test coverage of dependency code also marks peripheral, less relevant dependencies and weak test culture, so prioritization and maturity theories also predict an interaction. The claim that rival theories predict no interaction is asserted, not derived.
(7) It doesn't generalize to Skylayer's buyers, and the headline is weak. OSS maintainers merging bot PRs are not enterprise change boards. The crisp numbers the study can produce (green-CI security PRs left unmerged; revert rate) overlap Round-1(a). A low revert rate, which I expect, would suggest fear is irrational in this domain, which cuts against the urgency story. The result is a multi-contrast econometrics paper, not a single viral number like "179 servers".

**Prior art found:** Web search was exhausted and arXiv, Scholar, OpenAlex, Crossref, GH Archive, docs.renovatebot.com, developer.mend.io and dependabot-badges.githubapp.com were all blocked by the proxy. Only raw.githubusercontent.com was reachable. I verified the following from primary sources there:
(1) The GitHub docs source (github/docs, concepts/supply-chain-security/dependabot-security-updates.md) says the compatibility score is "calculated from CI tests in other public repositories where the same security update has been generated ... the percentage of CI runs that passed when updating between specific versions".
(2) In fetch-metadata's src/dependabot/verified_commits.ts, getCompatibility() fetches the SVG badge from dependabot-badges.githubapp.com, keyed on (dependency-name, package-manager, previous-version, new-version), and regex-parses '<title>compatibility: N%</title>'. It returns 0 when no score exists. No structured API exists. A real auto-merge script found in the shared scratchpad handles an 'aria-label="compatibility: unknown"' state and lets patch/minor updates proceed on unknown. So "unknown" is common enough that practitioners code around it.
(3) The Renovate docs (docs/usage/merge-confidence.md) confirm: the algorithm is private; Confidence combines Age, Adoption and Passing; Adoption and Passing are weighted toward organizations and private repos, so they are not raw percentages; npm packages under 3 days old cannot get High; Mend sells "Merge Confidence Workflows" (open a PR only at High confidence, or automerge at Very High), which can live in config the repo does not show.
(4) The GitHub Events API docs (github/docs reusables) show PushEvent no longer includes commits on github.com, and PullRequestEvent actions on github.com do not include 'synchronize'. So GH Archive alone cannot reconstruct rebases, force-pushes or PR bodies; you need REST.
From memory, unverified: He, He, Zhang & Zhou, TSE 2023, "Automating Dependency Updates in Practice: An Exploratory Study on GitHub Dependabot". I believe it discusses compatibility scores being rarely available and seen by surveyed developers as of little use, which would be a prior that predicts a null H1. Also Alfadel et al. MSR 2021 (Dependabot security PRs); Cogo, Oliva & Hassan TSE 2019 (npm dependency downgrades as a breakage signal, which is prior art for the revert and downgrade ground truth); Hejderup & Gousios JSS 2022 (tests cover and detect only about half of dependency changes, Java); Reyes et al. 2024 BUMP (a benchmark of breaking dependency updates from bot PRs); Rombaut et al. TOSEM 2023 (Greenkeeper overhead); Mirhosseini & Parnin ASE 2017 and Trockman et al. ICSE 2018 (badges and bot PRs as signals). I could not verify whether an MSR paper already censuses Dependabot and Renovate auto-merge policies; treat H4's novelty as unconfirmed. I found no evidence that anyone has run a within-PR event study on a silent change in a displayed breakage score. That core idea looks novel.

### C3 — Proof, Placebo or Poke: randomized safety proof on real fixes (opt-in app, RMM vendor, CSIRT) (score 4.97, wounded)

**Best headline:** Same N real security fixes, randomized: with a verified blast-radius proof, X% shipped within 14 days. With a same-length placebo note, Y%. The Z-point gap is what 'we don't know what it breaks' costs.

**Skeptic's flaws:** 1. The proof arm bundles REACHABILITY with breakage evidence. Reachability ("is the vulnerable code actually called in your project") is relevance and prioritization information, which is the rival hypothesis belief 2 must beat. If the proof arm wins, a critic says it won through relevance, not safety. As designed, the study cannot falsify belief 2.

2. The control arms are already contaminated. On Dependabot every security PR already carries a compatibility-score badge; on Renovate/Mend every PR carries Merge Confidence badges. Either "control" already contains proof, which weakens the contrast, or you strip a feature users rely on. Also, the repo's own CI result is already visible on every PR, so "the repo's own tests" adds almost nothing. The new information is only dependents' tests.

3. The placebo is not blind. A "true but non-diagnostic" note can be told apart from a data-rich proof. An effect of proof over placebo can then be explained by effort or authority signals, or by blame-shifting ("the bot said it was safe"), rather than by resolved uncertainty. The sign test ("risky" verdicts should slow merges) is the right answer to this, but security bumps are mostly patch-level and high-confidence. Risky verdicts will be rare, so the sign test is underpowered.

4. The trial is underpowered and the outcome is bimodal. OSS security PRs are either auto-merged or merged within hours (ceiling) or sit in dormant repos forever (floor). Detecting a 10pp difference in 14-day merge rates needs roughly 400 PRs per arm. With repo-level clustering (required to avoid maintainers seeing multiple arms and learning) that means thousands of repos. The 200-repo, 8-week pilot cannot say anything.

5. The OSS venue is off-wedge. Reverting a Git dependency bump is already trivial, so the revert-watch arm tests nothing that matters. OSS maintainers are not enterprise owners of production blast radius. Opt-in users of a "proof" app are self-selected proof-seekers, which inflates effects.

6. The DIVD venue is ethically and practically broken. Arms without the urgency block on actively exploited KEV edge devices (the ASA CVEs were under emergency directives) withhold safety-critical information, which IRBs and DIVD will reject. There is no outcome tracking: the case closed the day notifications went out. Scanning cannot see whether peers' upgrades broke anything, so the "safety proof" block is really a survivorship statement. Notices go to abuse@ contacts at ISPs, which prior RCTs show produce floor effects. A null there is uninterpretable.

7. The RMM venue, the only one on-wedge, needs a vendor that Skylayer would compete with to re-engineer its approval UI for a startup. The chance of getting that is low.

8. On constraints: this is a human-subjects behavioral field experiment built on delivering messages to people. It is not an interview, but it breaks the spirit of "technical evidence only", as the candidate itself admits.

9. It fails the brief's viral-stunt test. It needs 6–12 months, depends on partners, outsiders cannot reproduce it, and the likely result is a small difference ("41% vs 47%") or a null. Even a positive result shows that uncertainty is A marginal blocker for opt-in users, not THE blocker.

**Prior art found:** Most scholarly and vendor domains (usenix, arxiv, acm, semanticscholar, openalex, docs.github.com, divd.nl) were blocked, and the web search budget was used up. I checked through GitHub instead.

VERIFIED:
(1) The "proof" treatment is already a product running on real security PRs. GitHub docs (github/docs repo, content/code-security/concepts/supply-chain-security/dependabot-security-updates.md) say Dependabot security updates "may include compatibility scores to let you know whether updating a dependency could cause breaking changes… calculated from CI tests in other public repositories where the same security update has been generated." A GitHub PR search finds about 1.03M Dependabot PRs created since 2026-08-01 that carry the live compatibility-score badge. Both sampled PRs were still open.
(2) Mend Renovate "Merge Confidence" (renovatebot/renovate docs/usage/merge-confidence.md) adds Age, Adoption, Passing-tests and Confidence badges to every Mend-app PR, pitched to "prevent updates which break in production." It also sells "Merge Confidence Workflows" ("automerge Very High confidence updates", "only raise a PR once the update is in High confidence"). That is already Skylayer's "proof + gate by confidence" for dependencies. There is also a built-in rule: npm releases younger than 3 days can never be rated High.
(3) DIVD case DIVD-2025-00039 (Cisco ASA WebVPN, CVE-2025-20333/20362/20363) lists ips: 40887. The case opened 2025-09-25, the first notifications went out 2025-10-03, and it was closed the same day. The file shows no daily rescans or outcome tracking. The 40,887 are ASA instances found, not confirmed-vulnerable hosts. A grep of about 3,000 DIVD case files shows no randomized or experimental notification campaign ever.

FROM MEMORY, NOT RE-VERIFIED (blocked): a mature literature of randomized vulnerability-notification trials. Durumeric et al. IMC 2014 (Heartbleed notification RCT); Li et al. USENIX Sec 2016 "You've Got Vulnerability" (message detail randomized); Stock et al. USENIX Sec 2016 and NDSS 2018; Cetin et al. 2019 "Make Notifications Great Again" (sender and content randomized); Maass et al. USENIX Sec 2021 "Effective Notification Campaigns on the Web: A Matter of Trust, Framing, and Support". Changes to message content mostly had small or null effects, and base remediation rates were low. Also: Microsoft "Nudge" (Maddila et al., FSE/TSE 2022) randomized pure attention nudges on PRs and got large latency cuts, the salience rival stated outright. Mirhosseini & Parnin ASE 2017 (automated PRs vs badges). Alfadel et al. SANER 2021 and He et al. TOSEM 2023 on why Dependabot PRs go unmerged. Self-reports of fear of breakage: Li et al. SOUPS 2019 "Keepers of the Machines" and Tiefenau et al. SOUPS 2020. I know of no published RCT that sets a safety proof against a matched placebo on real fixes, so the exact design is probably new. But GitHub and Mend probably hold internal A/B data on exactly this.

### X2 — Canary Order: which server does each organization patch first? An internet-wide, within-organization sign test of belief 2 (score 4.96, wounded)

**Best headline:** The fix was already on their test box. Across N organizations, the same OpenSSH security update reached the servers M+ domains depend on a median X days after the organization had installed it on its own low-stakes hosts, and Y% of that self-imposed wait came after public exploit code existed.

**Skeptic's flaws:** 1. The headline cannot tell a staging policy apart from doubt about this particular change. HR<1 (dev and low-stakes boxes first) is exactly what standard staged rollout predicts: the ITIL dev→test→prod habit and fixed soak times. Li et al. and Tiefenau et al. already document that habit. A fixed ring or soak policy also predicts H3's 'canary survived d days → production follows' result, so that arm does not discriminate either. Only H2 and the 'canary reverted → production skips' events can tell the two apart.
- H2 has almost no variance with OpenSSH. Ubuntu and Debian security fixes are tiny backports and never a 'new upstream version' in a stable release. Jammy has had only about a dozen OpenSSH USNs, so the interaction is barely identified.
- OpenSSH regression USNs and real canary reverts are very rare, so the H3 event arms have maybe 1–3 events.
- The likely outcome is a clear HR<1 with null interactions. That reads as 'orgs do staged rollout', which critics will call good hygiene, not a bottleneck. The viral headline 'companies patch their least important servers first' sounds like praise for best practice, not proof of an urgent problem.

2. An organization is not one decision-maker. Org-owned ASNs with many exposed SSH hosts are mostly universities, ISPs, research labs and government. There, central IT runs the high-fan-in DNS, mail and web servers, and departments or grad students run the rest. Patch order then reflects which admin team is quicker, not canarying.
- t0_org removes awareness only for whoever patched first. It does not remove it for other admins, or when the first host was an unattended-upgrades box that 'knew' nothing.
- Excluding cloud and hosting ASNs removes most modern production estates. What remains skews toward immature or legacy on-prem operators; mature enterprises rarely expose SSH to the internet.

3. The same label predicts opposite signs. A dev/test box can be a canary, which pushes toward HR<1, or a forgotten box, which pushes toward HR>1. A mixture can give HR≈1 or HR>1 even when uncertainty drives production delay. So the claimed 'clean falsification' is not clean in either direction.

4. Effort and downtime are not actually equal. A banner change marks an apt install run, which usually carries a bundle (libc, openssl, kernel). needrestart then restarts dependent services, and on high-blast-radius mail or web hosts that gets scheduled into maintenance windows. So the gradient can be pure downtime-cost or SLA policy. The ex-ante uncertainty that matters belongs to the whole bundle, not the OpenSSH debdiff.

5. The scan cadence is too coarse to see the lag. The research tier appears to be weekly (research_1w) or monthly, and even commercial Censys refresh is not guaranteed daily per IP:port.
- A canary-to-production lag of a few days, and the '36h in ≥80% of USNs' auto-classifier, cannot be resolved at weekly cadence. With k=3–5 hosts per org, most orders become ties.
- Daily data means a commercial licence. That in turn clashes with academic publication or NC terms.

6. The revert census will mostly count artifacts. The same host key at one IP can front several load-balanced or cloned backends running different revisions, which looks like flapping. On top of that come IP reassignment, NAT or port-forwarding, and banner-rewriting middleboxes. Real openssh-server downgrades are rare, so noise dominates, and a published 'W% rolled back' number is a credibility risk.

7. Blast-radius data is thinner than claimed. CZDS zone files contain NS delegations only, not MX, A or CNAME. The public OpenINTEL bucket covers ccTLDs and toplists only, so fan-in for .com and other gTLDs needs an OpenINTEL agreement. Stratifying within role plus requiring ≥3 same-release manual hosts seen before the fix will shrink the sample hard.

8. The data licences block Skylayer's own use. Censys research terms and OpenINTEL's BY-NC-SA licence are non-commercial, and a startup marketing stunt sits badly with that. The study must be academic-led, and Skylayer cannot reuse the panel in product without separate commercial licences.

None of this is illegal. It is passive and uses existing data. But the belief-2 identification is weak, and the most likely result supports 'staged-rollout policy', not 'per-change doubt'.

**Prior art found:** I could verify very little. The session's web-search budget was used up (200/200). dblp, arXiv, Semantic Scholar, Crossref and docs.censys.com were all blocked by the proxy. What I did check:
(1) GitHub code search shows a Censys research-tier dataset called 'censys-io.research_1w.universal_internet_dataset' (InetIntel/ioda-censys-isi notebook, snapshot_20221206). The '1w' suggests research access is a weekly snapshot, and I recall a free monthly research_1m tier. Daily cadence probably needs a commercial licence.
(2) 'censys-io.universal_internet_dataset_v2.base' exists and is used in academic code (UCLA-SCaN, stanford-esrg). The candidate's claim that historical scan data exists holds.

Prior art from memory, not re-verified:
- Gasser, Holz & Carle, 'A deeper understanding of SSH: results from Internet-wide scans' (NOMS 2014), already parsed Debian/Ubuntu patch-level strings from SSH banners to measure outdated servers.
- Durumeric et al., Heartbleed (IMC 2014), measured population patch decay.
- Tajalizadehkhoob et al., 'Herding Vulnerable Cats' (CCS 2017), split banner-based patch levels between provider and customer.
- SSH host keys as stable host identifiers are established: IPv6 hitlist aliasing (Gasser et al., IMC 2018) and router alias resolution.
- Li et al., 'Keepers of the Machines' (SOUPS 2019), and Tiefenau et al. (SOUPS 2020) already report, qualitatively, that admins test updates on non-production before production. So the headline ordering is a documented practice, not a discovery.
- Kotzias et al. (NDSS 2019) and Sarabi et al. (PAM 2017) measure enterprise and host patch latency from telemetry.

I found nothing showing that anyone has run the specific within-organization, same-fix order test against externally measured blast radius. That part looks new. So do the revert census and the automation frontier split by blast radius, though I could not search properly.

### X5 — The Proof Bill: manufacturers' own 'safe to install' verdicts as a public ledger of how long proof takes, how often it says 'safe', and whether it bends under urgency or liability (score 4.92, wounded)

**Best headline:** Medical and industrial device makers took a median of X days to declare Microsoft's security fixes safe on their products, and Y% of the time the answer was 'no problem found'. For K fixes already exploited in the wild, the only configuration the maker approved stayed the vulnerable one for a median of W days.

**Skeptic's flaws:** 1. The design doesn't isolate impact uncertainty. For FDA-regulated makers (21 CFR 820 design controls, IEC 62304), and in practice for DCS vendors under warranty and IEC 62443, validation is required whatever the uncertainty. Makers would validate even if they were 99.9% sure. So "lag on no-problem verdicts = time spent resolving uncertainty" is true by definition, not a test. A critic will say "that's a compliance cadence," and a high no-problem share supports that reading ("the ritual almost always passes") as much as belief 2. Belief 2's actual rivals (volume, prioritization, unknown assets, site coordination) sit at the operator. The study admits it can't see operators, so it can't falsify belief 2 against those rivals. It can only describe the vendor's proof clock.
2. The urgency-elasticity test, the headline falsifier, is broken twice over. (a) Since 2016, Windows ships one cumulative update per OS per month, and almost every Patch Tuesday in 2022–2025 fixed at least one CVE already marked "Exploitation Detected." At the KB level, "exploited at release" is therefore nearly always 1, so there is almost no contrast. (b) The month×KB fixed effects absorb any KB-level urgency variable, so the main effect can't be estimated. Out-of-band releases are rare (a few a year), and many are themselves fixes for breakage (auth, printing, VPN), which mixes up urgency and breakage.
3. The measure is likely small next to total delay. Vendor proof lags are plausibly 1–5 weeks, while medical and OT sites often lag months or years (unsupported operating systems, maintenance windows, unknown assets). Without site data, "proof takes X days" doesn't show that proof is the bottleneck. It may instead show proof is a minor part, which would undercut the headline, and the partner arm that could settle this is optional and n=1.
4. Measurement and selection. Publication date is not when validation finished. Many lists are one cumulative page showing only current status. Wayback often captures dynamic vendor-portal URLs and PDFs sparsely (monthly or worse), so its resolution is similar in size to the effect being measured. The largest OT vendors (Rockwell, Emerson, Honeywell) and Varian are behind logins, which biases the sample. "Not applicable" verdicts inflate the no-problem share unless removed. Some makers use blanket "install unless we say otherwise" policies, which leaves lag undefined.
5. The secondary arms are underpowered or weakly linked. "Issue found" verdicts and retractions are rare, so PR-AUC on a time-split holdout will be noise. FDA software-change recalls concern the maker's own software, not Windows-patch compatibility, so linking them to validation speed is speculative, with few events per vendor. The IaC mirror arm (374 indexed files, mostly provider wrappers) is essentially anecdote.
6. Strategic mismatch. Even a perfect blast-radius predictor can't legally replace a regulated verification and validation step. The bottleneck measured here is only partly addressable by Skylayer's "proof then act" product, and "act" (auto-remediation on validated devices) is the part regulated customers are least able to allow.

**Prior art found:** I could verify almost nothing this session. The WebSearch budget was already used up (200/200), and WebFetch was blocked for api.fda.gov, web.archive.org, arxiv, Semantic Scholar, Google Scholar, Bing, DuckDuckGo, philips.com, siemens-healthineers.com, yokogawa.com and new.abb.com. GitHub code search turned up no scraped vendor patch-validation ledgers and no public use of openFDA's root_cause_description with the software-change values. Treat the points below as prior knowledge, not checked facts.
(1) P2 (Qualification Clock) already covers the core measure, the lag until the vendor qualifies a patch. X5 adds tests on top of it but has the same backbone.
(2) OT practitioners already treat "the OEM approves Microsoft patches weeks after Patch Tuesday" as common knowledge. IEC/TR 62443-2-3 (patch management) describes vendor qualification of patches, and vendor blogs and ICS commentary (e.g., Verve, Digital Bond) state 2–8 week OEM approval windows. So "vendors take weeks" is not news. A per-KB ledger across vendors with verdicts, retractions and KEV joins is, as far as I know, not published, and that part plausibly is novel.
(3) MDS2 forms (Manufacturer Disclosure Statement for Medical Device Security, 2019 version) are public for many products. They include manufacturer-stated patch-validation practices and timeframes, e.g., "Microsoft patches validated within N days". The candidate misses them. They give stated service levels to test real behavior against, and they already publish the headline "median days" number in rough form.
(4) Dissanayake et al. (CSCW 2022) and the Equifax/Log4j reviews (coordination, unknown assets) remain the main rival explanations. This design can't touch them because it never observes sites.
(5) Industry reports (Claroty, Armis, Unit 42) cover medical/OT patch posture as legacy or unsupported operating systems, not monthly validation lag. That suggests the real exposure in these fleets comes from multi-year OS obsolescence, not from 2–4 weeks of validation.
Data existence: from memory, public monthly lists do exist for ABB 800xA / Symphony Plus (third-party security update validation status), Siemens SIMATIC PCS 7/WinCC (tested Microsoft patches, on SIOS), Yokogawa, and several medical makers (Philips, GE HealthCare, Siemens Healthineers, Hologic, BD). Rockwell, Emerson, Honeywell and Varian (MyVarian) are gated behind logins. I could not confirm the formats or whether any history exists.

### X3 — Twin Servers: the staging-to-production proof gap (same org, same fix, same command, only blast radius differs) (score 4.8, wounded)

**Best headline:** Same company, same fix, same command: across N organizations, internet-facing production servers took a median of Y days to install the regreSSHion OpenSSH fix, versus X days on their own staging twins (Z times longer). Yet only R% of the servers that took the fix ever rolled it back.

**Skeptic's flaws:** No single flaw kills the idea, but several together badly weaken the causal claim.

1. It varies the stakes, not the uncertainty. The fix, and so the uncertainty about it, is identical within a pair; what differs is how much a breakage would cost and how prod is governed. Prod changes need change tickets, CAB or peer approval, customer maintenance windows, SOC2/ITIL change-control evidence and often a different owner (ops vs devs). Staging changes need none of these. A staging-first gap is predicted just as well by coordination and governance (Dissanayake), the main rival, as by belief 2.

2. The opposite-sign test is aimed at a straw man. Almost nobody predicts that internet-facing prod is patched before staging for a routine openssh update. The sign test therefore rules out only the weakest rival and does nothing against coordination. It is close to certain to 'confirm' in orgs with pipelines, so it is not a real falsification test.

3. The soak-vs-calendar test cannot separate the two stories. 'Wait for staging, then wait for an ad-hoc approver or the next change window' gives slope ≈1, with or without weekly clustering. A soak period that is itself calendar-aligned does the same. Timestamps alone cannot tell uncertainty-driven soak from an approval queue.

4. The placebo is weak. Certificate renewal is automated by a certbot timer and fails loudly, so prod will not lag there whatever the cause. A null says nothing about whether prod updates in general are neglected.

5. Staging may be patched for reasons unrelated to this CVE. unattended-upgrades is on by default in Ubuntu server and cloud images, and devs run routine apt upgrade sweeps on staging. So 'the org knew and had prioritized this CVE' is not shown by staging being patched. The manual-manual subset helps, but classifying hosts as manual needs daily-resolution history over several prior openssh USNs (only 2–4 a year), which may not exist.

6. The dominance test is biased toward belief 2. The twin sample selects orgs with named, structured environments, i.e. known assets. Computing the 'never patched / unknown asset' share inside that sample understates the main rival.

7. The flagship CVE is contaminated:
   - Many orgs mitigated regreSSHion with LoginGraceTime=0 without upgrading. The banner does not change, so prod 'vulnerable days' are overstated.
   - regreSSHion and Terrapin were widely judged hard or impractical to exploit, which weakens the 'prioritized' premise.
   - The CrowdStrike outage on 19 Jul 2024 falls inside the regreSSHion prod window and could shift prod update behaviour on its own.

8. Selection and external validity. The only prod hosts in the sample expose SSH publicly and terminate TLS on the same IP; production APIs usually sit behind CDNs/ALBs and bastions. That means small VPS shops, the opposite of the FDA-regulated enterprise design partner. Mature orgs also set DebianBanner=no.

9. Data and money are unverified.
   - Censys research access is non-commercial, so a Skylayer-branded stunt conflicts with it unless an academic PI owns and publishes the work.
   - Commercial historical Censys at this scale is likely well above the $10–30k estimate (unverified).
   - Shodan history is coarse.
   - The number of twin pairs is unknown; manual-manual pairs that are both patched in place may be only in the tens per USN.

The headline 'prod waits for staging' is also easy to dismiss as intended best practice.

**Prior art found:** I could only check a little. The web search budget was used up (200/200), and the proxy blocked every literature and data-source site I tried: dblp, arXiv, OpenAlex, Crossref, Semantic Scholar, DuckDuckGo, Bing, docs.censys.com, support.censys.io, help.shodan.io and bitsight.com.

What I did confirm:
(1) USN-6859-1 was published 1 Jul 2024 with fixes jammy 1:8.9p1-3ubuntu0.10, noble 1:9.6p1-3ubuntu13.3 and mantic 1:9.3p1-1ubuntu3.6.
(2) Since 22.10, Ubuntu (including noble) starts sshd through systemd socket activation. The banner still tracks the installed binary: package upgrades restart the service, and sshd re-execs itself for each connection. So the banner is a valid proxy for the installed revision.
(3) The censys-python v2 docs include view_host_events for the hosts index but say nothing about plan tiers or rate limits. Whether this history is available at scale, and at what price, is still unverified.
(4) A GitHub repo search for tools that measure patch lag from SSH banners returned 0 results.

Prior art I know of but could not re-check here:
- Gasser et al. 2014 read Debian/Ubuntu revision patch levels from SSH banners.
- Durumeric et al. IMC 2014 measured Heartbleed patch decay.
- Kotzias et al. NDSS 2019 used enterprise telemetry.
- Censys, Shodan, Qualys and others published regreSSHion exposure counts.
- Commercial ratings firms (Bitsight and SecurityScorecard 'patching cadence') already compute patch timing per organization from exactly this external banner signal. That is the closest prior art: same data, same unit (the org). They do not compare staging and production twins.
- Attack-surface vendors (e.g. Unit 42/Xpanse) report that dev/test assets are neglected, but descriptively, not as a timing contrast within one org.

I know of no published within-org comparison of staging and production twins that uses host-key continuity. Treat that as plausibly novel, but I could not rule out prior work.

### X6 — Nobody Goes First: the sibling-precedent trust gap in public government production pipelines (score 4.78, wounded)

**Best headline:** Nobody goes first: in N public government production services, security fixes that were already built, tested and live in pre-production waited a median X days for the first team to approve them for production. Once K sibling teams had shipped the same one-line fix without a rollback, the next team shipped it in X2 hours.

**Skeptic's flaws:** None of these kills the study outright, because the data exists and the design is legal. But several of them undercut the causal claim, which is the point of the study.

1) The comparison group shrinks to one department. GOV.UK has no human gate: whitehall is set to automatic deploy and auto-promote, and every commit is by the govuk-ci bot. So GOV.UK can only serve as the "machine acts" comparison, and the human-gated sample is essentially the MoJ DPS/HMPPS teams. GOV.UK is Ruby and HMPPS is Kotlin/Node, so few fixes appear in both. That makes the GOV.UK vs MoJ contrast apples to oranges.

2) The main identifying variation mostly disappears. Every sibling that posts to the shared channel sees the same precedent count on the same calendar day, apart from the small correction for the team's own services. Once the model stratifies by fix and calendar time, the effect has to be identified from differences between portfolios. There are few portfolios with overlapping fixes, and each has its own deployment culture.

The alternative is to measure time from when the fix goes live in preprod. Then precedent count is almost the same thing as how late the team is, which is post-treatment: precedent also affects whether and when a team merges. The instrument (siblings' usual release weekdays) is likely weak, because HMPPS deploys close to daily.

3) Correlated shocks (Manski's reflection problem) cannot be ruled out. A security or platform team pushing one specific fix across a portfolio (for example through the HMPPS developer portal, Veracode/Trivy dashboards, or a Slack ping) creates sibling prod deploys and focal prod deploys at the same time, with the siblings more than 24h earlier. None of the three placebos rules this out:
- Unrelated deploys do not mention the fix.
- Under a campaign, teams go straight to prod, so there is no preprod-only activity to compare against.
- Deploys in another department are not exposed to the campaign.

4) The salience placebo does not match the treatment. Changelog-bearing channel posts remind people about this specific fix, while the placebo is unrelated changes. Only the revert sign test separates a fix-specific reminder from safety evidence. Prod reverts of security bumps are rare: 75 'Revert "Update dependency' hits across all of MoJ, most of them probably not security and not in prod. So the test is underpowered.

Worse, the pre-registered rule "no sign reversal ⇒ belief 2 fails" treats a non-significant result as proof of no effect. That is an invalid falsifier.

5) The claim that precedent carries only one kind of information is false. A sibling's deploy also signals that the fix works through the shared pipeline (effort), that others are expected to do it (a norm), and that responsibility is shared (accountability herding, as in Scharfstein and Stein). The sign test cannot tell safety information apart from accountability herding.

6) Choosing "solo windows" (the fix is the only change between two prod deploys) conditions on the outcome. In trunk-based repos any merge before approval ends the window. The solo windows that survive therefore come mostly from dormant services, where a long wait means nobody is watching.

7) The container/OS subset for wedge B (Skylayer's candidate OS/package/container-patching entry point) can mostly not be seen. Floating base-image tags pull in OS fixes on every rebuild without any commit.

8) The viral headline is weak. The observed gate waits are on the order of hours to about a day, often just waiting for the next working morning. That makes the predefined falsifier "the trust gap is a small share of the exposure window" likely to fire. That would be an honest null, but it is not a stunt that cuts through the noise. The population (mature continuous-delivery teams that code in the open) also says little about FDA medical-device shops or ordinary enterprises.

9) There is an ethics gap. Masking department names does not work when the corpus is publicly named as MoJ, GOV.UK and DfE. A reproducible CLI that runs live against third-party orgs would list production services that are currently running a known-vulnerable version.

**Prior art found:** I could not complete the prior-art check. The WebSearch budget for this session was already used up (200/200), and the proxy blocks arxiv, usenix, semanticscholar, bing and duckduckgo. I could only reach GitHub. So the prior-art list below comes from memory and must be confirmed before anyone claims novelty.

What I found from memory:
1) The "wait for someone else to go first" behaviour is already documented, but only through interviews and surveys, never measured causally:
- Li et al., "Keepers of the Machines", SOUPS 2019
- Tiefenau et al., "Security, Availability, and Multiple Information Sources", SOUPS 2020. Admins watch other people's reports (e.g. Patch Tuesday megathreads) before patching.
- Pashchenko et al., CCS 2020. Fear of breaking changes in dependency updates.
- Beattie et al., LISA 2002, which modelled the optimal wait before patching.
2) Industry already sells precedent as proof of safety: Dependabot's compatibility score, Mend/Renovate Merge Confidence (adoption / passing / confidence), and Windows Update/Autopatch deployment rings. This competes with Skylayer's "manufactured precedent", though it does not replace the measurement.
3) Diffusion of adoption across GitHub has been measured before, but not for security fixes at production gates:
- Lamba et al., "Heard it through the Gitvine", FSE 2020
- Trockman et al. on badges, ICSE 2018
- Mirhosseini & Parnin, ASE 2017
- Alfadel et al., MSR 2021 (Dependabot security PRs)
- He et al., TSE 2023 (Dependabot)
4) Manski's reflection problem (1993) is the textbook reason this kind of peer-effect design gets attacked.

I did not find a study that estimates how much sibling precedent speeds up the human production gate in real pipelines. That specific measurement looks new, but the underlying mechanism does not.

Data checks, done this session through GitHub web pages:
- VERIFIED: alphagov/govuk-helm-charts has charts/app-config/image-tags/production/ with about 67 apps. Each app has a bot commit history ("Update whitehall image tag to vNNNN for production", by govuk-ci), which works as a production deploy log. The whitehall file sets automatic_deploys_enabled: true and promote_deployment: true.
- VERIFIED: ministryofjustice/hmpps-github-actions deploy_env.yml uses `environment: ${{ inputs.environment }}`, which enables the approval gate. It always posts prod releases to one shared Slack channel (CVA3MKDTR, "DPS releases"), and it has a show_changelog option.
- VERIFIED: in hmpps-prisoner-profile (2,178 pipeline runs), main-branch runs show several "Waiting" runs. The completed ones took 18h19m ("Bump multer 2.3.0→2.4.0") and 20h10m ("sec: pin moment and proxy-addr").
- NOT CHECKED: that the GitHub approvals endpoint (/actions/runs/{id}/approvals) returns data for these repos, and how many prod reverts of security bumps exist.

### P4 — Same Fix, New Warning: vendor-declared breakage risk on an identical patch (Known-Issue Shock, sharpened) (score 4.73, wounded)

**Best headline:** Same patch, same CVEs, one added warning: Citrix gateways the 'may break SSO logins' notice could affect stayed exposed X days longer than on a clean KEV fix, and Y% of gateways it could NOT affect stalled too, because nobody could prove it didn't apply to them.

**Skeptic's flaws:** 1. The test cannot fail as written. The hypothesis says users outside the warning's scope also slow down because they cannot prove the issue doesn't apply to them. The stated test is "falsified if exposed and unexposed patch equally fast", but full spillover to the unexposed predicts exactly that equal speed. Equal speed therefore cannot tell "the warning had no effect" apart from "everyone was frozen". The only no-warning comparison is the 2023 Citrix placebo, which differs in almost everything: a different bug and publicity cycle, different exploitation dynamics, and a fleet changed by IP churn and device replacement. That makes device fixed effects across 2023–2025 weak.

2. The design measures cost, not uncertainty. In both arms that can actually be run, the warning goes with a real incompatibility.
   - Citrix: CSP really does break some login flows, so for exposed gateways the fix is harder.
   - Jenkins: compatWarning literally says behavior or settings format changed and jobs may need reconfiguring. Installs below compatibleSinceVersion also face a larger real code change.
   So "same bytes, only the declared risk differs" is false for Jenkins and only partly true for Citrix. Any slowdown found can be read as "the fix is hard / known breakage", which belief 2 explicitly rules out. It does not show that delay comes from being unable to prove the change is safe. The pilot's own result, that about 57% of stuck installs needed a core upgrade first, points to linked changes and upgrade effort as the barrier.

3. Exposure in the Citrix arm is badly misclassified. A SAML/nFactor redirect usually does not show up in a pre-authentication fetch of the root page, and Duo over RADIUS is invisible from outside. The "unexposed" group will contain exposed gateways, which blurs both the main effect and the spillover. Exposed gateways (organizations with an external identity provider) are also bigger and run change boards, so they differ in kind from the rest.

4. Timing and data access.
   - As I recall, CVE-2025-6543 went on the KEV list on 30 Jun 2025, the same day as the warning; the proposal lists this as a risk.
   - The "fixes only one CVE" build (14.1-43.56) was already the natural target between 17 and 25 June, so choosing it is confounded with ordinary inertia.
   - The warning offered a one-line workaround (turn off CSP), so the treatment may be weak.
   - Censys historical access is for academic, non-commercial use, and it is unclear whether DIVD would share IP-level case data with a startup. The Citrix arm realistically needs an academic co-lead.
   - The Windows arm depends on raw Mozilla telemetry, which Mozilla does not give to outside commercial parties. The RMM and insurer arms are speculative.
   - Jenkins data is aggregate only (no per-install panels), and the overlap between compatibleSinceVersion and security fixes is rare, so statistical power is doubtful.

5. The headline is weak. "Exposed Citrix gateways patched X% slower" reads as a vendor-specific quirk, not a crisp, reproducible number that cuts through the noise. The Jenkins result will read as "breaking changes slow upgrades", which is already known.

It is legal as designed: third-party aggregates, no scanning. If anyone ran the Fox-IT fingerprinting themselves, that would be scanning and must be avoided.

**Prior art found:** Verification was limited. The web-search budget was already used up, and support.citrix.com, bleepingcomputer.com, csirt.divd.nl, stats.jenkins.io and updates.jenkins.io were all blocked by the proxy. So I could not check the text of the Citrix notice CTX694826, how DIVD shares data, or the terms of Censys research access. I checked what I could through git:
- The Jenkins data is real and current. The jenkins-infra/infra-statistics gh-pages branch was last updated 2026-09-23 and covers data through 2025-12, after a batch of backfill commits (so the pipeline had lagged).
- It has 2,421 plugin-installation-trend JSON files. Each holds a monthly install time series, but its per-version breakdown is only the latest snapshot. It also has 2,411 pluginversions pages, each a plugin-version × core-version matrix. Per-version history over time has to be rebuilt from git history (the branch has 231 commits).
- Everything is aggregate counts. There is no per-install record, so you cannot follow individual installs or compute a true upgrade hazard.
- In Jenkins core, updates.properties (compatWarning) says the warning appears because the new version "is marked as incompatible ... because its behavior changed, or because it uses a different settings format", and that "Jobs using this plugin may need to be reconfigured". So the warning goes with a real change the maintainer declared.
- Jenkins usage statistics are collected by default and admins opt out (Jenkins.java: noUsageStatistics == null means collected; UsageStatistics turns it off under FIPS). The candidate's claim that they are "opt-in" is wrong.

Prior art, from memory and not re-checked this session: a lot of software-ecosystem work already shows that breaking or incompatible changes slow adoption of fixes:
- Chinthanet et al., EMSE 2021, on lags in npm vulnerability-fix adoption
- Decan, Mens and Zerouali on technical lag and semantic versioning
- Kula et al., EMSE 2018, "Do developers update their library dependencies?"
- Derr et al., CCS 2017, on how easily Android libraries can be updated
- Nappa et al., S&P 2015, on patch deployment
- Tiefenau et al., SOUPS 2020, and Li et al., SOUPS 2019, on sysadmins holding back updates over breakage reports (these are survey and interview studies)

Shadowserver, Fox-IT, DIVD and Censys have all published Citrix patch-rate trackers. I know of none that uses the CSP-default warning as a treatment. So the exposed-vs-unexposed design on the same patch looks new in its details, but the general finding is already expected.

### C2 — Safe but Stuck Bench: perceived vs actual breakage of held-back security upgrades, and the AI fix-vs-proof clocks (score 4.72, wounded)

**Best headline:** Held back for fear, not breakage: X% of the security upgrades that N real projects skipped passed the project's own tests unchanged. The 'major' label, not the measured breakage, predicted which ones waited, and they waited Y times longer.

**Skeptic's flaws:** 1) It does not isolate impact uncertainty. The "fear premium" is a label effect among pairs that passed in the lab, but the major label also carries several other things:
- Expected migration effort: reading changelogs and migration guides, which is cost, not uncertainty.
- Tool friction: `npm audit fix` skips majors without --force, Renovate and automerge rules usually cover only minor and patch, and Dependabot `ignore versions` ranges can block security PRs (verified in the docs).
- Awareness.
- For library dependents, which is what deps.dev gives you, real downstream obligations. Bumping a dependency's major can force the library's own major release or cause dependency-convergence conflicts for its users, and the library's own tests never see that. Delaying there is rational, and it is not fear.
So a positive result fits prioritisation or effort just as well as uncertainty, and critics will say exactly that.

2) The headline oracle is weak and ironic. "Broke nothing in its own tests" is itself an unproven safety claim. Hejderup & Gousios showed tests miss about half of dependency changes, so a critic can argue the developers' caution was rational, and the claim "X% were safe" collapses. Measuring coverage of changed lines helps but does not catch behavioural or semantic breaks.

3) The prior art and existing products already cover the core number. GitHub's compatibility score is literally this measurement, done at scale. Novelty is thin, and it is a near-repeat of Round-1 (a).

4) The AI clock compares unlike things. A dependency fix is a one-line version bump that Dependabot already writes in seconds. SEC-bench and AutoPatchBench are about source-level vulnerability repair in C/C++, which is irrelevant to dependency upgrades. And "compute-hours for proof" is just CI runtime, which is not proof. Critics will dismiss the "minutes vs hours" line.

5) The production-vs-development sign test cannot identify the mechanism. If production PRs merge slower, the same result is predicted by review and CODEOWNERS or release-coordination overhead, which is Dissanayake's coordination finding. Repos that list a package as dev versus prod also differ systematically (libraries vs apps), and development-scope alerts are often dismissed by policy.

6) Strategic mismatch. The evidence is about OSS library SCA, a crowded market (Snyk, Endor, Socket, Mend, Dependabot). It is not about OS, package or container patching in enterprises (wedge B) or FDA-regulated operations, and "OSS is not enterprise" undercuts the belief-2 claim for Skylayer's buyer.

7) Feasibility is honest but thin. Reproducing builds of old Maven commits will likely come in under 50%, which leaves perhaps 1–3k usable pairs after filters. The major-security-fix subset where the lab run passes and the dependent is an "active abstainer" may be small and odd. The deps.dev dependents claim is unverified here; those are package-to-package edges, not applications.

It is not dead: it is legal, the data mostly exists, and it could falsify belief 2. But as designed it shows delay correlated with a label. It does not show delay caused by uncertainty about breakage.

**Prior art found:** Research limits: the WebSearch budget was already used up, and arxiv, Semantic Scholar, Crossref, ACM, dblp and Scholar were all blocked by the proxy. I could only reach raw.githubusercontent.com. The two items marked VERIFIED below were confirmed this session. Everything else is from memory and should be checked before anyone relies on it.

VERIFIED 1, GitHub's own docs (github/docs, dependabot-security-updates.md): "An update's compatibility score is the percentage of CI runs that passed when updating between specific versions of the dependency", computed from other public repositories that got the same security update. GitHub already measures, per security update, "does this bump break real dependents' tests" across many more dependents than the proposed lab would.

VERIFIED 2, BUMP README (chains-project/bump): BUMP is a benchmark of reproduced breaking updates only. It keeps a pair only when the build fails after the bump, it is 1,142 Docker images needing about 250 GB, and it has a folder of unsuccessful reproductions. It is not a harness for sampling random dependents, and it says nothing about how often an update is safe. "BUMP harness (verified)" overstates what it gives you. The reproduction pain is real, which supports the 30–50% risk.

VERIFIED 3, the dependabot-options-reference doc: `ignore` with `versions` ranges applies to security PRs, while `update-types` (for example semver-major) applies only to version updates. So a repo's tool policy can silently block or allow major-version security fixes. This is a measurable confound.

From memory, not re-verified this session:
- Ochoa et al., "Breaking Bad? Semantic versioning and impact of breaking changes in Maven Central", EMSE 2022: most majors do not affect most clients.
- Raemaekers et al., JSS 2017: the same finding, earlier.
- Venturini et al., "I Depended on You and You Broke Me", TOSEM 2023: ran npm clients' tests across dependency updates and found about 12% of clients affected, with many breaks in minor or patch releases.
- Jayasuriya et al., FSE 2024: behavioural breaking changes, measured with client tests.
- Hejderup & Gousios, "Can we trust tests to automate dependency updates?", JSS 2022: project tests caught only about half or fewer of injected dependency changes. This directly undercuts the headline "broke nothing in their own tests".
- Chinthanet et al., "Lags in the release, adoption and propagation of npm vulnerability fixes", EMSE 2021; Decan et al., MSR 2018; Zerouali (technical lag): adoption lag of security fixes by release type is already studied.
- Kula et al., EMSE 2018; Mirhosseini & Parnin, ASE 2017; Pashchenko et al., CCS 2020: fear of breakage is already documented qualitatively.
- Alfadel et al., MSR 2021, and He et al., TSE 2023, both on Dependabot security PRs, merge behaviour and compatibility score.
- Zhang et al., CORAL (ICSE 2023) and Ranger (ASE 2023); Wu et al., ICSE 2023: most Maven vulnerable dependencies can be fixed compatibly, yet they persist.
- The Reyes/Monperrus group's Breaking-Good and Byam: explaining and repairing breaking updates with LLMs.
- Industry: Mend/Renovate Merge Confidence (crowd-sourced pass rate and adoption), Endor Labs upgrade-impact analysis, OSV-Scanner guided remediation.

Net: "most held-back upgrades would pass tests, and semver labels over-predict breakage" is established in the literature. The only new part is the label-by-lab-outcome cross on security fixes with Cox models, plus an LLM benchmark arm. The candidate also overlaps heavily with Round-1 idea (a): Dependabot/Renovate security PRs, time to merge by CI result, and upgrading real dependents to run their tests.

### X8 — Patched Next Door: the Sibling Gap (within-organization hold time on the same fix, measured from public scan history) (score 4.61, wounded)

**Best headline:** Among N organizations that had already patched regreSSHion on at least one internet-facing server, X% of their total exposure-days came after that first fix, and their busiest servers waited a median Y days longer than their own test boxes. (The honest alternative: never-patched, forgotten boxes held Z% of exposure.)

**Skeptic's flaws:** 1) The identification premise fails on its own 'why now' default. The design argues that once a sibling is patched, the org has shown awareness and intent. But Ubuntu applies the fix automatically, usually within about a day. So the typical 'first fix' in an org is unattended-upgrades acting on a host with default settings, which shows no human awareness at all. The remaining 'sibling gap' then mostly measures differences between hosts: image lineage, hosting-provider templates that turn off unattended-upgrades, internal snapshot mirrors (Landscape/Aptly/Artifactory), no outbound access to the archive, missing ESM/Pro entitlement, a broken dpkg state. None of these is a decision to hold this fix. Telling 'autopilot' from 'human on day 2' needs daily-or-better scan cadence for port 22, and the design has not verified it. Requiring a clearly human first fix would shrink the sample sharply.
2) The headline number is nearly tautological. If the first sibling patches on day 0–1, then almost 100% of the other hosts' exposure-days fall after that first fix, simply because of how orgs are selected. X% says nothing about the cause of delay.
3) The 'opposite-sign' horse race does not separate the rival that matters. Process and coordination (the Dissanayake finding) predict the same signs as uncertainty. ITIL/CAB approval, per-tier maintenance windows and dev→staging→prod ring rollouts are process, and they are applied by criticality. They produce a positive blast-radius gradient, and production skipping windows in which test boxes were patched. The pre-registered claim that process predicts 'no link to blast radius' is a straw man. Prioritization and unknown assets both predict a negative gradient, so the four-way race is at best two-way. The burn-in test is not identified: without a sibling revert, 'clean sibling-days' is exactly 'days since the first patch', so a rising hazard fits a fixed ring-promotion delay or ordinary duration dependence just as well. The one test that could discriminate, the revert test, relies on in-place openssh downgrades on Ubuntu. These are nearly nonexistent: a downgrade reintroduces the CVE, and older security revisions are not kept in the pocket. That test is underpowered by construction.
4) The blast-radius index is confounded with who owns the host and how it is built. Apex/MX/VPN/SSO/git hosts are more often run by an ops team, built from hardened images with auto-updates off, placed under change control, rebuilt immutably (and so dropped as 'rebuilt'), or vendor-gated appliances. The gradient would largely measure operational maturity, not fear of breakage. Mature orgs also rarely expose production sshd to the internet, so the high-blast-radius cell is a strange selected sample.
5) 'Switched off the default-on patcher' cannot be observed, and it is misread as a refusal to let a tool act. Missing the autopilot window has many causes (listed in point 1). Orgs often disable unattended-upgrades precisely because a central tool (Ansible, Landscape, Automox) applies patches on a schedule. That is letting a tool act.
6) Org attribution collapses where it is needed. Most internet-facing Ubuntu sshd hosts sit in cloud or hosting ASNs, which the design excludes. What remains is ISPs (many unrelated customers), universities (independent departments, the admitted 'different teams' confound) and government. CT/DNS attribution only covers hosts that also serve named TLS.
7) The pilot event is contaminated. For regreSSHion, Qualys's widely repeated mitigation (LoginGraceTime 0) cannot be seen in the banner, and exploitation on 64-bit was considered impractical. Hosts that were mitigated, or rationally deprioritized, would be counted as 'held'. Several of the 2026 OpenSSH USNs are probably client-side CVEs, where not rushing the server is rational.
8) Data access is unproven. The Censys timeline is a per-host API costing 1 to N calls, so a panel of millions of hosts over 5 years needs bulk historical snapshots. Their availability after the Censys platform change, their cadence, and whether a startup may publish commercially from research-program data are all unverified. The research program is typically non-commercial. Legal and ethical design is otherwise clean: no scanning, results in aggregate, coordinated disclosure.

**Prior art found:** What I could check: my web-search budget was used up, and the proxy blocked arXiv, dblp, Google Scholar, Semantic Scholar, USENIX, Launchpad, Bing, DuckDuckGo and the Wayback Machine. I confirmed three things directly: (a) USN-6859-1 was published 1 Jul 2024 with fixes 22.04 1:8.9p1-3ubuntu0.10, 23.10 1:9.3p1-1ubuntu3.6 and 24.04 1:9.6p1-3ubuntu13.3; (b) Ubuntu Server docs say unattended-upgrades is 'installed by default', applies security updates only, runs daily from systemd timers with a random delay, and supports a Package-Blacklist; (c) the censys/censys-ai-skills README describes 'censys-timeline' as a per-host API that costs 1 to N calls per host. It does not state how far history goes, and some history features need the paid Threat Hunting module. Prior art from memory (unverified, but I am confident these exist): Kotzias et al., NDSS 2019 'Mind Your Own Business' (patch rollout across hosts inside 28K enterprises, which is the within-org spread of patching, via endpoint telemetry); Tajalizadehkhoob et al., CCS 2017 'Herding Vulnerable Cats' (uses software-version banners to split patch-level variance between hosting provider and customer, the same responsibility-decomposition logic); Zhang et al., NDSS 2014 and Liu et al., USENIX Security 2015 (org-level consistency of mismanagement signals); Durumeric et al., IMC 2014 (Heartbleed patch decay); Gasser et al. 2014 (SSH scans that read Debian patch levels from banners); Li et al., SOUPS 2019 'Keepers of the Machines' and Tiefenau et al., SOUPS 2020 (admins deliberately test updates on a subset of machines before production). That last point means the likely headline, 'prod waits longer than test', is already documented as normal admin practice. I found no published within-organization sibling design on scan history, so the framing looks new. The behavior it would find does not.

### X4 — Same Bits, New Badge: vendor 'preferred' relabels as a proof-only natural experiment on real firewalls (score 4.47, wounded)

**Best headline:** No code changed, just a label: when Palo Alto marked a firewall build 'preferred' a median 32 days after it shipped, X% of N internet-facing firewalls still on vulnerable builds upgraded within 14 days, versus Y% after a CISA KEV listing. W% of vulnerable firewall-days were spent waiting for a vendor's word that the fix was safe, not for the fix.

**Skeptic's flaws:** No single flaw kills it, but several serious ones stack up.

1. The treatment is not 'proof only'.
- The PAN 'preferred' flag is bundled with default visibility: the Device > Software and Panorama filters are checked by default, so an unlabeled build is effectively hidden.
- It is also bundled with mechanical availability: a verified Panorama bug stopped admins from upgrading to non-preferred releases.
- It also carries vendor authority and support posture. Change boards and MSPs often have 'vendor-recommended only' rules, and TAC pushes customers to preferred releases.
- A burst at the flip is therefore just as consistent with friction, visibility or a compliance rule as with impact uncertainty.
- The planned information-only arms are weak:
  - Pre-filter PAN-OS builds are old or EOL devices, so that arm is confounded with dormancy.
  - Cisco's 'Suggested' star sits on the download page, the point of acquisition, so it is not information-only.
  - Juniper's page needs a login.
  - Fortinet adds in-GUI Mature/Feature tags and, possibly, default automatic patch upgrades on some models (unverified).
- Falsifier (d) may be untestable, which leaves the UI-default confound unresolved.

2. Timing is tangled with urgency and attention shocks, and the clean pilot shrinks from 5 events to about 2.
- PAN publishes advisories on the second Wednesday of the month: 12 Aug and 9 Sep 2026.
- The 10 Sep flip came 1 day after the 9 Sep PSIRT day. 11.2.10-h14 was released on the same branch the day before the flip.
- The 5 Aug and 7 Aug flips fall within 7 days of the 12 Aug PSIRT day.
- The candidate's own ±7-day exclusion removes 3 of the 5 events. Of the 2 left, 11.1.13-h7 lost the label after 7 days, so its treatment reverses inside the 14-day window.
- Each branch ships a new hotfix every 2–4 weeks (11.1.13 had h5 to h12 between May and Sep). A ±28-day window around any flip therefore almost always contains another release or advisory, and the 'vulnerable pool' shifts under the analysis.
- The three-branch batch flip also contaminates the cross-branch same-day placebo.

3. The outcome data is unverified and the fingerprinting is stale.
- The panos-scanner table stops at April 2024.
- Hotfix-level resolution from static-asset timestamps for 2025–26 builds is unproven.
- It is unknown whether Shadowserver, Censys or DIVD would share per-build daily counts or hashed per-device panels.
- Internet-facing GlobalProtect portals are a biased slice. IP churn weakens device fixed effects and the downgrade measures.

4. Power and timeline are over-promised.
- Only the data since May 2026 gives day-level label dates. Wayback history gives dates only to within weeks, which breaks a daily regression discontinuity.
- At about 15 PAN flips a year, with roughly half lost to exclusions, 30 clean events is a multi-year prospective study, not 5–9 months.
- A latent-class typology over K events per device needs long device panels that may never be granted.

5. The headline numbers go beyond what the design can identify.
- 'W% of vulnerable firewall-days spent waiting for proof' is not identified. The discontinuity gives a local jump at the flip, and assigning device-days to classes depends on the model.
- The median lag of 32 days coincides with common 'wait 30 days' policies. With so few events, build age and label are nearly collinear.
- In the collision test, movers after the label may simply be following their maintenance calendar.

6. The finding sits off wedge B, the patching wedge the evidence favours.

**Prior art found:** Web search could not be used: this session's 200-search budget was already spent. The proxy also blocked knowledgebase.paloaltonetworks.com, security.paloaltonetworks.com, endoflife.date, dashboard.shadowserver.org and Reddit. The prior-art check therefore rests on GitHub and on memory, and is incomplete.

What I verified myself by cloning into /tmp:
(1) github.com/mrjcap/panos-versions exists, but it has no LICENSE file. The candidate's numbers reproduce exactly: 43 snapshots that carry the preferred field (14 May to 22 Sep 2026), 580 builds, 82 released in the window, and 5 flips to preferred:
- 11.1.13-h7 on 31 Jul, lag 58 days
- 12.1.7-h3 on 4 Aug, lag 12
- 10.2.18-h9 on 5 Aug, lag 15
- 11.1.13-h9 on 7 Aug, lag 32
- 11.2.10-h13 on 10 Sep, lag 43
The repo commits only when something changes, and the updater runs privately. So flip-date precision depends on a cron job whose uptime cannot be seen.
(2) github.com/noperator/panos-scanner: its version-table.txt was last updated 24 Apr 2024. It has no entries for 10.2.13+, 11.1.13, 11.2.x or 12.1.x, so none of the 2026 preferred builds can be fingerprinted with it.
(3) github.com/aaronaxvig/firewallissues (12.1.5 addressed issues) confirms a Panorama bug that stopped admins from upgrading to non-preferred releases.

Academic prior art, from memory and not re-checked:
- Beattie et al. LISA 2002 (optimal wait time).
- Tiefenau et al. SOUPS 2020 and Li et al. SOUPS 2019. These surveys and interviews found that admins wait for other people's field experience before patching, so the behaviour itself is already reported, though not causally.
- Kotzias et al. NDSS 2019 (enterprise patching); Nappa et al. 2015; Duebendorfer and Frei 2009.
- Vendor practice: Fortinet 'Mature/Feature' tags and the Cisco gold-star 'Suggested' release exist because vendors know customers wait.

I found no study that uses a vendor re-label of identical bits as a natural experiment. The identification idea looks novel. The underlying claim that admins wait for vendor endorsement does not.

### C9 — Switched Off: fixes vendors ship disabled, and fixes users switch back off (score 4.43, wounded)

**Best headline:** The fix was already installed: across X vendor security changes, vendors turned them on for new customers on day one but left them off for existing customers for a median of D days, and where the vendor shipped log-based readiness proof, that wait fell by N%.

**Skeptic's flaws:** 1. The design does not isolate uncertainty. A gap between new and existing customers is simply grandfathering: new customers have no legacy dependencies. The gap shows that dependencies exist, not that anyone is uncertain about them. It fits equally well with known incompatibility, commercial churn risk, contractual obligations or support cost. KB5014754, the flagship example, was postponed repeatedly because customers had to reissue certificates and update third-party CAs. That is known, costly work ("the fix is hard"), which the thesis explicitly excludes. The falsification rule only counts vendor bugs or vendor capacity, so customer remediation work would be coded as support, which makes the test biased toward confirming belief 2.
2. The lab removal test measures the wrong thing, and its result undercuts the thesis. These switches guard against dependencies that are not in the repository: corporate TLS-inspecting proxies (PYTHONHTTPSVERIFY=0), peers still using PKCS#1 v1.5 (Node --security-revert), CI runner user IDs (safe.directory). A lab run without those dependencies will pass, so "Z% removable with zero test failures" is an artifact of how the test is built. A critic will also note that Skylayer's own thesis says tests are not proof of safety.
3. Many switch-offs are sensible decisions, not fear. In a single-user container, the multi-user threat behind CVE-2022-24765 does not exist, so safe.directory '*' is a reasonable choice there. These cases would inflate the "stuck" count.
4. "Never flipped back" is better explained by neglect (the well-documented stale-flag and technical-debt pattern) than by uncertainty. The design has no way to tell fear from forgetting.
5. The vendor-side causal tools are weak. The SaaS vs self-managed comparison mixes different vendors, products and customer bases. Readiness tooling (audit modes, event logs) usually ships together with the first announcement, so there is almost no staggered timing for the difference-in-differences design, and where timing does vary it is chosen by the vendor. With 150–300 very different changes, the estimate would be noise plus the coders' judgment.
6. Stated postponement reasons are sanitized PR language, usually "give customers more time", which cannot distinguish uncertainty from workload.
7. The headline is four numbers (X, D, N, Z), not one crisp figure, and its most shareable part (Z) is the one that is invalid. It also measures vendors' decisions, not whether an organization's own remediation is delayed, so it only loosely supports wedge B.

**Prior art found:** Tooling limits: my WebSearch budget was already used up, and Semantic Scholar, arXiv, DBLP and support.microsoft.com were blocked by the proxy. GitHub was reachable, so the prior art below comes partly from memory and should be checked before anyone relies on it.
- Why developers disable security features in code, and how long those disables last: Georgiev et al. (CCS 2012) and Fahl et al. (CCS 2012/2013) on turning off certificate validation, mostly dev-time workarounds left in production. Rahman, Parnin & Williams, "The Seven Sins: Security Smells in IaC" (ICSE 2019, TOSEM 2021 extension), which covers disabled certificate validation and how long such smells survive.
- Helm/Kubernetes defaults: Rahman et al., "Security Misconfigurations in Open Source Kubernetes Manifests" (TOSEM 2023). Blaise & Rebecchi, "Stay at the Helm" (2022). Minna, Massacci et al. (2024), Helm chart misconfigurations from Artifact Hub, including missing NetworkPolicy. The "103 of 112 charts allow all traffic" figure is the kind of result these papers already report.
- Switches that never get flipped back: stale feature-flag work, e.g. Piranha at Uber (ICSE-SEIP 2020) and Meinicke et al. (2020). Dependency downgrades: Cogo, Oliva & Hassan (TSE 2019), whose reasons for downgrading overlap heavily with "turned the fix back off".
- Vendor-side delays: Microsoft's own hardening key-dates page already serves as the ledger for Microsoft. Chrome's TLS 1.0/1.1 and SameSite postponements, and its temporary enterprise policies (escape hatches with removal dates), are public and have been studied (e.g. Kotzias et al., IMC 2018, TLS longitudinal study). I know of no academic cross-vendor ledger that codes postponement reasons, so that part is the only clearly new element.
Data checks:
- Bitnami #22934 is real (31 Jan 2024, Redis chart 18.11.0, networkPolicy enabled in a minor release broke the Istio sidecar). The fix, PR #22971 (merged 1 Feb 2024, schema-registry chart), added allowExternalEgress=true "to avoid issues with Istio". So the reopening was a reaction to a reported breakage, not a response to uncertainty.
- GitHub code search: "security-revert" returns 1,452 files, mostly Node's own docs and changelogs, forks and CVE mirrors, so real-world use is small. safe.directory '*' appears in 4,856 Dockerfiles (Bearer, CKAN, Tencent CodeAnalysis and others), typically to work around mismatched user IDs on mounted volumes in containers.
- World of Code needs an approved access application. Software Heritage is open but rate-limited. GH Archive does not carry check-run or status events, and Actions logs expire after about 90 days, so "red CI before the flip" can mostly not be observed historically.

### C4 — One in N: the fate of Linux kernel CVE fixes — breakage, AI-picked vs human-vouched, and fixes that never reach LTS (score 4.38, wounded)

**Best headline:** Linux issued X kernel CVEs in 2025. Z% of the fixes for flaws that affect the 5.10 LTS kernel still shipping in devices never reached it. Of the fixes that did land, 1 in N was later reverted or re-fixed, and fixes pulled in as prerequisites were reverted about 3x as often as fixes their authors vouched for.

**Skeptic's flaws:** 1. It does not test the thesis. Belief 2 needs evidence that enterprises delay because they are unsure what a fix will break. This design measures how often upstream backports break, in a volunteer process with no enterprise, no delay clock and no decision-maker. The candidate says so itself ("does not measure enterprise delay"), and no redesign of this study removes that gap. Enterprises also rarely run stable kernels as-is: they run RHEL, SLES or Ubuntu kernels with their own backports, and for kernels the usual enterprise blocker is reboots and maintenance windows.

2. The headline works against Skylayer. The pilot's revert rates are 0.3–1.0%, which reads as "more than 99% of kernel fixes are safe", the "patches are safe" reading the candidate already fears. The follow-up rate (4.1% vs 11.4%) mostly repeats Yin et al. 2011. And "fix needed a follow-up" is not the same as "fix broke production": many follow-ups finish an incomplete fix rather than repair a regression.

3. The missing-fix measure is contaminated. When a CVE has no Fixes: tag, the CNA marks every version as affected. In my rough 2025 count, 293 of the 845 fixes "missing" on 5.10 (about 35%) had an unknown introduction point, so the bug may never have existed on that branch. Fixes that were backported in a different form, without the upstream hash in the record, also show up as missing. On top of that, the proposed reason codes cannot actually measure uncertainty. "Never attempted" and "failed to apply" are both effort or prioritization. "Dropped after a regression" is breakage after the fact, not doubt before the decision. Doubt before the decision is never measured.

4. The metric definitions are fragile. The pilot says 512 CVEs (3.1%) were introduced by another CVE's fix. Matching any fix commit, including stable-branch backport hashes, I get 1,230 (7.5%). The number more than doubles depending on a definition choice, so a critic can pick apart the headline.

5. The channel comparison is confounded:
- Authors deliberately left AUTOSEL patches untagged, and that choice is itself a risk judgment.
- Stable-dep-of patches are not fixes at all. They are refactors pulled in as prerequisites, often larger, so they break more by construction.
- AUTOSEL candidates pass a public review window in which maintainers can reject them.
- Obscure drivers get fewer bug reports, so their breakage is undercounted, and the bias could go either way.
- The difference-in-differences plan compares against the handful of subsystems that opted out of AUTOSEL. Opting out is a choice those maintainers made, not random, and the LLM change coincides with the CNA's CVE surge and the 6.12 LTS.

6. It will not cut through the noise. Many in the industry already treat kernel CNA CVEs as noise; the sample 2025 record I opened is a tracing warning. The AI-selection angle also points back at a single maintainer's tool, however it is aggregated.

**Prior art found:** Research access was limited. The WebSearch budget was already used up, and the proxy blocked lwn.net, arXiv, OpenAlex, dblp, Semantic Scholar, kernel.org and lore. So the prior art below comes from GitHub, the OSV dump I downloaded, and literature I know well but could not re-check online.

Verified this session:
(1) nluedtke/linux_kernel_cves (GitHub, 754 stars, now archived) tracked CVE fix status for each kernel stream for years.
(2) CIP cip-kernel-sec, the Civil Infrastructure Platform's tracker of which kernel CVEs are fixed in which branch (a fork is on GitHub).
(3) analogdevicesinc/linux-security-vulns builds on Greg Kroah-Hartman's vulns.git. For every patch release of each current LTS/stable kernel, it publishes plots of how many CVEs are still unfixed. That is essentially the "fixes that never reach LTS" arm, already running.
(4) hardenedlinux/kernel-backport-checker (2026) finds CVE fixes that are missing from a given LTS kernel and config.
(5) The OSV Linux dump holds 16,393 kernel-CNA CVEs published 2024–2026 (3,580 / 5,649 / 7,164 by year), so the pilot's scale is right.
(6) My own rough check of 2025 CVEs gives a missing-fix share of about 26% on 5.10 and about 13% on 6.1, in line with the pilot's ~30% and ~15%.

Known literature (not re-checked online):
- Yin et al., "How Do Fixes Become Bugs?" (ESEC/FSE 2011): 14.8–24.4% of post-release fixes in Linux and other OSes were incorrect. This is already the "1 in N fixes breaks" headline.
- Zhang et al., "An Investigation of the Android Kernel Patch Ecosystem" (USENIX Security 2021): measured how fixes travel from upstream to LTS to vendor kernels, and the delays and gaps along the way.
- FixMorph (ISSTA 2021) and TSBPORT: backport failures and security patches missing from old kernels.
- Tian/Lawall/Lo (ICSE 2012) and PatchNet (Hoang et al., TSE): machine selection of stable patches, the idea behind AUTOSEL.
- LWN has covered AUTOSEL disputes repeatedly since 2018 ("Machine learning and stable kernels"), counted stable regressions using Fixes: tags, and covered the 2025 LLM-assisted AUTOSEL. Exact LWN titles unverified.
- Greg Kroah-Hartman and the kernel CNA say publicly that fixes are only guaranteed on supported stable branches and that older LTS kernels miss fixes. That makes a "Z% never arrived" headline expected, not news.

What looks new: comparing breakage by who selected the fix (Cc: stable vs AUTOSEL vs Stable-dep-of) in the CNA era, and scoring how well the LLM-AUTOSEL risk verdicts are calibrated.

### C1 — Proof On, Proof Off: exogenous proof shocks on identical GitHub security fixes (score 4.37, wounded)

**Best headline:** Same security fix, same repo, only the proof changed: across N open-source security PRs, merges rose X% once an outside 'safe' signal appeared, and fixes waited Y times longer when GitHub's scheduled CI outage took the proof away, even though nothing in the code had changed.

**Skeptic's flaws:** 1) The retrospective proof-on arm for Dependabot cannot be built. The compatibility badge is a live image served from dependabot-badges.githubapp.com with no history. GH Archive does not record it, and fetch-metadata writes it only to workflow logs, which expire after about 90 days. You cannot know when a badge flipped on a PR from 2019-2025, so that event study can only be run going forward. The 6-8 week retrospective plan overclaims.

2) A flip cannot be separated from waves of peer adoption. The score is one value per version pair, driven by other repos' CI results. A flip therefore lines up exactly with version-pair × time, so version-pair×day fixed effects are impossible. A score usually leaves 'unknown' because many repos are merging and testing the same fix at once, which is a common attention or urgency shock that also moves the focal maintainer. The sign test does not clear this either: a flip to Low usually means the update really breaks things, so the focal repo's own CI is likely red too.

3) The Renovate 72h design has a contaminated control group and an unobserved first stage. config:recommended already shows the Confidence column for self-hosted users, so 'Mend app vs self-hosted' is not a badge/no-badge contrast. Crossing 72h only lifts a ceiling. Whether and when the badge became High is not stored, which leaves a fuzzy RD with an unknown first stage, i.e. intent-to-treat only. Repos using minimumReleaseAge also get a 'stability' status check that flips at 3 days, and any automerge fires then: a mechanical jump at the same cutoff. Security PRs skip the release-age delay, but repos that mix security and non-security updates still have this check.

4) Proof-off mostly measures a mechanical gate, not uncertainty. With required checks or auto-merge, a brownout-red PR cannot merge at all. The brownout error clearly says it is an infrastructure failure, so no maintainer changes their view of whether the fix is safe. The docs-PR placebo is weak, because docs PRs are often path-filtered and never run CI. Repos still pinned to deprecated images are a selected, neglected population. The 2027 prospective window is only 4 days × 10h.

5) The attention vs deliberation split cannot be measured. GitHub does not log page views, and most bot PRs are merged with no earlier recorded touch. By the stated falsification rule, the delay would look like it happens 'before any human touch' because of missing data.

6) Construct and external validity. OSS maintainers merging dependency bumps, often in dev or lockfile-only dependencies with no one owning the blast radius, are not an enterprise change board patching OS or packages (wedge B). Nulls are ambiguous, since maintainers may simply ignore badges. The likely headline is a single-digit percentage change in merge hazard with wide confidence intervals, not a crisp number that cuts through the noise.

Legality is fine: public data, the GitHub AUP research clause, low-rate public badge GETs, and aggregate results only.

**Prior art found:** Web search was capped mid-task (the session's 200-search budget was used up) and arxiv.org and docs.github.com were blocked, so I checked primary sources on github.com instead.

Confirmed from primary sources:
- actions/runner-images #11101: the ubuntu-20.04 brownouts ran on six days, 4 Mar to 8 Apr 2025, for 8 hours each (13:00-21:00 or 14:00-22:00 UTC). The image was retired on 15 Apr 2025, which is before the Oct 2025 GH Archive payload trim.
- actions/runner-images #14254: the ubuntu-22.04 brownouts are on only four days (23 and 30 Mar, 6 and 13 Apr 2027), each 14:00-00:00 UTC, so 10 hours, not 8. Retirement is 17 Apr 2027.
- dependabot-core #4001: GitHub never disclosed the score threshold or the algorithm.
- dependabot/fetch-metadata: compat-lookup needs a personal access token and returns 0 when the score is unknown.
- Renovate merge-confidence docs: the algorithm is private, and npm cannot get High before it is 3 days old.
- Renovate source code:
  - config:recommended extends mergeConfidence:age-confidence-badges, so Age and Confidence columns also appear for self-hosted users on the default preset.
  - config:best-practices adds security:minimumReleaseAgeNpm. That setting adds a pending, then passing, 'stability' status check at 3 days.
  - The minimum-release-age docs say security updates bypass minimumReleaseAge.

Prior art I know of but could not re-verify here:
- Alfadel et al., MSR 2021, on Dependabot security PRs: merge rates, latency, and why PRs are not merged, including breakage.
- He et al., TSE 2023, a large-scale Dependabot study. It reportedly discusses the compatibility score as mostly unavailable or distrusted by developers.
- Rombaut et al., TOSEM, on the overhead of Greenkeeper bot PRs and CI failures on bot PRs.
- Mirhosseini and Parnin, ASE 2017, comparing badges with automated PRs as drivers of upgrades.
- Trockman et al., ICSE 2018, on repository badges as quality signals.
- A long line of work showing that red CI lowers PR acceptance.

I found no published work that uses runner-image brownouts or the Merge Confidence 72-hour rule as natural experiments. The identification idea looks new. The setting (latency of OSS bot PRs) is heavily studied, and this is essentially a better-identified version of Round-1 idea (a).

### C18 — One apt-get Away: safe-backport lag vs risky-upgrade lag on real servers, and the pay/change/freeze fork at end of support (score 4.36, wounded)

**Best headline:** Of N internet-facing Ubuntu servers whose exact build we could date, X% were missing a security fix that changes no version and installs itself by default. Fixes of that kind needed a regression follow-up only R% of the time. When standard support for 20.04 ended, Y% of actively patched servers moved to extended support, Z% froze, and only W% upgraded. The exception was servers whose app already ran on the newer PHP: they upgraded K times as often.

**Skeptic's flaws:** 1. Neither outcome of the main test can decide the question. On Ubuntu, unattended-upgrades is on by default and installs S patches automatically; R requires a person to act. So 'S current, R stalled' is exactly what a server on autopilot with nobody watching produces. Seeing that pattern is not evidence for belief 2. The opposite result is just as uninformative. Large S-lag has at least three explanations: admins who turned auto-updates off because they fear breakage (which IS belief 2, per the SOUPS 2019/2020 interview studies); containers built from ubuntu:20.04 that only get S patches when someone rebuilds and redeploys; or plain neglect. The pre-registered rule (reject belief 2 if at least 50% of the debt is S-lag) therefore cannot actually falsify anything.

2. R-lag mixes effort with uncertainty. Moving PHP 7.4 to 8.x means real code migration, often known breakage rather than uncertain breakage. The thesis says the blocker is 'not because the fix is hard', but here the fix IS hard.

3. The triple difference is broken by a confound I verified. The Sury PPA deleted its 20.04 builds in May 2025, the same month standard support ended, and Ubuntu ESM does not cover Sury packages. Every Sury host on 20.04 lost its patch channel at once, while distro-7.4 hosts could buy ESM. On top of that, Sury PHP 7.4 still exists for 22.04 and 24.04, so both Sury groups can upgrade the OS without changing PHP at all. The 'proven vs unproven on PHP 8' contrast the design relies on is not what separates the groups.

4. The enroll/upgrade/freeze fork cannot be timed. Enrollment shows up only when the first ESM build installs: August 2025 for PHP and March 2026 for OpenSSH, 3 and 10 months after support ended. Competing-risks hazards of enrollment can't be fitted; at best there is one cross-section.

5. 'Paid backports' is wrong. Ubuntu Pro is free for personal use on up to 5 machines, and many people enroll for Livepatch or FIPS rather than to avoid upgrading.

6. The 'maintained' flag comes from month-to-month Wappalyzer technology changes. That signal is noisy and measures web-layer activity, not whether the OS admin is paying attention. HTTP Archive also tracks pages or origins, not hosts, so load balancers, CDNs, migrations and turnover in the sampled sites break the 'same host, same owner' claim.

7. The sample is biased: it contains only servers still showing the default expose_php, which skews toward unhardened setups.

8. The headline ('X% of sites missing a free fix') is a familiar outdated-software statistic, and a high X points to neglect, which cuts against the thesis. The regression base rate also shows S patches do regress (1 of 3 PHP ESM builds for 20.04 needed a regression fix). Admins who fear them are not obviously irrational, and the design treats S risk as near zero.

**Prior art found:** I hit the session's web-search limit (200 of 200 used), and the proxy blocks dblp, Semantic Scholar, arXiv, ACM, USENIX, NDSS, Censys, Debian's tracker and HTTP Archive's site. So the prior-art list below comes from my own knowledge and is unverified. I checked primary data directly where I could reach it (ubuntu.com notices JSON, Launchpad, raw.githubusercontent.com).

Prior art (from memory, unverified):
- Measuring patch or update lag from banners and crawls is a well-worn area. Examples: Demir, Urban, Wittek, Pohlmann, 'Our (in)Secure Web: Understanding Update Behavior of Websites and Its Impact on Security' (PAM 2021), which measures website software update lag from multi-year HTTP Archive data; Tajalizadehkhoob et al., 'Herding Vulnerable Cats' (CCS 2017), header-reported PHP and Apache versions per hosting provider, with backporting noted as a problem; Vasek and Moore on webserver compromise risk factors from headers; Van Goethem et al. (2014) on outdated PHP exposed via X-Powered-By; Durumeric et al., 'The Matter of Heartbleed' (patch curves); Kotzias et al., 'Mind Your Own Business' (NDSS 2019).
- Deciding whether a host is patched from its Debian/Ubuntu revision string is standard practice. Censys, Shadowserver and Qualys did it for OpenSSH regreSSHion and Terrapin.
- Interview work (Li et al., 'Keepers of the Machines', SOUPS 2019; Tiefenau et al., SOUPS 2020) reports admins turning OFF automatic updates for fear of breakage. That directly undermines this design's falsification logic (see flaws).
- New in C18: the split between S (backport, no version change) and R (release or upstream upgrade), and counting ESM enrollment vs upgrade at 20.04 end of standard support. The second part is essentially a publicly observable version of P1 'Fear Tax'. The S-patch regression base rate overlaps P5 and round-1 (c).

Data checks:
- Ubuntu notices API works. For 20.04, php7.4 had ESM builds 7.4.3-4ubuntu2.29+esm1 (2025-08-21), +esm2 (2025-09-04, which is a REGRESSION fix, USN-7648-3) and +esm3 (2026-01-12). Several 2026 PHP USNs (8336, 8513, 8564, 8734, 8743) list no 20.04 php7.4 fix.
- OpenSSH on 20.04: last free build 0ubuntu0.13 (2025-04-24). The first ESM build, +esm1, arrived only 2026-03-12, then +esm2 and +esm3 in Sept 2026.
- Crude base rate: a notices search for 'regression' returns 151 of 2996 notices for 20.04 and 84 of 2573 for 22.04, roughly 3–5%.
- Launchpad shows Ondřej Surý's PHP PPA (the 'Sury' source) stopped building for 20.04 at 8.3.21 (2025-05-09). Those 20.04 packages are marked 'Deleted'. The PPA now serves only 22.04 and 24.04.
- HTTP Archive's dataform crawl.requests and crawl.pages definitions exist (partitioned by date, clustered by rank). I did not verify how complete historical header coverage is.

### P2 — Qualification Yield: medical/OT vendor proof gates, what they catch, and whether installs wait for them (score 4.35, wounded)

**Best headline:** Medical and OT vendors cleared X% of N Windows security patches with no break found. Each clearance still took a median of Y days, and device installs jumped Z-fold in the week the 'validated' notice arrived.

**Skeptic's flaws:** 1. The key data (the 'installs rise Z% within 14 days' arm) probably does not exist in usable form. It needs device-level install times, per KB, across hospitals. Claroty, Armis and Asimily see mostly passive network data. They get patch level only through integrations with Windows management tools (SCCM, Intune), and vendor-locked medical devices usually aren't enrolled in those. Their customer contracts limit sharing, and a seed-stage startup is unlikely to get a data-use agreement for a stunt. Without this arm there is no 'Z', no isolation, and the project collapses to P2 with a yield column.
2. It measures permission, not uncertainty, and the vendor often installs the patch itself. Hospitals are forbidden by contract, warranty and regulation from installing unvalidated patches, and on many modalities the manufacturer pushes the patch through its own remote service or at service visits. So a jump in installs at validation is mechanical: the vendor's release pipeline, not a hospital's uncertainty being resolved. It is equally what the coordination/permission explanation predicts. The stated falsification test (a jump means proof; no jump means coordination) is therefore mis-specified: a jump does not discriminate between the explanations. A Skylayer-style third-party proof also cannot legally replace the manufacturer's validation under FDA's quality-system rules (21 CFR 820), so even a positive result does not show the market will accept outside proof.
3. The dates are too coarse. Public bulletins are overwritten lists. Wayback captures of vendor pages are sparse (months apart), and pages behind logins are never captured. That error of weeks is the same size as the lag being measured, which breaks both the lag distribution and a 14-day event window. Portals were also re-platformed (Rockwell's knowledge base, GE's move to securityupdate), so '10 years' is really about 3–6 years for 2–4 vendors.
4. 'Yield' is selection-biased and tiny. Many vendors list only approved updates. Failures show up as 'approved with exceptions', footnotes or silent version pins. With cumulative updates since 2016, the unit is one update per OS per month, so you get perhaps 10–40 breaks in total. That is too few to train or score the proposed time-split failure prediction, and a cumulative update touches thousands of files, so 'files each KB changes' carries almost no signal. The lab arm also needs licensed OT and medical software whose licences typically forbid benchmarking and reverse engineering, and much medical software cannot be bought at all.
5. Lag likely follows a fixed monthly batch cadence (Siemens, ABB and Rockwell validate one to three weeks after Patch Tuesday). Regressing lag on patch risk will probably return nothing, and 'Y days' is then just a release schedule.
6. The likely outcome undercuts the stunt. Vendor validation takes about 2–4 weeks, while hospital installs lag by months or years (devices still on Windows 7 and Windows 10 LTSC, installs done at scheduled service visits). So the post-validation wait probably dominates, which falsifies belief 2 in Dissanayake's favour. That is honest, but it is not the viral headline.
7. The MAUDE ratio of update-caused to attacker-caused events is set by reporting rules, not by real risk. Manufacturers must report malfunctions, while hospital-network ransomware rarely produces a device report, so any critic will dismiss it. Its headline ('updates harm patients more than hackers') also argues against patching urgency.
8. FDA recall termination dates are administrative closures, not install completion, so 'time to close' measures FDA paperwork.
9. On legality: the public documents, MAUDE, recall data and MDS2 forms are fine. Harvesting bulletins behind logins with a customer account for publication likely breaches the portals' terms of use, so those vendors must be excluded unless they give permission.

**Prior art found:** I could not verify anything live. The WebSearch budget for this session was already used up (200/200), and the egress proxy blocked every source I tried to fetch: Semantic Scholar, OpenAlex, the arXiv API, archive.org, api.fda.gov, securityupdate.gehealthcare.com, rockwellautomation.custhelp.com, support.industry.siemens.com and philips.com. Everything below comes from background knowledge. Following the "lean harsher" rule, I scored the unverified data claims as unproven.
(1) Dissanayake, Zahedi, Jayatilaka and Babar, 'Why, How and Where of Delays in Software Security Patch Management: An Empirical Investigation in the Healthcare Sector' (CSCW 2022). This is a longitudinal case study inside a healthcare organisation. It already names dependence on vendors and waiting for vendor approval as delay causes, and files them under coordination and socio-technical factors, not uncertainty. So the qualitative claim is already published, and in the rival framing.
(2) The manufacturer-approval gate itself is long documented. FDA's 2005 guidance on off-the-shelf software in networked devices and the 2016 postmarket cybersecurity guidance both put patch validation on the manufacturer. MDS2 (HN 1-2019) has a CSUP section on installing third-party patches. The SHTI 2025 MDS2 corpus the candidate cites suggests Arm 1 (the MDS2 census) may already be published, or is a trivial extension of it.
(3) The FDA-recall and MAUDE arms are well-trodden. Examples: Alemzadeh et al. 2013 (safety-critical computer failures in FDA recalls); Ronquillo and Zuckerman 2017 (software-related recalls); several MAUDE analyses of cybersecurity reports.
(4) Industry reports (Claroty Team82, Armis, Forescout healthcare/XIoT) already publish legacy-OS and unpatched-device rates in hospitals. OT consultancies (Verve, Industrial Defender) and SANS ICS surveys already report 'waiting for vendor approval' as a top barrier. Those are survey or anecdote, not a dated ledger.
(5) The vendor bulletins probably exist, but many are behind logins. Rockwell KB 35530 (Microsoft Patch Qualification) is largely behind a TechConnect login. Emerson DeltaV (Guardian), Honeywell, Schneider/Foxboro and Varian (myVarian) are portals that need a login. Siemens SIOS entry 18752994 (PCS 7/WinCC compatibility), ABB's monthly 800xA third-party update validation status and some Yokogawa, Philips and GE HealthCare pages are likely public, but they often show only the current list.
What is new: a multi-year, dated, cross-vendor ledger of qualification lag plus yield (the share of updates a vendor did not qualify or restricted). I found no evidence it has been published. This candidate is also mostly the round-2 P2 'Qualification Clock' with a yield metric and an event study added.

### C19 — Same Fix, Different Wrapper: disclosure vs relabel shocks, and fixes maintainers can't ship without breaking users (score 4.3, wounded)

**Best headline:** Same fix, new label: re-shipping a security fix as a patch release moved X% of stuck dependents within a week, while the advisory itself moved only Y% in 30 days. Z% of the holdouts' own test suites already passed on the fixed major version.

**Skeptic's flaws:** 1. The "relabel" shock does not isolate perceived risk. A backport to a patch release changes several things at once:
- It removes real breaking changes. The major often raises the engines field (semver 7 dropped old Node), and Maven backport lines exist because newer lines need a newer JDK (log4j 2.12.x and 2.3.x).
- It makes the fix reachable through version ranges: caret and tilde ranges pick it up on a fresh install, and `npm audit fix` applies it without `--force`.
- It fires the tooling again. GHSA updates its patched-versions field, so Dependabot, npm audit and scanners flip from "no fix in your range" to "fix available" and open new PRs. That is a second awareness shock and a convenience shock.

So "the relabel moved people and the advisory didn't" is predicted just as well by effort, defaults and automation, which are the rival explanations belief 2 has to beat. The falsification test is lopsided. Its failure condition ("relabel moves no one") can also happen mechanically: minimist 0.2.4 falls outside the `~0.0.1` range old dependents like optimist declare. Neither outcome tells impact uncertainty apart from speed or tooling.

2. "Fix held constant" does not hold across the horse race. The disclosure regression discontinuity runs on silent fixes that were already out as patches. By then caret users have moved, leaving pinned, abandoned, mirror and CI-cache traffic, so disclosure looks weak because of who is left. Within the same fix, the advisory arrives while only a costly major exists. So the two shocks come from different fixes, different populations and different costs.

3. The test oracle is weak proof. Tests catch only about half of the faults dependency changes introduce (Hejderup & Gousios). Rebuilding old npm test environments is fragile, and many packages have no tests or failing ones. A dependent whose tests would have passed but who never tried is showing inattention as much as fear.

4. Data gaps:
- npm offers per-version downloads only for the last week. The 307 npm backport events cannot be measured as installs in hindsight, only through dependents' published manifests. Few npm packages exact-pin, so that sample is small and self-selected.
- Maven has no public download data.
- PyPI and crates.io downloads are dominated by CI and mirrors.
- After weighting by dependents, the usable events are probably a few dozen, dominated by a handful of hub packages.

5. Backport timing is endogenous. Backports follow user demand, pressure from a big dependent, or a change of maintainer (the minimist backport came about 340 days later, after a maintainer change). The adoption spike can come from one hub dependent releasing and fanning out.

6. Relevance and novelty for Skylayer:
- This is developer behaviour in open-source library ecosystems, not enterprise change control over OS or container patches in production.
- In this domain "proof" is already productised (Merge Confidence, Dependabot compatibility score, Seal/Endor/HeroDevs backports), so the headline reads as SCA-vendor marketing. It says little about Skylayer's moat.
- The upstream count of "N trapped fixes" will be dominated by abandoned packages. The 700/1,516/1,116 no-patched-version advisories are mostly unmaintained packages, not fixes blocked by unreleased breaking changes.

**Prior art found:** Web search was used up and most scholarly domains were blocked by the proxy (arXiv, Semantic Scholar, Springer, Crossref, OpenAlex, dblp). I checked what I could against GitHub and the package registries. Paper findings marked "from memory" are not re-verified.

Verified here:
- semver: 7.5.2 was published 2023-06-15 and the 6.3.1 backport on 2023-07-10, so 25 days (npm registry).
- minimist: 1.2.6 was published 2022-03-22 and the 0.2.4 backport on 2023-02-25, about 340 days (npm registry).
- crates.io keeps a historical per-version download archive (static.crates.io/archive/version-downloads; for example 2020-01-01.csv returns 200).
- Decan et al. published a replication package for their backporting study, github.com/AlexandreDecan/secos-backports, with a "Backported updates" notebook and a "Vulnerabilities" notebook. It was archived in November 2025.
- Renovate's Merge Confidence scores each update by Age, Adoption (share of Renovate users already on it) and Passing (share of updates with passing tests). It is a commercial crowd-sourced "proof this update is safe" for exactly this domain.

Close prior art, from memory:
- Decan, Mens & Constantinou (MSR 2018), npm vulnerabilities: dependents' version constraints often block fix adoption, and fixes shipped as patches propagate more easily.
- Decan, Mens, Zerouali & De Roover, "Back to the past: analysing backporting practices in package dependency networks" (IEEE TSE 2022): backports are rare, mostly go to the previous major, and security is a main driver. This is the descriptive version of step 2.
- Chinthanet et al., "Lags in the release, adoption, and propagation of npm vulnerability fixes" (EMSE 2021): fix releases are bundled with unrelated commits, and adoption is faster when the fix ships as a patch. This is the direction of the headline, shown descriptively.
- Imtiaz, Khanom & Williams, "Open or Sneaky? Fast or Slow? Light or Heavy?" (TSE 2023): time from fix commit to release, how much is bundled into security releases, silent fixes, and how long advisories lag. This overlaps steps 1 and 3.
- Maven ecosystem: Wu et al. (ICSE 2023) on upstream vulnerabilities, where fixed versions are incompatible downstream, and Zhang et al. (ASE 2023, "Ranger") on vulnerabilities that persist because fixes exist only in versions downstream code can't take.
- Pashchenko et al. (ESEM 2018): dependencies that can only be fixed with a major upgrade.
- Hejderup & Gousios (JSS 2022), "Can we trust tests to automate dependency updates?": test suites catch only about half of faults introduced through dependencies. This undercuts the lab oracle.
- Kula et al. (EMSE 2018) on developers not updating dependencies.
- Alfadel et al. on silent fixes in PyPI.

Industry, also from memory:
- Dependabot compatibility score.
- Seal Security, HeroDevs NES, Endor Labs patches and upgrade-impact analysis, and TuxCare. All sell backports on the "the fix is trapped behind a breaking upgrade" story.

The genuinely new part is the causal horse race on the same fix plus the test-oracle subset. The direction of the headline is already published descriptively.

### C16 — Change Control on the Record: trust-score cutoffs, vulnerability-to-change tickets and outsourcing penalties (score 4.29, wounded)

**Best headline:** Security patches spend X% of their lead time waiting for someone to sign off that they're safe. Teams just below the score where ServiceNow stops auto-trusting them wait N days longer for the same fix, and their changes fail no less often (Y orgs, Z tickets).

**Skeptic's flaws:** 1. The centerpiece dataset may not exist. The RD only works if partner enterprises actually route approvals on Change Success Score cutoffs. The proposal admits few do, and I found nothing showing any do. Even with such partners, the analysis needs security-remediation changes that land near a team-level cutoff, carry CVE fixed effects, and are frequent enough to fill a bandwidth. That data is extremely thin, and one ticket often bundles hundreds of patches (monthly patch-window changes).
2. The RD does not isolate impact uncertainty. A jump at the cutoff shows the cost of an approval queue, and most of that is mechanical process time: weekly CAB cadence, approver availability, maintenance windows. It says nothing about fear of breakage. The 'is it safe?' reading is assumed, not measured. A critic will say, correctly, that the finding is 'bureaucracy adds latency', which is DORA's point and fits belief 2 being false (process and speed, not uncertainty).
3. The running variable is endogenous. The score moves in discrete jumps driven by past failures (+3/−2/−5/−10). Teams just below a cutoff have just had failures, which brings post-incident scrutiny, problem management and freezes. That breaks RD continuity. Discrete, heaped scores also make the McCrary density test unreliable. Teams can also game the score through how they record outcomes and route to assignment groups.
4. 'Fails no less often' rests on incident.caused_by and change-outcome coding. Those fields are notoriously incomplete, and the score is computed from the same fields, which makes the result circular.
5. The DiD on converting templates to standard changes is close to tautological. Standard changes skip approval by definition, and templates are converted because they already rarely fail. Selection explains both the lead-time drop and the unchanged failure rate.
6. The FOIA leg for ticket data will probably be withheld. Most state records laws exempt IT security and vulnerability information, for example Texas Gov't Code 552.139 and California's information-security exemption. Agencies are also often not required to build new database extracts. Timelines of AG rulings plus months make the 3 to 9 months / $10–50k estimate optimistic.
7. The contract census is legal and new, but it is an incentive argument, not causal evidence. Many SLAs also exclude outages during approved change windows, which could undercut the 'breaking production costs the vendor K×' premise.
8. Outsiders cannot reproduce the RD (private partner data), so it lacks the crisp, checkable single number the reference post had.
Legality and ethics look fine: partner data under agreements, lawful records requests, public contracts, aggregate reporting.

**Prior art found:** What I could check was limited. The WebSearch budget was already used up and the proxy blocked servicenow.com, dora.dev, Wikipedia, arXiv, Crossref and Semantic Scholar, so most items below come from my own knowledge and still need checking.
(1) I confirmed GitLab's public change tracker (gitlab-com/gl-infra/production). The API shows about 2,976 issues labelled 'change'. A search for CVE returns only 4, of which 3 are security changes: PG 16.6 minor upgrade C1 in prod, 32 days from issue to close; the same upgrade in staging, 118 days; Git 2.36.1.gl1 for CVE-2022-24765, 19 days. GitLab rates changes C1 to C4 and does not use ServiceNow scores. The pilot can therefore test neither the RD nor any statistics.
(2) Accelerate (Forsgren, Humble and Kim, 2018) and the State of DevOps 2019 report already published the headline claim: external change approval (a change advisory board, CAB) goes with longer lead time and lower throughput, and has no link to change failure rate. That finding comes from surveys, not administrative data, but it takes away the surprise of 'waits N days longer and fails no less often'.
(3) Dissanayake et al. (CSCW 2022, 'Why, How and Where of Delays in Software Security Patch Management', healthcare sector) already broke down the patch clock stage by stage using archival tickets and emails, and found that coordination and dependencies dominate. Step 2 largely repeats this at larger scale.
(4) The BPI Challenge 2014 dataset (Rabobank ITIL changes, CIs and incidents caused by changes) is already on the round-2 list and has many papers on change-impact prediction.
(5) ServiceNow already sells the 'machine-issued credential' idea as Change Success Score, Change Approval Policies, DevOps Change Velocity (automated approval from pipeline evidence) and Predictive Intelligence change risk. The vendor makes its own claims about shorter approval times, so a positive result mostly supports ServiceNow, not Skylayer.
(6) Ponemon and ServiceNow's 'Costs and Consequences of Gaps in Vulnerability Response' (2019) is a survey reporting time lost to cross-team coordination.
(7) Industry research on change risk and failure prediction exists, for example IBM Research ticket-mining papers and Microsoft Gandalf (NSDI 2020).
I found no prior census of outage-versus-late-patch penalty ratios in public outsourcing contracts. That component looks new.

### P6 — Forgotten Box or Deferred Decision? Breach-linked decomposition of the fix on the shelf (score 4.28, wounded)

**Best headline:** On the day a ransomware gang posted them, X% of N victims still had an internet-facing device with a ransomware-linked KEV whose fix had been public for a median Z days. Among victims with several such devices, W% had not patched a single one. 30 days after being posted, V% were still unpatched.

**Skeptic's flaws:** 1. DEFERRED doesn't mean uncertainty, so the study can't support belief 2.
- A fleet where no box was patched but an earlier upgrade was seen is equally explained by: no staff, change windows, an MSP contract that doesn't cover it, a missed advisory, an expired support contract (Fortinet, SonicWall and Palo Alto firmware downloads need an active contract, a big factor for small firms), end-of-life hardware that can't take the fix, or budget.
- A past upgrade proves the org could upgrade once, not that it knew about this fix now.
- The only test aimed at uncertainty is the fix-path risk code (branch jump, known-issue build, reboot without HA). Branch jump and reboot are effort just as much as risk. Nearly every Fortinet and PAN-OS build ships a 'known issues' list, so that code has almost no variation.
- Net effect: the design can falsify belief 2 (if FORGOTTEN wins), but a DEFERRED result can't confirm it. Critics will read DEFERRED as 'too busy or too cheap'.

2. The core measurement mostly doesn't exist in passive history.
- Exact firmware versions aren't in banners for FortiOS, PAN-OS, SonicOS or Ivanti. Researchers infer them from static-asset hashes or ETags fetched on specific paths, and historical scan corpora usually didn't store those paths. Citrix (Fox-IT hashes) and Exchange OWA build paths are the realistic exceptions.
- Hotfixes and mitigations often look the same as upgrades, or as nothing.
- Mapping victims to devices by certificate CN/SAN misses the many small firms whose VPN portals use default self-signed certs, which biases the sample toward larger, more mature orgs.
- Fleets with several visible boxes of one model are rare, and HA pairs sit behind one address and get patched together. The sibling test will have small, mechanically biased cells.

3. Timing and selection confounds.
- The leak-site listing date isn't the breach date: listing comes days to weeks after intrusion, and paying victims are never listed.
- After a breach, 'unplug fast, upgrade slow' is explained by forensic holds, insurer or incident-response rebuild plans and replacement lead times, not fear of breakage.
- Exposure is not a proven entry vector.

4. Data access and terms of service.
- Censys Research Access is, as I recall, for academic and non-commercial researchers. A startup running a marketing study probably doesn't qualify.
- Commercial Censys or Shodan historical licences are expensive and restrict publication.
- Shadowserver data goes to network owners and national CERTs, not to third-party researchers.
- ransomwatch may no longer be maintained, and ransomware.live has API terms.
- There's also a contradiction: the 30-days-after-listing metric pulls toward near-real-time tracking, but the plan only uses cohorts at least 6 months old.

5. The breach-notice arm is too thin. State AG notices, HHS OCR entries and SEC 8-K Item 1.05 filings rarely name a CVE. The few that do are skewed toward MOVEit-style third-party events, which the plan codes separately anyway.

6. The headline numbers (Y% ran a KEV, median shelf time Z) are old news given DBIR, Coalition and Fox-IT. Only the W% sibling number is new, and its N will be small.

**Prior art found:** Caveat first: I couldn't check anything live. The web-search budget was already used up, and the proxy blocked arXiv, Semantic Scholar, OpenAlex, dblp, Censys, Fox-IT, ransomware.live, CISA and the GitHub API. Everything below comes from memory and should be spot-checked before anyone relies on it.

(1) Fox-IT and NCSC-NL, "Approximately 2000 Citrix NetScalers backdoored" (Aug 2023). They fingerprinted NetScaler versions and found most backdoored boxes were already patched but still compromised. That is exactly the 'share breached after patching' arm for Citrix. Shadowserver and CISA published similar patched-but-compromised tracking for Citrix Bleed and Ivanti Connect Secure (2024).

(2) Verizon DBIR 2025 edge-device analysis, built on partner scan data: only about 54% of edge-device vulnerabilities were fully fixed, with a median of about 32 days. That already covers the 'shelf time of edge KEVs' number.

(3) Studies linking exposure to losses:
- Coalition Cyber Claims Reports 2024/2025: firms with an exposed Cisco ASA were about 5x more likely to file a claim, Fortinet about 2x.
- At-Bay InsurSec reports: self-managed VPN correlates with ransomware.
- Marsh McLennan Cyber Risk Analytics Center (2023): security controls vs incidents.
- BitSight (2021): firms with a poor patching grade were about 7x more likely to be hit by ransomware.
Between them they pre-empt the 'Y% of victims ran a KEV' headline and its case-control framing.

(4) Academic: Dissanayake et al. CSCW 2022 (coordination delay); Li & Paxson CCS 2017 (patch lifecycle); Durumeric et al. IMC 2014 (Heartbleed patch decay); Exchange ProxyLogon/ProxyShell patch-decay measurements; TU Delft work that uses leak-site and police victim data (Meurs, van Eeten et al.).

What I found no prior art for: the sibling-based FORGOTTEN vs DEFERRED split of breached fleets, and the post-listing patch vs remove vs replace event study. Those two parts look new.

### P5 — Call the Blast: pre-registered per-dependent breakage forecasts scored against Ubuntu's own CI (Patch Weather, upgraded) (score 4.17, wounded)

**Best headline:** Before any test ran, we published which of N dependent packages each Ubuntu update would break. Testing only the X% we flagged caught Y% of the real breakages, and Z% of the test failures that held updates back passed on a plain retry with nothing changed.

**Skeptic's flaws:** 1) WRONG PIPELINE FOR THE THESIS. The Ubuntu security pocket skips proposed-migration: CVE fixes for stable releases are built in the security PPA and published directly. What this CI mostly gates is devel-series uploads and SRUs, which are mostly upstream bumps. The security numbers would come from a small backtest sample of devel/SRU uploads that carry CVE patches. Comparing security-only patches with upstream bumps is also apples to oranges: a CVE-only patch is small by construction, so of course it breaks less.

2) THE MEASURE IS NOT PRODUCTION BLAST RADIUS. Whether a reverse dependency's autopkgtest passes or fails is a proxy for distro-internal compatibility, not for breakage in an enterprise workload. The Hejderup & Gousios result suggests tests miss most dependency faults. The "test everything (the CAB default)" baseline is a straw man, because enterprise change boards don't run distro reverse-dependency tests at all. A CISO or CIO will read "we predicted which Debian package tests fail" as release-engineering trivia.

3) THE LABELS ARE UNRELIABLE AND BIASED TOWARD "FALSE ALARM".
   - autopkgtest.db stores only the tested package's version and the triggers. It does not store the full testbed. A "retry pass with identical versions" can't be confirmed, because the release pocket moves between runs.
   - Retries often add triggers or fixing packages. That resolves a real breakage by co-migration, not a flake.
   - force-badtest is often applied to real regressions that were accepted or already known, not only to broken tests.
   So the "Z% vanished on retry" figure is inflated unless every case is checked against its Swift testbed-packages artifact. I could not verify that those artifacts are reachable or kept for 2017–2026.

4) BASE RATES MAKE THE HEADLINE CHEAP. Nearly all tests pass. Failures cluster in chronically flaky or always-failing tests and a few large transitions (default Python, gcc, glibc, perl). A history-only baseline will likely get most of the recall, so "misses per 10,000" looks impressive mostly because the base rate is low. The real test is lift over history-only, and it may be small.

5) IT DOES NOT ISOLATE BELIEF 2, AS THE PROPOSAL ADMITS. The "blocked by flaky proof" delay happens inside Ubuntu, is often measured in hours, and is already handled by bulk retries. It shows that gate noise delays migrations, not that enterprises hold patches because they fear breakage. It can't falsify the belief against coordination delays or unknown assets either.

6) WEAK HEADLINE. It carries three numbers aimed at release engineers, which is the opposite of the one-crisp-number MCP style the brief asks for. A skeptic's summary would be: "Google and Facebook did this in 2017–19. Ubuntu tests are flaky, which everyone knows."

7) TIMING RISK. Today is 2026-09-26, so 26.10 is in final freeze and upload volume is low. A window after the archive reopens for 27.04 would be dominated by mass syncs from Debian (upstream bumps), not security fixes.

**Prior art found:** Caveat: the web-search budget for this session was already used up, and dblp, Semantic Scholar, OpenAlex, arXiv and Google Scholar are all blocked by the proxy. So I could not run a live literature search. The prior art below comes from my own knowledge and has not been re-checked. I did verify the data sources directly.

DATA, VERIFIED:
- autopkgtest.ubuntu.com/static/autopkgtest.db exists and updates about every minute. The ETag suggests it is about 1.7 GB. I read its schema from the first 128 KB of the file:
  - result(test_id, run_id, version, triggers, duration, exitcode, requester, env)
  - test(id, release, arch, package)
  - current_version(...)
  - It has rows going back to trusty.
- Historical update_excuses archives exist per release, back to saucy/utopic (2014–15), at ubuntu-archive-team.ubuntu.com/proposed-migration/update_excuses/. Live update_excuses.yaml.xz and update_excuses_by_team.yaml are there too.
- The OSV Ubuntu all.zip returns 200.

DATA, NOT VERIFIED:
- git.launchpad.net (britney hints-ubuntu) and ci.debian.net return 403 from this proxy. I believe both are public.
- Swift artifact storage (objectstorage.prodstack5) also returns 403. That matters because it holds the per-run testbed-packages lists the labels would need (see below).

PRIOR ART (from knowledge, unconfirmed):
1. Predictive test selection is established industry work. Machalica et al., ICSE-SEIP 2019 (Facebook): caught more than 99.9% of faulty changes while running about a third of tests. That is essentially this project's headline ("cleared X% of the blast radius with Y misses"). Memon et al., ICSE-SEIP 2017 (Google TAP) predicted test outcomes from dependency-graph distance and flake history, the same features proposed here.
2. Blast radius on Debian's package graph was studied by the Mancoosi/Di Cosmo group: Abate et al., "Strong dependencies between software components" (ESEM 2009), on how sensitive packages are to a change, and "Learning from the future of component repositories" (CBSE 2012), which predicts which upgrades break other packages. Their unit is installability, not tests.
3. The "vanished on a plain retry" statistic is well documented: Luo et al. FSE 2014; Labuschagne et al. 2017 (Java CI failures, a share of them flaky); Durieux et al. ICSME 2020 (35M+ Travis jobs, restarted builds often change outcome); Olewicki et al. ICSE 2022 (brown/flaky builds). Ubuntu itself already has tooling for this: the retry-autopkgtest-regressions script, britney's "always failed" handling, the force-badtest hints, and autopkgtest's "Restrictions: flaky". To Ubuntu developers the phenomenon is routine.
4. Hejderup & Gousios, JSS 2022, "Can we trust tests to automate dependency updates?", found that tests catch only a minority of injected dependency faults. That weakens the claim that a passing test proves a change is safe.

I found no paper that does per-dependent autopkgtest forecasting with pre-registered, timestamped live predictions, so that part appears new. The mechanism and the flakiness finding do not.

### C15 — The Cause Column: what auditors and regulators recorded as the reason fixes weren't applied (score 4.13, wounded)

**Best headline:** Auditors have to write down why a fix wasn't applied. Across N audit findings on unpatched systems (FY2016-2025), the recorded cause was "the fix might break a system or wasn't vendor-certified" in X% and "nobody knew the asset existed" in Y%. The "might break" findings came back the next year Z times as often as matched non-technical findings.

**Skeptic's flaws:** 1. Wrong part of the audit. A cross-validation check in FAC's code rejects any findings-text reference number that is not declared in the Federal Award Audit Findings (Uniform Guidance) workbook. So the structured findings text covers only compliance findings on federal award programs, tagged by compliance requirement letter. Patching and IT-control findings normally sit in the financial-statement (GAGAS Section II) findings, which appear only in the report PDFs. The headline number would need hundreds of thousands of PDFs parsed, and the relevant findings may number only in the hundreds. The '40k audits/year' figure overstates the usable N by orders of magnitude, and a 2–3 week pilot is optimistic.
2. The cause text for security findings is often withheld. By my own recollection (not checked this session), GAGAS lets auditors leave sensitive details out of the public report, and state auditors and IGs routinely send IT security findings to management in confidential letters, publishing only a stub ('details communicated separately'). The public sample is therefore biased toward generic, non-sensitive findings, which is exactly where the real reasons are lost.
3. The measuring instrument leans away from 'fear of breakage'. As I recall, GAO's guidance on cause lists poorly designed policies, flawed implementation, and factors beyond management's control, and says elements need be developed only 'to the extent relevant and necessary'. My recollection (unverified) is that 2 CFR 200.516(b) does not explicitly require a cause either, so the pitch's 'auditors must write down why' is overstated. Causes are written in internal-control language ('did not have procedures to ensure timely patching'). 'Process/governance/boilerplate' will win by construction. The '<10% means falsified' rule could then fire because the instrument cannot see the cause, not because it is absent. The test is falsifiable in form but not a valid test.
4. The cause is not independent. Auditors usually take it from management's explanation and rarely check it, and audit firms reuse templates. It records excuses, not causes, which is the same weakness as the round-2 'excuse ledger'. Auditees also have reasons to cite resources or vendor certification.
5. The categories are hard to separate. 'Legacy system can't be patched' mixes up no fix available (end-of-life), migration cost, and genuine impact uncertainty. Expect low agreement between coders on exactly the category that matters.
6. The persistence test is confounded. Patch findings come back every year because new vulnerabilities keep arriving, so a repeat flag does not mean the same fix was never applied. The placebos (training, account recertification) recur at different base rates, and agency fixed effects cannot correct for differences between finding categories. Within patch findings, the cause is tied to the type of system (OT/medical/legacy), which drives persistence on its own.
7. Wrong population and weak headline. State and local governments, nonprofits and federal agencies are short of resources, so 'resources' will dominate, and they tell us little about the target (FDA-regulated medtech). The result is a text-classification percentage with no organisations named: nothing like the '179 servers, 147 open' style of claim, and easy to dismiss as 'auditor boilerplate'.
8. At most it shows which reason was written down. It does not show that uncertainty causes delay.

**Prior art found:** My web-search budget was already used up when this check started, and fac.gov, gao.gov, oversight.gov, ecfr.gov, openalex and semanticscholar were all blocked by the proxy. So I could not run a fresh literature search, and the prior-art claims below come partly from memory. What I could check directly was GSA's FAC source code on GitHub (raw.githubusercontent.com/GSA-TTS/FAC, backend/dissemination/api/api_v1_1_0/create_views.sql and backend/audit/cross_validation/check_ref_number_in_findings_text.py).
(1) Closest prior art in this tournament: C15 is largely the round-2 ideas 'excuse ledger', 'compelled-reason legal corpus', 'FOIA change logs' and P7 'Deviation Files' applied to a new source (audit findings). It does not explain why it is better than them.
(2) Accounting research (from memory): studies have coded SOX 404 IT material weaknesses using the Audit Analytics taxonomy (Klamm & Watson 2009; Stoel & Muhanna 2011; Li, Peters, Richardson & Watson 2012). There are also studies of repeat single-audit findings, and GAO single-audit oversight reports such as GAO-17-159. These show that cause/finding text mining is established. I know of no published coding of patch-finding causes specifically, but I could not confirm that.
(3) GAO and DoD OIG cyber summary reports already group recurring weaknesses. GAO's standard 'underlying cause' is 'agencies have not fully implemented their information security programs', which is itself an example of the governance-framing problem described below.
(4) Admin-behaviour studies that are not technical evidence but already support 'fear of breakage': Li et al. 2019 'Keepers of the Machines' and Tiefenau et al. SOUPS 2020. Dissanayake et al. CSCW 2022 found coordination delays dominate.
Data verified from FAC code: findings, findings_text and corrective_action_plans exist with is_repeat_finding and prior_finding_ref_numbers. There is no structured cause field; finding_text is one free-text field per finding.

### C14 — One-Way Doors: coding every exploited-flaw fix for reversibility and breakage risk, and whether ransomware shops for scary patches (score 4.05, wounded)

**Best headline:** X of N enterprise flaws CISA confirmed exploited since 2023 can only be fixed by an update the vendor's own documentation says cannot be cleanly rolled back, and 0 of N vendors say so anywhere a patch tool can read it.

**Skeptic's flaws:** 1) The design never measures delay. The claimed chain is: documented breakage risk leads defenders to defer, and deferral leads ransomware crews to pick the flaw. The middle step, deferral, is only an optional mediator, and Shadowserver's per-CVE data is aggregate-only and covers just a few appliance CVEs. What remains is a correlation between what vendors write in their docs and a flag CISA assigns. That does not show delay, let alone delay caused by uncertainty.
2) The arrow can run the other way. A flaw exploited in the wild, especially an edge-device zero-day, triggers a rushed out-of-band fix. Rushed fixes are exactly the ones that come with known issues, pulled builds and a "fix for the fix" within 30 days (often a bypass that is itself a new CVE, and sometimes a new KEV entry, so the rows are not independent). So the fix traits are partly caused by exploitation interest, not the other way round. The planned placebo ("fix traits must not predict zero-day status") will probably fail for this mechanical reason. The study would then call itself falsified for the wrong reason, which is uninformative either way.
3) Irreversibility is really a proxy for "edge appliance". Firmware anti-rollback and configuration loss on downgrade are properties of whole product classes, and ransomware initial access clusters on internet-facing appliances because they are exposed, not because their patches are frightening. Vendor fixed effects remove this, but they also remove nearly all the variation in reversibility: every FortiOS fix is the same firmware upgrade with the same downgrade caveat, and every SharePoint update is non-uninstallable. My calculation from the KEV catalog: after dropping consumer and mobile vendors, about 672 rows and 140 ransomware events since 2023. Only 35 vendors have both flagged and unflagged entries, covering 424 rows and 107 events, and Microsoft alone is 141 rows and 27 events. Windows fixes all ship in the same monthly cumulative update with no security-only option, so the fix traits vary by month, not by CVE. The effective sample is tiny and dominated by one vendor.
4) Confounding by the role of the vulnerability. Microsoft's ransomware-flagged entries are mostly privilege-escalation bugs (CLFS and similar) used after the attacker is already inside. They are picked for what they do in an attack, not because the patch is scary. The candidate's control list does not account for this.
5) The outcome and the controls are unreliable. The KEV ransomware flag depends on who reports to CISA (Microsoft Threat Intelligence drives many of the Microsoft flips) and is updated in batches. That makes the Cox time-to-flip model a model of CISA's review schedule. EPSS as a control leaks exploitation evidence, which is over-control.
6) It does not test belief 2. "Vendor says you can't cleanly undo it" is about reversibility (belief 4), and "vendor documented known issues" is about vendor transparency. Neither measures a defender's uncertainty about blast radius in their own environment. The two indices are coded from the same documents and overlap heavily (a forced train jump counts as both effort and uncertainty), so the head-to-head comparison between them cannot be interpreted.
7) The headline is easy to attack. Critics will reply that anti-rollback is a security feature against downgrade attacks, that HA pairs, snapshots and config backup make rollback possible in practice, and that KEV often accepts vendor mitigations, so the upgrade is not the "only fix". The X of N number depends on coding choices.
Legal and ethical: no problems. It uses only public documentation and catalogs.
Data access: the KEV data is fine. Some vendor knowledge-base pages sit behind logins (Ivanti, some Citrix/Cloud Software Group pages). Pre-2025 KEV history needs a third-party archive.

**Prior art found:** What I checked: the session's web search budget was already used up, so I verified the data directly and assessed prior art from known literature rather than live search. (1) I verified the data. I downloaded cisagov/kev-data (catalog 2026.09.25): 1,726 entries, 361 flagged 'Known' for ransomware, which matches the claim. Since 2023: 860 entries, 145 Known. The cisagov/kev-data git history only starts on 2025-01-27, so the pilot's "since Oct 2023" relies on the third-party lodestone archive, which I did not verify. Replaying the kev-data history myself, I found 114 Unknown-to-Known flips between Jan 2025 and Sep 2026. The median lag is 352 days and 48% took more than 365 days, which is consistent with the pilot. But 37 of the 114 flips (32%) land on just 4 dates (14 on 2025-05-12, 10 on 2026-08-14, 8 on 2025-06-09, 5 on 2025-04-07). The flip date therefore reflects when CISA does its catalogue reviews, not when attackers started using the flaw. (2) Prior art, from memory, not re-verified this session. Li & Paxson CCS 2017 ("A Large-Scale Empirical Study of Security Patches") coded patch traits such as size and bundled non-security changes, but for open source and not joined to exploitation. Nappa et al. S&P 2015 studied patch deployment using WINE data. The Cyentia/Kenna Prioritization-to-Prediction series covers remediation speed by vendor. Allodi & Massacci's work-averse attacker model says attackers reuse exploits for widely deployed software, which is a competing explanation. Suciu et al. USENIX 2022 (Expected Exploitability), EPSS, and the VulnCheck and Securin "ransomware spotlight" reports profile which CVEs ransomware uses, but none of them look at fix traits. I know of no published coding of KEV fixes for reversibility joined to the ransomware flag, so that part looks new. However, it overlaps heavily with Round 1(c) (vendor patch regression census), round 2's "same-bug-different-ask forced release-train jumps" and "Regression Replay", and P4 (Burn Effect). The genuinely new piece is the join to ransomware.

### P1 — Fear Tax, Proof Shock, then Cliff: managed-cloud upgrades with and without proof (score 4.02, wounded)

**Best headline:** X% of internet-visible EKS clusters are past standard support, each paying AWS ~$4.4k a year not to upgrade. After AWS started showing customers exactly which APIs would break, clusters facing API removals upgraded Y days faster, and clusters with nothing to break did not move at all.

**Skeptic's flaws:** 1) The free pilot cannot run the design. The raesene data is aggregate counts by version string. It has no cluster IDs, so cluster fixed effects are impossible. It has no region, so GovCloud and China cannot be split from commercial. It ends 2024-02-05, only about 7 weeks after Insights went GA on 2023-12-20. The "free pilot in 1–2 weeks" cannot estimate the core effect.

2) The full study depends on per-host historical Censys data. Censys research access is aimed at academic, non-commercial work, and I could not verify it because the domain was blocked; a startup's PR study is probably out of scope. Shadowserver gives per-IP data to network owners and CERTs, so data on AWS IP space goes to AWS, not to a vendor. The key data is not accessible as claimed.

3) The headline cliff is invisible. From EKS 1.32 on, /version returns 401. The Q1 2027 cliff is the end of 1.32 extended support on 2027-03-23, which forces 1.32→1.33, and both versions answer 401. Only the 1.31→1.32 flip (Nov 2026) is observable, and a 200→401 flip also happens for other auth or config reasons.

4) The premise is out of date. "EKS control planes cannot be downgraded" is false: EKS version rollback (N-1, within 7 days) is documented from 2026-06-30. The irreversibility framing that drives the story no longer holds.

5) The "fear tax" is mostly the default setting. The upgrade policy defaults to EXTENDED, so a cluster on an extended-support version shows inertia or an unnoticed bill, not a purchase of delay. External data cannot tell default from opt-in. The ~700 Terraform hits for support_type EXTENDED are largely module variables and examples.

6) "Zero removed APIs" does not mean "provably safe", and it cannot be measured anyway. Terraform defines the cluster, not the workloads that call the APIs. Removed APIs are a small share of upgrade risk next to add-on, CNI and ingress compatibility, AMI, cgroup and containerd changes, node-group rolls and Helm charts. Hops after 1.26 remove almost nothing people use, so X% would be trivially close to 100% and a critic dismisses it on sight.

7) The treatment is confounded. Insights is a passive console panel, so any effect could be salience or a reminder rather than proof. Several shocks land within about 3 months of it:
- the extended-support preview (late 2023)
- the pricing announcement (early 2024)
- end of standard support for 1.23 and 1.24 (Oct 2023 and Jan 2024)

   The API-removing vs non-removing split is at the level of a version hop. It is therefore collinear with calendar time and with hop-specific changes (1.24 dockershim, 1.25 PSP). The GovCloud control has a tiny public-endpoint N and a different population (FedRAMP change control), so parallel trends are doubtful. A null result cannot be interpreted, because take-up is low.

8) Belief 2 is not isolated. Even a positive result shows only that information helps at the margin. Delay on clusters that are safe fits equally well with labor, prioritization and coordination (Dissanayake). The GKE Rapid→Stable lag reflects Google's fixed channel cadence, not customer uncertainty. The Lambda repos (Wonderless, OpenLambdaVerse) are source repos rather than deployed functions, with postponed deadlines and AWS create/update blocks acting as forced-deadline confounds.

9) Only public-endpoint clusters are visible, and regulated enterprises (the target design partner) lean toward private endpoints, so the sample is selected against the target market.

**Prior art found:** WebSearch budget was already used up, so I checked sources directly with WebFetch. Several vendor and doc domains (aws.amazon.com, docs.aws.amazon.com, censys.com, fairwinds.com, chkk.io, raesene.github.io) were blocked by the proxy.

(1) The descriptive part is not news. Datadog's Container Report (datadoghq.com/container-report) already says K8s v1.24 was the most popular release at 16 months old, and that 40% of orgs ran versions about a year old or less, up from 5%. Rory McCune (raesene) published the same Censys version-uptake data and blogged about it. Fairwinds' benchmark reports and tools like Pluto, kubent, eksup and Chkk already quantify deprecated-API exposure, or sell "upgrade safety" as a product. AWS itself ships Upgrade Insights and now "rollback readiness insights".

(2) I found no published causal study of whether Upgrade Insights changed upgrade timing, or of extended-support fees as a "fear tax". The causal angle looks novel, but the search was limited.

(3) Data checks:
- github.com/raesene/public-k8s-censys holds daily counts per distribution and version string only. It has no per-cluster ID, no hostname and no region. It covers Sep 2022 to 2024-02-05 and was discontinued because Censys cancelled free API access on 2024-02-17.
- containers-roadmap #2570 confirms Insights enforcement began 2025-03-27 and was rolled back 2025-03-28. The EKS user guide still says enforcement is "temporarily rolled back".
- The EKS docs (awsdocs GitHub mirror) confirm that from 1.32, anonymous auth works only on /healthz, /livez and /readyz, so /version returns 401.
- The docs confirm the upgrade policy defaults to EXTENDED.
- Current extended-support versions are 1.31 (ends 2026-11-26), 1.32 (ends 2027-03-23) and 1.33 (ends 2027-07-29).
- The docs show a NEW EKS control-plane version rollback feature, first documented 2026-06-30: N to N-1, within 7 days of the upgrade.

### C5 — The Proof Tax: four public Linux release gates that hold finished fixes for proof (score 3.81, wounded)

**Best headline:** Finished Linux security fixes waited X days in release gates for proof they wouldn't break anything. Z% of the test failures that held them passed on retry, and the fast lane that skips the gates shipped N regressions.

**Skeptic's flaws:** 1. Gate 2 barely exists as a treatment. The +2 bar for non-critical-path updates was not a lasting policy change. Bodhi 8.2 applied it by accident, and FESCo reversed it through Bodhi 8.3 about 3–4 weeks later (Nov 25, 2024, with production then set back to 1). The window also overlaps the flood of updates after the Fedora 41 release (Oct 29, 2024). At the same time, 8.2 changed autopush-on-negative-karma and manual-push eligibility for both arms. So the DiD/DDD rests on a few weeks of security updates with several simultaneous treatments. It is not a clean policy shock.

2. The object of study mostly skips the gates. nixpkgs explicitly sends critical security fixes that trigger mass rebuilds to staging-next, not staging. For security PRs, the 1000-rebuild line mostly picks the batching route, not whether a proof gate applies. Ubuntu's -security pocket bypasses both britney (for stable releases) and phasing, as the candidate admits. So gate 3 measures devel-series CVE fixes, mostly synced from Debian, that almost no production user runs. Gate 4's "time inside the gate" for security is zero by construction.

3. "Time inside a gate is pure proof wait by construction" is false.
- nixpkgs staging and staging-next wait for Hydra compute plus the batch's unrelated breakages. That is batching and coordination, not uncertainty about this particular fix.
- Bodhi karma waits for volunteer testers to show up (attention), and then a fixed 7-day timer runs.
- Britney 'age' is a fixed timer, and 'tests running' is infrastructure queueing.
- Only a sliver is actual evaluation of whether this fix breaks things. The candidate's own falsifier (compute, batching or coordination dominate) is the likely outcome.

4. The counterfactual in gate 4 can't be identified. Phasing detects crashes only, not functional regressions. The halt rule is partly binary ("error only seen with the SRU version"), and past crash metrics aren't archived. So both "how many of the 486 regression USNs phasing would have caught" and the regression discontinuity at the halt threshold are guesses, not measurements.

5. It doesn't test belief 2. These are volunteer distributions' release-engineering gates, upstream of the enterprise. Even a strong result shows that vendors hold fixes for QA, which the industry already knows. It says nothing about why organizations don't deploy fixes once they're published. Worse, the headline evidence cuts against the pitch: the ecosystems best placed to measure breakage (Ubuntu, nixpkgs, and Debian security) have already waived proof for security fixes.

6. The headline is weak. It gives four separate numbers (X, Y, Z, W) about NixOS, Fedora and Ubuntu, rather than one crisp, CISO-relevant number like the MCP-server reference.

Legality and ethics are fine: public git, API and CI data, and lab rebuilds.

**Prior art found:** I could not run a proper literature search. The WebSearch budget was used up, and arXiv, Semantic Scholar, docs.fedoraproject.org and pagure were blocked. So the prior-art check covers primary sources plus the literature I already know.

(1) Known literature. The "technical lag" papers (Gonzalez-Barahona 2017; Zerouali et al. 2018–2021 on Debian, npm and Docker) already measure how far distributions lag upstream fixes. Claes/Mens-era MSR work mined Debian testing migration and package incompatibilities. Flakiness in distro CI, including autopkgtest retries and force-badtest hints, is widely known inside Ubuntu and Debian, and those hints are public. As far as I know, no one has published a per-gate breakdown of how long security fixes wait for proof, so that part is somewhat new.

(2) Overlap with ideas already proposed. Much of this repeats round-2 items: "dependents oracle on distro CI" (autopkgtest used as an oracle), "distro 'would break users' reason mining" (britney excuses), "Regression Replay" and P5 Patch Weather (Ubuntu USN regressions), and P2 Qualification Clock (the vendor holding a fix for qualification).

(3) Primary-source checks.
- Bodhi 8.2.0 was released 2024-10-26 and folded the critpath minimum karma into one min_karma. That made non-critical-path updates need +2 only "during phases where the policy minimum karma requirement is +2".
- Bodhi 8.3.0 (2024-11-25, PR #5802) put the separate critpath and non-critpath minimums back "because FESCo has decided to reinstate different minimum karma", and the developers said "We'll set it to 1 in downstream config".
- The nixpkgs CONTRIBUTING.md branch table routes "Critical security fixes: ✔️ for mass-rebuilds" to staging-next, with ❌ for staging.
- The phased-updates report (phased-updates.ubuntu.com, 2026-09-26) shows 4 halted and 17 phasing SRUs, with no history. It halts on "an increased rate of crashes or an error only seen with the SRU'ed version".

### C7 — Friendly Fire, Fast Path: security changes and burns in public outage records (score 3.74, wounded)

**Best headline:** X of the N biggest self-inflicted cloud and CDN outages since 2019 were caused by changes meant to improve security, and Y of those X went out globally with no canary. In the post-mortems, providers promised K fixes that slow changes down for every one that proves a change is safe.

**Skeptic's flaws:** 1. It measures the opposite of belief 2. Claim 1 shows that providers push urgent security changes fast, skipping canaries, and break things. That is the cost of acting without proof. It is not evidence that uncertainty about breakage causes delay. A critic will say that hyperscalers are not blocked by impact uncertainty at all: they ship and burn. So the headline supports 'proof is valuable' (belief 3) but says nothing causal about why enterprises wait. The inference 'so everyone else rationally waits' is the author's, not the data's.
2. Claim 3 (scar vs storm) cannot be fixed with public data.
   (a) The outcome is mostly unobservable. Providers rarely post security patching as maintenance. Hyperscaler Kubernetes patch timing follows release trains and the monthly upstream patch cadence, not individual incidents.
   (b) Status pages rarely state a cause, so the own-change versus upstream split is noisy.
   (c) There are only three 'storms'. That is three clusters, so no valid clustered inference.
   (d) The storms are not quasi-random for exposure: vendors hit by us-east-1 differ systematically in architecture and maturity.
   (e) A post-storm change freeze is also friction, which contaminates the subtraction.
   (f) The Statuspage v2 public API returns only the most recent 50 incidents, so history depends on the unpriced IsDown licence or archives.
3. The friction-versus-proof code has a construct problem. Canaries, staged rollout, health-mediated deployment and config validation are both friction (slower) and proof (new evidence). K:1 is set by the codebook's definitions, and two blinded coders give reliability, not validity. Cloudflare's actual response, staged health-gated config rollout, is arguably the proof/containment Skylayer sells. That undercuts the rhetorical headline.
4. There is no denominator. Without per-change counts, 'security changes cause outsized outages' is only a share among reported outages. Publication bias is severe: only big incidents get PIRs, Cloudflare's transparency will dominate, and motive is often hidden behind 'a configuration change'. Security-motivated N is likely tens, concentrated in 2 to 3 firms.
5. External validity is weak for wedge B. CDN and cloud control-plane config at hyperscalers is not enterprise OS, package or container patching, and not a medical-device company.
6. The crisp number is weak. Something like '11 of 140 outages were security changes' repeats well-known anecdotes and would not go viral.

**Prior art found:** Verification was limited. WebSearch was out of budget, and the proxy blocked arXiv, Semantic Scholar, the Cloudflare blog, the Wayback Machine, the Azure and GCP status sites, githubstatus, IsDown and VOID. I could only reach GitHub, so most of the prior art below comes from domain knowledge, not from fetches made in this session.
(1) Gunawi et al., 'Why Does the Cloud Stop Computing? Lessons from Hundreds of Service Outages' (SoCC 2016). It coded 597 public outages across 32 services from post-mortems and news, including upgrade, configuration and security root causes. That is the same census method as claim 1, minus the security-motive code.
(2) Huang et al., 'Metastable Failures in the Wild' (OSDI 2022), and Zhang et al., 'Understanding and Detecting Software Upgrade Failures in Distributed Systems' (SOSP 2021). Both code public incident reports.
(3) Microsoft production-incident studies (Liu et al., HotOS 2019; Ghosh et al., SoCC 2022) and Gandalf (NSDI 2020), plus the Google SRE book's claim that about 70% of outages come from changes. 'Changes cause outages' is settled.
(4) Uptime Institute's annual outage analyses and the VOID reports already publish aggregate cause and duration findings from public reports.
(5) The core anecdote is already public and was written up by the providers themselves. Cloudflare's WAF regex outage (2 Jul 2019) and its React2Shell WAF change (5 Dec 2025) both went through the fast global-config path. CrowdStrike's July 2024 RCA says Rapid Response Content was not staged. Other security-motivated cases include Slack's DNSSEC rollout (Sep 2021) and Azure AD's signing-key rotation (Mar 2021). Cloudflare then publicly committed to staged, health-gated rollout of config changes ('Code Orange: Fail Small', late 2025, from memory).
(6) Within this tournament, round 2 already lists a 'friendly-fire outage census' and a 'pre-registered outage blast radius'. Claim 3 is P4 (Burn Effect) moved to providers.
(7) GitHub has danluu/post-mortems (about 12.5k stars, 300+ entries, a handful security-triggered), icco/postmortems (structured metadata for that list) and Operations-Incident-Board/Postmortem-Report-Reviews. I found no published study that codes security motive against rollout path, or corrective actions as friction versus proof. That narrow combination is the only new part.

### C13 — The 24-Hour Test: forced certificate replacements with fix, deadline and information held constant (score 3.73, wounded)

**Best headline:** Ordered to swap a named certificate within 24 hours, with the free replacement already issued: X of N organizations were still serving the revoked certificate D days later, Y% of those that swapped put the revoked one back within a week, and mail, VPN and appliance ports lagged web ports on the same certificate by K×.

**Skeptic's flaws:** The central claim, that the design "holds fix, deadline and information constant and so isolates uncertainty", does not hold.

1. The cost of doing nothing varies by port. Browsers enforce revocation unevenly: Chrome mostly does not for DV/OV, Firefox does through CRLite, Apple does in part. SMTP STARTTLS, VPN and most appliance clients almost never check revocation. A revoked certificate left on 25/993/VPN/appliance ports breaks nothing, so waiting is rational with zero uncertainty. This alone predicts the headline "K× longer on mail/VPN/appliance ports".

2. The effort to fix varies by port. On load balancers the swap is often ACME or API driven. On appliances and mail daemons it means a manual import, a restart and sometimes a vendor ticket. The thesis says "not because the fix is hard", but the port contrast lines up exactly with how hard the fix is. The same-host cross-port lag is the textbook "forgot the Dovecot config" case: an unknown asset or toil, not fear.

3. The deadline is not constant. The DigiCert 2024 extensions, the TRO and the Mozilla delayed-revocation process let large or "critical" subscribers negotiate delays. Who gets a longer deadline is selected on the outcome. The 24h versus 5-day split is set by BR reason code, which differs by incident type, CA and subscriber mix, so it is not an exogenous contrast.

4. Signature D, the only one meant to indicate uncertainty, cannot be identified from scan data:
- Censys scans ports at different cadences, and non-top ports can go days between scans, so "last seen" is biased by port.
- A 24h canary is below the scans' time resolution.
- Round-robin DNS, anycast, CDNs and pools of backends behind one IP:port make the certificate appear to "flap". That mimics swap-then-revert.
- A real revert is evidence of breakage that actually happened, not of fear beforehand.
- IP scans without SNI see only default certificates, which skews the sample toward appliances.

5. The best control has a hidden problem. The within-endpoint DiD against routine renewals nets out toil, but it also nets out blast radius, since it is the same change on the same endpoint. What remains is unplanned-change or CAB friction, which cannot be told apart from plain bureaucracy.

6. The Bugzilla delay reasons are strategically biased. Root programs accept only exceptional-harm justifications, so CAs will frame delays as "customer outage risk" whatever the real cause. They are not evidence that uncertainty is the cause.

7. It is off-wedge. A same-CA certificate swap is among the lowest-uncertainty changes there is. The ACME/ARI contrast will almost certainly show "automated is fast, manual is slow", which supports speed/tooling (the Chrome "Moving Forward Together" and CLM-vendor narrative) and cuts against belief 2.

Net: the study can falsify belief 2 (lag mostly A/B/C) but cannot confirm it. It is a one-sided test, and a critic will dismiss any supporting result with points 1 and 2.

Feasibility and legal: legal overall (public CT, Bugzilla, CRLs, court records; no scanning of our own). There are two caveats:
(a) Censys academic research access is for non-commercial use. A startup's marketing stunt on academically licensed data risks breaching the terms unless the academic partner owns the work, and a commercial licence is costly.
(b) The fallback does not work. HTTP Archive covers only web pages, crawls about monthly and uses SNI, so it cannot support the port contrast or daily lag. Rapid7 Sonar public data was closed in 2022.

Few events meet the conditions (a large subscriber base, published serials and observable endpoints). Realistically that is DigiCert 2024, LE 2020 (mostly automated subscribers), the 2019 serial-entropy incident and some Entrust/Sectigo events.

**Prior art found:** Web verification was mostly blocked in this session. The WebSearch budget was used up, and arxiv, Semantic Scholar, Bugzilla, crt.sh, Censys, USENIX and the Let's Encrypt forum were all egress-blocked. The only live check was GitHub code search. Items marked (known) come from memory and were not re-checked here.

Found in this session:
(1) SystematicReasoning/webpkiobservatory on GitHub. It already pulls Mozilla Bugzilla CA incidents and uses an LLM to code them. Its codes include "delayed_or_refused_revocation", and it has root-cause pattern chains per CA, e.g. a CA failing to revoke 210 certificates in 24h because of a RabbitMQ queue failure, or revocations delayed nine months. So the "coded CA delay reasons" arm is already partly done in public.
(2) Mozilla root-store policy and a Mass-Revocation-Template in mozilla/pkipolicy. They now require CAs to keep mass-revocation plans and to put subscriber-cooperation clauses in customer contracts. Delay handling is therefore negotiated and documented, not uniform.

Known, not re-verified:
(3) Zhang et al., IMC 2014, "Analysis of SSL Certificate Reissues and Revocations in the Wake of Heartbleed". The canonical forced-replacement lag study using full-IPv4 scans. It found most vulnerable sites did not reissue, and some reissued with the same key.
(4) Durumeric et al., IMC 2014, "The Matter of Heartbleed". Patch and replacement curves, plus a notification experiment.
(5) Liu et al., IMC 2015, an end-to-end measurement of revocation.
(6) The Let's Encrypt 2020 CAA incident, about 3M certificates. Let's Encrypt publicly chose not to revoke a large remainder by the deadline because of breakage concerns. This is the CA itself showing fear of breakage, and it is widely discussed.
(7) The 2019 incident over 63-bit serial numbers. Several CAs, including large ones, delayed or declined revocation, citing customer impact.
(8) The Censys DigiCert 2024 counts (the candidate concedes these) and the Alegeus TRO, which was heavily covered in 2024. The headline's "went to court" line is old news.
(9) Ma et al., IMC 2023, on stale TLS certificates.

Revoked-certificate persistence and replacement lag are well studied. What is new is only the framing as a remediation natural experiment and the same-IP, cross-port contrast.

### C12 — Show Me What Breaks: RPKI signing and route-origin validation, where blast radius is exactly computable (score 3.64, wounded)

**Best headline:** Same operator, same button: prefixes whose signature would knock a customer's live route offline stayed unsigned X times longer than prefixes where it breaks nothing, and N networks could drop hijacked routes today while losing exactly zero destinations, yet Z% still don't.

**Skeptic's flaws:** 1) THE DESIGN DOES NOT ISOLATE UNCERTAINTY. B1 differs from B0 in more than blast radius. It also needs coordination with a third party (the customer's ASN and consent, and who is responsible for the ROA), and it carries an ongoing burden: the holder must maintain a ROA for someone else's routing. Frag-Int prefixes, which are entangled only with the holder's own space, were signed faster than Leaf prefixes. That points to "another org is involved" (the Dissanayake coordination story) rather than "unknown breakage." The customer-exit event study removes coordination and blast radius together, so it cannot separate them either.

2) THE PREVIEW IS NOT A PURE INFORMATION SHOCK. RIR dashboards and Krill show affected announcements and also offer ROA suggestions or one-click authorization. Visible B1 therefore becomes both known and easy. The B1-invisible placebo cannot separate information from effort, because invisible breakage also gets no one-click fix.

3) THE STAGGERED ROLLOUT IS WEAK. There are about five registry clusters, and RIPE/APNIC previews date from the 2011–2019 low-adoption era, so in practice ARIN is the only modern treated unit. ARIN's timing is confounded by RPA/LRSA legal changes, the 2024 US federal routing-security push and the FCC BGP proceeding. Five clusters also means unreliable inference. The launch dates themselves are still unpinned.

4) THE ROV ARM HAS A MEASUREMENT CONFOUND AT ITS KEY TEST. RoVista scores rise when an upstream filters, so a downstream AS's own adoption cannot be dated around upstream-enforcement events, which is exactly where the opposite-sign test lives. "Exactly zero destinations lost" is also not exact: it needs each AS's full RIB, and that is visible only for collector-feed peers. Since most invalids have covering routes, N would be close to everyone, a known and trivial result. "Z% still don't" shows delay, not its cause.

5) THE HEADLINE IS LIKELY TO DEFLATE. The within-holder "X× longer" looks like about 1.06x on crude data, which is not a viral number. B1 is also a tiny slice of the ROA gap.

6) IT IS OFF-WEDGE. The actors are ISPs and RIR members, not enterprise CIOs/CISOs, and ROA signing is hardening rather than vulnerability remediation under exploit pressure. The candidate already concedes that wedge A (network config) had zero interview support. The argument from routing to enterprise patching is only an analogy and is easy to dismiss.

Legality is fine: passive public data, aggregate reporting.

**Prior art found:** Caveat on method: WebSearch was exhausted and the proxy blocked arXiv, DBLP, Semantic Scholar, labs.ripe.net, blog.apnic.net and arin.net. I verified prior art through GitHub and by downloading public data.

VERIFIED:
(1) Gouda, Fontugne, Testart, "ru-RPKI-ready: the Road Left to Full ROA Adoption," IMC 2025 (github.com/ISS-GT/ru-RPKI-ready, ISS-GT/ru-RPKI-ready-Code, Zenodo 10.5281/zenodo.17237911). Their public monthly parquet snapshots (Jan 2025 to Sep 2026, v4 and v6) already tag every routed prefix as Covering/Leaf, Frag-Int/Frag-Ext (a covering prefix whose more-specifics are reassigned to other orgs, which is essentially C12's B1 class), Reassigned, Diff SKI pfx/ASN (signing needs cross-org coordination), ROA Org (the holder has signed elsewhere, i.e. "same org, same button"), org size, and Legacy/(L)RSA. The paper's stated conclusion is that "the complexity of planning and deploying ROAs remains a significant challenge," and it ships a planning tool. So C12's descriptive half, and its framing that planning uncertainty is the barrier, is already published by the group C12 hopes to partner with. The causal part (hazard with holder fixed effects, preview-rollout triple difference, customer-exit event study) appears new, but the same group holds the longitudinal data and could scoop it.

FROM MEMORY, NOT RE-VERIFIED:
- Gilad et al., NDSS 2017, "Are We There Yet? On RPKI's Deployment and Security": measured ROA misconfigurations and ran the ROAlert operator notifications, i.e. telling operators what breaks.
- Chung et al., IMC 2019, "RPKI is Coming of Age": invalids caused by provider/customer ROA mismatches.
- Testart et al., PAM 2020, on the benefits of registering in RPKI.
- RoVista (Li et al., IMC 2023): per-AS ROV scores that include "collateral benefit" from upstream filtering.
- Yoo and Wishnick, on legal barriers to RPKI (the ARIN RPA/LRSA).
- Cloudflare's "Is BGP Safe Yet."
The claim that ROV costs almost no reachability because most invalids have covering routes is well-trodden ground.

SKEPTIC PRE-TEST, RUN ON REAL DATA (IPv4; ru-RPKI-ready snapshots Jan 2025 vs Sep 2026; prefixes that were unsigned but certified in Jan 2025):
- Among orgs that already had at least one ROA, the share signed by Sep 2026 was 26.8% for Frag-Ext (n=5,768), 39.6% for Leaf (n=124,787) and 47.6% for Frag-Int (n=8,818). So the raw gap is about 1.5x.
- Within the same holder (holder fixed effects, linear probability model, holders that signed anything), Frag-Ext was only 4.1 points less likely to be signed than Leaf, against a 65.5% base rate: about 6% relative. Reassigned prefixes carried no penalty (+1.5 points). Most of the raw gap is therefore between-org selection, which leans toward falsifying prediction 1.
- Once signed, 99.6% of Frag-Ext prefixes were Valid: when orgs sign, they rarely break things.
- Frag-Ext is only about 3.5% of unsigned certified prefixes. The ROA gap is dominated by legacy/uncertified space and orgs that have never signed anything.

### C8 — One Browser, Two Fleets: what holds a free, automatic fix on work machines (score 3.59, wounded)

**Best headline:** Admins had switched off quantum-safe encryption on X% of Chrome traffic from enterprise networks. When Chrome 147 removed that switch, connection failures rose by only Y points. The same networks still held back Chrome 147's security fixes N days longer than home networks.

**Skeptic's flaws:** 1) The Z headline is wrong by construction. I verified that Chrome Extended Stable, the channel Google offers enterprises, skips odd milestones and got weekly security respins on 146 throughout the 147 window (Mar 10 to May 5, 2026). An enterprise ASN that looks like it is "holding back 147" at major-version level can be fully patched. Radar gives at most a major version, never a build, so security lag cannot be measured. The same fact moves the PQ-removal date for Extended fleets from 147 (Mar-Apr) to 148 (May), which blurs the triple difference. Edge Extended Stable probably has the same odd/even pattern, which weakens the Edge comparison.
2) The Y leg cannot be measured. Radar tcp_resets_timeouts has no browser or OS filter (verified), so a Chrome-specific breakage change cannot be separated from all other traffic on the ASN.
3) TLS-inspecting proxies and SSE services (Zscaler, Netskope, Prisma, and Cloudflare Gateway itself) terminate the browser's TLS. Cloudflare then sees the proxy's ClientHello and often the security vendor's ASN, not the enterprise's. The proxies are exactly the middleboxes that caused PQ opt-outs, so "had switched it off on purpose" cannot be told apart from "a proxy is in the path", and X is biased toward zero.
4) Hybrid work puts managed laptops on residential ASNs. The ASNs you can identify as enterprise (universities, government, large corporate campuses) are a biased, often BYOD-heavy subset. Radar may also suppress or low-confidence per-ASN × browser × PQ splits for small ASNs (unverified).
5) Belief-2 isolation is weak. Managed-fleet lag is mostly MSI/SCCM/Intune packaging cadence, VDI golden images, relaunch timing and sanctioned Extended Stable. Holds that track "releases with policy removals" fit change-review process just as well as fear of breakage. That is the coordination story from Dissanayake et al., not impact uncertainty. Calendar alignment (method 3) is also ambiguous.
6) The likely effect is tiny. PQ has been on by default since Chrome 124 (2024), and opt-outs by 2026 are probably rare, so X and Y are hard to detect and would not make a viral number.
7) The relevance to the thesis is thin. Browsers are the one area where the vendor already acts through staged, gated, reversible rollout. Wedge B (OS/package patching) is not tested, and the result may even undercut belief 1.
8) Enterprise ASNs identify organizations. Any per-ASN reporting would expose named organizations' configurations, so results must stay strictly aggregate. Radar data is CC BY-NC, and a commercial startup's marketing use needs Cloudflare's permission.

**Prior art found:** My web search budget ran out, so I could not run fresh prior-art searches. What I checked directly (verified this session):
(1) Chromium policy YAML for PostQuantumKeyAgreementEnabled: supported_on chrome.*/chrome_os/android 116-146, deprecated, "temporary measure... removed sometime after 145". The claim holds.
(2) Chrome VersionHistory API: Chrome 147 stable started 2026-03-25 at fraction 0.005, with rollout/control tags in rolloutData. The claim holds.
(3) VersionHistory, extended channel: Extended Stable SKIPS 147 entirely. It went 146.0.7680.72 (Mar 10) through .154/.165/.178/.188/.201/.208/.216, with weekly security respins until May 5, then 148.0.7778.97 (May 5-11).
(4) Cloudflare OpenAPI schema from github.com/cloudflare/api-schemas: /radar/http/summary|timeseries_groups/post_quantum accept asn, os, deviceType and browserFamily. /radar/http/top/browser ("top user agents", example value "chrome") may or may not return versions; I could not check without a token. /radar/tcp_resets_timeouts accepts ONLY asn, location and continent, so no browser or OS split is possible.
I could not reach developers.cloudflare.com, blog.cloudflare.com or learn.microsoft.com (Edge removal at 147 unverified).
Prior art from memory, not re-verified: Frei, Duebendorfer et al. "Firefox (In)Security Update Dynamics Exposed" (ACM CCR 2009) and "Why Silent Updates Boost Security" (ETH TIK 2009) measured browser version and patch lag from Google server logs; Nappa et al., "The Attack of the Clones" (IEEE S&P 2015), and Sarabi et al. (PAM 2017) measured Chrome and Firefox patch deployment on millions of hosts; tldr.fail (2024) documented middleboxes breaking on large PQ ClientHellos; Cloudflare's own PQ blog posts report PQ share by browser; industry browser-security reports claim enterprise browser patch lag. Measuring managed-versus-consumer browser lag from logs is therefore old. Using the PQ opt-out removal as a natural experiment appears novel.

### C6 — Scar vs Storm in the Open: GitLab's and Wikimedia's public production ledgers (score 3.2, wounded)

**Best headline:** GitLab runs production in public: X% of its N outages with a known cause came from its own changes, and after one, similar changes took D days longer to ship, while equally bad outages that no change caused slowed nothing. Its engineers' own pre-change risk ratings predicted which changes would break with an AUC of only Y.

**Skeptic's flaws:** 1) The security headline has almost no data. I pulled all 2,976 change issues through the unauthenticated API. Only 10 titles match real security or kernel patching across about 8 years (5 in 2018-19, 5 in 2025-26). Another 44 are OS upgrades, 30 of them from one Ubuntu 22.04 campaign in 2025. That campaign was driven by end-of-life, not by CVEs. Routine patching is automated through Chef and is not in the tracker. 'After a scar, security upgrades waited D days longer' cannot be estimated.

2) The pilot numbers do not replicate. Among issues labelled 'change' the counts are C1 150, C2 841, C3 1,214, C4 546, not 231/1,071/1,690/879. Median filing-to-close is C1 9.7 days vs C4 1.8 (claimed 14.7 vs 1.2). Abort rate is C1 6.0% vs C4 2.0% (claimed 12.2% vs 3.0%). The candidate's counts seem to include issues that are not changes, and C1 includes about 10 Production Change Lock issues, which are freezes, not changes.

3) Mechanical policy confounds. The handbook, fetched from its GitLab source repo, says:
- C1 and C2 changes automatically block deploys.
- Emergency Production Change Locks during critical incidents block all C2+ changes.
- Starting a C1 change needs on-call engineer approval that checks for ongoing incidents.
So any slowdown after a scar may just be a written rule being followed, not uncertainty. Emergency locks such as 2023-07-08 and 2024-09-03 sit right in the event windows.

4) Scars and storms do not drain capacity equally. A scar sends incident-review and corrective-action work to the team that made the change, which is the same team that files later changes. A storm mostly loads on-call staff and often creates capacity changes, which raise change volume. So scars fall and storms rise even if nobody is uncertain about anything. The design's claim that storms absorb capacity drain does not hold.

5) Root-cause labels are missing for recent data. 84 of 100 incidents from May 2023 have a RootCause label, but only 17 of the 100 most recent (Sep 2026), and those recent labels are ML-applied ('automation:ml'). Process regimes also shift over time: 2020 had 62 change issues against 706 incidents, and 2021 had 1,601 incidents, inflated by alerts. Event windows overlap: there are about 100 labelled S1/S2 incidents a year (roughly 290 change-caused and 245 not) against about 9 changes a week. Clean windows are rare, and outcome counts per window are about 15-20.

6) The calibration test is not identified, for two reasons. C-levels are assigned from what the change touches, not from a predicted probability of failure. The label also triggers extra safeguards, so a low AUC may only mean the safeguards worked. Aborts are often scheduling decisions or incident conflicts, not breakage. Linked issues and label timelines need a token: /links and /resource_label_events both returned 401.

7) Staging-to-production gaps are set by design: soak time and weekend windows for C1 changes. Without coded reasons they measure delay, not what causes it.

8) The fit to the goal is poor. This is one mature SaaS company with continuous deployment and automated patching, so it says little about enterprise or FDA-regulated remediation. The headline names GitLab and would expose its patch lag, which clashes with the rule against naming organizations and penalizes a company for being transparent. Even at best it is an SRE-behavior finding, not a security-industry stunt.

**Prior art found:** The prior-art check is incomplete. The WebSearch budget was used up, and the proxy blocked Semantic Scholar, OpenAlex, arXiv, DuckDuckGo, Bing, wikitech and handbook.gitlab.com. I could not rule out an MSR/ICSE-style paper mining gl-infra/production. From memory, not re-verified:
(a) 'X% of outages come from our own changes' is not new. The Google SRE book says about 70% of outages come from changes to live systems, and Uptime Institute and the VOID (Verica Open Incident Database, which includes GitLab's public incidents) repeat similar figures.
(b) The scar-vs-storm design is a known one. Choudhry et al., BMJ 2006: after a patient bled on warfarin, doctors prescribed it less; after a stroke from not prescribing, nothing changed. Related: the hot-stove effect (Denrell & March 2001) and learning from failure (Madsen & Desai 2010).
(c) Predicting change risk and catching bad deployments has a large industry literature: Microsoft Gandalf (NSDI 2020), SCWarn, and work at Alibaba, Huawei and IBM on change and incident risk.
(d) Dissanayake et al. (CSCW 2022) found that coordination causes most delay.
What looks new is running this design on public data from one production org. None of its parts is new.

### P3 — Last Blocker: the web's public dependency graph (HTTPS migration natural experiment, CAA, DMARC) (score 3.09, wounded)

**Best headline:** Of N home pages still on HTTP in 2016, X% could not switch without breaking a third-party script. When that one vendor turned on HTTPS, they switched Y× faster, and Chrome's 'Not Secure' warnings moved them Z× less than sites with no such blocker.

**Skeptic's flaws:** 1. Wrong construct, and it is built into the design. An HTTP-only active third party means certain, deterministic breakage: browsers block active mixed content. It is not uncertainty about breakage. Before the vendor unblocks, the only fix is to drop or replace the vendor (high effort, often lost revenue). Afterwards, the fix is a find-and-replace. So the treatment changes feasibility and effort. The proposal's claim that "fix and effort are fixed and only risk changes" is false. A positive result would show "dependencies make the fix hard or impossible," which is the very alternative the thesis says is not the cause. Belief 2 (uncertainty is the blocker) is not tested.

2. The falsification test is close to mechanical. Sites that cannot migrate without removing a dependency will respond less to Chrome warnings by construction, so the "falsified if blocked respond as much as unblocked" condition is almost guaranteed to pass and tells you little.

3. Vendors turning on HTTPS often came with a new hostname or snippet (e.g. ssl.google-analytics.com), or with plugin/CMS updates that rewrote the embed code for the site. The site's "migration" can then be mechanical, and effort changes at the same moment as risk.

4. Vendor timing is endogenous to industry pushes: the IAB LEAN/ad-tech HTTPS drive of 2015–16, AdSense, and the same Chrome and Let's Encrypt shocks. Ad-heavy publishers, the main blocked group, faced revenue and SEO risk from migrating (fill-rate drops, referrer loss). That was the real uncertainty, and it is unobserved here.

5. Hosting-platform flips (Cloudflare Universal SSL 2014, WordPress.com 2016, Blogger, Squarespace, Wix, Shopify) drove most long-tail adoption. They are site-level shocks tied to both the outcome and embed updates. Early crawls lack good platform detection.

6. Panel breaks. The crawl list moved from Alexa to CrUX origins (with scheme) in mid-2018, essentially the same month as Chrome 68 (July 2018). The Chrome 68 difference-in-differences is therefore confounded by a change in sample composition. Pre-2018 "long tail" means the Alexa top ~500K, not small sites.

7. Only home pages are crawled, and ad auctions vary from crawl to crawl. Blocker counts are noisy and blockers on inner pages are invisible, so sites get misclassified as unblocked. Restricting to the "last blocker" also thins the sample, and power is unknown.

8. The headline "bigger push than free certs or Chrome warnings" compares a site-level unblocking hazard ratio with population-wide time shocks. The two are not commensurable.

9. The CT "fix on the shelf" gap breaks down before April 2018: CT logging was not mandatory, so non-Let's-Encrypt DV certificates are missing. AutoSSL/cPanel also issues certificates without any site decision, so issuance-to-redirect is not a decision lag.

10. The live replay is mistimed and tests a different mechanism. HTTP-only active vendors are essentially extinct by 2026, Chrome 154 is weeks away, and the Chrome 147 ESB rollout is already in the pre-period.

11. Relevance and virality are weak. 2014–2019 web HTTPS is "solved, old news," it is only an analogy to OS/package patching, and it does not give a CISO a crisp number about today.

Legality is fine: public data only, no scanning, aggregate reporting.

**Prior art found:** Verification was limited. The session's web-search budget ran out after the first call, and the egress proxy blocked dl.acm.org, arxiv.org, usenix.org, semanticscholar, crt.sh, openintel.nl, chromium/googleblog and almanac.httparchive.org. Only GitHub raw files could be fetched.

VERIFIED via the HTTPArchive/almanac.httparchive.org repo:
- The 2019 Web Almanac methodology says HTTP Archive takes its URL list from Chrome UX Report origins, which include the scheme (e.g. https://www.example.com), and "only the home pages are included."
- The 2019 security chapter already reports about 20% of sites with mixed content and roughly 79–80.5% HTTPS adoption, with a mixed-content breakdown into active vs passive.

FROM MEMORY, NOT RE-VERIFIED THIS RUN:
- Kumar, Ma, Durumeric et al., "Security Challenges in an Increasingly Tangled Web" (WWW 2017) is the cross-sectional version of this project's descriptive headline. It found about 28% of HTTP Alexa-1M sites blocked by HTTP-only active third parties, and that a small number of third parties account for most of the blocking. So "X of N sites held back by a single third-party script" is largely already published.
- Felt et al., "Measuring HTTPS Adoption on the Web" (USENIX Security 2017).
- Aas et al., Let's Encrypt (CCS 2019), which already credits LE for adoption growth.
- Kotzias et al., TLS longitudinal study (IMC 2018).
- Chen et al., "A Dangerous Mix" (mixed content, 2013).
- Google's own public figures on the effect of Chrome 56/62 "Not Secure" warnings.
- CAA arm: Scheitle et al., "A First Look at Certification Authority Authorization (CAA)" (ACM CCR 2018) measured CAA deployment and misconfiguration. Cloudflare already adds its own CAs to CAA records automatically, which blunts the "primary-CA-only breaks issuance" story.
- DMARC/CSP arm: this is round-2 P3, already proposed.

WHAT SEEMS NEW: a staggered causal event study on vendor HTTPS dates. I could not find it, but I could not search properly.

Chrome timeline, from memory: Google announced (Oct 2025) Always-Use-Secure-Connections on by default in Chrome 154 (~Oct 2026), after a Chrome 147 (~Apr 2026) rollout to Enhanced Safe Browsing users. Chrome 154 is about 3–4 weeks from today, and the 147 rollout has already contaminated the pre-period.

### C10 — The Configured Wait: patch deferrals, auto-patch opt-outs and risk acceptances written in public code (score 1.4, dead)

**Best headline:** Across N real patch policies, production is set to wait a median X days longer than pilot for the same security update, a waiting period written into config and longer than time-to-exploit. Yet only Y% of written CVE exceptions cite fear of breakage, and Z% of those fixes pass the project's own tests.

**Skeptic's flaws:** 1. The headline arm has almost no operational data. The Windows ring figure ("N real patch policies ... pilot on day 0") rests on qualityUpdatesDeferralPeriodInDays, and that corpus is SDK code, API docs, books, tooling and community baselines. Orgs manage Intune rings in the tenant, not in Git, and security-mature orgs don't publish them. After deduping templates, N real org policies with paired pilot/prod rings is probably in the single or low double digits. SSM baselines are similar: the modal value 7 copies the AWS default, and only about 7% of sampled hits are keyed by environment.
2. The prod > pilot result can't fail. Rings are staggered by definition, and vendors tell you to stagger them. The pre-registered falsifier "prod ≈ pilot" therefore can't fire in any ring file. The gap measures whether an org adopted Microsoft/AWS guidance, not an org-specific "blast-radius premium".
3. Even a positive result points against belief 2. Configured waits are 7 to 13 days, while observed real-world remediation times run into months. So the "pure uncertainty premium" lower bound is a small fraction of total delay. The candidate itself treats this as a lower bound, and read honestly it says most delay is elsewhere (coordination, capacity, unknown assets), which matches Dissanayake. It also shows the proof mechanism (rings) already comes free from Microsoft and AWS, which weakens the moat.
4. The exception arm is already falsified by the proposal's own pilot, and its category is wrong. The pilot found breakage language in 15/100 .trivyignore files, below the proposal's own 25% falsifier. The breakage language that does appear mostly concerns misconfiguration rules (non-root USER, privileged mode) or known, certain incompatibilities (major bumps, ESM-only). That is "the fix is hard", which is exactly what belief 2 says is not the cause, and it is not uncertainty about impact. The lab counterfactual would also be run today, with hindsight: later compatible releases now exist and test suites are weak, so "Z% pass tests" can be dismissed either way. It also repeats Round-1 (a).
5. The KEV comparison is mechanical. Many KEV entries are zero-days exploited before a patch exists, and M-Trends reports average time-to-exploit as negative. Any deferral of 0 days or more gets counted as "exploited before install", so X% says nothing about uncertainty. The headline also compares Windows endpoint rings with the edge-device figure from DBIR, which is a different asset class.
6. Motives for opting out can't be separated. RDS auto_minor_version_upgrade=false, GKE no-channel clusters and a Manual Lambda runtime are chosen for maintenance-window control, stateful workloads, cost, compliance change control, or supply-chain cooldown. GKE doesn't even allow auto-upgrade to be turned off on release-channel clusters, so the population is self-selected. The event study around CrowdStrike (a content update, not an OS patch) and GKE upgrade waves has tiny N, and its commit timing is driven by template maintainers.
7. The reasons text is contaminated by coding agents. More and more 2026 ignore-file justifications are written by LLM coding agents, so coding "reasons" partly measures model boilerplate rather than human risk judgment.
Legality is fine: public code, reported in aggregate. The problem is that the stunt can't produce its crisp number honestly, and the parts that could be measured cut against the thesis.

**Prior art found:** Web search was not available in this pass: the session's WebSearch budget (200/200) was used up, and arxiv.org, export.arxiv.org, crossref, openalex and docs.aws.amazon.com were blocked by the proxy. So the prior-art list below comes from memory and should be checked before anyone relies on it. (1) The idea that admins deliberately delay patches to test for breakage is already well documented, though only through interviews and surveys: Li et al., "Keepers of the Machines" (SOUPS 2019); Tiefenau et al. on sysadmin update behavior (SOUPS 2020); Pashchenko et al. (CCS 2020), where developers avoid dependency updates for fear of breaking changes; Kula et al. (EMSE 2018); and Dissanayake et al. (CSCW 2022), who found coordination dominates. Showing that "rings/deferrals exist" is therefore not news. The only new thing would be a technical measurement. (2) Mining dependency-bot configs and ignore rules: He et al., "Automating Dependency Updates in Practice: Dependabot" (TSE 2023) already studied ignore rules, schedules and why projects turn the bot off. Alfadel et al. (MSR 2021) studied why Dependabot security PRs don't get merged. (3) Deferral that is motivated by something other than breakage: the 2025 "dependency cooldown" movement (Dependabot cooldown, Renovate minimumReleaseAge, pnpm/uv release-age gates; Woodruff's "We should all be using dependency cooldowns") presents configured waits as defense against supply-chain attacks, not fear of breakage. (4) Vendor defaults: AWS predefined patch baselines already auto-approve after about 7 days, and Windows Autopatch and Microsoft's WUfB guidance prescribe staggered rings (Test/First/Fast/Broad). The prod-vs-pilot gap is therefore mostly copied vendor best practice, not a choice each org makes. (5) The lab counterfactual (apply the fix, run the project's own tests) is essentially Round-1 idea (a), and the breaking-update literature (BUMP benchmark 2024; Ochoa et al. on Maven breaking changes) covers it. What I checked directly with GitHub code search: approve_after_days in .tf files has 167 hits (not 374). The most common value is 7, which matches the AWS default; 2 of 30 sampled hits reference environments or prod, and most paths are modules, examples, variables or catalog files. The top 50 hits for qualityUpdatesDeferralPeriodInDays (468 total) come from 21 distinct repos: Microsoft Graph SDKs in 5 languages, API docs, Packt Intune cookbooks, Microsoft365DSC, IntuneManagement, CIPP, mondoo, OpenIntuneBaseline. That is roughly zero operational org policies. In a sample of 40 .trivyignore hits containing "break", 23 were misconfiguration waivers (Dockerfile USER / non-root / privileged / writable rootfs), not CVE patches. Only 10 carried a CVE/GHSA/PYSEC id, and 7 described a KNOWN breaking change (major bump, ESM-only, API removed). Several comments read as agent-written boilerplate from 2026.

### C11 — The Plan Says Nothing Breaks: infrastructure code as a proof lab (plan verdicts, ForceNew flips, firewall rules) (score 1.29, dead)

**Best headline:** Same bot PR, same repo: when a Terraform plan proved it changed nothing, it merged in a median of A hours. When the plan could not run, it waited B days. Across N public repos, the same 'close 0.0.0.0/0' fix waited X times longer while Terraform labelled it destroy-and-recreate than after a provider upgrade relabelled it update-in-place.

**Skeptic's flaws:** 1. The main comparison measures CI mechanics, not uncertainty. In public repos, "unproven" means the plan check failed. That is a red, usually required status check, and it blocks both Renovate automerge and branch-protected merges. "Proven no-op" PRs are often merged by tooling configured to do exactly that (tfaction auto-merges no-change plans; Renovate automerge requires green checks). The A-hours vs B-days gap is therefore built in by configuration, and it mostly measures how long it takes to repair broken CI credentials or locks. Expired credentials also mark periods when a repo is neglected. A critic dismisses this in one sentence. Public data doesn't show which checks were required at the time.
2. The "proof" is not a proof about the fix. Most "No changes" plans sit on PRs that never touch Terraform (Java, Node or GitHub Actions bumps in app repos, e.g. hmcts). A no-op plan there is trivially true and says nothing about whether the change is safe. The candidate admits a plan proves an infrastructure no-op, not application safety.
3. These aren't security fixes. Almost all 29.8k PRs are routine version bumps, and roughly tens are security PRs. The headline "bot fixes" would really be about maintenance bumps, in hobby and one-government-org repos, so the result says little about enterprise remediation.
4. Arms 2 and 3 confuse a known cost with uncertainty. A plan showing destroy/replace is certainty of disruption, not uncertainty about it. The ElastiCache ForceNew flip in v5.47.0 followed a real AWS API capability, tied to engine-version conditions, so the real cost of the fix changed too, not just the displayed risk. Choosing aws_security_group_rule vs aws_vpc_security_group_ingress_rule is itself a marker of team maturity (selection). Open SSH, a missing description and an encryption change differ in severity and effort as well. If these arms find a gap, they support "the fix is costly", which is the opposite of belief 2.
5. Arms 2 and 3 have almost no statistical power. Public repos that have the exact insecure attribute, sit in production (not demos), and cross the provider version will number single digits to low tens. Security-group tightening commits aren't bot fixes, so the "identical fix" framing fails. "Consumers cannot be known" has no public measure.
6. It cannot really falsify belief 2. The gap is guaranteed by automation mechanics, so finding one confirms nothing and "no gap" is unlikely. The study also lands on network/firewall and IaC, wedge A, which the interviews didn't support, rather than OS/package patching (wedge B).

**Prior art found:** My web search budget was already used up, and arxiv, Semantic Scholar, OpenAlex, Crossref, DBLP and DuckDuckGo are all blocked by the proxy. So I checked prior art from memory and checked the data with GitHub search.
(1) The core design is a special case of Round-1 idea (a), which merges bot PRs by CI red vs green. A Terraform plan verdict is just one more CI signal. Published work on why bot PRs merge or don't, and on failed CI blocking them, already covers this ground: Mirhosseini & Parnin (ASE 2017), Alfadel et al. on Dependabot security PRs (SANER 2021), Rombaut et al. on Greenkeeper (TOSEM 2023), and He et al. on Dependabot (TOSEM 2023). I know of no paper that uses the plan verdict itself as the treatment, so that narrow angle is new.
(2) How long IaC security smells survive, and how Terraform security practices are adopted, is well studied. Examples: Rahman et al., "Seven Sins" (ICSE 2019; smells lasting up to 98 months); Rahman et al. on Ansible/Chef (TOSEM 2021); GLITCH (ASE 2022); Verdet et al. on Terraform security practices and policy adoption across cloud providers (EMSE 2023–24); the TerraDS dataset (MSR 2025). Arm 3 (how long open-SSH or missing-encryption findings take to fix in public .tf files) is an incremental extension of this work.
(3) Bypassing a Cloudflare origin through a stale or over-broad Cloudflare allowlist has already been published (Certitude 2024, "Cloudflare protection bypass using Cloudflare"). Also, 104.16.0.0/12 still maps to AS13335 (104.28.0.0/14 is WARP egress), so the planned "retired ranges now belong to other networks" check will likely come back empty.
Data checks on GitHub:
- Renovate PRs with a "No changes. Your infrastructure matches…" comment: 29,766 (confirmed). About 8.9k (30%) come from one org, hmcts, whose Jenkins pipeline posts a plan on every PR, including Java and Node bumps. The rest are dominated by homelabs and demos.
- Security PRs among them: only 24 carry label:security, and a "Vulnerability Alerts" body search returns 73, mostly non-security. So the security fixes in this dataset number in the tens.
- The "unproven" control arm is tiny: about 157 PRs with state-lock errors and about 156 with credential errors, clustered in a few repos (koyashiro/infra, antonio-bravo/GitHubActions-matrix).
- 104.16.0.0/12 appears in only 17 .tf files, mostly demos (test-terraform, 202003-immutable-infrastructure-vault). The claimed 3,760 files are mostly docs and nginx configs.
- GH Archive payloads are trimmed after Oct 2025, as the candidate itself notes.

### X7 — Dead Range, Live Rule: does anyone delete a firewall rule the vendor has already declared dead? (the Firewall Ratchet) (score 1.26, dead)

**Best headline:** Cloudflare retired 104.16.0.0/12 in 2021 and warned that part of it would carry untrusted WARP traffic. Five years later, N public configs still trust it. Among engineers who reopened that exact list to add Cloudflare's replacement ranges, X% kept the dead one (Y% in firewall allowlists vs Z% in log/real-IP settings), and configs that dropped it automatically broke W of M times.

**Skeptic's flaws:** 1. The oracle only holds in one context, which breaks the gradient. 104.16.0.0/12 is still Cloudflare-owned address space (AS13335). The retirement applies only to "Cloudflare proxy -> origin trust". I checked all 100 visible hits of the 236 "both ranges" files. Most are client-side routing and bypass lists (Zapret/AntiZapret ipsets, Quantumult/Shadowrocket/Surge rules, mikrotik and xray routes), WAF-enumeration and hacking cheatsheets, CF speed-test tools, and proxy/WARP detectors. In those files, keeping /12 is correct, not fearful. The "inert/intel" arm therefore differs in truth value, not in stakes, so the three-way gradient collapses.

2. The stakes and security-value orderings are assigned by the researcher and can be contested, so the rival predictions are not opposite in sign.
   - A stale set_real_ip_from lets anyone on WARP spoof their client IP directly. That is arguably the highest security value of deletion, not the lowest.
   - A wrongly configured real-IP setting routinely makes fail2ban or rate limiters ban Cloudflare edge IPs, which is a site-wide outage, so "costs nothing" is false.
   - Engineers' perceived stakes can't be measured without asking them, which the constraints forbid. This cannot be fixed.

3. The design cannot falsify belief 2 as framed. Cloudflare explicitly certified the change: "This change is safe to make today". That removes the uncertainty. So a low keep rate after a touch, which the pilot already hints at (about 2.3%), is equally consistent with "proof exists, so people act" (pro-thesis) and with "visibility/unknown asset" (anti-thesis). A high keep rate is the only discriminating outcome, and the data point away from it. There is also no arm without certification.

4. Awareness is not held fixed. Adding /13 and /14 does not show the author noticed that /12 was removed. It is equally consistent with additive copying of "new lines" and with not knowing CIDR containment. Among the "keeps" I inspected, the /12 was commented out, not live: vesta's ubuntu/24.04 nginx.conf ("#set_real_ip_from 104.16.0.0/12") and jempe's ufw script ("#ufw allow from 104.16.0.0/12"). String counts overstate "still trusts".

5. Power is effectively nil.
   - Enforcing stratum: 32 files, including blog posts, docs and one copy-pasted Tezos/Chainlink academy template family, so roughly 15 lineages. Enforcing-context touch events will be single digits.
   - Real-IP stratum: 18 of 18 sampled set_real_ip_from files were live /12 with no /13 or /14, so they were never touched.
   - Repo and author fixed effects with within-commit contrasts are infeasible.

6. Repo state is not deployed state, and this is concrete, not hypothetical. centminmod's config/nginx/cloudflare.conf still holds a live /12 on its default branch. But its tools/csfcf.sh curls cloudflare.com/ips-v4 and regenerates /usr/local/nginx/conf/cloudflare.conf at runtime. A static trace would count an auto-synced deployment as a "never-touched dead rule". Most of the population are templates (lempstack, bypanel, VirtuBox, pothi) or abandoned hobby repos, so "dead-rule-years" measures repo abandonment.

7. The breakage arm is predetermined. The removed /14 never carried proxy traffic, so realized breakage is about 0 by construction and says nothing about whether blast radius can be predicted, which is the actual gap.

8. It is off-strategy for the goal:
   - Wedge A had zero interview support.
   - The population is homelab-skewed.
   - The security impact is modest: the origin IP must be reachable and known, and Cloudflare allowlisting is already bypassable via other tenants.
   - The likely honest headline, "people who touch the list delete it; dead rules sit in files nobody opens", argues for the unknown-asset/visibility rival. It does not show that remediation is urgent or delayed by uncertainty.

Legality is fine: public code, no probing, aggregate reporting, coordinated disclosure. Legality is not the problem.

**Prior art found:** Web search budget was exhausted and scholarly APIs (Semantic Scholar, OpenAlex, dblp, arXiv, Crossref) plus cloudflare.com and archive.org were blocked by the proxy, so the literature check relied on GitHub search and memory only.

Checked on GitHub:
- Retirement oracle, now stronger than claimed. Commit 04bf5fc (outroll/vesta, 2021-04-09) reproduces Cloudflare's customer email: "[Action May Be Required] ... please make the following changes to your allow list by May 7, 2021. This change is safe to make today. Remove: 104.16.0.0/12  Add: 104.16.0.0/13, 104.24.0.0/14". Same-week commits (c-rack/plug_cloudflare 2021-04-08, rhymix 2021-04-09, theregister/nginx-cloudflare 2021-04-09 "as communicated by Cloudflare over e-mail", centminmod 2021-04-14) confirm the date. Public repos now label 104.28.0.0/14 as "WARP / iCloud Private Relay egress", so the consequence is real.
- Pilot counts reproduced: files with both "104.16.0.0/12" and "104.24.0.0/14" = 236 exactly; "allow 104.16.0.0/12" = 32; "set_real_ip_from 104.16.0.0/12" = 397.

Prior art from memory, not re-verified:
- Stale feature-flag debt: Ramanathan et al., Piranha, ICSE-SEIP 2020; Meinicke et al., MSR 2020. People failing to delete config that is known to be dead is an established SE topic.
- Firewall change-impact analysis: Liu et al., ESORICS 2007 / TOIT. Predicting the blast radius of a firewall-rule change is a solved-in-principle problem, which weakens wedge A as a proof moat.
- Wool 2004/2010 on firewall configuration errors; vendor telemetry and surveys from FireMon, AlgoSec and Tufin already claim "fear of breaking" as the top reason rules aren't removed. The folk claim has been asserted before, though not with real-artifact causal evidence.
- Origin-allowlist weakness: Certitude, circa 2024, showed that Cloudflare-IP allowlisting can be bypassed from other tenants.
- Pauley et al. (S&P 2022 / USENIX Sec 2023) on latent configs and IP reuse; Borgolte et al. (NDSS 2018) on dangling DNS.

I found no study that uses a vendor-certified range retirement plus edit-conditioning plus a stakes gradient. The exact design looks novel; the underlying phenomenon does not.

### C17 — The Stand-Still Bill: money paid for the right not to change, and what the proof bought (score 1.21, dead)

**Best headline:** Public agencies paid $X across N contracts to keep Windows Server 2012 alive after its end of support, while licensed to upgrade. When the price rose K× in the final year, Y% of seats renewed anyway, so demand barely moved.

**Skeptic's flaws:** 1. It measures the wrong thing. ESU and EUS buyers keep getting security patches every month. What they avoid is a major-version migration (new OS or platform, TPM 2.0 hardware, re-certified third-party apps). So the data shows organizations patching as long as the patch is vendor-guaranteed, which works against "can't remediate fast enough". It is also not wedge B (patching OS packages). The headline says nothing about exploit urgency or remediation delay.

2. The elasticity test cannot tell the hypotheses apart. ESU price steps are announced years ahead and fall on calendar dates, so any drop in seats is confounded with the migration progress that was going to happen anyway. There is no counterfactual price path. Seats that don't respond to price are also exactly what the rival explanations predict: migrations take more than a year to deliver, ESU costs little next to migration, and appropriations lag. The stated falsification rule is lopsided: inelastic seats would be read as "fear", when "known heavy work" predicts the same thing.

3. The bunching test is confounded. The Windows Server 2012 and Windows 10 ESU anniversaries (Oct 10–14) sit about two weeks after the US federal fiscal year starts on Oct 1. So any bunching of migration buys "before the price step" lands on the documented September year-end spending surge (Liebman & Mahoney, AER 2017).

4. The key data mostly doesn't exist in the named sources. FPDS and USAspending have no SKU or seat-count fields. ESU is usually bought as an add-on to an Enterprise Agreement through large resellers or government-wide vehicles (SEWP, DoD ESI), so it doesn't appear on its own. That means "Y% of seats bought in the final year" and within-buyer retention cannot be measured. J&As exist to justify sole-sourcing under FAR 6.302-1, so their stated reason will almost always be the boilerplate "only Microsoft can supply updates", not why the agency didn't migrate. The reason-coding therefore reads the legal template, not the real motive.

5. "Unknown whether it breaks" can't be separated from "known to break". J&A and FOI text such as "legacy application not supported on the newer OS" describes a known incompatibility, i.e. known work, not uncertainty. Nothing in the design separates the two.

6. The FIPS arm is confounded by compliance, and it has no outcome variable. Organizations run the frozen 'fips' stream because auditors or FedRAMP require the validated module. That is regulatory proof, not predicting breakage. Who is enrolled in which stream is private. Code-search counts are one snapshot of repositories, not deployments over time. Using CMVP queue time as an instrument breaks the exclusion restriction, because certificate events are the compliance outcome itself.

7. The RHEL EUS arm is driven by SAP and Oracle certifying specific minor releases, which is also compliance with vendor support. EUS prices are mostly bundled (for example in RHEL for SAP) and not public.

8. The UK FOI arm (2) asks officials to interpret ("which gate came right before rollout"). FOI covers recorded information only. In practice this is a self-reported survey, which breaks the "technical evidence only" constraint, and it invites refusals under s.24/s.31 (national security, law enforcement).

9. Timing and population. Windows Server 2012 ESU ends Oct 13, 2026, 17 days from today, so a 6–10 week study (plus months of FOI) misses the hook. The public sector is also not the FDA-regulated medical-device design partner.

10. Likely result. GAO has already found funding and planning to be the dominant reasons, so the most probable outcome is that Belief 2 is falsified with weak, uncontrolled evidence, not a crisp viral number.

**Prior art found:** Verification limits: the web-search budget for this session was used up, and the egress proxy blocked usaspending.gov, sam.gov, whatdotheyknow.com, learn.microsoft.com, gao.gov, TED, Contracts Finder, sec-certs and the academic indexes. The only source I could check live was ubuntu.com. Everything below that I did not check live comes from my own knowledge and should be read that way.

Checked live: Ubuntu really does run two FIPS streams. Canonical's docs say 'fips' holds "the exact packages validated by NIST" and 'fips-updates' holds the same packages "updated with security fixes". The USN API currently returns 126 FIPS kernel notices; the candidate counted 125. So the FIPS data claim holds.

Prior art for the headline "public bodies paid $X not to upgrade" (from knowledge). This is an old, repeated news story:
- the UK government's roughly £5.5m Windows XP custom-support deal (2014);
- the US Navy's roughly $9.1m XP custom-support contract (2015);
- the Dutch government's XP support deal (2015);
- the German federal government paying about €800k for Windows 7 ESU (2020, disclosed in answer to a parliamentary question);
- recurring FOI-based press surveys of UK councils and NHS trusts still running XP, 7 or 10 (Comparitech, The Register and others).

The reasons have also been covered. GAO's legacy-IT series (GAO-16-696T, GAO-19-471, GAO-25-107795) records why agencies keep legacy systems. It mostly points to funding, a lack of modernization plans, and O&M lock-in, not to fear of breakage. That is a published prior answer against Belief 2.

The FIPS criticism (validated modules frozen while CVEs pile up) is a well-known complaint among practitioners. A systematic count of CVEs fixed only in 'fips-updates' may be new.

What looks new: the within-buyer price-elasticity analysis and the pre-registered coding of J&A reasons.

### P7 — Deviation Files → the Grid's Excuse Ledger: why regulated utilities miss a legal 35-day patch clock (score 1.18, dead)

**Best headline:** We coded all N public US power-grid patch-rule violations (2010-2020): X% involved assets or patch sources nobody was tracking, and only Y% involved a patch held back for fear of breaking operations. On the legal clock, the grid's patching problem is inventory, not nerve.

**Skeptic's flaws:** 1) The dataset is filtered on the outcome, and that problem can't be fixed. CIP-007-6 R2.3 and R2.4 give a compliant way to defer a patch: a dated mitigation plan, which can be revised with CIP Senior Manager approval. A utility that holds a patch for years because it fears breakage, or is waiting on vendor qualification, is fully compliant and never shows up as a violation. So the violations corpus is the set of process failures (tracking, evaluation, paperwork) almost by definition. That makes 'asset or tracking causes dominate' close to guaranteed by how the regulation is built. It tells us nothing about why patches actually wait.

2) The falsification rule doesn't work. 'Uncertainty under 10% means falsified' reads the rule's design as evidence against belief 2. The candidate itself calls the result a lower bound, and a lower bound cannot falsify anything. And 'plurality within R2.3/R2.4 and at least twice the placebo rate' is almost impossible to reach for the same reason. The test is biased from the start and can neither support nor falsify belief 2 credibly.

3) The duration metric measures the wrong thing. NOP start and end dates are the violation window: noncompliance begins (often the date the standard took effect), then someone finds it (usually an internal review or audit), then compliance is restored (often by filing a mitigation plan after the fact, not by applying the patch). Kaplan–Meier curves by cause would therefore measure how long detection and enforcement took, not how long a patch waited. 'Stayed open Z days longer' can't be defended.

4) The contrasts are confounded. High-impact entities (CIP-010 R1.5 test environments) differ from Medium ones in size, staffing, EMS vendor and audit intensity, and there are only a few dozen of them. The v3-to-v5 comparison is swamped by the 2016 scope expansion and the transition-era wave of violations. The EMS outage 'join' is ecological, with no link between entities, so it is a fact placed next to the result, not evidence of cause.

5) The placebo isn't clean. Revoking access under CIP-004 can also break production, service accounts for example.

6) The construct is ambiguous. In OT, waiting for vendor qualification is also a contractual rule (applying an unqualified patch voids support), so a critic can call it vendor lock or liability rather than impact uncertainty.

7) The data are thin and dated. The public detail stops around 2020, so it is 6+ years old. The narratives are written by enforcement staff in stock root-cause language ('inadequate internal controls'). The findings are specific to grid OT, far from wedge B and the medical-device design partner.

8) It has no viral hook. A niche regulatory reading exercise whose most likely headline undercuts the thesis is not a stunt that cuts through industry noise.

Legality is fine (public, anonymized filings, no CEII, no de-anonymization), and it is cheap. Legality is not the problem; validity is.

**Prior art found:** I could not check anything live. The WebSearch budget for this session was used up (200/200), and the proxy blocked nerc.com, ferc.gov, rfirst.org, whitecase.com, arxiv and wikipedia. Everything below comes from memory and is unverified, and I have scored harshly because of that.

1) Regulators already analyse this corpus. NERC's CMEP annual reports and the regional entities' newsletters and webinars (ReliabilityFirst, WECC, SERC) have for years named CIP-007 R2 as one of the most-violated CIP requirements. They also publish the recurring 'themes': incomplete asset inventory, patch sources missing from tracking, manual spreadsheets and tool failures, and missed 35-day evaluations. That already goes a long way toward the likely headline, 'X% were assets or patch sources nobody tracked'.

2) The FOIA-based compilations of CIP violations by Michael Mabee / Protect Our Power, and the heavily analysed 2019 Duke Energy $10M settlement covering 127 violations, many of them patch-related, cover the same records.

3) NERC's reports on lost EMS functions already publish the share of events caused by software, database and update changes. The 'W% of outages caused by changes' number would just restate them.

4) Inside this tournament, the 'excuse ledger' and 'compelled-reason legal corpus' ideas from Round 2 and the original P7 already cover the concept of coding stated reasons for deferring a patch. This is a sharper version of those, not a new idea.

On data: the candidate's claims (anonymized NERC Spreadsheet NOP/FFT/CE postings with narratives, FERC eLibrary NP dockets, the AD19-18 disclosure change ending public CIP detail around 2020) match what I know. I could not confirm any of them here.
