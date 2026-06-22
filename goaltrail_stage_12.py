# === Stage 12: Add JSON import with friendly error handling for malformed data ===
# Project: GoalTrail
import json, os

def load_goals(path):
    if not os.path.exists(path): return []
    try:
        with open(path) as f: data = json.load(f); return [dict(g) for g in data.get("goals", [])]
    except json.JSONDecodeError as e:
        print(f"Warning: Malformed JSON at {path}: {e}")
        return []
