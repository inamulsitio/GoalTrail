# === Stage 18: Add an activity log with timestamps and action names ===
# Project: GoalTrail
class ActivityLog:
    def __init__(self):
        self.entries = []

    def log(self, action_name, details=""):
        entry = {
            "timestamp": datetime.now().isoformat(),
            "action": action_name,
            "details": details
        }
        self.entries.append(entry)
        return entry

    def get_recent(self, count=10):
        return self.entries[-count:] if len(self.entries) >= count else list(self.entries)
