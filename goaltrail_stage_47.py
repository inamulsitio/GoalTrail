# === Stage 47: Add a demo scenario that exercises the main workflow ===
# Project: GoalTrail
def run_demo():
    from datetime import date, timedelta
    goal = {"id": 1, "title": "Learn Python", "status": "active"}
    milestones = [
        {"date": (date.today() - timedelta(days=30)).isoformat(), "done": True},
        {"date": (date.today() - timedelta(days=7)).isoformat(), "done": False}
    ]
    routines = [{"name": "Daily Practice", "frequency": "daily"}]
    blockers = []
    notes = ["Started yesterday."]
    print(f"Goal: {goal['title']}")
    print("Milestones:")
    for m in milestones:
        status = "✓" if m["done"] else "○"
        print(f"  {status} {m['date'][:10]}")
    print("Routines:", routines[0]["name"])
    print("Blockers:", blockers)
    print("Notes:", notes)
