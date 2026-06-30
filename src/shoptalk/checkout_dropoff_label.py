"""Compact seller dashboard helper for checkout dropoff risk."""

from __future__ import annotations


def classify_checkout_dropoff(idle_minutes: int | float) -> str:
    """Return a short seller-facing label for checkout dropoff risk."""
    return "Active checkout" if idle_minutes < 20 else "Nudge checkout" if idle_minutes < 90 else "Rescue checkout"
