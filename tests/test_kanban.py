from uuid import uuid4

from shoptalk.enums import OrderStatus
from shoptalk.kanban import build_kanban_board
from shoptalk.schemas import Order


def test_kanban_groups_active_orders_by_status() -> None:
    business_id = uuid4()
    other_business_id = uuid4()
    board = build_kanban_board(
        [
            Order(business_id=business_id, title="Cupcake box", status=OrderStatus.NEW_INQUIRY),
            Order(business_id=business_id, title="Ribbon cake", status=OrderStatus.PAYMENT_PENDING),
            Order(business_id=business_id, title="Delivered brownies", status=OrderStatus.DELIVERED),
            Order(business_id=other_business_id, title="Other shop cake", status=OrderStatus.PAID),
        ],
        business_id=business_id,
    )

    columns = {column.status: column for column in board.columns}

    assert board.business_id == business_id
    assert board.total_orders == 3
    assert board.hidden_done_orders == 1
    assert columns[OrderStatus.NEW_INQUIRY].count == 1
    assert columns[OrderStatus.PAYMENT_PENDING].orders[0].title == "Ribbon cake"
    assert OrderStatus.DELIVERED not in columns


def test_kanban_can_include_done_columns() -> None:
    business_id = uuid4()
    board = build_kanban_board(
        [Order(business_id=business_id, title="Delivered cake", status=OrderStatus.DELIVERED)],
        include_done=True,
    )

    delivered_column = next(column for column in board.columns if column.status == OrderStatus.DELIVERED)

    assert delivered_column.count == 1
    assert board.hidden_done_orders == 0
