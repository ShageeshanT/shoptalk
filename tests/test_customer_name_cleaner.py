from shoptalk.customer_name_cleaner import clean_customer_name


def test_clean_customer_name():
    assert clean_customer_name("  nimal   perera ") == "Nimal Perera"
