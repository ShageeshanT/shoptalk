"""Small seller-facing helper for message intent label."""

from __future__ import annotations


def classify_message_intent(confidence: int | float | bool) -> str:
    """Return a compact dashboard label for message intent label."""
    return "Unclear" if confidence < 40 else "Likely" if confidence < 75 else "Clear"
