"""Channel adapters and helpers for messaging platforms."""

CHANNEL_ALIASES = {
    "wa": "whatsapp",
    "whats app": "whatsapp",
    "whatsapp": "whatsapp",
    "ig": "instagram",
    "instagram": "instagram",
    "manual": "manual",
    "telegram": "telegram",
}


def normalize_channel(value: str) -> str:
    return CHANNEL_ALIASES.get(value.strip().lower(), value.strip().lower())
