"""Compact seller dashboard helper for human handoff SLA."""

from __future__ import annotations


def classify_handoff_sla(minutes_waiting: int | float) -> str:
    """Return a short seller-facing label for human handoff SLA."""
    return "Normal handoff" if minutes_waiting < 15 else "Watch handoff" if minutes_waiting < 45 else "Urgent handoff"
