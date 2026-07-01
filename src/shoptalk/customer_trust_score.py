from __future__ import annotations


def customer_trust_score(successful_orders, failed_deliveries, unresolved_complaints) -> int:
    score = min(successful_orders * 12, 80)
    score -= min(failed_deliveries * 15, 30)
    score -= min(unresolved_complaints * 20, 40)
    return max(0, min(score, 100))
