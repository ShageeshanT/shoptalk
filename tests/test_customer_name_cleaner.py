from shoptalk.customer_name_cleaner import customer_name_cleaner

def test_customer_name_cleaner():
    assert customer_name_cleaner("  nIma   perera ") == "Nima Perera"
