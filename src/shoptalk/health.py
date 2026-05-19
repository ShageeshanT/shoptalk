from shoptalk.schemas import HealthCheck, HealthCheckItem
from shoptalk.state import state


def build_health_check() -> HealthCheck:
    checks = [
        HealthCheckItem(name="businesses", ok=len(state.businesses.list()) >= 0, detail="Business store is reachable."),
        HealthCheckItem(name="messages", ok=len(state.messages.list()) >= 0, detail="Message store is reachable."),
        HealthCheckItem(name="orders", ok=len(state.orders.list()) >= 0, detail="Order store is reachable."),
    ]
    return HealthCheck(status="ok" if all(check.ok for check in checks) else "degraded", checks=checks)
