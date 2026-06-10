from __future__ import annotations

def whatsapp_optin_label(status: str) -> str:
    normalized = (status or "").strip().lower().replace(" ", "_")
    labels = {
        'opted_in': 'WhatsApp opted in',
        'pending': 'WhatsApp pending',
        'opted_out': 'WhatsApp opted out',
    }
    return labels.get(normalized, 'WhatsApp unknown')
