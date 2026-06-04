from shoptalk.delivery_eta_copy import delivery_eta_copy


def test_delivery_eta_copy_window_only():
    assert delivery_eta_copy("Friday evening") == "Delivery is planned for Friday evening."


def test_delivery_eta_copy_with_location():
    assert delivery_eta_copy("Friday", "Colombo") == "Delivery is planned for Friday to Colombo."
