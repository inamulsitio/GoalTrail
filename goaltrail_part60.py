# === Stage 60: Add saved views for frequently used filters ===
# Project: GoalTrail
import json


def save_view(view_config, view_name):
    views_file = "view_history.json"
    if not os.path.exists(views_file):
        with open(views_file, 'w') as f:
            json.dump({}, f)
    with open(views_file, 'r') as f:
        saved_views = json.load(f)
    saved_views[view_name] = view_config
    with open(views_file, 'w') as f:
        json.dump(saved_views, f, indent=4)


def load_saved_views():
    views_file = "view_history.json"
    if not os.path.exists(views_file):
        return {}
    with open(views_file, 'r') as f:
        saved_views = json.load(f)
    return saved_views


def apply_view(view_config, goals_data, routines_data, blockers_data, notes_data):
    filtered_goals = goals_data.copy()
    if view_config.get("filter_status"):
        filtered_goals = [g for g in filtered_goals if g["status"] == view_config["filter_status"]]
    if view_config.get("sort_by") and "values" in view_config:
        sort_key = view_config["sort_by"]
        reverse = view_config["values"].get(sort_key, False)
        filtered_goals.sort(key=lambda x: x[sort_key], reverse=reverse)
    return filtered_goals


def display_saved_views():
    saved_views = load_saved_views()
    print("\nSaved Views:")
    for name, config in saved_views.items():
        print(f"  - {name}: {config}")
