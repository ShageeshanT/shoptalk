"""Pydantic schemas for the /analyze endpoint."""

from typing import Literal

from pydantic import BaseModel, Field


class AnalyzeRequest(BaseModel):
    """Incoming request to analyze a customer message."""

    business_id: str = Field(..., description="ID of the seller business")
    customer_id: str = Field(..., description="ID of the customer")
    raw_message: str = Field(..., min_length=1, max_length=4000, description="Raw message text from the customer")


IntentType = Literal[
    "new_order",
    "order_inquiry",
    "price_inquiry",
    "complaint",
    "cancellation",
    "general_inquiry",
    "greeting",
    "unknown",
]

UrgencyLevel = Literal["low", "normal", "high", "urgent"]
SentimentType = Literal["positive", "neutral", "negative"]


class AnalyzeResponse(BaseModel):
    """Structured analysis result for a customer message."""

    intent: IntentType = Field(..., description="Detected intent of the message")
    urgency: UrgencyLevel = Field(default="normal", description="Urgency level")
    sentiment: SentimentType = Field(default="neutral", description="Customer sentiment")
    product: str | None = Field(default=None, description="Product mentioned, if any")
    quantity: int | None = Field(default=None, description="Quantity requested")
    size: str | None = Field(default=None, description="Size or variant requested")
    needed_by: str | None = Field(default=None, description="Delivery or pickup deadline")
    follow_up_needed: bool = Field(default=False, description="Whether a follow-up is required")
    suggested_reply: str = Field(..., description="AI-generated reply suggestion for the seller")
    confidence: float = Field(default=1.0, ge=0.0, le=1.0, description="Confidence score 0-1")
