from shoptalk.catalog_availability_label import catalog_availability_label

def test_catalog_availability_label():
    assert catalog_availability_label(False)=="Hidden"