def delivery_slot_pressure(open_slots):
    return "full" if open_slots <= 0 else "tight" if open_slots <= 2 else "available"
