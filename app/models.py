"""Core data models for ShopTalk."""

from __future__ import annotations

import uuid
from dataclasses import dataclass, field
from datetime import datetime
from enum import Enum
from typing import List, Optional


class OrderStatus(str, Enum):
    PENDING = "pending"
    CONFIRMED = "confirmed"
    PROCESSING = "processing"
    SHIPPED = "shipped"
    DELIVERED = "delivered"
    CANCELLED = "cancelled"


class PaymentStatus(str, Enum):
    UNPAID = "unpaid"
    PAID = "paid"
    REFUNDED = "refunded"
    FAILED = "failed"


class MessageDirection(str, Enum):
    INBOUND = "inbound"
    OUTBOUND = "outbound"


@dataclass
class OrderItem:
    product_id: str
    name: str
    quantity: int
    unit_price: float

    @property
    def subtotal(self) -> float:
        return self.quantity * self.unit_price

    def to_dict(self) -> dict:
        return {
            "product_id": self.product_id,
            "name": self.name,
            "quantity": self.quantity,
            "unit_price": self.unit_price,
            "subtotal": self.subtotal,
        }


@dataclass
class Order:
    customer_phone: str
    items: List[OrderItem] = field(default_factory=list)
    id: str = field(default_factory=lambda: str(uuid.uuid4()))
    status: OrderStatus = OrderStatus.PENDING
    payment_status: PaymentStatus = PaymentStatus.UNPAID
    notes: str = ""
    created_at: datetime = field(default_factory=datetime.utcnow)
    updated_at: datetime = field(default_factory=datetime.utcnow)

    @property
    def total(self) -> float:
        return sum(item.subtotal for item in self.items)

    def add_item(self, item: OrderItem) -> None:
        self.items.append(item)
        self.updated_at = datetime.utcnow()

    def confirm(self) -> None:
        self.status = OrderStatus.CONFIRMED
        self.updated_at = datetime.utcnow()

    def cancel(self) -> None:
        self.status = OrderStatus.CANCELLED
        self.updated_at = datetime.utcnow()

    def mark_paid(self) -> None:
        self.payment_status = PaymentStatus.PAID
        self.updated_at = datetime.utcnow()

    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "customer_phone": self.customer_phone,
            "items": [i.to_dict() for i in self.items],
            "total": self.total,
            "status": self.status.value,
            "payment_status": self.payment_status.value,
            "notes": self.notes,
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat(),
        }


@dataclass
class Customer:
    phone: str
    name: str = ""
    email: str = ""
    address: str = ""
    id: str = field(default_factory=lambda: str(uuid.uuid4()))
    order_ids: List[str] = field(default_factory=list)
    tags: List[str] = field(default_factory=list)
    created_at: datetime = field(default_factory=datetime.utcnow)
    last_seen: datetime = field(default_factory=datetime.utcnow)

    def touch(self) -> None:
        self.last_seen = datetime.utcnow()

    def add_order(self, order_id: str) -> None:
        if order_id not in self.order_ids:
            self.order_ids.append(order_id)

    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "phone": self.phone,
            "name": self.name,
            "email": self.email,
            "address": self.address,
            "order_ids": self.order_ids,
            "tags": self.tags,
            "created_at": self.created_at.isoformat(),
            "last_seen": self.last_seen.isoformat(),
        }


@dataclass
class Message:
    chat_id: str
    content: str
    direction: MessageDirection
    id: str = field(default_factory=lambda: str(uuid.uuid4()))
    channel: str = "whatsapp"
    media_url: Optional[str] = None
    timestamp: datetime = field(default_factory=datetime.utcnow)

    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "chat_id": self.chat_id,
            "content": self.content,
            "direction": self.direction.value,
            "channel": self.channel,
            "media_url": self.media_url,
            "timestamp": self.timestamp.isoformat(),
        }
