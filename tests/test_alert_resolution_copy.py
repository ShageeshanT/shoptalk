from shoptalk.alert_resolution_copy import alert_resolution_copy


def test_resolved_status_copy():
    assert alert_resolution_copy("resolved") == "Resolved. Nice, one less gremlin in the inbox."


def test_waiting_status_copy():
    assert alert_resolution_copy("waiting_on_customer") == "Waiting for the customer to reply."


def test_unknown_status_defaults_to_seller_reply_needed():
    assert alert_resolution_copy("anything_else") == "Seller reply needed."
