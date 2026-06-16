"""WhatsApp Business API channel adapter."""

from __future__ import annotations

import logging
import time

from shoptalk.channels.base import BaseChannel, IncomingMessage, OutgoingMessage

logger = logging.getLogger(__name__)


class WhatsAppChannel(BaseChannel):
    """Adapter for the WhatsApp Business Cloud API.

    Handles webhook verification and message parsing.
    Sending is a stub until Phase 5 when the access token is configured.
    """

    def __init__(self, verify_token: str, access_token: str = "") -> None:
        self._verify_token = verify_token
        self._access_token = access_token

    @property
    def name(self) -> str:
        return "whatsapp"

    def verify_webhook(self, mode: str, token: str, challenge: str) -> str | None:
        """Verify a WhatsApp webhook subscription request.

        Returns the challenge string on success, None on failure.
        """
        if mode == "subscribe" and token == self._verify_token:
            return challenge
        return None

    def parse_webhook(self, payload: dict) -> list[IncomingMessage]:
        """Parse a WhatsApp Cloud API webhook payload."""
        messages: list[IncomingMessage] = []
        try:
            for entry in payload.get("entry", []):
                for change in entry.get("changes", []):
                    value = change.get("value", {})
                    for msg in value.get("messages", []):
                        if msg.get("type") != "text":
                            continue
                        messages.append(IncomingMessage(
                            channel=self.name,
                            sender_id=msg["from"],
                            sender_phone=msg["from"],
                            text=msg["text"]["body"],
                            timestamp=float(msg.get("timestamp", time.time())),
                            raw=msg,
                        ))
        except (KeyError, TypeError) as exc:
            logger.warning("Failed to parse WhatsApp payload: %s", exc)
        return messages

    async def send(self, message: OutgoingMessage) -> None:
        """Send a WhatsApp message. Stub — requires access token (Phase 5)."""
        if not self._access_token:
            logger.warning("WhatsApp send skipped: no access token configured")
            return
        # TODO: implement HTTP call to WhatsApp Cloud API in Phase 5
        logger.info("WhatsApp send to %s: %s", message.recipient_id, message.text[:50])
