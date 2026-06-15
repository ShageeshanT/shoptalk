"""ShopTalk repository layer.

This package provides the repository pattern for ShopTalk data access.
Repositories abstract storage details from the application logic, making
it possible to swap in-memory storage for SQL without changing route handlers.

Available repositories
----------------------
- :class:`~shoptalk.repositories.base.BaseRepository` — abstract interface
- :class:`~shoptalk.repositories.memory.InMemoryRepository` — in-memory implementation

Example
-------
>>> from shoptalk.repositories.memory import InMemoryRepository
>>> from shoptalk.models.order import Order
>>> repo = InMemoryRepository()
>>> order = Order(business_id=uuid4(), customer_id=uuid4(), product="cake")
>>> repo.save(order)
"""

from shoptalk.repositories.base import BaseRepository
from shoptalk.repositories.memory import InMemoryRepository

__all__ = ["BaseRepository", "InMemoryRepository"]
