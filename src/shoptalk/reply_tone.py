"""Reply tone selection for seller approved drafts."""

from __future__ import annotations


def choose_reply_tone(text: str) -> str:
    """Choose a safe reply tone from customer text."""

    normalized = text.lower()
    if any(word in normalized for word in ("angry", "refund", "complain", "bad")):
        return "apologetic"
    if any(word in normalized for word in ("thanks", "thank you", "great")):
        return "warm"
    if "?" in text:
        return "helpful"
    return "neutral"
