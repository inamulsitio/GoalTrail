# === Stage 52: Add clearer docstrings for public helper functions ===
# Project: GoalTrail
def _format_date(date_obj): return date_obj.strftime("%Y-%m-%d") if date_obj else "N/A"
def _calculate_progress(current, target): return round((current / max(target, 1)) * 100, 2)
def _generate_summary(goal_name, current_milestones, total_routines, active_blockers):
    status = "On Track" if active_blockers == 0 else "At Risk"
    progress_pct = _calculate_progress(current_milestones, goal_name.get("total", 1))
    return f"{goal_name['name']}: {status} | Progress: {progress_pct}% | Routines: {total_routines} | Blockers: {active_blockers}"
