# === Stage 70: Add a clear-state command protected by a confirmation flag ===
# Project: GoalTrail
CONFIRM = True


def clear_state(goal: Goal) -> None:
    """Reset a goal to its untouched initial state."""
    if not CONFIRM:
        raise PermissionError("clear_state requires CONFIRM=True")
    goal.status = "pending"
    goal.progress = 0
    goal.milestones.clear()
    goal.routines.clear()
    goal.blockers.clear()
    goal.notes.clear()
