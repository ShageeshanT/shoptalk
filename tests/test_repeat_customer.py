from shoptalk.repeat_customer import is_repeat_customer, repeat_customer_label


def test_repeat_customer_threshold():
    assert is_repeat_customer(1) is False
    assert is_repeat_customer(2) is True


def test_repeat_customer_label():
    assert repeat_customer_label(0) == "new"
    assert repeat_customer_label(3) == "repeat"
    assert repeat_customer_label(5) == "loyal"
