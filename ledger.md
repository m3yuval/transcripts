# Discovery ledger
Last updated: 2026-09-25

Claims derived from thesis.md (2026-09-25). Labels stable across runs.
UNPROMPTED = interviewee raised it before any founder named it. LED = only after a founder named it.

---

## C1 — The blocker on remediation is inability to prove a change is safe (fear of breaking production), not knowing what to fix

2026-09-24 | Mike Hiltz | nference / Anumana | CIO+CISO (practitioner) | UNPROMPTED | "Obviously there's concern that, especially for vulnerabilities, right? When we remediate, what could potentially break. So being able to test, I have a way to roll back"
2026-09-24 | Mike Hiltz | nference / Anumana | CIO+CISO (practitioner) | UNPROMPTED | "The worry that you're going to break something downstream. So that's why they want human, like engineers involved."
2026-09-10 | Chris | Wistia | Head of Security (practitioner) | UNPROMPTED | "This is too complex, and I'm not comfortable introducing potential breaking changes until we're sure"
2026-09-04 | Heather | ex-Nestle Purina | advisor, NS Advisory | UNPROMPTED | "there are things that you can do to automate some of these things, but nobody trusts it."
2026-09-04 | Heather | ex-Nestle Purina | advisor, NS Advisory | UNPROMPTED | "Because if it fixes it and it causes a line to go down, that's... hundreds of thousands of dollars a minute that we could be losing."
2026-08-28 | ABasu (Amit Basu) | shipping fleet | CIO+CISO (practitioner) | UNPROMPTED | "That will bring down my network, the downtown would be huge. Okay, so then I need a tool that may buy that time."
2026-09-02 | Eli Edelkind | Cava (story is Lowe's, pre-2022) | CISO (practitioner, stale) | UNPROMPTED | "you can't... you can't have business disruption. Ever in a business, right? Like, security doesn't really serve a purpose of security as the one taking down the company, right?"
2026-08-31 | Israel Bryski | Rogo | advisor / vendor-side | UNPROMPTED | "give them the assurance that we can do that in an automated way without breaking anything, without needing you in the loop. That's the next big thing in my book."
2026-09-18 | Yoni (Rplansky) | FICO | Deputy CISO, speaking as advisor | UNPROMPTED | "changing the system in a way that was not successful is something that can be done in the trash... Remediate them with minimum impact. It's difficult. If you succeed in doing that, I think it's like the Holy Grail"
2026-09-22 | Asaf Ezra | a16z | investor | UNPROMPTED | "people are afraid to update stuff, and they don't have time to update it. So if I need to take down a machine to update its let's say infrastructure, the Linux, whatever, then I have a problem, right? 'Cause it takes down my production"
2026-09-22 | Asaf Ezra | a16z | investor | UNPROMPTED | "if you can prove that a patch wouldn't impact the performance or wouldn't impact the functionality, then that's super important"
2026-09-04 | Ariel Litvin | ex-First Quality | retired CISO / would-be competitor | UNPROMPTED | "In production organizations it's very very very very different. That is, you can't make mistakes." (used to argue auto-remediation is impossible)
2026-09-22 | Shawn Anderson | (new role) | advisor | UNPROMPTED | "that's what everybody has a fear of, too. You're pen testing my environment. Is the AI going to go rogue?" (fear of the VENDOR's automation, not own change)
2026-09-15 | Andrew (ex-Nestle, veterinary) | ~1000 hospitals | CISO (practitioner) | UNPROMPTED | "If you think about those kind of hygiene things that will not break stuff, but only do some cleanup, in worst case scenario, you just have to turn something back on that you've turned off." (INVERSE: reversibility is why agents were ALREADY let in)

CONTRA — same witnesses naming speed/volume/tooling as the blocker instead:
2026-09-24 | Mike Hiltz | nference | practitioner | UNPROMPTED | "So I think that's probably our biggest pain point right now, is being able to patch quickly enough, especially with the, the, the volume of vulnerabilities"
2026-09-10 | Chris | Wistia | practitioner | UNPROMPTED | "The reason that I'm not optimistic that it'll work in its current form is because it doesn't move fast enough. I guess if I had to summarize it, it just doesn't move fast enough."
2026-08-28 | ABasu | shipping fleet | practitioner | UNPROMPTED | "I know the vulnerability, but even today, when companies are releasing 500, 600 vulnerabilities, even by knowing, prioritizing them, I still won't be able to fix every one of them in a short time. I need more time."
2026-09-02 | Eli Edelkind | Cava | practitioner | UNPROMPTED | "I haven't seen any holistic solution that makes me happy."
2026-09-18 | Yoni | FICO | advisor | UNPROMPTED | "there are two things that make it difficult. One is the sense of urgency, and the other is priorities."
2026-08-31 | Israel Bryski | Rogo | advisor | UNPROMPTED | "CESA's are going to have to get much faster. in being able to remediate vulnerabilities"
2026-09-08 | Al | (not stated) | advisor | UNPROMPTED | "And they don't know what the problems are, and they don't understand it." (contradicts "they know what to fix")

## C2 — Detection is covered; action is not, and buyers expect vendors to take the action

2026-09-24 | Mike Hiltz | nference | CIO+CISO (practitioner) | UNPROMPTED | "So we have solutions that identify vulnerabilities, but none that actually take action in most cases, right? Because it is a more convoluted process."
2026-09-24 | Mike Hiltz | nference | CIO+CISO (practitioner) | UNPROMPTED | "we're using Prisma Cloud for instance, right? They do a great job at detection and kind of telling you what's going on. But then what do you do with that telemetry? And I think that's where the gap is"
2026-09-24 | Mike Hiltz | nference | CIO+CISO (practitioner) | UNPROMPTED | "I think this is a problem that we expect our vendors to solve."
2026-08-31 | Israel Bryski | Rogo | advisor | UNPROMPTED | "Anything that ends in security posture management means you're telling me shit that's broken that I have to fix. I don't want vendors to tell me things that are fixed. You need to tell me what needs to be fixed. You fix it for me and tell me that you fixed it."
2026-09-09 | Andrew Dutton | Sumitomo Chemical America | regional architect (evaluator) | UNPROMPTED | "it's just the same behaviors that we cannot operationalize, okay?"
2026-09-09 | Andrew Dutton | Sumitomo Chemical America | regional architect | UNPROMPTED | "the tooling that I have now Does not do a good job of really really being able to operationalize those, things"
2026-09-18 | Jerry Carlson | Commvault | Field CISO (vendor-side advisor) | UNPROMPTED | "There is nothing out there today at machine speed that is pulling these together."
2026-09-10 | Chris | Wistia | practitioner | UNPROMPTED | "But in terms of action and due diligence, and discretion, and actual remediation, remediative efforts, it's all still manual."
2026-09-10 | Chris | Wistia | practitioner | UNPROMPTED | "These are the actions I've taken. I need you to review and push the button to say that this is an acceptable fix."
2026-09-22 | Shawn Anderson | (new role) | advisor | UNPROMPTED | "what they're doing is they're... they're telling me I have a problem. Well, okay, great. I can make an assumption, I already have a problem."
2026-08-31 | Andrey Lovchy | SoftClub | CISO (practitioner) | UNPROMPTED | "We didn't look every day, because we needed some time to fix what we saw."
2026-09-01 | Andrew Dutton | Sumitomo Chemical America | evaluator | UNPROMPTED | "We do logging to our SIM, so we can get some basic telemetry, but we haven't set up anything where that, if I see this thing, I can then tell the firewall to block it."

CONTRA — buyers refusing vendor-taken action (C2b):
2026-09-09 | Andrew Dutton | Sumitomo Chemical America | evaluator | UNPROMPTED | "one of the things I've told the vendors is. even when I deploy something, it's only gonna be read-only. I'm not gonna trust to shoot a gun."
2026-09-16 | Harris Schwartz | fractional CISO, ~600-person manufacturer | fractional | UNPROMPTED | "I fought with the client, very hard, and I said, you know, why don't you start off with read-only access, let's see how that goes... But right now, I would not."
2026-08-28 | ABasu | shipping fleet | practitioner | UNPROMPTED | "I would say it is more of a... not production tool, but it is more of a validation tool."
CONTRA — detection is NOT covered:
2026-09-01 | Igor Spektor | ex-Verizon | advisor | UNPROMPTED | "And you guys know, in security, it's all about what do you know and visibility, right?"
2026-09-14 | Daniel Silverman | Stanford | practitioner | UNPROMPTED | "if you can't see it, you can't quantify it or secure it."
2026-09-18 | John Murphy | (not stated) | IR practitioner, role undated | UNPROMPTED | "we're not even looking in the right areas in a lot of places"

## C3 — The blocker is impact uncertainty specifically, NOT speed, prioritization, or absence of tooling

(no evidence for)

CONTRA — see the seven CONTRA lines under C1 plus:
2026-09-16 | Thomas Sinnott | CDW | pre-sales (vendor-side) | UNPROMPTED | "Everybody wants to be able to identify the problem faster, resolve it faster, remediate it faster"
2026-09-16 | Thomas Sinnott | CDW | pre-sales | UNPROMPTED | "they're getting overwhelmed with, with the amount of alerts that they get, and so being able to, diagnose what's important to what isn't, is still a challenge for most of them."
2026-09-16 | Matthew Matturro | Trinetics | CISO (practitioner) | UNPROMPTED | "what are the things they do in a 40-hour week. How much time are they spending? ... And what time would they get back?" (automation selected purely on hours recovered)
2026-09-22 | Nelson | NS Advisory | vendor-side | UNPROMPTED | "I have too many tools. I don't have enough people to even, I have zero clue. don't even ask me about my environment."
2026-09-10 | (unnamed advisor/vCISO) | — | advisor | UNPROMPTED | "Lack of resources lack of tools lack of skills lack of training. It's always a short change."
2026-09-14 | Daniel Silverman | Stanford | practitioner | UNPROMPTED | "we tend to document that stuff in email and Slack... And for us specifically, it's small enough that it's like, well, that's good enough."

## C4 — Proof is the moat; an impact assessment nobody acts on is just a smarter findings list

2026-09-24 | Mike Hiltz | nference | practitioner | UNPROMPTED | "I have a consensus, I can do this without breaking anything. So go ahead and patch it... This is fine to patch, no human intervention, go ahead and push it."
2026-09-24 | Mike Hiltz | nference | practitioner | UNPROMPTED | "If you can see that blast radius, now you know the overall Impact."
2026-09-22 | Asaf Ezra | a16z | investor | UNPROMPTED | "if you are able to create a set of tests that run against the current environment and then you can prove that after upgrading nothing would happen, then I think you can have something here."
2026-09-16 | Matthew Matturro | Trinetics | practitioner | UNPROMPTED | "you have, you've got 15,000 vulnerabilities, you better fix your stuff now. That means nothing." (findings-list half only)

CONTRA — proof is table stakes, not a moat:
2026-09-18 | Yoni | FICO | advisor (board seat at competitor Orb) | UNPROMPTED | "impact analysis, and give the best way to do the remediation. Is this part necessary? Yes... The real question is what is the key differentiation... Zafran or Astellia do, or other organizations that are in the same direction"
2026-09-15 | Andrew (ex-Nestle, veterinary) | ~1000 hospitals | CISO | UNPROMPTED | "There's no mode anymore for cybersecurity companies."
2026-08-28 | ABasu | shipping fleet | practitioner | UNPROMPTED | "I've told my director of operations... that put a tool, I don't care if it works or not." / "If what's or not, it's very difficult to prove, to be very frank with you."
2026-09-22 | Shawn Anderson | — | advisor | UNPROMPTED | (Wiz won on usability, not capability) "it wasn't necessarily their capability, it was the fact that it was so... in their mind, easy to use."

## C5 — Trust is earned with reversibility; start where being wrong is cheap

2026-09-15 | Andrew (ex-Nestle, veterinary) | ~1000 hospitals | CISO (practitioner) | UNPROMPTED | "we did a design partnership with a company that was building AI agents for the security team, and we were able to use them on the identity side to do some kind If you think about those kind of hygiene things that will not break stuff, but only do some cleanup, in worst case scenario, you just have to turn something back on that you've turned off."
2026-08-31 | Israel Bryski | Rogo | advisor | UNPROMPTED | "if you broke something, give me a one click undone on rollback button."
2026-09-24 | Mike Hiltz | nference | practitioner | UNPROMPTED | "So being able to test, I have a way to roll back"
2026-09-16 | Harris Schwartz | fractional CISO | fractional | UNPROMPTED | "why don't you start off with read-only access, let's see how that goes, and then maybe you could move into write access."
2026-09-09 | Andrew Dutton | Sumitomo Chemical America | evaluator | UNPROMPTED | "even when I deploy something, it's only gonna be read-only. I'm not gonna trust to shoot a gun."
2026-08-31 | Israel Bryski | Rogo | advisor | UNPROMPTED | (map of where being wrong is cheap) "if the CISO's using any of the security-native services within AWS, like Security Hub, and GuardDuty, and Detective... that's squarely in the security department. They can do whatever they want with those things." vs "anything that can impact the reliability, the stability of the production environment... that's usually your indicator that the CIO will need to be involved."

## C6 — Wedge A: network / firewall config is the right first wedge

CONTRA (no supporting evidence found in 40 calls):
2026-09-15 | Andrew (ex-Nestle, veterinary) | ~1000 hospitals | CISO | UNPROMPTED | "For me, in my specific CISO role, network is not a big pain... I have a very uncomplex network. And it doesn't present a risk."
2026-09-08 | Mandy Andres | Elastic | CISO (practitioner) | UNPROMPTED | "We don't have a company network. So if you say, you know, let's go plug into your core router... We don't have firewalls specifically."
2026-09-11 | Ray Lewis | Pekin Insurance | security leader (practitioner) | UNPROMPTED | "I am fortunate here that our network is less complex. We have one headquarters."
2026-09-01 | Andrew Dutton | Sumitomo Chemical America | evaluator | LED (asked directly twice) | "The one I just described around networking, or the one I'm about to call into right there? No. No." / "Nope. Nope." / "right now, that's not a priority for me to do anything else in that area."
2026-09-04 | Ariel Litvin | ex-First Quality | retired CISO | UNPROMPTED | "the network team doesn't report to security in -- I want to say -- 85% of organizations."
2026-09-01 | Asaf | (IR / threat research) | responder | UNPROMPTED | "from my experience I haven't yet gotten to see AI-driven on an on-prem network, and not in cloud either."
2026-08-28 | Rajesh Kumar Thangavelu | advisory to Indian banks | advisor | UNPROMPTED | "For the standard operational network security issue, they are not much... interested."
2026-08-31 | Leda Muller | Stanford | practitioner | UNPROMPTED | "I just got pinged by two other people, that are doing network security in the last week." (crowded) + redirected her own top pain to identity offboarding
2026-09-09 | Adam | ex-bank (left 1.5 weeks prior) | practitioner | UNPROMPTED | "doesn't matter what it does on the network side, the identity can go hit all these resources"
2026-09-14 | Daniel Silverman | Stanford | practitioner | UNPROMPTED | "it needs to be an agent or a script running on an endpoint... because I can see what's happening on our servers, but I can't see what's happening anywhere else."
2026-09-22 | FOUNDERS' OWN SUMMARY (Shoval, to NS Advisory) | — | — | — | "that was our first direction... And basically, I'll be honest and say that we got no sense of urgency from CISO around this area. So we took a step back"

## C7 — Wedge B: OS / package / container patching is the right first wedge

2026-09-24 | Mike Hiltz | nference | CIO+CISO (practitioner) | UNPROMPTED | "I think vulnerability patch is probably one of the top ones." / "For misconfigurations in cloud, I think we're in a better spot there."
2026-09-24 | Mike Hiltz | nference | practitioner | UNPROMPTED | (full pipeline) "it really is defining which groups are responsible We go through the process of opening change management or change control tickets. There's testing involved there are Package dependencies that we have to consider"
2026-08-31 | Israel Bryski | Rogo | advisor | UNPROMPTED | "they have to figure out how to patch and do change management and patch management faster." (his own unprompted answer to an open 2027 question)
2026-09-10 | Chris | Wistia | practitioner | UNPROMPTED | "this version of this dependency is out of date. Just go fix it, or get it into stage at least, and then run it through the automated regression testing."
2026-09-22 | Asaf Ezra | a16z | investor | UNPROMPTED | "So patching historically has been the worst of everything, right?" / "it could be a good niche, but I would focus on let's say high and critical vulnerabilities."
2026-09-10 | (unnamed CISO, ReliaQuest customer) | — | practitioner | UNPROMPTED | "you're never going to be able to patch all the vulnerabilities faster. You've got to really focus on what needs to be patch faster."
2026-09-16 | Matthew Matturro | Trinetics | practitioner | UNPROMPTED | "good patch management... patch management hygiene. You're gonna cut down on so much"
2026-09-14 | Daniel Silverman | Stanford | practitioner | UNPROMPTED | "all they can do is say, hey, we're chasing CVEs, we're patching when we can, and that's all they've got. And it's very painful."

CONTRA:
2026-09-04 | Ariel Litvin | ex-First Quality | retired CISO | UNPROMPTED | "take the basic example of Microsoft's Patch Tuesday... No, it doesn't happen. There are SMBv1 and TLSv1 servers and such nonsense running in organizations for years."
2026-09-18 | Yoni | FICO | advisor | UNPROMPTED | (virtual patching is the community's existing answer) "the way of the community to support it needs to be a kind of a direction that is called virtual patching"

## C8 — Willingness to pay: budget line, approval chain, or design-partner intent exists

(NO evidence found in 40 calls. Zero budget lines, zero approval chains, zero design partners.)

CONTRA:
2026-09-15 | Bryan Brown | BioChrist | CISO (practitioner) | UNPROMPTED | "don't bother chasing BioChrist to spend money, because They're, they're cutting everything?"
2026-09-15 | Bryan Brown | BioChrist | CISO | UNPROMPTED | "looking at ripping out most of the security controls that I stood up, because they're slowing things down... they cost money, because they leverage external tools."
2026-09-15 | Andrew (ex-Nestle, veterinary) | ~1000 hospitals | CISO | UNPROMPTED | "what's value mean? Like, it's valuable to me, but I only want to spend $1,000 a year. You would go broke, right?"
2026-09-10 | (unnamed advisor/vCISO) | — | advisor | UNPROMPTED | "we're the shoemaker's children. We have no funding in cyber. We get crumbs and we have to beg for those crumbs."
2026-08-31 | Leda Muller | Stanford | practitioner | UNPROMPTED | "We're not going to be renewing with them... it's just out of our budget." (Darktrace)
2026-09-16 | Matthew Matturro | Trinetics | practitioner | UNPROMPTED (pre-emptive, before any pitch) | "right now, my dance card's full when it comes to design partnerships"
2026-09-01 | Andrew Dutton | Sumitomo Chemical America | evaluator | LED | "right now, that's not a priority for me to do anything else in that area."
2026-09-24 | Mike Hiltz | nference | practitioner | UNPROMPTED | "We'll go out to companies like you to solve these problems, you know?" — BUT the only concrete offer is "Happy to provide product feedback once you get to that point." No budget, no pilot, no timeline discussed. Also pre-flagged: "I just don't have enough hours in the day to do it."

## C9 — Mike Hiltz is typical, not an outlier

CONTRA (both directions):
2026-09-24 | Mike Hiltz | Anumana (FDA medical device) | practitioner | UNPROMPTED | "anytime we make a change like this, even for patching, right, for an FDA approved medical device, it has to go back to the FDA."
2026-09-24 | Mike Hiltz | nference | practitioner | UNPROMPTED | "I'm fortunate, I should say, if I deploy something, it's a research environment. I don't have SLAs with my downstream." (LESS uptime-constrained than typical)
2026-09-15 | Bryan Brown | BioChrist (research pharma) | CISO | — | NEVER mentioned FDA, validation, or regulated change control in 31 minutes. The only other regulated-pharma CISO in the corpus did not volunteer regulatory change friction at all.

## C10 — "AI changed the economics of attacks" (thesis does NOT claim this; tracking only)

PUSHBACK (all UNPROMPTED, all after founders asserted it first):
2026-09-01 | Asaf | IR / threat research | responder | UNPROMPTED | "AI-driven attacks don't necessarily change the attackers' playbook, but they change the tempo."
2026-09-09 | Adam | ex-bank | practitioner | UNPROMPTED | "none of the attacks that are coming in are novel, right? For the most part."
2026-09-15 | Bryan Brown | BioChrist | CISO | UNPROMPTED | "honestly, AI is just gee-go faster." / "all AI does is highlight what you've already done wrong."
2026-09-11 | Ray Lewis | Pekin Insurance | practitioner | UNPROMPTED | "no, this was all just old-fashioned, come in, get on the box, and try to move laterally."
2026-09-09 | Andrew Dutton | Sumitomo Chemical America | evaluator | UNPROMPTED | "business risks remain largely unchanged, right? AI makes familiar attacks and more scalable"
2026-09-18 | Jerry Carlson | Commvault | Field CISO | UNPROMPTED | "fundamentally, this is nothing new, it's just the time window is shrunk."
2026-09-16 | Matthew Matturro | Trinetics | practitioner | UNPROMPTED | "none of the attacks that are coming in are novel, right? For the most part."
2026-08-31 | Israel Bryski | Rogo | advisor | UNPROMPTED | "a lot of its marketing fluff for the IPOs of Entropic and OpenAI"
2026-09-18 | John Murphy | — | IR practitioner | UNPROMPTED | "that really falls more under the category of, like, a social engineering thing"
2026-09-14 | Daniel Silverman | Stanford | practitioner | UNPROMPTED | "dark trace hasn't picked up anything." (6 years of Darktrace, zero AI-attributed detections)
2026-09-10 | (unnamed CISO, ReliaQuest customer) | — | practitioner | UNPROMPTED | "I don't see that AI isn't inventing zero days on the fly that well"

SUPPORT:
2026-08-28 | Andrey Lovchy | SoftClub | CISO (practitioner) | UNPROMPTED | "now, artificial intelligence, can, pretty, fast, investigate, Internet, find all resources, check for vulnerabilities, find, who are owners of those resources... estimate what, Possible, value of the assets, how much, hackers can, get, ransomed"
2026-09-24 | Mike Hiltz | nference | practitioner | UNPROMPTED (hedged) | "the time to remediate has gone down from, you know, say you used to have maybe 60 days or so before something was actually being exploited, now it's probably cut in half"
2026-09-08 | ABasu | shipping fleet | practitioner | UNPROMPTED | "The firewalls are getting bridged very easily now." (in the 2026-08-28 call)
2026-09-07 | Jason Manar | (not stated) | CISO | UNPROMPTED | "to leverage and find, zero-day vulnerabilities... bugs, that can be pieced together for zero-day type vulnerabilities"

---

## Notes carried forward

- DUPLICATE RECORDINGS. Four calls exist twice under different filenames (Zoom + Drive PDF of the same session). Counted once each:
  Israel Bryski = 2026-08-31_ciso-strategy-and-network-security.txt + 2026-08-31_security-leadership-discovery_israel-bryski.txt
  Leda Muller = 2026-08-31_enterprise-network-security-consultation.txt + 2026-08-31_network-security-discussion_leda-muller.txt
  Igor Spektor = 2026-09-01_ciso-network-security-discovery-discussion.txt + 2026-09-01_security-leadership-discovery_igor-spektor.txt
  Eli Edelkind = 2026-09-02_network-security-management-discussion.txt + 2026-09-02_security-leadership-discussion_eli-edelkind.txt
  44 files = 40 distinct calls.
- NAME CHECK. The a16z interviewee is transcribed as "Asaf" / "Asaf Ezra". thesis.md credits "Asaf Perlman (a16z)". Verify which is correct before using the name externally.
- TWO ANDREWS. Andrew Dutton (Sumitomo Chemical America, two calls 09-01 and 09-09) is NOT the "Andrew (ex-Nestle)" in thesis.md, who is the 09-15 veterinary-sector CISO with ~1000 hospitals.
- DATA QUALITY. 2026-09-18_network-security-startup-advisory.txt (Yoni/FICO) is machine-translated Hebrew with mid-sentence speaker-label interleaving at several points; several lines labelled "Shoval" are the interviewee's. Treat its quotes as low-confidence.
- 2026-09-22_cybersecurity-startup-ideation-meeting.txt is a vendor (NS Advisory) selling TO the founders. No customer present. Not customer evidence.
- 2026-09-15_skylayer-product-strategy-advisory.txt, 2026-09-22_a16z-intro-call.txt, 2026-09-22_eliya-elon-generalize-vc.txt are advisor/investor calls. No environments.
- "200 patches after a pen test": checked all 44 files. The phrase appears ONLY in founder speech (a16z line 40; NS Advisory 41:43; Shawn Anderson 13:53; Eliya call). No interviewee ever said it. thesis.md is correct to disown it.

## Processed transcripts

- 2026-08-25_security-leadership-discovery_jacques-lucas.txt
- 2026-08-28_rajesh-shoval-yuval.txt
- 2026-08-28_security-leadership-conversation_abasu.txt
- 2026-08-28_security-leadership-discovery_andrey-lovchiy.txt
- 2026-08-31_ciso-strategy-and-network-security.txt (dup of israel-bryski)
- 2026-08-31_enterprise-network-security-consultation.txt (dup of leda-muller)
- 2026-08-31_network-security-discussion_leda-muller.txt
- 2026-08-31_security-leadership-discovery_israel-bryski.txt
- 2026-09-01_asaf-shoval-yuval.txt
- 2026-09-01_ciso-network-security-discovery-discussion.txt (dup of igor-spektor)
- 2026-09-01_security-leadership-discovery_igor-spektor.txt
- 2026-09-01_security-leadership-discussion_andrew-dutton.txt
- 2026-09-02_network-security-management-discussion.txt (dup of eli-edelkind)
- 2026-09-02_security-leadership-discussion_eli-edelkind.txt
- 2026-09-03_network-security-discovery-interview.txt
- 2026-09-04_security-leadership-discovery_ariel-litvin.txt
- 2026-09-04_security-leadership-discovery_heather.txt
- 2026-09-07_security-leadership-discussion_jason-manar.txt
- 2026-09-07_security-leadership-followup_jason-lawrence.txt
- 2026-09-08_ai-agent-network-security-discussion.txt
- 2026-09-08_ai-agent-security-product-validation.txt
- 2026-09-08_cybersecurity-strategy-and-ai-trends.txt
- 2026-09-08_elastic-ciso-security-discussion.txt
- 2026-09-08_security-leadership-discussion_al.txt
- 2026-09-09_network-security-discovery_adam.txt
- 2026-09-09_security-leadership-discovery_andrew-dutton.txt
- 2026-09-10_ai-cybersecurity-product-discovery-discussion.txt
- 2026-09-10_ai-threats-and-defense-strategies.txt
- 2026-09-10_cybersecurity-startup-advisory-discussion.txt
- 2026-09-11_security-leadership-discussion_ray-lewis.txt
- 2026-09-14_stanford-cybersecurity-and-ai-strategy.txt
- 2026-09-15_security-leadership-discussion_bryan-brown.txt
- 2026-09-15_skylayer-product-strategy-advisory.txt
- 2026-09-16_security-leadership-discovery_harris-schwartz.txt
- 2026-09-16_security-leadership-discovery_matthew-matturro.txt
- 2026-09-16_security-leadership-discussion_thomas-sinnott.txt
- 2026-09-18_network-security-startup-advisory.txt
- 2026-09-18_security-leadership-discovery_jerry-carlson.txt
- 2026-09-18_security-leadership-discovery_john-murphy.txt
- 2026-09-22_a16z-intro-call.txt
- 2026-09-22_cybersecurity-startup-ideation-meeting.txt
- 2026-09-22_eliya-elon-generalize-vc.txt
- 2026-09-22_security-leadership-discovery_shawn-anderson.txt
- 2026-09-24_vulnerability-remediation-process-discussion.txt
