"""Compact seller dashboard helper for promotion fit."""

from __future__ import annotations


def classify_promo_fit(margin_percent: int | float) -> str:
    """Return a short seller-facing label for promotion fit."""
    return "Skip promo" if margin_percent < 15 else "Light promo" if margin_percent < 35 else "Strong promo"
