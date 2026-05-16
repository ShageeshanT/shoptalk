from uuid import UUID

from shoptalk.enums import TaskPriority
from shoptalk.schemas import SellerTask, SellerTaskOut


def create_reply_task(
    business_id: UUID,
    title: str,
    customer_id: UUID | None = None,
    priority: TaskPriority = TaskPriority.MEDIUM,
) -> SellerTaskOut:
    return SellerTaskOut(
        business_id=business_id,
        customer_id=customer_id,
        title=title,
        priority=priority,
    )
