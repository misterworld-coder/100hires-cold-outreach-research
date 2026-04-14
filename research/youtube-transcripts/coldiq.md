# YouTube Content — ColdIQ (Vincent Paquette)

**Channel:** https://www.youtube.com/@ColdIQ
**Collected:** April 2025
**Why selected:** ColdIQ is one of the most technically advanced outbound agencies active today. Their YouTube channel publishes system-level walkthroughs of Clay, Apollo, signal-based prospecting, and AI sequencing — not strategy fluff, but literal step-by-step workflows.

---

## Video 1 — Full Cold Outreach Stack Walkthrough

**Topic:** Every tool in ColdIQ's outbound stack for 1,000+ prospects/month
**Tools covered:** Clay, Apollo, Instantly, Lemlist, domain warming systems
**Why valuable:** Shows the actual infrastructure of a modern outbound campaign — not just tactics, but the full system architecture

**Key frameworks shared:**
- Signal-based list building (intent data, hiring signals, funding rounds, tech stack installs)
- Inbox rotation strategy across multiple domains
- AI personalisation at scale without sacrificing reply quality

**Transcript status:** To be collected via Supadata API
**URL:** https://www.youtube.com/@ColdIQ

---

## Video 2 — Clay Workflow for B2B Outreach

**Topic:** How to use Clay.com to build hyper-targeted prospect lists
**Why valuable:** Clay has become the dominant tool for signal-based outbound. This video shows the exact workflow — from data sources to enrichment to export.

**Transcript status:** To be collected via Supadata API

---

## Video 3 — Signal-Based Outreach: 4x Higher Conversion

**Topic:** Using buying intent signals to identify warm prospects before they raise their hand
**Signals covered:**
- Job postings (hiring SDRs = actively building outbound)
- Tech stack installs (switching away from a competitor)
- Funding events (newly funded = budget to spend)
- LinkedIn activity (engaging with relevant content)

**Key stat from ColdIQ content:** Intent-driven outreach achieves 4x higher conversion rates vs. cold list blasting

**Transcript status:** To be collected via Supadata API

---

## Video 4 — Deliverability Setup from Scratch

**Topic:** Domain purchase, DNS configuration, inbox warming, and sending limits for new outbound infrastructure
**Why valuable:** Covers the technical setup that most beginners skip — which is why most beginners' emails land in spam

**Transcript status:** To be collected via Supadata API

---

## Agency Case Studies (for /research/other/)

ColdIQ publishes documented case studies on their site:
- Deliverability setup for a new domain → inbox placement improvements
- Signal-based outreach for a SaaS client → pipeline numbers
- Clay + Apollo workflow for a 500-prospect/week campaign

**Source:** https://coldiq.com/case-studies (to be fetched and stored in /research/other/coldiq-case-studies.md)

---

## API Collection Notes

```python
# ColdIQ YouTube Channel ID: UCxxxxxxxx (to be confirmed via YouTube API)
# Use Supadata or youtube-transcript-api to pull video transcripts

from youtube_transcript_api import YouTubeTranscriptApi

# Example video IDs from ColdIQ channel
video_ids = [
    "VIDEO_ID_1",  # Full stack walkthrough
    "VIDEO_ID_2",  # Clay workflow
]

for vid in video_ids:
    transcript = YouTubeTranscriptApi.get_transcript(vid)
    # Save to file
```
