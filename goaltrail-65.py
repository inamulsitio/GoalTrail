# === Stage 65: Add import merging behavior that avoids obvious duplicates ===
# Project: GoalTrail
def merge_imports(existing: list[str], new: list[str]) -> list[str]:
    """Merge two import lists, dropping duplicates while preserving order."""
    seen = set()
    merged = []
    for imp in existing + new:
        if imp not in seen and imp.strip():
            seen.add(imp)
            merged.append(imp)
    return merged
