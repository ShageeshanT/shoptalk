"""Lead scoring helpers for customer conversations."""

from __future__ import annotations


def lead_score(text: str) -> int:
    """Return a small intent score from message wording."""

    normalized = text.lower()
    score = 0
    if any(word in normalized for word in ("price", "how much", "available")):
        score += 1
    if any(word in normalized for word in ("order", "book", "buy")):
        score += 2
    if any(word in normalized for word in ("today", "now", "urgent")):
        score += 1
    return score


def lead_label(text: str) -> str:
    """Return a lead label from message wording."""

    score = lead_score(text)
    if score >= 3:
        return "hot"
    if score >= 1:
        return "warm"
    return "cold"
