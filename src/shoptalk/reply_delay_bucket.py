from __future__ import annotations

def reply_delay_bucket(minutes: int) -> str:
    if minutes < 15: return "healthy"
    if minutes < 120: return "watch"
    return "late"
