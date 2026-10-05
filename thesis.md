# Skylayer — thesis

Last updated: 2026-10-05

---

## The claim

Every security finding can be fixed in more than one way. A vulnerable Redis
can be upgraded, made unreachable on the network, or locked down through
identity. Exposed data can be closed off at the data layer or hidden behind a
firewall rule. But **each security tool recommends only the fix in its own
domain**: the vulnerability scanner says upgrade, the DSPM says revoke access,
the cloud-posture tool says tighten the security group.

Nobody compares the options. And the context needed to compare them, which is
what depends on the asset, who uses it, and what the business runs on it, is
spread across tools, domains and teams. So teams either take the tool's default
fix and risk breaking production, or they wait.

**We assess the impact of every possible fix for a finding and recommend the
one that closes the risk fastest, at the lowest cost, without hurting
production. Then we execute it and verify.**

Executing isn't the hard part. Knowing which fix is safe is.

## Why now

- **Attackers move faster than changes do.** CrowdStrike 2026 Global Threat
  Report: average breakout time (initial access to lateral movement) is
  **29 minutes**, the fastest **27 seconds**. Mandiant M-Trends 2026: average
  time-to-exploit is **−7 days**. A fix that waits for the next change window is
  too late; a fast, low-impact alternative that is available today is worth more
  than the perfect fix next week.
- **The number of tools, each with its own recommendation, keeps growing.**
  "I have too many tools" (Nelson). Every new tool adds findings and its own
  domain-specific fix, and none of them see the others.
- **The data to assess impact now exists.** Flow logs, identity and access logs,
  and data-access logs show what actually uses an asset, so impact can be
  predicted from observed usage instead of guessed from configuration.

AI is one driver of attack speed. It is not the claim.

## What we believe

1. **Detection is covered. Choosing the right fix is not.** — "solutions that
   identify vulnerabilities, but none that actually take action in most cases"
   (Mike Hiltz, CISO, nference)
2. **The default fix is often not the best one.** The tool's recommendation
   optimizes for its own domain, not for the least disruption. The Redis
   advisory's own workaround (disable Lua) would break any service that relies
   on Lua scripts.
3. **Impact assessment is the product.** For each option: what it breaks and for
   whom, how long it takes and who must approve it, how much risk it actually
   closes, and whether it can be undone.
4. **Friction is organizational as much as technical.** A one-line firewall rule
   can be the hardest change in the company, because the network team owns it
   and has been burned before (Rajiv). The model has to know owners, approvals
   and change windows, not just configuration.
5. **Trust is earned with reversibility.** Prefer fixes that can be rolled back
   instantly; start where being wrong is cheap.

## How it works

1. Ingest findings and the recommended fixes from the security tools already in
   place.
2. For each finding, enumerate the possible fixes across domains: patch or
   upgrade, network restriction, identity or ACL change, data-access change,
   configuration change.
3. For each fix, assess the impact from observed usage: which services, users and
   data flows depend on what the fix would change.
4. Rank the fixes by production impact, time to apply, effort and approvals,
   risk closed, and reversibility. Recommend a plan (often a fast mitigation now
   and the full fix in the next window).
5. Execute, verify, and roll back if verification fails.

## The wedge — OPEN

The mechanism is domain-agnostic; the first set of findings is not decided.
Candidates: findings where the default fix is painful (a hard upgrade, a risky
access revocation) and a lower-friction alternative exists in another domain.

## Competition

- **Zafran** already positions itself as reducing risk "without waiting on patch
  cycles", mapping vulnerabilities to existing controls (NGFW, WAF, EDR, CNAPP)
  and prescribing configuration changes. To check: whether they assess the
  production impact of each option, and whether they cover non-vulnerability
  findings (data, identity, posture).
- To research: Seemplicity, Nagomi, XM Cyber, and the exposure-management
  platforms (Tenable One and similar).
- "They do the attack path analysis, fix validation through vuln scanning,
  etc." (Javed Ikbal). Our answer has to be one sentence.

## Proven

- **Fear of breaking production is a real blocker.** Eleven people, unprompted,
  unconnected: Mike Hiltz (nference), Chris, Heather (Nestlé Purina), Israel
  Bryski, ABasu, Eli Edelkind (Cava), Yoni (FICO), Andrew (ex-Nestlé), Asaf
  (a16z), Ariel Litvin (ex-First Quality), Asaf (IR manager). Rajiv (sitting
  CIO) confirms it for network changes, led.
- **The detection-to-action gap is real, and buying is expected over
  building.** Mike: "this is a problem that we expect our vendors to solve."
- **The default fix often isn't possible.** Ariel: Patch Tuesday "doesn't
  happen"; SMBv1 and TLS 1.0 servers run in organizations for years. Yoni:
  virtual patching is already the community's workaround.

## Unproven

- **That teams compare fixes across domains at all.** No interviewee has yet
  described weighing several fixes from different domains for the same finding.
  This is the central new assumption.
- **The impact-assessment mechanism.** Whether observed usage predicts impact
  well enough to trust, and what it misses (rare jobs, failover paths, a DR test
  that ran twice in eighteen months).
- **That it is a separate product.** Javed: "Fix impact assessment: what will
  you do that my vuln scanner or patching tool can't do?" and "it's not a big
  enough gap for a separate product."
- **Whether the action can be autonomous in a large enterprise.** Ariel: auto
  remediation "simply doesn't work at the Fortune 500." Several CISOs: read-only
  first.
- **Who buys.** The CISO owns the finding; the platform, network or data team
  owns the change and often the budget (Rajiv: CISOs "don't know the budget" for
  network).
- **Any number.** No interviewee gave an MTTR, backlog size or breakage rate from
  their own environment.
- **Willingness to pay.** No budget line, no approval chain, no design partner.
  Javed: "not many CISOs have that kind of budget."

## Not claiming

- "AI changed the economics of attacks" — seven interviewees pushed back.
- "CISOs get a list of 200 patches after a pen test" — this sentence is ours,
  not a customer's.
- "Network ownership is unclear" — it isn't; the infrastructure team owns it
  (Rajiv).
- Headcount reduction ("four engineers instead of eight") — Shawn Anderson:
  "That is a non-starter."

## Open questions

1. How are we different from Zafran, in one sentence?
2. Which findings first: where is the gap between the default fix and the best
   fix largest and most frequent?
3. What data do we need from the customer to assess impact, and how fast can we
   get it?
4. Who signs: the CISO who owns the finding, or the team that owns the change?
5. Next-call question: "Tell me about the last finding you didn't fix the way the
   tool recommended. What did you do instead, and who had to approve it?"
6. First design partner: Mike Hiltz remains the best candidate. What do we need
   to show him?
7. **Name check.** Two different Asafs are in the evidence: the a16z investor and
   the incident responder. Confirm names before using them outside.
