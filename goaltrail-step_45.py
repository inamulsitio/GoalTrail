# === Stage 45: Add restore from backup with validation ===
# Project: GoalTrail
import json, os, hashlib

def restore_backup(backup_path: str) -> bool:
    if not backup_path.endswith('.json'): return False
    try:
        with open(backup_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        expected_hash = hashlib.sha256(json.dumps(data, sort_keys=True).encode()).hexdigest()[:10]
        if not os.path.exists('.goaltrail_backup_hash'): return False
        with open('.goaltrail_backup_hash', 'r') as hf:
            stored_hash = hf.read().strip()
        if expected_hash != stored_hash: raise ValueError("Hash mismatch")
    except (json.JSONDecodeError, IOError):
        print(f"Invalid backup file: {backup_path}")
        return False
    try:
        with open('goaltrail.json', 'w') as f: json.dump(data, f)
        os.remove(backup_path)
        print("Backup restored successfully.")
        return True
    except IOError as e:
        print(f"Failed to write backup: {e}")
        return False
