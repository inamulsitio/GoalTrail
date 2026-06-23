# === Stage 13: Add file save support using a configurable path ===
# Project: GoalTrail
import os, json, sys
from pathlib import Path

def get_data_path():
    base = Path.home() / ".goaltrail"
    if not base.exists():
        base.mkdir(parents=True)
    return base / "data.json"

def save_state(state):
    path = get_data_path()
    try:
        with open(path, 'w', encoding='utf-8') as f:
            json.dump(state, f, indent=2, ensure_ascii=False)
        print(f"[OK] Saved to {path}")
    except Exception as e:
        print(f"[ERR] Save failed: {e}", file=sys.stderr)

def load_state():
    path = get_data_path()
    if not path.exists():
        return {"goals": [], "settings": {"save_dir": str(path.parent)}}
    try:
        with open(path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        if "version" in data and data["version"] != 1:
            print("[WARN] Unsupported data version", file=sys.stderr)
            return {"goals": [], "settings": {}}
        return data
    except Exception:
        return {"goals": [], "settings": {}}

if __name__ == "__main__":
    # Demo save/load cycle
    state = load_state()
    state["goals"].append({"id": 1, "title": "Demo Goal", "status": "active"})
    state["settings"]["save_dir"] = str(get_data_path().parent)
    save_state(state)
