from __future__ import annotations

def contact_channel_badge(channel: str) -> str:
    normalized = (channel or "").strip().lower().replace(" ", "_")
    labels = {
        'whatsapp': 'WhatsApp contact',
        'email': 'Email contact',
        'phone': 'Phone contact',
    }
    return labels.get(normalized, 'No contact')
