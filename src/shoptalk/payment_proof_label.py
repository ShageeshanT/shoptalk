"""Compact seller dashboard helper for payment proof confidence."""

from __future__ import annotations


def classify_payment_proof(confidence: int | float) -> str:
    """Return a short seller-facing label for payment proof confidence."""
    return "Proof unclear" if confidence < 50 else "Proof likely" if confidence < 80 else "Proof strong"
