"""Service for generating the seller's daily briefing."""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime, timezone

from shoptalk.models.followup import FollowUp
from shoptalk.models.order import Order, OrderStatus
from shoptalk.repositories.order_repository import OrderRepository


@dataclass
class BriefingSummary:
    """A snapshot of the seller's current workload."""

    pending_orders: list[Order] = field(default_factory=list)
    in_progress_orders: list[Order] = field(default_factory=list)
    due_followups: list[FollowUp] = field(default_factory=list)
    generated_at: datetime = field(default_factory=lambda: datetime.now(timezone.utc))

    @property
    def total_active_orders(self) -> int:
        return len(self.pending_orders) + len(self.in_progress_orders)

    @property
    def overdue_followups(self) -> list[FollowUp]:
        now = datetime.now(timezone.utc)
        return [f for f in self.due_followups if f.due_at < now]


class DailyBriefingService:
    """Aggregates data for the seller's daily briefing view."""

    def __init__(self, order_repo: OrderRepository) -> None:
        self._order_repo = order_repo

    async def get_briefing(self, business_id: str) -> BriefingSummary:
        """Build a briefing summary for the given business."""
        pending = await self._order_repo.list_by_business(
            business_id, status=OrderStatus.PENDING
        )
        in_progress = await self._order_repo.list_by_business(
            business_id, status=OrderStatus.IN_PROGRESS
        )
        return BriefingSummary(
            pending_orders=list(pending),
            in_progress_orders=list(in_progress),
            due_followups=[],  # TODO: inject FollowUpRepository in Phase 3
        )
