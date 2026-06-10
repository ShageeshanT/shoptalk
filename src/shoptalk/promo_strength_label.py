from __future__ import annotations

def promo_strength_label(score: int) -> str:
    try:
        value = int(score)
    except (TypeError, ValueError):
        value = 0
    if value >= 80:
        return 'Strong promo'
    if value >= 50:
        return 'Good promo'
    if value >= 20:
        return 'Weak promo'
    return 'No promo'
