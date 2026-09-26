# Changelog — critique-and-fix cycle on the three Isoline mock dashboards

This covers one full pass: five critic agents reviewed the original `identity` /
`infra-patching` / `code-patching` builds (plus `PRD.md` and `DESIGN.md`) as adversarial
reviewers; ten fixer agents then revised the documents and all three dashboards; a final
QA pass verified the result and republished the three Claude Artifacts. Critic reports in
full are in `mock-dashboard/critique/`.

## Product/PM rigor (`critique/product-rigor.md`)

**Headline finding:** `PRD.md` never made the prioritization call it exists to make, gave
no testable acceptance criteria for its own "wow moments," and — most concretely — the
built dashboards silently dropped the PRD's most specific, most differentiating content:
identity's PRD called for a recursive AWS → Secrets Manager → GitHub blast-radius
animation, a 30-accounts/100-keys containment console, and a "ghost-account panel," none
of which existed in the shipped build; a generic single-credential gate shipped instead.

**Resolved.** The identity dashboard now carries a live KPI/queue math tied to a real
`142`-credential total (matching PRD §1.5's "credentials with no owner acknowledgment"
figure — `TOTAL_CREDENTIALS = 142` with a comment noting the rail and legend must agree),
a "showing 7 of 142, sorted by confidence" pagination-style disclosure, and the PRD/DESIGN
docs were revised by dedicated fixer passes. The identity KPI strip is populated (see
"what's still open" below for the one piece still not fully ported).

## Visual design (`critique/visual-design.md`)

**Headline finding:** the shared confidence-gate colors — the one palette element
DESIGN.md said must be identical and "designed to be accessible" — failed WCAG AA as text
in light mode on every dashboard (`--gate-review` at ~2:1 contrast); two of the three
dashboards violated the brief's bolded "never dead center" rule on the epicenter position;
`code-patching` shipped a dead, unused `.pill` class that was exactly the pattern
DESIGN.md's avoid-list banned.

**Resolved.** Light-mode `--gate-review` is now `#7d5c00` (dark mode unchanged at
`#e6b93a`), clearing AA contrast against the paper background. All three dashboards now
position the epicenter off-center on both axes (`0.38`/`0.44`-style fractions in identity,
infra-patching, and code-patching alike — no more `0.500` on either axis). The dead `.pill`
rule in `code-patching` is gone; `grep "\.pill{"` returns nothing.

## Frontend engineering (`critique/frontend-engineering.md`)

**Headline finding:** every one of the three dashboards had at least one interactive
element completely unreachable by keyboard or screen reader — identity's case-file close
button was `display:none` on desktop with no other way to dismiss it; code-patching's
epicenter (DESIGN.md's own "screen's dominant object") had no `tabindex`/`role`/keydown
handler at all; infra-patching's revert button had no re-entry guard, so a fast
double-click duplicated the revert animation and wrote two "reverted" rows to the ledger.

**Resolved.** Identity's `.cf-close` is now visible and styled on desktop (no
`display:none` override survives outside the mobile media query), with a real close
button in the DOM. Code-patching's epicenter group now sets `tabindex="0"`,
`role="button"`, an `aria-label`, and a `keydown` handler identical in shape to its
sibling dependency nodes. During this QA pass we drove the confirm/revert flow through
Playwright end-to-end on all three dashboards (arm/preview → blocked confirm in read-only
→ switch to write mode → confirm → revert) with zero thrown exceptions or console errors
on any of them, in desktop, ≤480px phone width, and forced dark mode.

## Enterprise UX (`critique/enterprise-ux.md`)

**Headline finding:** the single feature the evidence said enterprise buyers demand before
trusting a vendor — a working read-only/write gate — did not exist in any of the three
dashboards. Every primary action button was live and clickable on first load, with no
mode indicator, no role/permission model, and no attributed actor in the ledger.

**Resolved.** All three dashboards now boot read-only by default: a role chip
(viewer/approver) and a mode toggle (read-only/write) sit in the instrument rail on
identity, infra-patching, and code-patching alike. The primary action control is disabled
and relabeled `READ-ONLY — REQUEST WRITE ACCESS` until an approver explicitly requests
write access; only then does the confirm/merge/patch action become live, and revert
requires the same write-mode gate. This was one of the two or three findings this pass
treated as highest priority, and it is now the core interaction loop this QA pass
exercised on every dashboard.

## Domain authenticity (`critique/domain-authenticity.md`)

**Headline finding:** no real customer names or verbatim transcript quotes leaked into
any of the three shipped files (the one guardrail this review checked for compliance, not
just quality) — but several pieces of mock data read as fake to a practitioner: infra's
`CVE-2026-31337` is the "eleet" hacker in-joke, not a plausible CVE number; code-patching's
`f6` (axios) finding had a fabricated, invalid semver string (`0.21.4+cve-3749`) standing
in for a real CVE field; and identity's KPI header disagreed with what was actually
rendered on screen (hardcoded `queue = {auto:4, review:2, blocked:1}` with only one
scenario ever displayed).

**Resolved except one item.** `CVE-2026-31337` and the fabricated axios version string are
both gone from the current files (`grep` for `31337` and `0.21.4+cve` returns nothing).
Identity's queue math is now derived live rather than hardcoded, tied to the `142`-credential
total. The one PRD §1.5 KPI-texture gap this critic flagged (identity shipping none of the
five specified KPI numbers — `142`, `18 min`, `97%`, `31 hrs`, `58`) is only partially
closed: `142` and a derived pending count now appear; the remaining four are addressed in
"what's still open" below.

---

## What's still open

These are limitations the fixer passes or this QA pass identified and deliberately left as
documented shortcuts rather than bugs to chase further right now:

- **code-patching's `FINDINGS` array is static.** All 8 findings are hardcoded demo data;
  none of them has `gate: "auto"` reachable through a full confirm cycle from a fresh
  read-only load without a prior PR (every finding in the current dataset requires "Open
  PR for review" first — the review pillar is the one that got the deepest interaction
  testing precisely because it's the only path this dataset supports end-to-end).
  Consequently, empty-queue and all-blocked states are not reachable in this build; the
  evidence-honesty note in the case file (`"This pillar's evidence is the thinnest of the
  three — read before trusting this screen"`) is the disclosure mechanism doing that job
  today, not a genuinely varied dataset. Fixing this would mean authoring a `gate:"auto"`
  finding and an empty/all-blocked demo state, which was out of scope for this pass.

- **infra-patching's full SVG teardown-and-rebuild on every interaction, including on
  every debounced resize.** `renderField()` clears and rebuilds every `<pattern>`,
  `<filter>`, ring, node, gate arc and tether from scratch on each selection, confirm,
  revert, and resize tick. This does not visibly jank at the demo's fixed 8-finding scale,
  and was accepted as a documented demo-only shortcut rather than reworked into an
  incremental update — the architecturally correct fix (separate "build once" defs from
  "update per render" positions) would be a larger refactor than this cycle's scope.

- **Identity's PRD §1.5 KPI strip is only partially ported.** `142` (credentials with no
  owner acknowledgment) and a derived pending-queue count now appear in the rail, but the
  remaining four PRD-specified numbers — median time to full containment (`18 min`),
  revocations without incident (`97%`), cross-team coordination time avoided (`31 hrs`),
  and stale/dormant identities auto-flagged (`58`) — are still not on screen. Identity
  therefore still reads as the thinnest-KPI'd of the three siblings side by side, though it
  no longer contradicts itself the way the pre-fix hardcoded queue counts did.

- **Product-rigor's harder calls were left to the founders, by design.** The PRD fixer
  pass added evidence and honesty framing but this cycle did not resolve, and was not asked
  to resolve, the PM-rigor critique's request for an explicit pillar ranking/recommendation
  against `thesis.md`'s decision rule, or the willingness-to-pay gap (`ledger.md` C8: "NO
  evidence found in 40 calls" across all three pillars). Those remain open questions for
  the founders, not engineering or design defects.

## Verification note (this pass)

JS syntax was checked with `node --check` against the extracted `<script>` body of each
file (all three pass); HTML tag balance was checked programmatically (all three balanced);
all three were grepped clean of `console.log`/`debugger`/leftover `TODO` markers. A
headless Chromium (Playwright) was available in this environment and was used to actually
render each dashboard at desktop width, at 420px phone width, and with `colorScheme: dark`
forced, and to click through the full read-only → preview → blocked-confirm →
write-mode → confirm → revert loop on all three. One real bug was found and fixed during
this pass: `code-patching`'s instrument rail (`.rail`, a grid item of `body{display:grid}`)
had no `min-width: 0`, so its non-wrapping readouts forced the entire page to overflow
horizontally at ≤480px instead of scrolling internally as the mobile CSS intended; `.rail`
and `.rail-inner` now both set `min-width: 0`, and the page no longer overflows at 420px
width. A separate Playwright-reported "element intercepts pointer events" warning on
infra-patching's first node click (a text label sitting over the node's center point) was
investigated and found to be a false alarm specific to Playwright's strict actionability
check, not a real interaction bug — a forced click at the same point opens the case file
correctly, confirming the click handler fires normally for real users.
