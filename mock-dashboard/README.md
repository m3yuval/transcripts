# Mock dashboard — three wedge candidates, one instrument

Decision-support mockups for the founders' open wedge question in `thesis.md`
("Which layer do we start with?"). Not a shipped product, not real customer
data — a way to *feel* what Identity, Infrastructure Patching, and Code
Patching would each look and act like before picking one.

Built by a small agent team, independently, against two shared briefs:

| File | What it is | Written by |
|---|---|---|
| `PRD.md` | Transcript-grounded product brief for all three pillars: persona, core objects, impact-assessment view, remediation view, KPIs, "wow" moments, UI-safe anonymized copy. Every claim is cited to a transcript, honestly graded by evidence strength per pillar. | PM agent |
| `DESIGN.md` | The **Isoline** visual system all three dashboards share: blast radius as a seismic/isobar survey field instead of a card grid, confidence as line quality, reversibility as a tether, one instrument reskinned per pillar. Includes the full color-token, typography, layout, and motion spec. | Design agent |
| `identity/index.html` | Identity pillar — the *Downstream Dark Map*. Epicenter: a credential/session queued for revocation. Rings: direct tokens → automations/service accounts → dependent sessions, dimming toward dark as they enter the blast radius. | Dev agent |
| `infra-patching/index.html` | Infrastructure patching pillar — the *Downstream Break Map*. Epicenter: a host/container queued for patch/reboot. Rings: services on the host → their callers → SLA-bound endpoints. | Dev agent |
| `code-patching/index.html` | Code/app patching pillar — the *Call Path / Regression Proof Map*. Epicenter: a dependency bump or merge. Rings: direct callers → transitive callers → public entry points, with a regression-test proof strip that can veto the gate on a single untested reached path. | Dev agent |

## Why it looks like this

The founder's brief was explicit: no generic AI-dashboard look (purple
gradients, glassmorphism, shadcn-style card grids). Skylayer's own customers
already describe the product spatially — "blast radius" (Mike Hiltz),
"one click undo or rollback" (Israel Bryski), "read-only... let's see how
that goes" (Harris Schwartz) — so the design system takes that literally.
Every screen's dominant object is a survey-instrument field: an off-center
epicenter surrounded by concentric rings that fall off by dependency
hop-distance, the way a seismic-intensity map or a weather isobar chart
falls off from its center. Confidence is drawn as line quality (crisp vs.
soft/blurred rings), not a percentage badge. Reversibility is a permanent
tether back to a last-known-good state that visibly reels the state back in
on revert. Full rationale and avoid-list in `DESIGN.md`.

## Viewing them

Each `index.html` is fully self-contained (no build step, no shared
imports across folders — open any one on its own) and was also published
as a Claude Artifact for a live interactive preview:

- **Identity**: https://claude.ai/artifact/UmwG5EGSShje91CQBurZxj
- **Infrastructure patching**: https://claude.ai/artifact/HN7o2ZWKvAgxL4X4dqBZ3b
- **Code patching**: https://claude.ai/artifact/BWbCjyHZDj1eRyvoGHQm1K

## Evidence honesty (from `PRD.md`)

The three pillars are **not** equally evidenced in the 44 transcripts:

- **Infrastructure patching** is the strongest cluster by far — Mike Hiltz
  (CIO+CISO, nference) walks through his real end-to-end patch pipeline
  unprompted, including the exact gate condition ("I have a consensus, I can
  do this without breaking anything... go ahead and push it").
- **Identity** is real but nascent — vivid mechanics from an incident
  responder's cross-client casework (30 AWS accounts, ~100 access keys,
  four different owning teams per revocation), but no CISO owns an
  identity-remediation process end to end the way Mike owns his patch
  pipeline.
- **Code/app patching** is the thinnest — one workflow sentence from Chris
  (Wistia) plus a structural analogy an investor draws to Cognition's
  test-then-prove method, not a security buyer describing their own pain.

Don't read the polish of any one mockup as a signal of validation strength —
that's tracked in `PRD.md`, not in how finished the pixels look.
