from shoptalk.seller_alerts import SellerAlert, build_seller_alert


def test_builds_danger_alert_for_refund_request():
    alert = build_seller_alert("Customer wants a refund because order is late")
    assert alert == SellerAlert("danger", "Customer needs attention", "Customer wants a refund because order is late")


def test_builds_warning_alert_for_urgent_message():
    alert = build_seller_alert("Need this today please")
    assert alert is not None
    assert alert.level == "warning"


def test_ignores_normal_message():
    assert build_seller_alert("Can I order two cupcakes?") is None
