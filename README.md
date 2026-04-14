# Cold Outreach Pipeline for B2B SaaS — Research Project

> **Context:** This research project was built as part of a portfolio task for 100Hires. The goal is to collect and organise high-signal content from active B2B SaaS cold outreach practitioners to support the development of a real outbound playbook.

---

## Why Cold Outreach?

Cold outreach is one of the most operationally rich topics in B2B SaaS go-to-market — covering list building, copywriting, deliverability, multichannel sequencing, and offer positioning. It's also a field where the gap between practitioners and theorists is enormous. Generic "10 cold email tips" content is everywhere. Actual system-level knowledge from people running campaigns at scale is rare and high-value.

This research focuses exclusively on people who show their work.

---

## Tools Installed & Setup Completed

| Tool | Purpose | Status |
|------|---------|--------|
| Cursor IDE | AI-powered code editor | ✅ Installed |
| Claude Code (Cursor extension) | AI coding assistant | ✅ Installed |
| Codex (Cursor extension) | Code generation | ✅ Installed |
| Git + GitHub | Version control | ✅ Active |
| Python 3 | Scripting for API collection | ✅ Available |
| youtube-transcript-api | YouTube transcript collection | ✅ pip install ready |

---

## Repository Structure

```
/
├── README.md                          ← This file
├── collect_transcripts.py             ← Script to pull YouTube transcripts via API
└── research/
    ├── sources.md                     ← All 10 experts with annotations
    ├── linkedin-posts/
    │   ├── nick-abraham.md            ← 5 posts collected + analysed
    │   ├── belal-batrawy.md           ← Posts + frameworks
    │   └── vin-matano.md             ← Posts + creative prospecting notes
    ├── youtube-transcripts/
    │   ├── alex-berman.md            ← Video index + transcript collection notes
    │   └── coldiq.md                 ← Video index + system walkthroughs
    └── other/
        └── podcast-notes.md          ← Cold Outreach Podcast + Hey {First Name} summaries
```

---

## The 10 Experts Selected

These were chosen for practitioner credibility — not follower counts or SEO rankings.

| # | Expert | Why Selected | Primary Channel |
|---|--------|-------------|-----------------|
| 1 | **Nick Abraham** | Sends 1M+ emails/month, runs 3 cold email SaaS tools | LinkedIn |
| 2 | **Jack Reamer** | 48% positive reply rates, CEO of SalesBread | LinkedIn + Podcast |
| 3 | **Alex Berman** | 100K+ YT subs, authored Cold Email Manifesto, exited 5 SaaS | YouTube |
| 4 | **Belal Batrawy** | 15+ yrs, $15M+ generated, "enemy-based" methodology | LinkedIn |
| 5 | **Vin Matano** | 6 yrs as practitioner at Demandbase before becoming a founder | LinkedIn |
| 6 | **Jeremy Chatelaine** | CEO of QuickMail, deliverability expert, Cold Outreach Podcast | Podcast |
| 7 | **Morgan Williams** | Host of *Hey {First Name}*, 130+ practitioner interviews | Podcast |
| 8 | **Ricky Pearl** | Outbound team builder, evergreen frameworks | LinkedIn |
| 9 | **Yassin Hariss** | Deliverability specialist, 14M+ emails tracked | LinkedIn |
| 10 | **ColdIQ (V. Paquette)** | Agency with documented case studies, Clay/Apollo system walkthroughs | YouTube |

Full annotations in [`/research/sources.md`](research/sources.md)

---

## What's Been Collected

### LinkedIn Posts
- **Nick Abraham:** 5 posts covering sequence structure, deliverability, offer-market fit, volume strategy, and CTA frameworks
- **Belal Batrawy:** 3 posts covering enemy-based messaging, Mic Drop cold call method, and email playbook
- **Vin Matano:** 4 posts covering creative prospecting, the four-part email framework, and multi-channel sequencing

### YouTube Content
- **Alex Berman:** 4 videos indexed with frameworks extracted (transcripts to be pulled via API — see `collect_transcripts.py`)
- **ColdIQ:** 4 videos indexed covering Clay workflows, signal-based outreach, and deliverability setup

### Podcast Notes
- **Cold Outreach Podcast** (Jack Reamer + Jeremy Chatelaine): Key episode summaries
- **Hey {First Name}** (Morgan Williams): Episodes 132 and selected others summarised

---

## How to Collect More Transcripts

```bash
# 1. Install dependency
pip install youtube-transcript-api

# 2. Add video IDs to collect_transcripts.py (EXPERT_VIDEOS dict)
#    Get video IDs from YouTube URLs: youtube.com/watch?v=VIDEO_ID

# 3. Run the script
python collect_transcripts.py

# Transcripts save to /research/youtube-transcripts/
```

---

## Key Themes Emerging from the Research

1. **Offer-market fit > copywriting** — Every top practitioner agrees that a mediocre email to the right ICP outperforms a great email to a vague audience
2. **Deliverability is infrastructure** — Treat domains like servers. DNS setup, IP diversity, warm-up timing are make-or-break
3. **Multi-channel is table stakes** — Email + LinkedIn + phone is the baseline in 2024–2025
4. **Signal-based targeting is the frontier** — Hiring signals, funding events, tech stack installs are turning cold outreach into warm outreach
5. **Volume needs targeting to work** — Scaling bad emails makes things worse; scaling good targeting with decent emails works

---

## Commit History

- `init`: Repo setup, README, tools documentation
- `feat: add sources.md with 10 annotated experts`
- `feat: add linkedin posts for nick-abraham, belal-batrawy, vin-matano`
- `feat: add youtube transcript index for alex-berman and coldiq`
- `feat: add podcast notes and transcript collection script`
