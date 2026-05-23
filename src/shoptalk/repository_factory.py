from dataclasses import dataclass

from sqlalchemy.orm import Session

from shoptalk.db_business_repository import SqlBusinessRepository
from shoptalk.db_customer_repository import SqlCustomerRepository
from shoptalk.db_order_repository import SqlOrderRepository
from shoptalk.db_message_repository import SqlMessageRepository
from shoptalk.db_followup_repository import SqlFollowUpRepository


@dataclass
class SqlRepositories:
    businesses: SqlBusinessRepository
    customers: SqlCustomerRepository
    orders: SqlOrderRepository
    messages: SqlMessageRepository
    follow_ups: SqlFollowUpRepository


def build_sql_repositories(session: Session) -> SqlRepositories:
    return SqlRepositories(
        businesses=SqlBusinessRepository(session),
        customers=SqlCustomerRepository(session),
        orders=SqlOrderRepository(session),
        messages=SqlMessageRepository(session),
        follow_ups=SqlFollowUpRepository(session),
    )
