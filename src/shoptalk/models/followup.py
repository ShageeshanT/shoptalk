"""SQLAlchemy ORM model for follow-up reminders."""

from datetime import datetime

from sqlalchemy import Boolean, DateTime, String, Text, func
from sqlalchemy.orm import Mapped, mapped_column

from shoptalk.models.base import Base


class FollowUp(Base):
    """A reminder to follow up with a customer at a specific time."""

    __tablename__ = "followups"

    id: Mapped[str] = mapped_column(String(36), primary_key=True)
    business_id: Mapped[str] = mapped_column(String(36), nullable=False, index=True)
    customer_id: Mapped[str] = mapped_column(String(36), nullable=False, index=True)
    order_id: Mapped[str | None] = mapped_column(String(36), nullable=True)
    reason: Mapped[str] = mapped_column(String(300), nullable=False)
    due_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), nullable=False, index=True)
    completed: Mapped[bool] = mapped_column(Boolean, nullable=False, default=False)
    completed_at: Mapped[datetime | None] = mapped_column(DateTime(timezone=True), nullable=True)
    notes: Mapped[str | None] = mapped_column(Text, nullable=True)
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now(), nullable=False
    )

    def __repr__(self) -> str:
        return f"<FollowUp id={self.id!r} due_at={self.due_at!r} completed={self.completed!r}>"
