from __future__ import annotations


def return_risk_score(wrong_size_reports, damage_reports, unclear_photos, days_since_delivery, resolved) -> int:
    if resolved:
        return 0
    score = min(wrong_size_reports * 18, 36)
    score += min(damage_reports * 22, 44)
    if unclear_photos:
        score += 10
    if days_since_delivery >= 7:
        score += 10
    return min(score, 100)
