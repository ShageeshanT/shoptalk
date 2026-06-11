"""Small seller-facing helper for order risk label."""

from __future__ import annotations


def classify_order_risk(risk_score: int | float | bool) -> str:
    """Return a compact dashboard label for order risk label."""
    return "Low" if risk_score < 30 else "Medium" if risk_score < 70 else "High"
