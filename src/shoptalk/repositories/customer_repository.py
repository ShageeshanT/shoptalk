"""Data access layer for customers."""

from __future__ import annotations

from typing import Sequence

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from shoptalk.models.customer import Customer


class CustomerRepository:
    """Handles all database operations for Customer records."""

    def __init__(self, session: AsyncSession) -> None:
        self._session = session

    async def create(self, customer: Customer) -> Customer:
        """Persist a new customer."""
        self._session.add(customer)
        await self._session.flush()
        await self._session.refresh(customer)
        return customer

    async def get_by_id(self, customer_id: str) -> Customer | None:
        """Return a customer by primary key."""
        return await self._session.get(Customer, customer_id)

    async def get_by_phone(
        self, business_id: str, phone: str
    ) -> Customer | None:
        """Look up a customer by phone number within a business."""
        stmt = select(Customer).where(
            Customer.business_id == business_id,
            Customer.phone == phone,
        )
        result = await self._session.execute(stmt)
        return result.scalar_one_or_none()

    async def list_by_business(
        self, business_id: str, limit: int = 50, offset: int = 0
    ) -> Sequence[Customer]:
        """Return all customers for a business."""
        stmt = (
            select(Customer)
            .where(Customer.business_id == business_id)
            .order_by(Customer.created_at.desc())
            .limit(limit)
            .offset(offset)
        )
        result = await self._session.execute(stmt)
        return result.scalars().all()

    async def get_or_create(
        self, business_id: str, phone: str, name: str | None = None
    ) -> tuple[Customer, bool]:
        """Return existing customer or create a new one. Returns (customer, created)."""
        import uuid
        existing = await self.get_by_phone(business_id, phone)
        if existing:
            return existing, False
        customer = Customer(
            id=str(uuid.uuid4()),
            business_id=business_id,
            phone=phone,
            name=name,
        )
        return await self.create(customer), True
