from __future__ import annotations


def seller_health_score(
    *,
    open_followups: int,
    pending_payments: int,
    unanswered_messages: int,
) -> int:
    """Return a simple 0-100 score for the seller dashboard."""
    penalty = (open_followups * 8) + (pending_payments * 10) + (unanswered_messages * 12)
    return max(0, min(100, 100 - penalty))


def seller_health_label(score: int) -> str:
    if score >= 85:
        return "healthy"
    if score >= 60:
        return "needs_attention"
    return "at_risk"
