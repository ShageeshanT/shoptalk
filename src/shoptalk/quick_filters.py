"""Quick filter helpers for dashboard tabs."""

from __future__ import annotations


def quick_filter_label(filter_key: str) -> str:
    """Return a readable label for a quick filter key."""

    labels = {
        "needs_reply": "Needs reply",
        "payment_pending": "Payment pending",
        "today": "Today",
        "vip": "VIP customers",
    }
    return labels.get(filter_key, filter_key.replace("_", " ").title())
