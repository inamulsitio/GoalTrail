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
