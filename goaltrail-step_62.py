# === Stage 62: Add simple scoring or priority recommendation logic ===
# Project: GoalTrail
import math

def compute_goal_priority(goal):
    priority_score = 0

    if goal.get("status") == "active":
        priority_score += 10
    elif goal.get("status") == "completed":
        return ("done", 5)

    blockers = goal.get("blockers", [])
    milestones = goal.get("milestones", {})
    notes = goal.get("notes", "")

    if not blocks:
        priority_score -= 10 * len(blockers)

    milestones_completed = sum(1 for m in milestones.values() if m.get("status") == "completed")
    total_milestones = len(milestones)
    milestone_progress = (milestones_completed / total_milestones * 20) if total_milestones else 0
    priority_score += milestone_progress

    routine_count = goal.get("routine_count", 0)
    target_routine = goal.get("target_routines", 10)
    routine_progress = (routine_count / target_routine * 15) if target_routine else 0
    priority_score += routine_progress

    urgency_keywords = ["urgent", "critical", "deadline"]
    for keyword in urgency_keywords:
        if keyword.lower() in notes.lower():
            priority_score += 8
            break

    return ("active", max(1, min(priority_score, 20)))
