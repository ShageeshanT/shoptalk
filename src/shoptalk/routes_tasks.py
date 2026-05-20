from uuid import UUID

from fastapi import APIRouter, HTTPException, status

from shoptalk.schemas import SellerTask, SellerTaskOut
from shoptalk.status_updates import TaskStatusUpdate
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


@router.patch("/{task_id}", response_model=SellerTaskOut)
def update_task_status(task_id: UUID, payload: TaskStatusUpdate) -> SellerTaskOut:
    task = state.tasks.get(task_id)
    if task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    updated = task.model_copy(update={"done": payload.done})
    state.tasks.add(updated)
    return updated
