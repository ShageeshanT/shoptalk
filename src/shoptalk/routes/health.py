"""Health check endpoint."""

from datetime import datetime, timezone

from fastapi import APIRouter
from pydantic import BaseModel

from shoptalk import __version__

router = APIRouter(tags=["health"])

_started_at = datetime.now(timezone.utc)


class HealthResponse(BaseModel):
    status: str
    version: str
    uptime_seconds: float


@router.get("/health", response_model=HealthResponse)
def health_check() -> HealthResponse:
    """Return service health status."""
    uptime = (datetime.now(timezone.utc) - _started_at).total_seconds()
    return HealthResponse(status="ok", version=__version__, uptime_seconds=uptime)
