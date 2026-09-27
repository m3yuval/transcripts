# 07 — Legal and ethics

Concrete checklist, the policy texts that were read, draft letters, and the rules the implementing
agents must follow. This is a research design, not legal advice: the founder should have counsel
(or the academic partner's research office) review §1–§4 before Step 6 starts.

Status legend as in 02: VERIFIED (primary text read), VERIFIED-SNIPPET (search snippet only),
BLOCKED/UNVERIFIED.

---

## 1. Checklist (all must be ✅ before the step named)

| # | item | owner | before |
|---|---|---|---|
| L1 | Read GitHub AUP §7 and ToS §H (texts below); commit in writing to open-access publication | founder | Step 3 |
| L2 | Written OK from GitHub for badge polling (dependabot-badges.githubapp.com) and occasional camo fetches, at ≤1 req/s with identified UA | founder | Step 6 (G0) |
| L3 | Mend ToS + AUP read; written permission for automated Merge Confidence badge reads — else Mend arm OFF | founder | Mend part of Step 6 |
| L4 | IRB exemption determination (or "not human-subjects research") in writing | founder / academic partner | Step 5 |
| L5 | GDPR: legitimate-interest assessment (LIA), Art. 89 safeguards, Art. 14 notice approach, record of processing, DPIA screening | founder | Step 3 |
| L6 | Privacy notice published on the OSF project page (template §5) | founder | Step 3 |
| L7 | Zero-intervention rule acknowledged by every agent (§6) | agents | always |
| L8 | Disclosure hygiene rules (§7) in code (k ≥ 10 check, no names) | agents | any output |
| L9 | Licences/attribution: GH Archive (CC-BY-4.0 site content), OSV/GitHub Advisory DB, Wikidata (CC0?), GLEIF terms, EPSS terms, OpenCorporates share-alike if used | agents | publication |
| L10 | OSF pre-registration filed before outcomes are unmasked | founder | Step 5 |
| L11 | Data retention: raw data deleted 12 months after publication; salted IDs only in releases | agents | publication |
| L12 | Secrets found in any config/IaC file: never stored, never reported, counted only | agents | Step 8 |

## 2. Policy texts

### 2.1 GitHub Acceptable Use Policies, §7 "Information Usage Restrictions" (VERIFIED)
Source: `github/docs` → `content/site-policy/acceptable-use-policies/github-acceptable-use-policies.md`
(https://docs.github.com/en/site-policy/acceptable-use-policies/github-acceptable-use-policies).

> You may use information from our Service for the following reasons, regardless of whether the
> information was scraped, collected through our API, or obtained otherwise:
> * Researchers may use public, non-personal information from the Service for research purposes,
>   only if any publications resulting from that research are open access.
> * Archivists may use public information from the Service for archival purposes.
>
> Scraping refers to extracting information from our Service via an automated process, such as a
> bot or webcrawler. Scraping does not refer to the collection of information through our API.
> Please see Section H of our Terms of Service for our API Terms.
>
> You may not use information from the Service (whether scraped, collected through our API, or
> obtained otherwise) for spamming purposes, including for the purposes of sending unsolicited emails
> to users or selling personal information, such as to recruiters, headhunters, and job boards.
>
> Your use of information from the Service must comply with the GitHub Privacy Statement.

Also §6: "You will not reproduce, duplicate, copy, sell, resell or exploit any portion of the
Service ... without our express written permission." And §8: "Misuse of personal information is
prohibited."

**Implications.** (a) Every publication — paper, preprint, blog posts — is open access. (b) The
research clause covers *non-personal* information: usernames, emails and commit identities are
personal data → do not use them as research data; hash at ingestion, keep only aggregates and
non-personal attributes (org type, domain of an organisation, counts). (c) Skylayer is a company:
the research must be genuine research with open publication, not lead generation — **never** use the
data to contact, market to, or profile maintainers or companies (§6 of this file).

### 2.2 GitHub Terms of Service, §H "API Terms" (VERIFIED)
> Abuse or excessively frequent requests to GitHub via the API may result in the temporary or
> permanent suspension of your Account's access to the API. GitHub, in our sole discretion, will
> determine abuse or excessive usage of the API. ...
> You may not share API tokens to exceed GitHub's rate limitations.
> You may not use the API to download data or Content from GitHub for spamming purposes, including
> for the purposes of selling GitHub users' personal information ...
> All use of the GitHub API is subject to these Terms of Service and the GitHub Privacy Statement.
> GitHub may offer subscription-based access to our API for those Users who require high-throughput
> access or access that would result in resale of GitHub's Service.

Rate limits (VERIFIED, 02 §S2): 5,000 REST req/h; 5,000 GraphQL points/h; secondary limits.

### 2.3 Dependabot badge endpoint
No published terms were found; the endpoint is GitHub infrastructure called by GitHub's own
`dependabot/fetch-metadata` Action. Polling it at scale is arguably "use of the Service"; the founder
requires **written OK from GitHub** first (L2). Until then: at most the Step-0 single request and the
≤50-request keying test only if GitHub's reply allows it.

### 2.4 Mend (BLOCKED)
Terms of Service `https://www.mend.io/terms-of-service/` and Acceptable Use Policy
`https://www.mend.io/acceptable-use-policy/` could not be read from the design container. Search
snippets say use must follow the AUP and Mend may suspend on violation. Treat automated badge reads
as **not permitted** until Mend says yes in writing (L3).

### 2.5 GDPR (links BLOCKED; articles cited from the regulation, text to be re-read by counsel)
- **Applicability.** Maintainers include EU residents. Art. 3(2)(b) extends the GDPR to controllers
  outside the EU that monitor the behaviour of people in the EU; tracking when named accounts merge
  PRs is arguably monitoring → **assume GDPR applies** regardless of where Skylayer is incorporated.
  (Check also the founder's local law, e.g. Israel's Privacy Protection Law, with counsel — UNVERIFIED.)
- **Personal data here:** GitHub logins, user IDs, names, emails, commit author identities, avatar
  URLs; possibly an org login when the org is effectively one person.
- **Lawful basis:** Art. 6(1)(f) legitimate interests (scientific research on software security),
  documented in an LIA; Art. 89(1) safeguards: data minimisation, pseudonymisation (VERIFIED-SNIPPET:
  Art. 89 safeguards must "ensure respect for the principle of data minimisation").
- **Research scope:** Recital 159 — "scientific research" is interpreted broadly, including
  privately funded research (VERIFIED-SNIPPET), but safeguards still apply.
- **Transparency:** data are not collected from the subjects → Art. 14 notice; Art. 14(5)(b) exempts
  where notice is impossible or would involve disproportionate effort, "in particular for ...
  scientific ... research purposes subject to the conditions and safeguards referred to in Art.
  89(1)", provided the controller makes the information publicly available → publish the privacy
  notice (§5) on the OSF page. (Text from memory; UNVERIFIED — counsel to confirm.)
- **Special categories:** none collected. Do not infer nationality, gender, etc.
- **Rights:** provide an email for objections; honour erasure/objection by adding the hashed ID to a
  suppression list and re-running aggregates.

### 2.6 IRB / human-subjects
- Skylayer has no IRB; US Common Rule binds federally funded/institutional research, but an
  exemption **determination** is still wanted for publication and ethics.
- Most relevant category: **45 CFR 46.104(d)(4)(i)** — "Secondary research uses of identifiable
  private information ... if ... (i) The identifiable private information ... [is] publicly
  available" (VERIFIED-SNIPPET via eCFR/LII search results; eCFR BLOCKED). The study also involves no
  interaction or intervention with people.
- **Routes:** (a) an academic co-author's IRB (free; recommended — also helps the OA venue);
  (b) an independent commercial IRB (fee UNVERIFIED; may exceed the budget — README D5).
- Submit: protocol (01, 03, 04, 07), data-management plan (§4), privacy notice (§5).

### 2.7 Open-access publication
Required by GitHub AUP §7. Plan: arXiv preprint (CC-BY) + an open-access venue (e.g. MSR/ICSE/
security venues with OA options, or a gold-OA journal); blog posts link the preprint.

## 3. Draft letters (send in Step 1)

### 3.1 To GitHub (support ticket, category API/Terms; keep the ticket number)
> Subject: Research request — polite polling of Dependabot compatibility-score badges
>
> Hello, I am <name> at Skylayer. We are running a pre-registered, open-access research study
> (<OSF link>) on how the safety evidence shown on Dependabot security pull requests relates to when
> they are merged. We would like permission to fetch the public compatibility-score badge images
> (dependabot-badges.githubapp.com/badges/compatibility_score?...) that appear in public PR bodies,
> for security-update PRs in about <N> public repositories, at <8–40> fetches per PR over its life,
> never more than 1 request per second in total, with the User-Agent "<UA>" and caching, for
> <16–26> weeks, plus a weekly 1% sample through camo to measure caching. We will not interact with
> any repository, will publish aggregate results only (open access, per AUP §7), never name
> repositories with unmerged fixes, and will stop immediately if asked. If GitHub can share historical
> score or badge-render data under a research agreement, we would welcome that too.
> Contact: <email>.

### 3.2 To Mend (support/legal; keep the reply)
> Subject: Permission request — reading Merge Confidence badges for an open-access research study
>
> (Same content, for developer.mend.io/api/mc/badges/{confidence,age,adoption,passing}/... URLs in
> public Renovate PR bodies; ask whether automated reads at ≤1 req/s are allowed under Mend's terms,
> whether an API or data agreement exists, and whether the Merge Confidence algorithm changes are
> logged so we can note them.)

### 3.3 To the IRB (academic partner or independent)
> Request for exemption determination: secondary analysis of publicly available GitHub activity and
> public badge images; no interaction or intervention; identifiers hashed at ingestion; aggregate
> publication; protocol and DMP attached; requested category 45 CFR 46.104(d)(4)(i) or "not
> human-subjects research".

## 4. Data-management plan (summary)

- **Collect only:** public events and PR metadata; badge values; repo files needed for the rules;
  commit-email **domains** (never local parts); org profile fields.
- **Pseudonymise at ingestion:** HMAC-SHA256(login or id, secret salt) for people; repo/org IDs
  salted-hashed in any shared or released table. The salt lives outside the data directory.
- **Restricted file:** `owners_private.parquet` (org logins/domains in clear) only for classification
  and validation; encrypted disk; never uploaded.
- **Storage:** founder-controlled encrypted disk/VM; GCP project with minimal IAM; no data in the
  `transcripts` repo, in chat logs, or in public buckets.
- **Retention:** raw JSON deleted after derived tables are validated (≤3 months after collection
  ends); derived tables deleted 12 months after publication except the released aggregate dataset.
- **Release:** aggregates with k ≥ 10 repos per cell; released row-level data (if any) contains only
  salted IDs, no timestamps finer than a day, no package-version pairs for unmerged fixes; release
  delayed 90 days after the analysis date.

## 5. Privacy notice (for the OSF page)

> **Skylayer Study 1 — privacy notice.** We analyse public GitHub activity (bot-written dependency
> pull requests, merge events, public repository files and public badge images) to study how safety
> evidence relates to how quickly security fixes are merged. Controller: Skylayer, <address,
> contact>. Legal basis: legitimate interests in scientific research (GDPR Art. 6(1)(f)) with Art. 89
> safeguards. We pseudonymise GitHub usernames at collection, never store email addresses (only the
> organisation domain), publish only aggregate results, and never name repositories or organisations
> with unmerged security fixes. Data are kept until <date> and then deleted. You can object or ask
> for erasure at <email>; we will exclude your account and recompute aggregates.

## 6. Zero-intervention rules (all agents)

- No comments, reviews, reactions, issues, PRs, forks, stars, follows, watches, or notifications on
  any repository or account in the study; no emails or messages to maintainers or companies found in
  the data; no use of the data for sales, marketing, recruiting or "outreach".
- Never delay, influence or trigger any fix; never re-run anyone's CI; never trigger Dependabot or
  Renovate.
- The lab runs **copies** of public code in isolated containers; no exploit code, no testing of any
  third-party system, no scanning.
- Only one exception class: GitHub/Mend/IRB correspondence about the study itself.

## 7. Disclosure hygiene

Repos with unmerged security fixes are live targets.
- Never name a repo, package instance, org or company with an unmerged security fix — in papers,
  posts, slides, OSF, chat, issues, or reports back to the founder. Reports use counts only.
- Illustrative examples in publications only from fixes merged ≥90 days earlier, with the owner's
  permission — or none.
- Cells < 10 repos are suppressed; small-ecosystem breakdowns merged into "other".
- If the analysis surfaces a systemic issue in a vendor's score (e.g. mis-scored badges), report it
  privately to GitHub/Mend first (coordinated disclosure), then publish in aggregate.
- If any file read in Step 8 contains a secret (token, key, password), do not store it, do not report
  its location; increment an aggregate counter only.
