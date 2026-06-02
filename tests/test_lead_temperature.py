from shoptalk.lead_temperature import lead_temperature


def test_lead_temperature_hot_for_high_urgency_orders():
    assert lead_temperature("new_order", "high") == "hot"


def test_lead_temperature_warm_for_price_questions():
    assert lead_temperature("general", "normal", asks_price=True) == "warm"
