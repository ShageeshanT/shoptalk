from shoptalk.inventory_signal import inventory_signal

def test_inventory_signal():
    assert inventory_signal(0) == "out"
    assert inventory_signal(2) == "low"
