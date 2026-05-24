from sqlalchemy.orm import Session

from shoptalk.db_mappers import customer_from_record, customer_to_record
from shoptalk.db_customer_queries import search_customers
from shoptalk.db_models import CustomerRecord
from shoptalk.schemas import Customer, CustomerCreate


class SqlCustomerRepository:
    def __init__(self, session: Session):
        self.session = session

    def create(self, payload: CustomerCreate) -> Customer:
        customer = Customer(**payload.model_dump())
        self.session.add(customer_to_record(customer))
        self.session.commit()
        return customer

    def get(self, customer_id) -> Customer | None:
        record = self.session.get(CustomerRecord, str(customer_id))
        return customer_from_record(record) if record else None

    def list_for_business(self, business_id) -> list[Customer]:
        return self.search_for_business(business_id)

    def search_for_business(self, business_id, term: str | None = None) -> list[Customer]:
        query = self.session.query(CustomerRecord).filter(CustomerRecord.business_id == str(business_id))
        query = search_customers(query, term)
        records = query.order_by(CustomerRecord.created_at.desc()).all()
        return [customer_from_record(record) for record in records]
