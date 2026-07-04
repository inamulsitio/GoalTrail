# === Stage 50: Add unit tests for import and export behavior ===
# Project: GoalTrail
import json, os
from pathlib import Path

def test_goal_tracker_io():
    from goal_tracker import GoalTracker  # Adjust import path if needed
    with tempfile.TemporaryDirectory() as tmpdir:
        tracker = GoalTracker(Path(tmpdir) / "data.json")
        
        # Setup initial state
        assert not (Path(tmpdir) / "data.json").exists()
        tracker.add_goal("Learn Python", milestones=[10, 20], routines=["Read docs"], blockers=[], notes="Start here")
        data = json.loads((Path(tmpdir) / "data.json").read_text())
        assert len(data["goals"]) == 1
        
        # Test export to JSON string
        exported = tracker.export()
        assert isinstance(exported, str)
        loaded_data = json.loads(exported)
        assert loaded_data["version"] == data["version"]
        
        # Test import from JSON string
        new_tracker = GoalTracker(Path(tmpdir) / "new.json")
        new_tracker.import_(exported)
        imported_goals = list(new_tracker.get_all_goals())
        assert len(imported_goals) == 1
        
        # Verify data integrity after round-trip
        original_goal = tracker.get_goal("Learn Python")
        imported_goal = new_tracker.get_goal("Learn Python")
        assert imported_goal["milestones"] == original_goal["milestones"]
        
        print("All import/export tests passed.")
