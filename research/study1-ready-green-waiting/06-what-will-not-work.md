# 06 — What will not work, or is at risk

An honest list, with workarounds. Items marked **[must check first]** go into Step 0 of
`05-implementation-plan.md`.

---

## A. Environment problems

### A1. What the design container could not reach (2026-09-27)

The design ran in a Claude Code **cloud** session whose egress proxy allows only some hosts. Probes
were `curl` HEAD/GET requests (status `000` = CONNECT refused by the proxy) and WebFetch
(`EGRESS_BLOCKED`). WebSearch worked, so several facts are VERIFIED-SNIPPET only.

**Blocked (could not reach):**

| area | domains |
|---|---|
| GH Archive | www.gharchive.org, data.gharchive.org |
| badge endpoints | **dependabot-badges.githubapp.com**, **developer.mend.io** |
| Mend / Renovate docs and terms | www.mend.io, docs.renovatebot.com, renovatebot.com |
| GitHub docs/blog | docs.github.com, github.blog, github.githubassets.com (raw.githubusercontent.com worked and was used for the docs *source*) |
| vulnerability data | api.osv.dev, osv.dev, www.osv.dev, api.deps.dev, docs.deps.dev, www.first.org, api.first.org, epss.empiricalsecurity.com, epss.cyentia.com, www.cisa.gov |
| company registries | www.wikidata.org, query.wikidata.org, dumps.wikimedia.org, api.gleif.org, www.gleif.org, leidata.gleif.org, goldencopy.gleif.org, opencorporates.com, api.opencorporates.com, www.sec.gov, efts.sec.gov, find-and-update.company-information.service.gov.uk, api.company-information.service.gov.uk, crunchbase.com, clearbit.com |
| literature | arxiv.org, export.arxiv.org, api.semanticscholar.org, api.crossref.org, api.openalex.org, dblp.org, doi.org, dl.acm.org, ieeexplore.ieee.org, link.springer.com, www.researchgate.net, zenodo.org, sailresearch.github.io, hehao98.github.io, orbilu.uni.lu |
| pre-registration | osf.io, api.osf.io |
| legal texts | gdpr-info.eu, gdpr.eu, eur-lex.europa.eu, www.ecfr.gov, www.hhs.gov, www.law.cornell.edu, opensource.org, creativecommons.org |
| other research infra | ecosyste.ms, packages.ecosyste.ms, repos.ecosyste.ms, libraries.io, www.softwareheritage.org, www.ghtorrent.org, huggingface.co, api.securityscorecards.dev, scorecard.dev, www.bestpractices.dev, pnpm.io, dev.to, console.cloud.google.com |

**Reachable:** raw.githubusercontent.com, github.com (git clone; WebFetch of pages),
storage.googleapis.com (OSV bucket), cloud.google.com (pricing pages), bigquery.googleapis.com
(host only; no credentials in the container), registry.npmjs.org, pypi.org, yarnpkg.com,
camo.githubusercontent.com and objects.githubusercontent.com (host only).

**api.github.com** was reachable but **session-scoped**: every non-repository endpoint
(e.g. `/orgs/{org}`, `/zen`) returned 403 "sessions are bound to their configured repositories".
The GitHub MCP tools could still run a couple of global searches (used for the 1,300 Renovate count).

**Does it matter on the founder's machine?** No, none of these are blocked on an ordinary internet
connection; the api.github.com scoping is a Claude-cloud feature. If the future agents run Claude
Code with its own sandbox/network allowlist on the founder's machine, add the hosts above (at least:
`*.googleapis.com`, `api.github.com`, `github.com`, `raw.githubusercontent.com`,
`dependabot-badges.githubapp.com`, `developer.mend.io`, `query.wikidata.org`, `*.gleif.org`,
`storage.googleapis.com`, `registry.npmjs.org`, `pypi.org`, `epss.empiricalsecurity.com`, `osf.io`).

### A2. Claude Code cloud sessions are the wrong place to run this
- They are **ephemeral** (the container is discarded; only what is pushed to `main` of the
  `transcripts` repo survives — see CLAUDE.md) and **proxied** (badge hosts, GH Archive site,
  Wikidata, GLEIF blocked).
- The badge logger must run **16+ weeks continuously**; a cloud session cannot. Study data (which
  includes repos with unmerged security fixes) must **never** be committed to the transcripts repo.
- **Workaround:** run everything on the founder's always-on machine or a small VM; keep only design
  documents in this repo.

### A3. Founder's machine risks
Laptop sleep, reboots, ISP outages → logger gaps. Use a VM or an always-on box, a process supervisor
(systemd), a heartbeat, and record gaps (gaps >24 h drop PR-days from P2, 04 §Q9).

## B. Data limitations

1. **GH Archive payloads were trimmed on 2025-10-07.** PullRequestEvent `pull_request` now has only
   `id, url, number, head, base` (no title, body, user, `merged`); PushEvent has no `commits` (no
   author emails); `author_association` removed; there is no `synchronize` action on github.com, so
   rebases/force-pushes/body edits are invisible. (VERIFIED from github/docs source + VERIFIED-SNIPPET
   of the changelog and community discussion #177735.)
   *Workaround:* pre-trim window for retrospective work; GraphQL hydration only for the company
   sample; Tier B email domains from pre-trim PushEvents or GraphQL commit history.
   **[must check first]** whether `head.ref`/`head.sha` survive and whether `merged` actions still appear.
2. **GH Archive BigQuery freshness in 2026 and table sizes are unverified.** An old GitHub discussion
   said a *different* dataset (`bigquery-public-data.github_repos`) stopped updating.
   **[must check first]**. *Fallback:* hourly `data.gharchive.org` JSON files (not tested) or a
   GraphQL watch-list of company repos for the prospective window.
3. **Badge endpoints have no structured API.** Values are parsed from SVG `<title>`; format changes
   silently break parsing. *Workaround:* store raw SVG hash + headers; alert on parse failures.
4. **Badge display is not universal.** In the tournament's 5-PR sample, 4 bodies (one large org)
   were stripped to ~250 characters with no badge; yet 317,204 PRs in one week contained the badge
   text. Display must be measured per PR (it is also the placebo source). G2 requires ≥50% display.
5. **What maintainers saw is uncertain.** Camo caching TTL is unknown **[must check first]**; nobody
   observes whether a maintainer opened the PR. The human-activity restriction is a proxy only.
6. **Scores are usually absent and usually high.** Rombaut et al.: 83% of Dependabot updates have
   no computable score; existing ones are mostly >90% → few flips, fewer low scores; H2's sign test
   is not reachable in the company sample (needs ~1,751 events).
7. **Keying unknown.** If the Dependabot score depends only on `new-version`, all PRs for a fix flip
   together and fix fixed effects absorb the treatment (G2 iv).
8. **Flip timing.** Security PRs for an advisory open en masse; popular pairs may get a score within
   hours — before most maintainers look (G2 ii: <70% of flips within 24 h).
9. **Age gates crowd the 72-hour Mend cutoff.** pnpm ≥ v11 defaults `minimumReleaseAge` to 1,440
   minutes (24 h) (VERIFIED by the tournament from pnpm docs source); the tournament counted 32,064
   `pnpm-workspace.yaml` files with `minimumReleaseAge` and 2,204 `.yarnrc.yml` with
   `npmMinimalAgeGate` (raw code-search counts); Mend Merge Confidence Workflows and org presets are
   invisible in repo files. A pnpm age gate can also make CI **red** on a fresh security version,
   confounding "green at head". Dependabot's default 3-day **cooldown applies to version updates,
   not security updates** (VERIFIED, github/docs); Renovate's `vulnerabilityAlerts` sets
   `minimumReleaseAge: null` (VERIFIED). *Workaround:* H8 is secondary with placebo cutoffs; record
   CI state as a time series, not once.
10. **Historical badge values are not observable** → P1 and P2 are prospective only; retrospective
    work uses semver/CVSS/EPSS.
11. **Company definition is imperfect by construction.** Verified domains are opt-in; Wikidata covers
    mainly notable companies (biased to large firms); GLEIF has LEIs mostly for entities in
    financial transactions and matches by name only; commit emails are often noreply. Expect low
    recall and a sample skewed to larger, more mature companies — which are also the ones most likely
    to have change control. Report recall and describe the skew.
12. **Public company repos are rarely production services.** The deployed-service filter will cut
    most Tier A repos; "build in public" companies are unusual and may differ from typical buyers.
13. **Security classification of Dependabot PRs** relies on joining versions to advisories (no public
    "security update" marker was found); version-range parsing differs per ecosystem.
14. **Revert detection is a lower bound**: fix-forward, squash rewrites, and private follow-ups are
    missed; low escaped-breakage rates can read as "fear is irrational" — pre-registered both ways.
15. **Merge sessions** are inferred from public events; private review activity and CI-driven merges
    by humans via bots are misclassified.
16. **Comparison group (individuals)** rarely passes the deployed-service rule, so H7 compares
    different kinds of repos unless fix FE and service status are both controlled.

## C. Rate limits and terms

- GitHub REST 5,000 req/h and GraphQL 5,000 points/h per token; secondary limits (100 concurrent,
  900 REST points/min per endpoint, 2,000 GraphQL points/min, CPU-time budget, undisclosed limits).
  Sharing tokens to exceed limits is prohibited (ToS §H). *Workaround:* one token, ≤1 req/s,
  batching, caching; accept a multi-day wall clock.
- **GitHub Search** hits secondary limits almost immediately (2 queries in the tournament) and caps at
  1,000 results — not used.
- **Wikidata WDQS:** 60 s timeout, 60 s processing/min per UA+IP, 5 parallel queries; bad UAs blocked.
- **GLEIF API** 60 req/min → use the bulk file.
- **OpenCorporates** free keys ~50 req/day; the paid plan is out of budget → validation-sample use only.
- **Dependabot badge endpoint:** no published terms found; the study needs GitHub's written OK
  before scale (founder requirement). **Mend:** terms unread (blocked) → arm off without written OK.
- **GitHub AUP §7:** research use only of "public, non-personal information" and only with open-access
  publication; usernames/emails are personal data → minimise (07).

## D. Could not verify here — check first on an open network

| # | item | where it matters |
|---|---|---|
| 1 | GH Archive BigQuery 2026 freshness; bytes per day pre/post trim | cost, feasibility |
| 2 | post-trim `head.ref`/`sha` presence; `merged` action still emitted | D3 pre-filter; merge sessions |
| 3 | `is_verified` returned for all orgs to a non-member token | Tier A |
| 4 | Wikidata Q-ids/P-ids from memory; # companies with P2037 | Tier A size |
| 5 | GLEIF licence (CC0?) and absence of website field | A3 |
| 6 | Badge response format, "unknown" rate, sample threshold, (from,to) keying, cache headers | P1, P2 |
| 7 | Camo cache TTL | exposure timing |
| 8 | Mend ToS/AUP text on automated badge reads | Mend arm |
| 9 | EPSS terms; GitHub Advisory DB licence | H5, redistribution |
| 10 | deps.dev project→package table name and scan cost | library filter |
| 11 | GraphQL `deployments`/`environments` visible on public repos to non-members | S4 service rule |
| 12 | commit `author.email` exposure via GraphQL for public repos | Tier B |
| 13 | Full texts of He et al. 2023, Rombaut et al. 2024 (venue?), Alfadel 2021, Rebatchi 2024, Mohayeji 2025, Tanaka 2026 — especially whether anyone already estimated the causal effect of a displayed score | novelty of P2 |
| 14 | VM and spot-instance prices | budget |
| 15 | IRB fee for an independent determination | budget / D5 |

## E. Risks to the thesis (the study may say "no")

1. **Prior predicts a null.** He et al. (TSE 2023): scores "too scarce to be effective in reducing
   update suspicion" (search snippets also report a weak Spearman ρ=0.37 between compatibility score
   and merge rate — attribution to confirm). Rombaut et al.: 83% no score. Alfadel et al. (MSR 2021)
   and Rebatchi et al. (EMSE 2024): most security PRs merge within a day. A "proof matters" effect may
   be small because most green fixes already move fast.
2. **P1 ≥ 35% is plausible.** If many proven-safe fixes still wait in company services, belief 2 is
   falsified *in this domain* — and the pre-registration says so. The founder must be prepared to
   publish that (README D6).
3. **Off-wedge.** Application dependencies in public company repos ≠ enterprise OS/network change
   boards. A falsification here does not settle wedge B; a support here does not prove it either.
   Bridge: Dependabot docker base-image bumps (if scored) and the OS-IaC census (Step 8); later the
   C3 RCT phase (README "Later phase").
4. **Selection:** companies that build in public and verify domains are likely more mature; their
   fear may be lower (or their change control heavier) than typical buyers'.
5. **Salience vs information:** a positive P2 could be salience; H2 is underpowered to separate them
   in Tier A; H3 (hollow-green) is the main discriminator.
6. **Herding:** scores arrive as peers adopt; the invisible-flip placebo tests it but may itself be
   small-N in Tier A.
7. **Low escaped-breakage rate** reads as "fear is irrational" — reported with the pre-registered
   interpretation both ways.

## F. What the under-$1,000 budget rules out

- Paid company databases (Crunchbase, PitchBook, Clearbit/HubSpot, ZoomInfo, Dun & Bradstreet) and
  the paid OpenCorporates API → company matching relies on free registries (lower recall).
- Repeated full-history GH Archive payload scans (each full pre-trim year could cost tens to ~$100 or
  more; scan once and materialize).
- Higher GitHub rate limits (GitHub Enterprise Cloud org apps get 15,000/h) → multi-day crawls.
- A large provability lab (2,000+ PRs with mutation testing) → capped at ~200–500 PRs.
- Commercial IRB review if fees exceed the remaining budget → prefer an academic partner's IRB.
- Paid human annotators → the founder labels (~20 h).
- Internet-scale scanning (Censys/Shodan) and the RMM randomized trial (C3 phase B, $80–200k) —
  out of scope.
- Large-scale LLM labelling via API is not budgeted (use only for pre-labels on ≤300 owners, if at
  all, and only if the founder counts it outside the $1k).
- Historical score logs from GitHub/Mend cannot be bought; only requested for free.
