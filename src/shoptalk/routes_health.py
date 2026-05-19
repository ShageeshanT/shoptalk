from fastapi import APIRouter

from shoptalk.health import build_health_check
from shoptalk.schemas import HealthCheck

router = APIRouter(prefix="/health", tags=["health"])


@router.get("", response_model=HealthCheck)
def get_health_check() -> HealthCheck:
    return build_health_check()
