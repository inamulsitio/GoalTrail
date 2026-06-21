# === Stage 7: Add list and detail formatting helpers for console output ===
# Project: GoalTrail
def format_goal(g):
    return f"[{g['status']}] {g['title']} (Milestones: {len(g.get('milestones', []))})"

def format_milestone(m, indent="  "):
    return f"{indent}- [{m['done']}✓] {m['description']} ({m['target_date']})"

def format_routine(r):
    days = ", ".join([d.capitalize() for d in r.get('days', [])])
    return f"[{r['active']}] Routine: {r['name']} | Days: {days}"

def format_blocker(b):
    return f"[!] Blocker: {b['description']} (Impact: {b['impact']})"

def format_note(n, indent="  "):
    lines = n.get('content', '').split('\n')
    return "\n".join([f"{indent}{line}" for line in lines])

def print_goal_detail(g):
    print(f"\n=== {format_goal(g)} ===")
    if g.get('milestones'):
        print("Milestones:")
        for m in g['milestones']:
            print(format_milestone(m))
    if g.get('routines'):
        print("\nRoutines:")
        for r in g['routines']:
            print(format_routine(r))
    if g.get('blockers'):
        print("Blockers:")
        for b in g['blockers']:
            print(format_blocker(b))
    if g.get('notes'):
        print("\nNotes:")
        print(format_note(g['notes']))

def format_progress_report(goals):
    total = len(goals)
    completed = sum(1 for g in goals if g.get('status') == 'completed')
    pct = (completed / total * 100) if total else 0
    return f"Progress: {completed}/{total} goals ({pct:.1f}%)"
