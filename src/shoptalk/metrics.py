from shoptalk.enums import FollowUpStatus, OrderStatus
from shoptalk.state import state


def business_metrics() -> dict[str, int]:
    orders = state.orders.list()
    follow_ups = state.follow_ups.list()
    tasks = state.tasks.list()
    return {
        "businesses": len(state.businesses.list()),
        "customers": len(state.customers.list()),
        "orders": len(orders),
        "open_orders": sum(order.status not in {OrderStatus.DELIVERED, OrderStatus.CANCELLED} for order in orders),
        "pending_follow_ups": sum(follow_up.status == FollowUpStatus.OPEN for follow_up in follow_ups),
        "open_tasks": sum(not task.done for task in tasks),
    }
