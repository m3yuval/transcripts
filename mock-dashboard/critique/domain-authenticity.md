# Domain authenticity & guardrail critique — identity / infra-patching / code-patching mocks

Reviewed: `mock-dashboard/identity/index.html`, `mock-dashboard/infra-patching/index.html`,
`mock-dashboard/code-patching/index.html`, against `PRD.md` §1–3 (core objects, UI-safe copy) and
spot checks against `ledger.md` and root transcripts.

## Verdict

**No guardrail violations found.** I grepped all three shipped `index.html` files for every real
interviewee name and every real company name in the brief (Hiltz, Litvin, Asaf, Chris, Heather,
Dutton, Muller, Schwartz, Andres, Carlson, Matturro, Bryski, nference, Anumana, Wistia, Elastic,
Cava, FICO, Sumitomo, Commvault, Rogo, Trinetics, First Quality, Nestlé, Stanford). The only hits
were substring false-positives (`ml-inference` matching `nference`) inside `infra-patching`, which
is a fake service name in mock data, not the real customer nference/Anumana. Every on-screen quote
in all three files traces back word-for-word (or is a direct further-trim of) PRD.md §7's
UI-safe anonymized copy, correctly attributed to role-only citations ("CISO, cloud-native software
company," "Head of security, mid-size software company," etc.) — none of it is a verbatim
transcript quote re-attached to a name. On guardrail compliance specifically, the developers did
the right thing.

That is the only thing this review has good news about. The realism and internal-consistency
findings below are real problems and should be fixed before any of these three mocks goes in front
of a security buyer or a technical advisor.

---

## Findings

### 1. `CVE-2026-31337` is a joke number, not a plausible CVE — infra-patching, `pay-gw` finding
File: `mock-dashboard/infra-patching/index.html`, line 354.
```
cve:"CVE-2026-31337", pkg:"openssl", from:"3.0.11", to:"3.0.14",
```
`31337` is "eleet" — a hacker in-joke, not a number the CVE Program hands out. Real CVE identifiers
are sequential allocation numbers with no meaning; a security practitioner will spot `31337`
instantly and read the whole dashboard as unserious, the same way a fake receipt with amount
`$1337.00` reads as fake. This is the single most avoidable authenticity failure in the deck because
it costs nothing to fix.
**Fix:** replace with a boring, plausible number in the same year band as the sibling findings, e.g.
`CVE-2026-30412`. No other change needed — the openssl/heap-overflow framing is fine.

### 2. Fabricated, invalid version string masquerading as a CVE — code-patching, `f6` (axios)
File: `mock-dashboard/code-patching/index.html`, line 700.
```
{ id:"f6", pkg:"axios", from:"0.21.4", to:"0.21.4+cve-3749", repo:"notifications-svc", ... }
```
Two separate problems in one field:
- `0.21.4+cve-3749` is not a real semver string. npm's semver spec allows a build-metadata suffix
  after `+`, but nobody ships `+cve-3749` as a version identifier — build metadata is a build
  number/commit hash, never a vulnerability ID. No real npm registry, lockfile, or dependency-audit
  tool would ever produce this string.
- Unlike every other finding in this file, `f6` has no `cve` field at all — the vulnerability
  reference is smuggled into the fake version string instead. That's an inconsistent data model:
  a practitioner reading this case file sees a version bump with no CVE and a version number that
  looks hand-edited to *contain* a CVE reference, which reads as sloppy rather than illustrative.
- For what it's worth, there *is* a real CVE here to draw from if the team wants the realism:
  axios 0.21.4 → 1.6.0 for the SSRF/proxy-redirect issue (CVE-2023-45857) is real and well known.
**Fix:** either give `f6` a real `cve` field like the other findings (`cve:"CVE-2023-45857"`) and a
plausible target version (`to:"1.6.0"` or a smaller illustrative bump like `"0.21.4"` → `"0.28.0"`),
or drop the CVE pretense entirely and frame it as a plain dependency-freshness bump with no `cve`
key, matching how Chris's own quote frames "this version of this dependency is out of date" (PRD §3
core objects) — but don't do both at once by burying a fake CVE inside a fake version string.

### 3. Test-framework naming convention is wrong for the ecosystems it's attached to — code-patching
File: `mock-dashboard/code-patching/index.html`, lines 644–738 (all `tests` arrays).
Every single test name across all 8 findings uses `ClassName::testMethod` (PHPUnit/pytest/Rust
style), including on findings whose package and repo framing is unmistakably Java
(`jackson-databind`/`billing-api`, e.g. `BillingWorkerRegressionSuite::testQueueDrain`,
`PublicApiV2ContractTest::testCreateInvoiceEndpoint`) and JavaScript
(`lodash`/`checkout-service`, `axios`/`notifications-svc`, e.g.
`CheckoutOrchestratorRegressionSuite::testFinalizeIdempotent`). Real JUnit output never uses `::` —
it's `ClassName.testMethod` (JUnit4) or `ClassName > test method name` (JUnit5/Gradle), and real
Jest/Mocha output is `describe block > it block`, not a `::`-joined pseudo-class name either. Any
engineer who has read a CI log will clock this in two seconds as "written by someone who's only
ever seen pytest." The `::` convention is *correct* only for the genuinely Python findings
(`requests`/`reporting-worker`, `pyjwt`/`auth-gateway`, `urllib3`/`payments-connector`,
`PyYAML`/`data-ingest-pipeline`) — four of the eight are fine as-is.
**Fix:** rewrite the Java-ecosystem test names to dot notation
(`BillingWorkerRegressionSuite.testQueueDrain`, `PublicApiV2ContractTest.testCreateInvoiceEndpoint`,
`InvoiceParserTest.testParseValidPayload`, `WebhookIngestIT.testDuplicateEventIdempotency`) and the
JS-ecosystem ones to a Jest-style label (`CheckoutOrchestratorRegressionSuite > finalize is
idempotent`, `CartSerializerTest > deep-merges arrays`). Leave the four Python ones untouched.

### 4. Identity dashboard's header KPI counts are hardcoded and unfalsifiable — identity
File: `mock-dashboard/identity/index.html`, lines 908–913 and 481–484.
```js
var queue = { auto:4, review:2, blocked:1 };
...
function paintQueue(){ roAuto.textContent = queue.auto; roReview.textContent = queue.review; ... }
```
Compare this to infra-patching and code-patching, where the exact same rail readout is computed
live from the `FINDINGS` array (`FINDINGS.filter(function(f){return f.gate==="auto"}).length`, infra
line 581–583; code line 796–797). Identity has no `FINDINGS` array at all — there is exactly one
rendered scenario (`svc-billing-legacy`, gate = review), yet the header claims 4 auto + 2 review + 1
blocked = 7 items in the queue that never appear anywhere on screen. This is precisely the
off-by/contradiction check the brief asked for: the KPI header and the rendered findings disagree,
and unlike the other two pillars there's no underlying data model to reconcile them against — the
numbers are just typed in. A reviewer who clicks around the identity mock looking for the other 6
items will find nothing, which undercuts trust in every other number on the same screen.
**Fix:** either (a) build a real `FINDINGS`-style array for identity with 7 distinct credential
scenarios and derive the header from it the same way the other two pillars do, or (b) if one
scenario is all this mock needs, make the header honestly reflect that single scenario (e.g. drop
the auto/review/blocked breakdown and show only this credential's own gate state) rather than
implying a queue of items that isn't there.

### 5. Identity pillar ships none of PRD §1.5's specified KPI texture — identity
File: `mock-dashboard/identity/index.html` vs. `PRD.md` §1.5.
PRD.md explicitly calls for five KPI numbers on the identity header: credentials with no owner
acknowledgment (`142`), median time to full containment (`18 min`), revocations without incident
(`97%`), cross-team coordination time avoided (`31 hrs`), and stale/dormant identities auto-flagged
(`58`). None of these appear anywhere in the shipped file (grep confirms zero hits for `142`, `18
min`, `97%`, `31 hrs`, `58`). Instead identity ships a generic confidence/auto/review/blocked rail
that's structurally identical to the other two pillars' rails but with none of the pillar-specific
demo texture the PRD called out as "texture on every screen." Since the Appendix's whole point is
letting the founders "look at all three side by side and recognize the family resemblance," an
identity mock that's visibly thinner on demo numbers than its siblings undercuts that comparison —
it will read as "we ran out of time on this one," not as a deliberate design choice.
**Fix:** add a compact KPI strip (even 3 of the 5 numbers) using PRD §1.5's illustrative figures
verbatim, styled consistently with the infra/code rail readouts.

### 6. Several infra vulnerability blurbs are too vague to read as a real advisory — infra-patching
File: `mock-dashboard/infra-patching/index.html`, lines 358, 371, 382, 395, 408, 420, 433, 446
(`blurb` fields).
Compare `"log4j-core 2.14.1 is present in the auth-worker image but not on the runtime classpath..."`
(specific, technically grounded, matches Mike Hiltz's real example) against
`"python 3.9.7 needs a parsing fix."` (`batch-etl`, line 408) and
`"fluent-bit 1.4.1 needs a log-parsing fix."` (`log-relay`, line 446) and
`"glibc 2.35 needs a buffer-handling fix."` (`db-proxy`, line 395). These three read as filler —
real CVE advisories always name the vulnerable *thing* (a function, a header parser, a specific
protocol path), not just "a parsing fix." A CISO who has read actual NVD/vendor advisories will
notice the log4j and nginx entries were clearly researched and the python/fluent-bit/glibc entries
were not, which makes the dashboard look uneven rather than deliberately varied.
**Fix:** give each of the three vague blurbs one concrete technical detail, e.g. for `batch-etl`:
`"python 3.9.7's tarfile module allows path traversal on extraction; fixed upstream in 3.9.17."` —
doesn't need to cite a real CVE, just needs the texture of one.

### 7. `PyYAML 5.4.1 → 6.0.1` undersells what actually changed — code-patching, `f7`
File: `mock-dashboard/code-patching/index.html`, line 714–724.
The real-world PyYAml story (arbitrary code execution via `yaml.load()` defaulting to the unsafe
loader — the actual reason 5.4 and 6.0 exist as security-relevant releases) is well known to anyone
who has done Python dependency hygiene. The mock's finding is on the right package and roughly the
right version jump, which is good, but the test name `ConfigLoaderRegressionSuite::testSafeLoadRejectsArbitraryTags`
is the only signal that this is *that* vulnerability — the `blurb` field for this finding is missing
entirely (there's no `blurb` key on `f7` at all, unlike every finding in the infra file). A reader
gets the epicenter label (`PyYAML 5.4.1 → 6.0.1`) and the repo/function name but no one-line "why
this matters" text the way every infra finding gets. This is a smaller version of finding #6, but
worth calling out separately because it's a missing field, not just a thin one.
**Fix:** add a one-line rationale surfaced in the case file, e.g. "PyYAML's default loader can
execute arbitrary Python objects embedded in YAML; `safe_load` is enforced only after 6.0.1."

### 8. `CVE-2026-14477` on Python 3.9.7→3.9.18 spans an implausibly large number of point releases for one CVE fix
File: `mock-dashboard/infra-patching/index.html`, line 404.
A single CVE fix is normally addressed in the *next* patch release, not an 11-point-release jump
(3.9.7 → 3.9.18). Real Python security backports look like `3.9.7` → `3.9.8` or `3.9.16` →
`3.9.18` if bundling several fixes, but `from`/`to` spanning that many versions for "a parsing fix"
implies this host has been unpatched for roughly two years, which contradicts the dashboard's own
`gate:"auto"` / `confidence:.99` framing (a host that far behind wouldn't cleanly auto-approve).
**Fix:** either tighten the version gap (`3.9.17` → `3.9.18`) to match a single-CVE story, or if the
multi-version gap is intentional (long-neglected staging host), say so explicitly in the blurb so
the gap reads as a deliberate demo of a stale-staging scenario rather than an error.

---

## Note on what's done well (for calibration, not praise for its own sake)

The `log4j`/"present but not running" finding (infra, `auth-log4j`) and the confidence-gated
auto/review/blocked math in infra and code-patching (computed live from the `FINDINGS` array, not
hardcoded) are the two places where the mock data actually holds up under a practitioner's
scrutiny — they should be the template the identity pillar and the weaker infra blurbs are brought
up to, not the exception.
