from shoptalk.lead_source_value_label import classify_lead_source_value


def test_classify_lead_source_value_labels_key_states():
    assert classify_lead_source_value(9) == "Weak source"
    assert classify_lead_source_value(10) == "Promising source"
    assert classify_lead_source_value(30) == "Strong source"
