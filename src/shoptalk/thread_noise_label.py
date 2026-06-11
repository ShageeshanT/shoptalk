"""Small seller-facing helper for thread noise label."""

from __future__ import annotations


def classify_thread_noise(messages: int | float | bool) -> str:
    """Return a compact dashboard label for thread noise label."""
    return "Quiet" if messages <= 2 else "Active" if messages <= 12 else "Noisy"
