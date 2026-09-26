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

### Legibility without the spec

The instrument metaphor is only earning its keep if a viewer who has never read this
document can decode the field in the first few seconds. Nothing below is optional
because it's "just a legend": **every field must render a minimal, always-visible
key** — never hidden behind a tooltip, an expander, or dropped entirely at a
breakpoint — stating, in plain words next to the field (not buried in the case file):

- what the epicenter is (one line, domain-specific: "Epicenter: credential selected
  for revocation")
- what a ring means and how many hops it represents ("Ring = 1 hop: services calling
  this credential directly")
- what line quality (crisp vs. soft/dashed) encodes ("Line quality = confidence")
- what the gate arc means at the point it's crossed ("Gate: crossing here needs
  human review")

This key is part of the field, not a separate help screen — see §5.2 for its exact
placement and the phone-width requirement that it compress, never disappear entirely.
A build that passes every other spec item but ships a field a first-time viewer can't
decode in ~10 seconds without having read this document has failed the actual goal
of the visual system, not just a nice-to-have.

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

**No dead code matching this list.** A class, mixin, or component matching any
avoid-list pattern above — a `.pill`/rounded-stat-badge class chief among them —
must not exist in the shipped CSS/JS *even if it is never referenced in markup*.
"It didn't render" is not a pass: an unused `.pill` rule sitting in the stylesheet is
still evidence the avoided pattern was reached for, and it's a loaded gun for the next
person who adds one more badge. Treat this as a lint rule: before shipping, grep the
stylesheet for every avoid-list term (`pill`, `rounded-lg`-equivalent radii on panels,
gradient, glassmorphism blur, etc.) and delete anything with zero references in the
rendered DOM.

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

  /* confidence gate — saturated, shared across all three dashboards.
     Verified AA (≥4.5:1) as TEXT against BOTH --paper-0 and --paper-1 — see
     "Verified contrast ratios" below. Same hue family as the original palette,
     darkened until they clear AA; do not re-lighten these without re-running the
     contrast check against both paper tokens. */
  --gate-auto:    #1f6e46;  /* auto-approved */
  --gate-review:  #7d5c00;  /* needs-review */
  --gate-blocked: #b81f35;  /* blocked */

  /* blast-radius severity ramp — shared, sequential, independent of pillar hue */
  --radius-0: #8a94a0;  /* contained: no material downstream effect */
  --radius-1: #c79a1e;  /* moderate */
  --radius-2: #b8621e;  /* elevated */
  --radius-3: #a3273a;  /* severe: reaches an SLA / production / untested boundary */

  /* type scale — the repeated "eyebrow" / label role. Exactly two sizes; every
     .readout-label / .cf-eyebrow / .cf-h / .queue-head / .readout .label class
     across all three dashboards uses one of these two, never a third value. */
  --type-label-sm: 9px;    /* dense inline labels (readout labels, tags) */
  --type-label-md: 10.5px; /* section headers inside the case file / ledger */

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
    --gate-blocked: #e35062;  /* brightened from #e0495c — see verified ratios below */

    --radius-0: #7c8791;
    --radius-1: #e6b93a;
    --radius-2: #d1893f;
    --radius-3: #e35062;
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
  --gate-blocked: #e35062;  /* brightened from #e0495c — see verified ratios below */

  --radius-0: #7c8791;
  --radius-1: #e6b93a;
  --radius-2: #d1893f;
  --radius-3: #e35062;
}
```

### Verified contrast ratios (gate tokens as text, both modes)

Computed WCAG 2 relative-luminance contrast, text color against each paper token it
is actually laid on top of (`.readout .value`, `.cf-tag`, gate-arc labels all sit on
either `--paper-0` or `--paper-1`, so both must clear AA — checking only one, as the
original palette did, is exactly how the light-mode failure shipped last time):

| Token | Mode | Hex | vs. `--paper-0` | vs. `--paper-1` | AA (4.5:1) |
|---|---|---|---|---|---|
| `--gate-auto` | light | `#1f6e46` | 5.46:1 | 5.02:1 | Pass |
| `--gate-review` | light | `#7d5c00` | 5.42:1 | 4.99:1 | Pass |
| `--gate-blocked` | light | `#b81f35` | 5.61:1 | 5.17:1 | Pass |
| `--gate-auto` | dark | `#3fae76` | 6.89:1 | 6.41:1 | Pass |
| `--gate-review` | dark | `#e6b93a` | 10.41:1 | 9.69:1 | Pass |
| `--gate-blocked` | dark | `#e35062` | 5.12:1 | 4.76:1 | Pass |

The original dark `--gate-blocked` (`#e0495c`) passed against `--paper-0` (4.83:1)
but fell to **4.496:1 against `--paper-1`** — under 4.5, a real (if narrow) AA
failure that only showed up once both surfaces were checked. It's brightened to
`#e35062` above specifically to clear `--paper-1` with margin; `--radius-3` is kept
identical to `--gate-blocked` in both modes (it was already aliased), so it inherits
the same fix.

**Rule, restated so it can't regress:** gate colors are approved for use as literal
text/border color (readout values, `.cf-tag`, gate-arc labels) *because* the hex
values above are chosen to clear AA against both paper tokens — this is a change to
the fix, not a relaxation of the rule. Any future edit to a `--gate-*` value must
re-run this check against both `--paper-0` and `--paper-1` in the mode being edited
before shipping, and gate colors still may never be the *only* signal for a state —
they are always paired with the gate's name in text or a distinct shape, per §7.

Each dashboard sets one line at its own top level: `--accent: var(--accent-identity)`
(or `-infra` / `-code`). Everything else — gate colors, severity ramp, neutrals — is
identical across all three so the family reads as one product.

---

## 5. Layout philosophy — "the station," not sidebar+topbar+cards

Structural metaphor: a monitoring station instrument desk, organized as three fixed
horizontal strata plus one edge panel that opens on demand. No left nav. No top
search-and-avatar bar. No card grid.

1. **Instrument rail** (top, exactly **52px fixed height** — not min-height, not a
   per-file guess in the 48–56px range that used to be given here; pin the box model
   so all three dashboards' top chrome is pixel-identical — fixed, hairline bottom
   border only, no shadow, no fill change on scroll). Left-aligned: a small pillar
   mark (a single glyph, §7) plus the product name in Big Shoulders caps, set at
   **exactly 14.5px, letter-spacing 0.045em** (the one literal, shared value for
   `.rail-mark`/`.mark-text`/`.rail-title` — this is shared chrome, not a per-file
   typographic choice). Right-aligned: 3–5 live mono-numeral readouts separated by
   hairlines, not pills — e.g. `CONFIDENCE AVG 0.82` `AUTO 3` `REVIEW 1` `BLOCKED 0`.
   These are read like a ticker, not clicked like nav items. Also right-aligned, left
   of the readouts: the **mode indicator and role chip** — see item 5 below; it lives
   in the rail because it must be visible at all times, not opened to be checked.

2. **The field** (center, dominant — at least 60% of viewport height on desktop,
   never boxed in a card, no border, no radius, no shadow: it *is* the page's
   surface). A faint fixed-spacing grid (`--grid-line`, 1px, ~24px cells) covers the
   whole area as base texture, evoking graph paper / a survey sheet.

   **Epicenter position — exact formula, not prose.** Given field viewport width `w`
   and height `h`:
   ```
   cx = w * 0.38
   cy = h * 0.44
   ```
   `cx` may vary between `0.36` and `0.40`, `cy` between `0.42` and `0.46`, to allow
   per-pillar breathing room, but **neither value may ever equal 0.5** on either
   axis — that is the exact rule two of three implementations broke by only offsetting
   `x`. Put a comment at the computation site: `// never 0.5 on either axis — see
   DESIGN.md §5.2`.

   **Ring / hop spacing — exact formula.** Rings are positioned by hop distance from
   the epicenter, not by eye:
   ```
   R0 = 0.10 * min(w, h)        // radius of ring 1 (hop 1)
   ΔR = 0.12 * min(w, h)        // spacing added per additional hop
   r(hop) = R0 + (hop - 1) * ΔR // hop = 1, 2, 3
   ```
   Dependency nodes sit *on* their hop's ring, spaced by equal angular sectors
   (`360° / nodeCountOnRing`), never by hand-authored per-node angles — a field with
   30 nodes on one ring must still lay out without collisions, which a fixed per-node
   `angle:` value (fine for 7 nodes) cannot guarantee.

   A confidence-gate arc (§6.2) is drawn across the field wherever the current blast
   radius crosses from auto-approved into needs-review territory. The field's
   always-visible legend (§1, "Legibility without the spec") renders as a compact
   key anchored to one corner of the field (bottom-left on desktop) — never inside
   the case file, never behind a click.

3. **Case file** (right edge on desktop, width ~360px, a hinged panel that slides
   in from the edge and *pushes* the field rather than covering it — never a modal,
   never a scrim). Opens when a node or the epicenter is selected. Holds the literal
   evidence for that node: what it is, why it's in the blast radius, the confidence
   basis, and (for code) the regression-matrix strip. Closed by default; the field
   is the resting state of the page.

   **Dismissal contract — required at every breakpoint, not just phone.** The panel
   must always render a visible close control in its header (an `X`, Lucide `x`
   glyph) — it is never `display: none` on desktop. In addition, all three of the
   following are baseline behavior, not optional polish:
   - **Escape key** closes the case file whenever it is open, regardless of what has
     focus on the page.
   - **Click/tap outside** the panel (on the field or rail) closes it.
   - **The visible close control** closes it.
   On close, focus returns to the node or epicenter that opened the panel. On open,
   focus moves into the panel (its heading or close control) — see §6.5.

4. **Ledger rail** (bottom, exactly **72px fixed height** — not min-height, not
   "however the content resolves"; every dashboard's footer strip must be
   pixel-identical when switching tabs — fixed, horizontal scroll, hairline top
   border). A filmstrip of past actions, oldest to newest, each a narrow vertical
   instrument reading (timestamp, one-line epicenter description, **an attributed
   actor/approver** — e.g. "revoked by j.ferrer · approved by platform-eng-oncall" —
   even as illustrative demo data, never action-only text — and an outcome glyph:
   confirmed safe / reverted / still monitoring) — not a table, not a card list, not
   a bell dropdown. This replaces navigation history entirely: the past *is* the
   sidebar.

5. **Read-only / write mode.** Every dashboard boots **read-only by default**. The
   rail (item 1) shows a persistent mode indicator — plain text, not color alone:
   `MODE: READ-ONLY` or `MODE: WRITE`, paired with a small role chip naming who is
   viewing (`VIEWER` or `APPROVER` — an approver role is required before write mode
   can even be requested; a viewer sees the toggle but it stays disabled with a
   tooltip/label explaining why). Toggling to write mode is itself a logged, visible
   action — it produces a ledger entry ("j.ferrer granted write access, 14:02"), it
   is never silent. In read-only mode, every action control that would apply a
   change (`REVOKE CREDENTIAL`, `PUSH PATCH`, `Confirm — merge & deploy`) is
   **disabled and relabeled** to name the blocker directly — e.g. `READ-ONLY — REQUEST
   WRITE ACCESS` — never just grayed out with the original label still showing,
   since a disabled button that still says "REVOKE CREDENTIAL" reads as broken, not
   as gated. The preview/arm/bloom interaction (§6.1) still works fully in read-only
   mode — previewing a blast radius is inspection, not a write — only the final
   confirm/apply step is gated.

6. **Scale and queue depth.** The field stays a small, legible scene (1 epicenter,
   a handful of nodes) by design — it is a survey instrument reading *one* action,
   not a table of everything. But the rail and the field together must never imply
   that scene is the whole environment. The rail's readout row (item 1) always
   includes a queue-depth pair, not just the counts for the currently-selected
   action: `PENDING <n> OF <total>` (e.g. `PENDING 8 OF 312`), where `<total>` is the
   full environment count the KPI header/copy claims elsewhere on the page — these
   two numbers must always agree; a mock that states 312 findings anywhere and only
   ever renders 8 clickable rows must say so on the rail, not just in a caption.
   Additionally, the queue itself (the list a node is selected from, not the field)
   gets a visible **pagination/"showing N of total" affordance** — even a simple
   "showing 8 of 312, sorted by confidence ↓" label with next/prev controls is
   enough; the point is that the UI acknowledges its own scale rather than silently
   contradicting the header number.

**Phone collapse (≤480px):** strata stack in the same order, no strata are hidden.
Instrument rail becomes a single horizontally-scrollable row of readouts, and the
mode indicator/role chip (item 5) stays visible in that row rather than being cut —
it is exactly the kind of state a mobile-first CISO check needs at a glance. The
field keeps full width and stays the largest region but simplifies to at most two
rings (collapsing distant hops into a single outer "beyond" band with a count) so
glyphs stay legible without shrinking below a 32px touch target; the field's legend
(§1) compresses to a single abbreviated row at this width — it is never removed via
`display: none`, since the phone width is exactly the "first, cold look" surface the
legend exists for. Ledger rail becomes a vertically stacked list, most recent first,
full width. Case file becomes a bottom sheet that slides up over the bottom third of
the screen (not the full screen — the field stays partly visible above it) with a
**4px-radius drag handle only** — the sheet's own container is square-cornered
(`border-radius: 0`), matching the "hairlines, not rounded chrome" language used
everywhere else in the system, not the rounded `14px 14px 0 0` conventional
iOS-action-sheet look. It is dismissible by swipe-down, by Escape, by tap-outside, or
by the same always-visible close control required in item 3. Side gutter is 16px
minimum at every width; the field's grid texture and ring strokes scale down but
never crop.

---

## 6. Motion and interaction principles

1. **Preview is the confirmation UI.** Selecting an action never applies it. The
   field animates the epicenter's rings expanding outward hop by hop (~130ms stagger
   per hop, ease-out), each ring's nodes transitioning from resting state to
   predicted state in sync with that ring's arrival. The action control is disabled
   and labeled "previewing…" until the animation settles, then relabels to the real
   confirm action with the final number. There is no separate "preview" button —
   arming an action *is* watching its blast radius bloom.
2. **Confidence is line quality, not a separate badge — one formula, shared
   literally.** Every ring's stroke reads its confidence directly via:
   ```
   strokeWidth = 1.5 + (1 - confidence) * 4.5   // clamp to [1.5, 6.0]
   ```
   (base `1.5`, range `4.5` — this is the single `K` the three builds previously
   guessed independently as `5.5`, `4.3`, and `4`; every dashboard imports this
   literal formula, not its own coefficient). Pair the stroke width with blur:
   ```
   blurStdDeviation = (1 - confidence) * 2.5   // clamp to [0, 2.5]
   ```
   via `feGaussianBlur`, and `stroke-dasharray` scaled the same way, so a
   high-confidence ring is a crisp ≤2px solid line and a low-confidence ring is a
   soft, ~6px, blurred/dashed band — never a color swap. This is one CSS custom
   property per ring (`--confidence: 0–1`) driving all three outputs.

   **Gate arc — one shared weight and one shared shape.** The gate arc is a single
   computed SVG path (never a static double-arc, never a separate notch line drawn
   as its own stroke), `stroke-width: 3`, `stroke-linecap: round`. Where the gate
   glyph's notch (§7) needs to sit on the arc, draw it as a short perpendicular tick
   at `stroke-width: 1.5`, positioned at the crossing point — a mark on the one arc,
   not a second competing stroke. This one spec (3px arc, round cap, 1.5px notch
   tick) replaces the three different implementations (2.5px/4px/5px+3px) that
   shipped previously.
3. **Reversibility is travel, not a toggle.** Every settled action keeps a visible
   thin dashed tether back to its last-known-good snapshot at rest, with a small
   anchor glyph at the far end. Triggering revert animates the tether reeling in —
   the affected node visibly travels back along the tether's own path to the anchor
   — rather than the state instantly flipping. The tether's stroke *weight* encodes
   how expensive that rollback actually is (thin = instant/cheap, thick = costly),
   set once per action and never animated away. The primary rollback control's
   *label* is always plain operational language first — "Undo — restore last
   known-good" — with the tether/reel-in metaphor as the visual only; a metaphor the
   viewer must decode ("REEL IN TETHER") never carries the only explanation of what
   the button does. Revert must guard against re-entrancy: disable the control (or
   set a `reverting` state) synchronously before starting the travel animation, so a
   second click inside the animation window cannot start a second traveler or write
   a duplicate ledger entry.
4. **Reduced motion, same order.** Under `prefers-reduced-motion: reduce`, replace
   travel and stagger with instant cross-fades (a hard zero on transition duration,
   not merely a shorter one — "faster" is not "instant"), but keep the
   outward-then-inward reveal *order* so the information hierarchy (nearest hop
   first) survives without motion. Re-check the media query live (a `change`
   listener, or re-read `matchMedia(...).matches` at each point of use) rather than
   snapshotting it once at load — the CSS side already reacts live, and the JS side
   must match it or the page half-respects the setting.
5. **Baseline keyboard and focus contract — required on the epicenter and every
   field node, no exceptions.** Every one of these is a spec requirement, not left
   to an implementer's judgment:
   - `tabindex="0"` and `role="button"` on the epicenter's `<g>` and on every
     dependency node's `<g>` — the epicenter is "the screen's dominant object"
     (§1) and is never harder to reach by keyboard than a peripheral node.
   - a `keydown` handler on each that activates on `Enter` and `Space`, calling the
     *same* function the `click` handler calls — never a separate, drifting code
     path.
   - a real `aria-label` on every one of them, built from actual node data (name +
     type + hop/ring, e.g. `"svc-billing-legacy, service account, ring 2"`) — never
     left unset. An unlabeled `role="button"` that a screen reader announces as a
     bare "button" fails this contract even if the keydown handler works.
   - the field's outer `<svg>` never carries `role="img"` while it contains these
     focusable children — `role="img"` tells assistive tech to treat the subtree as
     one flat picture and stop descending, which silently swallows every node above.
     Use `role="group"` (or `role="application"` only if the field truly behaves
     like a custom widget end to end) with a `<desc>` describing the static
     backdrop (rings, grid, gate arc), and let the interactive children carry their
     own roles.
   - dynamic state changes that matter to a non-visual user — the rail readouts,
     the gate/queue counts, the action button's label changing from "previewing…"
     to the real confirm label, a completed revert — are announced through a small,
     dedicated `aria-live="polite"` status node with a short, targeted sentence
     ("Gate: review — 1 untested path"). `aria-live` is never placed on a container
     that gets fully torn down and rebuilt on every render (a whole re-announced
     table or field is the opposite of considerate); it lives on a node whose text
     content is set to exactly what should be announced, no more.
   - opening the case file moves focus into it (its heading or close control);
     closing it returns focus to whatever opened it (§5.3).

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
