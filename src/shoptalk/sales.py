from shoptalk.enums import OrderStatus
from shoptalk.schemas import SalesFunnel
from shoptalk.state import state


def sales_funnel() -> SalesFunnel:
    counts = {status: 0 for status in OrderStatus}
    for order in state.orders.list():
        counts[order.status] += 1

    return SalesFunnel(
        new_inquiries=counts[OrderStatus.NEW_INQUIRY],
        payment_pending=counts[OrderStatus.PAYMENT_PENDING],
        paid=counts[OrderStatus.PAID],
        preparing=counts[OrderStatus.PREPARING],
        ready=counts[OrderStatus.READY],
        delivered=counts[OrderStatus.DELIVERED],
        cancelled=counts[OrderStatus.CANCELLED],
    )
