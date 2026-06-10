from __future__ import annotations

def checkout_status_label(status: str) -> str:
    normalized = (status or "").strip().lower().replace(" ", "_")
    labels = {
        'ready': 'Checkout ready',
        'sent': 'Checkout sent',
        'paid': 'Checkout paid',
    }
    return labels.get(normalized, 'Checkout draft')
