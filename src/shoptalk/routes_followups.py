from uuid import UUID

from fastapi import APIRouter, HTTPException, status

from shoptalk.followups import follow_up_priority
from shoptalk.schemas import FollowUp, FollowUpCreate, FollowUpQueueItem
from shoptalk.status_updates import FollowUpStatusUpdate
from shoptalk.state import state

router = APIRouter(prefix="/follow-ups", tags=["follow-ups"])


def _validate_follow_up_links(payload: FollowUpCreate) -> None:
    if state.businesses.get(payload.business_id) is None:
        raise HTTPException(status_code=404, detail="Business not found")
    if payload.customer_id is not None and state.customers.get(payload.customer_id) is None:
        raise HTTPException(status_code=404, detail="Customer not found")
    if payload.order_id is not None and state.orders.get(payload.order_id) is None:
        raise HTTPException(status_code=404, detail="Order not found")


@router.post("", response_model=FollowUp, status_code=status.HTTP_201_CREATED)
def create_follow_up(payload: FollowUpCreate) -> FollowUp:
    _validate_follow_up_links(payload)
    follow_up = FollowUp(**payload.model_dump())
    return state.follow_ups.add(follow_up)


@router.get("", response_model=list[FollowUp])
def list_follow_ups(business_id: UUID | None = None) -> list[FollowUp]:
    if business_id is None:
        return state.follow_ups.list()
    if state.businesses.get(business_id) is None:
        raise HTTPException(status_code=404, detail="Business not found")
    return state.follow_ups.list_for_business(business_id)


@router.get("/queue", response_model=list[FollowUpQueueItem])
def follow_up_queue(business_id: UUID | None = None) -> list[FollowUpQueueItem]:
    follow_ups = list_follow_ups(business_id)
    queue = [
        FollowUpQueueItem(follow_up=follow_up, priority=follow_up_priority(follow_up))
        for follow_up in follow_ups
    ]
    return sorted(queue, key=lambda item: item.priority, reverse=True)


@router.get("/{follow_up_id}", response_model=FollowUp)
def get_follow_up(follow_up_id: UUID) -> FollowUp:
    follow_up = state.follow_ups.get(follow_up_id)
    if follow_up is None:
        raise HTTPException(status_code=404, detail="Follow-up not found")
    return follow_up


@router.patch("/{follow_up_id}/status", response_model=FollowUp)
def update_follow_up_status(follow_up_id: UUID, payload: FollowUpStatusUpdate) -> FollowUp:
    follow_up = state.follow_ups.get(follow_up_id)
    if follow_up is None:
        raise HTTPException(status_code=404, detail="Follow-up not found")
    updated = follow_up.model_copy(update={"status": payload.status})
    state.follow_ups.add(updated)
    return updated
