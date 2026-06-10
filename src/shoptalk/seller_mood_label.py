from __future__ import annotations

def seller_mood_label(score: int) -> str:
    try:
        value = int(score)
    except (TypeError, ValueError):
        value = 0
    if value >= 80:
        return 'Great day'
    if value >= 50:
        return 'Steady day'
    if value >= 20:
        return 'Needs attention'
    return 'Rough day'
