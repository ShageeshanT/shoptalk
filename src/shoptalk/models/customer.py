"""Customer domain model.

A Customer represents a person who has contacted a business through
any supported channel. Customers are scoped to a single business.
"""

from __future__ import annotations

from datetime import datetime, timezone
from uuid import UUID, uuid4

from pydantic import BaseModel, Field

from shoptalk.models.message import Channel


class Customer(BaseModel):
    """A customer who has contacted a business.

    Customers are scoped to a single business. The same person contacting
    two different businesses creates two separate Customer records.

    Attributes
    ----------
    id:
        Unique identifier for this customer.
    business_id:
        The business this customer belongs to.
    name:
        Customer display name (may be inferred from the channel).
    phone:
        Customer phone number, normalised to E.164 format where possible.
    channel:
        The primary channel through which this customer contacts the business.
    last_seen:
        When the customer last sent a message (UTC).
    notes:
        Optional seller notes about this customer.

    Example
    -------
    >>> customer = Customer(
    ...     business_id=uuid4(),
    ...     name="Priya",
    ...     phone="+94771234567",
    ...     channel=Channel.WHATSAPP,
    ... )
    >>> customer.channel
    'whatsapp'
    """

    id: UUID = Field(default_factory=uuid4, description="Unique customer identifier")
    business_id: UUID = Field(..., description="Business this customer belongs to")
    name: str = Field(..., min_length=1, description="Customer display name")
    phone: str | None = Field(
        default=None, description="Phone number in E.164 format"
    )
    channel: Channel = Field(
        default=Channel.MANUAL,
        description="Primary contact channel",
    )
    last_seen: datetime | None = Field(
        default=None,
        description="When the customer last sent a message (UTC)",
    )
    notes: str | None = Field(
        default=None, description="Optional seller notes about this customer"
    )

    model_config = {"use_enum_values": True}

    def update_last_seen(self) -> "Customer":
        """Return a copy of this customer with last_seen set to now (UTC)."""
        return self.model_copy(update={"last_seen": datetime.now(timezone.utc)})
