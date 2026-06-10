from __future__ import annotations

def customer_trust_label(score: int) -> str:
    try:
        value = int(score)
    except (TypeError, ValueError):
        value = 0
    if value >= 80:
        return 'Trusted customer'
    if value >= 50:
        return 'Normal trust'
    if value >= 20:
        return 'Low trust'
    return 'Unknown trust'
