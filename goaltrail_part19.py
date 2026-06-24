# === Stage 19: Add undo support for the last simple mutation ===
# Project: GoalTrail
import json
from datetime import datetime, timedelta

def undo_last_mutation(data_file="goals.json"):
    """Undo the last mutation by restoring from a backup snapshot."""
    if not os.path.exists(f"{data_file}.bak"):
        print("No backup found to restore.")
        return
    
    with open(f"{data_file}.bak", "r") as f:
        restored_data = json.load(f)
    
    # Overwrite current data with the last known good state
    with open(data_file, "w") as f:
        json.dump(restored_data, f, indent=2)

# Usage example within main script logic
try:
    undo_last_mutation()
except Exception as e:
    print(f"Undo failed: {e}")
