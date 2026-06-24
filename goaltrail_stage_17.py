# === Stage 17: Add dry-run behavior for commands that mutate state ===
# Project: GoalTrail
def dry_run_mode():
    import sys, os
    if len(sys.argv) > 1 and sys.argv[1] == "--dry-run":
        print("DRY RUN MODE: No state changes will be made.")
        return True
    return False

def safe_write(path, content):
    if dry_run_mode():
        print(f"[DRY-RUN] Would write to {path}:")
        for line in content.splitlines():
            print(f"  {line}")
        return False
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    return True

def safe_append(path, lines):
    if dry_run_mode():
        print(f"[DRY-RUN] Would append to {path}:")
        for line in lines:
            print(f"  +{line}")
        return False
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "a", encoding="utf-8") as f:
        f.write("\n".join(lines))
    return True
