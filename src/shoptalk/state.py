from shoptalk.schemas import Business, Customer, FollowUp, Order
from shoptalk.storage import InMemoryRepository


class AppState:
    def __init__(self) -> None:
        self.businesses: InMemoryRepository[Business] = InMemoryRepository()
        self.customers: InMemoryRepository[Customer] = InMemoryRepository()
        self.orders: InMemoryRepository[Order] = InMemoryRepository()
        self.follow_ups: InMemoryRepository[FollowUp] = InMemoryRepository()


state = AppState()
