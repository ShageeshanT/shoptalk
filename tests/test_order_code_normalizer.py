from shoptalk.order_code_normalizer import order_code_normalizer

def test_order_code_normalizer():
    assert order_code_normalizer(" st 12 ") == "ST-12"
