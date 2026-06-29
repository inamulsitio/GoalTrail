# === Stage 36: Add templates for quickly creating common records ===
# Project: GoalTrail
from datetime import date, timedelta
import random

TEMPLATES = {
    "daily_routine": lambda: {"type": "routine", "name": f"Routine-{date.today().strftime('%Y-%m-%d')}", "description": "Daily habits checklist.", "items": ["Exercise", "Reading", "Planning"]},
    "weekly_goal": lambda: {"type": "milestone", "name": f"Weekly Goal-{random.randint(1, 52)}", "target_date": date.today() + timedelta(days=7), "description": "Main objective for this week.", "status": "pending"},
    "blocker_report": lambda: {"type": "note", "category": "blocker", "content": f"Blocked by: {random.choice(['Lack of time', 'Technical debt', 'External factors'])}", "severity": random.choice(["low", "medium", "high"])},
    "progress_update": lambda: {"type": "report", "milestone_id": None, "completion_percent": random.randint(10, 95), "notes": f"Progress update for {date.today()}.", "sentiment": random.choice(["positive", "neutral", "negative"])},
}

def get_template(name: str) -> dict | None:
    """Retrieve a predefined template by name."""
    return TEMPLATES.get(name.lower())
