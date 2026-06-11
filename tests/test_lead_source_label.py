from shoptalk.lead_source_label import classify_lead_source


def test_classify_lead_source_labels_key_states():
    assert classify_lead_source(False) == 'Unknown'
    assert classify_lead_source(True) == 'Known'
