# Skylayer Dashboard Mocks — PRD
**Three wedge candidates, one mechanism.** Internal working doc for the founders' wedge decision.
Last updated: 2026-09-26. Sources: `thesis.md`, `ledger.md`, and the 44 root-level transcripts in this repo.

> **This is a decision-support artifact, not a shipped product.** The three dashboards briefed
> below exist so the founders can *feel* what each pillar's product would look and act like
> before picking a wedge — not to define an MVP. Every pain point and workflow claim below is
> cited to a transcript (file + speaker), the way `ledger.md` cites claims. Anything that reads
> like a customer quote *is* one; nothing here is invented. **All KPI numbers written into the
> mockups themselves (MTTR figures, dollar amounts, percentages, counts) are illustrative demo
> data for the mockup, not measurements from any real customer.** Developers should treat every
> number on-screen as a placeholder to make the screen feel alive, never as a claim.

---

## 0. Shared intro — one mechanism, three surfaces

Skylayer's thesis (`thesis.md`) is that organizations don't fail to remediate because they don't
know what to fix — they fail because **nobody can prove a change is safe**, so the fix waits. The
mechanism we believe closes that gap is the same regardless of what's being fixed:

> **Model the dependencies → predict the blast radius → gate by confidence → revert when wrong.**

All three dashboards below are the same product skeleton with a different "finding" plugged in.
That's deliberate: the founders should look at all three side by side and recognize the family
resemblance, then judge each one on how hard its version of "blast radius" is to compute and how
believable its "gate by confidence" screen feels to a CISO who has been burned before.

| | Identity | Infrastructure patching | Code / app patching |
|---|---|---|---|
| Finding | over-privileged credential, stale session, retired-but-active account | CVE on a host/container/package | vulnerable dependency or code pattern in a repo |
| Blast radius | what else this identity can reach, across consoles | what services/SLAs sit downstream of this patch | what services import this library/function |
| Confidence signal | is this identity's activity on-baseline (IP, user-agent, time)? | did staging regression tests pass? | did CI/regression tests pass against the fix PR? |
| Cheapest place to start | hygiene actions on dormant/offboarded identities (reversible) | non-production / staging patches first | dependency bumps with no behavior change |

Two claims are already proven across 11+ unprompted interviews and should show up as texture on
every screen, not just the KPI header: **fear of breaking production is the real blocker** (not
speed or prioritization — C1 in `ledger.md`), and **buyers expect the vendor to take the action**,
not just point at it (C2). Two claims are explicitly *not* proven and the mockups should not imply
otherwise: nobody has given us a real MTTR, backlog size, or dollar figure from their own
environment (C8/"Unproven" in `thesis.md`), and whether large enterprises will actually let this
run autonomously is contested — Ariel Litvin (ex-CISO, First Quality; 11 years) says outright that
auto-remediation "doesn't work... simply doesn't work at the Fortune 500"
(`2026-09-04_security-leadership-discovery_ariel-litvin.txt`). The dashboards should make the
*gate* — not the automation — the hero, because that's the only version of this story anyone in
the evidence actually believed.

---

## 1. PILLAR: IDENTITY

### Evidence honesty check
This is the nascent pillar. There is no interview where a CISO owns an identity-remediation P&L and
walks us through their process end to end. What we have instead: one incident-response
practitioner describing the *mechanics* of identity-based containment across many client
environments in vivid, specific detail; one CISO who redirected her own stated top pain to
identity offboarding unprompted; one evaluator who named identity as the layer that makes network
irrelevant; and one CISO who ran an actual (if narrow) AI-agent design partnership on identity
hygiene because it was reversible. It's real signal, but it is breadth-of-mentions, not
depth-of-process — nobody has shown us their identity remediation runbook the way Mike Hiltz showed
us his patch pipeline.

### 1. Buyer / persona
The CISO or IAM/security-engineering lead evaluates and buys. Who **owns the blast radius if a
revocation goes wrong is fragmented and often not security at all**: Asaf, an incident-response
manager speaking from casework across many client environments, describes a single revocation
touching "the team that owns the application on AWS... the team that owns the AWS keys... source
control, which can be a completely different team... and the DB administrators who own the
databases" — and says "before every revocation you have to coordinate and understand the business
impact" (`2026-09-01_asaf-shoval-yuval.txt`). Leda Muller (IT/security leadership, Stanford's
business-within-a-business unit) confirms the ownership problem from the practitioner side:
offboarding isn't "always about RBAC," because employees accumulate access to third-party apps
outside SSO that nobody remembers to revoke (`2026-08-31_network-security-discussion_leda-muller.txt`).
Mandy Andres (CISO, Elastic) is the exception that proves the rule: at a company with no
traditional network, identity visibility (access keys, API tokens) *is* the security team's main
lever, squarely under her (`2026-09-08_elastic-ciso-security-discussion.txt`).

### 2. Core objects
A "finding" here is one of:
- an **over-privileged or stale access key / credential** (Asaf IR: "30 AWS accounts and 100 access
  keys" needing revocation in one incident)
- a **retired-but-still-active identity** — Leda Muller: "even if it's gone to an inactive state or
  retired state, to me that doesn't mean anything, because if I was a hacker, I would start
  activating all of these retired [accounts]... they're still in the system"
- a **non-human identity / ephemeral token** nearing end-of-life — Elastic's stated program: "moving
  to short-lived ephemeral tokens and sessions," working toward nobody ever touching the raw secret
- a **reversible hygiene action** on the identity side generally — the category Andrew (ex-Nestlé,
  now veterinary-sector CISO) actually let an AI-agent design partner touch, because "in worst case
  scenario, you just have to turn something back on that you've turned off"
  (`2026-09-15_skylayer-product-strategy-advisory.txt`)

### 3. Impact assessment view — what "blast radius" means for identity
Blast radius here is **lateral reachability**, shown as a live graph rooted at the credential in
question. Asaf's description of how these incidents actually unfold is the literal spec for this
screen: an attacker (or an audit) finds one access key, enumerates what it can reach, and the graph
grows recursively — "I found access keys that give me access to AWS, and inside AWS I can go to
Secrets Manager, and from there I find a secret to that org's GitHub, and inside their repos there
are more secrets, and it just keeps going" — a **parallel, recursive expansion**, not the old
sequential kill chain, that only stops "when it truly runs out of new assets to find"
(`2026-09-01_asaf-shoval-yuval.txt`). The dashboard should render exactly that: a directed graph
that expands hop by hop (AWS account → Secrets Manager → GitHub → more secrets), a running count of
"assets reachable from this credential," and a confidence signal built from **behavioral
baseline** — is this key being used from its normal IP/user-agent/time-of-day, or has it drifted
("if the same key was used from IP X for the whole past year and now suddenly gets used from a
different address, that's a flag" — Asaf, same file). Below the graph, a **cross-team impact
panel** lists which consoles/teams this specific revocation would touch (AWS, source control, DB
admin, EDR) — turning Asaf's "you have to coordinate and understand the business impact" from a
frantic Slack thread into a single screen.

### 4. Remediation / action view
A gated queue, split identically to the other two pillars:
- **Auto-approved lane**: single dormant/retired credentials with zero recent activity and no
  write-scope to production — the hygiene category Andrew's design partner was trusted with.
- **Needs-human-review lane**: any credential with active production write-scope, or any batch
  revocation spanning multiple teams/consoles (the 30-accounts/100-keys scenario) — each one shows
  which teams must sign off before the button is live, directly mirroring Asaf's "before every
  revocation you have to coordinate."
- **Rollback / one-click-undo**: reinstate an access key or session instantly — Israel Bryski's
  general remediation demand applies directly here: "if you broke something, give me a one-click
  undo, unrollback button" (`2026-08-31_security-leadership-discovery_israel-bryski.txt`).
- **Change-management trail**: a timestamped log of who/what revoked which credential, which team
  approved it, and what was reachable from it at the time — the artifact Asaf implies incident
  responders currently reconstruct by hand under time pressure.
- **Read-only / write toggle**: defaults to read-only (list, graph, flag) with write access
  (revoke, disable) a separate, explicitly granted mode — matching Andrew Dutton's "even when I
  deploy something, it's only gonna be read-only, I'm not gonna trust it to shoot a gun"
  (`2026-09-09_security-leadership-discovery_andrew-dutton.txt`) and Harris Schwartz's insistence
  that a vendor "start off with read-only access, let's see how that goes, and then maybe you could
  move into write access" (`2026-09-16_security-leadership-discovery_harris-schwartz.txt`).

### 5. KPIs / metrics header (illustrative demo data — not real figures)
- **Credentials with no owner acknowledgment > 30 days:** `142` — the Leda Muller "retired but
  still active" problem, made visible.
- **Median time to full containment** (first credential found → last credential in the blast
  radius revoked): `18 min` — this is the metric Asaf's story is actually about: speed of
  *complete* containment, not just first response.
- **Revocations completed without a production incident:** `97%` — the safety metric every
  pillar shares (thesis C4/C5: proof is the moat, reversibility earns trust).
- **Cross-team coordination time avoided this month:** `31 hrs` — a stand-in for the
  Matthew-Matturro-style "hours recovered per week" framing he uses to justify any automation
  (`2026-09-16_security-leadership-discovery_matthew-matturro.txt`), applied to identity ops.
- **Stale/dormant identities auto-flagged this week:** `58`

### 6. "Wow" moments
1. **The recursive blast-radius animation.** Drop in one leaked access key and watch the graph
   expand hop by hop exactly the way Asaf described it live — AWS → Secrets Manager → GitHub →
   more secrets — with a running "assets reachable" counter. This is the single most concrete,
   filmable incident-response story in the whole evidence base, staged as a screen.
2. **The 30-accounts/100-keys containment console.** A single view that lists every AWS account
   and access key touched by one incident, grouped by which team owns each one, with a "coordinate
   revocation" button that pings each owner instead of an incident commander doing it by hand.
   This directly answers Asaf's "it's very hard to figure out on the fly."
3. **The ghost-account panel.** A quiet list titled "retired — but still active," pulled straight
   from Leda Muller's fear, with a one-click "deactivate for real" action — the kind of screen that
   makes a CISO wince because they already know the answer.
4. **The "nothing here can break production" banner.** On the auto-approved lane specifically,
   because reversibility is the entire reason this pillar's evidence exists at all (Andrew's design
   partnership only worked because hygiene actions were undoable).

### 7. UI-safe anonymized copy
For on-screen "why this matters" panels and empty states — no real names, companies, or
verbatim-attributable quotes:
- *"IT/security leader, large research institution"* — "Offboarding isn't just one system. People
  pick up access to a dozen tools over their time here, some outside single sign-on, and nobody
  remembers to take it all back. If I were an attacker, the accounts I'd go after first are the
  ones everyone already assumes are dead."
- *"Incident responder, works across many client environments"* — "A real incident isn't one
  stolen key, it's dozens, spread across accounts and tools that don't share a console. Before you
  can even start revoking, someone has to work out what breaks if you do — and that coordination is
  the slowest part, not the detection."
- *"CISO, healthcare-adjacent organization"* — "We let an outside team automate a narrow slice of
  identity cleanup — the kind where, worst case, you just turn something back on. That's the only
  reason it got approved at all."
- *"CISO, cloud-native software company"* — "We don't have a traditional network to defend, so
  identity — keys, tokens, sessions — is where almost all of our visibility work already lives."

---

## 2. PILLAR: INFRASTRUCTURE PATCHING (OS / package / container / CVE)

### Evidence honesty check
This is the strongest cluster in the corpus by a wide margin — one CISO walked us through his
entire pipeline end to end, an a16z investor gave a structural argument for why the space is ripe,
and a second practitioner described the exact remediation gap in his own environment. This pillar
is not thin; it is thesis.md's own "Option B."

### 1. Buyer / persona
CISO/CIO jointly evaluate; **who owns the blast radius if a patch breaks something is usually not
security** — it's the engineering/platform team that owns the service, mediated by change
management. Mike Hiltz (CIO+CISO, nference/Anumana) describes the actual mechanics: "it really is
defining which groups are responsible... we go through the process of opening change management or
change control tickets... there are package dependencies that we have to consider"
(`2026-09-24_vulnerability-remediation-process-discussion.txt`). Israel Bryski generalizes the
ownership boundary directly: "anything that can impact the reliability, the stability of the
production environment... that's usually your indicator that the CIO will need to be involved"
(`2026-08-31_security-leadership-discovery_israel-bryski.txt`). Ariel Litvin adds the sharpest
version of the same point for the network-adjacent slice of infra: "the network team doesn't report
to security in — I want to say — 85% of organizations," and he could only force change there because
he reported to the Chairman, not the CIO (`2026-09-04_security-leadership-discovery_ariel-litvin.txt`).

### 2. Core objects
A "finding" is a **CVE on a specific host, container image, or package version** — Mike's own
example is log4j: a vulnerable file present in a deployed image but not actually running or
reachable (`vulnerability-remediation-process-discussion.txt`). Other object types raised
unprompted: **misconfigured cloud resources** (Mike: "for misconfigurations in cloud, I think we're
in a better spot"), **stale base images** needing rebase to a secure baseline (Mike names Wolfi by
name), and **legacy protocol/server instances** that never get retired — Ariel Litvin: "there are
SMBv1 and TLSv1 servers... running in organizations for years."

### 3. Impact assessment view — what "blast radius" means for infra patching
Blast radius is a **dependency graph of what's downstream of a patch**: which services consume the
package, which teams own those services, and what regression risk they carry. Mike's own words are
almost a product spec: "if you can see that blast radius, now you know the overall impact"
(`vulnerability-remediation-process-discussion.txt`). Confidence is built from **automated
regression-test results in staging before the patch ever reaches production** — Chris (Head of
Security, mid-size SaaS company) names this exact flow unprompted: "this version of this dependency
is out of date, just go fix it, or get it into stage at least, and then run it through the
automated regression testing" (`2026-09-10_cybersecurity-startup-advisory-discussion.txt`). Asaf
(a16z) frames the most ambitious version of this screen — borrowing explicitly from Cognition's
approach — as generating a test suite against the *current* production behavior first, so the
system can "prove that after upgrading, nothing would happen" before it ever proposes the patch
(`2026-09-22_a16z-intro-call.txt`). Mike's log4j example is the screen's most important nuance: a
CVE that is technically present but unreachable/not-running should show as low-blast-radius even
though the finding itself is "critical" — teaching the CISO viewer that the dashboard reasons about
*reachability*, not just CVSS score.

### 4. Remediation / action view
- **Auto-approved lane**: patches where staging regression tests pass at 100% and no downstream
  service is flagged as SLA-sensitive — the exact scenario Mike describes as the end state: "I have
  a consensus, I can do this without breaking anything... this is fine to patch, no human
  intervention, go ahead and push it" (`vulnerability-remediation-process-discussion.txt`).
- **Needs-human-review lane**: anything touching a regulated or SLA-bound system. Mike is explicit
  that this can be a hard requirement, not a preference: "anytime we make a change like this, even
  for patching, for an FDA-approved medical device, it has to go back to the FDA." Review items
  surface as a PR-style card — Mike's own framing: "it could be just a gate, right? Yep, this looks
  good, approved, just like you do GitHub PRs."
- **Rollback / one-click-undo**: Mike names this directly as the thing that makes remediation
  possible for him at all — "being able to test, I have a way to roll back." Israel Bryski's
  one-click-undo demand applies here too.
- **Change-management trail**: a ticket-shaped record per patch (which group was responsible,
  which tests ran, who approved) — this is literally how Mike's org already works; the dashboard
  should look like an upgrade to that process, not a replacement of its paper trail.
- **Read-only / write toggle**: defaults to "detect + recommend" only, consistent with Andrew
  Dutton's and Harris Schwartz's read-only-first stance, generalized from identity to infra.

### 5. KPIs / metrics header (illustrative demo data — not real figures)
- **MTTR (mean time to remediate, critical/high):** `4.2 days` — the metric Mike frames as having
  been cut roughly in half already by faster exploitation timelines, though he never gave us his
  own number; shown here only as demo texture.
- **Patch backlog burn-down:** `1,204 → 340 this quarter` — a direct answer to Andrew Dutton's
  complaint that telling a plant a bare count ("you've got 15,000 vulnerabilities, you better fix
  your stuff now... that means nothing") is useless without a trend and a "why it matters"
  (`2026-09-09_security-leadership-discovery_andrew-dutton.txt`).
- **% auto-remediated safely, zero incidents:** `89%` — the number the whole thesis is staked on
  (C4/C5).
- **Engineer-hours recovered this week:** `26 hrs` — modeled directly on Matthew Matturro's stated
  methodology for deciding what to automate at all: "what are the things they do in a 40-hour week
  ... and what time would they get back?" (`2026-09-16_security-leadership-discovery_matthew-matturro.txt`).
- **Risk bought down per dollar spent:** `$10 : $1` — Matturro's own framing for what a board wants
  to hear: "I'm spending $100,000 a year with you to buy down a million dollars of risk. That's a
  10-to-1 ratio."
- **Change-management tickets closed without escalation:** `212 / 218`

### 6. "Wow" moments
1. **The log4j "present but not running" screen.** A critical CVE that the dashboard downgrades in
   priority because the vulnerable code path is unreachable in this deployment — directly
   dramatizing Mike's real example and teaching the CISO viewer the dashboard reasons about actual
   risk, not just severity labels.
2. **The confidence-gated push button.** A patch card showing "regression tests: 47/47 passed,
   0 downstream services flagged, no human intervention required — push?" next to a second card
   for an FDA-regulated system that's hard-blocked with "requires regulatory sign-off" — showing
   both ends of Mike's own spectrum on one screen.
3. **The blast-radius graph for one patch.** Click a CVE, see every downstream service and the team
   that owns it, instead of a bare CVSS score — literally Mike's "if you can see that blast radius,
   now you know the overall impact," rendered.
4. **The backlog-with-a-story view.** Instead of "15,000 vulnerabilities," a burn-down chart with
   the top-line why-it-matters sentence Andrew Dutton asked for, per item.
5. **The one-click rollback receipt** after a bad patch — proof the system reverted itself before
   anyone had to file an incident.

### 7. UI-safe anonymized copy
- *"CIO/CISO, health-tech company operating in a regulated space"* — "Patching is our biggest pain
  point, mostly because of volume and because every change to a regulated system has to be
  provable, tested, and — sometimes — reported before it can go live. If I can see exactly what a
  patch affects downstream, I can approve it in minutes instead of days."
- *"Head of security, mid-size software company"* — "We know which dependency is out of date. The
  hard part has never been knowing — it's tracing who owns the affected service, opening the
  change ticket, running regression tests, and getting a human to sign off. I want to see the
  actions taken and just approve them, not re-do the investigation myself."
- *"Retired CISO, large manufacturer"* — "In a real production environment you cannot afford to be
  wrong. 'We'll patch automatically and fix it fast' sounds nice in a pitch. In practice, legacy
  systems sit unpatched for years because nobody will risk the outage — the tooling has to earn
  trust before it gets anywhere near a write action."
- *"Advisor to financial-services vendors"* — "Tell me what's broken, fix it, and tell me you fixed
  it. I don't want another dashboard that just reports the same problem back to me."

---

## 3. PILLAR: CODE / APPLICATION PATCHING (vulnerable dependencies, code-level fixes)

### Evidence honesty check
**This is the thinnest pillar in the corpus, and it should be reported as thin, not dressed up.**
No interviewee describes an end-to-end code-remediation workflow the way Mike Hiltz described infra
patching. What exists: one practitioner's dependency-out-of-date example (which is really a
special case of the infra-patching flow, just scoped to a repo/package rather than a host); one
investor's structural argument for why "prove the patch is safe" generalizes to code via automated
test generation (explicitly modeled on Cognition, a coding-agent company, not a security vendor);
and one fractional CISO's adjacent-but-different worry about developers pasting code into AI tools
(a data-exposure concern, not a remediation-workflow one). `thesis.md` is honest about this too: it
places Skylayer's evidence here as "closer to Cognition and to Reclaim Security" — i.e., adjacent to
AI coding-agent companies that auto-fix code and open PRs — rather than pointing to a security buyer
who described wanting this. Treat every claim below accordingly; there is real color, but it is
borrowed from an adjacent workflow (dependency patching) more than it is a security buyer's own
described pain.

### 1. Buyer / persona
The most plausible buyer is an **AppSec/product-security lead** — Matthew Matturro (CISO,
healthcare-tech company) names "product security" as one of his three organizational pillars
alongside GRC and security operations (`2026-09-16_security-leadership-discovery_matthew-matturro.txt`),
which is the closest thing in the corpus to a named owner for this pillar. **Who owns the blast
radius is the engineering team that owns the repo/service**, not security — Chris (Head of
Security, Wistia) describes exactly this handoff: "we have different teams... responsible for
different components... it's really you know for us anyway, it's very painful, we have to fan out
and try to identify which engineering groups are responsible"
(`2026-09-10_cybersecurity-startup-advisory-discussion.txt`). Harris Schwartz's worry — a developer
pasting proprietary code into an AI tool to "find the problems" — points to a second, adjacent
buyer (data-loss-prevention/AI-governance), not this one; it's included only because it's the
closest thing to "code" as an attack surface anyone raised unprompted
(`2026-09-16_security-leadership-discovery_harris-schwartz.txt`).

### 2. Core objects
A "finding" is a **vulnerable or outdated dependency in a repository or service**. Chris's own
example: "this version of this dependency is out of date... run it through the automated
regression testing." The one full worked example anyone gave — Mike Hiltz's log4j story — actually
lives at the boundary between this pillar and infra patching: the vulnerable *file* ships inside a
container image (infra object) but the underlying question ("is this dependency actually reachable
in code, or just present") is a code-level analysis. That overlap is worth naming explicitly to the
founders: **code and infra patching may not be two different wedges so much as two zoom levels
on the same dependency graph.**

### 3. Impact assessment view — what "blast radius" means for code patching
Blast radius is **which services/consumers actually import or call the vulnerable
package/function** — the code-level version of Mike's "is it running" question, scoped to source
rather than deployed infrastructure. The strongest evidence for how confidence should be built here
is borrowed, explicitly, from a company outside security: Asaf (a16z) describes Cognition's actual
method — "they create a huge amount of tests for your production so they know what your current
deployment does... then when they try to do patches... they have a much broader set of tests they
can run against, and they know what changed" — and proposes Skylayer do the security-specific
version of that: "if you are able to create a set of tests that run against the current
environment and then you can prove that after upgrading nothing would happen, then I think you can
have something here" (`2026-09-22_a16z-intro-call.txt`). Yuval (Skylayer co-founder, same call)
names this correctly as "kind of an impact assessment" — which is the same phrase this whole
mechanism uses everywhere else in the corpus.

### 4. Remediation / action view
- **Auto-approved lane**: dependency version bumps where the generated regression suite shows
  zero behavior change and no security-sensitive code path is touched.
- **Needs-human-review lane**: anything touching authentication, data handling, or a public API —
  surfaced as a pull request with the generated tests attached, echoing Chris's stated ideal
  end-state exactly: "these are the actions I've taken, I need you to review and push the button to
  say that this is an acceptable fix."
- **Rollback / one-click-undo**: revert the merged PR and redeploy the previous version —
  structurally identical to the other two pillars' rollback, just scoped to a git revert instead of
  a config or credential rollback.
- **Change-management trail**: the PR itself *is* the change-management record here — this pillar
  is the one place where "change management" and "version control" are almost the same artifact,
  which is worth showing explicitly since it's a real structural advantage over the other two
  pillars' change-management overhead.
- **Read-only / write toggle**: defaults to "open a PR, don't merge it" — the code-native version of
  read-only-first.

### 5. KPIs / metrics header (illustrative demo data — not real figures)
- **Vulnerable dependencies open across tracked repos:** `312`
- **% of fixes shipped as an auto-generated PR (merged, not just opened):** `41%`
- **Regression-suite pass rate on generated fixes:** `98.6%`
- **Median time, disclosure → merged fix:** `36 hrs` — a code-scoped stand-in for the same
  time-to-exploit urgency `thesis.md` opens with (Mandiant/VulnCheck time-to-exploit data),
  illustrative only.
- **Engineer review hours saved this week:** `14 hrs` — same Matturro-style hours-back framing
  used in the other two pillars, for comparability.

### 6. "Wow" moments
1. **The generated-test proof screen.** Before proposing a dependency bump, show the system writing
   a regression-test suite against *current* behavior first, then running it against the proposed
   fix — dramatizing Asaf's Cognition-style pitch ("prove that after upgrading, nothing would
   happen") as a concrete, watchable two-step process rather than an abstract promise.
2. **The PR-as-remediation screen.** A vulnerability finding that resolves not into a ticket but
   into an actual, reviewable pull request with a diff, a test result, and a single approve button
   — Chris's literal ask, staged.
3. **The "present but not reachable" code-path view**, the code-level sibling of the infra pillar's
   log4j screen — showing a vulnerable function that exists in the codebase but is never called in
   the deployed build, so it's correctly deprioritized instead of triggering a false-urgency ticket.
4. **A frank "this is early" empty state** (internal-team-facing, not for the CISO viewer): a note
   that this pillar's workflow is inferred from one dependency-patching example and one investor's
   analogy to a coding-agent company, not from a security buyer's own described process — so nobody
   mistakes the mock's confidence for validated evidence.

### 7. UI-safe anonymized copy
- *"Head of security, mid-size software company"* — "When a dependency needs updating, the fix
  itself usually isn't the hard part — it's finding which team owns the affected component,
  getting it staged, and running it through regression testing before anyone will approve pushing
  it."
- *"Investor and advisor to security startups"* — "Historically, almost nothing gets patched,
  because people are afraid to touch production. The way through that isn't a faster scanner — it's
  being able to prove, with real tests, that a fix won't change behavior before you ask anyone to
  approve it."
- *"Fractional CISO, mid-market manufacturer"* — "One thing I actively block is developers pasting
  our code into outside AI tools to get it 'fixed.' Whatever tool does that job needs to keep the
  code and the fix inside our own boundary."

---

## Appendix: cross-pillar notes for the mockup developers

- **Keep the shell identical across all three.** Same header KPI strip layout, same three-pane
  structure (findings list → impact-assessment detail → gated action queue), same color language
  for auto-approved / needs-review / blocked. The point of building all three is to let the
  founders compare pillars, not dashboards.
- **The confidence gate is the product, not a feature of the product.** Every "wow" moment above is
  really the same screen — a system showing its work before asking for a write action — reskinned
  per pillar. If a reviewer doesn't feel the gate, the mock has failed regardless of how good the
  graph visualization looks.
- **Do not let the identity or code mockups imply more validated process than the transcripts
  support.** Where the infra pillar can show a screen that mirrors an interviewee's literal
  described workflow (Mike Hiltz), the identity and code pillars are extrapolating from thinner,
  more anecdotal evidence — reversibility framing (identity) and an investor's analogy to a
  non-security company (code). That's fine for a decision-support mock; it would not be fine to
  carry into a real PRD without saying so, which is why this document says so twice.
