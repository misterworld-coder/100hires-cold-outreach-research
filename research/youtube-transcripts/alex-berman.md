# YouTube Content — Alex Berman

**Channel:** https://www.youtube.com/@AlexBerman
**Collected:** April 2025
**Subscribers:** 100K+
**Why selected:** Longest-running cold email educator on YouTube with verifiable business outcomes (exited 5 SaaS companies, authored The Cold Email Manifesto, ran Experiment27 agency). Hundreds of tactical videos with real campaign walkthroughs.

---

## Video 1 — "How I Sent 1 Million Cold Emails" (Foundational)

**Topic areas covered:**
- Why volume beats cleverness in cold email
- Domain setup and infrastructure at scale
- How to build lists for B2B SaaS companies specifically
- The role of cold email in the full agency revenue model

**Key quotes/frameworks:**
- "The goal isn't to craft the perfect email — the goal is to send 10x more emails than your competition with a good-enough email."
- The "3 Buckets" system: Targeting → Copy → Infrastructure. Most people over-invest in copy and under-invest in the other two.

**Transcript status:** To be collected via Supadata API
**URL:** https://www.youtube.com/@AlexBerman (search: "million cold emails")

---

## Video 2 — B2B Cold Email Teardowns (Series)

**Topic:** Real cold emails submitted by viewers, dissected live
**Why valuable:** Shows exactly what breaks cold emails in practice — subject lines, CTA structure, ICP mismatch, length

**Transcript status:** To be collected via Supadata API
**URL:** https://www.youtube.com/@AlexBerman (search: "cold email teardown")

---

## Video 3 — How to Use YouTube for B2B Lead Generation

**Topic:** Using content as a warm-up channel before cold outreach
**Key insight:** Alex used an event ("What We Learned Sending 1M Cold Emails") promoted via event directories rather than cold email — generated warm leads at $20/ticket
**Cross-reference:** Also discussed on The Salesman Podcast (https://salesman.com/how-to-generate-more-sales-leads-using-youtube-with-alex-berman/)

**Transcript status:** To be collected via Supadata API

---

## Video 4 — The Baking Method (Long-Term Follow-Up)

**Topic:** Year-long cold email follow-up sequence for B2B
**Why unique:** Most practitioners focus on 3–5 touch sequences. Alex's "Baking Method" reframes follow-up as a 12-month nurture, not an annoyance.
**Key insight:** Prospects often convert 6–12 months after first contact. A follow-up system that respects this timeline dramatically changes pipeline math.

**Transcript status:** To be collected via Supadata API

---

## API Collection Notes

To pull transcripts programmatically:

```python
# Using Supadata API (free tier available)
# Docs: https://supadata.ai

import requests

SUPADATA_API_KEY = "your_key_here"
VIDEO_ID = "video_id_here"  # extract from YouTube URL

response = requests.get(
    f"https://api.supadata.ai/v1/youtube/transcript",
    params={"videoId": VIDEO_ID},
    headers={"x-api-key": SUPADATA_API_KEY}
)

transcript = response.json()
```

Alternative: youtube-transcript-api (Python, no API key needed for public videos)
```bash
pip install youtube-transcript-api
python -c "from youtube_transcript_api import YouTubeTranscriptApi; print(YouTubeTranscriptApi.get_transcript('VIDEO_ID'))"
```
