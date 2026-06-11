"""Small seller-facing helper for checkout readiness label."""

from __future__ import annotations


def classify_checkout_readiness(completed_steps: int | float | bool) -> str:
    """Return a compact dashboard label for checkout readiness label."""
    return "Blocked" if completed_steps < 2 else "Almost ready" if completed_steps < 5 else "Ready"
