from shoptalk.slip_reference_hint import slip_reference_hint

def test_slip_reference_hint():
    assert slip_reference_hint("st12") == "Use ST12 as the payment reference."
