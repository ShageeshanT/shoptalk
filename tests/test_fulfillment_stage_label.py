from shoptalk.fulfillment_stage_label import fulfillment_stage_label

def test_fulfillment_stage_label():
    assert fulfillment_stage_label(True, False, False) == "prepare"
