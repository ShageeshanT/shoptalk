from contextlib import AbstractContextManager
from types import TracebackType
from sqlalchemy.orm import Session


class SqlUnitOfWork(AbstractContextManager["SqlUnitOfWork"]):
    def __init__(self, session: Session):
        self.session = session

    def __enter__(self) -> "SqlUnitOfWork":
        return self

    def __exit__(self, exc_type: type[BaseException] | None, exc: BaseException | None, tb: TracebackType | None) -> bool | None:
        if exc_type is None:
            self.session.commit()
        else:
            self.session.rollback()
        self.session.close()
        return None
