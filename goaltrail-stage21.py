# === Stage 21: Add archive and restore behavior for completed or old records ===
# Project: GoalTrail
from datetime import datetime, timedelta
import json
import os

ARCHIVE_DIR = "archive"
RETENTION_DAYS = 365

def archive_old_records(data):
    if not data: return data
    cutoff_date = (datetime.now() - timedelta(days=RETENTION_DAYS)).date()
    archived = []
    remaining = {}
    for goal_id, record in data.items():
        last_updated = datetime.strptime(record.get("last_updated", ""), "%Y-%m-%d").date()
        if last_updated < cutoff_date:
            os.makedirs(ARCHIVE_DIR, exist_ok=True)
            filename = f"{goal_id}_{record['created_at']}.json"
            with open(os.path.join(ARCHIVE_DIR, filename), "w", encoding="utf-8") as f:
                json.dump(record, f, ensure_ascii=False, indent=2)
            archived.append(goal_id)
        else:
            remaining[goal_id] = record
    return remaining

def restore_from_archive(data):
    if not os.path.exists(ARCHIVE_DIR): return data
    restored_data = dict(data)
    for filename in os.listdir(ARCHIVE_DIR):
        filepath = os.path.join(ARCHIVE_DIR, filename)
        try:
            with open(filepath, "r", encoding="utf-8") as f:
                record = json.load(f)
                goal_id = record.get("goal_id") or filename.split("_")[0]
                restored_data[goal_id] = record
        except (json.JSONDecodeError, KeyError):
            continue
    return restored_data
