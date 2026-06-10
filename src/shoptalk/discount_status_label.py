from __future__ import annotations

def discount_status_label(percent: int) -> str:
    try:
        value = int(percent)
    except (TypeError, ValueError):
        value = 0
    if value >= 30:
        return 'Heavy discount'
    if value >= 10:
        return 'Standard discount'
    if value >= 1:
        return 'Small discount'
    return 'No discount'
