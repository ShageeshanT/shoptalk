from __future__ import annotations

def customer_wait_label(minutes: int) -> str:
    if minutes <= 5: return "fast reply"
    if minutes <= 60: return "normal wait"
    return "slow reply"
