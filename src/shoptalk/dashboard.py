from pydantic import BaseModel

from shoptalk.enums import FollowUpStatus, OrderStatus
from shoptalk.state import state


class DashboardSummary(BaseModel):
    businesses: int
    customers: int
    orders: int
    messages: int
    approval_drafts: int
    open_follow_ups: int
    payment_pending_orders: int


def get_dashboard_summary() -> DashboardSummary:
    orders = state.orders.list()
    follow_ups = state.follow_ups.list()
    return DashboardSummary(
        businesses=len(state.businesses.list()),
        customers=len(state.customers.list()),
        orders=len(orders),
        messages=len(state.messages.list()),
        approval_drafts=len(state.approvals.list()),
        open_follow_ups=sum(1 for item in follow_ups if item.status == FollowUpStatus.OPEN),
        payment_pending_orders=sum(1 for item in orders if item.status == OrderStatus.PAYMENT_PENDING),
    )
