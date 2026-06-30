from shoptalk.seller_focus_label import label_seller_focus


def test_seller_focus_label():
    assert label_seller_focus(1) == "overdue"
