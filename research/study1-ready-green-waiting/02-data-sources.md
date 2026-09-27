# 02 — Data sources

Every source Study 1 uses, with what it contains, how to access it, what it costs, the terms, and
whether the facts were **verified** in the design session (2026-09-27), are **unverified**, or were
**blocked-from-here** (the design ran in a Claude Code cloud container whose egress proxy blocked
most domains; see `06-what-will-not-work.md` §A). The implementing agents run on the founder's own
machine or VM with open internet. **Step 0 of `05-implementation-plan.md` re-checks every
"unverified" or "blocked" item below before anything else.**

Status legend:
- **VERIFIED**: read from a primary source (raw GitHub docs source, official source code, the
  official pricing page) on 2026-09-27, or measured with a small read-only request.
- **VERIFIED-SNIPPET**: confirmed only from web-search snippets of the primary page, which was blocked.
- **UNVERIFIED**: from memory or secondary sources; must be checked.
- **BLOCKED**: the domain could not be reached from the design container.

Identity used for every request (put it in every tool): User-Agent
`Skylayer-Study1/<version> (+<OSF project URL>; <research contact email>)`. Never rotate tokens,
IPs or User-Agents to get around limits.

---

## Summary table

| # | Source | Used for | Access | Auth | Cost | Status |
|---|---|---|---|---|---|---|
| S1 | GH Archive on BigQuery (`githubarchive.day.*`) | discovering bot PRs, merges, human activity; repo/org IDs | BigQuery SQL | GCP project with billing | $6.25/TiB after 1 TiB/month free | schema VERIFIED; sizes and 2026 freshness UNVERIFIED; site BLOCKED |
| S2 | GitHub REST API | org profile (`is_verified`, `blog`, `email`), deployments, rate-limit checks | HTTPS | founder's GitHub token | free | VERIFIED (schema, limits) |
| S3 | GitHub GraphQL API | PR hydration (title, body, merge, CI, timeline, edits), config files, commit-author email domains | HTTPS | same token | free | VERIFIED (schema) |
| S4 | Dependabot compatibility badge | peer "safe to merge" score over time | HTTPS image (SVG) | none | free | URL format VERIFIED; endpoint BLOCKED; terms: needs GitHub's written OK |
| S5 | Mend Merge Confidence badges | Renovate peer confidence over time | HTTPS image (SVG) | none | free | URL format VERIFIED-SNIPPET; endpoint BLOCKED; terms UNVERIFIED — needs Mend's written OK |
| S6 | GitHub Advisory Database (git) | security classification (vulnerable ranges, patched versions, GHSA, CVSS) | `git clone` | none | free | VERIFIED reachable |
| S7 | OSV bulk export (GCS) | same, cross-ecosystem | HTTPS / `gsutil` | none | free | VERIFIED reachable |
| S8 | CISA KEV (GitHub mirror) | "known exploited" flag | raw GitHub | none | free | VERIFIED reachable |
| S9 | EPSS daily CSV | exploit-probability covariate for H5 | HTTPS | none | free | VERIFIED-SNIPPET; BLOCKED |
| S10 | Wikidata (WDQS / dumps) | Tier A company match: P2037 GitHub username, P856 website, P31 class | SPARQL / dump | none | free | properties VERIFIED-SNIPPET; BLOCKED |
| S11 | GLEIF LEI golden copy / API | Tier A corroboration by legal name | bulk file / REST | none | free | VERIFIED-SNIPPET; BLOCKED |
| S12 | OpenCorporates API | Tier A corroboration (validation sample only) | REST | API key | free keys limited; paid out of budget | VERIFIED-SNIPPET; BLOCKED |
| S13 | Public Suffix List | registrable-domain (eTLD+1) extraction | file | none | free | UNVERIFIED (standard) |
| S14 | npm registry / PyPI JSON | release timestamps; tarballs for the lab | HTTPS | none | free | VERIFIED reachable |
| S15 | deps.dev BigQuery (`bigquery-public-data.deps_dev_v1`) | library-vs-service filter (does the repo publish a package?) | BigQuery | GCP | per TiB | VERIFIED-SNIPPET; docs BLOCKED |
| S16 | git clones of candidate repos | revert/downgrade ground truth; lab | `git clone --filter` | none | bandwidth only | VERIFIED (git works) |
| S17 | OSF | pre-registration | web | account | free | BLOCKED |

---

## S1. GH Archive (BigQuery public dataset)

**What it is.** An hourly archive of GitHub's public Events API, loaded into BigQuery. The GH Archive
BigQuery README says "the dataset is automatically updated every hour". Licence: GH Archive site
content CC-BY-4.0; the README notes the dataset "includes material that may be subject to third
party rights" (attribute GH Archive in every publication). Source of these statements: the
`igrigorik/gharchive.org` repository (README.md and bigquery/README.md), VERIFIED via `git clone`.
www.gharchive.org itself was BLOCKED.

**Tables.** `githubarchive.day.YYYYMMDD` (one table per day), plus `githubarchive.month.YYYYMM` and
`githubarchive.year.YYYY` (UNVERIFIED that month/year tables are still maintained). Always query the
**day** tables with a wildcard and `_TABLE_SUFFIX` so that only the needed days are billed.

**Schema** (VERIFIED from `bigquery/schema.js` in the GH Archive repo):

| column | type | notes |
|---|---|---|
| `type` | STRING | event type, e.g. `PullRequestEvent` |
| `public` | BOOLEAN | always true |
| `payload` | STRING | the event payload as a JSON **string**; by far the largest column |
| `repo.id`, `repo.name`, `repo.url` | INTEGER/STRING | |
| `actor.id`, `actor.login`, `actor.gravatar_id`, `actor.avatar_url`, `actor.url` | | who did it (`dependabot[bot]`, `renovate[bot]`, humans) |
| `org.id`, `org.login`, ... | | **present only when the repo is owned by an Organization** — a free first filter |
| `created_at` | TIMESTAMP | |
| `id` | STRING | event id |
| `other` | STRING | leftovers |

**What the payload still contains (critical).** GitHub trimmed Events API payloads on
**2025-10-07** (announced 2025-08-08; brownout 2025-09-08). VERIFIED-SNIPPET from the GitHub
changelog ("Upcoming changes to GitHub Events API payloads", github.blog — BLOCKED) and GitHub
community discussion #177735 (read via WebFetch): *the `pull_request` object in PullRequestEvent
now includes only `id`, `url`, `number`, `head` and `base`*; `title` and `merged` are explicitly
missing. Which sub-fields of `head`/`base` survive (`ref`, `sha`, `repo`) is UNVERIFIED — check in
Step 0. VERIFIED from the github/docs source (`data/reusables/webhooks/*`):
- PullRequestEvent `action` on github.com is one of `opened, closed, merged, reopened, assigned,
  unassigned, labeled, unlabeled` — **there is no `synchronize`** (so pushes/rebases to a PR are
  invisible in GH Archive).
- PushEvent on github.com has only `repository_id, push_id, ref, head, before` — **no `commits`
  array, no `size`, no author emails** (those are GHES-only now).
- Payload has `number` (PR number) at top level.

Consequences:
- **Before 2025-10-07** (e.g. 2025-01-01..2025-10-06) GH Archive PR payloads are rich (title,
  body, user, merged flag, merged_by, labels) and PushEvents carry commit author emails. This
  window is the cheapest source for the retrospective analyses (D1, H5, H6) and for Tier B email
  domains.
- **From 2025-10-07** GH Archive gives the skeleton only (who opened/merged/closed which PR number in
  which repo, when, and probably the head branch name). Everything else is hydrated through
  GraphQL (S3) — and only for PRs in the company sample, which keeps API volume small.

**Discovery keys available in the skeleton.**
- Dependabot branch names follow `dependabot/<package_manager>/<directory>/<dependency>-<version>`
  (VERIFIED from dependabot-core `branch_namer/solo_strategy.rb` and `base.rb`; prefix default
  `dependabot`, configurable separator). The new version is in the branch name; the old version is
  not (it comes from the title after hydration).
- Renovate security PRs use `branchTopic: {{{datasource}}}-{{{depNameSanitized}}}-vulnerability`
  under the default `renovate/` prefix, `commitMessageSuffix: '[SECURITY]'`, `prCreation:
  'immediate'`, `minimumReleaseAge: null`, `prConcurrentLimit: 0`, `groupName: null` (VERIFIED from
  `renovatebot/renovate` `lib/config/options/index.ts`, option `vulnerabilityAlerts`). So a
  `...-vulnerability` head ref identifies a Renovate security PR without any API call (users can
  override the template; the title `[SECURITY]` check after hydration is the backstop).

**Cost.** VERIFIED from cloud.google.com/bigquery/pricing (2026-09-27): on-demand queries cost
**$6.25 per TiB** processed; **the first 1 TiB per month is free** (per billing account); charges
round up to the nearest MB with a **minimum of 10 MB per table referenced** and per query; queries
that error or hit the cache are free; cancelling a running query can still bill the full cost.
Cost controls exist: "User-level and project-level custom cost controls" and "The maximum bytes
billed by a query". Storage: active logical storage $0.000031507 per GiB-hour (~$0.023/GiB-month),
first 10 GiB free. BigQuery charges for **every byte of every column referenced**, regardless of
`WHERE` filters, and `payload` is the dominant column; wildcard day tables are billed only for the
days in `_TABLE_SUFFIX`.

**Size estimates (UNVERIFIED — replace with dry-run numbers in Step 0).** A 2020 example
(Chris Wilcox blog, via search snippet) reported ~223 GB processed for one month of
`PullRequestEvent` queries on `githubarchive.day` and >3 TB for 2.5 years. Event volume has grown
since, and payloads shrank sharply after 2025-10-07. Planning ranges used in this design:

| window | payload-scanning query | cost per month of data |
|---|---|---|
| pre-trim (≤2025-10-06) | 0.3–1.5 TiB per month | $2–$9 |
| post-trim (≥2025-10-07) | 0.1–0.5 TiB per month | $0.6–$3 |
| header columns only (`type, created_at, repo, org.login, actor.login`) | 0.01–0.05 TiB per month | ~$0–$0.3 |

Rule for agents: **every query is dry-run first** (`bq query --dry_run`), its bytes are logged to
`costs.csv`, and it is run with `--maximum_bytes_billed` set to 1.2× the dry-run figure. Each month
of GH Archive payload is scanned **once** and the needed fields are materialized into the study's own
dataset (partitioned by date, clustered by `repo_id`); all later work queries the small table.

**Sample query (Step 0 freshness + skeleton check; header columns only, cheap):**
```sql
-- Is 2026 data present and fresh? Billed: created_at + type only.
SELECT _TABLE_SUFFIX AS day, COUNT(*) AS n, MAX(created_at) AS last_event
FROM `githubarchive.day.202609*`
WHERE _TABLE_SUFFIX BETWEEN '01' AND '30'
GROUP BY day ORDER BY day;
```

**Sample materialization (one month, run once; dry-run first):**
```sql
CREATE TABLE IF NOT EXISTS s1.gha_events_2026_08
PARTITION BY DATE(created_at) CLUSTER BY repo_id AS
SELECT
  created_at, type, repo.id AS repo_id, repo.name AS repo_name,
  org.login AS org_login, actor.login AS actor_login,
  JSON_VALUE(payload, '$.action')                        AS action,
  SAFE_CAST(JSON_VALUE(payload, '$.number') AS INT64)    AS pr_number,
  JSON_VALUE(payload, '$.pull_request.head.ref')         AS head_ref,   -- check it survives the trim
  JSON_VALUE(payload, '$.pull_request.head.sha')         AS head_sha,
  JSON_VALUE(payload, '$.review.state')                  AS review_state
FROM `githubarchive.day.202608*`
WHERE type IN ('PullRequestEvent','PullRequestReviewEvent',
               'PullRequestReviewCommentEvent','IssueCommentEvent')
  AND org.login IS NOT NULL;  -- org-owned only (keep a 5% hash sample of user-owned repos for the comparison group, see 03)
```
Actor logins are personal data: they are replaced by `is_bot` / `actor_hash` at the next step and
the raw column is dropped (see `07-legal-ethics.md`).

---

## S2. GitHub REST API

- **Endpoints used:** `GET /orgs/{org}` (profile: `is_verified`, `blog`, `email`, `name`, `company`,
  `description`, `location`, `created_at`, `public_repos`, `type`); `GET /users/{user}` (to confirm
  `type` = User for the comparison group); `GET /repos/{o}/{r}/deployments` and
  `/environments` (deployed-service signal); `GET /rate_limit`.
- **`is_verified`** is in the `organization-full` schema of GitHub's official OpenAPI description
  (`github/rest-api-description`, `api.github.com.json`), type boolean, **not in the required list**
  (VERIFIED). GitHub's docs example for `GET /orgs/{org}` shows `"is_verified": true` (VERIFIED-SNIPPET).
  Whether the field is returned to a non-member token for every org is UNVERIFIED → Step 0.
- **What "verified" means** (VERIFIED from github/docs source,
  `content/organizations/managing-organization-settings/verifying-or-approving-a-domain-for-your-organization.md`
  and reusable `verified-domains-details.md`): owners prove control of a domain with a DNS TXT
  record; "After verifying ownership of your organization's domains, a 'Verified' badge will display
  on the organization's profile"; "To display a 'Verified' badge, the website and email information
  shown on an organization's profile must match the verified domain or domains." The page is
  versioned `fpt: '*'`, i.e. available on free github.com plans too. Therefore **`is_verified =
  true` implies the profile `blog` (website) and `email` domains are verified**, which is how Study 1
  obtains the verified domain without admin access.
- **Rate limits** (VERIFIED, github/docs source): authenticated personal token **5,000
  requests/hour**; secondary limits: ≤100 concurrent requests (REST+GraphQL shared), ≤900 points per
  minute per REST endpoint (GET = 1 point), ≤90 s CPU time per 60 s real time, and "you may also
  encounter a secondary rate limit for undisclosed reasons". On 403/429: honour `retry-after`; if
  `x-ratelimit-remaining` is 0 wait until `x-ratelimit-reset`; otherwise wait ≥1 minute, then back
  off exponentially. Study rule: **one token, one process, ≤1 request/second** (3,600/h, below the
  5,000/h cap).
- **Terms:** GitHub Terms of Service §H "API Terms" (VERIFIED text): "Abuse or excessively frequent
  requests to GitHub via the API may result in the temporary or permanent suspension of your
  Account's access"; "You may not share API tokens to exceed GitHub's rate limitations." See 07.
- **Search API is NOT used** for discovery: the tournament's pilot hit a secondary rate limit after
  2 queries; the Search API also caps results at 1,000 per query.

Sample request:
```bash
curl -sS -H "Authorization: Bearer $GITHUB_TOKEN" -H "X-GitHub-Api-Version: 2022-11-28" \
     -A "$STUDY_UA" https://api.github.com/orgs/$ORG \
 | jq '{login, type, is_verified, blog, email, name, company, created_at, public_repos}'
```

## S3. GitHub GraphQL API

- **Fields VERIFIED present** in the public schema (`github/docs` `src/graphql/data/fpt/schema.docs.graphql`):
  - `Organization`: `isVerified` ("Whether the organization has verified its profile email and
    website"), `websiteUrl`, `email`, `description`, `location`, `createdAt`, `domains(isVerified:)`
    ("A list of domains owned by the organization" — **probably admin-only; UNVERIFIED**, do not
    rely on it).
  - `Repository`: `isFork`, `isTemplate`, `isArchived`, `pushedAt`, `homepageUrl`,
    `repositoryTopics`, `primaryLanguage`, `languages`, `deployments`, `environments`,
    `object(expression:)` (read any file/tree at `HEAD:`), `autoMergeAllowed`, `defaultBranchRef`,
    `stargazerCount`. (`vulnerabilityAlerts` exists but needs admin rights — not usable.)
  - `PullRequest`: `title`, `body`, `author`, `authorAssociation`, `createdAt`, `mergedAt`,
    `mergedBy`, `closedAt`, `headRefName`, `baseRefName`, `isDraft`, `labels`, `lastEditedAt`,
    `userContentEdits` (body edit history — needed to know when a badge was removed from a body),
    `autoMergeRequest`, `commits(last:1){ nodes{ commit{ statusCheckRollup{ state } } } }` (CI at
    head), `reviewDecision`, `timelineItems(itemTypes: [...])`.
  - Timeline item types used: `HEAD_REF_FORCE_PUSHED_EVENT`, `MERGED_EVENT`, `AUTO_MERGE_ENABLED_EVENT`,
    `READY_FOR_REVIEW_EVENT`, `REVIEW_REQUESTED_EVENT`, `PULL_REQUEST_COMMIT`, `HEAD_REF_DELETED_EVENT`,
    plus closed/reopened/labeled.
- **Rate limits** (VERIFIED): 5,000 points/hour for a personal token; ≤2,000 points/minute on the
  GraphQL endpoint (secondary); ≤60 s of the 90 s CPU budget per minute may be GraphQL; a single
  call may not request more than 500,000 nodes. Batch 25–50 PRs per query with aliases.

Sample hydration query:
```graphql
query($owner:String!, $name:String!, $n:Int!) {
  repository(owner:$owner, name:$name) {
    pullRequest(number:$n) {
      title body createdAt mergedAt closedAt state headRefName isDraft lastEditedAt
      author { __typename login }
      mergedBy { __typename login }
      autoMergeRequest { enabledAt mergeMethod }
      labels(first:10) { nodes { name } }
      userContentEdits(first:20) { nodes { editedAt } }
      commits(last:1) { nodes { commit { oid statusCheckRollup { state } } } }
      timelineItems(first:100, itemTypes:[HEAD_REF_FORCE_PUSHED_EVENT, MERGED_EVENT,
                    AUTO_MERGE_ENABLED_EVENT, CLOSED_EVENT, REOPENED_EVENT]) {
        nodes { __typename ... on HeadRefForcePushedEvent { createdAt }
                           ... on MergedEvent { createdAt } ... on ClosedEvent { createdAt } }
      }
    }
  }
}
```
Logins returned are hashed at ingestion (`author_hash`, `merger_hash`) and only `__typename`
(`Bot` vs `User`) is kept in clear.

## S4. Dependabot compatibility-score badge

- **Definition** (VERIFIED, github/docs `dependabot-security-updates.md`): security updates "may
  include compatibility scores ... calculated from CI tests in other public repositories where the
  same security update has been generated. An update's compatibility score is the percentage of CI
  runs that passed when updating between specific versions of the dependency." Security PRs update
  "to the minimum version that includes the patch". Grouped security updates exist (drop them).
- **Endpoint** (VERIFIED from `dependabot/fetch-metadata` `src/dependabot/verified_commits.ts`, the
  official Action):
  `https://dependabot-badges.githubapp.com/badges/compatibility_score?dependency-name=<name>&package-manager=<ecosystem>&previous-version=<old>&new-version=<new>`;
  the Action regex-parses `<title>compatibility: (\d+)%</title>` from the SVG. A practitioner script
  seen by the tournament also handles an `aria-label="compatibility: unknown"` state. There is **no
  structured API** — it is an image.
- **Display to maintainers:** the badge URL sits in the PR body; GitHub serves body images through
  its camo image proxy (`camo.githubusercontent.com`), so what a maintainer sees is the image as of
  view time (modulo camo caching — UNVERIFIED TTL). The PR body itself does not change when the score
  changes. (Mend's equivalent is documented to work this way — "Renovate embeds badge URLs blindly
  ... when a user loads the PR, their browser loads the badge URL" — renovatebot discussion #27225,
  VERIFIED-SNIPPET.)
- **Access status: BLOCKED from the design container** (403 CONNECT). Response format, the
  "unknown" rate, the minimum sample before a number appears, whether the score is keyed on the
  (from, to) pair or only on `new-version`, and cache headers are all **UNVERIFIED** → Step 0 and
  the week-2 gate, with ≤50 requests for the keying test.
- **Prior evidence on availability** (VERIFIED-SNIPPET, Rombaut, Cogo & Hassan, arXiv:2403.09012):
  across 579,206 Dependabot PRs and 618,045 score records, "a compatibility score cannot be
  calculated for 83% of the dependency updates"; when a score exists, "the vast majority of the
  scores are above 90%". Expect flips and low scores to be rare (see 06 §E).
- **Terms:** no published terms for this endpoint found. **Get GitHub's written OK before polling at
  scale** (07). Rate: ≤1 request/second total across all badge hosts.

Sample request (one PR, one time):
```bash
curl -sS -A "$STUDY_UA" -D headers.txt \
  "https://dependabot-badges.githubapp.com/badges/compatibility_score?dependency-name=lodash&package-manager=npm_and_yarn&previous-version=4.17.20&new-version=4.17.21" \
  | grep -oE 'compatibility: ([0-9]+%|unknown)'
```

## S5. Mend Merge Confidence badges (Renovate)

- **Docs** (VERIFIED from `renovatebot/renovate` `docs/usage/merge-confidence.md`, read via raw
  GitHub): badges Age, Adoption, Passing, Confidence; levels Low / Neutral / High / Very High;
  "npm packages can only get the High Confidence badge when they are at least three days old";
  "The percentages for Adoption and Passing are weighted towards Organizations, private
  repositories, and projects with high test reliability"; the algorithm is private; Mend sells
  "Merge Confidence Workflows" ("only raise a PR once the update is in High confidence",
  "automerge Very High confidence updates") which may live in configuration the repo does not show;
  badges can be disabled with `ignorePresets: ["mergeConfidence:all-badges"]`; supported
  datasources: go, npm, maven, pypi, nuget, packagist, rubygems.
- **Endpoint format** (VERIFIED-SNIPPET, seen in live PR bodies by the tournament and in search
  results): `https://developer.mend.io/api/mc/badges/{age|adoption|passing|confidence}/{datasource}/{package}/{from}/{to}?slim=true`,
  e.g. `.../badges/confidence/maven/org.jetbrains.kotlin.kapt/1.9.0/1.9.20?slim=true`.
- **Access status: BLOCKED** (developer.mend.io, www.mend.io and docs.renovatebot.com all blocked).
  Mend's Terms of Service and Acceptable Use Policy (`https://www.mend.io/terms-of-service/`,
  `https://www.mend.io/acceptable-use-policy/`) could not be read. **The Mend arm stays OFF until
  Mend gives written permission** (07).
- Renovate security PRs have `minimumReleaseAge: null` by default (VERIFIED, S1) — so Renovate's own
  age gate does not delay security PRs, but repo-level package-manager gates can (pnpm below).

## S6. GitHub Advisory Database

`git clone --depth 1 https://github.com/github/advisory-database` (VERIFIED reachable). Use
`advisories/github-reviewed/**.json` (OSV format): `affected[].package.{ecosystem,name}`,
`affected[].ranges[].events[{introduced|fixed}]`, `database_specific.severity`, `severity[]` (CVSS
vector), `aliases` (CVE), `published`, `modified`. Licence: CC-BY-4.0 (UNVERIFIED — check the repo
LICENSE file). Free.

## S7. OSV bulk export

`https://storage.googleapis.com/osv-vulnerabilities/<Ecosystem>/all.zip` (VERIFIED reachable;
npm's was 216,651,333 bytes on 2026-09-26 per the tournament; `ecosystems.txt` lists ecosystems,
VERIFIED). `api.osv.dev` was BLOCKED — the bulk export makes it unnecessary. Free.

## S8. CISA KEV

`https://raw.githubusercontent.com/cisagov/kev-data/main/known_exploited_vulnerabilities.json`
(VERIFIED reachable; catalogVersion 2026.09.25 with 1,726 entries per the tournament). Few
application-library CVEs are in KEV; use as a flag only.

## S9. EPSS

Daily CSV `https://epss.empiricalsecurity.com/epss_scores-current.csv.gz` (older host
`epss.cyentia.com`), archive back to 2021-04-14 (VERIFIED-SNIPPET via first.org/epss/data; all EPSS
hosts BLOCKED). Licence/usage terms UNVERIFIED — read `https://www.first.org/epss/` terms in Step 0.
Use the score on the PR-open date.

## S10. Wikidata

- Properties (VERIFIED-SNIPPET from wikidata.org property pages, which were BLOCKED):
  **P2037 "GitHub username"** (allowed on instances of human, organization, project, software, ...;
  7,121 pages used it in Nov 2021 — a total count for all entity types, companies are a subset);
  **P1278 "Legal Entity Identifier"** (20-character ISO 17442 LEI); **P1320 "OpenCorporates company
  ID"** (format `<jurisdiction>/<number>`, e.g. `gb/02906991`).
- From memory, UNVERIFIED (check labels in Step 0): P31 instance of, P279 subclass of, P856 official
  website, P17 country; classes Q4830453 business, Q783794 company, Q6881511 enterprise, Q891723
  public company, Q163740 nonprofit organization, Q157031 foundation, Q3918 university, Q327333
  government agency.
- Access: WDQS `https://query.wikidata.org/sparql` — hard 60 s timeout per query; each client
  (User-Agent + IP) gets 60 s of processing per 60 s; ≤5 parallel queries per IP; clients violating
  the User-Agent policy may be blocked; over-limit → HTTP 429 (VERIFIED-SNIPPET, Wikidata query-limits
  page). Alternative: Wikidata JSON/truthy dumps on dumps.wikimedia.org (large; only needed if WDQS
  times out). Data licence CC0 (UNVERIFIED).

Sample query (all items with a GitHub username, their classes and websites — small result):
```sparql
SELECT ?item ?gh ?class ?site WHERE {
  ?item wdt:P2037 ?gh .
  OPTIONAL { ?item wdt:P31 ?class }
  OPTIONAL { ?item wdt:P856 ?site }
}
```
A second query returns the subclass closure of business (`?c wdt:P279* wd:Q4830453`) and of the
non-profit classes; classification is done locally (avoids timeouts from `P31/P279*` joins).

## S11. GLEIF

API `https://api.gleif.org/api/v1/lei-records?filter[entity.legalName]=...` and
`/api/v1/fuzzycompletions?field=entity.legalName&q=...`; **60 requests per minute** (VERIFIED-SNIPPET,
GLEIF API docs). Free daily **Golden Copy / Concatenated files** (XML/CSV in ZIP, published three
times a day) — use the bulk file, not the API. Licence: GLEIF says free of charge subject to its "LEI
Data Terms of Use"; CC0 is from memory (UNVERIFIED). LEI Level-1 records carry legal name, addresses,
legal form (ELF code), status — **not a website** (UNVERIFIED; so GLEIF can only corroborate by name,
never by domain). All GLEIF hosts BLOCKED.

## S12. OpenCorporates

API key required; free "share-alike" keys for open-data projects and public-benefit users
(researchers) on application; default ~50 requests/day and 200/month on free accounts; paid plans
remove the share-alike condition (VERIFIED-SNIPPET, OpenCorporates terms and API reference pages,
BLOCKED). Use **only** for the ~300-owner validation sample, or skip. The paid API is out of budget.

## S13. Public Suffix List

`https://publicsuffix.org/list/public_suffix_list.dat` via the Python `tldextract` or `publicsuffix2`
package, to reduce hostnames to registrable domains (`www.example.co.uk` → `example.co.uk`).
UNVERIFIED reachability (not tested); standard.

## S14. Package registries

`https://registry.npmjs.org/<pkg>` (`time` map = release timestamps; `versions[v].dist.tarball`) and
`https://pypi.org/pypi/<pkg>/json` (VERIFIED reachable). Maven Central, NuGet, RubyGems, crates.io,
Go proxy: not checked. Polite use (cache every document; ≤5 req/s).

## S15. deps.dev BigQuery

`bigquery-public-data.deps_dev_v1` with `PackageVersions(Latest)`, `Dependencies(Latest)`,
`Advisories` (VERIFIED-SNIPPET from docs.deps.dev, BLOCKED). A project-to-package mapping table
(believed to be `ProjectPackageVersions`) would tell whether a GitHub repo is the source of a
published package, i.e. a **library** rather than a deployed service — table name and cost
UNVERIFIED → dry-run in Step 0. The deps.dev API (`api.deps.dev`) was BLOCKED and, per the
tournament, returns only dependent **counts**.

## S16. Git clones

`git clone --filter=blob:none --no-checkout` then targeted `git log -p -- <lockfile>` for the
revert/downgrade scan (H6), and shallow full clones only for the ≤200–500 lab PRs. Public repos
only, never pushed anywhere, deleted after measurement.

## S17. OSF

osf.io was BLOCKED. Use the "Preregistration of secondary data analysis" template (van den Akker et
al.; OSF `https://osf.io/x4gzt/`, VERIFIED-SNIPPET) — it fits because GH Archive data already exists
before registration. File the registration, with the frozen company definition, **before** any
outcome (merge/close timing) of the company sample is computed.

## Sources considered and rejected

- **GitHub Search API** — secondary rate limits after 2 queries in the tournament pilot; 1,000-result
  cap. Only used, if at all, for ≤10 manual spot checks.
- **`bigquery-public-data.github_repos`** (file contents) — reported stale for years (search snippet,
  UNVERIFIED); read config files directly with GraphQL `object(expression:)` for the company sample.
- **Crunchbase, Clearbit, PitchBook, ZoomInfo** — paid; out of budget and licence-incompatible with
  open publication.
- **Censys/Shodan** — not needed; out of budget.
- **ecosyste.ms, libraries.io, Software Heritage, World of Code, Hugging Face GH Archive mirrors** —
  BLOCKED here, unverified; possible fallbacks only.
