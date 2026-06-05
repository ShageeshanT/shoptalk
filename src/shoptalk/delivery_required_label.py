from __future__ import annotations

def delivery_required_label(required: bool | None) -> str:
    return "Delivery needed" if required is True else "Pickup/no delivery" if required is False else "Delivery not confirmed"