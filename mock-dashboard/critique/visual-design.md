# Visual design critique — Isoline dashboards

Reviewer: senior visual/product design critique (adversarial pass)
Scope: `DESIGN.md` vs. `identity/index.html`, `infra-patching/index.html`, `code-patching/index.html`

## Verdict

The concept survived; the execution didn't hold the line. DESIGN.md is a genuinely
sharp, specific brief — better than most agencies write. But three independent builds
from one spec produced three dashboards that disagree with each other on the exact
numbers the spec bothered to specify, one of the three quietly reintroduces the exact
pattern the brief named and banned (a dead, unused `.pill` stat-pill class), two of
the three violate the brief's explicit "never dead center" rule on the single most
important compositional decision on the page, and the shared "confidence gate" colors
— the one palette element DESIGN.md says must be identical across all three and
"designed to be accessible" — fail WCAG AA as text in light mode on every single
dashboard that uses them that way. This would not clear an agency internal review.
**`code-patching` is the weakest of the three overall** (dead CSS, most corner-radius
inconsistency, dead-centered epicenter); `identity` is the thinnest/least crafted
(zero hover states anywhere); `infra-patching` is the most disciplined build and the
one the other two should have been checked against before shipping.

---

## 1. Shared "confidence gate" colors fail WCAG AA as text — on all three dashboards, in light mode

DESIGN.md §4 is explicit that gate colors are "shared identically across all three
dashboards" and calls the whole palette "designed to be accessible." Nobody checked.
Computing contrast against `--paper-0` (`#eef1f0`, the page ground every readout and
tag sits on in light mode), sRGB-linearized per WCAG:

| Token | Hex | Contrast vs `--paper-0` | AA (4.5:1 normal text) |
|---|---|---|---|
| `--gate-review` | `#d9a400` | **1.99:1** | Fails badly |
| `--gate-auto` | `#2e8b57` | **3.73:1** | Fails (passes only large/bold-text 3:1) |
| `--gate-blocked` | `#c4293e` | **4.95:1** | Barely passes |

`--gate-review` is used as literal text color/border in all three files:
- `identity/index.html:194` — `.readout .value.gate-review { color: var(--gate-review); }` at 15px normal weight-600 text.
- `identity/index.html:375` — `.cf-tag { color: var(--gate-review); border: 1px solid var(--gate-review); }` at 9.5px.
- `code-patching/index.html:161` — `.readout.g-review .rval{color:var(--gate-review);}`
- `infra-patching` draws the gate label with `style:"fill:"+colorVar` where `colorVar` is `var(--gate-review)` (`infra-patching/index.html:857`).

A ~2:1 ratio is not a marginal miss, it's roughly what you'd get from mid-gray on
mid-gray. Dark mode is fine (the dark `--gate-review` hits ~10:1), which is exactly
why nobody caught it — whoever eyeballed this was looking at the dark scheme.

**Fix:** either darken the light-mode `--gate-review`/`--gate-auto` values until they
clear 4.5:1 against `--paper-0` (a `#a37a00`-range amber and a `#1f6e46`-range green
will get you there without changing hue identity), or stop using gate colors as text
color at all and use them only for strokes/fills/dots ≥3px, pairing every one with
`--ink-900` text as DESIGN.md's own "never color alone" rule already requires
elsewhere. The second option is more consistent with the rest of the spec's own logic
and should be the actual fix, applied once in the shared token block, not per-file.

## 2. Two of three dashboards violate the brief's own "never dead center" rule

DESIGN.md §5.2, in bold: "never dead center — asymmetry is deliberate, see avoid
list." Checking actual epicenter coordinates against their viewBox:

- `identity/index.html:689` — `var CX = 420, CY = 310;` in `viewBox="0 0 1300 620"`
  (`identity/index.html:494`). CY/height = 310/620 = **exactly 0.500** — dead center
  vertically. Only X is offset (0.323, fine).
- `code-patching/index.html:606` — `var EPI = {x:380,y:320};` in
  `viewBox="0 0 1000 640"` (`code-patching/index.html:519`). y/height = 320/640 =
  **exactly 0.500** — dead center vertically, same mistake.
- `infra-patching/index.html:676` — `var ecy = Math.round(h*0.56);` — the only one of
  the three that actually offsets on both axes as specified.

Two out of three implementers took "off-center on desktop" to mean "shift X only,"
which is the one thing the spec called out by name as the thing *not* to do. This
isn't a subtle miss — it's checking one line of arithmetic (`height / 2`) against a
rule stated in bold in the document they were building from.

**Fix:** set `CY`/`ecy` to something like `0.42–0.46` of the field height in both
files, matching infra-patching's approach, and add a lint-style comment at the
computation site (`// never 0.5 — see DESIGN.md §5.2`) so the next edit doesn't
regress it back to center.

## 3. The "same instrument, reskinned" claim doesn't hold up numerically — stroke-width formulas diverge across all three

DESIGN.md §1 promises "same field, same tether, same gate, different epicenter." The
confidence→line-quality formula (§6.2) is the single most important shared piece of
visual logic in the whole system, and each file invented its own coefficients:

```
identity/index.html:673:      var width = 1.5 + (1 - conf) * 5.5;
infra-patching/index.html:529:      width: 1.5 + (1-c)*4.3,
code-patching/index.html:817:  var width = 1.5 + (1-c)*4;
```

At `conf = 0.5` that's a 4.25px ring in identity, 3.65px in infra-patching, 3.5px in
code-patching — a visible difference if you open the three tabs side by side, for a
value the spec describes as *the* signature encoding of the entire system ("one CSS
custom property per ring... driving stroke-dasharray"). The gate arc itself drifts
even harder — this is drawn to the same visual role (announcing the confidence gate
crossing) but rendered at three different weights with three different
implementations of what "the gate" even is:

- `identity/index.html:329` — `.gate-arc { stroke-width: 2.5; opacity: 0.35→1; }` — a
  static double-arc-with-notch, CSS-driven opacity toggle.
- `infra-patching/index.html:851` — `"stroke-width":4` on a single computed path,
  `stroke-linecap:"round"`.
- `code-patching/index.html:924` — `"stroke-width":5` for the arc, plus a separate
  `"stroke-width":3` notch line (`code-patching/index.html:927`) that neither other
  file has an equivalent of.

None of these numbers appear in DESIGN.md — the spec left them as an implementation
detail — but that's precisely the failure mode: a shared visual language needs a
shared token even where the spec is silent, and nobody proposed one, so three people
guessed three times.

**Fix:** promote gate-arc stroke-width and the confidence→width coefficient to
`DESIGN.md` §4 or a new shared `--gate-arc-weight` / a documented formula
`width = 1.5 + (1-conf) * K`, pick one `K`, and have all three files import it
literally rather than re-derive it.

## 4. Rail height and rail-title type size: three specced-as-shared elements, three different numbers

DESIGN.md §5.1 gives a range ("~48–56px") for the rail, which each file nails
differently but defensibly (identity `min-height: 52px`, infra `height:54px`, code
`height:56px`) — technically all in-range, so not a hard violation, but worth flagging
because it means the three dashboards, opened in adjacent tabs of the same product
family, have a visibly different top-chrome height for no reason anyone could explain
to a customer.

The real miss is the product-name lockup inside that rail, which the spec does *not*
give a range for — it just says "Big Shoulders caps" — and which is a literal shared
component (`▣ SKYLAYER · <PILLAR>`) that should render at one size everywhere:

```
identity/index.html:165:      .rail-mark .disp { font-size: 17px; letter-spacing: 0.06em; ... }
infra-patching/index.html:137: font-size:14.5px; ... letter-spacing:.045em;
code-patching/index.html:142:  font-size:16px; ... letter-spacing:.04em;
```

17px/0.06em, 14.5px/0.045em, 16px/0.04em: three sizes and three trackings for what is
supposed to be the one piece of chrome that says "this is the same product family."
This is the header lockup — it is the most-seen, least-changing element on the page,
and it's the one place a customer flipping between the three demo pillars would
actually notice a mismatch.

**Fix:** pin `.rail-mark`/`.mark-text`/`.rail-title` to one literal value (pick
infra-patching's 14.5px/.045em, it's the most restrained) and treat it as a shared
component, not a per-file guess.

## 5. `identity` has zero `:hover` states — the only one of the three with no mouse affordance

```
grep ":hover" identity/index.html   → 0 matches
grep ":hover" infra-patching/index.html → 3 matches (.queue-row, incl. aria-current pairing)
grep ":hover" code-patching/index.html  → 6 matches (.hit, g.node-g, .cf-close, .btn.ghost, .slot-g)
```

Every clickable thing in `identity` — the epicenter, the seven field nodes, the case
file close control on desktop (`identity/index.html:362-364` even sets
`.cf-close { display: none; }` on desktop, so there's no visible close affordance at
all above 480px, relying on... nothing, since clicking the field again doesn't close
it either) — reacts only via `:focus-visible`, i.e. only to keyboard tab order. A
mouse user hovering over `svc-billing-legacy` or any of `n1`–`n7` gets no cursor
feedback beyond the browser's default pointer (`cursor: pointer` is set, but no visual
state change accompanies it — no stroke-width bump, no fill shift, nothing). Compare
`code-patching/index.html:241` — `.hit:hover ~ .node-shape, g:hover .node-shape{filter:brightness(1.08);}`
— a real, if minimal, hover response. This is a basic craft item ("hover/focus/active
states") the review brief explicitly asked to check, and identity fails it outright
while its two siblings pass.

**Fix:** add a `.node:hover .glyph { stroke-width: 2; }`-equivalent (mirroring the
existing `:focus-visible` rule at `identity/index.html:302`) and give desktop users a
visible way to close the case file — either restore `.cf-close` above 480px or add an
explicit "click empty field to close" affordance and say so in the placeholder copy.

## 6. `code-patching` ships a dead, unused `.pill` class that is exactly the pattern DESIGN.md's avoid list bans

```
code-patching/index.html:423-426:
.pill{
  display:inline-flex; align-items:center; gap:4px; font-family:"IBM Plex Mono",monospace;
  font-size:10px; padding:2px 7px; border-radius:10px; border:1px solid var(--border); color:var(--text-muted);
}
```

`grep -n "pill" code-patching/index.html` shows this class is defined and never
referenced anywhere in the markup or the JS render functions — it's leftover code,
probably copy-pasted from a generic-dashboard starting point before the author
remembered DESIGN.md's avoid list bans exactly this ("sidebar + topbar + stat-pill
row," §2) and the rail spec's explicit instruction that readouts are "separated by
hairlines, not pills" (§5.1). It didn't ship *visibly*, so it's not a user-facing
defect, but it is direct, checkable evidence that the avoided pattern was the
implementer's first instinct and had to be caught, not that it was never reached for.
Any future edit that adds one more badge to this file has a ready-made
generic-dashboard pill sitting right there to grab.

**Fix:** delete the dead rule. If a compact inline tag is actually needed somewhere,
build it using the bordered, square-cornered treatment identity already uses for
`.cf-tag` (`border: 1px solid var(--gate-review); padding: 2px 6px;`, no
`border-radius`) so it matches the family's "hairline everything" language instead of
reintroducing a pill.

## 7. Corner-radius treatment of the mobile bottom sheet disagrees across all three, and one of them uses actual rounded corners the spec's tone argues against

- `identity/index.html:450` — only the drag handle gets `border-radius: 2px`; the
  sheet itself is square.
- `infra-patching/index.html:296` — same pattern, handle only, `border-radius:2px`.
- `code-patching/index.html:468` — `border-radius:14px 14px 0 0;` **on the sheet
  container itself**, not just the handle.

DESIGN.md never says the bottom sheet must be square-cornered, so this isn't a spec
violation on its face — but §2's avoid list bans "uniform `rounded-lg` + drop-shadow on
every panel regardless of role," and a 14px-radius slide-up panel with a drop-shadow
(`code-patching/index.html:0 -6px 18px`-style shadow present at the same breakpoint,
mirroring the pattern in the other two files at `identity/index.html:444` and
`infra-patching/index.html:292`) is precisely the rounded-card-with-shadow silhouette
the system is supposed to have replaced everywhere else on the page. It's a minor
component, but it's the one place all three dashboards independently reached for a
conventional "iOS action sheet" look, and code-patching went one small step further
into it than its siblings.

**Fix:** square off the sheet's own corners (radius 0) to match identity and
infra-patching; keep the radius only on the 4px drag handle, consistent with the
"hairlines, not rounded chrome" language the rest of the system already follows.

## 8. Ledger rail height: DESIGN.md gives one number, the three files give three different behaviors

DESIGN.md §5.4: "Ledger rail (bottom, ~72px, fixed...)". Actual implementation:

```
infra-patching/index.html:262: height:74px;
code-patching/index.html:435:  height:73px;
identity/index.html:386-393: no explicit height at all — height is whatever
  `padding: 10px 4px calc(10px + safe-area) + content` resolves to.
```

74px and 73px are both close enough to "~72px" to not be worth a separate complaint on
their own. The real problem is identity: it never fixes a height, so its footer strip's
actual rendered height is a function of the ledger item's font metrics and line-height
at render time, not a controlled 72px like its siblings. Put the three dashboards in
adjacent tabs and the bottom strip visibly changes height when you switch — a "fixed,
~72px" rail per DESIGN.md that is, in one of the three implementations, not actually
fixed.

**Fix:** give `identity`'s `.ledger` an explicit `height: 72px` (or `min-height`, if
the two-line phone stack needs to grow) matching the other two, rather than letting it
float.

## 9. Type scale is closer to "consistent family, sloppy execution" than "ad hoc," but the label tier alone has five different sizes doing the same job

This is the one place the three files agree on more than they disagree — Big
Shoulders / Plex Sans / Plex Mono are used correctly and consistently for their
assigned roles across all three, and font-weight is used meaningfully (700–800 for
display, 500–600 for labels, 400 for body) so the hierarchy is legible from
weight+size alone. Credit where due: this is not "ad hoc pixel values scattered
through the CSS" the way a first-draft AI dashboard usually is.

But the "uppercase eyebrow label" role — `.readout-label` / `.cf-eyebrow` / `.cf-h` /
`.queue-head` / `.readout .label` — the single most repeated micro-pattern on the
page, is set at a different size in nearly every place it appears:
`identity/index.html:184` (9px), `identity/index.html:365` (10px, `.cf-eyebrow`),
`identity/index.html:370` (10.5px, `.cf-section h4`), `infra-patching/index.html:150`
(9px), `infra-patching/index.html:229` (11.5px, `.cf-h`), `code-patching/index.html`
labels sit at 9.5–11px across its own file. None of this is specced by DESIGN.md, so
it's not a spec violation, but a type *system* — as opposed to a type palette everyone
happened to draw from — would collapse all of these into 2–3 named sizes
(`--label-sm: 9px`, `--label-md: 10.5px`) used consistently by role, not a different
value invented at every call site.

**Fix:** define `--type-label-sm`/`--type-label-md` in the shared token block next to
the color tokens (DESIGN.md §4 already exists as the place implementers copy from
verbatim — extend it to type scale, not just color) and require all "eyebrow" labels
across all three files to use one of exactly two sizes.

## 10. Reduced-motion handling is inconsistent in rigor, not just numbers

DESIGN.md §6.4 requires `prefers-reduced-motion: reduce` to "replace travel and
stagger with instant cross-fades, but keep the outward-then-inward reveal order."
`identity` and `code-patching` compute a JS-level `reduceMotion` flag and use it to
zero out `STAGGER`/`SETTLE_BUFFER` in their JS animation scheduling, in addition to a
global CSS `* { transition-duration: 0.01ms !important; }` catch-all
(`identity/index.html:463-465`, mirrored in code-patching). `infra-patching` also
computes `reduceMotion()` and uses it (`infra-patching/index.html:783`), but its CSS
fallback is narrower — only `.flicker` and `.casefile` transitions are explicitly
disabled under the media query (`infra-patching/index.html:301-303`); the ring-bloom
`transition` set inline via `re.g.style.transition` at
`infra-patching/index.html:786` is shortened (`dur = rm ? 140 : 300`) rather than
removed, so infra's "reduced motion" mode still animates, just faster — a materially
different interpretation of "instant cross-fades" than the other two files' "zero out
the transition." A reduced-motion user comparing pillars gets a genuinely different
product behavior depending which one they're on, which is exactly the kind of
cross-dashboard inconsistency this review was asked to hunt for.

**Fix:** standardize on identity/code-patching's approach (hard zero via the
`!important` global rule, not a shortened-but-nonzero duration) since it's the only
one of the three that actually satisfies "instant."

---

## Which one is worst, and why

**`code-patching`** is the weakest dashboard of the three on balance: it's the only
one with dead leftover generic-dashboard CSS (finding 6), the only one that rounds the
mobile sheet's own corners into a conventional action-sheet look (finding 7), and it
shares the dead-center epicenter mistake (finding 2) that only infra-patching avoided.

**`identity`** is the thinnest: it has zero hover states (finding 5), no fixed ledger
height (finding 8), a desktop-hidden close control with no replacement affordance
(finding 5), and — separately from anything above — the simplest field of the three
(binary lit/dark nodes only, no severity texture, no flicker states), which is
defensible given its domain (a credential is either compromised or not, there's no
"degraded" state the way a host has) but does mean it reads as the "unfinished-looking"
one of the three sitting side by side, even though nothing in it is strictly broken.

**`infra-patching`** is the most disciplined of the three: it's the only one that got
the off-center epicenter rule right (finding 2), it has real hover states (finding 5),
and its hazard-hatch/flicker vocabulary for degrade-vs-hardfail states is the most
fully worked-out execution of the "confidence is line quality, texture is state, never
color alone" rule DESIGN.md asks for. It should have been the reference the other two
were checked against before anything shipped — instead, all three shipped in parallel
with nobody diffing them against each other, which is how findings 1–4 and 8–10 all
happened at once.
