from shoptalk.catalog_search_phrase import catalog_search_phrase


def test_catalog_search_phrase():
    assert catalog_search_phrase("  Chocolate   Cake ") == "chocolate cake"
