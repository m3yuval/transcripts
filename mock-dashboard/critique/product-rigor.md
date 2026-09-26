# Product/PM rigor critique — PRD.md and the built mocks

**Verdict: No.** This is a well-cited research memo wearing PRD formatting — it does evidence
attribution better than most real PRDs, but it ducks the two things a PRD actually exists to
do (make the prioritization call, define what "done" looks like), and the PM never checked the
build against the PRD's own spec, so two of the three dashboards silently dropped the most
concrete, most differentiating content the PRD asked for.

---

## 1. The document never makes the call it exists to make (PRD.md §0, lines 24–27)

**What's wrong:** Section 0 says "the founders should look at all three side by side... and
judge each one" and gives no recommendation. Every pillar section is graded honestly on
evidence strength (infra: strongest cluster by a wide margin; identity: nascent; code:
thinnest), but the document stops one sentence short of the only conclusion that evidence
supports. `thesis.md` already has a decision rule pointing at Option B (infra patching) and
flags that the rule isn't yet met — the PRD doesn't even mention the decision rule, let alone
argue for or against acting on it early.

**Why it matters:** A PM's job on a three-way wedge decision is to have a risk-weighted opinion,
not to hand the founders three folders and a shrug. An investor or a co-founder reading this
would ask "OK, so which one — you clearly think it's infra, why doesn't the doc say so?" A
document that grades its own evidence 9/10 strong, 5/10 nascent, 2/10 thin and then declines to
rank the pillars isn't neutral, it's abdicating.

**Exact fix:** Add a "Recommendation" subsection to §0 that states, in one paragraph: rank the
three pillars by evidence strength AND by feasibility risk (not the same axis — identity's
evidence is thinner but its blast-radius computation is arguably easier than infra's regression
harness), name the pillar the PM would build first if forced to choose, and explicitly address
why that recommendation does or doesn't satisfy the decision rule in thesis.md ("three more
Mikes settles it — status NOT MET"). If the PM genuinely believes founders should decide,
justify that as a call, not silence — e.g. "I'm not recommending because X evidence gap would
make any pick premature" — with the X named.

---

## 2. No success/acceptance criteria anywhere — "wow moments" are adjectives, not specs

**What's wrong:** Every pillar's §6 ("Wow moments") is written as filmable prose ("watch the
graph expand hop by hop," "a screen that makes a CISO wince because they already know the
answer"). There is no line anywhere in the 428-line document that says what a developer needs
to build for the mock to be considered done, or what a founder should be able to click through
to confirm it's done. Compare to the KPI sections, which at least commit to numbers.

**Why it matters:** This is exactly why the build drifted (see finding #4 below) without anyone
catching it — there was no checklist to check against. A real PRD's acceptance criteria are what
let someone other than the PM tell a build apart from a miss. "Should evoke a wince" is not
verifiable by anyone; "the graph must show the epicenter expanding through at least 3 named hops
(AWS account → Secrets Manager → GitHub) with a live reachable-asset counter" is.

**Exact fix:** Under each pillar's §6, add 3–5 bullet acceptance criteria phrased as testable
statements ("clicking [X] must show [Y]; absence of [Y] is a fail"), one per wow moment, so a
QA pass (or the founders themselves) can grade the build against the spec instead of vibes.

---

## 3. Built dashboards drop the PRD's most specific "wow moments" and the PM never caught it

**What's wrong:** Cross-checking `identity/index.html` against PRD §1.6: wow moment #1 (recursive
blast-radius animation naming AWS → Secrets Manager → GitHub, with a running "assets reachable"
counter) is not in the file — there is no "Secrets Manager" or "GitHub" string anywhere in
`identity/index.html`. Wow moment #2 (the 30-accounts/100-keys containment console, grouped by
owning team, with a "coordinate revocation" button) is also absent — no "30" or "100" anywhere
tied to accounts/keys. Wow moment #3 (the "ghost-account panel," a list titled "retired — but
still active") is likewise absent. What got built instead is a generic single-credential gate
(auto/review/blocked counters, one "ci-bot-token-central" example) — a materially less specific,
less evidence-grounded screen than the PRD spec'd. Same pattern in `code-patching/index.html`:
PRD wow moment #4 ("a frank 'this is early' empty state... so nobody mistakes the mock's
confidence for validated evidence") — arguably the single most important honesty device the PM
designed for the thinnest pillar — never made it into the build.

**Why it matters:** This is the PRD's own stated point of the whole exercise (§0: "the founders
should look at all three side by side and recognize the family resemblance") undermined by the
fact that the identity mock doesn't demonstrate the one scene the PM said was "the single most
concrete, filmable incident-response story in the whole evidence base." If a founder or investor
clicks through expecting the Asaf story staged on screen and instead gets a generic gate queue,
the mock has failed at its actual job, and nobody signed off on that substitution. A PM who writes
detailed wow-moment specs and then doesn't check the build against them isn't reviewing, they're
just writing prose that gets read once.

**Exact fix:** Before calling any pillar done, the PM walks each built dashboard against its own
§6 checklist (once #2's acceptance criteria exist, this is mechanical) and either (a) gets the
dev agent to add the missing scene, or (b) writes an explicit "spec deviation" note in the PRD or
README stating what was cut and why. Silence is not an option here — right now the deviation is
undocumented and undiscoverable without diffing spec against code by hand, which is what this
critique had to do.

---

## 4. KPI numbers are not differentiated across pillars — they're the same metric copy-pasted with a new noun

**What's wrong:** "Cross-team coordination time avoided this month: 31 hrs" (identity §5),
"Engineer-hours recovered this week: 26 hrs" (infra §5), and "Engineer review hours saved this
week: 14 hrs" (code §5) are the same Matturro "hours back" framing, restated three times with
different numbers and no explanation of why 31 vs. 26 vs. 14, or why one is "this month" and the
other two are "this week." Likewise "% auto-remediated safely, zero incidents: 89%" (infra) and
"Regression-suite pass rate on generated fixes: 98.6%" (code) measure conceptually different
things (safe-automation rate vs. test-pass rate) but read, on a KPI strip, as interchangeable
"our system is basically always right" numbers. The PRD's own framing note says these are
illustrative demo data — fine — but "illustrative" doesn't excuse metrics that don't actually
help a founder tell the three pillars apart, which is the doc's stated purpose for building all
three.

**Why it matters:** A real exec skimming three KPI headers should immediately see what's
structurally different about each pillar's economics (identity's cost is coordination overhead
across teams; infra's cost is regulatory/change-control friction; code's cost is developer review
time) — but three near-identical "hours saved" tiles obscure that instead of surfacing it. This
is a missed opportunity the PM should have caught: the whole point of KPI selection is to make
each pillar's story legible at a glance, and right now all three tell the same story with a
different number bolted on.

**Exact fix:** For each pillar, replace at least one of the generic "hours saved" metrics with a
KPI that only makes sense for that pillar's actual owner-fragmentation problem: e.g., for
identity, "teams that had to sign off on last month's revocations, median 3.2" (dramatizes
Asaf's cross-team coordination point, which is identity's actual differentiator per the PRD's own
§1.1); for code, "% of fixes where the generated test suite caught a behavior change before
merge" (dramatizes the Cognition-style proof mechanism, which is code's actual pitch per §3.3,
not a generic hours metric).

---

## 5. "Thin evidence" pillars get a disclaimer, not a strategy

**What's wrong:** The Appendix (line 423) says "Do not let the identity or code mockups imply
more validated process than the transcripts support" — twice, per the doc's own count. That's a
guardrail against overclaiming, not a strategy for making a thin pillar's mock feel credible on
its own terms. The one genuine strategic idea in the whole document — code's wow moment #4, the
internal-facing "this is early" empty state that turns thin evidence into an honest feature
rather than a hidden weakness — is (a) only in the code pillar, not identity, which has the exact
same evidence problem, and (b) never made it into the actual build (see finding #3).

**Why it matters:** Telling developers "don't overclaim" produces mocks that either quietly
overclaim anyway (because nothing operationalizes the warning) or feel thin and unconvincing with
no mitigation. A real PM strategy for a thin pillar is not "disclaim harder" — it's things like:
lean on a stronger *adjacent* analogy explicitly and visibly (code pillar could show the
Cognition analogy on-screen as the credibility source, not bury it in an evidence-honesty
paragraph only devs read), or scope the mock's confidence claims down to exactly what's evidenced
(identity's mock should visibly claim only "reversible hygiene automation," never suggest
end-to-end autonomous revocation, since that's the one thing nobody in the evidence actually
validated for identity).

**Exact fix:** Give identity the same "this is early" treatment code got in spec (and make sure
both actually ship it, per finding #3). Add one explicit sentence per thin pillar naming which
on-screen claim is allowed by the evidence and which is not, so the dev agent has an
operational rule instead of a mood.

---

## 6. Buyer/owner fragmentation is evidence-cited but never treated as a product risk

**What's wrong:** All three pillars name, in almost identical language, that the person who owns
the blast radius if something breaks is usually not the security buyer (identity: fragmented
across "AWS... source control... DB administrators," §1.1; infra: "usually not security," §2.1;
code: "the engineering team that owns the repo/service," §3.1). This is one of the sharpest,
most consistent findings in the whole evidence base — and Ariel Litvin's specific number (network
sits outside security in ~85% of orgs) is even quoted. But nowhere does the PRD turn this into a
stated risk with a consequence: if the buyer (CISO) doesn't control the blast radius, the CISO
also can't unilaterally approve write access, which means the entire "auto-approved lane" concept
central to all three dashboards may require sign-off from people who were never in the sales
conversation. `thesis.md` itself flags this as open question #3 ("who is the buyer — the CISO...
or the platform owner who gets paged"), unresolved. The PRD imports the evidence but not the
open question.

**Why it matters:** This is a real buyer objection an actual CISO would raise in the room: "I
can't approve your auto-approved lane for anything that touches the platform team's stuff, and
that's most of what you're showing me." If the mock doesn't anticipate that objection — e.g. by
showing the cross-team approval step as a first-class, unavoidable part of the flow rather than a
footnote lane — the demo will get punctured in the first five minutes by exactly the persona it's
trying to sell to.

**Exact fix:** Add a named "Risk" subsection (not just "evidence honesty check") to §0 or each
pillar that states: "the auto-approved lane assumes the security buyer can unilaterally authorize
the action; the evidence says ownership is fragmented in most orgs, so this may not hold outside
identity's narrowest hygiene case." Then require the mock to make the cross-team-approval step
visually unmissable (not a secondary panel) specifically because of this named risk, not just
because Asaf mentioned coordination.

---

## 7. No feasibility risk section for the actual technical bet ("blast radius" computation)

**What's wrong:** The entire mechanism ("model the dependencies → predict the blast radius →
gate by confidence → revert when wrong," line 22) is repeated as the product's spine six times
across the document, but the PRD never once asks whether Skylayer can actually compute it. For
infra, the dependency graph is at least grounded in one practitioner's real workflow (Mike
Hiltz). For identity, the "live graph... expanding hop by hop" (§1.3) requires cross-console
reachability data (AWS, Secrets Manager, GitHub, DB admin) that no evidence in the transcripts
says Skylayer has, can get API access to, or can compute in real time — Asaf's account describes
what an *attacker or human investigator* pieced together by hand, not a system that already
does this. `thesis.md`'s own "Unproven" section says outright: "We don't know what evidence we
can actually produce, or how. Everything else is downstream of this" — this is the single most
important unresolved risk in the whole thesis, and the PRD, which cites `thesis.md` as a source
in line 3, does not surface it once.

**Why it matters:** This is the difference between a demo the founders can safely show a
prospect ("here's the direction, we're building toward it") and a demo that overpromises a
capability nobody has validated Skylayer can build ("here's live cross-console reachability
computed in real time from a single leaked key" — if a technical buyer asks "how do you get that
data," there's no evidenced answer). A PM who has read `thesis.md`'s own "Unproven" list closely
enough to quote it elsewhere in the document (line 39–40, citing C8) but omits the far bigger
"proof mechanism" unproven item is being selectively careful.

**Exact fix:** Add a "Technical feasibility" note to §0, naming the proof-mechanism gap from
`thesis.md`'s Unproven section directly, and add one sentence per pillar's §3 stating what data
access the live version would actually require (cross-account IAM/audit log access for identity,
CI/staging integration for infra, source-control + test-runner integration for code) so the mock
doesn't read as "we already have this working," which nothing in the evidence supports.

---

## 8. Willingness-to-pay gap is in the evidence but absent from the document entirely

**What's wrong:** `ledger.md` C8 states flatly: "NO evidence found in 40 calls. Zero budget
lines, zero approval chains, zero design partners" — and lists direct pushback (BioChrist CISO:
"don't bother chasing... they're cutting everything"; Andrew: "I only want to spend $1,000 a
year, you'd go broke"). The PRD's intro (lines 8–12) is careful to disclaim fabricated *numbers*
on screen, but says nothing about the fact that no pillar has any evidence of willingness to pay
for it at all — this is a different and arguably more important gap than "the MTTR number is
made up," and the document is silent on it.

**Why it matters:** A mock built to help founders pick a wedge should flag, in the same breath as
"which pillar is best evidenced," whether any pillar has better commercial signal than the
others — right now all three are commercially unvalidated and the document never says so, which
lets a reader assume the strongest-evidence pillar (infra) is also the closest to a sale. It
isn't, per the evidence: Mike Hiltz's only concrete offer is "happy to provide feedback," no
budget or pilot discussed.

**Exact fix:** Add one line to §0 or the appendix: "None of the three pillars has any
willingness-to-pay evidence (ledger.md C8) — pain and process evidence should not be read as
purchase-intent evidence, and the strongest-evidenced pillar (infra) is not thereby the
closest to a sale."

---

## 9. Minor: KPI/wow-moment sections cite the same three or four transcripts repeatedly, understating the corpus's actual weak spots

**What's wrong:** Across all three pillars, the recurring citation set is small (Mike Hiltz,
Asaf/a16z, Israel Bryski, Andrew Dutton/Harris Schwartz for read-only, Matturro for hours-back
framing) — reasonable, since those are the strongest quotes, but the PRD never flags that this
concentration means the mock's credibility rests on roughly 5–6 people out of 40 calls, which is
exactly the kind of "is Mike typical" question `ledger.md` C9 already interrogates and leaves
open. The PRD doesn't mention C9 at all.

**Why it matters:** If a founder walks into a room citing this PRD as "grounded in 44 transcripts,"
a sharp investor doing diligence on the underlying evidence (not just the deck) would find that
the load-bearing quotes come from a handful of speakers, one of whom (Mike) the ledger itself
flags as possibly atypical (FDA-regulated, unusually heavy testing burden, "fortunate" to have no
SLA pressure — his own words). The PRD should pre-empt that instead of leaving it to be
discovered.

**Exact fix:** Add one line to the infra pillar's evidence-honesty check (§2, currently the most
confident section in the doc) explicitly acknowledging ledger.md C9's open question about
whether Mike is typical, since infra's entire "strongest cluster" claim leans on him more than
any other single source.

