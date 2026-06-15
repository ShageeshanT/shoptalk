"""Order domain model.

An Order represents a confirmed or pending purchase from a customer.
Orders move through a status pipeline from inquiry to delivery.
"""

from __future__ import annotations

from datetime import datetime, timezone
from enum import Enum
from uuid import UUID, uuid4

from pydantic import BaseModel, Field


class OrderStatus(str, Enum):
    """Order lifecycle statuses.

    The pipeline moves roughly left to right:
    NEW_INQUIRY → CONFIRMED → PAYMENT_PENDING → PAID → PREPARING → READY → DELIVERED

    CANCELLED can occur at any stage.
    """

    NEW_INQUIRY = "new_inquiry"
    CONFIRMED = "confirmed"
    PAYMENT_PENDING = "payment_pending"
    PAID = "paid"
    PREPARING = "preparing"
    READY = "ready"
    DELIVERED = "delivered"
    CANCELLED = "cancelled"


class Order(BaseModel):
    """A customer order tracked through the sales pipeline.

    Attributes
    ----------
    id:
        Unique identifier for this order.
    business_id:
        The business fulfilling this order.
    customer_id:
        The customer who placed this order.
    product:
        Human-readable product description extracted from the customer message.
    quantity:
        Number of units ordered.
    status:
        Current position in the order pipeline.
    created_at:
        When the order was created (UTC).
    follow_up_needed:
        Whether a follow-up action is required (e.g. payment chase, delivery confirmation).
    notes:
        Optional seller notes about this order.
    total_amount:
        Order total in the business currency, if known.
    delivery_date:
        Requested delivery or pickup date, if specified.

    Example
    -------
    >>> order = Order(
    ...     business_id=uuid4(),
    ...     customer_id=uuid4(),
    ...     product="1kg chocolate cake",
    ...     quantity=1,
    ... )
    >>> order.status
    'new_inquiry'
    """

    id: UUID = Field(default_factory=uuid4, description="Unique order identifier")
    business_id: UUID = Field(..., description="Business fulfilling this order")
    customer_id: UUID = Field(..., description="Customer who placed this order")
    product: str = Field(..., min_length=1, description="Product description")
    quantity: int = Field(default=1, ge=1, description="Number of units ordered")
    status: OrderStatus = Field(
        default=OrderStatus.NEW_INQUIRY,
        description="Current order pipeline status",
    )
    created_at: datetime = Field(
        default_factory=lambda: datetime.now(timezone.utc),
        description="When the order was created (UTC)",
    )
    follow_up_needed: bool = Field(
        default=True,
        description="Whether a follow-up action is required",
    )
    notes: str | None = Field(default=None, description="Optional seller notes")
    total_amount: float | None = Field(
        default=None, ge=0, description="Order total in business currency"
    )
    delivery_date: datetime | None = Field(
        default=None, description="Requested delivery or pickup date"
    )

    model_config = {"use_enum_values": True}
