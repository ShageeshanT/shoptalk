from __future__ import annotations

def customer_note_status(count: int) -> str:
    try:
        value = int(count)
    except (TypeError, ValueError):
        value = 0
    if value >= 5:
        return 'Rich notes'
    if value >= 1:
        return 'Has notes'
    if value >= 0:
        return 'No notes'
    return 'No notes'
