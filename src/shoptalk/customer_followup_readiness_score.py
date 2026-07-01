from __future__ import annotations


def customer_followup_readiness_score(has_reason, has_offer, has_deadline, has_channel, has_owner) -> int:
    checks = (has_reason, has_offer, has_deadline, has_channel, has_owner)
    return min(sum(20 for check in checks if check), 100)
