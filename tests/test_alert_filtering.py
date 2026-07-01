from shoptalk.alert_filtering import filter_alert_levels


def test_filter_alert_levels_behavior():
    assert filter_alert_levels(["danger", "info"], "all") == ["danger", "info"]
    assert filter_alert_levels(["danger", "info"], "danger") == ["danger"]
