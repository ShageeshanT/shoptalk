from shoptalk.customer_trust_label import label_customer_trust


def test_customer_trust_label():
    assert label_customer_trust(4) == "trusted"
