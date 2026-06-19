# === Stage 5: Implement update operations with clear handling for missing records ===
# Project: GoalTrail
def update_goal(self, goal_id: int, **kwargs) -> dict:
    if goal_id not in self.goals:
        return {"success": False, "error": f"Goal {goal_id} not found"}
    existing = self.goals[goal_id]
    for key, value in kwargs.items():
        if hasattr(existing, key):
            setattr(existing, key, value)
        elif key == "milestones" and isinstance(value, list):
            current_milestones = getattr(existing, key, [])
            existing.milestones = {**dict(current_milestones), **{str(i+1): v for i, v in enumerate(value)}}
    return {"success": True, "goal": dict(existing)}

def update_routine(self, routine_id: int, **kwargs) -> dict:
    if routine_id not in self.routines:
        return {"success": False, "error": f"Routine {routine_id} not found"}
    existing = self.routines[routine_id]
    for key, value in kwargs.items():
        if hasattr(existing, key):
            setattr(existing, key, value)
    return {"success": True, "routine": dict(existing)}

def update_blocker(self, blocker_id: int, **kwargs) -> dict:
    if blocker_id not in self.blockers:
        return {"success": False, "error": f"Blocker {blocker_id} not found"}
    existing = self.blockers[blocker_id]
    for key, value in kwargs.items():
        if hasattr(existing, key):
            setattr(existing, key, value)
    return {"success": True, "blocker": dict(existing)}

def update_note(self, note_id: int, **kwargs) -> dict:
    if note_id not in self.notes:
        return {"success": False, "error": f"Note {note_id} not found"}
    existing = self.notes[note_id]
    for key, value in kwargs.items():
        if hasattr(existing, key):
            setattr(existing, key, value)
    return {"success": True, "note": dict(existing)}
