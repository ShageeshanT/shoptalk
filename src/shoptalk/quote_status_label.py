from __future__ import annotations

def quote_status_label(status: str) -> str:
    normalized = (status or "").strip().lower().replace(" ", "_")
    labels = {
        'accepted': 'Quote accepted',
        'sent': 'Quote sent',
        'expired': 'Quote expired',
    }
    return labels.get(normalized, 'Quote draft')
