from shoptalk.delivery import detect_delivery_preference


def test_detect_delivery_preference_finds_delivery() -> None:
    assert detect_delivery_preference("can you deliver to malabe") == "delivery"


def test_detect_delivery_preference_finds_pickup() -> None:
    assert detect_delivery_preference("I will pick up at 5") == "pickup"
