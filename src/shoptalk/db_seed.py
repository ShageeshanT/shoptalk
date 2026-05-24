from shoptalk.db_business_repository import SqlBusinessRepository
from shoptalk.schemas import BusinessCreate


def ensure_demo_business(session, name: str = "Kavi Bakes"):
    repo = SqlBusinessRepository(session)
    for business in repo.list():
        if business.name == name:
            return business
    return repo.create(BusinessCreate(name=name))
