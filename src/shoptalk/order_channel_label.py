from __future__ import annotations

def order_channel_label(channel: str) -> str:
    normalized = (channel or "").strip().lower().replace(" ", "_")
    labels = {
        "whatsapp": "WhatsApp",
        "instagram": "Instagram",
        "facebook": "Facebook",
        "web": "Website",
        "store": "In-store",
    }
    return labels.get(normalized, "Manual")
