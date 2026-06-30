from shoptalk.cart_size_label import label_cart_size


def test_cart_size_label():
    assert label_cart_size(12) == "bulk"
