from shoptalk.seller_next_step_label import label_seller_next_step


def test_seller_next_step_label():
    assert label_seller_next_step(True, False) == "collect payment"
