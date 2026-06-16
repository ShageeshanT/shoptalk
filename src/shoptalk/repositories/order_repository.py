"""Data access layer for orders."""

from __future__ import annotations

from typing import Sequence

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from shoptalk.models.order import Order, OrderStatus


class OrderRepository:
    """Handles all database operations for Order records."""

    def __init__(self, session: AsyncSession) -> None:
        self._session = session

    async def create(self, order: Order) -> Order:
        """Persist a new order and return it with its generated ID."""
        self._session.add(order)
        await self._session.flush()
        await self._session.refresh(order)
        return order

    async def get_by_id(self, order_id: str) -> Order | None:
        """Return an order by primary key, or None if not found."""
        return await self._session.get(Order, order_id)

    async def list_by_business(
        self,
        business_id: str,
        status: OrderStatus | None = None,
        customer_id: str | None = None,
        limit: int = 50,
        offset: int = 0,
    ) -> Sequence[Order]:
        """Return orders for a business, optionally filtered by status or customer."""
        stmt = (
            select(Order)
            .where(Order.business_id == business_id)
            .order_by(Order.created_at.desc())
            .limit(limit)
            .offset(offset)
        )
        if status is not None:
            stmt = stmt.where(Order.status == status)
        if customer_id is not None:
            stmt = stmt.where(Order.customer_id == customer_id)
        result = await self._session.execute(stmt)
        return result.scalars().all()

    async def update_status(self, order_id: str, status: OrderStatus) -> Order | None:
        """Update the status of an order. Returns the updated order or None."""
        order = await self.get_by_id(order_id)
        if order is None:
            return None
        order.status = status
        await self._session.flush()
        await self._session.refresh(order)
        return order

    async def delete(self, order_id: str) -> bool:
        """Delete an order. Returns True if deleted, False if not found."""
        order = await self.get_by_id(order_id)
        if order is None:
            return False
        await self._session.delete(order)
        return True
