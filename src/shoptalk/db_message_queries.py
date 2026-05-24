from sqlalchemy.orm import Query

from shoptalk.db_models import MessageRecord


def filter_messages_by_customer(query: Query, customer_id):
    if not customer_id:
        return query
    return query.filter(MessageRecord.customer_id == str(customer_id))


def filter_messages_by_channel(query: Query, channel: str | None):
    if not channel:
        return query
    return query.filter(MessageRecord.channel == channel)
