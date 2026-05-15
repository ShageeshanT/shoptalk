from uuid import UUID

from fastapi import APIRouter, HTTPException, status

from shoptalk.schemas import SellerTask, SellerTaskOut
from shoptalk.state import state

router = APIRouter(prefix="/tasks", tags=["tasks"])


@router.post("", response_model=SellerTaskOut, status_code=status.HTTP_201_CREATED)
def create_task(payload: SellerTask) -> SellerTaskOut:
    if state.businesses.get(payload.business_id) is None:
        raise HTTPException(status_code=404, detail="Business not found")
    task = SellerTaskOut(**payload.model_dump())
    state.tasks.add(task)
    return task


@router.get("", response_model=list[SellerTaskOut])
def list_tasks(business_id: UUID | None = None, done: bool | None = None) -> list[SellerTaskOut]:
    tasks = state.tasks.list()
    if business_id is not None:
        tasks = [task for task in tasks if task.business_id == business_id]
    if done is not None:
        tasks = [task for task in tasks if task.done is done]
    return tasks
