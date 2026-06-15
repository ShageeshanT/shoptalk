"""Business domain model.

A Business represents a seller account in ShopTalk.
Each business has its own customers, orders, and follow-ups.
"""

from __future__ import annotations

from datetime import datetime, timezone
from uuid import UUID, uuid4

from pydantic import BaseModel, Field


class CatalogItem(BaseModel):
    """A single item in a business product catalog.

    Attributes
    ----------
    name:
        Product name as it appears in customer messages.
    price:
        Unit price in the business currency.
    description:
        Optional longer description for the product.
    available:
        Whether this item is currently available for ordering.
    """

    name: str = Field(..., min_length=1, description="Product name")
    price: float | None = Field(default=None, ge=0, description="Unit price")
    description: str | None = Field(default=None, description="Product description")
    available: bool = Field(default=True, description="Whether the item is available")


class Business(BaseModel):
    """A seller account in ShopTalk.

    Attributes
    ----------
    id:
        Unique identifier for this business.
    name:
        Business display name.
    whatsapp_number:
        The WhatsApp number used for customer communication.
    catalog:
        List of products this business sells.
    created_at:
        When the business account was created (UTC).
    timezone:
        Business timezone for scheduling and briefings (e.g. "Asia/Colombo").
    tone:
        Preferred reply tone for AI-generated drafts (e.g. "friendly", "professional").
    currency:
        ISO 4217 currency code for order amounts (e.g. "LKR", "USD").

    Example
    -------
    >>> biz = Business(
    ...     name="Amaya's Cakes",
    ...     whatsapp_number="+94771234567",
    ... )
    >>> biz.currency
    'USD'
    """

    id: UUID = Field(default_factory=uuid4, description="Unique business identifier")
    name: str = Field(..., min_length=1, description="Business display name")
    whatsapp_number: str | None = Field(
        default=None, description="WhatsApp number for customer communication"
    )
    catalog: list[CatalogItem] = Field(
        default_factory=list, description="Products this business sells"
    )
    created_at: datetime = Field(
        default_factory=lambda: datetime.now(timezone.utc),
        description="When the business account was created (UTC)",
    )
    timezone: str = Field(
        default="UTC",
        description="Business timezone (e.g. Asia/Colombo)",
    )
    tone: str = Field(
        default="friendly",
        description="Preferred reply tone for AI-generated drafts",
    )
    currency: str = Field(
        default="USD",
        min_length=3,
        max_length=3,
        description="ISO 4217 currency code",
    )
