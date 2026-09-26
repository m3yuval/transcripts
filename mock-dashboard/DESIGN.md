# ISOLINE — a design system for Skylayer's three product wedges

Prepared for the mock dashboards for **Identity**, **Infrastructure Patching**, and
**Code Patching**. This document is the shared brief three independent implementers
build from; it is not itself the artifact.

---

## 1. The concept

**Name: Isoline.**

An isoline is a line of equal value on a map — a contour line on a topographic
survey, an isobar on a weather chart. Nothing in security software looks like this,
which is the point: Skylayer's own customers already describe the product's job in
spatial, physical terms — "blast radius" (Mike Hiltz), "one click undo or rollback"
(Israel Bryski), "read-only... let's see how that goes" (Harris Schwartz), "I'm not
gonna trust to shoot a gun" (Andrew Dutton). Nobody in those calls talks about scores
or dashboards. They talk about *where the damage would land* and *how to get back*.
Isoline takes that literally: every dashboard is a survey instrument reading the
terrain around a proposed action, not a grid of cards summarizing it.

The story: **every action is a disturbance at a point, and Skylayer draws where it
will actually be felt before it happens.** The screen's dominant object is always a
*field* — an epicenter (the credential, the host, the merge) surrounded by concentric
rings that fall off in intensity the further a dependency sits from it, the way a
seismic-intensity map or a weather isobar chart falls off from its center. Confidence
is not a badge; it's whether those rings draw as crisp survey lines or soft,
uncertain bands. Reversibility is not a toggle; it's a visible tether — a drawn line
back to the last known-good state that never disappears until the action is
confirmed safe, and that *reels the state back in* along its own path if triggered.
Three pillars, one instrument: same field, same tether, same gate, different
epicenter and a different accent lamp.

---

## 2. Avoid list

Everything the founder named, verbatim:

- Generic purple-to-blue AI gradients
- Glassmorphism cards
- Generic shadcn/Tailwind admin-template look: rounded white cards in a grid,
  sidebar + topbar + stat-pill row
- Emoji as icons
- Generic "dashboard" cliché layouts
- Stock gradient hero banners

Added for this system, because they're just as generic in security specifically or
would undercut the concept:

- Matrix-green terminal / monospace-on-black hacker aesthetic
- Hoodie-and-hacker stock imagery, or any stock photography at all
- Padlock, shield, or checkmark glyphs standing in for "secure" / "safe" — Isoline's
  own instrument glyphs (§7) carry that meaning instead
- Literal explosion, bomb, or blast/shockwave *imagery* (fireballs, cracks, debris) —
  "blast radius" is the mechanism, not a special effect; the visual language stays a
  survey instrument, not a disaster illustration
- Traffic-light red/amber/green as the *only* encoding of state — every state below
  also carries a distinct shape, stroke, or texture so the page holds up for
  color-blind viewers and in print
- Neumorphism / soft-embossed skeuomorphic buttons
- Uniform `rounded-lg` + drop-shadow on every panel regardless of role
- Numbered 01/02/03 step markers where the content isn't actually a sequence
- Sparkle/glow "AI" iconography anywhere in the chrome
- Centering everything; this system is asymmetric by design (see §5)

---

## 3. Typography

- **Display / heading — Big Shoulders** (variable family; use the *Big Shoulders
  Display* and *Big Shoulders Text* faces, weights 600–800). Condensed, engraved,
  industrial — cut for cornerstones and gauges, not software chrome. Use it large,
  set in caps for section labels and the big confidence/severity numerals, tightly
  tracked at display sizes.
- **Body / UI — IBM Plex Sans** (400 body copy, 500–600 for labels and controls).
  A working, engineered face with enough personality to not read as a default, and
  excellent at small UI sizes.
- **Mono / data — IBM Plex Mono.** Every numeral that must line up — confidence
  scores, timestamps, hop counts, IP/ARN/hash strings, ledger entries — sets in this
  face with `font-variant-numeric: tabular-nums`. Plex Mono and Plex Sans share
  proportions, so switching between them mid-line (a label next to a value) doesn't
  jar.

Load once:
```html
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Big+Shoulders:wght@500;600;700;800&family=Big+Shoulders+Text:wght@500;600;700&family=IBM+Plex+Sans:ital,wght@0,400;0,500;0,600;1,400&family=IBM+Plex+Mono:wght@400;500;600&display=swap">
```
Fallback stacks: `"Big Shoulders", "Arial Narrow", sans-serif` /
`"IBM Plex Sans", system-ui, sans-serif` / `"IBM Plex Mono", ui-monospace, monospace`.

---

## 4. Color system

Rule for the palette: **pillar accents are muted instrument-lamp colors** (identity,
infra, code — one per product, used for the epicenter mark, the field's active
ring, and primary controls on that product's dashboard only). **Confidence-gate and
blast-radius colors are saturated signal colors, shared identically across all three
dashboards** — never reused as a pillar accent, so "this is the infra product" and
"this needs review" are never the same color doing double duty.

```css
:root {
  color-scheme: light;

  /* neutrals — cool survey-paper family, not warm cream */
  --paper-0: #eef1f0;   /* page ground */
  --paper-1: #e3e8e6;   /* recessed panels, field base */
  --paper-2: #d4dbd8;   /* hairlines, base contour grid */
  --ink-900: #10151a;   /* primary text */
  --ink-700: #3c4750;   /* secondary text */
  --ink-400: #74838a;   /* muted labels, tick marks, captions */
  --line:    #b7c2be;   /* borders, dividers */

  /* pillar accents — muted, one per product, never used for state */
  --accent-identity: #1f7a8c;  /* teal-cyan — sessions, credentials, signal */
  --accent-infra:    #a8621e;  /* amber-brown — hosts, hardware, machinery */
  --accent-code:     #5c7a3a;  /* moss-olive — branches, dependency trees */

  /* confidence gate — saturated, shared across all three dashboards */
  --gate-auto:    #2e8b57;  /* auto-approved */
  --gate-review:  #d9a400;  /* needs-review */
  --gate-blocked: #c4293e;  /* blocked */

  /* blast-radius severity ramp — shared, sequential, independent of pillar hue */
  --radius-0: #8a94a0;  /* contained: no material downstream effect */
  --radius-1: #c79a1e;  /* moderate */
  --radius-2: #b8621e;  /* elevated */
  --radius-3: #a3273a;  /* severe: reaches an SLA / production / untested boundary */

  /* semantic surfaces, derived */
  --surface:        var(--paper-0);
  --surface-panel:  var(--paper-1);
  --surface-field:  var(--paper-1);
  --grid-line:      var(--paper-2);
  --text:           var(--ink-900);
  --text-muted:     var(--ink-700);
  --text-faint:     var(--ink-400);
  --border:         var(--line);
}

@media (prefers-color-scheme: dark) {
  :root:not([data-theme="light"]) {
    color-scheme: dark;

    --paper-0: #0b0f13;
    --paper-1: #12181d;
    --paper-2: #232c31;
    --ink-900: #e8ecec;
    --ink-700: #aab4b8;
    --ink-400: #6d7980;
    --line:    #2b363c;

    --accent-identity: #3fa6bb;
    --accent-infra:    #d1893f;
    --accent-code:     #8bab5e;

    --gate-auto:    #3fae76;
    --gate-review:  #e6b93a;
    --gate-blocked: #e0495c;

    --radius-0: #7c8791;
    --radius-1: #e6b93a;
    --radius-2: #d1893f;
    --radius-3: #e0495c;
  }
}

:root[data-theme="dark"] {
  color-scheme: dark;

  --paper-0: #0b0f13;
  --paper-1: #12181d;
  --paper-2: #232c31;
  --ink-900: #e8ecec;
  --ink-700: #aab4b8;
  --ink-400: #6d7980;
  --line:    #2b363c;

  --accent-identity: #3fa6bb;
  --accent-infra:    #d1893f;
  --accent-code:     #8bab5e;

  --gate-auto:    #3fae76;
  --gate-review:  #e6b93a;
  --gate-blocked: #e0495c;

  --radius-0: #7c8791;
  --radius-1: #e6b93a;
  --radius-2: #d1893f;
  --radius-3: #e0495c;
}
```

Each dashboard sets one line at its own top level: `--accent: var(--accent-identity)`
(or `-infra` / `-code`). Everything else — gate colors, severity ramp, neutrals — is
identical across all three so the family reads as one product.

---

## 5. Layout philosophy — "the station," not sidebar+topbar+cards

Structural metaphor: a monitoring station instrument desk, organized as three fixed
horizontal strata plus one edge panel that opens on demand. No left nav. No top
search-and-avatar bar. No card grid.

1. **Instrument rail** (top, ~48–56px, fixed, hairline bottom border only — no
   shadow, no fill change on scroll). Left-aligned: a small pillar mark (a single
   glyph, §7) plus the product name in Big Shoulders caps. Right-aligned: 3–5 live
   mono-numeral readouts separated by hairlines, not pills — e.g.
   `CONFIDENCE AVG 0.82` `AUTO 3` `REVIEW 1` `BLOCKED 0`. These are read like a
   ticker, not clicked like nav items.

2. **The field** (center, dominant — at least 60% of viewport height on desktop,
   never boxed in a card, no border, no radius, no shadow: it *is* the page's
   surface). A faint fixed-spacing grid (`--grid-line`, 1px, ~24px cells) covers the
   whole area as base texture, evoking graph paper / a survey sheet. One epicenter
   mark sits off-center (left-of-center on desktop, roughly golden-ratio position,
   never dead center — asymmetry is deliberate, see avoid list). Concentric rings
   (§8) expand from it; dependency nodes are small glyphs positioned by hop-distance
   along the rings, not by any decorative arrangement. A confidence-gate arc (§6,
   §8) is drawn across the field wherever the current blast radius crosses from
   auto-approved into needs-review territory.

3. **Case file** (right edge on desktop, width ~360px, a hinged panel that slides
   in from the edge and *pushes* the field rather than covering it — never a modal,
   never a scrim). Opens when a node or the epicenter is selected. Holds the literal
   evidence for that node: what it is, why it's in the blast radius, the confidence
   basis, and (for code) the regression-matrix strip. Closed by default; the field
   is the resting state of the page.

4. **Ledger rail** (bottom, ~72px, fixed, horizontal scroll, hairline top border).
   A filmstrip of past actions, oldest to newest, each a narrow vertical instrument
   reading (timestamp, one-line epicenter description, outcome glyph — confirmed
   safe / reverted / still monitoring) — not a table, not a card list, not a bell
   dropdown. This replaces navigation history entirely: the past *is* the sidebar.

**Phone collapse (≤480px):** strata stack in the same order, no strata are hidden.
Instrument rail becomes a single horizontally-scrollable row of readouts. The field
keeps full width and stays the largest region but simplifies to at most two rings
(collapsing distant hops into a single outer "beyond" band with a count) so glyphs
stay legible without shrinking below a 32px touch target. Ledger rail becomes a
vertically stacked list, most recent first, full width. Case file becomes a bottom
sheet that slides up over the bottom third of the screen (not the full screen — the
field stays partly visible above it) with a drag handle, dismissible by swipe-down
or a close control. Side gutter is 16px minimum at every width; the field's grid
texture and ring strokes scale down but never crop.

---

## 6. Motion and interaction principles

1. **Preview is the confirmation UI.** Selecting an action never applies it. The
   field animates the epicenter's rings expanding outward hop by hop (~130ms stagger
   per hop, ease-out), each ring's nodes transitioning from resting state to
   predicted state in sync with that ring's arrival. The action control is disabled
   and labeled "previewing…" until the animation settles, then relabels to the real
   confirm action with the final number. There is no separate "preview" button —
   arming an action *is* watching its blast radius bloom.
2. **Confidence is line quality, not a separate badge.** Every ring's stroke reads
   its confidence directly: high confidence draws a crisp 1.5px solid line; low
   confidence draws the same ring as a soft ~6px blurred/dashed band. This is one
   CSS custom property per ring (`--confidence: 0–1`) driving `stroke-dasharray` and
   an SVG `feGaussianBlur`, not a color swap.
3. **Reversibility is travel, not a toggle.** Every settled action keeps a visible
   thin dashed tether back to its last-known-good snapshot at rest, with a small
   anchor glyph at the far end. Triggering revert animates the tether reeling in —
   the affected node visibly travels back along the tether's own path to the anchor
   — rather than the state instantly flipping. The tether's stroke *weight* encodes
   how expensive that rollback actually is (thin = instant/cheap, thick = costly),
   set once per action and never animated away.
4. **Reduced motion, same order.** Under `prefers-reduced-motion: reduce`, replace
   travel and stagger with instant cross-fades, but keep the outward-then-inward
   reveal *order* so the information hierarchy (nearest hop first) survives without
   motion.

---

## 7. Iconography

A bespoke, single-weight (1.5px stroke) line-icon set drawn as inline SVG — never a
webfont, never emoji. The set is small and is *the same vocabulary as the
visualization*, reused at label size, so the page never needs a separate generic
icon language for domain concepts:

- **Ring glyph** (concentric arcs) — used for "blast radius" labels and the pillar
  mark, styled per-pillar with the accent color.
- **Tether glyph** (a line to a small anchor dot) — reversibility, rollback,
  "last known good."
- **Gate glyph** (a partial arc with a notch, drawn open / half / shut) — the three
  confidence states, always paired with the gate's name in text, never color alone.
- **Hop-marker glyph** (a small tick on a radius) — used in legends to explain what
  a ring distance means for that pillar (1 hop, 2 hops, SLA boundary, etc).

For incidental interface chrome only (close, expand, filter, sort — never a domain
concept) use **Lucide** static SVGs via
`https://cdnjs.cloudflare.com/ajax/libs/lucide-static/<pinned version>/` so
implementers aren't hand-drawing every utility glyph, but keep it strictly out of
anything that means "safe," "vulnerable," "credential," or "service" — those always
use the bespoke set above.

---

## 8. The three signature visualizations

All three are the same instrument (epicenter → rings by hop-distance → gate arc →
tether) reskinned per domain. Each section below is implementable on its own.

### 8a. Identity — the Downstream Dark Map

- **Epicenter:** the credential or session selected for revocation.
- **Rings by hop:** ring 1 = things that authenticate directly with it (API keys,
  scoped tokens); ring 2 = automations and service accounts those feed; ring 3 =
  end-consumers/dependent sessions those automations trigger.
- **Node state on preview:** unaffected nodes stay lit at full `--ink-900`/paper
  contrast. Nodes inside the blast radius **dim toward `--paper-1`/near-ink-black**
  hop by hop as the preview animates outward — literally going dark — each carrying
  a small "last active" mono timestamp so the CISO reads *what* goes dark, not a
  spreadsheet row.
- **Gate arc:** drawn wherever the radius crosses from "session tokens only" (cheap
  to be wrong — auto-revoke, `--gate-auto`) into "touches an automation or service
  account" (`--gate-review`) — rendered as the gate glyph's notch sitting literally
  on the boundary ring, not a separate banner.
- **Tether:** after revocation, a tether persists from the epicenter to a restore
  anchor for one click undo, tether weight thin (session-scoped) to thick
  (service-account-scoped, costlier to restore correctly).

### 8b. Infrastructure patching — the Downstream Break Map

- **Epicenter:** the host or container queued for patch/reboot.
- **Rings by hop:** ring 1 = services running directly on the host; ring 2 =
  services that call those; ring 3 = customer-facing, SLA-bound endpoints.
- **Node state on preview:** nodes predicted to only degrade (brief retry, no
  outage) render with a light flicker animation during preview; nodes predicted to
  hard-fail render static, filled with the matching `--radius-*` severity color.
  Any node in ring 3 carries a small SLA tag (e.g. `99.95%`) so a boundary crossing
  into contractual territory is visible at the glyph, not buried in a tooltip.
- **Gate arc:** auto-approved when the full predicted radius resolves inside the
  next scheduled maintenance window; needs-review the moment the radius reaches an
  SLA-tagged node outside that window.
- **Tether:** weight encodes rollback mechanism cost directly — thin for an instant
  snapshot restore, thick for anything requiring a reimage — so the CISO can read
  "how hard would undo actually be" before confirming, matching Andrew's own
  framing: cheap-to-reverse hygiene work is where trust starts.

### 8c. Code patching — the Call Path / Regression Proof Map

- **Epicenter:** the dependency version bump or merge under review.
- **Rings by hop:** ring 1 = direct callers of the changed function/package;
  ring 2 = transitive callers; ring 3 = public entry points / deployed services
  that terminate a call path reaching the change.
- **Proof strip:** anchored directly beneath the field (not a separate tab) — rows
  are the call paths the field just lit up, columns are the regression tests that
  exercise them, cells shaded pass/fail/**no coverage**. A reached-but-uncovered
  path is the loudest state in the whole system: hazard diagonal-hash texture (not
  color alone) on both the field node and the matrix cell, so it reads under a
  color-blind or grayscale render too.
- **Gate arc:** auto-approve requires every node inside the radius to have at least
  one passing test; a single reached-and-untested path forces needs-review
  regardless of the aggregate confidence number — the matrix can veto the field.
- **Tether:** literally "revert this commit," tether weight set at merge time from
  the radius size recorded then, so a later rollback decision is compared against
  the blast radius that was actually accepted, not re-estimated from scratch.

---

## 9. Page structure sketch

Desktop (≥900px):

```
┌───────────────────────────────────────────────────────────────────────┐
│ ▣ SKYLAYER · IDENTITY        CONF AVG 0.82 │ AUTO 3 │ REVIEW 1 │ BLK 0 │  ← instrument rail
├───────────────────────────────────────────────────────────────┬───────┤
│  · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · ·│ CASE  │
│  · · · · · ╭──────────╮· · · · · · · · · · · · · · · · · · · ·│ FILE  │
│  · · · ·╭──┤  ring 3  ├──╮· · · · · · · gate arc ─ ─ ─ ─ ─ ─ ─│(hidden│
│  · · · ·│ ╭┤ ring 2   ├╮ │· · · · · · · · · · · · · · · · · ·│ until │
│  · · · ·│ │╭┤ring1├╮  │ │· · · · · · · · · · · · · · · · · ·│select)│
│  · · · ·│ │● EPICENTER │ │· · · · · · · · · · · · · · · · · ·│       │
│  · · · ·│ ╰┤    ├╯  │ │· · · · · · · · · · · · · · · · · · ·│       │
│  · · · ·╰──┤    ├──╯· · · · · · · · · · · · · · · · · · · · ·│       │
│  · · · · · ╰──────────╯· · · · · · · ⇢ tether ⇢ ⚓ · · · · · ·│       │
│  · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · ·│       │  ← the field
├───────────────────────────────────────────────────────────────┴───────┤
│ 09:14 revoked→confirmed safe │ 09:02 patched→reverted │ 08:41 …       │  ← ledger rail
└───────────────────────────────────────────────────────────────────────┘
```

Phone (≤480px), strata stacked, case file as a bottom sheet:

```
┌─────────────────────────┐
│ ▣ SKYLAYER   ⟷ readouts │  instrument row (scrolls sideways)
├─────────────────────────┤
│    · · · ╭────────╮ · · │
│    · · ╭┤ ring 2  ├╮· · │
│    · · │● EPI  ring1│· ·│  the field (full width, 2 rings + "beyond")
│    · · ╰┤        ├╯· · │
│    · · · ╰────────╯ · · │
├─────────────────────────┤
│ 09:14  revoked  ✓safe   │  ledger, stacked
│ 09:02  patched  ↺revert │
├─────────────────────────┤
│ ▔▔▔ case file (sheet) ▔▔│  slides up on selection
└─────────────────────────┘
```

Same regions, same order, same objects at every width — only the field's ring
count and the ledger's orientation change.
