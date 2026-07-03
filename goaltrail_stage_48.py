# === Stage 48: Add small unit tests for creation and validation helpers ===
# Project: GoalTrail
from typing import Optional, List
import re

def validate_email(email: str) -> bool:
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return bool(re.match(pattern, email))

def parse_date(date_str: Optional[str]) -> Optional[int]:
    if not date_str:
        return None
    try:
        from datetime import datetime
        dt = datetime.strptime(date_str, "%Y-%m-%d")
        return int(dt.timestamp())
    except ValueError:
        return None

def create_milestone(title: str, target_date: Optional[str], status: str = "pending") -> dict:
    if not title or len(title.strip()) < 2:
        raise ValueError("Milestone title must be at least 2 characters.")
    if status not in ["pending", "in_progress", "completed"]:
        raise ValueError("Status must be one of: pending, in_progress, completed.")
    
    timestamp = parse_date(target_date)
    return {
        "id": hash(title),
        "title": title.strip(),
        "target_date": target_date,
        "timestamp": timestamp,
        "status": status
    }

def validate_goal(goal: dict) -> bool:
    required_keys = ["name", "description"]
    if not all(key in goal for key in required_keys):
        return False
    if len(goal["name"].strip()) < 3 or len(goal["description"]) < 10:
        return False
    return True

def calculate_progress(milestones: List[dict]) -> float:
    if not milestones:
        return 0.0
    completed = sum(1 for m in milestones if m.get("status") == "completed")
    total = len(milestones)
    return round((completed / total) * 100, 2)
