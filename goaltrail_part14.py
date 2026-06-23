# === Stage 14: Add file load support with fallback demo data ===
# Project: GoalTrail
def load_data(path=None):
    if path and os.path.exists(path):
        try:
            with open(path, 'r', encoding='utf-8') as f:
                return json.load(f)
        except (json.JSONDecodeError, IOError):
            pass
    return {
        "goals": [
            {"id": 1, "title": "Learn Python", "milestones": ["Install IDE", "Write Hello World"], "status": "completed"},
            {"id": 2, "title": "Build App", "milestones": ["Design DB", "Implement API"], "status": "in_progress"}
        ],
        "routines": [{"name": "Morning Code", "time": "09:00", "active": True}],
        "blockers": [],
        "notes": []
    }
