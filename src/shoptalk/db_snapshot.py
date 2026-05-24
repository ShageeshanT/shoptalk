from sqlalchemy.orm import Session

from shoptalk.db_counts import business_record_counts
from shoptalk.db_mappers import business_from_record
from shoptalk.db_models import BusinessRecord


def business_snapshot(session: Session, business_id) -> dict[str, object] | None:
    record = session.get(BusinessRecord, str(business_id))
    if record is None:
        return None
    business = business_from_record(record)
    return {"business": business.model_dump(mode="json"), "counts": business_record_counts(session, business_id)}
