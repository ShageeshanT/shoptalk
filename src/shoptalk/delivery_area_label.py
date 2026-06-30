def delivery_area_label(distance_km):
    return "nearby" if distance_km <= 5 else "city" if distance_km <= 20 else "far"
