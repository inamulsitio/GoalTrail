# === Stage 9: Add sorting by title, date, priority, and last update time ===
# Project: GoalTrail
class GoalSorter:
    def __init__(self, goals): self.goals = goals
    def by_title(self) -> list: return sorted(self.goals, key=lambda g: g['title'].lower())
    def by_date(self) -> list: return sorted(self.goals, key=lambda g: g.get('created_at', ''), reverse=True)
    def by_priority(self) -> list: return sorted(self.goals, key=lambda g: {'high': 0, 'medium': 1, 'low': 2}.get(g.get('priority', 'medium'), 1))
    def by_updated(self) -> list: return sorted(self.goals, key=lambda g: g.get('updated_at', ''), reverse=True)
