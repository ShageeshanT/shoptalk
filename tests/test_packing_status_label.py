from shoptalk.packing_status_label import packing_status_label

def test_packing_status_label_known_values():
    assert packing_status_label('packed') == 'Packed'
    assert packing_status_label('packing') == 'Packing'
    assert packing_status_label('blocked') == 'Packing blocked'

def test_packing_status_label_unknown_value():
    assert packing_status_label("") == 'Not packed'
