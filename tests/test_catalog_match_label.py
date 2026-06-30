from shoptalk.catalog_match_label import label_catalog_match


def test_catalog_match_label():
    assert label_catalog_match(82) == "exact"
