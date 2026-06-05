from shoptalk.address_preview import address_preview

def test_address_preview():
    assert address_preview("  Colombo   Sri Lanka ")=="Colombo Sri Lanka"