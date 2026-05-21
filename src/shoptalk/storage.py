from __future__ import annotations

from collections.abc import Iterable
from builtins import list as builtins_list
from typing import Generic, TypeVar
from uuid import UUID

from pydantic import BaseModel

ModelT = TypeVar("ModelT", bound=BaseModel)


class InMemoryRepository(Generic[ModelT]):
    """Tiny repository for the manual MVP.

    It keeps early API work runnable without database setup. The interface is intentionally
    small so a SQLAlchemy implementation can replace it without rewriting route handlers.
    """

    def __init__(self) -> None:
        self._items: dict[UUID, ModelT] = {}

    def add(self, item: ModelT) -> ModelT:
        item_id = getattr(item, "id")
        self._items[item_id] = item
        return item

    def get(self, item_id: UUID) -> ModelT | None:
        return self._items.get(item_id)

    def list(self) -> list[ModelT]:
        return builtins_list(self._items.values())

    def list_for_business(self, business_id: UUID) -> list[ModelT]:
        return self.filter_by(business_id=business_id)

    def filter_by(self, **criteria: object) -> list[ModelT]:
        return [
            item
            for item in self._items.values()
            if all(getattr(item, field, None) == expected for field, expected in criteria.items())
        ]

    def extend(self, items: Iterable[ModelT]) -> list[ModelT]:
        return [self.add(item) for item in items]
