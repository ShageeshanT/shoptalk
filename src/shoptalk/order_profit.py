"""Profit and margin helpers for seller order summaries."""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class ProfitSummary:
    """Computed order profit metrics."""

    revenue: float
    cost: float
    profit: float
    margin_percent: float
    label: str


def summarize_profit(revenue: float, cost: float = 0) -> ProfitSummary:
    """Return revenue, cost, profit, margin percentage, and a seller-friendly label."""

    safe_revenue = max(float(revenue or 0), 0)
    safe_cost = max(float(cost or 0), 0)
    profit = safe_revenue - safe_cost
    margin_percent = (profit / safe_revenue * 100) if safe_revenue else 0.0
    return ProfitSummary(
        revenue=round(safe_revenue, 2),
        cost=round(safe_cost, 2),
        profit=round(profit, 2),
        margin_percent=round(margin_percent, 2),
        label=_profit_label(profit, margin_percent),
    )


def _profit_label(profit: float, margin_percent: float) -> str:
    if profit < 0:
        return "loss"
    if margin_percent >= 40:
        return "strong_margin"
    if margin_percent >= 20:
        return "healthy_margin"
    if margin_percent > 0:
        return "thin_margin"
    return "break_even"
