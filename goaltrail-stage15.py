# === Stage 15: Add a simple command dispatcher for text commands ===
# Project: GoalTrail
class CommandDispatcher:
    def __init__(self, handlers):
        self.handlers = {cmd.lower(): handler for cmd, handler in handlers.items()}

    def dispatch(self, text):
        clean_text = text.strip().lower()
        if clean_text in self.handlers:
            return self.handlers[clean_text]()
        elif clean_text.startswith("help"):
            print("Available commands:", ", ".join(sorted(self.handlers.keys())))
            return True
        else:
            print(f"Unknown command: {text}")
            return False

    def register(self, cmd, handler):
        self.handlers[cmd.lower()] = handler
