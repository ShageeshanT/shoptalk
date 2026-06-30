from shoptalk.customer_wait_label import customer_wait_label

def test_customer_wait_label():
    assert customer_wait_label(90) == "slow reply"
