# === Stage 2: Add dataclasses or typed dictionaries for the main domain records ===
# Project: GoalTrail
from dataclasses import dataclass, field
from datetime import date
from typing import List, Optional

@dataclass
class Milestone:
    title: str
    target_date: date
    completed: bool = False
    notes: str = ""

@dataclass
class Routine:
    name: str
    frequency_days: int  # e.g., every 7 days
    last_performed: Optional[date] = None

@dataclass
class Blocker:
    description: str
    severity: int  # 1-5
    status: str = "open"  # open, mitigated, resolved

@dataclass
class Note:
    content: str
    category: str = "general"
    created_at: date = field(default_factory=date.today)

@dataclass
class GoalRecord:
    id: int
    title: str
    milestones: List[Milestone] = field(default_factory=list)
    routines: List[Routine] = field(default_factory=list)
    blockers: List[Blocker] = field(default_factory=list)
    notes: List[Note] = field(default_factory=list)
    progress_report: Optional[str] = None
