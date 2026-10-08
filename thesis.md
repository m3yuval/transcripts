# Skylayer — thesis

Last updated: 2026-10-08 (rewritten from the "Network Risk Assessment" slides)

---

## The claim

**Network Risk Assessment.** AI-speed threats. Fragmented networks. Blind
security decisions.

Enterprise networks span cloud, on-prem, data centers, firewalls and endpoints,
with limited understanding of how everything connects. Security teams struggle
to reduce exposure and contain threats **without risking business disruption**.

We turn network complexity into actionable security control: a unified
intelligence and enforcement layer across the entire hybrid network.

## What we believe

1. **Fragmented visibility.** There is no unified view of connectivity,
   configurations and critical assets across cloud, on-prem, data centers,
   firewalls and endpoints.
2. **Unknown impact.** Security teams cannot confidently assess the risk of
   network changes.
3. **AI-speed threats.** Fast-moving attacks demand faster segmentation and
   containment decisions.
4. **The cost is disruption.** Because of 1–3, security teams cannot reduce
   exposure or contain threats without risking business disruption.

## The product

A **Unified Network Security Context** built from cloud, on-prem, firewalls,
data centers and endpoints: connectivity, configuration, exposure and business
criticality. On top of it, three jobs:

- **Understand** — map connectivity and identify hidden exposure.
- **Reduce risk** — recommend segmentation and security policies.
- **Enforce** — assess changes and block critical policy violations.

Tagline: *Reduce exposure. Prevent risky changes. Contain threats faster.*

## The wedge — DECIDED: network

The 2026-09-25 thesis left the wedge open between **A — network / firewall
config** and **B — OS / package / container patching**. This version commits
to A: the network layer, across the hybrid estate.

## What changed from the 2026-09-25 thesis

So the debrief can map the ledger (claims C1–C10) onto this version:

| 2026-09-25 | 2026-10-08 |
|---|---|
| #1 Detection is covered; action is not | Dropped. Visibility is now part of the problem (#1). |
| #2 The blocker is impact uncertainty, not speed / prioritization / tooling | Kept, narrowed to network changes (#2). "Not prioritization" is no longer stated. |
| #3 Proof is the moat; the action is the product | Not stated. "Enforce" is the action; "assess changes" is the proof. |
| #4 Trust is earned with reversibility | Not stated. |
| Wedge open (A network / B patching) | A chosen. B dropped. |
| "AI changed the economics of attacks" under *Not claiming* | Now claimed as #3 (AI-speed threats). |
| Action = security's own remediation changes | Also guarding everyone else's changes ("block critical policy violations"). |

## Evidence status (from ledger.md, calls through 2026-10-05)

For this version:
- **#2 on others' changes:** Fernando Medrano (Fastly, 09-30), unprompted: "it's
  very hard for security teams to know whether or not a particular change" …
  "is introducing risk or not."
- **Network changes are feared:** Rajiv (insurance broker CIO, 09-28, led) and
  Eli Edelkind (a Palo Alto threat-intel update that took Dynamics down).

Against the network wedge, unprompted, from the C6 CONTRA list:
- Andrew (ex-Nestlé)
- Mandy Andres (Elastic)
- Ray Lewis (Pekin)
- Ariel Litvin: network sits outside security in ~85% of orgs, and NSPM is ~$350M ARR
- Davon's call (10-05): firewalls "a lot easier to solve for"
- The 09-29 interviewee: "legacy networks, not AWS or public clouds"
- Fernando: "applies maybe a little bit more to … legacy companies that
  actually operate on-prem"

Against #3 (AI speed): six interviewees pushed back on the AI-economics framing
before this rewrite.

## Not claiming

- "CISOs get a list of 200 patches after a pen test." This sentence is ours,
  not a customer's.
- "It came up in every conversation."
- Headcount reduction ("four engineers instead of eight"). Shawn Anderson:
  "That is a non-starter."

## Open questions

1. **Who is the buyer?** Network sits outside security in ~85% of orgs
   (Ariel). Rajiv: "The infrastructure team owns the network."
2. **Cloud or on-prem?** Fernando, Davon and the 09-29 interviewee all say cloud
   networks are already controlled. Is the ICP hybrid or legacy on-prem enterprises?
3. **What is "assess changes", concretely?** Is it a pre-change gate on security's
   own changes, or a guardrail on engineering's changes (Fernando's ask)?
4. **What is new against incumbents and newcomers?** Tufin, AlgoSec, FireMon,
   Forward Networks, Batfish; named on calls: Astellia, Zafran, Nimble
   Security, styc.io.
5. **First design partner.** No budget line, approval chain or design partner
   yet (C8).
6. **Name check.** Two different Asafs are in the evidence: the a16z investor
   and the incident responder.
