def normalize_priority_label(score: int) -> str:
    if score >= 80:
        return "critical"
    if score >= 50:
        return "high"
    if score >= 20:
        return "normal"
    return "low"


def message_priority_score(urgency: str, sentiment: str, needs_reply: bool) -> int:
    score = 0
    if needs_reply:
        score += 30
    if urgency == "high":
        score += 50
    elif urgency == "normal":
        score += 20
    if sentiment == "negative":
        score += 20
    return min(score, 100)


def message_priority_label(urgency: str, sentiment: str, needs_reply: bool) -> str:
    return normalize_priority_label(message_priority_score(urgency, sentiment, needs_reply))
