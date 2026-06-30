from __future__ import annotations

def customer_reply_tone(text: str) -> str:
    words = text.lower()
    if any(token in words for token in ("angry", "complaint", "wrong", "refund")):
        return "calm recovery"
    if any(token in words for token in ("thanks", "great", "love")):
        return "warm appreciation"
    return "clear and helpful"
