"""Abstract base class for messaging channel adapters."""

from __future__ import annotations

from abc import ABC, abstractmethod
from dataclasses import dataclass


@dataclass
class IncomingMessage:
    """Normalised representation of a message from any channel."""

    channel: str          # e.g. "whatsapp", "telegram"
    sender_id: str        # platform-specific sender identifier
    sender_phone: str     # E.164 phone number when available
    text: str             # raw message text
    timestamp: float      # Unix timestamp
    raw: dict             # original platform payload


@dataclass
class OutgoingMessage:
    """A reply to be sent back to the customer."""

    recipient_id: str
    text: str


class BaseChannel(ABC):
    """Abstract adapter for a messaging channel.

    Subclasses implement platform-specific parsing and sending logic.
    The rest of the application works only with IncomingMessage and
    OutgoingMessage, keeping business logic channel-agnostic.
    """

    @property
    @abstractmethod
    def name(self) -> str:
        """Return the channel identifier, e.g. "whatsapp"."""

    @abstractmethod
    def parse_webhook(self, payload: dict) -> list[IncomingMessage]:
        """Parse a raw webhook payload into normalised messages.

        A single webhook event may contain multiple messages.
        Return an empty list if the payload contains no actionable messages.
        """

    @abstractmethod
    async def send(self, message: OutgoingMessage) -> None:
        """Send a reply message to the customer."""
