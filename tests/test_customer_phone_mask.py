from shoptalk.customer_phone_mask import customer_phone_mask

def test_customer_phone_mask():
    assert customer_phone_mask("94771234567") == "***4567"
