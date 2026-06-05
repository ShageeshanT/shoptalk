from __future__ import annotations

def channel_icon_label(channel: str) -> str:
    icons={"whatsapp":"WhatsApp","telegram":"Telegram","manual":"Manual"}
    return icons.get(channel.lower(), channel.title())