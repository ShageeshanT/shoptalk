"""Conversation stage detection for seller inbox grouping."""

from __future__ import annotations


def detect_conversation_stage(text: str) -> str:
    """Return a simple stage label for a customer message."""

    normalized = text.lower()
    if any(word in normalized for word in ("paid", "payment", "deposit", "receipt")):
        return "payment"
    if any(word in normalized for word in ("deliver", "pickup", "address", "location")):
        return "fulfillment"
    if any(word in normalized for word in ("price", "available", "how much", "can i order")):
        return "ordering"
    return "general"
