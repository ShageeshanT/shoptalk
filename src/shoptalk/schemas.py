from datetime import datetime
from typing import Literal
from uuid import UUID, uuid4

from pydantic import BaseModel, Field

from shoptalk.enums import BusinessType, FollowUpStatus, OrderStatus


Intent = Literal[
    "new_order",
    "product_inquiry",
    "payment_question",
    "delivery_question",
    "complaint",
    "follow_up",
    "general",
]

Urgency = Literal["low", "normal", "high"]
Sentiment = Literal["positive", "neutral", "negative"]


class MessageAnalyzeRequest(BaseModel):
    text: str = Field(..., min_length=1, examples=["Hi, can I order a 1kg cake for Saturday?"])
    business_type: BusinessType = BusinessType.HOME_BAKERY
    tone: str = Field(default="friendly")


class OrderDetails(BaseModel):
    product: str | None = None
    quantity: int | None = None
    size: str | None = None
    needed_by: str | None = None
    custom_text: str | None = None
    delivery_required: bool | None = None


class MessageAnalysis(BaseModel):
    intent: Intent
    urgency: Urgency
    sentiment: Sentiment
    customer_needs_reply: bool
    order_details: OrderDetails = Field(default_factory=OrderDetails)
    payment_status: str = "unknown"
    follow_up_needed: bool = False
    follow_up_reason: str | None = None
    suggested_reply: str
    confidence: float = Field(default=0.7, ge=0, le=1)


class BusinessCreate(BaseModel):
    name: str = Field(..., min_length=1)
    business_type: BusinessType = BusinessType.HOME_BAKERY
    timezone: str = "Asia/Colombo"
    tone: str = "friendly"
    currency: str = "LKR"


class Business(BusinessCreate):
    id: UUID = Field(default_factory=uuid4)
    created_at: datetime = Field(default_factory=datetime.utcnow)


class CustomerCreate(BaseModel):
    business_id: UUID
    name: str = Field(..., min_length=1)
    channel: str = "manual"
    channel_id: str | None = None
    notes: str | None = None


class Customer(CustomerCreate):
    id: UUID = Field(default_factory=uuid4)
    last_message_at: datetime | None = None
    created_at: datetime = Field(default_factory=datetime.utcnow)


class OrderCreate(BaseModel):
    business_id: UUID
    customer_id: UUID | None = None
    title: str = Field(..., min_length=1)
    status: OrderStatus = OrderStatus.NEW_INQUIRY
    payment_status: str = "unknown"
    total_amount: float | None = Field(default=None, ge=0)
    delivery_date: str | None = None
    notes: str | None = None


class Order(OrderCreate):
    id: UUID = Field(default_factory=uuid4)
    created_at: datetime = Field(default_factory=datetime.utcnow)


class FollowUpCreate(BaseModel):
    business_id: UUID
    customer_id: UUID | None = None
    order_id: UUID | None = None
    title: str = Field(..., min_length=1)
    due_at: datetime | None = None
    status: FollowUpStatus = FollowUpStatus.OPEN


class FollowUp(FollowUpCreate):
    id: UUID = Field(default_factory=uuid4)
    created_at: datetime = Field(default_factory=datetime.utcnow)
