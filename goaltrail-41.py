# === Stage 41: Add plain text import for a simple line-based format ===
# Project: GoalTrail
class PlainTextLoader:
    def __init__(self, path):
        self.path = path
        self.data = {}

    def load(self):
        with open(self.path, 'r', encoding='utf-8') as f:
            for line in f:
                line = line.strip()
                if not line or line.startswith('#'): continue
                parts = line.split('=', 1)
                if len(parts) == 2:
                    key, value = parts[0].strip(), parts[1].strip().strip('"\'')
                    self.data[key] = value

    def get(self, key):
        return self.data.get(key)
