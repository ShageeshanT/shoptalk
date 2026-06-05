from shoptalk.customer_initials import customer_initials

def test_customer_initials():
    assert customer_initials("Nimal Perera") == "NP"
    assert customer_initials(" ") == "?"