from shoptalk.campaign_status_label import campaign_status_label

def test_campaign_status_label_known_values():
    assert campaign_status_label('active') == 'Active campaign'
    assert campaign_status_label('paused') == 'Paused campaign'
    assert campaign_status_label('ended') == 'Ended campaign'

def test_campaign_status_label_unknown_value():
    assert campaign_status_label("") == 'Draft campaign'
