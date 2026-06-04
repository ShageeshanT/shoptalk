from shoptalk.customer_wait_label import customer_wait_label


def test_customer_wait_label_fresh():
    assert customer_wait_label(10) == "fresh"


def test_customer_wait_label_overdue():
    assert customer_wait_label(300) == "overdue"
