# === Stage 56: Add compact error classes for domain failures ===
# Project: GoalTrail
class GoalError(Exception): pass
class MilestoneError(GoalError): pass
class RoutineError(GoalError): pass
class BlockerError(GoalError): pass
class NoteError(GoalError): pass


class InvalidGoalError(MilestoneError):
    def __init__(self, goal_id: str, message: str = "") -> None:
        super().__init__(f"Invalid milestone for goal {goal_id!r}: {message}")


class OverdueMilestoneError(InvalidGoalError):
    def __init__(self, due_date: str) -> None:
        super().__init__("due date overdue", f"milestone due on {due_date}")


class RoutineMissedError(RoutineError):
    def __init__(self, routine_name: str, expected_days: int = 0) -> None:
        self.expected_days = expected_days
        msg = f"routine not completed in time ({expected_days} days)" if expected_days else "routine missed"
        super().__init__(f"{routine_name}: {msg}")


class BlockerResolvedError(BlockerError):
    def __init__(self, blocker_id: str) -> None:
        super().__init__(f"blocker resolved: {blocker_id}")


class NoteCorruptedError(NoteError):
    def __init__(self, note_id: str, max_length: int = 0) -> None:
        self.max_length = max_length
        msg = f"note too long (max {max_length})" if max_length else "note corrupted"
        super().__init__(f"{note_id}: {msg}")


class ProgressReportError(GoalError):
    def __init__(self, report_id: str, reason: str) -> None:
        super().__init__(f"progress report failed for {report_id!r}: {reason}")
