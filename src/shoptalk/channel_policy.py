from __future__ import annotations

SUPPORTED_REPLY_CHANNELS = {"whatsapp", "manual", "telegram", "email"}
AUTOMATED_REPLY_CHANNELS = {"whatsapp", "telegram", "email"}


def normalize_channel(channel: str | None) -> str:
    if not channel:
        return "manual"
    return channel.strip().lower().replace(" ", "_")


def can_send_automated_reply(channel: str | None) -> bool:
    return normalize_channel(channel) in AUTOMATED_REPLY_CHANNELS


def channel_policy_label(channel: str | None) -> str:
    normalized = normalize_channel(channel)
    if normalized not in SUPPORTED_REPLY_CHANNELS:
        return "unsupported_channel"
    if normalized == "manual":
        return "manual_approval_only"
    return "automated_with_approval"
