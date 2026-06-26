# === Stage 24: Add grouped summaries by category or status ===
# Project: GoalTrail
def generate_grouped_summary(goals, status_map=None):
    if status_map is None:
        status_map = {g['status']: g.get('category', 'General') for g in goals}
    groups = {}
    for goal in goals:
        cat = status_map.get(goal['status'], 'Uncategorized')
        groups.setdefault(cat, []).append(goal)
    summary_lines = []
    for category, items in sorted(groups.items()):
        completed = sum(1 for g in items if g['status'] == 'completed')
        pending = len(items) - completed
        progress_pct = round(completed / max(len(items), 1) * 100, 0)
        summary_lines.append(f"[{category}] ({progress_pct}%): {len(items)} goals — {completed} done, {pending} pending")
    return "\n".join(summary_lines)
