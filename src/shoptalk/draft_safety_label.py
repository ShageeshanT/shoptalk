from __future__ import annotations

def draft_safety_label(text: str) -> str:
    lowered = text.lower()
    if any(word in lowered for word in ("idiot", "stupid")): return "needs review"
    return "safe"
