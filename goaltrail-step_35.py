# === Stage 35: Add active user switching and user-specific records ===
# Project: GoalTrail
from typing import Optional, Dict, List
import json
from pathlib import Path

class UserContext:
    def __init__(self, user_id: str):
        self.user_id = user_id
        self._data_dir = Path.home() / ".goaltrail" / user_id
        self._data_dir.mkdir(parents=True, exist_ok=True)
    
    def _load(self) -> Dict:
        path = self._data_dir / "records.json"
        if not path.exists():
            return {"goals": [], "routines": []}
        with open(path) as f:
            data = json.load(f)
        return {k: v for k, v in data.items() if isinstance(v, list)}
    
    def _save(self, records: Dict):
        path = self._data_dir / "records.json"
        with open(path, 'w') as f:
            json.dump(records, f)

class GoalTrackerMultiUser:
    @staticmethod
    def get_active_user() -> Optional[str]:
        active_file = Path.home() / ".goaltrail" / "active_user.txt"
        if not active_file.exists():
            return None
        with open(active_file) as f:
            return f.read().strip()
    
    @staticmethod
    def set_active_user(user_id: str):
        path = Path.home() / ".goaltrail" / "active_user.txt"
        path.parent.mkdir(parents=True, exist_ok=True)
        with open(path, 'w') as f:
            f.write(user_id)
    
    @staticmethod
    def get_records_for_user(user_id: str) -> Dict:
        ctx = UserContext(user_id)
        return ctx._load()
    
    @staticmethod
    def add_goal(user_id: str, title: str, milestones: List[str]):
        ctx = UserContext(user_id)
        records = ctx._load()
        goal_data = {"title": title, "milestones": milestones, "status": "active"}
        records["goals"].append(goal_data)
        ctx._save(records)
    
    @staticmethod
    def add_routine(user_id: str, name: str, schedule: str):
        ctx = UserContext(user_id)
        records = ctx._load()
        routine_data = {"name": name, "schedule": schedule}
        records["routines"].append(routine_data)
        ctx._save(records)

if __name__ == "__main__":
    uid = GoalTrackerMultiUser.get_active_user() or "guest"
    print(f"Current user: {uid}")
    GoalTrackerMultiUser.add_goal(uid, "Learn Python", ["Finish basics", "Build app"])
    GoalTrackerMultiUser.add_routine(uid, "Daily Code", "30 mins")
