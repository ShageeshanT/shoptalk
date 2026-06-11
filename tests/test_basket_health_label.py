    from shoptalk.basket_health_label import classify_basket_health


    def test_classify_basket_health_labels_key_states():
        assert classify_basket_health(-1) == 'Empty'
assert classify_basket_health(1) == 'Healthy'
assert classify_basket_health(10) == 'Review bulk'
