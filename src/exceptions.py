"""Custom exceptions for ShopTalk."""


class ShopTalkError(Exception):
    """Base exception for all ShopTalk errors."""

    def __init__(self, message: str, error_code: str = "SHOPTALJ_ERROR"):
        self.message = message
        self.error_code = error_code
        super().__init__(message)

    def __str__(self):
        return f"[{self.error_code}] {self.message}"

    def __repr__(self):
        return f"{self.__class__.__name__}(message={self.message!r}, error_code={self.error_code!r})"


class AuthenticationError(ShopTalkError):
    def __init__(self, message: str = "Authentication failed"):
        super().__init__(message, "AUTH_ERROR")


class OrderNotFoundError(ShopTalkError):
    def __init__(self, order_id: str):
        super().__init__(f"Order not found: {order_id}", "ORDER_NOT_FOUND")
        self.order_id = order_id


class CustomerNotFoundError(ShopTalkError):
    def __init__(self, identifier: str):
        super().__init__(f"Customer not found: {identifier}", "CUSTOMER_NOT_FOUND")
        self.identifier = identifier


class PaymentError(ShopTalkError):
    def __init__(self, message: str, reference: str = ""):
        super().__init__(message, "PAYMENT_ERROR")
        self.reference = reference


class WebhookValidationError(ShopTalkError):
    def __init__(self, message: str = "Webhook validation failed"):
        super().__init__(message, "WEBHOOK_VALIDATION_ERROR")


class RateLimitError(ShopTalkError):
    def __init__(self, customer_id: str, retry_after: int = 60):
        super().__init__(
            f"Rate limit exceeded for customer {customer_id}. Retry after {retry_after}s",
            "RATE_LIMIT_ERROR",
        )
        self.customer_id = customer_id
        self.retry_after = retry_after


class ProductNotFoundError(ShopTalkError):
    def __init__(self, product_id: str):
        super().__init__(f"Product not found: {product_id}", "PRODUCT_NOT_FOUND")
        self.product_id = product_id


class InsufficientStockError(ShopTalkError):
    def __init__(self, product_id: str, requested: int, available: int):
        super().__init__(
            f"Insufficient stock for {product_id}: requested {requested}, available {available}",
            "INSUFFICIENT_STOCK",
        )
        self.product_id = product_id
        self.requested = requested
        self.available = available
