# === Stage 75: Add a validation report that lists warnings and errors ===
# Project: GoalTrail
def validate_goals(tracker):
    warnings = []
    errors = []
    for goal in tracker.get("goals", []):
        if "title" not in goal:
            errors.append(f"Goal missing 'title': {goal}")
        elif len(goal["title"]) > 100:
            warnings.append(f"Goal title too long ({len(goal['title'])} chars): {goal['title'][:50]}...")
        if "milestones" not in goal:
            errors.append(f"Goal '{goal.get('id', 'unknown')}' has no milestones")
        else:
            ms = goal["milestones"]
            for i, m in enumerate(ms):
                if "target_date" not in m:
                    warnings.append(f"Milestone {i+1} of goal '{goal['title']}' missing target_date")
        if "routines" not in goal:
            errors.append(f"Goal '{goal.get('id', 'unknown')}' has no routines")
    return warnings, errors
