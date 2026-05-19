from uuid import UUID

from fastapi import APIRouter, HTTPException

from shoptalk.kanban import build_kanban_board
from shoptalk.schemas import KanbanBoard
from shoptalk.state import state

router = APIRouter(prefix="/kanban", tags=["kanban"])


@router.get("/orders", response_model=KanbanBoard)
def get_order_kanban(
    business_id: UUID | None = None,
    include_done: bool = False,
) -> KanbanBoard:
    if business_id is not None and state.businesses.get(business_id) is None:
        raise HTTPException(status_code=404, detail="Business not found")
    return build_kanban_board(
        orders=state.orders.list(),
        business_id=business_id,
        include_done=include_done,
    )
