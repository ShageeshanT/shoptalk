from __future__ import annotations

def attachment_status_label(count: int) -> str:
    try:
        value = int(count)
    except (TypeError, ValueError):
        value = 0
    if value >= 3:
        return 'Many attachments'
    if value >= 1:
        return 'Has attachment'
    if value >= 0:
        return 'No attachments'
    return 'No attachments'
