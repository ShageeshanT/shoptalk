from __future__ import annotations


def percentage_delta(current: float, previous: float) -> float | None:
    if previous == 0:
        return None
    return round(((current - previous) / previous) * 100, 2)


def trend_label(current: float, previous: float) -> str:
    delta = percentage_delta(current, previous)
    if delta is None:
        return "new_activity" if current > 0 else "no_activity"
    if delta > 0:
        return "up"
    if delta < 0:
        return "down"
    return "flat"
