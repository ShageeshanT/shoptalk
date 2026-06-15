"""ShopTalk domain models.

This package provides Pydantic models for the core ShopTalk domain entities.
These models are used for data validation, serialisation, and documentation.

Available models
----------------
- :class:`~shoptalk.models.message.CustomerMessage`
- :class:`~shoptalk.models.order.Order`
- :class:`~shoptalk.models.business.Business`
- :class:`~shoptalk.models.customer.Customer`
- :class:`~shoptalk.models.follow_up.FollowUp`
"""

from shoptalk.models.business import Business
from shoptalk.models.customer import Customer
from shoptalk.models.follow_up import FollowUp
from shoptalk.models.message import CustomerMessage
from shoptalk.models.order import Order

__all__ = [
    "Business",
    "Customer",
    "CustomerMessage",
    "FollowUp",
    "Order",
]
