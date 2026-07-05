# === Stage 53: Add command help text and usage examples ===
# Project: GoalTrail
def print_help():
    """Display usage instructions and examples for GoalTrail CLI."""
    help_text = (
        "GoalTracker: A simple goal tracking tool.\n"
        "Usage:\n"
        "  python main.py <command> [options]\n\n"
        "Commands:\n"
        "  add-goal      Add a new goal with optional description and deadline.\n"
        "  list-goals    Display all active goals with their current status.\n"
        "  complete-goal Mark a specific goal as completed by ID or name.\n"
        "  add-milestone Add a milestone to an existing goal (requires goal ID).\n"
        "  log-routine   Record completion of a daily routine task.\n"
        "  add-blocker   Log a blocker preventing progress on a specific goal.\n"
        "  view-notes    Show all notes associated with goals or routines.\n"
        "  report        Generate a text summary of overall progress and stats.\n\n"
        "Examples:\n"
        "  python main.py add-goal --desc 'Learn Python' --deadline '2025-12-31'\n"
        "  python main.py list-goals\n"
        "  python main.py complete-goal --id 1\n"
        "  python main.py log-routine --task 'Morning stretch' --date today\n"
        "  python main.py report\n"
    )
    print(help_text)
