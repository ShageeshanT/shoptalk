"""Compact seller dashboard helper for message noise level."""

from __future__ import annotations


def classify_message_noise(non_order_messages: int | float) -> str:
    """Return a short seller-facing label for message noise level."""
    return "Clean thread" if non_order_messages < 3 else "Some noise" if non_order_messages < 8 else "Noisy thread"
