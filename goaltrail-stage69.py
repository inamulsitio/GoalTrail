# === Stage 69: Add a reset-demo-data command for manual testing ===
# Project: GoalTrail
import json, random, os


def reset_demo_data(db_path: str = "goals.json"):
    """Reset GoalTrail database to a clean demo state for testing."""
    if os.path.exists(db_path):
        os.remove(db_path)
    goals = [
        {"id": 1, "title": "Learn Python", "status": "active", "progress_pct": 75},
        {"id": 2, "title": "Build GoalTrail", "status": "in_progress", "progress_pct": 60},
    ]
    milestones = [
        {"goal_id": 1, "description": "Complete Python basics", "done": True},
        {"goal_id": 2, "description": "Design data model", "done": False},
    ]
    routines = [
        {"name": "Daily coding", "frequency": "daily", "completed_today": True},
    ]
    blockers = []
    notes = [
        {"content": "Start with clear goals.", "created": 1700000000},
    ]
    reports = []

    demo_db = {
        "goals": goals,
        "milestones": milestones,
        "routines": routines,
        "blockers": blockers,
        "notes": notes,
        "reports": reports,
    }
    with open(db_path, "w") as f:
        json.dump(demo_db, f, indent=2)

    print(f"Demo data reset. Stored in {db_path}")


if __name__ == "__main__":
    reset_demo_data()
