from shoptalk.approval import ApprovalDraft
from shoptalk.schemas import Business, ConversationMessageOut, Customer, FollowUp, Order, SellerTaskOut
from shoptalk.storage import InMemoryRepository


class AppState:
    def __init__(self) -> None:
        self.businesses: InMemoryRepository[Business] = InMemoryRepository()
        self.customers: InMemoryRepository[Customer] = InMemoryRepository()
        self.orders: InMemoryRepository[Order] = InMemoryRepository()
        self.follow_ups: InMemoryRepository[FollowUp] = InMemoryRepository()
        self.messages: InMemoryRepository[ConversationMessageOut] = InMemoryRepository()
        self.tasks: InMemoryRepository[SellerTaskOut] = InMemoryRepository()
        self.approvals: InMemoryRepository[ApprovalDraft] = InMemoryRepository()


state = AppState()
