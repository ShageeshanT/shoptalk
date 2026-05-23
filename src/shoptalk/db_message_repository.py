from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from shoptalk.db_mappers import message_from_record, message_to_record
from shoptalk.db_models import MessageRecord
from shoptalk.persistence_errors import DuplicateRecordError
from shoptalk.schemas import ConversationMessage, ConversationMessageOut


class SqlMessageRepository:
    def __init__(self, session: Session):
        self.session = session

    def create(self, payload: ConversationMessage) -> ConversationMessageOut:
        message = ConversationMessageOut(**payload.model_dump())
        self.session.add(message_to_record(message))
        try:
            self.session.commit()
        except IntegrityError as exc:
            self.session.rollback()
            raise DuplicateRecordError("external_message_id already exists") from exc
        return message

    def list_for_business(self, business_id) -> list[ConversationMessageOut]:
        records = (
            self.session.query(MessageRecord)
            .filter(MessageRecord.business_id == str(business_id))
            .order_by(MessageRecord.received_at.desc())
            .all()
        )
        return [message_from_record(record) for record in records]
