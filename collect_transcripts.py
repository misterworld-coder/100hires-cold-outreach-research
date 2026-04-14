"""
collect_transcripts.py
----------------------
Script to collect YouTube transcripts from expert channels
using youtube-transcript-api (no API key needed for public videos).

Usage:
    pip install youtube-transcript-api
    python collect_transcripts.py

Output:
    Saves transcripts to /research/youtube-transcripts/ as .txt files
"""

import os
import json
from youtube_transcript_api import YouTubeTranscriptApi, TranscriptsDisabled, NoTranscriptFound

# Expert YouTube video IDs to collect
# Format: { "expert_name": ["video_id_1", "video_id_2", ...] }
EXPERT_VIDEOS = {
    "alex-berman": [
        # Add video IDs from https://www.youtube.com/@AlexBerman
        # Example: "dQw4w9WgXcQ" is the video ID from youtube.com/watch?v=dQw4w9WgXcQ
    ],
    "coldiq": [
        # Add video IDs from https://www.youtube.com/@ColdIQ
    ],
    "jack-reamer": [
        # Add video IDs from Jack Reamer's Cold Outreach Podcast YouTube appearances
    ],
}

OUTPUT_DIR = os.path.join(os.path.dirname(__file__), "research", "youtube-transcripts")


def get_transcript(video_id: str) -> str | None:
    """Fetch transcript for a YouTube video ID."""
    try:
        transcript_data = YouTubeTranscriptApi.get_transcript(video_id)
        # Join all text segments into a single string
        full_text = " ".join([entry["text"] for entry in transcript_data])
        return full_text
    except TranscriptsDisabled:
        print(f"  ⚠️  Transcripts disabled for video {video_id}")
        return None
    except NoTranscriptFound:
        print(f"  ⚠️  No transcript found for video {video_id}")
        return None
    except Exception as e:
        print(f"  ❌  Error for video {video_id}: {e}")
        return None


def save_transcript(expert: str, video_id: str, transcript: str):
    """Save transcript to file."""
    filename = f"{expert}-{video_id}.txt"
    filepath = os.path.join(OUTPUT_DIR, filename)
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(f"Expert: {expert}\n")
        f.write(f"Video ID: {video_id}\n")
        f.write(f"URL: https://www.youtube.com/watch?v={video_id}\n")
        f.write("=" * 60 + "\n\n")
        f.write(transcript)
    print(f"  ✅  Saved: {filename}")


def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    print("🎬 Starting YouTube transcript collection...\n")

    total_collected = 0
    for expert, video_ids in EXPERT_VIDEOS.items():
        print(f"📺 Processing: {expert}")
        if not video_ids:
            print(f"  ⏭️  No video IDs configured yet for {expert}. Add them to EXPERT_VIDEOS.\n")
            continue

        for video_id in video_ids:
            print(f"  Fetching transcript for video: {video_id}")
            transcript = get_transcript(video_id)
            if transcript:
                save_transcript(expert, video_id, transcript)
                total_collected += 1

        print()

    print(f"✅ Done. Collected {total_collected} transcripts.")
    print(f"📁 Saved to: {OUTPUT_DIR}")


if __name__ == "__main__":
    main()
