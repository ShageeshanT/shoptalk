from shoptalk.alert_empty_state import seller_alert_empty_state


def test_returns_empty_state_when_alert_queue_is_clear():
    assert seller_alert_empty_state(0) == "No urgent chats right now. Keep selling, tiny chaos goblin contained."


def test_returns_none_when_alerts_exist():
    assert seller_alert_empty_state(3) is None
