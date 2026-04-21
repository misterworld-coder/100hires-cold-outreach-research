# Cold Outreach Pipeline for B2B SaaS — Playbook & SOP

**Author:** Vignesh
**Based on:** Research collected in `/research/` folder
**Last updated:** April 2025
**Status:** Living document — will be updated as new data comes in

---

## What This Playbook Is

This is a step-by-step Standard Operating Procedure (SOP) for building a cold outreach pipeline for a B2B SaaS company — from zero to a consistent flow of booked meetings. Every recommendation in this document is sourced from practitioners who actively run campaigns at scale. Where experts disagree, I've noted it and taken a side.

This is not a list of tips. It is a system you can execute.

---

## Who This Is For

- A B2B SaaS founder or early sales hire with no outbound pipeline yet
- A company with a defined product and at least a rough idea of who their customer is
- Someone willing to invest 4–6 weeks in setup before expecting results

This playbook is **not** for:
- Consumer products (B2C)
- Companies with no defined ICP
- Anyone looking for a quick hack that bypasses the fundamentals

---

## Table of Contents

1. [Phase 1 — Foundation: ICP and Offer](#phase-1)
2. [Phase 2 — Infrastructure: Domains and Deliverability](#phase-2)
3. [Phase 3 — List Building](#phase-3)
4. [Phase 4 — Copywriting](#phase-4)
5. [Phase 5 — Sequencing and Multi-Channel](#phase-5)
6. [Phase 6 — Sending and Optimisation](#phase-6)
7. [Where Experts Disagree](#disagreements)
8. [What I Rejected and Why](#rejected)
9. [My Original Ideas](#original)
10. [Weaknesses of This Playbook](#weaknesses)
11. [Who I Would NOT Recommend Following](#not-recommended)

---

<a name="phase-1"></a>
## Phase 1 — Foundation: ICP and Offer

This is the most important phase. Most cold outreach fails here, before a single email is sent.

### 1.1 Define Your ICP (Ideal Customer Profile) With Surgical Precision

Do not start with "B2B SaaS companies." That is not an ICP — it is an industry. A real ICP looks like this:

> "VP of Sales at a B2B SaaS company with 20–100 employees, using Salesforce, that has recently posted at least 2 SDR job openings."

The more specific, the better. Specificity enables personalisation, and personalisation drives replies.

**Source:** Nick Abraham, LinkedIn (October 2023) — https://www.linkedin.com/in/nick-abraham/
> "They offered something incredibly valuable, to an extremely specific clientele. We pulled lists of that clientele, and stuck to the cold email principles. They worked like a charm."

**Source:** Hey {First Name} Podcast, Episode 132, Morgan Williams interviewing Nick Abraham — https://morgandwilliams.com
> Targeting + Offer + Personalisation as the three-legged stool. Narrow ICP enables higher personalisation at scale.

**Action:** Before writing a single email, answer these questions in writing:
- What job title does your buyer hold?
- How big is their company (employees, revenue)?
- What tools do they currently use that yours replaces or integrates with?
- What does their company look like when they are ready to buy? (e.g., raised funding, hiring SDRs, expanding into new markets)

### 1.2 Build an Irresistible Offer

Your offer needs to be specific enough that saying no to it feels like a mistake.

A weak offer: "We help B2B companies grow their pipeline."
A strong offer: "We generate 12 meeting-ready leads in 30 days for B2B SaaS companies doing $50K–$500K ARR, or you don't pay."

The three components of a strong offer (Source: Nick Abraham, LinkedIn, 2023 — https://www.linkedin.com/in/nick-abraham/):
1. **One specific service** → One result → For one specific ICP
2. **Quantifiable outcome** → Not "more leads" but "12 qualified meetings in 30 days"
3. **Risk reversal** → Performance basis, refund guarantee, or "pay only when you see results"

### 1.3 Define Your "Enemy" Before Writing Copy

Before writing any email, identify what your prospect hates about their current situation — not what your product does, but what pain they already feel every day.

**Source:** Belal Batrawy, LinkedIn (2024) — https://www.linkedin.com/in/belbatrawy/
> "Forget leading with how you can solve their problems — they aren't even aware they have a problem! Instead, pick on the stuff that annoys them daily, the tedious tasks they dread."

This "enemy" becomes the emotional anchor of your outreach. Every email should lead with it.

---

<a name="phase-2"></a>
## Phase 2 — Infrastructure: Domains and Deliverability

Most beginners skip this phase. It is why most beginners' emails land in spam.

### 2.1 Never Send Cold Email from Your Primary Domain

Your primary domain (the one on your website) must be protected. If it gets flagged as spam, your entire company's email reputation is damaged — including internal emails.

**Action:** Buy 3–5 secondary domains that look like your main domain. Examples:
- Primary: `yourcompany.com`
- Outreach domains: `getyourcompany.com`, `tryourcompany.com`, `yourcompany.io`

**Source:** Nick Abraham, LinkedIn (2023) — https://www.linkedin.com/in/nick-abraham/
> "Don't spread inboxes across multiple organizational panels, so they don't share the same subnet IP."

**Source:** Yassin Hariss, LinkedIn — https://www.linkedin.com/in/yassin-hariss/
> Specialises in DNS configuration, inbox rotation, and domain health. Key principle: treat domains like servers, not email addresses.

### 2.2 Configure DNS Correctly

For each outreach domain, set up:
- **SPF** — tells email providers which servers are allowed to send from your domain
- **DKIM** — adds a digital signature to verify your emails
- **DMARC** — policy that tells providers what to do if SPF/DKIM fail

Without these three, your emails will not land in inboxes at scale.

### 2.3 Warm Up Every Domain Before Sending

New domains have zero reputation. Sending cold emails from them immediately will get them flagged.

**Warm-up process:**
- Week 1–2: 5–10 emails/day (automated warm-up tool)
- Week 3–4: 20–30 emails/day
- Week 5+: 40–50 emails/day per inbox

**Source:** Cold Outreach Podcast, Jeremy Chatelaine + Jack Reamer — https://open.spotify.com/show/coldoutreachpodcast
> "Inbox warming timing: 3–4 weeks minimum before high-volume sends."

**Tools:** Instantly, Lemwarm, Mailreach (all have free or cheap warm-up plans)

### 2.4 Use Inbox Rotation

Do not send all emails from a single inbox. Rotate across 3–5 inboxes per domain. This mimics natural human sending behaviour and protects your domain score.

**Source:** Nick Abraham, LinkedIn (2023) — https://www.linkedin.com/in/nick-abraham/
> "Don't spread inboxes across multiple organizational panels, so they don't share the same subnet IP." [i.e., spread them across different panels/subnets]

---

<a name="phase-3"></a>
## Phase 3 — List Building

A great email to the wrong person gets zero replies. A mediocre email to the right person gets meetings.

### 3.1 Build Lists From High-Signal Sources, Not Scraped Databases

The difference between a 1% reply rate and a 10% reply rate is almost always list quality, not copy quality.

**Source:** ColdIQ (Vincent Paquette), YouTube — https://www.youtube.com/@ColdIQ
> Signal-based list building using intent data: hiring signals, funding rounds, tech stack installs, and LinkedIn activity.

**High-signal triggers to look for:**
- Company just raised a funding round → they have budget
- Company is actively hiring SDRs → they are building outbound and need infrastructure
- Company recently switched from a competitor tool → they are evaluating the space
- Decision maker just changed roles → new role = new budget and willingness to change tools

### 3.2 Use Clay to Enrich and Filter Leads

Clay is the current standard tool for building signal-based prospect lists. It pulls data from LinkedIn, Apollo, Clearbit, and dozens of other sources and lets you build precise lists based on multiple signals at once.

**Source:** ColdIQ YouTube channel — https://www.youtube.com/@ColdIQ
> Full Clay workflow walkthroughs showing how to combine intent signals into actionable prospect lists.

**Basic Clay workflow:**
1. Pull a company list from Apollo based on size, industry, tech stack
2. Enrich in Clay with LinkedIn data, hiring signals, recent funding
3. Filter to only companies matching 2+ signals
4. Export with verified email addresses

### 3.3 Verify Every Email Address

A bounce rate above 5% damages your domain reputation permanently.

**Action:** Run every list through an email verification tool (NeverBounce, Zerobounce, or Millionverifier) before sending a single email.

**Source:** Nick Abraham, LinkedIn (2023) — https://www.linkedin.com/in/nick-abraham/
> "Clean + format company names, titles, and lead names" — sloppy data is one of the top deliverability killers.

---

<a name="phase-4"></a>
## Phase 4 — Copywriting

### 4.1 The Structure of a High-Converting Cold Email

Every cold email should have exactly four parts. Nothing more.

**Source:** Vin Matano, Sales Evangelist Podcast (June 2024) — https://podcasts.apple.com/us/podcast/vin-matano-my-four-part-cold-email-secret/id788738885

1. **Relevant hook** — Something specific to this prospect. Their recent LinkedIn post, a company announcement, a hiring signal. Not "I came across your profile."
2. **Problem statement** — One sentence naming the pain they already feel (the "enemy" from Phase 1)
3. **Solution bridge** — One sentence connecting your offer to that pain
4. **Soft CTA** — Not "book a 30-minute call." Instead: "Would it be worth a quick conversation?" or "Happy to send over a case study if useful."

**Internal consistency check (Vin Matano's rule):** Read the hook, problem, and solution independently. If they don't flow naturally together as a connected thought, the email will not convert. Rewrite until all three are talking to each other.

### 4.2 Subject Line: Mimic Internal Emails

The subject line's only job is to get the email opened. The highest-performing subject lines look like emails from a colleague — not a marketing campaign.

**Examples that work:**
- "quick question"
- "intro"
- "{First Name} / {Your Name}"
- "following up on [company name]"

**Source:** Cold Outreach Podcast, Jeremy Chatelaine — https://open.spotify.com/show/coldoutreachpodcast
> "Subject lines that mimic internal emails consistently outperform clever/creative ones."

**Source:** Nick Abraham, LinkedIn (2023) — https://www.linkedin.com/in/nick-abraham/
> "Mimic an internal email, and use the prospect's first name" in the subject line.

### 4.3 Length: 2–3 Sentences Per Email

This is non-negotiable. Nobody reads long cold emails.

**Source:** Nick Abraham, LinkedIn (October 2023) — https://www.linkedin.com/in/nick-abraham/
> "Every email in the sequence needs to be 2-3 sentences max."

**Source:** Vin Matano, LinkedIn (2023) — https://www.linkedin.com/in/vinmatano/
> "You're overcomplicating it." — The best cold emails are simple, not sophisticated.

### 4.4 The CTA: Ask for Less Than You Want

Asking for a 30-minute demo call in a cold email is asking for too much from a stranger. The goal of the first email is not to close a deal — it is to start a conversation.

**Better CTAs:**
- "Would it be worth a 10-minute chat?"
- "Happy to send over a short case study — want me to?"
- "Is this something your team is actively working on?"

**Source:** Nick Abraham, LinkedIn (October 2023) — https://www.linkedin.com/in/nick-abraham/
> "Have a soft CTA offering sales asset" — a sales asset (case study, breakdown, short video) is less threatening than a calendar invite.

### 4.5 Write Like a Human, Not a Marketer

Remove: buzzwords, jargon, passive voice, vague claims ("industry-leading," "world-class," "synergy")
Use: specific numbers, direct sentences, the prospect's actual language

**Source:** Belal Batrawy, LinkedIn (2024) — https://www.linkedin.com/in/belbatrawy/
> The "Death to Fluff" principle: every word in a cold email must earn its place. If it doesn't move the reader toward a reply, cut it.

---

<a name="phase-5"></a>
## Phase 5 — Sequencing and Multi-Channel

### 5.1 The 4-Step Email Sequence

Do not send one email and give up. Do not send 12 emails and become a pest. The optimal sequence is 4 steps.

**Source:** Nick Abraham, LinkedIn (October 2023) — https://www.linkedin.com/in/nick-abraham/

| Step | Timing | Content |
|------|--------|---------|
| Email 1 | Day 0 | Offer + Value (your hook + problem + solution + soft CTA) |
| Email 2 | Day 3–4 | Follow-up + Value/Sales Asset (send a relevant case study or insight) |
| Email 3 | Day 7–8 | Follow-up + Different angle (approach the problem from a different direction) |
| Email 4 | Day 14 | Break-up email ("I won't reach out again — but if timing changes, I'm here.") |

Each email must stand alone. Email 2 is not just "bumping this up" — it adds new value.

### 5.2 Add LinkedIn as a Second Channel

Email + LinkedIn together dramatically outperforms email alone. The sequence is:

1. Connect on LinkedIn (no note, or a short non-pitchy note)
2. Wait for acceptance
3. Like or comment on a recent post (genuine, not a bot comment)
4. Send the cold email
5. If no reply in 5 days, follow up via LinkedIn DM with a shorter version of Email 2

**Source:** Jack Reamer, SalesBread + Cold Outreach Podcast — https://www.linkedin.com/in/jackreamer/
> 48.14% positive reply ratio achieved through ultra-personalised LinkedIn outreach. Key driver: referencing specific prospect activity before messaging.

**Source:** Hey {First Name} Podcast, Episode 132 — https://morgandwilliams.com
> 30% LinkedIn accept rate + 25% email reply rate when targeting and personalisation are combined.

### 5.3 The Fibonacci Follow-Up Rule

Spacing follow-ups using the Fibonacci sequence (1, 2, 3, 5, 8 days between touches) keeps you present without being annoying.

**Source:** Jack Reamer / Cold Outreach Podcast — https://salesbread.com/linkedin-outreach-strategy/
> "We have found that you should follow up using the Fibonacci sequence. This approach creates consistent but not overwhelming follow-ups, respecting the customer's time while keeping your business top-of-mind."

### 5.4 Creative Outreach for High-Value Accounts

For accounts where the ACV (annual contract value) justifies the extra effort — think enterprise targets — use pattern-interrupting creative touches:

- Personalised Loom video (60 seconds, screen share showing something specific about their business)
- A short, specific observation about their product/website/job posting sent via LinkedIn
- A relevant piece of content (not your own) sent with a one-line note on why it's relevant to them

**Source:** Vin Matano, Aspireship Live Session — https://aspireship.com/aspireship-live-with-vin-matano-creative-multi-channel-prospecting/
> Used fitness challenges and personalised video assets to land meetings with hard-to-reach enterprise accounts at Demandbase.

---

<a name="phase-6"></a>
## Phase 6 — Sending and Optimisation

### 6.1 Sending Limits Per Inbox

- Maximum 30–50 cold emails per inbox per day
- Randomise send times (not all at 9:00 AM)
- Use spintax to create slight variations in copy across sends

**Source:** Nick Abraham, LinkedIn (2023) — https://www.linkedin.com/in/nick-abraham/
> "Create more variance in campaign setup (warm-up randomization, sending time variation, etc)."

### 6.2 The Only Metric That Matters: Reply Rate

Open rates are broken. Apple Mail Privacy Protection auto-loads tracking pixels, making open rates meaningless.

Track instead:
- **Reply rate** (target: 3–8% for cold email, higher for LinkedIn)
- **Positive reply rate** (interested replies only — target: 1–3%)
- **Meeting booked rate** (target: 0.5–1% of total emails sent)

**Source:** Outreaches.ai Benchmarks Report (2025) — https://outreaches.ai/blog/cold-outreach-benchmarks
> "Reply rate is now a more valuable indicator of true engagement" than open rate.

### 6.3 A/B Test One Variable at a Time

When reply rates are low, change one thing per week and measure:
- Week 1: Test two different subject lines
- Week 2: Test two different opening hooks
- Week 3: Test two different CTAs

Never change multiple things at once — you won't know what moved the needle.

### 6.4 Maintain a Do-Not-Contact List

Anyone who replies with "unsubscribe," "not interested," or "stop emailing me" goes on a DNC list immediately. Emailing them again damages deliverability and reputation.

**Source:** Nick Abraham, LinkedIn (2023) — https://www.linkedin.com/in/nick-abraham/
> "Remove all people from campaign who don't want to be emailed, and add them to your DNC."

---

<a name="disagreements"></a>
## Where Experts Disagree

### Disagreement 1: Volume vs. Personalisation

**Alex Berman's position** (YouTube, alexberman.com): Volume is the primary lever. Send 10x more emails than your competitors with a "good enough" message. The math works in your favour at scale.

**Jack Reamer's position** (SalesBread, Cold Outreach Podcast): Ultra-personalisation is the only sustainable edge. A highly personalised campaign to 100 people will outperform a blasted campaign to 10,000.

**My take: Jack Reamer is right for most B2B SaaS companies.** Alex Berman's volume approach works for agencies selling commodity services where the ACV is low and the ICP is broad. For B2B SaaS — where you're targeting specific personas with longer sales cycles and higher ACVs — a 48% positive reply rate from 100 personalised emails beats a 0.5% reply rate from 10,000 blasted ones, both in results and in brand reputation. Volume without targeting just burns your domain faster.

---

### Disagreement 2: Length of Follow-Up Sequences

**Nick Abraham's position** (LinkedIn, October 2023): 4-step sequences. After 4 emails, move on. Longer sequences are spam.

**Alex Berman's position** ("The Baking Method", alexberman.teachable.com): Year-long follow-up sequences. Prospects often convert 6–12 months after first contact. A "baking" approach keeps you top of mind without pressure.

**My take: Both are right in different contexts.** For volume outbound to a broad list, Nick's 4-step approach is the right default — clean, efficient, respects the prospect's time. But for a carefully curated list of high-value dream accounts where you've done deep research, Alex's long-game approach makes sense. The solution is to have two separate workflows: a 4-step sequence for general outreach, and a slower "baking" sequence for your top 20–30 target accounts.

---

### Disagreement 3: Should You Name Competitors in Your Email?

**Belal Batrawy's position** (LinkedIn, 2024): Yes. Name competitors directly. It frames your offer in a context the prospect already understands and positions you as confident rather than vague. His Grain cold call script explicitly names Gong, Chorus, and Clari.

**Common industry advice** (including many QuickMail blog posts): Avoid naming competitors. It sounds defensive, can feel aggressive, and risks alienating prospects who are happy with a competitor.

**My take: Belal is right, but with conditions.** Naming a competitor works when: (1) the competitor is well-known, (2) you have a clear, specific differentiator — not just "we're cheaper," and (3) you frame it around the prospect's frustration, not a feature comparison. "A lot of teams using Gong find the onboarding complex and expensive" is useful. "We're better than Gong" is not.

---

<a name="rejected"></a>
## What I Rejected and Why

### Rejected Idea 1: AI-Generated Personalisation at High Volume

Several sources (including Yassin Hariss and ColdIQ) recommend using AI tools (like Quicklines.ai) to auto-generate personalised first lines at scale — pulling from a prospect's LinkedIn posts, company news, etc., and auto-writing an opener for each email.

**Why I rejected it for this playbook:** The personalisation floor is rising fast. What felt personalised in 2022 (mentioning someone's LinkedIn post in an opener) is now immediately recognisable as automated. Prospects have seen thousands of "I noticed you recently posted about X" openers and they know it's a tool doing it, not a human. Including this as a primary tactic risks making the entire system feel robotic.

It is useful as a *fallback* for large lists where manual personalisation isn't feasible — but it should not be the main personalisation strategy for a B2B SaaS company with a focused ICP.

**Source considered:** Yassin Hariss, LinkedIn — https://www.linkedin.com/in/yassin-hariss/; ColdIQ YouTube — https://www.youtube.com/@ColdIQ

---

### Rejected Idea 2: WhatsApp as an Outreach Channel

The Outreaches.ai benchmarks report (2025) mentions WhatsApp as an emerging cold outreach channel alongside email and LinkedIn, with some regional data suggesting higher engagement in certain markets.

**Why I rejected it:** WhatsApp cold outreach sits in a legal and ethical grey zone in most markets. In the EU, it almost certainly violates GDPR without prior consent. In the US, unsolicited business messages on WhatsApp create a bad first impression — it feels invasive in a way that a cold email does not. The channel may work in specific geographies (Latin America, parts of Southeast Asia), but recommending it as a default tactic in a general B2B SaaS playbook is irresponsible.

**Source considered:** Outreaches.ai Cold Outreach Benchmarks 2025 — https://outreaches.ai/blog/cold-outreach-benchmarks

---

<a name="original"></a>
## My Original Ideas

### Original Idea: The "Hiring Signal + Pain Bridge" Opener

None of the sources I researched explicitly combined hiring signal data with a pain-framing opener in a single, structured template. Most sources either talk about signal-based list building OR pain-based copywriting — but not the bridge between them.

Here is the idea:

When a prospect's company is actively hiring SDRs, it is one of the highest-quality signals that they are building or scaling outbound. But instead of writing "I see you're hiring SDRs" (which every cold email tool now does automatically), you lead with the *implication* of that signal — the pain it reveals:

> **Subject:** SDR ramp time
>
> Hi [Name],
>
> Most teams hiring their first SDRs underestimate how long ramp takes — 3 months before they're productive is optimistic, 6 months is common.
>
> We help [ICP] compress that to 6 weeks with [specific mechanism].
>
> Worth 10 minutes to see if it applies to you?

**Why this could work:** It uses the hiring signal as research, not as a pickup line. The prospect doesn't know you saw their job posting — they just see someone who understands a pain they are actively experiencing. The "enemy" (slow SDR ramp) is real, timely, and felt. The offer is specific. The CTA is small.

This combines Belal Batrawy's "enemy" framework, Nick Abraham's offer specificity principles, and ColdIQ's signal-based targeting — but the specific combination is not something I found explicitly stated anywhere in the research.

---

<a name="weaknesses"></a>
## Weaknesses of This Playbook

I want to be honest about what this playbook does not solve and what assumptions it makes that may not hold.

**1. It assumes you already have a validated offer.**
This playbook does not teach product-market fit. If your SaaS product does not solve a real problem, no amount of cold outreach infrastructure will generate sustainable revenue. The playbook will help you discover that faster — but it won't fix it.

**2. The personalisation recommendations are time-intensive.**
The tactics recommended here — custom hooks, Fibonacci sequencing, LinkedIn warming — require real time per prospect. A solo founder cannot do this for 500 prospects a week. The playbook works best for focused, high-intent campaigns of 50–200 prospects per week, not mass blasting.

**3. Deliverability advice changes fast.**
Email providers update their spam filters constantly. The DNS setup and warm-up guidance in this playbook reflects 2024–2025 best practice. In 12 months, some of it may be outdated. Always cross-reference with current sources before launching a new campaign.

**4. The LinkedIn tactics depend on your network and profile.**
Jack Reamer's 48% positive reply rate is not a universal result. It is achieved by practitioners with strong, optimised LinkedIn profiles and established credibility in their niche. A brand-new LinkedIn profile with no posts and no connections will not get the same results.

**5. None of this has been tested by me personally.**
I am a researcher, not a practitioner. This playbook is built from synthesising the experience of people who have run these campaigns. The frameworks are credible and sourced, but I have not personally run A/B tests on these variables. Treat it as a strong starting hypothesis, not a proven playbook.

---

<a name="not-recommended"></a>
## Who I Would NOT Recommend Following and Why

### Morgan Williams — with a caveat

I want to be careful here, because Morgan Williams produces genuinely good interview content through *Hey {First Name}*. The podcast is worth listening to for the guests he brings on. However, I would not recommend following Morgan Williams as a primary source for execution-level guidance.

**The reason:** Morgan is a curator and interviewer, not an active campaign operator. His LinkedIn content is lighter on tactical depth compared to Nick Abraham or Belal Batrawy. When building a playbook, you want to learn from people who are running campaigns this week — not people who are talking to people who are running campaigns.

This is not a criticism of his character or the quality of his platform. It is a practical observation: if you have limited time to follow cold outreach content, spend it on Nick Abraham, Belal Batrawy, and ColdIQ — all of whom post execution-level frameworks from live campaigns. Use Morgan's podcast as a supplementary source, not a primary one.

**The nuance:** If you are a beginner and want to understand the landscape before diving into execution, Morgan's podcast is an excellent starting point precisely because it is curated and accessible. Once you have a foundational understanding, graduate to the more technical practitioners.

---

## Quick Reference: The Full System

```
Phase 1: Foundation
└── Define ICP (specific persona, company size, tech stack, signals)
└── Build offer (one service + quantified result + risk reversal)
└── Identify the "enemy" (the pain they already feel)

Phase 2: Infrastructure
└── Buy 3–5 secondary domains
└── Configure SPF, DKIM, DMARC on each
└── Warm up for 3–4 weeks before high-volume sends
└── Rotate across 3–5 inboxes per domain

Phase 3: List Building
└── Use Clay to filter by intent signals (hiring, funding, tech stack)
└── Target 50–200 high-signal prospects per week
└── Verify all email addresses before sending

Phase 4: Copywriting
└── Structure: Hook → Problem → Solution → Soft CTA
└── Subject line: mimic internal email
└── Length: 2–3 sentences per email
└── Voice: human, specific, no fluff

Phase 5: Sequencing
└── 4-step email sequence over 14 days
└── Add LinkedIn: connect → engage → email → DM follow-up
└── Fibonacci spacing for follow-ups
└── Creative touches (Loom video) for top 20–30 accounts

Phase 6: Optimisation
└── Max 30–50 emails/inbox/day
└── Track reply rate, not open rate
└── A/B test one variable per week
└── Maintain and honour DNC list
```

---

*This playbook was built from research collected in April 2025. Sources are linked inline throughout. For the full annotated source list, see [/research/sources.md](research/sources.md).*
