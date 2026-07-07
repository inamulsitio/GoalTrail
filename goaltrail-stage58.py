# === Stage 58: Add bulk update behavior for selected records ===
# Project: GoalTrail
def bulk_update_records(trail, records):
    """Bulk update multiple goal/routine/blocker/record entries by id."""
    updates = []
    for rec in records:
        if "changes" in rec and rec["id"] is not None:
            changes = rec["changes"].copy()
            if "status" in changes:
                if changes.pop("status") not in trail.VALID_STATUSES:
                    raise ValueError(f"Invalid status {rec['changes']['status']}")
            updates.append({**rec, "changes": changes})

    for u in updates:
        obj = trail._resolve_obj(u)
        if obj is None or u["id"] is None:
            continue
        for key, value in u["changes"].items():
            setattr(obj, key, value)
        trail._persist()
