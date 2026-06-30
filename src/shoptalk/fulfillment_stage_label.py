from __future__ import annotations

def fulfillment_stage_label(paid: bool, ready: bool, delivered: bool) -> str:
    if delivered: return "completed"
    if ready: return "ready"
    if paid: return "prepare"
    return "collect payment"
