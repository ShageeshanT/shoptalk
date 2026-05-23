from sqlalchemy.orm import Session

from shoptalk.db_mappers import business_from_record, business_to_record
from shoptalk.db_models import BusinessRecord
from shoptalk.schemas import Business, BusinessCreate


class SqlBusinessRepository:
    def __init__(self, session: Session):
        self.session = session

    def create(self, payload: BusinessCreate) -> Business:
        business = Business(**payload.model_dump())
        self.session.add(business_to_record(business))
        self.session.commit()
        return business

    def get(self, business_id) -> Business | None:
        record = self.session.get(BusinessRecord, str(business_id))
        return business_from_record(record) if record else None

    def list(self) -> list[Business]:
        records = self.session.query(BusinessRecord).order_by(BusinessRecord.created_at.desc()).all()
        return [business_from_record(record) for record in records]
