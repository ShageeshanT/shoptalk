from __future__ import annotations

def invoice_status_label(status: str) -> str:
    normalized = (status or "").strip().lower().replace(" ", "_")
    labels = {
        'sent': 'Invoice sent',
        'paid': 'Invoice paid',
        'overdue': 'Invoice overdue',
    }
    return labels.get(normalized, 'Invoice draft')
