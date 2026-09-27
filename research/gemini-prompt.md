# Prompt given to Gemini (Deep Research)

Self-contained version of the research request, written 2026-09-26. Interviewee names were replaced
with roles. Delete the appendix for a run that is independent of our own ideas.

```markdown
# Mission: find the security research that proves remediation is the real bottleneck

## Who we are
Skylayer is an early-stage cybersecurity startup. We need one research project, or a
small set of them, that cuts through the noise of the security industry and gives
real, technical evidence for our thesis. Your job is to THINK OF and research these
projects, not implement them. We will implement.

## Our thesis
Organizations can't remediate security issues fast enough. That is not because they
don't know what to fix, and not because the fix is hard. It is because nobody can
prove a change is safe. The fix might break production, someone owns that blast
radius, so the change waits.

We want to produce that proof (model dependencies, predict blast radius, gate by
confidence, revert when wrong) and then act on it automatically.

Why now: the gap between disclosure and exploitation has collapsed, but the time it
takes to make a change safely has not moved. (Mandiant M-Trends 2026: average
time-to-exploit is -7 days, meaning exploitation before a patch exists. Verizon
DBIR 2025: median time to mass exploitation of edge-device KEVs is 0 days, and only
about 54% are ever fully remediated. Please verify these figures yourself.)

Our four beliefs:
1. Detection is covered; action is not.
2. The blocker is impact uncertainty, not speed, prioritization, or lack of tooling.
3. Proof is the moat; the action is the product.
4. Trust is earned through reversibility: start where being wrong is cheap.

We have not decided where to start: (A) network and firewall configuration, or
(B) OS, package and container patching. The evidence so far leans toward B.

## What 40 discovery calls did and did not show
- Supported: eleven unconnected security leaders said without prompting that fear
  of breaking production blocks fixes. A CIO+CISO at an FDA-regulated medical-device
  company: "When we remediate, what could potentially break." A manufacturing CISO:
  a bad fix that stops a line costs "hundreds of thousands of dollars a minute."
- Supported: "We have solutions that identify vulnerabilities, but none that
  actually take action."
- NOT supported: belief 2 has zero evidence. Several of the same people named
  speed, volume and prioritization as the blocker instead. Nobody showed that impact
  uncertainty specifically causes the delay.
- No hard numbers: no time-to-fix, backlog size or breakage rate from any real
  environment.
- Unknown whether blast radius can be predicted at all. This is the proof mechanism
  everything depends on.
- Many CISOs say they would allow "read-only only". Unknown whether enterprises will
  ever let a tool act.
- Risk to the thesis: prior research found coordination delays dominate, and major
  breach reviews (Equifax, Log4j) point to "we didn't know the asset existed" rather
  than fear of breakage.

## Examples of research that cut through the noise
1. A recent viral LinkedIn post: "We found 179 publicly reachable MCP servers. 147
   were wide open. No login, no token. Root shell access on production servers,
   plaintext cloud/GitHub/Stripe credentials, SQL against production data. No 0-day,
   no jailbreak. If we could find them, attackers can too." It worked because it had
   one crisp number, no exploit, a reproducible method, and a clear implication.
2. Air Security's research, which we want you to read and learn from:
   https://www.air.security/blog-posts/anthropic-scanner

Ours does not need to look like these, but it must be that technical and that
interesting.

## Hard rules
- Technical evidence only. No interviews, surveys or conversations.
- No honeypots, no fake or simulated environments, no synthetic data. Only real
  artifacts, real systems, and public or legally obtainable data (public datasets,
  FOIA/public-records requests, purchased data, research-access programs, data
  partnerships under agreement).
- Fully legal and ethical: no unauthorized access, no exploitation, nothing beyond
  what a normal public visit does to systems we don't own, respect terms of service.
  Prefer existing research datasets over running our own scans. Report in aggregate;
  never name or expose specific vulnerable organizations. No exploit details.
- Feasibility is NOT a filter. Big, expensive, multi-year or partnership-dependent
  ideas are welcome. Just say honestly what each would take.
- Design every study so it COULD fail. If the result could disprove belief 2, a
  positive result becomes far more credible. We want to know the truth either way.

## What "best" means (rank on these)
1. Thesis proof: does it produce real evidence for belief 2 (impact uncertainty
   CAUSES delay) and/or show the proof mechanism is possible? Showing that delay
   exists is not enough; we want designs that isolate the cause. Examples: hold the
   fix constant and vary only its risk or the proof required; natural experiments;
   before/after a public breakage event; placebo comparisons; within-organization
   comparisons.
2. Noise-cutting: one surprising, reproducible number that CISOs, press and investors
   would share.
3. Rigor: survives a hostile expert looking for confounds.
4. Novelty: check prior art. Say what has already been published and how ours
   differs.
5. Fit: bonus if it fits patching (wedge B), doubles as a demo of our product, or is
   relevant to regulated industries such as medical devices.

## How to work
1. Research broadly. Cover at least these angles:
   - internet-scale passive datasets (DNS, certificate transparency, TLS/HTTP, BGP/RPKI)
   - package ecosystems and Linux distributions (per-version downloads, security
     trackers, backports, yanked releases)
   - cloud, infrastructure-as-code and managed services (forced upgrades,
     extended-support pricing)
   - legal and regulatory records (SEC, courts, regulators, FOIA, FedRAMP, NERC CIP,
     CISA directives)
   - change-induced outages and public postmortems
   - vendor-published patch materials (advisories, known issues, fix availability
     per version line)
   - AI: it shrinks the time to write exploits and fixes, but does it shrink the time
     to prove a fix safe?
   - whether blast radius can be predicted (public pre-registered forecasts,
     backtests)
   - aggregate links between real breaches and fixes that weren't applied
   - regulated and physical systems (medical devices, OT/ICS, automotive OTA,
     aviation, elections)
   - telemetry partnerships (patch-management vendors, change-ticket systems,
     vulnerability-management vendors, insurers)
   - economics (prices paid to avoid change, procurement data, disclosures)
   - open-source maintainer behavior
   - fleet-wide version data (browser, OS and mobile patch-level share)
   - network/firewall configuration (give wedge A its best shot)
   - wildcards and stunts nobody else would think of
2. For each angle, come up with several ideas. Check that the key data sources really
   exist and are accessible, and look for prior art.
3. Attack your own ideas as a skeptic. Has it been done? Does the data exist? Is it
   legal? What confound would let a critic dismiss it? Drop or fix the weak ones.
4. Take your top 3 and try to beat them: combine them, go 10x bigger, find a cheaper
   version, design a sharper test that could disprove belief 2, argue from the
   board/CFO view and from the on-call engineer's view.
5. Deep-dive the final top 5.

## Deliverable
A. Top 5, ranked. For each:
   - Name and one-line hypothesis
   - The headline it would produce (use X/N placeholders; never invent numbers)
   - Which belief or gap it tests, and exactly how it isolates impact uncertainty
     as the cause (or honestly, that it doesn't)
   - Data sources: named datasets, APIs or partners with links, each marked
     verified / unverified / needs agreement
   - Method: concrete technical steps
   - Pre-registered hypotheses, and what result would support vs disprove the thesis
   - A 6-week first version, and the full version
   - Prior art and why this is new
   - Legal and ethics checklist
   - Cost, time, access needed, and the biggest risks and confounds
B. Up to 15 runner-up ideas, one or two lines each.
C. A kill list: ideas that sound good but shouldn't be done, and why.
D. A recommended sequence of 2–4 studies and the reasoning.
Cite sources with links. Flag anything you could not verify. Never make up statistics.

## Appendix (optional): ideas already on our list
Go beyond these, or propose a clearly better version and say which one it improves.
- Dependabot/Renovate security PRs on GitHub: time to merge when CI passes vs fails,
  reverts of security bumps; plus upgrading real dependent projects to the fixed
  version and running their own tests.
- Internet-wide patch decay on edge devices, tracking rollbacks and forced upgrades
  to a newer version line.
- A census of vendor patches that caused regressions (Windows known issues, PAN-OS
  hotfixes, Ubuntu "regression" notices).
- Container images and Helm charts with fixes available but not applied.
- "Fear Tax": teams paying cloud providers extended-support fees to avoid an upgrade,
  then what happens at forced-upgrade deadlines.
- "Qualification Clock": how long industrial and medical vendors take to approve the
  same Microsoft patch that laptops install on day 0.
- "Safe But Stuck": domains that left DMARC, CSP or MTA-STS in test mode for years,
  plus checking whether enforcing would break anything.
- "Burn Effect": after a public breakage, does adoption of the next security fix slow?
- "Patch Weather": a public, pre-registered forecast of which updates will regress,
  scored monthly.
- Ransomware victims linked, in aggregate, to fixes that had long been available.
- FedRAMP "can't patch, it would break" exceptions checked against what happened
  when the patch was eventually applied.
```
