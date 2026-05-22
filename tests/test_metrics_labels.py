from shoptalk.metrics_labels import metric_name


def test_metric_name_normalizes_metric_parts() -> None:
    assert metric_name("Shop Talk", "Open Orders") == "shop_talk.open_orders"
