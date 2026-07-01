from __future__ import annotations

def customer_patience_score(wait_minutes: int, previous_delays: int, friendly_replies: int) -> int:
    raw_score = 100 - wait_minutes - previous_delays * 12 + friendly_replies * 5
    return max(0, min(100, int(raw_score)))
