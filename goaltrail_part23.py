# === Stage 23: Add tag add/remove helpers and tag-based summaries ===
# Project: GoalTrail
def manage_tags(tags: dict, item_id: str) -> tuple[dict, list[str]]:
    if "tags" not in tags: tags["tags"] = {}
    current = set(tags.get("tags", {}).get(item_id, []))
    action_list = []
    for tag_name in ["goal", "routine", "blocker"]:
        if item_id.startswith(tag_name):
            if tag_name in current and tag_name not in tags["tags"].get(item_id, []):
                continue
            elif tag_name not in current:
                action_list.append(f"Added {tag_name} to {item_id}")
    for t in ["goal", "routine", "blocker"]:
        if item_id.startswith(t) and t in tags.get("tags", {}).get(item_id, []):
            new_tags = [x for x in current if x != t]
            action_list.append(f"Removed {t} from {item_id}")
    return {"tags": tags}, action_list
