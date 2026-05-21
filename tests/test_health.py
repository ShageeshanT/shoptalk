from shoptalk.health import build_health_check


def test_health_check_reports_in_memory_stores() -> None:
    health = build_health_check()

    assert health.status == "ok"
    assert {check.name for check in health.checks} == {"businesses", "messages", "orders", "approvals", "follow_ups"}
    assert all(check.ok for check in health.checks)
