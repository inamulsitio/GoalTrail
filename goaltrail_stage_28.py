# === Stage 28: Add overdue item detection based on due dates ===
# Project: GoalTrail
def detect_overdue_items(data, today):
    overdue = []
    for item in data.get("items", []):
        due_date_str = item.get("due_date")
        if due_date_str:
            try:
                due_date = datetime.fromisoformat(due_date_str.replace("Z", "+00:00"))
                if today > due_date:
                    overdue.append({
                        "id": item["id"],
                        "title": item.get("title"),
                        "days_overdue": (today - due_date).days,
                        "priority": item.get("priority", "medium")
                    })
            except ValueError:
                pass
    return sorted(overdue, key=lambda x: x["days_overdue"], reverse=True)
