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
