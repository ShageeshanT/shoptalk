from __future__ import annotations


def seller_response_load_score(pending_replies, urgent_replies, ai_drafts_ready, staff_online, after_hours) -> int:
    score = min(pending_replies * 8, 40) + min(urgent_replies * 15, 30)
    score -= min(ai_drafts_ready * 10, 20)
    if not staff_online:
        score += 15
    if after_hours:
        score += 10
    return max(0, min(score, 100))
