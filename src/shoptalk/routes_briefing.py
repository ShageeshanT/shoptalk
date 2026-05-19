from uuid import UUID

from fastapi import APIRouter, HTTPException

from shoptalk.action_plan import build_daily_action_plan
from shoptalk.briefing import daily_brief
from shoptalk.schemas import DailyActionPlan, DailyBrief
from shoptalk.state import state

router = APIRouter(prefix="/briefing", tags=["briefing"])


@router.get("/daily", response_model=DailyBrief)
def get_daily_brief(business_id: UUID | None = None) -> DailyBrief:
    if business_id is not None and state.businesses.get(business_id) is None:
        raise HTTPException(status_code=404, detail="Business not found")
    return daily_brief(business_id)


@router.get("/daily/action-plan", response_model=DailyActionPlan)
def get_daily_action_plan(business_id: UUID | None = None) -> DailyActionPlan:
    if business_id is not None and state.businesses.get(business_id) is None:
        raise HTTPException(status_code=404, detail="Business not found")
    return build_daily_action_plan(business_id)
