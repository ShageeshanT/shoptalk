from shoptalk.delivery_slot_pressure import delivery_slot_pressure


def test_delivery_slot_pressure():
    assert delivery_slot_pressure(1) == "tight"
