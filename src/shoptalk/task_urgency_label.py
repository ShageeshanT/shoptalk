from __future__ import annotations

def task_urgency_label(hours: int) -> str:
    try:
        value = int(hours)
    except (TypeError, ValueError):
        return 'Later task'
    if value <= 1:
        return 'Immediate task'
    if value <= 6:
        return 'Today task'
    if value <= 24:
        return 'Tomorrow task'
    return 'Later task'
