from shoptalk.catalog_matcher import match_catalog_items


def test_match_catalog_items():
    assert match_catalog_items("Need brownies and cake", ["Brownies", "Cupcakes", "Cake"]) == ["Brownies", "Cake"]


def test_match_catalog_items_empty():
    assert match_catalog_items("hello", ["Cake"]) == []
