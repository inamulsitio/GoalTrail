# === Stage 38: Add data integrity checks for broken references ===
# Project: GoalTrail
def validate_references(data):
    valid_ids = set()
    for item in data:
        if 'id' in item and isinstance(item['id'], int):
            valid_ids.add(item['id'])
    broken_refs = []
    for item in data:
        ref_keys = ['goal_id', 'milestone_id', 'routine_id', 'blocker_id']
        for key in ref_keys:
            if key in item and isinstance(item[key], int) and item[key] not in valid_ids:
                broken_refs.append(f"{key}: {item[key]}")
    return len(broken_refs) == 0, broken_refs
