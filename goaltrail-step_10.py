# === Stage 10: Add case-insensitive search across the most useful fields ===
# Project: GoalTrail
class SearchFilter:
    def __init__(self, data):
        self.data = data

    def search(self, query, fields=None):
        if not query:
            return self.data
        q = query.lower().strip()
        if fields is None:
            fields = ['goal', 'milestone', 'routine', 'blocker', 'note']
        results = []
        for item in self.data:
            match = False
            for f in fields:
                val = getattr(item, f)
                if isinstance(val, str):
                    if q in val.lower():
                        match = True
                        break
            if match:
                results.append(item)
        return results
