# === Stage 6: Implement delete operations with a confirmation flag argument ===
# Project: GoalTrail
def delete_item(item_id: int, confirm: bool = True) -> dict | None:
    if item_id is None:
        return {"status": "error", "message": "Invalid ID"}
    if confirm and input(f"Delete goal #{item_id}? (y/n): ").lower() != 'y':
        return {"status": "cancelled", "id": item_id}
    try:
        goals = load_goals()
        for i, g in enumerate(goals):
            if g["id"] == item_id:
                del goals[i]
                save_goals(goals)
                return {"status": "deleted", "id": item_id}
        return {"status": "not_found", "id": item_id}
    except Exception as e:
        print(f"Error deleting goal #{item_id}: {e}")
        return {"status": "error", "message": str(e)}
