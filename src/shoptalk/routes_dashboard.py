from fastapi import APIRouter

from shoptalk.dashboard import DashboardSummary, get_dashboard_summary

router = APIRouter(prefix="/dashboard", tags=["dashboard"])


@router.get("/summary", response_model=DashboardSummary)
def dashboard_summary() -> DashboardSummary:
    return get_dashboard_summary()
