from __future__ import annotations

def sla_status_label(minutes: int) -> str:
    try:
        value = int(minutes)
    except (TypeError, ValueError):
        return 'Critical delay'
    if value <= 5:
        return 'Fast response'
    if value <= 30:
        return 'Within SLA'
    if value <= 120:
        return 'Slow response'
    return 'Critical delay'
