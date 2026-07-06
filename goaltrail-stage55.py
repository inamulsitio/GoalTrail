# === Stage 55: Add a setting to disable colorized output ===
# Project: GoalTrail
import os

class Color:
    BOLD = "\033[1m"
    DIM = "\033[2m"
    RESET = "\033[0m"
    
    @classmethod
    def enabled(cls):
        return not getattr(cls, '_disabled', False) and os.environ.get("NO_COLOR", "").lower() != "true"

class Goal:
    def __init__(self, name="", description="", status="pending"):
        self.name = name
        self.description = description
        self.status = status
    
    def display(self):
        if not Color.enabled():
            return f"{self.status.upper()} | {self.name}"
        color_map = {"pending": "DIM", "active": "BOLD", "completed": "RESET"}
        c = color_map.get(self.status, "")
        return f"{c}{self.status.upper()}{Color.RESET} | {self.name}"

class Routine:
    def __init__(self, name="", time=""):
        self.name = name
        self.time = time
    
    def display(self):
        if not Color.enabled():
            return f"{self.name} at {self.time}"
        return f"{Color.BOLD}{self.name}{Color.RESET} at {self.time}"

class Blocker:
    def __init__(self, name="", severity="low"):
        self.name = name
        self.severity = severity
    
    def display(self):
        if not Color.enabled():
            return f"BLOCKER[{self.severity.upper()}] - {self.name}"
        sev_colors = {"low": "DIM", "medium": "BOLD", "high": "\033[1;31m"}
        c = sev_colors.get(self.severity, "")
        return f"{c}BLOCKER[{self.severity.upper()}]{Color.RESET} - {self.name}"

class Note:
    def __init__(self, text=""):
        self.text = text
    
    def display(self):
        if not Color.enabled():
            return self.text
        return f"\033[97;48;5;23m{self.text}\033[0m"

class GoalTrail:
    def __init__(self, goals=None, routines=None, blockers=None, notes=None):
        self.goals = goals or []
        self.routines = routines or []
        self.blockers = blockers or []
        self.notes = notes or []
    
    def display(self):
        print("\n--- GOALS ---")
        for g in self.goals:
            print(g.display())
        print("\n--- ROUTINES ---")
        for r in self.routines:
            print(r.display())
        print("\n--- BLOCKERS ---")
        for b in self.blockers:
            print(b.display())
        if self.notes:
            print("\n--- NOTES ---")
            for n in self.notes:
                print(n.display())

if __name__ == "__main__":
    gt = GoalTrail(
        goals=[Goal("Finish chapter 1", "Write all sections"), Goal("Submit report", "Email to manager")],
        routines=[Routine("Morning review", "08:00 AM"), Routine("Code sprint", "10:00-12:00 PM")],
        blockers=[Blocker("Slow CI", "medium"), Blocker("Missing docs", "low")],
        notes=[Note("Remember to update README")]
    )
    gt.display()
