# === Stage 67: Add a function that returns key project metrics ===
# Project: GoalTrail
def project_metrics(goals, milestones, routines, notes):
    """Return key metrics for the GoalTrail project."""
    active = sum(1 for g in goals if g.get("status") == "active")
    completed = sum(1 for g in goals if g.get("status") == "completed")
    total_milestones = len(milestones)
    milestone_done = sum(1 for m in milestones if m.get("done"))
    milestone_pct = (milestone_done / total_milestones * 100) if total_milestones else 0

    routine_count = len(routines)
    routine_active = sum(1 for r in routines if not r.get("paused", False))

    note_count = len(notes)

    return {
        "active_goals": active,
        "completed_goals": completed,
        "total_milestones": total_milestones,
        "milestones_completed": milestone_done,
        "milestone_percentage": round(milestone_pct, 1),
        "routines_total": routine_count,
        "routines_active": routine_active,
        "notes_total": note_count,
    }
