# === Stage 27: Add monthly summary calculations ===
# Project: GoalTrail
def calculate_monthly_summary(data, target_date):
    from datetime import timedelta
    start = (target_date - timedelta(days=1)).replace(day=1)
    end = target_date.replace(day=end.day if hasattr(end, 'day') else 30) + timedelta(days=28)
    month_data = [d for d in data if start <= d['date'] <= end]
    total_milestones = sum(1 for m in month_data if m.get('completed', False))
    routines_completed = sum(r.get('count', 0) for r in month_data if r.get('routine_id'))
    blockers_resolved = sum(b.get('resolved', False) for b in month_data if b.get('blocker_id'))
    notes_count = len([n for n in month_data if n.get('note')])
    progress_pct = min(100, (total_milestones / max(len(month_data), 1)) * 100)
    return {
        'month': target_date.strftime('%Y-%m'),
        'milestones_completed': total_milestones,
        'routines_executed': routines_completed,
        'blockers_resolved': blockers_resolved,
        'notes_added': notes_count,
        'overall_progress_percent': round(progress_pct, 1)
    }
