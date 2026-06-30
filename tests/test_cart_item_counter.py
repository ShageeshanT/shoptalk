from shoptalk.cart_item_counter import cart_item_counter

def test_cart_item_counter():
    assert cart_item_counter(["cake", "", " candle "]) == 2
