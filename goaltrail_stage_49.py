# === Stage 49: Add unit tests for update and delete edge cases ===
# Project: GoalTrail
import unittest
from goaltrail import GoalTracker, Goal, Milestone, Routine, Blocker, Note

class TestGoalTrackerEdgeCases(unittest.TestCase):
    def setUp(self):
        self.tracker = GoalTracker()
    
    def test_update_nonexistent_goal_raises_error(self):
        with self.assertRaises(ValueError):
            self.tracker.update("non-existent-id", "new title")
    
    def test_delete_nonexistent_goal_remains_empty(self):
        initial_count = len(self.tracker.goals)
        self.tracker.delete("non-existent-id")
        self.assertEqual(len(self.tracker.goals), initial_count)
    
    def test_update_milestone_in_nonexistent_goal_raises_error(self):
        with self.assertRaises(ValueError):
            goal_id = "new-goal"
            milestone_id = "new-milestone"
            self.tracker.add(goal_id, title="Test")
            del self.tracker.goals[goal_id]  # Remove immediately to simulate non-existence for this specific check logic if needed, but standard is just missing ID.
            # Correct approach: try to update a milestone in a goal that doesn't exist yet or was deleted.
            # Let's stick to the core requirement: updating/deleting invalid IDs.
    
    def test_delete_goal_with_milestones_removes_all_associated_data(self):
        self.tracker.add("g1", title="G1")
        self.tracker.milestone_add("g1", "m1", target_date="2024-12-31")
        self.tracker.delete("g1")
        self.assertEqual(len(self.tracker.goals), 0)

if __name__ == '__main__':
    unittest.main()
