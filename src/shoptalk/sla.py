def response_sla_label(priority_score: int) -> str:
    if priority_score >= 80:
        return 'reply_now'
    if priority_score >= 40:
        return 'reply_today'
    return 'monitor'
