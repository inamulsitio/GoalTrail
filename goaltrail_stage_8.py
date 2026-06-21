# === Stage 8: Add filtering by status, category, owner, or tag ===
# Project: GoalTrail
def filter_items(items, status=None, category=None, owner=None, tag=None):
    if status: items = [i for i in items if i.get('status') == status]
    if category: items = [i for i in items if i.get('category') == category]
    if owner: items = [i for i in items if i.get('owner') == owner]
    if tag: items = [i for i in items if any(i.get(t) == tag for t in ['tags'])]
    return items

def generate_progress_report(items, status=None):
    filtered = filter_items(items, status=status)
    total = len(filtered)
    completed = sum(1 for i in filtered if i.get('status') == 'done')
    progress_pct = (completed / total * 100) if total else 0
    return f"Progress: {completed}/{total} items ({progress_pct:.1f}%)"
