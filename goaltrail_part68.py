# === Stage 68: Add a compact changelog generated from the activity log ===
# Project: GoalTrail
def generate_changelog(activity_log, max_entries=10):
    """Generate a compact changelog from an activity log."""
    if not activity_log:
        return "No entries yet.\n"
    
    lines = []
    for entry in activity_log[-max_entries:]:
        date = entry.get("date", "Unknown")
        message = entry.get("message", "")
        lines.append(f"{date} - {message}")
    
    return "\n".join(lines)

if __name__ == "__main__":
    sample_log = [
        {"date": "2024-01-01", "message": "Initial project setup"},
        {"date": "2024-01-15", "message": "Added goal tracking features"},
        {"date": "2024-02-01", "message": "Implemented milestone system"},
        {"date": "2024-03-10", "message": "Created progress reports module"},
        {"date": "2024-04-20", "message": "Integrated routine tracking"},
    ]
    
    changelog = generate_changelog(sample_log)
    print(changelog)
