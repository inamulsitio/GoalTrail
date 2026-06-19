# === Stage 4: Implement create operations for the primary records ===
# Project: GoalTrail
class GoalTrailDB:
    def __init__(self):
        self._goals = {}
        self._milestones = []
        self._routines = []
        self._blockers = []
        self._notes = []

    def create_goal(self, title, description=""):
        goal_id = len(self._goals) + 1
        self._goals[goal_id] = {"id": goal_id, "title": title, "description": description}
        return goal_id

    def add_milestone(self, goal_id, title, date=None):
        milestone_id = len(self._milestones) + 1
        entry = {"id": milestone_id, "goal_id": goal_id, "title": title, "date": date or None}
        self._milestones.append(entry)
        return milestone_id

    def add_routine(self, name, frequency="daily", duration_minutes=0):
        routine_id = len(self._routines) + 1
        entry = {"id": routine_id, "name": name, "frequency": frequency, "duration_minutes": duration_minutes}
        self._routines.append(entry)
        return routine_id

    def add_blocker(self, title, severity="medium", resolved=False):
        blocker_id = len(self._blockers) + 1
        entry = {"id": blocker_id, "title": title, "severity": severity, "resolved": resolved}
        self._blockers.append(entry)
        return blocker_id

    def add_note(self, content, goal_id=None):
        note_id = len(self._notes) + 1
        entry = {"id": note_id, "content": content, "goal_id": goal_id}
        self._notes.append(entry)
        return note_id
