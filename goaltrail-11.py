# === Stage 11: Add JSON export for the current application state ===
# Project: GoalTrail
def export_state(json_path: str) -> None:
    import json
    from pathlib import Path
    
    state = {
        "goals": list(goals.values()),
        "routines": list(routines.values()),
        "blockers": list(blockers.keys()) if blockers else [],
        "notes": notes,
        "last_updated": datetime.now().isoformat()
    }
    
    Path(json_path).write_text(
        json.dumps(state, indent=2, ensure_ascii=False),
        encoding="utf-8"
    )

# === Stage 11: Add JSON export for the current application state ===
# Project: GoalTrail
def export_state_to_json(data, filename="goaltrail_export.json"):
    import json
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    print(f"State exported to {filename}")
