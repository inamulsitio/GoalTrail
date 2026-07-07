# === Stage 59: Add bulk delete behavior guarded by a confirmation flag ===
# Project: GoalTrail
import os, sys, shutil, json


def bulk_delete(directory, confirm=False):
    """Recursively delete all files and empty directories under *directory*,
    but only if *confirm* is True (or the user answers 'y' to a prompt)."""
    try:
        for root, dirs, files in os.walk(directory, topdown=False):
            for f in files:
                path = os.path.join(root, f)
                if not confirm and input(f"Delete {path}? [Y/n] ") != "y":
                    return False
                os.remove(path)
            for d in dirs:
                dir_path = os.path.join(root, d)
                if not confirm and input(f"Remove empty dir {dir_path}? [Y/n] ") != "y":
                    return False
                shutil.rmtree(dir_path)
        return True
    except Exception as e:
        print(f"Bulk delete failed: {e}")
        raise


def bulk_delete_safe(directory):
    """Ask the user once and then delete everything (no per-file prompts)."""
    answer = input("Delete ALL contents of {}? [Y/n] ".format(os.path.abspath(
        directory)))
    if answer not in ("y", "yes"):
        print("Aborted.")
        return False
    return bulk_delete(directory, confirm=True)


if __name__ == "__main__":
    import sys
    target = sys.argv[1] if len(sys.argv) > 1 else "/tmp/goaltrail_backup"
    result = bulk_delete(target, confirm=False)
    print("Done." if result else "Cancelled.")
