from shoptalk.health_report import DependencyHealth, HealthReport


def test_health_report_ok_requires_all_dependencies() -> None:
    report = HealthReport(dependencies=[DependencyHealth(name="api", ok=True)])
    assert report.ok is True
