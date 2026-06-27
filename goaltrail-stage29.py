# === Stage 29: Add reminder helpers that return upcoming items ===
# Project: GoalTrail
def get_upcoming_items(items: list[dict], now: datetime = None) -> list[tuple[str, str]]:
    if items is None:
        return []
    if now is None:
        now = datetime.now()
    today = date.today()
    upcoming = []
    for item in items:
        due_date_str = item.get("due_date") or item.get("deadline")
        if not due_date_str:
            continue
        try:
            due_date = datetime.strptime(due_date_str, "%Y-%m-%d").date()
        except ValueError:
            continue
        delta = (due_date - today).days
        if delta <= 0 and delta > -365:
            status = "overdue" if delta < 0 else "today"
            upcoming.append((item.get("title", "Unknown"), status))
    return sorted(upcoming, key=lambda x: datetime.strptime(x[1], "%Y-%m-%d").date() if len(x) > 1 else today)
