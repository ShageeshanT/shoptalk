from shoptalk.enums import OrderStatus
from shoptalk.schemas import Order


def unpaid_orders(orders: list[Order]) -> list[Order]:
    return [order for order in orders if order.payment_status != 'paid']


def active_orders(orders: list[Order]) -> list[Order]:
    return [order for order in orders if order.status not in {OrderStatus.DELIVERED, OrderStatus.CANCELLED}]
