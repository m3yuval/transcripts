# 05 — Implementation plan (for future agents)

Step-by-step tasks for the agents that will build and run Study 1 on the **founder's own computer or
a VM with open internet**. Each step lists inputs, outputs, schemas, commands/query sketches, time,
cost, a checkpoint, and what to report back to the founder. Read `README.md` first, then 02–04, 06,
07. Do not start a step until its prerequisites' checkpoints have passed.

**Hard rules for every step** (from 07):
1. No writes to anyone's GitHub repo: no comments, PRs, issues, reactions, stars, forks, follows.
2. One GitHub token, one process at a time, ≤1 request/second to any single host; identified
   User-Agent `Skylayer-Study1/<ver> (+<OSF url>; <contact email>)`; stop on 403/429 and back off.
3. No badge polling at scale before G0 (written OK). Mend arm off without Mend's written OK.
4. Usernames hashed at ingestion (HMAC-SHA256 with a secret salt kept outside the data directory);
   email local parts never written to disk.
5. Never publish, commit to a public place, or paste into chat any list of repos/orgs with unmerged
   security fixes. Study data never goes into the `transcripts` repo.
6. Every BigQuery query: dry-run first, log bytes to `costs.csv`, run with `--maximum_bytes_billed`.
7. Company-sample merge outcomes stay masked (not computed, not looked at) until the OSF
   registration is filed (Step 5).

---

## Directory layout

Code lives in a new **private** git repo (e.g. `skylayer-study1`), data outside git:

```
~/skylayer-study1/                 # private code repo
  README.md                        # link back to this design folder
  config/
    study.yaml                     # windows, thresholds, UA string, paths (no secrets)
    regex/                         # frozen deploy/automerge/security regexes (hashed in prereg)
    lists/                         # freemail, academic, gov, foundation domain lists
  sql/                             # BigQuery SQL, one file per query, with dry-run bytes in a header
  src/study1/
    gha.py  classify_owner.py  deployed.py  hydrate.py  secclass.py
    badge_logger.py  census.py  breakage.py  lab/  analysis/
  tests/                           # unit tests incl. synthetic data for frozen analysis code
  notebooks/                       # exploratory only; never on masked outcomes
~/study1-data/                     # NOT in git; encrypted disk; backed up
  raw/ (bq exports, badge SVG headers, graphql json)  derived/ (parquet)  labels/  logs/
  secrets/ -> separate location: GITHUB_TOKEN, HASH_SALT, GCP creds
~/study1-data/costs.csv            # every billed query and VM-month
```

Formats: Parquet (zstd) + DuckDB for analysis; JSONL for raw API responses (gzip); CSV only for
small label files. Timestamps UTC ISO-8601. IDs: GitHub numeric `repo_id`, `owner_id`; PR key
`(repo_id, pr_number)`.

## Core schemas

```
owners.parquet        owner_id, owner_type{Organization|User}, is_verified, d_web, d_mail,
                      wd_qid, wd_match{A1|A2|none}, gleif_lei, a3_match, tierB_domain,
                      tierB_share, tierB_n_authors, tier{A|B|C|U}, classified_at, rule_version
                      (org login kept in clear only in a restricted file owners_private.parquet)
repos.parquet         repo_id, owner_id, is_fork, is_archived, is_template, default_branch,
                      s1_container, s2_cd, s3_iac, s4_deploy_env, s5_publishes_pkg,
                      deployed_service, service_rule_version, automerge_evidence_at{date},
                      renovate_cfg_hash, dependabot_cfg_hash
prs.parquet           repo_id, pr_number, bot{dependabot|renovate}, opened_at, head_ref,
                      ecosystem, package, from_version, to_version, semver_jump, grouped,
                      sec_class{security|incidental_fix|not_security}, ghsa, cvss, epss, kev,
                      draft, ci_state_at_open, ci_state_series, automerge_at_open,
                      body_has_badge_at{json}, human_active_30d,
                      -- MASKED until registration: merged_at, merged_by_type, closed_at,
                         superseded_by, fixed_at, fixed_by
badge_obs.parquet     repo_id, pr_number, badge_host, badge_kind, url_hash, observed_at,
                      http_status, value_raw, value_num, value_level, etag, cache_control, age_hdr,
                      via{origin|camo}
sessions.parquet      repo_id, day, n_human_merges, n_human_reviews, n_human_comments
policies.parquet      repo_id, file_path, content_hash, is_template_copy, gates[{field, op, value,
                      class{breakage|severity|relevance|other}}], excludes_security{bool}
breakage.parquet      repo_id, pr_number, merge_sha, revert_30, revert_90, downgrade_30/90,
                      pin_30/90, fixbuild_30/90, audited{bool}, audit_label
lab.parquet           repo_id, pr_number, changed_fns, covered_changed_fns, mutants, killed,
                      hollow_green{bool}, overall_cov, prod_import{bool}, run_status
```

---

## Step 0 — Environment and verification (day 1–2)

**Do:** set up Python 3.11+, `google-cloud-bigquery`, `bq` CLI, DuckDB, `gh`/`httpx`, `tldextract`.
Create GCP project `skylayer-study1` with billing; **set a project-level custom quota on "Query
usage per day" (e.g. 2 TiB/day)** and a billing budget alert at $100/$250/$500. Create a
fine-grained GitHub token with **public read-only** access (no repo write scopes).

**Verify on the open network (record each result in `verification.md`):**
1. GH Archive BigQuery 2026 freshness (sample query in 02 §S1) and dry-run bytes for one post-trim
   day and one pre-trim day (header columns vs payload).
2. Post-trim PullRequestEvent payload keys: print `JSON_KEYS(payload)` and
   `JSON_QUERY(payload,'$.pull_request')` for 5 bot PR events from yesterday (tiny query on one day
   table after dry run). Is `head.ref` there? Is `action='merged'` emitted?
3. `GET /orgs/{org}` for ~20 known orgs (mix of companies/communities): is `is_verified` present for a
   non-member token? Also GraphQL `isVerified`, `domains` (expect permission error).
4. Wikidata: property labels for P2037/P856/P31/P279/P1278/P1320 and the Q-ids in 03 §3.2; count of
   items with P2037 (one SPARQL `COUNT`).
5. GLEIF golden-copy download URL, size, licence; does the record have any website field?
6. Badge endpoints: **one** request each to dependabot-badges and (only if Mend terms allow reading
   in a browser-like way) none to Mend yet. Record status, content type, `cache-control`, the SVG
   `<title>`. No more until G0.
7. Read and save texts: Mend Terms of Service + AUP; EPSS terms; GH Archive licence; GitHub Advisory
   Database licence; OSF template.
8. Re-verify prior-art claims (01 §3) from full texts: He et al. 2023, Rombaut et al. 2024, Alfadel
   et al. 2021, Rebatchi et al. 2024, Mohayeji et al. 2025, Tanaka et al. 2026. **If any paper already
   estimated the causal effect of a displayed score on merging, stop and tell the founder** (P2 becomes
   a replication; headline shifts to P1, D1, H4, hollow-green).

**Output:** `verification.md`, `costs.csv`. **Time:** 1–2 days. **Cost:** <$1.
**Checkpoint / report back:** a table of every UNVERIFIED item in 02/03/06 with the new status, and
any item that changes the design.

## Step 1 — Legal pack (day 1; replies take 1–3 weeks — start immediately, in parallel)

Send the letters drafted in 07 §3: GitHub (badge polling + camo fetches, rate, UA, purpose, OA
publication), Mend (terms/permission for Merge Confidence badge reads), IRB determination request
(academic partner or independent IRB), draft privacy notice for the OSF page. **Output:**
`legal/` folder with sent letters and replies. **Report back:** who replied, what they allowed.
**G0 gate** lives here.

## Step 2 — Advisory table (day 2–3)

Inputs: S6 (git clone), S7 (all.zip per ecosystem: npm, PyPI, Maven, Go, NuGet, RubyGems, crates.io,
Packagist), S8, S9. Output `advisories.parquet`: (ecosystem, package, introduced, fixed, ghsa, cve,
cvss_score, published_at, kev, epss_by_date). Map bot ecosystems (`npm_and_yarn`, `pip`, `maven`,
`gomod`, `nuget`, `bundler`, `cargo`, `composer`) to OSV ecosystems. Unit-test version-range logic per
ecosystem (semver, PEP 440, Maven). **Time:** 1 day. **Cost:** $0.

## Step 3 — Discovery, classification and supply measurement (week 1) — outcome-blind

1. **BigQuery materialization** (02 §S1): one payload scan per month for
   2025-01..(current month); keep the event types and fields listed there, org-owned plus a 5%
   `MOD(FARM_FINGERPRINT(CAST(repo_id AS STRING)),20)=0` sample of user-owned repos. For pre-trim
   months also keep `title`, `user.login→hash`, `merged`, `merged_by.type`, and PushEvent
   `commits[].author.email` **domain only** (`REGEXP_EXTRACT(email, r'@(.+)$')`) for Tier B.
   *Estimated* 5–15 TiB total → $25–$95 (dry-run first; see 02).
2. **Skeleton and pre-filter:** `bot_pr_skeleton`, `candidate_fix_prs` (03 §2 D2–D3).
3. **Owner classification** (03 §3): REST `/orgs/{org}` for each distinct org owning a candidate PR
   (expected tens of thousands of orgs → ≤ ~10–30 h at 1 req/s); Wikidata/GLEIF joins locally;
   Tier B email rule (GraphQL history for post-trim orgs; GH Archive domains for pre-trim).
4. **Deployed-service filter** (03 §4) for Tier A/B repos.
5. **Supply report:** counts per week by tier, bot, ecosystem; the full funnel of 03 §9 with measured
   values. **Do not compute merge/close outcomes for Tier A/B.**

**Time:** 4–6 days of wall-clock (mostly rate-limited API). **Cost:** $25–$100 BigQuery.
**Checkpoint G1** (04 §7). **Report back:** measured funnel vs the planning table; G1 decision;
recommended option F1/F2/F3 if Tier A is small.

## Step 4 — Classifier validation (week 1–2)

Draw the ~300-owner and 150-repo samples (03 §8), produce a labelling sheet (CSV + evidence URL
column), hide predictions, collect founder labels (and second rater). Compute precision/recall/kappa.
**Time:** ~20 h of human labelling. **Cost:** $0. **Checkpoint G3.** **Report back:** metrics table and
the confusion list (what kinds of non-companies leak in).

## Step 5 — Freeze and pre-register (end of week 2)

Freeze: code commit hash, regex/list hashes, thresholds, G1/G3 outcomes, fallback option. Write the
analysis code against **synthetic data** with the real schemas (tests in `tests/`), outcomes masked.
File the OSF registration (04 §10). **Output:** OSF link, frozen tag `prereg-v1`. **Report back:** OSF
link. From here on, amendments only via OSF.

## Step 6 — Badge logger (prospective, 16 weeks + follow-up) — only after G0

- **Host:** an always-on machine (small VM or home server); not a laptop that sleeps; **never a
  Claude Code cloud session** (ephemeral, proxied, badge hosts blocked — 06 §A).
- **Feed:** every hour, new bot PRs in Tier A/B deployed repos (+ comparison samples if chosen) —
  from the newest GH Archive day table (header query; if GH Archive lags >6 h, fall back to a
  GraphQL poll of the watch-list repos' open bot PRs, ≤1 req/s).
- **Parse** badge URLs from the PR body (Dependabot `compatibility_score?...`; Mend
  `/api/mc/badges/{kind}/...`). Record `body_has_badge` at each body edit.
- **Schedule per PR:** t0, +6 h, +1 d, +2 d, +3 d, +7 d, +14 d, +30 d, and daily while open; stop at
  close. Global token bucket ≤1 req/s across all badge hosts; cache by URL (identical (pkg,from,to)
  URLs across repos are fetched once per slot). Once a week, fetch the **camo** URL (from REST
  `body_html`) for a 1% sample to measure cache staleness — only if GitHub's OK covers it.
- **Pair-keying test** (G2 iv): ≤50 extra requests varying `previous-version` for fixed
  `new-version`.
- **Stop conditions:** any 403/429 from a badge host → pause that host 24 h and alert; a written
  request from GitHub or Mend to stop → stop permanently.
- **Health:** heartbeat file every 10 min; daily summary (counts only) e-mailed or written to
  `logs/daily.md`; gaps >24 h flagged in data.
- **Expected load** (central 03 §9): ~400 new PRs/week × ~10 observations ≈ 4,000 requests/week
  before URL de-duplication — far below 1 req/s.

**Time:** 2–3 days to build + 16 weeks running + 30 d (P1) / 90 d (H6) follow-up. **Cost:** VM
roughly $10–$30/month (UNVERIFIED — check the GCP pricing calculator; $0 on the founder's own
always-on machine). **Checkpoint G2** at week 2 (counts only). **Report back:** weekly one-line
health + counts; the G2 decision memo.

## Step 7 — Hydration and outcome collection (runs alongside Step 6)

GraphQL hydration (02 §S3) in batches of 25–50 PRs, daily for open PRs (CI state series, edits,
automerge, timeline) and once at close. Outcomes are written to a separate masked table
(`prs_outcomes_masked.parquet`, readable only by the analysis step after the pre-registered analysis
date — enforce with a file permission and a check in the analysis code). Supersession chains linked
nightly. **Cost:** $0 (API). **Load:** a few hundred to a few thousand points/hour.

## Step 8 — Policy census, H4 (weeks 2–4; independent of outcomes)

For all Tier A/B repos (not only those with PRs): read at `HEAD` via GraphQL `object(expression:)`:
`.github/dependabot.yml`, `.github/workflows/*` that mention `dependabot`/`fetch-metadata`/
`gh pr merge`, `renovate.json`, `renovate.json5`, `.github/renovate.json5`, `.renovaterc*`,
`package.json#renovate`, `pnpm-workspace.yaml` (`minimumReleaseAge`), `.yarnrc.yml`
(`npmMinimalAgeGate`), `bunfig.toml`, and OS-level IaC holds (`unattended-upgrades` blacklist,
`apt-mark hold`, `versionlock`, GKE/EKS/AKS maintenance exclusions). Resolve Renovate `extends` presets
where public. De-duplicate by content hash; drop files identical (after whitespace/comment
normalisation) to the GitHub docs or fetch-metadata README examples; classify each gate.
**Output:** `policies.parquet`; POST 1 draft (aggregate only). **Time:** 1 week. **Cost:** $0.

## Step 9 — Retrospective analyses (weeks 3–6; after registration)

Window 2025-01-01..2025-10-06 (+ follow-up to today). D1, H5-retro (conditional logit on merge-session
days; covariates: semver, dependency type, CVSS, EPSS on the open date, KEV, PR age), H6-retro
(Step 10 labels). Run the frozen code; any deviation is logged as a deviation, not silently fixed.
**Report back:** Tables 1, 2, 5, 7 (draft) with CIs.

## Step 10 — Escaped-breakage ground truth (weeks 3–8)

For merged green security PRs in the sample: `git clone --filter=blob:none --no-checkout`, then
`git log --since=<merge> --until=<merge+90d> -p -- <lockfiles/manifests/bot configs>` and commit
messages; apply the §3 rules in 04. Hand-audit 300 flagged + 100 unflagged cases for precision and
a recall estimate. Delete clones after extraction. **Cost:** bandwidth only.

## Step 11 — Provability lab (weeks 4–8)

Pilot 200 merged PRs (npm + PyPI), then up to 500 total within budget (04 §6). Containers with
network disabled after install; tests unmodified; timeouts 20 min per version; no credentials; never
run on a machine holding the study secrets. **Cost:** $0 on the founder's machine; ≤$150 if run on
spot VMs (UNVERIFIED pricing). **Report back:** hollow-green share with CI by ecosystem; run-failure
rate.

## Step 12 — Prospective analysis and publication (after 16 w + 30 d; H6 after +90 d)

Unmask outcomes only on the registered analysis date. Run P1, P2, H2, H3, H7, H8 and robustness (04
§4). Write the open-access paper (arXiv + OA venue) and two short posts; replication package with
salted-hash IDs; data release delayed 90 days; k ≥ 10 per cell. **Report back:** verdict per the
pre-registered rule, the filled headline, and what it means for thesis.md belief 2 (the founder
updates thesis.md and ledger.md by hand — agents must not edit them).

---

## Timeline (wall-clock)

| week | work |
|---|---|
| 0 | Steps 0, 1, 2 |
| 1 | Step 3 (G1) |
| 1–2 | Step 4 (G3), Step 5 registration; logger built |
| 2 | logger starts (after G0) |
| 4 | G2 pilot gate; Step 8 census → POST 1 |
| 3–8 | Steps 9, 10, 11 → POST 2 (D1, H5-retro, H6-retro, hollow-green) |
| 18 | logging ends |
| 22 | P1/P2 analysis (after 30-day follow-up) |
| 31 | H6 prospective (after 90-day follow-up); paper |

## Budget (hard cap $1,000; target ≤ $600)

| item | estimate | notes |
|---|---|---|
| BigQuery GH Archive scans (once per month of data) | $25–$100 | dry-run gated; first 1 TiB/month free |
| BigQuery deps.dev + ad-hoc + reruns | $10–$50 | |
| BigQuery storage of materialized tables | <$10 | tens of GiB |
| Always-on VM for logger (5–7 months) | $0–$210 | $0 on founder's machine; VM price UNVERIFIED |
| Lab compute | $0–$150 | founder's machine preferred |
| OpenCorporates / GLEIF / Wikidata / OSV / npm | $0 | free tiers only |
| Contingency | ~$200 | reruns, a bigger lab |
| **Total** | **~$250–$700** | IRB fees and people's time not included (README D5) |

## Reporting template (each step)

```
STEP <n> — <name> — <date>
Status: done | blocked | failed
Outputs: <paths>   Costs this step: $<x> (cumulative $<y>)
Key numbers: <counts only; no repo/org names>
Deviations from plan: <none | list>
Needs founder decision: <none | question>
```
