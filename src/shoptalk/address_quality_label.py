from __future__ import annotations

def address_quality_label(score: int) -> str:
    try:
        value = int(score)
    except (TypeError, ValueError):
        value = 0
    if value >= 80:
        return 'Clear address'
    if value >= 50:
        return 'Needs landmark'
    if value >= 20:
        return 'Needs confirmation'
    return 'Missing address'
