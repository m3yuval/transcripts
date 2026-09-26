# Frontend engineering critique — mock-dashboard (identity / infra-patching / code-patching)

## Verdict

None of these three ship-ready. Every file gets the color tokens, the type system and the
overall "station" layout right — that part was clearly copy-pasted correctly from DESIGN.md and
is not in question here. What's wrong is underneath the paint: **every single dashboard has at
least one interactive element that a keyboard-only or screen-reader user cannot use at all**, two
of the three have a **race condition that corrupts on-screen state** the moment a user clicks
faster than the demo's own animation timers, and the "verified in headless Chromium" claims in
the build reports do not survive tracing the actual event handlers — headless Chromium has no
screen reader and no keyboard-only user, so it never would have caught any of this. Fix the
findings below before calling any of these "accessible" or "done."

---

## `identity/index.html`

1. **The case file cannot be closed on desktop at all — the close button is `display:none`
   unconditionally.**
   Line 362-364:
   ```css
   .cf-close { display: none; }
   ```
   This is only overridden back to `display:inline-flex` inside the `@media (max-width:480px)`
   block (line 451). At any desktop width there is no close button in the DOM's visible layout,
   no `Escape` key handler anywhere in the script, and no click-outside-to-dismiss. Once a user
   opens the case file (click or Enter/Space on any node), it is permanently open for the rest of
   the session — the only way to change its content is to select a different node.
   **Fix:** either drop the `display:none` override entirely and give `.cf-close` a real
   always-visible style, or add a real desktop-appropriate close affordance (an `X` in the panel
   header) plus an `Escape` keydown handler that calls `closeCasefile()`.

2. **`role="img"` on an SVG that contains focusable, `role="button"` children.**
   Lines 494 and 530:
   ```html
   <svg class="field-svg full" ... role="img" aria-label="Downstream blast radius map for svc-billing-legacy">
   ```
   `role="img"` tells assistive tech "this subtree is a single flat picture, do not descend into
   it." Several screen readers (including recent VoiceOver/Safari combinations) will not expose
   the nested `tabindex="0" role="button"` epicenter and node groups as separately operable
   elements once they're inside an `img`-rolewrapped container, regardless of how carefully those
   nodes are labeled individually. This directly undercuts the very keyboard/AT support the file
   otherwise tries to build in.
   **Fix:** drop `role="img"` from the `<svg>` itself (or change it to `role="group"` /
   `role="application"` with a `<title>`/`<desc>`), and describe the *static* backdrop (rings,
   grid, gate arc) with a `<desc>` element rather than an image role that swallows the interactive
   children.

3. **No `aria-live` region anywhere — every dynamic state change is silent to screen reader
   users.** The confidence/auto/review/blocked readouts (`#ro-conf`, `#ro-auto`, …, updated in
   `paintQueue`/`paintConfidence`), the ledger (`renderLedger`, called after every confirm/revert),
   and the epicenter's own status line (`#epi-status-full`) all mutate via plain
   `textContent`/`innerHTML` writes with zero `aria-live` anywhere in the document. A screen
   reader user who presses "REVOKE CREDENTIAL" hears nothing when the button becomes "PREVIEWING…",
   nothing when it becomes armed, and nothing when the revocation is confirmed — they'd have to
   blindly re-focus the button to discover the state changed.
   **Fix:** wrap `#action-hint` (or a dedicated status node) in `aria-live="polite"`, and announce
   ledger pushes and gate/queue count changes through the same or a second live region.

4. **Opening the case file does not move focus into it, and there's no focus trap.** `openCasefile()`
   (line 855) toggles a class and an `aria-hidden` attribute but never calls `.focus()` on anything
   inside `#casefile`. Combined with finding #1, a keyboard user who activates a node is left with
   focus still on the field while a panel they cannot reach or dismiss via keyboard sits open next
   to it.
   **Fix:** on open, focus the panel's heading or (once it exists) its close button; on close,
   return focus to the node/epicenter that was activated.

5. **Node positions are hardcoded pixel/angle pairs with no collision handling** (`NODES` array,
   lines 619-640, each with a literal `angle:` in degrees consumed by `polar()`). This is fine for
   exactly 7 nodes tuned by hand, but there is no logic anywhere to space labels/glyphs apart if a
   ring gets more entries — a real "30 accounts / 100 keys" scenario the PRD itself describes
   would immediately overlap glyphs and text at ring 2/3 with no fallback.
   **Fix:** at minimum, compute angular spacing (`sectorAngles`-style, as infra-patching does)
   rather than authoring literal angles per node, so the layout survives a longer findings list.

---

## `infra-patching/index.html`

1. **Rapid double-click (or repeated clicks) on the revert button duplicates the revert and
   ledger entry.** `revertAction()` (line 931) is invoked directly from a plain `click` listener
   on `#cfRevertBtn` and does **not** disable the button, set any "reverting" state flag, or guard
   re-entry before kicking off its 650ms `requestAnimationFrame` travel animation. Two clicks
   inside that 650ms window each independently:
   - read `line.getAttribute("x1"/"y1"/"x2"/"y2")` — the *second* call reads coordinates the
     *first* call's rAF loop is actively mutating (`line.setAttribute("x1", cx)` at line 951), so
     it starts its traveler mid-path instead of at the epicenter;
   - create their own `<circle class="traveler">` via `el(..., svg)` (line 944), so two dots
     animate simultaneously;
   - each schedule and eventually call `finishRevert(f)` (line 953), which calls
     `addLedgerEntry(f, "reverted")` (line 959) — **twice** — producing two duplicate "reverted"
     rows in the ledger rail for one user action, and setting `state.status[f.id]` twice.
   **Fix:** set `state.status[f.id] = "reverting"` (or simply disable `#cfRevertBtn`) synchronously
   at the top of `revertAction()`, before scheduling the animation, and re-render the button as
   disabled immediately.

2. **Epicenter and every dependency node have no accessible name whatsoever.**
   Line 757: `el("g", { class:"epicenter", tabindex:"0", role:"button" }, svg);`
   Line 799: `var g = el("g", { class:"node", tabindex:"0", role:"button" }, parentG);`
   Neither call sets `aria-label` (or any text alternative) anywhere — compare this to the
   identity file's `'aria-label': n.name + ', ' + typeLabel(n.type) + ...` on every node, and to
   this same file's own `aria-label` on the queue rows (`renderQueue`, line 606-612) and pending
   slots. A screen reader user tabbing through the field here hears a bare, unlabeled "button" for
   the epicenter and for every one of the up to 8 host/CVE nodes, with no way to tell them apart.
   This is a straightforward regression relative to the other two dashboards in the same set and
   the single worst accessibility gap in this file.
   **Fix:** add `aria-label` to both the epicenter `<g>` (host + CVE + gate) and each node `<g>`
   (name + predicted state + SLA if present), matching what `renderCaseFile`/tooltips already know.

3. **`role="img"` on the field `<svg>`** (`<svg class="field-svg" id="fieldSvg" role="img">`,
   line 325) wraps the same interactive epicenter/node buttons as identity's file — same failure
   mode as identity finding #2, same fix.

4. **Full SVG teardown and rebuild on every interaction, including on every debounced resize.**
   `renderField()` (line 654) opens with `svg.innerHTML = ""` and rebuilds every `<pattern>`,
   `<filter>`, ring, node, gate arc and tether from scratch — called from `selectFinding`,
   `confirmAction`, `revertAction`, `finishRevert`, and the 140ms-debounced `resize` handler
   (line 1079). With 8 findings and ~3 rings/node each this doesn't visibly jank today, but it's
   architecturally the wrong shape: resizing the window recreates every `<filter id="blur-...">`
   element and every path/text node in the field on every debounce tick instead of just
   repositioning existing elements, and there is no memoization of the ring/gate geometry beyond
   the throwaway `layoutCache` (which is written but only read by `revertAction`, never reused by
   `renderField` itself). This will not scale past the demo's fixed 8-finding dataset.
   **Fix:** separate "build once" (defs/patterns) from "update per render" (positions/opacities),
   or accept the constant-rebuild approach explicitly as a demo-only shortcut and say so in a
   comment — right now it reads as an oversight, not a decision.

---

## `code-patching/index.html`

1. **The epicenter — the single most important interactive element in the whole design — is
   completely unreachable by keyboard.** `renderEpicenter()` (line 1007) builds
   `<g id="epicenterLayer">` and attaches only `mouseenter`, `mousemove`, `mouseleave`, and `click`
   listeners (lines 1018-1022):
   ```js
   layer.addEventListener("mouseenter", function(ev){ showTip(ev, ...); });
   layer.addEventListener("mousemove", moveTip);
   layer.addEventListener("mouseleave", hideTip);
   layer.style.cursor = "pointer";
   layer.addEventListener("click", function(){ openCasefile(f.id); });
   ```
   There is no `tabindex`, no `role="button"`, and no `keydown` handler — contrast this with the
   dependency nodes three lines away (`renderNodes`, line 955: `tabindex:"0", role:"button"` plus
   an Enter/Space `keydown` handler) and the pending-slot glyphs (`renderPendingSlots`, line 847,
   same pattern). A keyboard-only user can Tab through every peripheral dependency node and every
   queued finding, but can never focus or activate the epicenter itself — the one object
   DESIGN.md calls "the screen's dominant object." This is the single clearest instance across all
   three files of a build report's "verified in headless Chromium" claim not surviving an actual
   keyboard trace.
   **Fix:** add `tabindex="0"`, `role="button"`, an `aria-label`, and an Enter/Space `keydown`
   handler to the epicenter group, identical to what `renderNodes` already does two functions
   above it.

2. **Stale-closure race in `selectFinding()` corrupts the case file after fast successive
   selections.** (line 1326)
   ```js
   function selectFinding(id){
     selectedId = id;
     var f = FINDINGS.find(function(x){ return x.id === id; });
     previewing = true;
     renderField(f, true);
     renderMatrix(f);
     renderCasefile(f);
     var settleAt = 3*STAGGER + 420;
     setTimeout(function(){
       previewing = false;
       renderCasefile(f);       // <-- closes over the OLD `f`, not the current selection
     }, settleAt);
   }
   ```
   If the user clicks a second pending-slot node (or the matrix/hop-list of another finding)
   within `settleAt` (~810ms with motion, ~510ms reduced) of the first click, the first call's
   timeout still fires afterward and calls `renderCasefile(f)` with the **previous** finding —
   silently overwriting whatever case file content is currently showing for the finding the user
   actually has selected now, a few hundred milliseconds after they moved on. `previewing` is also
   a single module-level boolean shared across every finding, so the stale timeout also flips it
   back to `false` and can prematurely mark the *currently* selected finding's own preview
   animation as "settled" (enabling its action button) before that finding's own animation has
   actually finished. This is exactly the "rapid clicking through the queue" edge case the review
   brief asked to trace, and it reproduces with two ordinary clicks.
   **Fix:** capture a request token (e.g. `var token = ++selectionToken;`) at the top of
   `selectFinding`, and inside the timeout check `if (id !== selectedId) return;` before touching
   `previewing` or re-rendering, so a superseded selection's timer becomes a no-op.

3. **The regression matrix — the pillar's signature "proof strip" — is not operable by keyboard
   and barely accessible to screen readers.** In `renderMatrix()` (line 1039), each `<td class="cell">`
   gets only `mouseenter`/`mousemove`/`mouseleave` listeners (line 1077) that show pass/fail/no-
   coverage detail via a floating `#tip` div; the actual semantic content lives in a `title`
   attribute (`td.title = t.name + ": PASS"`, etc.) that browsers only surface on mouse hover
   after a delay, and that most screen readers do not reliably announce for table cells at all.
   No cell has `tabindex`, and there's no `aria-describedby` linking cells to their meaning. A
   keyboard user or screen reader user gets a grid of colored/patterned `<span>` glyphs (good —
   shape-coded, not color-only) but literally no way to learn which test each glyph refers to or
   whether it passed, failed, or was never run, for the one screen in this whole three-dashboard
   set whose entire premise is "the matrix can veto the field" (PRD §3, code pillar).
   **Fix:** give each `<td>` `tabindex="0"` plus a visible or `aria-describedby` text equivalent of
   what's currently only in `title`/the mouse tooltip, or make the row-click behavior (`focusNode`)
   reachable per-cell via keyboard too.

4. **`aria-live="polite"` on the entire proof section causes a full-table re-announcement on
   every selection.** Line 547: `<div class="proof" id="proofSection" aria-live="polite">`. This
   `<div>` contains the whole `<table class="matrix">`, and `renderMatrix(f)` (called from every
   `selectFinding`) does `clear(table)` and rebuilds the full `<thead>`/`<tbody>` from scratch —
   inside a live region. Every time a user picks a different finding from the queue, a screen
   reader is liable to queue up an announcement of the entire regenerated table's text content
   (every call-path row, every test name, every "PASS"/"FAIL"), rather than something targeted
   like "gate updated to review." That's the opposite of what a considerate live region should do.
   **Fix:** move `aria-live` off the whole section and onto a small, purpose-built status string
   (e.g. "Gate: REVIEW — 1 untested path" injected into a dedicated `aria-live` node), leaving the
   matrix itself as ordinary, non-live table markup.

5. **`prefers-reduced-motion` is snapshotted once at script load, not re-checked live.** Line 601:
   ```js
   var reduceMotion = false;
   try{ reduceMotion = matchMedia("(prefers-reduced-motion: reduce)").matches; }catch(e){}
   ```
   This is a one-time read with no `change` listener. Contrast with `infra-patching/index.html`,
   which wraps the same check in a `reduceMotion()` function re-evaluated on every call site. If a
   user (or an automated accessibility test toggling the OS setting mid-session, which is exactly
   how "verified... in headless Chromium" claims are often produced) flips the setting after the
   page has loaded, `STAGGER` and the revert-animation branch in `animateRevert()` keep using the
   value captured at load and will not respect the change until the page is reloaded — even though
   the CSS-side `@media (prefers-reduced-motion: reduce)` rules react immediately, so the page ends
   up half-respecting the setting.
   **Fix:** either re-read `matchMedia(...).matches` at the point of use (as infra-patching does)
   or attach a `change` listener on the `MediaQueryList` and update the module-level flag.

---

## Summary table

| File | Worst finding | Category |
|---|---|---|
| identity | Case file has no close control on desktop at all | Correctness / a11y |
| infra-patching | Double-click on revert duplicates the revert and the ledger entry | Correctness (race) |
| code-patching | Epicenter is entirely unreachable by keyboard | Accessibility |

Common thread across all three: **every keyboard/ARIA claim needs to be re-verified by actually
tracing `addEventListener` calls, not by reading the markup that looks right next to it.** Two of
the three files get this wrong in ways a quick keyboard-only pass (no screen reader needed) would
have caught in under a minute per dashboard.
