"""In-memory repository implementation for ShopTalk.

InMemoryRepository provides a fast, zero-dependency implementation of
BaseRepository backed by a Python dictionary. It is used for the manual
MVP and for testing.

The interface is intentionally identical to the SQL repository so that
route handlers can switch between implementations without code changes.
"""

from __future__ import annotations

from typing import Any, Generic, TypeVar
from uuid import UUID

from pydantic import BaseModel

from shoptalk.repositories.base import BaseRepository

ModelT = TypeVar("ModelT", bound=BaseModel)


class InMemoryRepository(BaseRepository[ModelT], Generic[ModelT]):
    """In-memory repository backed by a Python dictionary.

    All data is lost when the process restarts. This implementation is
    suitable for the manual MVP and for unit tests.

    Example
    -------
    >>> from uuid import uuid4
    >>> from shoptalk.models.order import Order
    >>> repo: InMemoryRepository[Order] = InMemoryRepository()
    >>> order = Order(business_id=uuid4(), customer_id=uuid4(), product="cake")
    >>> saved = repo.save(order)
    >>> repo.get(saved.id) == saved
    True
    >>> repo.delete(saved.id)
    True
    >>> repo.get(saved.id) is None
    True
    """

    def __init__(self) -> None:
        self._store: dict[UUID, ModelT] = {}

    def get(self, item_id: UUID) -> ModelT | None:
        """Retrieve a single entity by its UUID.

        Parameters
        ----------
        item_id:
            The UUID of the entity to retrieve.

        Returns
        -------
        ModelT | None
            The entity if found, or None.
        """
        return self._store.get(item_id)

    def save(self, item: ModelT) -> ModelT:
        """Persist an entity in memory.

        Parameters
        ----------
        item:
            The entity to persist. Must have an ``id`` field of type UUID.

        Returns
        -------
        ModelT
            The persisted entity.

        Raises
        ------
        AttributeError
            If the entity does not have an ``id`` field.
        """
        item_id: UUID = getattr(item, "id")
        self._store[item_id] = item
        return item

    def list_all(self) -> list[ModelT]:
        """Return all entities in the repository.

        Returns
        -------
        list[ModelT]
            All stored entities. Returns an empty list if none exist.
        """
        return list(self._store.values())

    def delete(self, item_id: UUID) -> bool:
        """Delete an entity by its UUID.

        Parameters
        ----------
        item_id:
            The UUID of the entity to delete.

        Returns
        -------
        bool
            True if the entity was found and deleted, False otherwise.
        """
        if item_id in self._store:
            del self._store[item_id]
            return True
        return False

    def filter_by(self, **criteria: Any) -> list[ModelT]:
        """Return entities matching all given field criteria.

        Parameters
        ----------
        **criteria:
            Field name and expected value pairs. All criteria must match.

        Returns
        -------
        list[ModelT]
            Entities where all specified fields match the given values.

        Example
        -------
        >>> orders = repo.filter_by(business_id=biz_id, status="new_inquiry")
        """
        return [
            item
            for item in self._store.values()
            if all(
                getattr(item, field, None) == expected
                for field, expected in criteria.items()
            )
        ]

    def list_for_business(self, business_id: UUID) -> list[ModelT]:
        """Return all entities belonging to a specific business.

        Parameters
        ----------
        business_id:
            The UUID of the business to filter by.

        Returns
        -------
        list[ModelT]
            All entities with a matching ``business_id`` field.
        """
        return self.filter_by(business_id=business_id)

    def count(self) -> int:
        """Return the total number of entities in the repository.

        Returns
        -------
        int
            The number of stored entities.
        """
        return len(self._store)

    def clear(self) -> None:
        """Remove all entities from the repository.

        This is primarily useful for test teardown.
        """
        self._store.clear()
