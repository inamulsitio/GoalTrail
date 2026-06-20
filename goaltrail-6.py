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

# === Stage 6: Implement delete operations with a confirmation flag argument ===
# Project: GoalTrail
def delete_goal(goal_id, confirm=False):
    if goal_id in goals:
        entry = goals[goal_id]
        if confirm or input(f"Удалить цель '{entry['title']}'? (y/n) ") == 'y':
            del goals[goal_id]
            print("Цель удалена.")
            return True
    print("Не удалось удалить цель или подтверждение не получено.")
    return False

def delete_milestone(goal_id, milestone_index):
    if goal_id in goals:
        entry = goals[goal_id]
        milestones = entry.get('milestones', [])
        if 0 <= milestone_index < len(milestones):
            del milestones[milestone_index]
            print("Майлстоун удален.")
            return True
    print("Не удалось удалить майлстоун или индекс неверный.")
    return False

def delete_routine(goal_id, routine_name):
    if goal_id in goals:
        entry = goals[goal_id]
        routines = entry.get('routines', [])
        for i, r in enumerate(routines):
            if r['name'] == routine_name:
                del routines[i]
                print("Рутина удалена.")
                return True
    print("Не удалось удалить рутину или она не найдена.")
    return False

def delete_blocker(goal_id, blocker_text):
    if goal_id in goals:
        entry = goals[goal_id]
        blockers = entry.get('blockers', [])
        for i, b in enumerate(blockers):
            if b['text'] == blocker_text:
                del blockers[i]
                print("Блокер удален.")
                return True
    print("Не удалось удалить блокер или он не найден.")
    return False

def delete_note(goal_id, note_text):
    if goal_id in goals:
        entry = goals[goal_id]
        notes = entry.get('notes', [])
        for i, n in enumerate(notes):
            if n['text'] == note_text:
                del notes[i]
                print("Заметка удалена.")
                return True
    print("Не удалось удалить заметку или она не найдена.")
    return False
