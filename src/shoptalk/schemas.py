from datetime import datetime
from typing import Literal
from uuid import UUID, uuid4

from pydantic import BaseModel, Field

from shoptalk.enums import BusinessType, FollowUpStatus, MessageDirection, OrderStatus


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


class OrderAction(BaseModel):
    order_id: UUID
    status: OrderStatus
    active: bool
    next_step: str


class PaymentRequestDraft(BaseModel):
    order_id: UUID
    required: bool
    message: str


class OrderRisk(BaseModel):
    order_id: UUID
    level: Literal["low", "medium", "high"]
    score: int = Field(..., ge=0, le=100)
    flags: list[str]


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


class FollowUpQueueItem(BaseModel):
    follow_up: FollowUp
    priority: int


class ConversationMessage(BaseModel):
    business_id: UUID
    customer_id: UUID | None = None
    channel: str = "whatsapp"
    sender: MessageDirection = MessageDirection.CUSTOMER
    text: str = Field(..., min_length=1)
    external_message_id: str | None = None
    received_at: datetime = Field(default_factory=datetime.utcnow)


class ConversationMessageOut(ConversationMessage):
    id: UUID = Field(default_factory=uuid4)
    created_at: datetime = Field(default_factory=datetime.utcnow)


class MessageTag(BaseModel):
    message_id: UUID
    tags: list[str]


class ReplyDraft(BaseModel):
    analysis: MessageAnalysis
    suggested_reply: str
    requires_human_approval: bool = True


class SellerTask(BaseModel):
    business_id: UUID
    title: str = Field(..., min_length=2)
    source: str = "manual"
    priority: Literal["low", "normal", "high"] = "normal"
    done: bool = False


class SellerTaskOut(SellerTask):
    id: UUID = Field(default_factory=uuid4)
    created_at: datetime = Field(default_factory=datetime.utcnow)


class CustomerSignal(BaseModel):
    customer_id: UUID | None = None
    latest_message: str
    intent: Intent
    urgency: Urgency
    sentiment: Sentiment
    needs_reply: bool
    suggested_reply: str


class CustomerInsight(BaseModel):
    customer_id: UUID
    total_orders: int
    active_orders: int
    delivered_orders: int
    cancelled_orders: int
    total_spend: float
    inbound_messages: int
    pending_follow_ups: int
    latest_message_at: datetime | None = None


class ConversationSummary(BaseModel):
    business_id: UUID
    customer_id: UUID | None = None
    messages: int
    customer_messages: int
    seller_messages: int
    latest_message: ConversationMessageOut | None = None
    signal: CustomerSignal | None = None


class InboxItem(BaseModel):
    customer_id: UUID
    signal: CustomerSignal


class CatalogMatchRequest(BaseModel):
    message: str = Field(..., min_length=1)
    catalog: list[dict]


class MessageThreadItem(BaseModel):
    message: ConversationMessageOut
    direction: MessageDirection
    display_name: str


class MessageThread(BaseModel):
    business_id: UUID
    customer_id: UUID | None = None
    messages: list[MessageThreadItem]


class MessageSendDraft(BaseModel):
    business_id: UUID
    customer_id: UUID | None = None
    channel: str = "whatsapp"
    text: str = Field(..., min_length=1)
    requires_human_approval: bool = True


class CustomerProfile(BaseModel):
    customer: Customer
    orders: list[Order]
    follow_ups: list[FollowUp]
    messages: list[ConversationMessageOut]


class CatalogItemCreate(BaseModel):
    business_id: UUID
    name: str = Field(..., min_length=1)
    price: float | None = Field(default=None, ge=0)
    tags: list[str] = Field(default_factory=list)
    available: bool = True


class CatalogItemRecord(CatalogItemCreate):
    id: UUID = Field(default_factory=uuid4)
    created_at: datetime = Field(default_factory=datetime.utcnow)


class CheckoutDraft(BaseModel):
    order_id: UUID
    amount: float | None = None
    currency: str = "LKR"
    payment_label: str = "manual_transfer"
    message: str


class SalesFunnel(BaseModel):
    new_inquiries: int
    payment_pending: int
    paid: int
    preparing: int
    ready: int
    delivered: int
    cancelled: int


class KanbanOrderCard(BaseModel):
    order_id: UUID
    title: str
    customer_id: UUID | None = None
    total_amount: float | None = None
    delivery_date: str | None = None


class KanbanColumn(BaseModel):
    status: OrderStatus
    title: str
    count: int
    orders: list[KanbanOrderCard]


class KanbanBoard(BaseModel):
    business_id: UUID | None = None
    columns: list[KanbanColumn]
    total_orders: int
    hidden_done_orders: int = 0


class DailyBrief(BaseModel):
    business_id: UUID | None = None
    open_orders: int
    pending_follow_ups: int
    urgent_messages: int
    suggested_actions: list[str]


class DailyActionItem(BaseModel):
    title: str
    priority: Literal["low", "normal", "high"]
    reason: str


class DailyActionPlan(BaseModel):
    business_id: UUID | None = None
    generated_from: str
    actions: list[DailyActionItem]
    total_actions: int


class HealthCheckItem(BaseModel):
    name: str
    ok: bool
    detail: str


class HealthCheck(BaseModel):
    status: Literal["ok", "degraded"]
    checks: list[HealthCheckItem]


class BusinessSettingsUpdate(BaseModel):
    tone: str | None = None
    currency: str | None = None
    timezone: str | None = None
