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

### 0.1 Recommendation

**Lead the decision-support exercise with Option B — infrastructure/OS/package/container
patching — but keep all three mocks in front of the founders side by side.** Ranked on two
separate axes, not one:

- **Evidence strength:** infra (9/10 — Mike Hiltz's end-to-end pipeline, Chris's regression-test
  flow, Asaf/a16z's structural argument) > identity (5/10 — breadth-of-mentions from four
  sources, no single owned end-to-end process) > code (2/10 — one borrowed example plus an
  investor's analogy to a non-security company).
- **Feasibility risk (can Skylayer actually build the "blast radius" computation this pillar
  needs):** identity's is arguably *cheaper* than infra's despite thinner evidence — a
  cross-console reachability graph (AWS IAM → Secrets Manager → GitHub) is a data-access problem
  (can we get API scopes to enumerate what a key reaches), while infra's regression-test-based
  confidence gate requires standing up a staging/CI harness credible enough for an FDA-regulated
  buyer to trust with an automated push. Code's feasibility is closest to identity's (git/CI
  integration, not novel infra) but inherits infra's regression-harness dependency without
  infra's depth of process evidence to de-risk it.

Infra wins on both axes when weighted for what a founder decides *first*: it is the only pillar
where a real practitioner (Mike) has already described the workflow end to end, which means the
mock can be built against a validated process rather than an extrapolation, and it is the pillar
where a design-partner ask ("what do we need to build before Mike says yes," `thesis.md` open
question 5) is answerable today. Identity's cheaper-seeming feasibility does not outweigh this,
because identity's mock still has to invent the cross-console reachability mechanism from
scratch with zero interviewee describing a system (rather than a human investigator) doing it —
see §0.2.

**This recommendation does not satisfy `thesis.md`'s own decision rule.** The rule is explicit:
"run the next three calls on Option B's framing. Three more Mikes settles it." Status as of
2026-09-25 is **NOT MET** — the three most recent calls (Ariel, Asaf IR, Jason Lawrence) are
backfill from before Mike's call and were not run on Option B's framing. So this recommendation
is a **provisional lead, not a settled pick**: build and show all three mocks, but brief the
founders that Option B is the working hypothesis pending those three forward-looking calls, and
that if Mike turns out to be atypical (see §2 evidence-honesty note on C9), Option A/identity
should be revisited before committing engineering time past the mock stage.

### 0.2 Technical feasibility — the unproven proof mechanism

`thesis.md`'s own "Unproven" section states plainly: "We don't know what evidence we can actually
produce, or how. Everything else is downstream of this." This is the single biggest open
technical question behind every pillar's "wow moment," and it must not be papered over by how
smooth the animation looks:

- **Identity**: the recursive blast-radius graph (§1.3/§1.6) depicts what Asaf described an
  *incident responder piecing together by hand* — no evidence in the transcripts says Skylayer
  has, or can get, live cross-console reachability data (AWS IAM policy evaluation, Secrets
  Manager access, GitHub org-level secret scanning) needed to compute this automatically. A live
  version would require standing IAM/audit-log read access across every connected AWS account,
  Secrets Manager list/read permissions, and a GitHub App with org-wide secret-scanning scope —
  none of which any interviewee describes granting a vendor today.
- **Infra**: partially grounded — Mike's own workflow already produces change-management tickets
  and staging regression results, so the mechanism has a real analog. A live version still
  requires CI/staging integration deep enough to run and score regression suites automatically,
  which nobody in the evidence has handed a vendor yet.
- **Code**: the generated-test-suite mechanism (§3.3/§3.6) is borrowed wholesale from Cognition,
  a coding-agent company, not a security vendor's own demonstrated capability. A live version
  requires source-control write access plus a test-runner/CI integration capable of generating
  and executing a regression suite against arbitrary repos — an even larger lift than infra's,
  with less evidence it's wanted from a security vendor specifically.

**Mock-building rule:** none of the three dashboards may read as "we already have this working."
Every wow-moment scene (§1.6/§2.6/§3.6) must be staged as a **demonstration of the intended
mechanism**, not a claim of a live capability — see each pillar's acceptance criteria for the
specific on-screen language required.

### 0.3 Risks & assumptions

1. **Unproven proof mechanism (highest-priority risk).** See §0.2. If Skylayer cannot actually
   compute cross-console blast radius (identity) or reliable regression-based confidence (infra,
   code), the entire "gate by confidence" mechanism — the hero of every screen — has nothing
   real behind it. Mitigation for the mock stage: stage the mechanism as an intended workflow
   (§0.2's rule), not a shipped capability.
2. **Blast-radius ownership is fragmented, and the auto-approved lane assumes it isn't.** All
   three pillars' own evidence says the person who owns the blast radius if something breaks is
   usually *not* the security buyer: identity ("the team that owns the application on AWS... the
   team that owns the AWS keys... source control... the DB administrators," Asaf IR), infra
   ("usually not security," Israel Bryski; "the network team doesn't report to security in ~85%
   of organizations," Ariel Litvin), code (Chris/Wistia: "we have to fan out and try to identify
   which engineering groups are responsible"). **Product consequence:** the "auto-approved lane"
   central to all three dashboards assumes the security buyer (CISO) can unilaterally authorize
   a write action. The evidence says that authority is fragmented across teams the CISO doesn't
   control in most orgs. This may not hold outside identity's narrowest hygiene case (dormant,
   zero-write-scope credentials — the one category Andrew's design partner was actually trusted
   with). `thesis.md` open question 3 ("who is the buyer — the CISO, or the platform owner who
   gets paged") is unresolved and this PRD does not resolve it either; it only requires the mock
   to stop hiding the question. **Build requirement:** the cross-team-approval step (identity
   §1.4's needs-human-review lane, infra §2.4's change-management gate, code §3.4's review lane)
   must be a first-class, visually unmissable part of every dashboard's remediation view — not a
   secondary panel, footnote, or collapsed section — specifically because a real buyer will
   object "I can't approve this for anything that touches another team's stuff" within the first
   five minutes of a live demo.
3. **Willingness-to-pay gap.** `ledger.md` C8: "NO evidence found in 40 calls. Zero budget lines,
   zero approval chains, zero design partners" — including direct pushback (BioChrist CISO:
   "don't bother chasing... they're cutting everything"; Andrew: "I only want to spend $1,000 a
   year, you'd go broke"). Mike Hiltz's only concrete offer is "happy to provide product
   feedback," no budget or pilot. **None of the three pillars has any willingness-to-pay
   evidence** — pain and process evidence should not be read as purchase-intent evidence, and the
   strongest-evidenced pillar (infra, §0.1) is not thereby the closest to a sale. Nothing in this
   document should be read by the founders as "and therefore infra will sell first."
4. **Evidence concentration.** The load-bearing quotes across all three pillars come from roughly
   5–6 people out of 40 calls (Mike Hiltz, Asaf/a16z, Asaf/IR, Israel Bryski, Andrew
   Dutton/Harris Schwartz for read-only, Matturro for the hours-back framing) — see `ledger.md`
   C9's open question about whether Mike specifically is typical. See §2's evidence-honesty note.

### 0.4 Scope & non-goals

These mocks are decision-support artifacts for an internal wedge decision, not a product. Explicitly
out of scope for all three dashboards:

- **No real backend.** All data is static/mock, generated client-side or hardcoded; there is no
  database, API, or persistence layer behind any screen.
- **No real authentication or authorization.** There is no login, no real user identity, and no
  real RBAC enforcement. (A *simulated* role/approver indicator is in scope and required — see
  each pillar's §4 and §6 acceptance criteria — but it must not be presented as a working
  permission system.)
- **No real customer data, ever.** Every name, company, credential, CVE, dollar figure, and count
  on screen is illustrative demo data (per the framing note at the top of this document) or
  UI-safe anonymized copy from §7 of each pillar. Nothing traceable to a real transcript speaker
  or company appears verbatim.
- **No real ML/AI confidence scoring.** Confidence values, "behavioral baseline" assessments, and
  regression-test results are scripted/mocked, not the output of any model or live test run. The
  mock may *simulate* what a confidence explanation would look like (see each pillar's §6
  acceptance criteria for required per-node reasoning text) without claiming a working scoring
  system exists.
- **No live third-party integrations.** No real AWS, GitHub, Secrets Manager, CI/CD, or SIEM
  connection. Any "connect your AWS account"-style affordance is decorative, not functional.
- **No production write actions.** Every "revoke," "push," or "merge" button in every dashboard
  is a simulated action against mock data; nothing it does is reversible or irreversible in any
  real system, because nothing real is touched.
- **Not a wedge decision by itself.** These mocks inform the founders' judgment; they are not
  designed to be shown to a real prospect as a product demo, and they should not be treated as
  evidence of product-market fit independent of the underlying transcripts.

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

**Thin-evidence strategy (required, not optional):** identity gets the same "this is early"
treatment as code (§3, Evidence honesty check) — not as a disclaimer buried in this section, but
as an on-screen device. **What's allowed on screen:** the mock may claim "reversible hygiene
automation" on dormant/retired/zero-write-scope credentials only — this is the one category any
interviewee (Andrew) actually described a vendor being trusted to touch. **What's not allowed on
screen:** the mock must never suggest end-to-end autonomous revocation of active,
production-write-scope credentials, and must never suggest the cross-console reachability graph
(§3, §6) is computed from a live, working data pipeline — see §0.2's mock-building rule. The
credibility mechanism for the thinner claims (the recursive graph, the containment console) is
**visible attribution to Asaf's incident-response casework**, not a generic security-vendor
claim: every screen depicting the recursive graph or the containment console must carry a
persistent, non-collapsed label such as "modeled on incident-response casework across many
environments — not yet a Skylayer-observed live capability" (see §6 acceptance criteria for exact
placement). This is the identity equivalent of code pillar's Cognition-analogy citation — the
adjacent-evidence source has to be visible on the screen itself, not buried in this PRD.

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

**Feasibility note (see §0.2):** a live version of this screen would require standing
cross-account IAM/audit-log read access, Secrets Manager list/read permissions, and a GitHub App
with org-wide secret-scanning scope — access nobody in the evidence describes granting a vendor
today. The mock must stage this as the intended mechanism, not a working capability.

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
- **Teams that had to sign off on last month's revocations, median:** `3.2` — identity's
  differentiating KPI, not a generic hours-saved number: it dramatizes Asaf's cross-team
  coordination point directly ("before every revocation you have to coordinate and understand
  the business impact" across AWS, source control, and DB-admin teams), which is identity's
  actual economic story per §1.1, not a speed claim.
- **Stale/dormant identities auto-flagged this week:** `58`

*(Note: the previous KPI list included "cross-team coordination time avoided this month: 31 hrs,"
a restatement of the Matturro hours-saved framing used verbatim in the other two pillars. It is
replaced above with the sign-off-count KPI so identity's header reads as identity's own story, not
infra's or code's with a different noun — see §0's cross-pillar KPI-differentiation rule below.)*

### 6. "Wow" moments

Each moment below has 3–5 acceptance criteria. A moment is **done** only when every bullet under
it is checkably true in the built dashboard; missing any bullet is a fail, not a stylistic
choice. (This is what the developer must build — walk the finished dashboard against this list
before calling the pillar done, per the Appendix's build-verification rule.)

1. **The recursive blast-radius animation.** Drop in one leaked access key and watch the graph
   expand hop by hop exactly the way Asaf described it live — AWS → Secrets Manager → GitHub →
   more secrets — with a running "assets reachable" counter. This is the single most concrete,
   filmable incident-response story in the whole evidence base, staged as a screen.
   - **Acceptance criteria:**
     - The graph literally contains, as named/labeled nodes, at least the hop sequence: AWS
       account → Secrets Manager → GitHub. The strings "Secrets Manager" and "GitHub" must appear
       on screen (label text, not just a generic "service" node) — their absence is a fail.
     - Clicking/triggering the starting credential expands the graph hop-by-hop with a visible
       animation step per hop (not an instant full-graph render).
     - A numeric "assets reachable" counter is visible and increments live as each hop's nodes
       are added, ending on a final total that matches the node count on screen.
     - A persistent, non-collapsed caption near the graph reads (or closely paraphrases): "modeled
       on incident-response casework across many environments — not yet a Skylayer-observed live
       capability" (per the thin-evidence strategy above).
2. **The 30-accounts/100-keys containment console.** A single view that lists every AWS account
   and access key touched by one incident, grouped by which team owns each one, with a "coordinate
   revocation" button that pings each owner instead of an incident commander doing it by hand.
   This directly answers Asaf's "it's very hard to figure out on the fly."
   - **Acceptance criteria:**
     - A dedicated view/panel exists showing a multi-account, multi-key incident scenario; the
       screen or its data must reference the 30-accounts/100-keys scale from Asaf's account
       (exact numbers or a clearly labeled illustrative equivalent of that order of magnitude —
       not a single-credential example).
     - Rows are grouped by owning team (at minimum: AWS/platform, source control, DB admin), with
       the team name visible per row or per group header.
     - A "coordinate revocation" (or equivalently named) button is present and, when activated,
       visibly changes state (e.g., shows "pinged: 3 teams" or a per-team pending/acknowledged
       status) rather than doing nothing observable.
3. **The ghost-account panel.** A quiet list titled "retired — but still active," pulled straight
   from Leda Muller's fear, with a one-click "deactivate for real" action — the kind of screen that
   makes a CISO wince because they already know the answer.
   - **Acceptance criteria:**
     - A panel or section titled "retired — but still active" (or an exact paraphrase) exists and
       lists at least 3 distinct identity/account rows.
     - Each row shows a status contradiction on its face (e.g., "status: retired" next to "last
       active: 2 days ago") — the wince only works if the retired/active contradiction is visible
       without a click.
     - A one-click "deactivate for real" (or equivalently named) action exists per row and, when
       clicked, visibly moves the row out of the ghost list (e.g., to a "resolved" state).
4. **The "nothing here can break production" banner.** On the auto-approved lane specifically,
   because reversibility is the entire reason this pillar's evidence exists at all (Andrew's design
   partnership only worked because hygiene actions were undoable).
   - **Acceptance criteria:**
     - A visible banner/badge on the auto-approved lane specifically (not the review or blocked
       lanes) states, in plain language, that these actions are reversible/undoable.
     - The banner is present on every item in that lane, not a one-time dismissible tooltip.
     - Every item in the auto-approved lane is, per §1.4's scope rule, actually a
       dormant/retired/zero-write-scope credential — an item with production write-scope must
       never appear in this lane, or the banner's claim is false on its face.

**Build status as of this revision:** the currently shipped `identity/index.html` does not
implement wow moments 1–3 above (no "Secrets Manager"/"GitHub" strings, no 30-accounts/100-keys
console, no ghost-account panel) and ships a generic single-credential gate instead. This is a
**required fix**, not an optional enhancement — a fixer agent working on this file must add all
three scenes before this pillar can be considered built to spec.

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

**Open question this confidence rests on (`ledger.md` C9):** this pillar's entire
"strongest-cluster" claim leans on Mike Hiltz more than any other single source in the corpus, and
`ledger.md` C9 flags, in Mike's own words, reasons he may not be typical: he manages an
FDA-regulated medical device ("anytime we make a change like this... it has to go back to the
FDA" — a *harder* constraint than most orgs) but also describes himself as "fortunate" to run a
research environment with no SLA pressure on his downstream ("I don't have SLAs with my
downstream" — an *easier* constraint than most orgs). The one other regulated-pharma CISO in the
corpus (Bryan Brown, BioChrist) never volunteered regulatory change-control friction at all in 31
minutes. Whether Mike is typical is unresolved — this pillar's mock should be built and presented
with that caveat live, not as settled fact.

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

**Feasibility note (see §0.2):** this pillar has the strongest real-world analog (Mike's org
already produces change-management tickets and staging regression results by hand), but a live
version still requires CI/staging integration deep enough to run and score regression suites
automatically against production-bound services — a capability nobody in the evidence has handed
a vendor yet.

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
- **Change-management tickets closed without escalation:** `212 / 218` — infra's differentiating
  KPI: it dramatizes the regulatory/change-control friction that is this pillar's actual economic
  story (Mike's FDA-gated approvals, Israel Bryski's "CIO will need to be involved" threshold),
  not a generic speed or hours claim — a CISO reading this header should see "friction reduced,"
  not "time saved."
- **Risk bought down per dollar spent:** `$10 : $1` — Matturro's own framing for what a board wants
  to hear: "I'm spending $100,000 a year with you to buy down a million dollars of risk. That's a
  10-to-1 ratio."
- **Patch backlog burn-down:** `1,204 → 340 this quarter` — a direct answer to Andrew Dutton's
  complaint that telling a plant a bare count ("you've got 15,000 vulnerabilities, you better fix
  your stuff now... that means nothing") is useless without a trend and a "why it matters"
  (`2026-09-09_security-leadership-discovery_andrew-dutton.txt`).
- **MTTR (mean time to remediate, critical/high):** `4.2 days` — the metric Mike frames as having
  been cut roughly in half already by faster exploitation timelines, though he never gave us his
  own number; shown here only as demo texture.

*(Note: "Engineer-hours recovered this week: 26 hrs" is removed from this header — it was the same
Matturro hours-saved framing restated with a different noun in all three pillars. The
change-management-tickets KPI above replaces it as infra's own differentiator; see §0's
cross-pillar KPI-differentiation rule.)*

### 6. "Wow" moments

Each moment below has acceptance criteria; a moment is done only when every bullet is checkably
true in the built dashboard (see identity §6 for the format and the Appendix for the
build-verification rule).

1. **The log4j "present but not running" screen.** A critical CVE that the dashboard downgrades in
   priority because the vulnerable code path is unreachable in this deployment — directly
   dramatizing Mike's real example and teaching the CISO viewer the dashboard reasons about actual
   risk, not just severity labels.
   - **Acceptance criteria:**
     - At least one finding is explicitly log4j (or an equivalent named CVE) marked
       critical/high severity by CVSS-style label, but shown with a *lower* priority/gate state
       than a lower-severity finding elsewhere on the same screen.
     - The finding's detail view states in plain text why: the vulnerable code path/file is
       present but not running/not reachable in this deployment.
     - The screen visibly distinguishes "severity" from "blast radius/priority" as two separate,
       independently labeled values — not one merged score.
2. **The confidence-gated push button.** A patch card showing "regression tests: 47/47 passed,
   0 downstream services flagged, no human intervention required — push?" next to a second card
   for an FDA-regulated system that's hard-blocked with "requires regulatory sign-off" — showing
   both ends of Mike's own spectrum on one screen.
   - **Acceptance criteria:**
     - One visible card shows a specific regression-test pass count (e.g., "47/47") and a
       downstream-services-flagged count (e.g., "0"), with its primary action available
       (unblocked).
     - A second visible card on the same screen is hard-blocked with a "requires regulatory
       sign-off" (or exact paraphrase) label, and its primary action is disabled/unclickable —
       not merely a lower confidence number on an otherwise-live button.
3. **The blast-radius graph for one patch.** Click a CVE, see every downstream service and the team
   that owns it, instead of a bare CVSS score — literally Mike's "if you can see that blast radius,
   now you know the overall impact," rendered.
   - **Acceptance criteria:**
     - Clicking any finding opens a graph/list of downstream services, each labeled with the team
       that owns it (not just a service name with no owner).
     - The CVSS/severity score is visible but is not the only number shown — the number of
       downstream services and owning teams must be visible on the same view.
4. **The backlog-with-a-story view.** Instead of "15,000 vulnerabilities," a burn-down chart with
   the top-line why-it-matters sentence Andrew Dutton asked for, per item.
   - **Acceptance criteria:**
     - A trend/burn-down chart (not a single static count) is visible, showing at least two time
       points (e.g., start-of-quarter vs. now).
     - At least one item in the backlog carries a one-line "why it matters" sentence distinct from
       its CVE ID/severity label.
5. **The one-click rollback receipt** after a bad patch — proof the system reverted itself before
   anyone had to file an incident.
   - **Acceptance criteria:**
     - Triggering a rollback (simulated) produces a visible, timestamped "receipt" — a record of
       what was reverted and when — distinct from the action button itself.
     - The receipt states explicitly that the revert happened before an incident was filed/escalated.

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

**Thin-evidence strategy (required, not optional):** the credibility mechanism for this pillar is
the Cognition analogy, and it must be **on-screen and visible, not buried in this PRD**. Every
screen depicting the generated-test proof mechanism (§3, §6 moment 1) must carry a persistent,
non-collapsed caption naming the source explicitly, e.g.: "this workflow is modeled on Cognition's
test-generation approach for coding agents, adapted here for security — not yet a
security-buyer-validated process." **What's allowed on screen:** the mock may claim "prove no
behavior change before merging" for dependency-version-bump-class fixes only. **What's not
allowed on screen:** the mock must never suggest a security buyer has already validated this
workflow, and must never suggest the generated-test suite is running against a real, live
codebase rather than mock data (see §0.2). See wow moment 4 below for the internal-facing device
that operationalizes this.

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

**Feasibility note (see §0.2):** a live version requires source-control write access plus a
test-runner/CI integration capable of generating and executing a regression suite against
arbitrary repos — a larger lift than infra's, and with less evidence anyone wants it from a
security vendor specifically rather than a coding-agent company.

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
- **% of fixes where the generated test suite caught a behavior change before merge:** `7%` —
  code's differentiating KPI: it dramatizes the Cognition-style proof mechanism that is this
  pillar's actual pitch (§3), not a generic hours-saved number — it tells a viewer "the tests are
  doing real work, not rubber-stamping," which is precisely the claim §3's evidence rests on.

*(Note: "Engineer review hours saved this week: 14 hrs" is removed — it was the same
Matturro-style hours-back framing restated with a different noun in all three pillars. The
test-suite-catch-rate KPI above replaces it as code's own differentiator; see §0's cross-pillar
KPI-differentiation rule.)*

### 6. "Wow" moments

Each moment below has acceptance criteria; a moment is done only when every bullet is checkably
true in the built dashboard (see identity §6 for the format and the Appendix for the
build-verification rule).

1. **The generated-test proof screen.** Before proposing a dependency bump, show the system writing
   a regression-test suite against *current* behavior first, then running it against the proposed
   fix — dramatizing Asaf's Cognition-style pitch ("prove that after upgrading, nothing would
   happen") as a concrete, watchable two-step process rather than an abstract promise.
   - **Acceptance criteria:**
     - The screen shows two distinct, sequential steps: (1) tests generated/written against
       current behavior, (2) those same tests run against the proposed fix — both visible as
       separate stages, not a single "passed" badge.
     - Named test identifiers (not just a pass count) are visible for at least one finding.
     - A persistent caption names Cognition explicitly as the source of this approach (per the
       thin-evidence strategy above) — its absence is a fail.
2. **The PR-as-remediation screen.** A vulnerability finding that resolves not into a ticket but
   into an actual, reviewable pull request with a diff, a test result, and a single approve button
   — Chris's literal ask, staged.
   - **Acceptance criteria:**
     - At least one finding's detail view shows a diff (added/removed lines), a test result
       summary, and a single primary approve/merge action — all three present together, not
       split across unconnected screens.
3. **The "present but not reachable" code-path view**, the code-level sibling of the infra pillar's
   log4j screen — showing a vulnerable function that exists in the codebase but is never called in
   the deployed build, so it's correctly deprioritized instead of triggering a false-urgency ticket.
   - **Acceptance criteria:**
     - At least one finding is explicitly marked as present-in-code-but-not-called/not-reachable
       in the deployed build, with that reachability state shown as a distinct label from
       severity (mirroring infra §6 moment 1's acceptance criteria).
     - That finding's gate/priority state is visibly lower than a comparable-severity, reachable
       finding elsewhere on the same screen.
4. **A frank "this is early" empty state** (internal-team-facing, not for the CISO viewer): a note
   that this pillar's workflow is inferred from one dependency-patching example and one investor's
   analogy to a coding-agent company, not from a security buyer's own described process — so nobody
   mistakes the mock's confidence for validated evidence.
   - **Acceptance criteria (this is the single most important requirement in this pillar's spec —
     it must not be dropped again):**
     - A visible, non-collapsed panel or banner exists somewhere on the pillar's main screen
       (not hidden behind a click, not a `<details>` toggle) stating in plain language that this
       pillar's workflow is inferred from one dependency-patching example and an investor's
       analogy to a non-security coding-agent company, not from a security buyer's own described
       end-to-end process.
     - The panel is legible without requiring the viewer to already know this PRD's evidence
       grading — it must read as self-contained, e.g.: "Early: this workflow is our best guess,
       built from one practitioner's dependency-patching example and an investor's analogy to a
       coding-agent company — no security buyer has described this exact process to us yet."
     - This state must render by default on page load, not require a developer-only flag or
       hidden route to see.

**Build status as of this revision:** the currently shipped `code-patching/index.html` does not
implement wow moment 4 above — no "this is early" empty-state device exists anywhere in the file.
This is a **required fix**: a fixer agent must add this panel, rendered by default, before this
pillar can be considered built to spec. This is arguably the single most important honesty device
in the whole document (it is what stops a thin pillar from silently overclaiming) and it must not
be dropped a second time.

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
  carry into a real PRD without saying so, which is why this document says so twice — and each
  pillar's "Thin-evidence strategy" note now gives the operational rule (what's allowed on screen,
  what isn't), not just this warning.
- **Cross-pillar KPI-differentiation rule.** No two pillars' KPI headers may share a
  generic "hours/time saved" metric restated with a different noun and number. Each pillar's
  header must include at least one KPI that only makes sense for that pillar's own
  owner-fragmentation/economics story (identity: cross-team sign-off count; infra:
  change-management tickets closed without escalation; code: generated-test catch rate) — see
  each pillar's §5 for the specific replacement and rationale.
- **Build-verification rule (do this before calling any pillar done).** Once a pillar's dashboard
  is built or revised, walk the finished file against that pillar's §6 acceptance criteria,
  moment by moment. Every bullet must be checkably true in the running dashboard. If a moment
  cannot be verified, either (a) fix the build so it can, or (b) if a deliberate scope cut is
  being made, add an explicit "spec deviation" note to this PRD or the README stating exactly what
  was cut and why — silent deviation (shipping a materially different screen than the spec without
  saying so anywhere) is not an acceptable outcome regardless of how polished the substitute looks.
  This is what should have caught it the first time: identity shipped without wow moments 1–3 and
  code shipped without wow moment 4, and nobody checked the build against this section until an
  external review did.
