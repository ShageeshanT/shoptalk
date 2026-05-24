from sqlalchemy.orm import Session

from shoptalk.db_models import CustomerRecord, FollowUpRecord, MessageRecord, OrderRecord


def business_record_counts(session: Session, business_id) -> dict[str, int]:
    bid = str(business_id)
    return {
        "customers": session.query(CustomerRecord).filter(CustomerRecord.business_id == bid).count(),
        "orders": session.query(OrderRecord).filter(OrderRecord.business_id == bid).count(),
        "messages": session.query(MessageRecord).filter(MessageRecord.business_id == bid).count(),
        "follow_ups": session.query(FollowUpRecord).filter(FollowUpRecord.business_id == bid).count(),
    }
