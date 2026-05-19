from collections import Counter
from uuid import UUID

from shoptalk.enums import OrderStatus
from shoptalk.schemas import KanbanBoard, KanbanColumn, KanbanOrderCard, Order

ACTIVE_STATUSES = [
    OrderStatus.NEW_INQUIRY,
    OrderStatus.PAYMENT_PENDING,
    OrderStatus.PAID,
    OrderStatus.PREPARING,
    OrderStatus.READY,
]

STATUS_TITLES = {
    OrderStatus.NEW_INQUIRY: "New inquiries",
    OrderStatus.CONFIRMED: "Confirmed",
    OrderStatus.PAYMENT_PENDING: "Payment pending",
    OrderStatus.PAID: "Paid",
    OrderStatus.PREPARING: "Preparing",
    OrderStatus.READY: "Ready",
    OrderStatus.DELIVERED: "Delivered",
    OrderStatus.CANCELLED: "Cancelled",
}


def build_order_card(order: Order) -> KanbanOrderCard:
    return KanbanOrderCard(
        order_id=order.id,
        title=order.title,
        customer_id=order.customer_id,
        total_amount=order.total_amount,
        delivery_date=order.delivery_date,
    )


def build_kanban_board(
    orders: list[Order],
    business_id: UUID | None = None,
    include_done: bool = False,
) -> KanbanBoard:
    filtered_orders = [
        order for order in orders if business_id is None or order.business_id == business_id
    ]
    statuses = list(OrderStatus) if include_done else ACTIVE_STATUSES
    orders_by_status: dict[OrderStatus, list[Order]] = {status: [] for status in statuses}

    for order in filtered_orders:
        if order.status in orders_by_status:
            orders_by_status[order.status].append(order)

    columns = [
        KanbanColumn(
            status=status,
            title=STATUS_TITLES[status],
            count=len(status_orders),
            orders=[build_order_card(order) for order in status_orders],
        )
        for status, status_orders in orders_by_status.items()
    ]

    totals = Counter(order.status for order in filtered_orders)
    return KanbanBoard(
        business_id=business_id,
        columns=columns,
        total_orders=len(filtered_orders),
        hidden_done_orders=0 if include_done else totals[OrderStatus.DELIVERED] + totals[OrderStatus.CANCELLED],
    )
