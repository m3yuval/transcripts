# Skylayer — thesis

Last updated: 2026-09-25

---

## The claim

Organizations can't remediate fast enough. Not because they don't know what to
fix, and not because the fix itself is hard — but because **nobody can prove a
change is safe**. The fix might break production, and someone owns that blast
radius. So the change waits.

We want to produce that proof, and then act on it.

## Why now

The window between disclosure and exploitation has collapsed. The time it takes
to make a change safely has not moved.

- Mandiant M-Trends 2026: average time-to-exploit is **−7 days** — exploitation
  before a patch exists. It was −1 day in 2024.
- Verizon DBIR 2025: median time to mass exploitation for edge-device KEVs is
  **0 days**. Only 54% of those are ever remediated; about a third never are.
- VulnCheck: 32.1% of KEVs in 1H 2025 had exploitation evidence on or before
  disclosure day, up from 23.6% in 2024.

AI is one driver of this curve. It is not the claim.

## What we believe

1. **Detection is covered. Action is not.** — "solutions that identify
   vulnerabilities, but none that actually take action in most cases"
   (Mike Hiltz, CISO, nference)
2. **The blocker is impact uncertainty** — not speed, not prioritization, not
   the absence of tooling.
3. **Proof is the moat; the action is the product.** An impact assessment that
   nobody acts on is just a smarter findings list.
4. **Trust is earned with reversibility.** Start where being wrong is cheap.

## The wedge — OPEN

Same mechanism either way: model the dependencies, predict the blast radius,
gate by confidence, revert when wrong. The first wedge is not decided.

**Option A — network / firewall config.** Our founder-market fit is
unarguable. Incumbents (Tufin, AlgoSec, FireMon) compute risk from static
config models, not observed traffic. Forward Networks and Batfish prove what a
config *allows*, never what the traffic *means*. Nobody joins those two.
Skybox's collapse (Feb 2025) left a live buying window.
*Weakened 2026-09-25:* Ariel Litvin, who researched the space to found in it,
puts the whole NSPM market at **$350M ARR**. He also puts network outside
security's control in **~85%** of organizations. Asaf (IR) has never seen an
agentic attack on an on-prem network — all his cases are cloud and identity.
Other names in this space to check: Nimble Security (Ross), styc.io, Astrix.

**Option B — OS / package / container patching.** Where our strongest evidence
actually points (Mike, Chris, Asaf a16z). Closer to Cognition and to Reclaim
Security.

**Decision rule:** run the next three calls on Option B's framing. Three more
Mikes settles it. If Mike turns out to be unusual, Option A is better ground.
*Status 2026-09-25: NOT MET.* The three calls added on 09-25 (Ariel, Asaf IR,
Jason Lawrence) are backfill from 09-01 to 09-07 — all before Mike, none run on
Option B's framing. The rule still needs three forward-looking calls.

## Proven

- **Fear of breaking production is the real blocker.** Eleven people,
  unprompted, unconnected: Mike Hiltz (nference), Chris, Heather (Nestlé
  Purina), Israel Bryski, ABasu, Eli Edelkind (Cava), Yoni (FICO), Andrew
  (ex-Nestlé), Asaf (a16z), Ariel Litvin (ex-First Quality, 11 yrs CISO),
  Asaf (IR manager — speaks from casework across many customer environments,
  not from owning one).
- **The detection-to-action gap is real, and buying is expected over
  building.** Mike: "this is a problem that we expect our vendors to solve."

## Unproven

- **The proof mechanism.** We don't know what evidence we can actually produce,
  or how. Everything else is downstream of this.
- **Whether the action can be autonomous at all in a large enterprise.** Ariel
  Litvin, 11 years CISO at a Fortune-500-scale manufacturer, unprompted: "in
  production organizations it's very very very very different — you can't make
  mistakes… saying I can do auto-remediation and handle things fast, configure
  the network or segment in real time — it's nice, it doesn't work. It simply
  doesn't work at the Fortune 500." He accepts the premise and rejects the
  action.
- **Any number.** Not one interviewee gave an MTTR, backlog size, SLA breach
  rate or finding count from their own environment.
- **Willingness to pay.** No budget line, no approval chain, no design partner.
- **Whether Mike is typical.** FDA-regulated medical device, unusually heavy
  testing burden.

## Not claiming

- "AI changed the economics of attacks" — six interviewees pushed back on this
  unprompted.
- "CISOs get a list of 200 patches after a pen test" — this sentence is ours,
  not a customer's. No source in 42 transcripts.
- "Most CISOs said their current stack is enough for detection."
- "It came up in every conversation."
- Headcount reduction ("four engineers instead of eight") — Shawn Anderson:
  "That is a non-starter."

## Open questions

1. Which layer do we start with?
2. What is the proof mechanism, concretely? How would it know about a DR
   failover that ran twice in eighteen months?
3. Who is the buyer — the CISO who wants exposure closed, or the platform owner
   who gets paged when it breaks? Ariel: network sits outside security in ~85%
   of orgs, and when he pushed firewalls back to IT they reverted to "routing
   and nonsense, not security capabilities." He could only hold it because he
   reported to the Chairman, not the CIO.
4. What is our answer to "it's not novel, I see this exact proposition
   everywhere" (Jerry Carlson) and "there's no moat, I'll build my own tool"
   (Andrew)? Ariel adds: almost every company with a supposed moat, Koi
   included, got copycats fast — Consool sold to Palo for $500M doing nothing
   new, on timing and GTM alone.
5. First design partner — Mike Hiltz is the best candidate in 42 calls. What do
   we need to build before he says yes?
6. **NEW, undecided — is there a third wedge?** Asaf (IR) describes the same
   blocker inside incident containment: "before every revocation you have to
   coordinate and understand the business impact," across 30 AWS accounts and
   100 access keys, where "it's not the same security product, not the same
   team, and containment actions have consequences." Same mechanism, different
   surface. Not added as an option until we decide.
7. **Name check.** Two different Asafs are now in the evidence — the a16z
   investor and the incident responder. The a16z transcript renders him as
   "Asaf Ezra"; earlier notes say "Asaf Perlman." Confirm before using either
   name outside.
