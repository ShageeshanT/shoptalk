from shoptalk.seller_greeting_copy import seller_greeting_copy

def test_seller_greeting_copy():
    assert "Bakery" in seller_greeting_copy("Bakery")
