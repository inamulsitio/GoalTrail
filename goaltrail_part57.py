# === Stage 57: Add structured result objects for command handlers ===
# Project: GoalTrail
class CommandResult:
    """Structured response returned by goal-tracker command handlers."""

    def __init__(self, status="ok", message="", data=None):
        self.status = status  # "ok" | "error" | "warning"
        self.message = message
        self.data = data or {}

    @staticmethod
    def ok(message=""):
        return CommandResult(status="ok", message=message)

    @staticmethod
    def error(msg):
        return CommandResult(status="error", message=msg, data={"trace": ""})

    @staticmethod
    def warning(msg):
        return CommandResult(status="warning", message=msg)

    def __repr__(self):
        return f"CommandResult({self.status!r}, {self.message[:40]!r})"
