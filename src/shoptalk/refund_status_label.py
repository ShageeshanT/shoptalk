from __future__ import annotations

def refund_status_label(eligible: bool) -> str:
    return "Refund eligible" if eligible else "Refund not eligible"