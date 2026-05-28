from shoptalk.customer_value import customer_value_label


def test_customer_value_vip():
    assert customer_value_label(10, 50000) == "vip"
    assert customer_value_label(2, 100000) == "vip"


def test_customer_value_repeat():
    assert customer_value_label(3, 1000) == "repeat"


def test_customer_value_new_and_prospect():
    assert customer_value_label(1, 500) == "new_buyer"
    assert customer_value_label(0, 0) == "prospect"
