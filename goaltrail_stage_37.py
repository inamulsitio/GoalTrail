# === Stage 37: Add recommendations for the next useful action ===
# Project: GoalTrail
def generate_next_action(goal, current_state):
    """Generates a single recommended next action based on goal status and blockers."""
    if not goal.get('active'):
        return "Review completed goals and archive them."
    
    active_blockers = [b for b in goal.get('blockers', []) if b.get('status') == 'open']
    if active_blockers:
        blocker_text = ", ".join([f"{b['title']} ({b['priority']})" for b in active_blockers])
        return f"Resolve blockers: {blocker_text}"

    milestones = goal.get('milestones', [])
    routines = goal.get('routines', [])
    
    if current_state.get('today_routine_completed'):
        next_milestone_index = None
        for i, m in enumerate(milestones):
            if not m.get('completed') and (m.get('due_date') is None or m['due_date'] >= '2025-12-31'):
                next_milestone_index = i
                break
        
        if next_milestone_index is not None:
            return f"Work on milestone {next_milestone_index + 1}: {milestones[next_milestone_index]['title']}"

    if routines and current_state.get('today_routine_completed') == False:
        routine_text = ", ".join([r['name'] for r in routines])
        return f"Complete daily routines: {routine_text}"

    notes = goal.get('notes', [])
    recent_note_date = max((n.get('date') for n in notes if n.get('date')), default=None)
    
    if not recent_note_date or (recent_note_date < '2025-12-31'):
        return "Review progress and update status."

    return "Maintain current momentum."
