# === Stage 66: Add export of a short status dashboard ===
# Project: GoalTrail
def status_dashboard(goals):
    """Return a compact text dashboard for all goals."""
    if not goals:
        return "GoalTrail Status Dashboard\nNo goals yet.\n"
    lines = ["GoalTrail Status Dashboard", "=" * 40]
    total, active, done = 0, 0, 0
    for g in goals:
        total += 1
        if g["done"]:
            done += 1
            status = "✓ DONE"
        elif any(m["done"] for m in g.get("milestones", [])):
            status = "~ IN PROGRESS (some milestones)"
        else:
            active += 1
            status = "○ ACTIVE"
        lines.append(f"[{g['name']}] {status} | progress: {g.get('progress', 'N/A')}")
    lines.append("-" * 40)
    lines.append(f"Total goals: {total}")
    lines.append(f"Active: {active}, Done: {done}")
    return "\n".join(lines)

print(status_dashboard([
    {"name": "Learn Python", "progress": "75%", "done": False, "milestones": [{"desc": "Basics", "done": True}, {"desc": "OOP", "done": False}]},
    {"name": "Build Todo App", "progress": "30%", "done": False, "milestones": []},
    {"name": "Read 12 books", "progress": "4 of 12", "done": True, "milestones": []}
]))
