"""Catalog stock signal helpers."""

from __future__ import annotations


def stock_signal(quantity: int) -> str:
    """Return a seller friendly stock status label."""

    if quantity <= 0:
        return "out_of_stock"
    if quantity <= 3:
        return "low_stock"
    return "available"


def should_warn_low_stock(quantity: int) -> bool:
    """Return whether a stock warning should be shown."""

    return stock_signal(quantity) in {"out_of_stock", "low_stock"}
