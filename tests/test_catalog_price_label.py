from shoptalk.catalog_price_label import catalog_price_label

def test_catalog_price_label():
    assert catalog_price_label(1500)=="LKR 1,500"