# === Stage 74: Add a snapshot comparison helper for before/after states ===
# Project: GoalTrail
def snapshot_compare(before, after):
    """Compare two state snapshots and return a human-readable diff."""
    if before is None:
        return {"status": "new", "changes": list(after.items())}
    if after is None:
        return {"status": "deleted", "removed": list(before.items())}
    changes = []
    for key in set(list(before.keys()) + list(after.keys())):
        old, new = before.get(key), after.get(key)
        if old != new:
            status = "added" if new is not None else "removed"
            changes.append({"key": key, "status": status, "before": old, "after": new})
    return {"status": "changed", "changes": changes}
