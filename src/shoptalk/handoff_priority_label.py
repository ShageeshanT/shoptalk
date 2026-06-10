from __future__ import annotations

def handoff_priority_label(priority: int) -> str:
    try:
        value = int(priority)
    except (TypeError, ValueError):
        value = 0
    if value >= 3:
        return 'Urgent handoff'
    if value >= 2:
        return 'Normal handoff'
    if value >= 1:
        return 'Low handoff'
    return 'No handoff'
