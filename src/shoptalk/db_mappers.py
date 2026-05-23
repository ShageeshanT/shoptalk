import json

from shoptalk.db_models import BusinessRecord, CustomerRecord, OrderRecord
from shoptalk.schemas import Business, Customer, Order


def business_to_record(business: Business) -> BusinessRecord:
    return BusinessRecord(
        id=str(business.id),
        name=business.name,
        business_type=business.business_type.value,
        timezone=business.timezone,
        tone=business.tone,
        currency=business.currency,
        created_at=business.created_at,
    )


def business_from_record(record: BusinessRecord) -> Business:
    return Business(
        id=record.id,
        name=record.name,
        business_type=record.business_type,
        timezone=record.timezone,
        tone=record.tone,
        currency=record.currency,
        created_at=record.created_at,
    )


def customer_to_record(customer: Customer) -> CustomerRecord:
    return CustomerRecord(
        id=str(customer.id),
        business_id=str(customer.business_id),
        name=customer.name,
        channel=customer.channel,
        channel_id=customer.channel_id,
        phone=customer.phone,
        email=customer.email,
        tags=json.dumps(customer.tags),
        notes=customer.notes,
        last_message_at=customer.last_message_at,
        created_at=customer.created_at,
    )


def customer_from_record(record: CustomerRecord) -> Customer:
    return Customer(
        id=record.id,
        business_id=record.business_id,
        name=record.name,
        channel=record.channel,
        channel_id=record.channel_id,
        phone=record.phone,
        email=record.email,
        tags=json.loads(record.tags or "[]"),
        notes=record.notes,
        last_message_at=record.last_message_at,
        created_at=record.created_at,
    )


def order_to_record(order: Order) -> OrderRecord:
    return OrderRecord(
        id=str(order.id),
        business_id=str(order.business_id),
        customer_id=str(order.customer_id) if order.customer_id else None,
        title=order.title,
        status=order.status.value,
        payment_status=order.payment_status,
        total_amount=order.total_amount,
        delivery_date=order.delivery_date,
        notes=order.notes,
        created_at=order.created_at,
    )


def order_from_record(record: OrderRecord) -> Order:
    return Order(
        id=record.id,
        business_id=record.business_id,
        customer_id=record.customer_id,
        title=record.title,
        status=record.status,
        payment_status=record.payment_status,
        total_amount=record.total_amount,
        delivery_date=record.delivery_date,
        notes=record.notes,
        created_at=record.created_at,
    )


from shoptalk.db_models import MessageRecord
from shoptalk.schemas import ConversationMessageOut


def message_to_record(message: ConversationMessageOut) -> MessageRecord:
    return MessageRecord(
        id=str(message.id),
        business_id=str(message.business_id),
        customer_id=str(message.customer_id) if message.customer_id else None,
        channel=message.channel,
        sender=message.sender.value,
        text=message.text,
        external_message_id=message.external_message_id,
        received_at=message.received_at,
        created_at=message.created_at,
    )


def message_from_record(record: MessageRecord) -> ConversationMessageOut:
    return ConversationMessageOut(
        id=record.id,
        business_id=record.business_id,
        customer_id=record.customer_id,
        channel=record.channel,
        sender=record.sender,
        text=record.text,
        external_message_id=record.external_message_id,
        received_at=record.received_at,
        created_at=record.created_at,
    )


from shoptalk.db_models import FollowUpRecord
from shoptalk.schemas import FollowUp


def followup_to_record(follow_up: FollowUp) -> FollowUpRecord:
    return FollowUpRecord(
        id=str(follow_up.id),
        business_id=str(follow_up.business_id),
        customer_id=str(follow_up.customer_id) if follow_up.customer_id else None,
        order_id=str(follow_up.order_id) if follow_up.order_id else None,
        title=follow_up.title,
        due_at=follow_up.due_at,
        status=follow_up.status.value,
        created_at=follow_up.created_at,
    )


def followup_from_record(record: FollowUpRecord) -> FollowUp:
    return FollowUp(
        id=record.id,
        business_id=record.business_id,
        customer_id=record.customer_id,
        order_id=record.order_id,
        title=record.title,
        due_at=record.due_at,
        status=record.status,
        created_at=record.created_at,
    )
