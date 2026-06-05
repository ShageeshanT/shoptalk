from __future__ import annotations

def currency_label(currency: str) -> str:
    mapping={"LKR":"Rs", "USD":"$", "EUR":"€", "GBP":"£"}
    return mapping.get(currency.upper(), currency.upper() or "LKR")