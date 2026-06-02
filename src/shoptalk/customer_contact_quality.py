def contact_quality_score(phone: str | None = None, email: str | None = None, channel_id: str | None = None) -> int:
    score = 0
    if phone:
        score += 45
    if email:
        score += 25
    if channel_id:
        score += 30
    return min(score, 100)


def contact_quality_label(score: int) -> str:
    if score >= 80:
        return "strong"
    if score >= 45:
        return "usable"
    return "weak"
