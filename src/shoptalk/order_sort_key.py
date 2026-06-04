PRIORITY_WEIGHT = {"urgent": 0, "high": 1, "normal": 2, "low": 3}


def order_sort_key(priority: str, created_index: int) -> tuple[int, int]:
    return (PRIORITY_WEIGHT.get(priority, 2), created_index)
