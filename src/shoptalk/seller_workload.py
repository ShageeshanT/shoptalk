def workload_label(open_tasks: int, overdue_tasks: int = 0) -> str:
    if overdue_tasks > 0 or open_tasks >= 15:
        return "overloaded"
    if open_tasks >= 7:
        return "busy"
    return "clear"


def should_show_workload_warning(open_tasks: int, overdue_tasks: int = 0) -> bool:
    return workload_label(open_tasks, overdue_tasks) in {"busy", "overloaded"}
