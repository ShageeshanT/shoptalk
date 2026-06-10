from __future__ import annotations

def conversation_health_label(score: int) -> str:
    try:
        value = int(score)
    except (TypeError, ValueError):
        value = 0
    if value >= 80:
        return 'Healthy conversation'
    if value >= 50:
        return 'Needs follow-up'
    if value >= 20:
        return 'At risk'
    return 'Cold conversation'
