"""Revenue summary helpers."""

from __future__ import annotations


def revenue_summary(totals: list[float]) -> dict[str, float | int]:
    """Return compact revenue summary metrics."""

    count = len(totals)
    total = round(sum(totals), 2)
    average = round(total / count, 2) if count else 0.0
    return {"count": count, "total": total, "average": average}
