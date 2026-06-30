from __future__ import annotations

def message_source_label(channel: str) -> str:
    value = channel.strip().lower()
    if value in {"wa", "whatsapp"}: return "WhatsApp"
    if value == "telegram": return "Telegram"
    return "Manual"
