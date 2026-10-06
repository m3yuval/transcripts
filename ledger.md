# Discovery ledger
Last updated: 2026-10-06

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
2026-10-05 | interviewee, name not given ("Devon" once, in a founder line) | company not named ("world's largest travel company") | head of security, cyber physical and fraud (sitting exec; spoke only in general terms) | LED (Speaker 3 asked "Do you think that this is the point that makes the latency in the remediation process?") | "The patch is always where the hesitation is because you always like, you know, is this really going to work, right?" / "what's my level of trust and confidence that this patch is not going to break my business?"
2026-10-05 | interviewee, name not given ("Devon" once, in a founder line) | company not named ("world's largest travel company") | head of security, cyber physical and fraud (sitting exec; spoke only in general terms) | UNPROMPTED (the mechanism, not the pain) | "you would have a digital twin, you would have virtual patching to where you can evaluate, verify that that patch is going to work on the digital twin before you push a production" / "especially the digital twin concept is expensive"
2026-10-05 | Frederick (first name only) | independent advisor, ex-KPMG / Check Point consultant | advisor | LED (Shoval stated the dependency/impact gap first; the detail is his, second-hand from a KPMG client) | "they patched a system and then that brought down a production line for an entire car." / "And then they stop and then they let it be unpatched or unremediated instead. Because no one wants to bring down production, right?" (frequency: "I can't give you a figure how often")

CONTRA — same witnesses naming speed/volume/tooling as the blocker instead:
2026-09-24 | Mike Hiltz | nference | practitioner | UNPROMPTED | "So I think that's probably our biggest pain point right now, is being able to patch quickly enough, especially with the, the, the volume of vulnerabilities"
2026-09-10 | Chris | Wistia | practitioner | UNPROMPTED | "The reason that I'm not optimistic that it'll work in its current form is because it doesn't move fast enough. I guess if I had to summarize it, it just doesn't move fast enough."
2026-08-28 | ABasu | shipping fleet | practitioner | UNPROMPTED | "I know the vulnerability, but even today, when companies are releasing 500, 600 vulnerabilities, even by knowing, prioritizing them, I still won't be able to fix every one of them in a short time. I need more time."
2026-09-02 | Eli Edelkind | Cava | practitioner | UNPROMPTED | "I haven't seen any holistic solution that makes me happy."
2026-09-18 | Yoni | FICO | advisor | UNPROMPTED | "there are two things that make it difficult. One is the sense of urgency, and the other is priorities."
2026-08-31 | Israel Bryski | Rogo | advisor | UNPROMPTED | "CESA's are going to have to get much faster. in being able to remediate vulnerabilities"
2026-09-08 | Al | (not stated) | advisor | UNPROMPTED | "And they don't know what the problems are, and they don't understand it." (contradicts "they know what to fix")
2026-09-27 | Eliya Elon | Generalize.vc | investor | LED | "אני יכול להאמין שסיסואים יענו לכם שכן, יש בעיה" (I can believe CISOs will tell you yes, there is a problem; said after the founders pitched impact as the pain)
2026-09-28 | Rajiv (Speaker 2) | insurance broker, 200+ offices | sitting CIO with cyber accountability | LED (own incident; framing may come from the founders' slide, which the transcript does not capture) | "there are certain things in the environment like network and storage specifically that can bring down the entire enterprise and I've actually done it. I brought down the speedier network for six hours."
2026-09-28 | Rajiv (Speaker 2) | insurance broker, 200+ offices | sitting CIO with cyber accountability | LED (same caveat) | "that's why people are cautious to mess with the network because it's complex. You don't know where the remnants are and then you think you know where things are and then also you make a change and something downstream kicks in and brings down your entire network."
2026-09-28 | Rajiv (Speaker 2) | insurance broker, 200+ offices | sitting CIO with cyber accountability | LED (same caveat) | "it's not a lack of urgency it's more only pivoting on the protection and not causing outages" (reframes the "no urgency on network" finding as outage fear)
2026-09-28 | Javed Ikbal | (company not stated; supplies a global top-10 bank) | CISO, written LinkedIn thread | LED (Shoval wrote "what can be safely changed" first) | "\"what can be safely changed,\"--this is the biggest challenge that no software can solve. Talk to people who run change control boards. Taking down a production application for patching is always a struggle."
2026-10-05 | Frederick (first name only) | independent advisor, ex-KPMG / Check Point consultant | advisor | UNPROMPTED | "they're probably too small for that. They just don't know what to do to remediate." (his mid-market clients: not knowing what to fix IS the blocker)
2026-09-30 | Fernando Medrano | Fastly (CDN, "600 terabit per second") | security program leader, 7 years (sitting practitioner, live environment) | UNPROMPTED | "we rely on the engineering team to define what the operational impact might be of a particular change that we are suggesting." / "there's not a lot of friction, there's not a lot of…" (impact is owned by engineering and is not his blocker)
2026-09-30 | Fernando Medrano | Fastly (CDN, "600 terabit per second") | security program leader, 7 years (sitting practitioner, live environment) | UNPROMPTED (own environment, not measured) | "within a month usually gets fixed. If it's lower priority, if it's particularly high priority, you do it within, I'd say, a week." (pen-test findings: "For us, not too many.")

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
2026-09-28 | Javed Ikbal | (company not stated; supplies a global top-10 bank) | CISO, written LinkedIn thread | CONTRA | "Your target companies already have CS or PA." / "They do the attack path analysis, fix validation through vuln scanning, etc." (says the big platforms already cover detection-to-validation)
2026-10-05 | interviewee, name not given ("Devon" once, in a founder line) | company not named ("world's largest travel company") | head of security, cyber physical and fraud (sitting exec; spoke only in general terms) | UNPROMPTED (detection is NOT covered) | "But even upstream of that, be able to detect machine speed attacks. How do we know it's an agent?"
2026-10-05 | Frederick (first name only) | independent advisor, ex-KPMG / Check Point consultant | advisor | UNPROMPTED (C2b, vendor should not take the action yet) | "Helping them prioritize what they need to do first, I think is where the real value is." (after advising against building execution)
2026-09-30 | Fernando Medrano | Fastly (CDN, "600 terabit per second") | security program leader, 7 years (sitting practitioner, live environment) | UNPROMPTED (his pain is detecting risky changes engineers make, the reverse direction) | "it's very hard for security teams to know whether or not a particular change" … "is introducing risk or not" / "security teams, I don't think by and large are in the position anymore to approve network changes."

## C3 — The blocker is impact uncertainty specifically, NOT speed, prioritization, or absence of tooling

(no evidence for)

CONTRA — see the seven CONTRA lines under C1 plus:
2026-09-16 | Thomas Sinnott | CDW | pre-sales (vendor-side) | UNPROMPTED | "Everybody wants to be able to identify the problem faster, resolve it faster, remediate it faster"
2026-09-16 | Thomas Sinnott | CDW | pre-sales | UNPROMPTED | "they're getting overwhelmed with, with the amount of alerts that they get, and so being able to, diagnose what's important to what isn't, is still a challenge for most of them."
2026-09-16 | Matthew Matturro | Trinetics | CISO (practitioner) | UNPROMPTED | "what are the things they do in a 40-hour week. How much time are they spending? ... And what time would they get back?" (automation selected purely on hours recovered)
2026-09-22 | Nelson | NS Advisory | vendor-side | UNPROMPTED | "I have too many tools. I don't have enough people to even, I have zero clue. don't even ask me about my environment."
2026-09-10 | (unnamed advisor/vCISO) | — | advisor | UNPROMPTED | "Lack of resources lack of tools lack of skills lack of training. It's always a short change."
2026-09-14 | Daniel Silverman | Stanford | practitioner | UNPROMPTED | "we tend to document that stuff in email and Slack... And for us specifically, it's small enough that it's like, well, that's good enough."
2026-09-27 | Eliya Elon | Generalize.vc | investor | CONTRA | "הטענה היסודית לווליו היא כאילו... אני חוסך שעות אדם" (the basic value claim is... I save man-hours; he names labor, not impact uncertainty, as what the category sells)
2026-09-28 | Javed Ikbal | (company not stated; supplies a global top-10 bank) | CISO, written LinkedIn thread | CONTRA | "It is not a real pain now, but in 6-12 months when threat actors start using Mythos-like AI to exploit vulns, \"faster\" is going to be a major requirement." (names speed, and not yet)
2026-09-28 | Javed Ikbal | (company not stated; supplies a global top-10 bank) | CISO, written LinkedIn thread | CONTRA (client environment, secondhand) | "A global top-10 bank has asked us to patch CISA KEV issues within 24 hours. I asked them what is their own internal timeline, and they admitted that they are struggling." (symptom confirmed; cause not given)
2026-09-28 | Scott (Speaker 5) | ex-Global CIO Wells Fargo | advisor (NS Advisory circle) | CONTRA | "Networks are stuck 15 years ago from a visibility perspective." (names visibility as the problem); also "I'm worried about the thesis"
2026-09-28 | Nicole (Speaker 4) | ex-Microsoft, "five times CISO" | advisor | CONTRA | "I know that it's more futuristic and not like, let's talk about today. It's my problem today." (AI-speed remediation is a future concern, not today's)
2026-10-05 | Frederick (first name only) | independent advisor, ex-KPMG / Check Point consultant | advisor | UNPROMPTED | "Helping them prioritize what they need to do first, I think is where the real value is." (names prioritization, which C3 rules out)
2026-09-29 | interviewee, not named (possibly "Yoni"; unconfirmed) | company not named | security leader, own environment "70% AWS" (no workflow described) | UNPROMPTED | "The second problem is who is actually on the power. Do you take it to IT or security?" / "security is doing vulnerability scanning, but you feel the difficulty of patching IT and IT needs to do it." (ownership, not impact)
2026-09-30 | Fernando Medrano | Fastly (CDN, "600 terabit per second") | security program leader, 7 years (sitting practitioner, live environment) | UNPROMPTED | "ultimately the tough part is which of the things that are happening in the organization are, are increasing our risk" / "if it's simply a platform that is informing me of changes, I'm… it's gonna be too much." (prioritization of risk, not impact of the fix)

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
2026-09-27 | Eliya Elon | Generalize.vc | investor | CONTRA | "שכל השחקנים האמריקאים יגידו אנחנו גם מבינים את האימפקט, וגם עושים איזה שהוא Downstream Impact Analysis" (every American player will say they also understand the impact and do downstream impact analysis)
2026-09-27 | Eliya Elon | Generalize.vc | investor | CONTRA | "תכלס גם זה מה שרוב כל שחקני ה- CTEM כאילו נכנסו אליו" (this is also where most CTEM players have gone)
2026-09-27 | Eliya Elon | Generalize.vc | investor | note | "הטענה הזאת מונדור היא מאוד מאוד קשה לבנייה" (this claim from a vendor is very, very hard to build): proof is hard, which cuts both ways
2026-09-28 | Javed Ikbal | (company not stated; supplies a global top-10 bank) | CISO, written LinkedIn thread | CONTRA | "Fix impact assessmnet: what will you do that my vuln scanner or patching tool can't do?" / "it’s not a big enough gap for a separate product" / on safe-change: "no software can solve"
2026-09-29 | interviewee, not named (possibly "Yoni"; unconfirmed) | company not named | security leader, own environment "70% AWS" (no workflow described) | UNPROMPTED | "Astellia is one of the companies that has the ability to do the network analysis and the impact analysis of change." / "There are other groups, Zafran, who know how to do it very well"
2026-10-05 | Frederick (first name only) | independent advisor, ex-KPMG / Check Point consultant | advisor | UNPROMPTED | "very few wanted to pay for it because it cost so much because of the manual work." (his own Check Point attempt at impact mapping, abandoned)
2026-10-05 | interviewee, name not given ("Devon" once, in a founder line) | company not named ("world's largest travel company") | head of security, cyber physical and fraud (sitting exec; spoke only in general terms) | UNPROMPTED | "I think what you have here are additional tools that could benefit the team in taking steps to protect the assets."

## C5 — Trust is earned with reversibility; start where being wrong is cheap

2026-09-15 | Andrew (ex-Nestle, veterinary) | ~1000 hospitals | CISO (practitioner) | UNPROMPTED | "we did a design partnership with a company that was building AI agents for the security team, and we were able to use them on the identity side to do some kind If you think about those kind of hygiene things that will not break stuff, but only do some cleanup, in worst case scenario, you just have to turn something back on that you've turned off."
2026-08-31 | Israel Bryski | Rogo | advisor | UNPROMPTED | "if you broke something, give me a one click undone on rollback button."
2026-09-24 | Mike Hiltz | nference | practitioner | UNPROMPTED | "So being able to test, I have a way to roll back"
2026-09-16 | Harris Schwartz | fractional CISO | fractional | UNPROMPTED | "why don't you start off with read-only access, let's see how that goes, and then maybe you could move into write access."
2026-09-09 | Andrew Dutton | Sumitomo Chemical America | evaluator | UNPROMPTED | "even when I deploy something, it's only gonna be read-only. I'm not gonna trust to shoot a gun."
2026-08-31 | Israel Bryski | Rogo | advisor | UNPROMPTED | (map of where being wrong is cheap) "if the CISO's using any of the security-native services within AWS, like Security Hub, and GuardDuty, and Detective... that's squarely in the security department. They can do whatever they want with those things." vs "anything that can impact the reliability, the stability of the production environment... that's usually your indicator that the CIO will need to be involved."
2026-09-27 | Eliya Elon | Generalize.vc | investor | UNPROMPTED (investor) | "האם יש מספיק Trust מהארגון שה- Agent יעשה פעולה ב- Prod , לעומת פעולה במקום אחר" (is there enough trust from the org for the agent to act in prod, versus elsewhere); he frames trust-by-blast-radius as the axis, before the founders used the word trust

## C6 — Wedge A: network / firewall config is the right first wedge
2026-09-30 | Fernando Medrano | Fastly (CDN, "600 terabit per second") | security program leader, 7 years (sitting practitioner, live environment) | UNPROMPTED (one hard network remediation; cause is scale, impact owned by engineering) | "And that used to be a very contentious thing, and it's still a very difficult thing, because the number of services that we provide… that we run." (outbound network filtering)

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
2026-09-28 | Rajiv (Speaker 2) | insurance broker, 200+ offices | sitting CIO with cyber accountability | SUPPORT (as a pain) / CONTRA (as a CISO buy) | "The infrastructure team owns the network." and "when it comes to the network spend seat source [CISOs] don't know the budget" — the fear of network change is real, but the owner and budget are the CIO/infra side
2026-09-28 | Rajiv (Speaker 2) | insurance broker, 200+ offices | sitting CIO with cyber accountability | note | "What is it going to do to my network downstream?" (his own example of what he would want simulated)
2026-10-05 | interviewee, name not given ("Devon" once, in a founder line) | company not named ("world's largest travel company") | head of security, cyber physical and fraud (sitting exec; spoke only in general terms) | UNPROMPTED | "certainly protecting what's in our virtual firewalls is a priority and that is a lot easier to solve for." / "But the dependencies from third-party, fifth-party applications upon which we also rely, that's a much bigger problem."
2026-09-29 | interviewee, not named (possibly "Yoni"; unconfirmed) | company not named | security leader, own environment "70% AWS" (no workflow described) | UNPROMPTED | "you are talking about legacy networks, not AWS or public clouds." / "Right, because it's really a very dangerous area." (he also says "the network is a priority" at 00:18:11 in a garbled passage; his position is unclear)
2026-09-30 | Fernando Medrano | Fastly (CDN, "600 terabit per second") | security program leader, 7 years (sitting practitioner, live environment) | LED (answer to Shoval's "Does it resonate with you?") | "I think it… this probably applies maybe a little bit more to, let's say, more legacy companies that actually operate on-prem infrastructure" (cloud is controlled via org policies, Terraform, Sentinel; only "On the bare metal side, that's where it gets a lot more difficult")

## C7 — Wedge B: OS / package / container patching is the right first wedge

2026-09-24 | Mike Hiltz | nference | CIO+CISO (practitioner) | UNPROMPTED | "I think vulnerability patch is probably one of the top ones." / "For misconfigurations in cloud, I think we're in a better spot there."
2026-09-24 | Mike Hiltz | nference | practitioner | UNPROMPTED | (full pipeline) "it really is defining which groups are responsible We go through the process of opening change management or change control tickets. There's testing involved there are Package dependencies that we have to consider"
2026-08-31 | Israel Bryski | Rogo | advisor | UNPROMPTED | "they have to figure out how to patch and do change management and patch management faster." (his own unprompted answer to an open 2027 question)
2026-09-10 | Chris | Wistia | practitioner | UNPROMPTED | "this version of this dependency is out of date. Just go fix it, or get it into stage at least, and then run it through the automated regression testing."
2026-09-22 | Asaf Ezra | a16z | investor | UNPROMPTED | "So patching historically has been the worst of everything, right?" / "it could be a good niche, but I would focus on let's say high and critical vulnerabilities."
2026-09-10 | (unnamed CISO, ReliaQuest customer) | — | practitioner | UNPROMPTED | "you're never going to be able to patch all the vulnerabilities faster. You've got to really focus on what needs to be patch faster."
2026-09-16 | Matthew Matturro | Trinetics | practitioner | UNPROMPTED | "good patch management... patch management hygiene. You're gonna cut down on so much"
2026-09-14 | Daniel Silverman | Stanford | practitioner | UNPROMPTED | "all they can do is say, hey, we're chasing CVEs, we're patching when we can, and that's all they've got. And it's very painful."
2026-10-05 | interviewee, name not given ("Devon" once, in a founder line) | company not named ("world's largest travel company") | head of security, cyber physical and fraud (sitting exec; spoke only in general terms) | UNPROMPTED (dependency patching as the bigger problem; OS/container never named) | "But the dependencies from third-party, fifth-party applications upon which we also rely, that's a much bigger problem."

CONTRA:
2026-09-04 | Ariel Litvin | ex-First Quality | retired CISO | UNPROMPTED | "take the basic example of Microsoft's Patch Tuesday... No, it doesn't happen. There are SMBv1 and TLSv1 servers and such nonsense running in organizations for years."
2026-09-18 | Yoni | FICO | advisor | UNPROMPTED | (virtual patching is the community's existing answer) "the way of the community to support it needs to be a kind of a direction that is called virtual patching"
2026-09-28 | Rajiv (Speaker 2) | insurance broker, 200+ offices | sitting CIO with cyber accountability | LED | "the infrastructure vulnerability is a huge pocket"

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
2026-09-28 | Javed Ikbal | (company not stated; supplies a global top-10 bank) | CISO, written LinkedIn thread | CONTRA | "not many CISOs have that kind of budget. I don't." (also: small companies "simply do not have the budget")
2026-09-28 | Rajiv (Speaker 2) | insurance broker, 200+ offices | sitting CIO with cyber accountability | CONTRA (budget owner) | "when it comes to the network spend seat source [CISOs] don't know the budget"
2026-10-05 | Frederick (first name only) | independent advisor, ex-KPMG / Check Point consultant | advisor | CONTRA | "very few wanted to pay for it because it cost so much because of the manual work." Soft interest only: "Absolutely, it would be fun to be a part of your journey." (no budget, no owner)
2026-10-05 / 2026-09-29 | Davon call, Frederick, 09-29 interviewee | — | — | none | No budget, approval chain or design-partner question was asked in any of the three calls.
2026-09-30 | Fernando Medrano | Fastly (CDN, "600 terabit per second") | security program leader, 7 years (sitting practitioner, live environment) | LED (Yuval: "Would you pay for something that will solve this problem?") | "Maybe. There's a lot of network discovery tools out there" … "it needs to be more intelligent than simply" … "A change happened in the network". Next step offered: "Happy to be a sounding board." (no pilot)

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
2026-09-30 | Fernando Medrano | Fastly (CDN, "600 terabit per second") | security program leader, 7 years (sitting practitioner, live environment) | LED (after Shoval named agentic attacks) | "And AI is certainly making it worse, because the second something gets exposed that you didn't intend"

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

- 2026-09-27_eliya-elon-generalize-vc-followup.txt (Hebrew PDF, no timestamps): speaker labels are unreliable. Several turns tagged "שובל" are Eliya by content (L47, L61 tagged יובל, L64 Rapid7/market numbers, L66 San Francisco advice, second half of L67), and L60 tagged "איליה" is Shoval (feminine verbs). Only quote Eliya from turns that are both labeled and read as his.
- PITCH vs EVIDENCE (09-27 Eliya call): Yuval told Eli Edelkind's Lowe's outage as "a firewall version upgrade done because of a CVE ... firewall A and B ... everything crashed" with CRM/call-center downtime. Eli's transcript (09-02) says "one bad threat intel ... in a Palo firewall" — a vendor threat-intel update, not a CVE-driven upgrade, and no A/B pair. Shoval also said they met "more than 50 CISOs"; the corpus holds 41 distinct calls, many not CISOs. Correct both before telling them to investors again.
- CORRECTION 2026-09-27 to the note above: the "more than 50 CISOs" claim (Shoval) is NOT contradicted. The repo holds only recorded calls (41 distinct); about 8 more external meetings sit in Zoom as 403/untranscribed, and at least 6 more contacts on the founders' list have no recording. Roughly 55 conversations with security leaders, not all of them CISOs. Only the Eli Edelkind retelling is contradicted by a transcript.

- 2026-09-28_ns-advisory.txt (Google Doc, Google Meet call, second NS Advisory session): generic Speaker 1-5 labels. By self-introduction: Speaker 1 = Nelson (host), 2 = Rajiv (sitting CIO, insurance broker, "I actually do have the accountability"), 3 = Shoval, 4 = Nicole ("five times CISO", ex-Microsoft), 5 = Scott (ex-Global CIO Wells Fargo). Lines 35-36 (Paragon background) are Yuval despite the Speaker 2/1 tags. The transcript has gaps of minutes between several turns and does not capture the slides shown, so first-mention calls are uncertain: everything Rajiv said is marked LED.
- 2026-09-28_javed-feedback_javed-ikbal.txt is a written LinkedIn exchange, not a call. Shoval's opening message states the thesis ("how teams assess impact, remediate, and verify"), so nothing in it is unprompted.

- 2026-10-05_yuval-shoval.txt is an internal 5-minute founders' prep call (Hebrew) before a CISO call that day. No interviewee. It shows the pitch going in: lead with code/infra patching, "שלא שוברת את הפרודקשן" (doesn't break production), and close with "היית קונה דבר כזה? ... רוצה להיות עידן פרטנר?" Any 10-05 call that echoes C1/C3/C7 was led.
- 2026-10-05_davon-booking.txt (Google Doc, date inferred): starts mid-call, Speaker 1-3 only. Speaker 1 is the interviewee; the founders are 2 and 3 (which is which unknown). Turn merges at 04:41 ("Absolutely."), 09:59 ("Yes, absolutely.") and 17:32/18:02 (his question split under Speaker 3). The name "Davon" is only in the filename; the transcript has "Devon" once. Company never named.
- 2026-10-05_cybersecurity-remediation-product-validation.txt: Speaker 1 = Yuval (Paragon), Speaker 2 = Frederick. Shoval stated C1, C2, C3 and C10 in one 3-minute monologue (07:50-10:52) before any problem question, so all agreement on those is LED.
- 2026-09-29_security-remediation-strategy-discussion.txt: machine-translated from Hebrew, heavily garbled. 00:00-03:25 is the founders alone. Several one-line "Shoval:" turns inside Speaker 2's sentences are his words split off. Interviewee never named or placed at a company.

- 2026-09-30_security-leadership-discovery_fernando-medrano.txt: Zoom 403 until 2026-10-06. Clean English transcript, speakers named. Shoval opened with the network-wedge slide ("we are focusing on the network, layer") at 08:50, so everything network-related he said after is in answer to that frame.

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
- 2026-09-27_eliya-elon-generalize-vc-followup.txt
- 2026-09-28_javed-feedback_javed-ikbal.txt
- 2026-09-28_ns-advisory.txt
- 2026-09-29_security-remediation-strategy-discussion.txt
- 2026-10-05_cybersecurity-remediation-product-validation.txt
- 2026-10-05_davon-booking.txt
- 2026-10-05_yuval-shoval.txt (internal, no evidence)
- 2026-09-30_security-leadership-discovery_fernando-medrano.txt
