from __future__ import annotations

def review_status_label(rating: int) -> str:
    try:
        value = int(rating)
    except (TypeError, ValueError):
        value = 0
    if value >= 5:
        return 'Excellent review'
    if value >= 4:
        return 'Good review'
    if value >= 3:
        return 'Mixed review'
    return 'Needs attention'
