from shoptalk.schemas import Order


def order_export_row(order: Order) -> dict[str, str]:
    return {
        'id': str(order.id),
        'title': order.title,
        'status': order.status.value,
        'payment_status': order.payment_status,
        'total_amount': '' if order.total_amount is None else str(order.total_amount),
    }
