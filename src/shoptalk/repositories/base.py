"""Abstract base repository for ShopTalk data access.

All repository implementations must extend BaseRepository and implement
the four core methods: get, save, list_all, and delete.

This interface is intentionally minimal so that in-memory and SQL
implementations can be swapped without changing route handlers.
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Generic, TypeVar
from uuid import UUID

from pydantic import BaseModel

ModelT = TypeVar("ModelT", bound=BaseModel)


class BaseRepository(ABC, Generic[ModelT]):
    """Abstract repository interface for ShopTalk entities.

    All concrete repository implementations must extend this class and
    implement the four abstract methods.

    Type Parameters
    ---------------
    ModelT:
        The Pydantic model type this repository manages.
        Must be a subclass of ``pydantic.BaseModel``.

    Example
    -------
    >>> class MyRepo(BaseRepository[Order]):
    ...     def get(self, item_id: UUID) -> Order | None: ...
    ...     def save(self, item: Order) -> Order: ...
    ...     def list_all(self) -> list[Order]: ...
    ...     def delete(self, item_id: UUID) -> bool: ...
    """

    @abstractmethod
    def get(self, item_id: UUID) -> ModelT | None:
        """Retrieve a single entity by its UUID.

        Parameters
        ----------
        item_id:
            The UUID of the entity to retrieve.

        Returns
        -------
        ModelT | None
            The entity if found, or None if it does not exist.
        """
        ...

    @abstractmethod
    def save(self, item: ModelT) -> ModelT:
        """Persist an entity, creating or updating as needed.

        Parameters
        ----------
        item:
            The entity to persist. Must have an ``id`` field of type UUID.

        Returns
        -------
        ModelT
            The persisted entity (may differ from input if defaults were applied).
        """
        ...

    @abstractmethod
    def list_all(self) -> list[ModelT]:
        """Return all entities managed by this repository.

        Returns
        -------
        list[ModelT]
            All stored entities. Returns an empty list if none exist.
        """
        ...

    @abstractmethod
    def delete(self, item_id: UUID) -> bool:
        """Delete an entity by its UUID.

        Parameters
        ----------
        item_id:
            The UUID of the entity to delete.

        Returns
        -------
        bool
            True if the entity was found and deleted, False if it did not exist.
        """
        ...

    def exists(self, item_id: UUID) -> bool:
        """Return True if an entity with the given UUID exists.

        Parameters
        ----------
        item_id:
            The UUID to check.

        Returns
        -------
        bool
            True if the entity exists, False otherwise.
        """
        return self.get(item_id) is not None

    def save_many(self, items: list[ModelT]) -> list[ModelT]:
        """Persist multiple entities in sequence.

        Parameters
        ----------
        items:
            The entities to persist.

        Returns
        -------
        list[ModelT]
            The persisted entities in the same order as the input.
        """
        return [self.save(item) for item in items]
