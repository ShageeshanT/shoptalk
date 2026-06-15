"""FollowUp domain model.

A FollowUp represents a scheduled action that a seller needs to take
for a specific customer or order. Examples include chasing a payment,
confirming a delivery, or sending a catalog.
"""

from __future__ import annotations

from datetime import datetime, timezone
from enum import Enum
from uuid import UUID, uuid4

from pydantic import BaseModel, Field


class FollowUpType(str, Enum):
    """Common follow-up action categories."""

    PAYMENT_CHASE = "payment_chase"
    DELIVERY_CONFIRMATION = "delivery_confirmation"
    ORDER_CONFIRMATION = "order_confirmation"
    CATALOG_SEND = "catalog_send"
    PICKUP_CONFIRMATION = "pickup_confirmation"
    GENERAL = "general"


class FollowUp(BaseModel):
    """A scheduled follow-up action for a seller.

    Attributes
    ----------
    id:
        Unique identifier for this follow-up.
    order_id:
        The order this follow-up is associated with, if any.
    customer_id:
        The customer this follow-up is for.
    business_id:
        The business this follow-up belongs to.
    due_at:
        When this follow-up should be actioned (UTC).
    note:
        Description of what the seller needs to do.
    done:
        Whether this follow-up has been completed.
    follow_up_type:
        Category of follow-up action.
    created_at:
        When this follow-up was created (UTC).

    Example
    -------
    >>> fu = FollowUp(
    ...     customer_id=uuid4(),
    ...     business_id=uuid4(),
    ...     due_at=datetime(2026, 6, 20, 10, 0, tzinfo=timezone.utc),
    ...     note="Chase payment for chocolate cake order",
    ...     follow_up_type=FollowUpType.PAYMENT_CHASE,
    ... )
    >>> fu.done
    False
    """

    id: UUID = Field(default_factory=uuid4, description="Unique follow-up identifier")
    order_id: UUID | None = Field(
        default=None, description="Associated order, if any"
    )
    customer_id: UUID = Field(..., description="Customer this follow-up is for")
    business_id: UUID = Field(..., description="Business this follow-up belongs to")
    due_at: datetime = Field(..., description="When this follow-up should be actioned (UTC)")
    note: str = Field(..., min_length=1, description="What the seller needs to do")
    done: bool = Field(default=False, description="Whether this follow-up is complete")
    follow_up_type: FollowUpType = Field(
        default=FollowUpType.GENERAL,
        description="Category of follow-up action",
    )
    created_at: datetime = Field(
        default_factory=lambda: datetime.now(timezone.utc),
        description="When this follow-up was created (UTC)",
    )

    model_config = {"use_enum_values": True}

    def mark_done(self) -> "FollowUp":
        """Return a copy of this follow-up marked as complete."""
        return self.model_copy(update={"done": True})

    @property
    def is_overdue(self) -> bool:
        """Return True if this follow-up is past its due date and not done."""
        return not self.done and datetime.now(timezone.utc) > self.due_at
