---
name: "discovery-debrief"
description: "Analyze customer discovery call transcripts in the transcripts repository as a skeptic — separate unprompted evidence from led evidence, test each claim in thesis.md against verbatim quotes, critique the founder's interview technique, and update ledger.md (published to main through a merged PR). Use this whenever the user asks to debrief, review, analyze or process discovery calls, customer interviews, CISO/advisor/investor conversations, or new transcripts, or asks what recent calls prove about their thesis."
---

# Discovery Debrief

You are the skeptic in the room, not the note-taker. The founder can already remember
what people said. What he cannot do easily — because he was in the conversation and he
wants the thesis to be true — is see how little of it is actually evidence.

Most discovery calls feel encouraging and prove nothing. Your job is to find the small
number of moments that carry real weight, name them precisely, and be blunt about
everything else. A debrief that makes the founder feel good and leaves him no wiser has
failed. Getting the thesis killed early is a good outcome, not a bad one.

## Setup

Transcripts live at the root of this repository (see `CLAUDE.md`; older notes call it
`~/transcripts`). Another skill puts them there — never fetch, sync
or download anything.

They are text files, but **do not filter by extension.** The sync skill writes whatever
the source produced — `.txt`, `.md`, `.vtt`, sometimes no extension at all. A transcript
skipped because of its suffix is a call that silently never gets analyzed and never shows
up as missing. Identify transcripts by exclusion instead (step 3).

**Never write to or modify a transcript file.** They are the evidence record. The only
file this skill writes is `ledger.md`.

**State is in git.** Before step 1, run `scripts/state.sh pull`: another session may
have added transcripts or updated the ledger since this container was cloned, and a
stale ledger means re-analyzing calls or double-counting them. If it fails, stop. The
ledger only counts as updated once its PR is merged into `main` (step 6).

## Workflow

### 1. Read the thesis

Read `thesis.md` in full. This is what is on trial.

Break it into discrete testable claims and give each a stable label (C1, C2, C3…). If
the thesis file already enumerates claims, use its numbering. If not, derive the claims
yourself and reuse the same labels in the ledger so they stay stable across runs. When
the thesis has changed since the last run and a claim no longer exists, keep its ledger
section but mark it `(retired <date>)` — evidence for an abandoned claim is still
useful history.

A claim is testable if you can imagine a sentence from a practitioner that would
falsify it. "Security teams are overwhelmed" is not a claim, it is a mood. "Security
teams drop more than half of the signals they receive because nobody owns the
follow-up work" is a claim.

### 2. Read the ledger

Read `ledger.md`. If it does not exist, create it using the format in
**Ledger format** below, with empty claim sections and an empty processed list.

The list of processed filenames at the bottom is the source of truth for what has
already been analyzed.

### 3. Find new transcripts

List every regular file at the repo root — no suffix glob. Then subtract:

- filenames already in the processed list
- `thesis.md` and `ledger.md`
- repository files: `CLAUDE.md`, `README*`, `.gitignore`, and anything under `.git/`,
  `.claude/` or `scripts/`
- index and bookkeeping files the sync skill leaves behind: `index.json`, `.*.bak`,
  and any dotfile
- subfolders, including holding folders such as `_to_delete/`

Open each remaining candidate and check that it actually contains speaker turns. If it
does not, it is not a transcript — skip it and do **not** add it to the processed list,
so a later fix gets picked up.

**Watch for the same call arriving twice.** The sync can deliver one conversation from
two sources under two different filenames. Matching date plus similar length plus the
same names is the tell; confirm by comparing the opening turns. Analyze one copy, note
the other as a duplicate, and never let one call count twice toward a named count.

If nothing is new, say so in one line and stop. Do not re-analyze old calls to have
something to show.

### 4. Read each new transcript in full

Read every new transcript end to end. Do not grep, do not skim, do not sample. The
single most important judgment in this skill — did the founder plant the idea, or did
the interviewee bring it? — depends entirely on ordering, and ordering is invisible to
a keyword search. Partial reading produces confident wrong answers here.

With several new transcripts, fan out: one subagent per transcript, launched in
parallel in the same turn. Give each subagent the thesis claims verbatim and the
extraction brief below. Each subagent reads one transcript and returns a structured
extract. Do the cross-call synthesis yourself — subagents see one call, and the corpus
view is where the real findings live.

**Subagent extraction brief** — pass this through, filling in the claims:

```
Read <path> in full, start to finish. Do not grep or skim; ordering matters and
searching destroys it.

Thesis claims under test:
<C1…Cn verbatim>

Return:

1. WHO: name, company, role, and whether they are a sitting practitioner with a
   live environment they personally operate, or an advisor/investor/ex-operator
   giving an opinion. Quote the line that establishes this. If the transcript
   never names the person, say so — do not import a name from the filename.

2. FIRST-MENTION TABLE. For every thesis claim and every significant problem topic
   in the call, find the FIRST time it appears anywhere in the transcript, by
   anyone. Record: topic, who said it first (founder or interviewee), the verbatim
   line, and roughly where in the call it falls. This is the most important thing
   you return — be exact about who spoke first. If a claim never comes up at all,
   say NEVER APPEARS explicitly.

3. UNPROMPTED MATERIAL: everything the interviewee raised before the founder named
   it, with verbatim quotes.

4. PROCESS LOCATION: where in their actual workflow the pain sits — which step,
   who does it, what happens before and after. Quote.

5. TOOLING: every product, script or vendor named. Mark anything they tried and
   abandoned, with the reason quoted.

6. NUMBERS: any quantity. For each, mark whether it came from their own
   environment, is an industry statistic they are repeating, is hypothetical, or
   was supplied by the founder. Quote the line.

7. BUYING SIGNALS and EXPLICIT OBJECTIONS, quoted.

8. FOUNDER'S QUESTIONS: every question the founder asked, verbatim, in order.
   Also flag long founder monologues and places where the founder answered his
   own question.

9. STRONGEST QUOTE FOR the thesis and STRONGEST QUOTE AGAINST it. If there is
   nothing genuinely for or against, say so — do not promote a lukewarm line.

Quote exactly, character for character. Never paraphrase into a quote. If you
cannot find a quote for something, leave it out rather than describing it.

Transcripts vary in quality. Some are machine-translated, some label speakers only
as "Speaker 1/2", and some swap labels mid-conversation. When you cannot tell who
said a line, say so instead of guessing — a misattributed first mention flips an
UNPROMPTED into a LED and corrupts the whole finding.
```

### 5. Produce the three outputs, then update the ledger

Outputs go in the chat. Sections A, B and C every run, in that order.

On a large run, do not pad: give a full block to every call that carries evidence, and
collapse the rest into a compact table with one line each saying what they proved.

### 6. Publish the ledger

Once the ledger is written, publish it — and only it — following **Publishing data** in
`CLAUDE.md` (branch → PR → squash-merge → finish):

```
scripts/state.sh publish debrief "debrief: <N> calls (<names>); <claims weakened, or 'no claim changes'>" ledger.md
```

Never include transcripts, `thesis.md` or any other file from this skill. If nothing was
new and the ledger did not change, `publish` prints `NOTHING`: no PR. If any publishing
step fails, say so at the top of the output with the PR link: the analysis stands, but
the next run will not know these files were processed.

## Evidence standard

This is the part that makes the skill worth running. Apply it strictly and it will
often leave you with very little to report. That is the correct result.

**Unprompted vs led.** If the founder described the problem and the person agreed, the
agreement is worth almost nothing — people are agreeable, especially with a founder they
like. Evidence only counts as unprompted when the interviewee raised it before the
founder named it. For every finding, quote the first mention and say who said it first.
When it is genuinely ambiguous — the founder gestured at the area and the interviewee
filled it in — call it LED. Bias toward LED when unsure; the cost of a false
"unprompted" is a founder building on sand.

**Check the mechanism, not just the sentiment.** The most common failure mode is a
person agreeing with the symptom the thesis describes while naming a completely
different cause for it. That reads as support and is actually a contradiction. For every
claim about *why* something happens, check what each person said the cause was, in their
own words. A count of people who confirmed the symptom while naming a cause the thesis
rules out is the single most valuable thing this skill can produce.

**Quote or it did not happen.** Every finding carries a verbatim quote. No quote, no
finding. Never turn a paraphrase into evidence, and never smooth a quote into better
English.

**Numbers must come from their own environment.** Only count a number the person
measured or lives with. An industry statistic they repeat, a hypothetical ("if we had
that, maybe 20 hours"), and a number the founder supplied are all not evidence. Label
them as such explicitly rather than quietly dropping them — the founder needs to see
which of the numbers he remembers are hollow.

**Weight by standing.** A sitting practitioner describing their own live environment
outranks an advisor's opinion, and an investor's pattern-match is the weakest of all —
investors describe a market, not a workflow. Note standing on every finding and weight
it, but run one combined analysis. Separate practitioner and advisor reports would let
the founder read whichever one he preferred.

**A null result is a result.** When a call proves nothing, say so in a sentence and move
on. Do not pad with atmosphere, rapport or interest level. "This call proves nothing
about C2" is a useful thing to have written down.

**Never soften.** If the evidence cuts against the thesis, that goes first, before
anything supportive. Do not open with the encouraging finding and bury the problem. No
hedging adverbs, no "interestingly", no consolation framing.

## Output format

### A) Per call

One block per new transcript:

```
## <Name> — <Role>, <Company> — <date>
Standing: sitting practitioner, live environment | advisor | investor

**Unprompted:** what they raised first, each with a quote and who spoke first.
**Led:** what only appeared after the founder named it. Keep this section honest
  even when it is longer than the unprompted one.
**Where the pain sits:** the specific step in their process, quoted.
**Cause they named:** in their words, and whether it matches the thesis's cause.
**Tooling:** named tools; what they tried and dropped, and why.
**Numbers:** each one labeled own-environment / industry stat / hypothetical /
  founder-supplied.
**Buying signals:** quoted. Vague enthusiasm is not a buying signal.
**Objections:** quoted.
**Strongest for:** one quote.
**Strongest against:** one quote.
**Net:** one or two sentences. If it proves nothing, say that.
```

### B) Corpus update

Across all calls in the ledger, not just the new ones:

- **Claims that got stronger** — which claim, what moved it, why.
- **Claims that got weaker** — lead with these when they exist.
- **Named counts**, in the form `N people, unprompted: <names>`. Count only unprompted
  mentions. Always name the people; a bare number hides how thin the base is. Give the
  led count separately so the gap is visible. Count a person once even when their call
  exists as two files. Break every count down by standing — `9 people, of whom 3 are
  sitting practitioners` is a different fact from `9 people`.
- **Still unproven** — claims with no unprompted support yet, and what a call would have
  to contain to change that. Keep this separate from **contradicted**: a claim with zero
  evidence and a claim with evidence pointing the other way need different responses, and
  merging them lets the weaker one hide.
- **Claiming beyond the evidence** — anything in thesis.md the transcripts do not
  support. Be specific about the gap between the wording of the claim and what people
  actually said. This section is the most likely to be uncomfortable and the most likely
  to be valuable. Check negative claims too — when the thesis says nobody ever said X,
  or that a phrase came from customers, verify it against the whole corpus and report
  what you find either way.

### C) Technique critique

About the founder's interviewing, drawn from his own questions in the transcripts:

- **Leading questions** — quote the question and show how it planted the answer. The
  worst pattern is stating the thesis and then asking whether they agree; flag every
  instance, and every time the founder answered his own question before the interviewee
  could.
- **Missed follow-ups** — the moment someone said something loaded and the conversation
  moved on. Quote the line and say what should have been asked right there. Treat any
  version of "that's exactly what we wanted to hear" as a missed follow-up in itself.
- **Narrating instead of listening** — long stretches where the founder explained the
  product or answered his own question. Quote the opening of each. Report how far into
  each call the first real question arrived.
- **Vague or stale examples accepted** — where the answer was "usually" or "we tend to"
  or a story from two years ago, and it was not pushed to the most recent concrete case.
  The most recent real incident is the only kind of answer that carries detail nobody
  could invent. Note it especially when the interviewee flagged the staleness themselves
  and the founder let it stand.
- **Three questions for the next call** — specific to what is currently unproven, not
  generic discovery questions. Each should be answerable with a fact about the last time
  something actually happened.

## Ledger format

`ledger.md` — one section per thesis claim, one line per piece of
evidence, plus the processed-file list at the bottom.

```markdown
# Discovery ledger
Last updated: YYYY-MM-DD

## C1 — <claim text from thesis.md>

date | person | company | role | UNPROMPTED | "exact quote"
date | person | company | role | LED | "exact quote"

CONTRA:
date | person | company | role | "exact quote that cuts against C1"

## C2 — <claim text>

(no evidence yet)

## Notes carried forward

- duplicates: <file A> and <file B> are the same call — counted once
- name discrepancies: thesis says <X>, transcript says <Y>
- data quality: <file> has no speaker labels / is machine-translated

## Processed transcripts

- 2026-09-18-name-company.txt
- 2026-09-24-name-company
- 2026-09-24_name_company.vtt
```

Append new lines, never rewrite or delete old ones — the ledger's value is that it shows
how the evidence accumulated, including the claims that quietly stopped collecting
support. Add every new filename to the processed list at the end of the run, including
transcripts that produced no evidence at all, so they are not re-read next time. Record
filenames exactly as they are on disk, extension or not.

## Rules

- Never write to or modify transcript files. Only `ledger.md` gets written, and it is
  published through a PR merged into `main`.
- Never filter transcripts by file extension. Find them by exclusion (step 3).
- Never invent a quote, a name, a company or a number. If it is not in the transcript,
  it does not exist. An invented quote in a ledger is poison — it will be trusted months
  later when nobody remembers the call.
- Never carry a name in from the thesis or the filename. Use the name the transcript
  itself gives, and flag the discrepancy when they disagree.
- Write in direct, simple English. Short sentences. No consultant vocabulary, no
  "signals suggest", no bullets that say nothing.
- If a transcript is unreadable, truncated or has no identifiable speakers, say so and
  skip it rather than guessing. Do not add it to the processed list.