# === Stage 44: Add backup creation for the data file ===
# Project: GoalTrail
import os, json, datetime
from pathlib import Path

def backup_data(data_file: str, target_dir: str = "backups") -> None:
    """Create a timestamped backup of the data file."""
    path = Path(data_file)
    if not path.exists():
        return
    
    # Ensure backup directory exists
    os.makedirs(target_dir, exist_ok=True)
    
    # Generate unique filename with timestamp
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_name = f"{path.stem}_{timestamp}{path.suffix}"
    backup_path = Path(target_dir) / backup_name
    
    try:
        # Read original content
        with open(path, "r", encoding="utf-8") as src:
            content = src.read()
        
        # Write to backup location
        with open(backup_path, "w", encoding="utf-8") as dst:
            dst.write(content)
            
    except Exception as e:
        print(f"Backup failed: {e}")
