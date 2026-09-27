# 03 — Population and company filter

How future agents obtain the candidate repos and PRs, how an owner is classified as a company, how
a repo is classified as a deployed service, how the classifier is validated, and how many units to
expect. **Everything in §2–§5 is frozen in the OSF pre-registration before any outcome (merge or
close timing, revert) of the company sample is computed.** Agents may compute counts of *opened*
PRs and owner/repo attributes before registration; they may not look at merge outcomes.

Data sources referenced as S1–S17 are specified in `02-data-sources.md`.

---

## 1. Units

| unit | definition |
|---|---|
| **fix PR** | a pull request opened by `dependabot[bot]` or `renovate[bot]` (Mend-hosted app) that updates **one** dependency to a version that fixes a published advisory (classification §6) |
| **repo** | the GitHub repository receiving the PR; excluded if fork, archived, template, or mirror |
| **owner** | the GitHub account owning the repo: an `Organization` or a `User` |
| **company owner** | an Organization classified Tier A or Tier B (§3) |
| **deployed-service repo** | a repo meeting the frozen deployed-service rule (§4) |
| **headline stratum** | fix PRs in **Tier A** × **deployed-service** repos, human-active, no automerge at PR open |

Individuals' repos (`User` owners) and non-company Organizations are **never** in headline results.
They may be analysed as a clearly labelled, pre-registered secondary comparison (§7).

## 2. Discovery pipeline (no GitHub Search)

```
GH Archive (BigQuery, S1)                                           outputs (Parquet)
 ├─ D1  scan each month once; keep PullRequestEvent / Review / IssueComment
 │      rows (header + a few payload fields) for org-owned repos,          gha_events_<YYYYMM>
 │      plus a 5% hash sample of user-owned repos
 ├─ D2  bot PR opens: actor in {dependabot[bot], renovate[bot]},
 │      action = 'opened' → (repo_id, repo_name, org_login, number,       bot_pr_skeleton
 │      head_ref, created_at)
 ├─ D3  cheap security pre-filter from head_ref (no API):
 │      Renovate: head_ref ends '-vulnerability'
 │      Dependabot: parse <ecosystem>/<...>/<dep>-<version>; keep if
 │      (ecosystem, dep, version) is a 'fixed' event in S6/S7              candidate_fix_prs
 ├─ D4  distinct org_login → org classification (§3)                      owners
 ├─ D5  repos of Tier A/B orgs → deployed-service filter (§4)             repos
 └─ D6  PR hydration via GraphQL (S3) for PRs in A/B deployed repos
        (+ sampled comparison groups) → final security classification (§6),
        CI state, automerge, merge/close, edits, timeline                 prs (outcomes MASKED until registration)
```

Notes:
- **Why GH Archive first:** it enumerates every public bot PR without Search limits; the `org`
  column identifies org-owned repos for free; bot PR opens are identifiable from `actor.login`.
- **Post-2025-10-07 trim** (02 §S1): the PR payload keeps only `id, url, number, head, base`. D3 relies
  on `head.ref` surviving; Step 0 confirms it. If `head.ref` is gone, D3 is skipped and hydration
  (D6) runs on all bot PRs of Tier A/B deployed repos instead (more API calls, still feasible:
  GraphQL batches of 25–50 PRs).
- **Pre-trim window** (2025-01-01..2025-10-06): payloads include title, body, user, `merged`,
  `merged_by`; hydration is needed only for CI state at head. This window is used for the
  retrospective analyses (D1, H5-retro, H6-retro).
- **Prospective window** (16 weeks from logger start): D2–D6 run hourly-to-daily on the newest GH
  Archive day tables (or, if GH Archive lags, on a repo watch-list polled via GraphQL — see 05 Step 6).
- The **advisory pre-filter** is keyed on to-version = a `fixed` version of an advisory affecting that
  package; final classification (§6) additionally checks from-version ∈ vulnerable range.

## 3. Company classification

### 3.1 Why "Organization" is not enough
A GitHub Organization can be a company, an OSS community, a foundation, a university lab, a
government body, a hobby group, or one person's side project. In the tournament's small sample of
Renovate security-PR owners, Organizations included both companies and a fintech open-source
foundation. The filter must separate them with evidence that exists outside GitHub.

### 3.2 Tiers (frozen rule)

Let `org` be the Organization profile from REST `GET /orgs/{org}` (S2) and `D_web`, `D_mail` the
registrable domains (Public Suffix List, S13) of `org.blog` and `org.email`.

**Tier A — high confidence company** = `org.is_verified == true` AND at least one registry link:
- **A1 (Wikidata by account):** a Wikidata item has `P2037` (GitHub username) equal to `org.login`
  (case-insensitive) AND its `P31` class is in the subclass closure of *business* (Q4830453) AND not
  in the closure of the non-profit / academic / government classes (nonprofit organization,
  foundation, university, research institute, government agency, open-source project, software).
- **A2 (Wikidata by domain):** a Wikidata item of a business class (as above) has `P856` (official
  website) whose registrable domain equals `D_web` or `D_mail`.
- **A3 (legal-entity registry by name):** no Wikidata match, but the org's display name (or the
  `<title>`-free brand in `D_web` — no web crawling; use the name only) matches exactly, after
  normalisation (case, punctuation, legal suffixes such as Inc/Ltd/GmbH/SAS/BV removed), an
  **active** GLEIF LEI record whose legal form (ELF code) is a for-profit form, or an OpenCorporates
  active company (validation sample only). A3 is reported as part of Tier A but flagged; a
  sensitivity analysis drops it (A1+A2 only).

Because GitHub shows the Verified badge only when the profile website and email match verified
domains (02 §S2), `is_verified` guarantees that `D_web`/`D_mail` are controlled by the org. The
registry link guarantees that the domain/account belongs to a business, not a community.

**Tier B — likely company** = Organization, not Tier A, AND the commit-email rule:
- Take commits on the default branch of the org's up to 5 most recently pushed non-fork repos, in
  the 180 days before the PR window starts (GraphQL `history(first:100){ nodes { author { email
  user { __typename } } } }`, or pre-trim GH Archive PushEvent `commits[].author.email` for 2025).
- Drop bots (`[bot]`, `__typename != User`, known bot emails), GitHub noreply addresses
  (`@users.noreply.github.com`), and addresses on a frozen **exclusion list**: free-mail providers
  (gmail.com, outlook.com, hotmail.com, yahoo.*, icloud.com, proton.me/protonmail.com, qq.com,
  163.com, gmx.*, yandex.*, mail.ru, etc.), academic (`.edu`, `.ac.*`, known university domains),
  government (`.gov`, `.gov.*`, `.mil`), and OSS foundations/communities (apache.org,
  linuxfoundation.org, eclipse.org, python.org, mozilla.org-community aliases, etc.; list frozen in
  the registration).
- Tier B if **≥3 distinct human authors remain** AND **≥50%** of them share one registrable domain
  `D_c`, AND (`D_c` = `D_web` OR `D_c` = `D_mail` OR no profile domain exists).
- Only the domain is kept; the local part of each email is discarded in memory and never stored
  (07 §GDPR). This follows the premise of Spinellis et al., MSR 2020 ("A Dataset of
  Enterprise-Driven Open Source Software"; 17,252 enterprise projects; 89% accuracy on a manual
  sample — VERIFIED-SNIPPET), adapted to owners instead of projects.

**Tier C — not classified as company**: all other Organizations. **Tier U**: User accounts.

Main analyses use **Tier A**. **A+B** is the pre-registered robustness sample. If the Step-3 gate
(05) shows Tier A is too small, the pre-registered fallback in `04-analysis-design.md` §8 applies —
the founder must pick it before registration (README decision D1).

### 3.3 Mechanisms verified vs to verify

| mechanism | status |
|---|---|
| `is_verified` in REST org schema; `isVerified` in GraphQL Organization | VERIFIED (schema) |
| Verified badge requires website and email to match verified domains; available on free plans | VERIFIED (github/docs source) |
| `is_verified` returned to a non-member token for all orgs | UNVERIFIED → Step 0 on 20 known orgs |
| GraphQL `Organization.domains` readable by non-admins | UNVERIFIED, assume **no** |
| Wikidata P2037 GitHub username, P1278 LEI, P1320 OpenCorporates ID | VERIFIED-SNIPPET |
| Wikidata P31/P279/P856 and class Q-ids | UNVERIFIED (memory) → Step 0 label lookup |
| Share of verified orgs; Wikidata coverage of company GitHub accounts | UNKNOWN → Step 3 counts |
| GLEIF has no website field (name-only matching) | UNVERIFIED |
| Commit author emails via GraphQL `author.email` for public repos | schema VERIFIED; values UNVERIFIED |

## 4. Deployed-service filter

Public company repos are mostly libraries, SDKs, docs and examples; the thesis is about production
blast radius. A repo is a **deployed service** if (frozen rule):

**(S4) Deployment evidence** — GraphQL `repository.deployments(last:20)` shows ≥1 deployment in the
180 days before PR open to an environment whose name matches
`(?i)^(prod|production|live|main|www|app|api)([-_ ].*)?$` or the repo has an `environments` entry
with such a name that has a protection rule;
**OR (S2 ∧ (S1 ∨ S3))**:
- **S1 container:** a `Dockerfile`, `Containerfile`, or `*.dockerfile` exists at root or in
  `deploy/`, `docker/`, `build/`, `infra/`, `ops/`;
- **S2 CD workflow:** a `.github/workflows/*.y*ml` file triggered on `push` to the default branch or
  on `release`/`workflow_dispatch` that contains a deploy step matching a frozen regex list, e.g.
  `kubectl (apply|rollout|set image)`, `helm (upgrade|install)`, `terraform apply`, `pulumi up`,
  `aws ecs update-service`, `aws lambda update-function-code`, `serverless deploy`, `sam deploy`,
  `gcloud (run|app|functions) deploy`, `az (webapp|containerapp|functionapp)`, `flyctl deploy`,
  `railway up`, `vercel .*--prod`, `netlify deploy .*--prod`, `docker push` to a non-Docker-Hub
  registry followed by an `environment:` key, `argocd app sync`, `cf push`; or a job with
  `environment: production`-like name (regex above);
- **S3 infra-as-code:** `*.tf`, `Pulumi.yaml`, `kustomization.yaml`, `Chart.yaml`, k8s manifests
  (`apiVersion:` + `kind: Deployment|StatefulSet|Service`), `serverless.yml`, `fly.toml`,
  `render.yaml`, `app.yaml` (App Engine), `Procfile`, `vercel.json`, `netlify.toml`;

**AND NOT library-only (S5):** the repo is **not** the source of a package published to a public
registry in the last 2 years (deps.dev project→package mapping, S15; fallback: registry metadata
`repository` URL) **unless** S4 holds. A monorepo that both publishes packages and deploys (S4) is
kept.

Files are read with GraphQL `object(expression:"HEAD:")` (root tree) and
`object(expression:"HEAD:.github/workflows")` plus targeted blob reads — 2–6 points per repo. No
code search, no cloning.

**"Build in public" sub-stratum** (descriptive only, not a separate filter): Tier A deployed repos
whose org's website domain equals the product's service domain (`homepageUrl` registrable domain =
`D_web`). Reported as a subgroup; not used for inference unless pre-registered with ≥30 repos.

## 5. Other frozen eligibility rules

| rule | definition | why |
|---|---|---|
| human-active repo | ≥1 PR (any author) merged by a `User` (not Bot) in the repo in the 30 days before PR open | a human was around to merge |
| no automerge at PR open | no `autoMergeRequest` enabled within 1 h of open; no workflow at PR open that calls `gh pr merge --auto`, `enable-pull-request-automerge`, or gates on `fetch-metadata` outputs; no `automerge: true` in the resolved Renovate config; PR not merged by a Bot | excludes machine decisions |
| single dependency | Dependabot not grouped (title "Bump X from A to B", one package); Renovate `groupName` null / one package in body table | fix is identical across repos |
| patch/minor | semver jump of to vs from is patch or minor (major kept for descriptive only) | |
| own CI green at head | `statusCheckRollup.state == SUCCESS` at the PR's head commit at the measured time; repos with no checks at all are a separate stratum ("no CI") | "proven safe" needs the owner's own tests |
| PR not draft, base = default branch | | |

## 6. Security classification (final, after hydration)

- **Renovate:** head ref ends `-vulnerability` or title contains `[SECURITY]`, and body contains a
  GHSA/CVE id; drop grouped PRs.
- **Dependabot:** parse `Bump <pkg> from <A> to <B>` (and `in /<dir>`); security if `A` ∈ an
  advisory's vulnerable range for (ecosystem, pkg) AND `B` equals the advisory's first `fixed`
  version (Dependabot targets the minimum patched version — 02 §S4). Version updates that happen to
  fix an advisory are labelled `incidental_fix` and kept for a sensitivity analysis only.
- **Validation:** 200 hand-checked PRs (stratified by ecosystem and bot), plus repos that label
  security PRs (e.g. a `security` label) as a silver standard. Report precision/recall.

## 7. Secondary comparison groups (optional; founder decision D3)

- **Tier C** (non-company Organizations) and **Tier U** (individuals): a 5% deterministic hash sample
  of repos (by `repo_id`), same eligibility rules, same deployed-service rule where applicable
  (individuals rarely pass it; report the count).
- Pre-registered secondary hypothesis H7 (04): for the **same fix** (fix fixed effects), time-to-merge
  among human-active, green, no-automerge PRs is longer in Tier A than in Tier U. The thesis predicts
  "yes" (someone answers for the blast radius); a "no" is reported, not buried.
- Comparison groups are **never** pooled into headline estimates.

## 8. Validation protocol for the company classifier

Goal: precision and recall of Tier A, Tier B and A+B for the construct "the repo owner is a
for-profit business", measured before registration and reported in the paper.

1. **Sampling frame:** all Organizations that own ≥1 candidate fix PR in the discovery window.
2. **Sample of ~300 owners**, drawn by a seeded script:
   - 100 predicted Tier A, 100 predicted Tier B, 100 predicted Tier C — for precision;
   - the Tier C draw is also used to estimate recall (companies missed), with inverse-probability
     weights back to the population shares of each predicted tier.
3. **Blind labelling:** each owner shown as login + profile fields + org website (opened by a human
   in a browser) + registry search results; the predicted tier is hidden. Labels: `company`
   (for-profit legal entity selling products/services; subsidiaries count), `nonprofit/foundation`,
   `academic`, `government`, `community/OSS project`, `individual-in-org`, `unknown`. Evidence URL
   recorded for every label.
4. **Two raters** (founder + second person, or founder + LLM pre-label that the founder
   confirms/overrides — founder decision D4). Report Cohen's kappa on a 60-owner overlap; resolve
   disagreements by discussion; `unknown` counted as not-company for precision.
5. **Metrics:** precision (Tier A, Tier B, A+B), weighted recall, F1, with Wilson 95% CIs; confusion
   by class (which non-companies leak in).
6. **Acceptance bar (pre-registered):** Tier A precision ≥ 0.90 (lower CI bound ≥ 0.80). If missed,
   the rule may be tightened **once** (e.g., drop A3) before registration; the change and both
   precisions are reported.
7. **Deployed-service validation:** 150 repos (75 predicted service, 75 predicted not), labelled from
   the README/workflows by a human: `deployed service`, `library/SDK`, `docs/examples`, `other`.
   Precision bar ≥ 0.80.
8. **Frozen after validation:** the exact regexes, lists, thresholds and code commit hash go into the
   registration.

Time: ~3 min per owner, ~2 min per repo → ~15 h + ~5 h of human labelling.

## 9. Expected counts (planning estimates — replace with measured values in Step 3)

**Measured anchors** (small read-only checks; all owner types, not only companies):
- Renovate: **1,300** PRs by `app/renovate` with `[SECURITY]` in the title created 2026-09-14..20
  (GitHub PR search `total_count`, 2026-09-27; case-insensitive, includes grouped PRs). The
  tournament counted 1,044 for 2026-09-18..24 and 543 for 2026-09-20..26 (different windows/queries).
- Dependabot: **317,204** PRs whose body contains "Dependabot compatibility score" created
  2026-09-20..26 (tournament, GitHub search; all update types, not only security).
- Rombaut et al.: 83% of Dependabot updates have no computable score (02 §S4).
- Alfadel et al., MSR 2021: 65.42% of Dependabot security PRs in 2,904 JavaScript projects were
  accepted, "often merged within a day" (VERIFIED-SNIPPET). Rebatchi et al., EMSE 2024: security PR
  fixes are typically applied "in less than one day" (VERIFIED-SNIPPET). Most merges are fast; the
  study is about the tail.

**Unmeasured shares (assumptions, no source; ranges deliberately wide):**

| factor | low | central | high |
|---|---|---|---|
| security share of Dependabot PRs | 5% | 10% | 20% |
| single-dependency, non-grouped | 70% | 85% | 95% |
| org-owned (vs user-owned) | 35% | 50% | 60% |
| Tier A among org-owned fix PRs | 3% | 10% | 20% |
| deployed-service among Tier A repos' fix PRs | 15% | 30% | 50% |

**Resulting Tier A × deployed security fix PRs per week** (Dependabot + Renovate):
- low ≈ 317,204×0.05×0.70×0.35×0.03×0.15 + 1,300×0.5×0.35×0.03×0.15 ≈ **18**
- central ≈ 317,204×0.10×0.85×0.50×0.10×0.30 + 1,300×0.65×0.50×0.10×0.30 ≈ **417**
- high ≈ 317,204×0.20×0.95×0.60×0.20×0.50 + 1,300×0.8×0.60×0.20×0.50 ≈ **3,678**

Over a 16-week prospective window: **~300 / ~6,700 / ~59,000** fix PRs (low / central / high).

**Downstream funnel (central, assumptions):** own CI green at head 70% → human-active and no
automerge 45% → **~2,100 eligible PRs**; of these:
- "proven safe" (score ≥90% or Mend High/Very High displayed within 7 days of open): 10–30% →
  **~200–650** PRs for the co-primary share (§04 P1). At n=400 and design effect 3, the 95% CI
  half-width at p=0.25 is ±0.073 — enough to separate "<15%" from "≥35%" if the truth is near either
  end.
- **flip-while-open with human activity after the flip** (H1 events): 2–10% of eligible → **~40–210
  events**. The pre-registered H1 needs 631 events (HR 1.25, 50/50, α=0.05, 80% power); at 100 events
  the minimum detectable HR is ~1.75. **H1 is very likely underpowered in Tier A** — see 04 §8 for the
  pre-registered handling and README decision D2.

**Retrospective window** (2025-01-01..2025-10-06, ~40 weeks): roughly 2.5× the 16-week counts for D1,
H5 and H6 (no badge values, so no P1/H1).

Step 3 of the implementation plan measures every row of these tables for <$20 of BigQuery and a
few thousand API calls, **without touching outcomes**, and the go/no-go gate G1 uses the measured
numbers.
