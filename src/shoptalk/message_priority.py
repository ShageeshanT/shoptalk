def message_priority_score(urgency: str, sentiment: str, needs_reply: bool) -> int:
    score = 0
    if needs_reply:
        score += 30
    if urgency == 'high':
        score += 50
    elif urgency == 'normal':
        score += 20
    if sentiment == 'negative':
        score += 20
    return min(score, 100)
