from uuid import uuid4

from shoptalk.action_plan import build_daily_action_plan
from shoptalk.schemas import Business, ConversationMessageOut, Order
from shoptalk.state import state


def test_daily_action_plan_prioritizes_urgent_messages() -> None:
    business = state.businesses.add(Business(name="Plan Bakery"))
    state.orders.add(Order(business_id=business.id, title="Cake"))
    state.messages.add(
        ConversationMessageOut(business_id=business.id, text="urgent delivery update please")
    )

    plan = build_daily_action_plan(business.id)

    assert plan.business_id == business.id
    assert plan.actions[0].priority == "high"
    assert "urgent" in plan.actions[0].reason.lower()
    assert plan.total_actions >= 2


def test_daily_action_plan_has_low_priority_fallback() -> None:
    empty_business_id = uuid4()

    plan = build_daily_action_plan(empty_business_id)

    assert plan.total_actions == 1
    assert plan.actions[0].priority == "low"
