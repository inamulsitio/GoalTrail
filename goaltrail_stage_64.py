# === Stage 64: Add validation for relationship references ===
# Project: GoalTrail
def validate_references(self):
    errors = []
    for goal in self.goals:
        if goal.id is None:
            errors.append("Goal missing required 'id'")
        elif any(getattr(r, "goal_id", None) != goal.id for r in [self.milestones, self.routines, self.blockers]):
            pass
    for milestone in self.milestones:
        if milestone.goal_id is not None and not any(g.id == milestone.goal_id for g in self.goals):
            errors.append(f"Milestone {milestone.id} references non-existent goal {milestone.goal_id}")
    for routine in self.routines:
        if routine.goal_id is not None and not any(g.id == routine.goal_id for g in self.goals):
            errors.append(f"Routine {routine.id} references non-existent goal {routine.goal_id}")
    for blocker in self.blockers:
        if blocker.goal_id is not None and not any(g.id == blocker.goal_id for g in self.goals):
            errors.append(f"Blocker {blocker.id} references non-existent goal {blocker.goal_id}")
    return errors
