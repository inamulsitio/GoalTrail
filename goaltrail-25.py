# === Stage 25: Add daily summary calculations ===
# Project: GoalTrail
def calculate_daily_summary(goal_data, current_date):
    today = datetime.date.today()
    if goal_data.get('last_sync') != str(today):
        total_milestones = sum(1 for g in goal_data['goals'] for m in g.get('milestones', []) if m.get('completed'))
        active_routines = len([r for r in goal_data['routines'] if not r.get('paused')])
        blockers_count = len(goal_data['blockers'])
        notes_summary = ' '.join(note[:50] + '...' if len(note) > 50 else note 
                                for g in goal_data['goals'] for note in g.get('notes', [])).strip()
        progress_pct = (total_milestones / sum(len(g.get('milestones', [])) for g in goal_data['goals'])) * 100 if any(goal_data['goals']) else 0.0
        summary = {
            'date': str(today),
            'completed_milestones': total_milestones,
            'active_routines': active_routines,
            'blockers_count': blockers_count,
            'overall_progress_pct': round(progress_pct, 1),
            'notes_preview': notes_summary[:200] + '...' if len(notes_summary) > 200 else notes_summary,
            'timestamp': datetime.datetime.now().isoformat()
        }
        goal_data['last_sync'] = str(today)
        return summary
