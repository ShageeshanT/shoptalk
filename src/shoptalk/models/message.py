"""CustomerMessage domain model.

A CustomerMessage represents a single inbound message from a customer
received through any supported channel (WhatsApp, Telegram, manual paste).
"""

from __future__ import annotations

from datetime import datetime, timezone
from enum import Enum
from uuid import UUID, uuid4

from pydantic import BaseModel, Field


class Channel(str, Enum):
    """Supported inbound message channels."""

    WHATSAPP = "whatsapp"
    TELEGRAM = "telegram"
    INSTAGRAM = "instagram"
    MANUAL = "manual"


class Intent(str, Enum):
    """Detected customer intent categories."""

    NEW_ORDER = "new_order"
    PAYMENT_QUESTION = "payment_question"
    DELIVERY_QUESTION = "delivery_question"
    PRODUCT_INQUIRY = "product_inquiry"
    COMPLAINT = "complaint"
    GENERAL = "general"
    UNKNOWN = "unknown"


class Urgency(str, Enum):
    """Message urgency level."""

    HIGH = "high"
    NORMAL = "normal"
    LOW = "low"


class CustomerMessage(BaseModel):
    """A single inbound message from a customer.

    Attributes
    ----------
    id:
        Unique identifier for this message.
    business_id:
        The business that received this message.
    customer_id:
        The customer who sent this message.
    content:
        The raw message text as received from the customer.
    channel:
        The channel through which the message was received.
    timestamp:
        When the message was received (UTC).
    intent:
        The detected intent of the message, if analysed.
    urgency:
        The detected urgency level, if analysed.

    Example
    -------
    >>> msg = CustomerMessage(
    ...     business_id=uuid4(),
    ...     customer_id=uuid4(),
    ...     content="Hi, can I order a chocolate cake for Saturday?",
    ...     channel=Channel.WHATSAPP,
    ... )
    >>> msg.channel
    <Channel.WHATSAPP: 'whatsapp'>
    """

    id: UUID = Field(default_factory=uuid4, description="Unique message identifier")
    business_id: UUID = Field(..., description="Business that received this message")
    customer_id: UUID = Field(..., description="Customer who sent this message")
    content: str = Field(..., min_length=1, description="Raw message text")
    channel: Channel = Field(default=Channel.MANUAL, description="Inbound channel")
    timestamp: datetime = Field(
        default_factory=lambda: datetime.now(timezone.utc),
        description="When the message was received (UTC)",
    )
    intent: Intent | None = Field(default=None, description="Detected intent")
    urgency: Urgency | None = Field(default=None, description="Detected urgency")

    model_config = {"use_enum_values": True}
