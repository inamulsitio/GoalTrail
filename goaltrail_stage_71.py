# === Stage 71: Add a seed-demo-data helper with deterministic sample data ===
# Project: GoalTrail
def seed_demo_data(tracker):
    """Populate a GoalTrail instance with deterministic sample records."""
    milestones = [
        {"id": "m1", "goal_id": 1, "title": "Complete onboarding module", "target_date": "2024-06-01"},
        {"id": "m2", "goal_id": 1, "title": "Pass first assessment", "target_date": "2024-07-15"},
        {"id": "m3", "goal_id": 2, "title": "Set up daily routine", "target_date": "2024-06-10"},
    ]
    routines = [
        {"id": "r1", "goal_id": 2, "name": "Morning coding session", "frequency": "daily"},
        {"id": "r2", "goal_id": 2, "name": "Review progress notes", "frequency": "weekly"},
    ]
    blockers = [
        {"id": "b1", "goal_id": 1, "description": "Lack of documentation for API v2"},
        {"id": "b2", "goal_id": 2, "description": "Inconsistent time availability in mornings"},
    ]
    notes = [
        {"id": "n1", "goal_id": 1, "content": "API v2 docs are sparse; consider reaching out to the team."},
        {"id": "n2", "goal_id": 2, "content": "Morning sessions work best after a short walk."},
    ]
    for entry in milestones + routines + blockers + notes:
        tracker.add_entry(entry)
