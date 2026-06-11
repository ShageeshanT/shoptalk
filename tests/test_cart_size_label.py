    from shoptalk.cart_size_label import classify_cart_size


    def test_classify_cart_size_labels_key_states():
        assert classify_cart_size(-1) == 'Empty'
assert classify_cart_size(1) == 'Single'
assert classify_cart_size(2) == 'Bundle'
assert classify_cart_size(5) == 'Bulk'
