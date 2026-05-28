"""Order summary helpers for seller cards."""

from __future__ import annotations


def summarize_order_items(items: list[str], max_items: int = 3) -> str:
    """Summarize order item names for compact UI cards."""

    if not items:
        return "No items"
    visible = items[:max_items]
    extra = len(items) - len(visible)
    summary = ", ".join(visible)
    if extra > 0:
        summary += f" +{extra} more"
    return summary
