from __future__ import annotations

def conversation_priority_score(intent_score: int, wait_minutes: int, order_value: float) -> int:
    wait_boost = min(30, max(0, wait_minutes) // 10)
    value_boost = min(25, int(max(0.0, order_value) // 1000))
    return max(0, min(100, intent_score + wait_boost + value_boost))
