from __future__ import annotations

def pickup_window_label(minutes: int) -> str:
    if minutes <= 0:
        return "now"
    if minutes <= 60:
        return "within the hour"
    if minutes <= 24 * 60:
        return "today"
    return "later"
