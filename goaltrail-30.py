# === Stage 30: Add date parsing helpers with clear error messages ===
# Project: GoalTrail
def parse_date(date_str: str) -> datetime.date | None:
    """Parse date string returning None on failure with clear error."""
    if not date_str.strip():
        return None
    formats = ["%Y-%m-%d", "%d.%m.%Y", "%d/%m/%Y", "%m/%d/%Y", "%Y/%m/%d"]
    for fmt in formats:
        try:
            return datetime.strptime(date_str.strip(), fmt)
        except ValueError:
            continue
    raise ValueError(f"Unrecognized date format for '{date_str}'. Supported: YYYY-MM-DD, DD.MM.YYYY, etc.")
