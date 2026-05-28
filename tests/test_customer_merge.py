from shoptalk.customer_merge import likely_same_customer, normalized_phone


def test_normalized_phone():
    assert normalized_phone("+94 77 123 4567") == "94771234567"


def test_likely_same_customer_by_phone():
    assert likely_same_customer("A", "+94 77 1", "B", "94771")


def test_likely_same_customer_by_name():
    assert likely_same_customer("Nimal", "", " nimal ", "")
