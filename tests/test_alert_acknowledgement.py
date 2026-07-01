from shoptalk.alert_acknowledgement import alert_acknowledgement_copy


def test_alert_acknowledgement_copy_behavior():
    assert alert_acknowledgement_copy("danger") == "Danger alert acknowledged."
    assert alert_acknowledgement_copy("info") == "Alert acknowledged."
