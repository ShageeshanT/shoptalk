from __future__ import annotations

def payment_due_label(is_due: bool, days: int=0) -> str:
    if not is_due: return "Payment not due"
    return "Payment due today" if days == 0 else f"Payment due in {days} day(s)"