from __future__ import annotations

def sentiment_badge(sentiment: str) -> str:
    return {"positive":"🙂 Positive","neutral":"😐 Neutral","negative":"⚠️ Negative"}.get(sentiment, "Unknown")