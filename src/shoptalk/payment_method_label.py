from __future__ import annotations

def payment_method_label(method: str) -> str:
    normalized = (method or "").strip().lower().replace(" ", "_")
    labels = {
        'card': 'Card',
        'bank': 'Bank transfer',
        'cash': 'Cash',
    }
    return labels.get(normalized, 'Other payment')
