from uuid import uuid4

from shoptalk.schemas import Business, Customer
from shoptalk.state import state


def seed_demo_data() -> dict[str, str]:
    business = Business(id=uuid4(), name="Demo Bakery", owner_name="Demo Seller", whatsapp_number="+94770000000")
    customer = Customer(id=uuid4(), business_id=business.id, name="Sample Customer", phone="+94771111111")
    state.businesses.add(business)
    state.customers.add(customer)
    return {"business_id": str(business.id), "customer_id": str(customer.id)}
