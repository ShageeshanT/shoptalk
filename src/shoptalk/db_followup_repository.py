from sqlalchemy.orm import Session

from shoptalk.db_mappers import followup_from_record, followup_to_record
from shoptalk.db_models import FollowUpRecord
from shoptalk.schemas import FollowUp, FollowUpCreate


class SqlFollowUpRepository:
    def __init__(self, session: Session):
        self.session = session

    def create(self, payload: FollowUpCreate) -> FollowUp:
        follow_up = FollowUp(**payload.model_dump())
        self.session.add(followup_to_record(follow_up))
        self.session.commit()
        return follow_up

    def list_open_for_business(self, business_id) -> list[FollowUp]:
        records = (
            self.session.query(FollowUpRecord)
            .filter(FollowUpRecord.business_id == str(business_id), FollowUpRecord.status == "open")
            .order_by(FollowUpRecord.created_at.desc())
            .all()
        )
        return [followup_from_record(record) for record in records]
