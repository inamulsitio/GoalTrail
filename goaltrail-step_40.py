# === Stage 40: Add plain text report export ===
# Project: GoalTrail
def export_report_to_text(tracker, filename="report.txt"):
    with open(filename, "w", encoding="utf-8") as f:
        for goal in tracker["goals"]:
            f.write(f"Goal: {goal['name']}\n")
            f.write(f"Milestones: {' | '.join(goal.get('milestones', [])) or 'None'}\n")
            f.write(f"Routines: {' | '.join(goal.get('routines', [])) or 'None'}\n")
            f.write(f"Blockers: {' | '.join(goal.get('blockers', [])) or 'None'}\n")
            f.write(f"Notes: {goal.get('notes', '')}\n\n")
