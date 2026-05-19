from uuid import UUID

from shoptalk.briefing import daily_brief
from shoptalk.schemas import DailyActionItem, DailyActionPlan
from shoptalk.state import state


def build_daily_action_plan(business_id: UUID | None = None) -> DailyActionPlan:
    brief = daily_brief(business_id)
    actions: list[DailyActionItem] = []

    if brief.urgent_messages:
        actions.append(
            DailyActionItem(
                title="Reply to urgent customers",
                priority="high",
                reason=f"{brief.urgent_messages} urgent message(s) are waiting.",
            )
        )
    if brief.pending_follow_ups:
        actions.append(
            DailyActionItem(
                title="Clear follow-up queue",
                priority="high" if brief.pending_follow_ups >= 3 else "normal",
                reason=f"{brief.pending_follow_ups} follow-up(s) need seller attention.",
            )
        )
    if brief.open_orders:
        actions.append(
            DailyActionItem(
                title="Review open orders",
                priority="normal",
                reason=f"{brief.open_orders} open order(s) could affect delivery promises.",
            )
        )

    if not actions:
        actions.append(
            DailyActionItem(
                title="Keep inbox monitored",
                priority="low",
                reason="No urgent sales desk work is queued right now.",
            )
        )

    return DailyActionPlan(
        business_id=business_id,
        generated_from="daily_brief",
        actions=actions,
        total_actions=len(actions),
    )
