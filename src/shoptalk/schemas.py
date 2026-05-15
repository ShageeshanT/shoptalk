from typing import Literal

from pydantic import BaseModel, Field


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
    business_type: str = Field(default="home_bakery")
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
