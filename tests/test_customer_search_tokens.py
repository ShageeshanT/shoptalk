from shoptalk.customer_search_tokens import customer_search_tokens


def test_customer_search_tokens_include_name_parts():
    assert customer_search_tokens("Nimal Perera") >= {"nimal", "perera"}


def test_customer_search_tokens_include_phone_digits():
    tokens = customer_search_tokens("Nimal", "+94 77 123 4567")
    assert "94771234567" in tokens
    assert "4567" in tokens
