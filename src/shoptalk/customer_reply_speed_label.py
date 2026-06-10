from __future__ import annotations

def customer_reply_speed_label(minutes: int) -> str:
    try:
        value = int(minutes)
    except (TypeError, ValueError):
        return 'Slow reply'
    if value <= 5:
        return 'Instant reply'
    if value <= 60:
        return 'Same hour reply'
    if value <= 1440:
        return 'Same day reply'
    return 'Slow reply'
