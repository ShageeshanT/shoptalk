from enum import StrEnum


class BusinessType(StrEnum):
    HOME_BAKERY = "home_bakery"
    CLOTHING = "clothing"
    FLORIST = "florist"
    SALON = "salon"
    REPAIR = "repair"
    RENTAL = "rental"
    GENERAL = "general"


class OrderStatus(StrEnum):
    NEW_INQUIRY = "new_inquiry"
    CONFIRMED = "confirmed"
    PAYMENT_PENDING = "payment_pending"
    PAID = "paid"
    PREPARING = "preparing"
    READY = "ready"
    DELIVERED = "delivered"
    CANCELLED = "cancelled"


class FollowUpStatus(StrEnum):
    OPEN = "open"
    DONE = "done"
    CANCELLED = "cancelled"
