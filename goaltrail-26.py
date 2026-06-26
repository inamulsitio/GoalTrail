# === Stage 26: Add weekly summary calculations ===
# Project: GoalTrail
def calculate_weekly_summary(github_data):
    from datetime import date, timedelta
    today = date.today()
    week_start = today - timedelta(days=today.weekday())  # Monday of current week
    week_end = week_start + timedelta(days=6)
    
    weekly_stats = {
        "week_range": f"{week_start} to {week_end}",
        "total_goals_updated": sum(1 for g in github_data if date.fromtimestamp(g['updated_at']) >= week_start),
        "new_milestones_reached": 0,
        "active_routines_count": 0,
        "resolved_blockers_count": 0,
        "notes_added": 0
    }

    for repo in github_data:
        if 'goals' not in repo or not repo['goals']:
            continue
        
        # Check milestones reached this week (assuming status change to 'completed')
        for goal in repo['goals']:
            if date.fromtimestamp(goal.get('updated_at', 0)) >= week_start and goal.get('status') == 'completed':
                weekly_stats["new_milestones_reached"] += 1
        
        # Count active routines (assuming status 'active' or similar)
        for routine in repo.get('routines', []):
            if date.fromtimestamp(routine.get('updated_at', 0)) >= week_start:
                weekly_stats["active_routines_count"] += 1
        
        # Count resolved blockers this week
        for blocker in repo.get('blockers', []):
            if date.fromtimestamp(blocker.get('resolved_at')) and \
               date.fromtimestamp(blocker['resolved_at']) >= week_start:
                weekly_stats["resolved_blockers_count"] += 1
        
        # Count new notes (assuming a 'created_at' field)
        for note in repo.get('notes', []):
            if date.fromtimestamp(note.get('created_at', 0)) >= week_start:
                weekly_stats["notes_added"] += 1
    
    return weekly_stats
