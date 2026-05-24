from sqlalchemy import or_
from sqlalchemy.orm import Query

from shoptalk.db_models import CustomerRecord


def search_customers(query: Query, term: str | None):
    if not term:
        return query
    like = f"%{term.lower()}%"
    return query.filter(or_(CustomerRecord.name.ilike(like), CustomerRecord.phone.ilike(like), CustomerRecord.email.ilike(like)))
