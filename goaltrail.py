# === Stage 1: Create the base application structure, in-memory state, and a small demo dataset ===
# Project: GoalTrail
from dataclasses import dataclass, field
from datetime import date
from typing import List, Optional

@dataclass
class Goal:
    id: int
    title: str
    description: str
    milestones: List[str] = field(default_factory=list)
    routines: List[str] = field(default_factory=list)
    blockers: List[str] = field(default_factory=list)
    notes: List[str] = field(default_factory=list)

class GoalTracker:
    def __init__(self):
        self._goals: dict[int, Goal] = {}
        self._next_id: int = 1
    
    def add_goal(self, title: str, description: str) -> Goal:
        goal = Goal(id=self._next_id, title=title, description=description)
        self._goals[goal.id] = goal
        self._next_id += 1
        return goal
    
    def get_goals(self) -> List[Goal]:
        return list(self._goals.values())

tracker = GoalTracker()
demo_goal_1 = tracker.add_goal("Learn Python", "Master basics and advanced concepts")
demo_goal_1.milestones.append("Complete Python Crash Course")
demo_goal_1.routines.append("Code 30 minutes daily")
demo_goal_1.blockers.append["Lack of time"]

demo_goal_2 = tracker.add_goal("Build Web App", "Create a full-stack application")
demo_goal_2.milestones.append("Design database schema")
demo_goal_2.routines.append("Review pull requests")
demo_goal_2.notes.append("Use TypeScript for type safety")
