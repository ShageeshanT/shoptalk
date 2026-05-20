from pydantic import BaseModel

from shoptalk.enums import FollowUpStatus, OrderStatus


class TaskStatusUpdate(BaseModel):
    done: bool


class FollowUpStatusUpdate(BaseModel):
    status: FollowUpStatus


class OrderStatusUpdate(BaseModel):
    status: OrderStatus


class CustomerNoteUpdate(BaseModel):
    notes: str
