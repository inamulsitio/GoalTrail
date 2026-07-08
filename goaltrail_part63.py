# === Stage 63: Add relationships between records where useful ===
# Project: GoalTrail
class Relationship:
    """Base class for all relationships between records."""
    def __init__(self, source_id, target_id):
        self.source_id = source_id
        self.target_id = target_id

    def to_dict(self):
        return {"source_id": self.source_id, "target_id": self.target_id}


class GoalMilestoneLink(Relationship):
    """Links a goal to one of its milestones."""
    pass


class RoutineDayLog(Relationship):
    """Records that a routine was completed on a given day."""
    def __init__(self, source_id, target_id, date):
        super().__init__(source_id, target_id)
        self.date = date

    def to_dict(self):
        d = {"source_id": self.source_id, "target_id": self.target_id}
        d["date"] = self.date.isoformat() if isinstance(self.date, datetime) else str(self.date)
        return d


class BlockerNote(Relationship):
    """Associates a blocker with a note that explains it."""
    pass


class NoteProgressReport(Relationship):
    """Links a note to a progress report for context."""
    pass


def apply_relationships(records, rels_data=None):
    """Attach relationship records to the main record collection.

    Args:
        records: dict mapping primary keys (e.g., goal_id) to Goal objects.
        rels_data: optional list of Relationship instances or dicts; if None, empty.

    Returns:
        The same `records` dict with each key pointing to a Goal that has its
        `.relationships` attribute populated.
    """
    from datetime import datetime

    records["relationships"] = rels_data if isinstance(rels_data, list) else []
    for r in records["relationships"]:
        if isinstance(r, Relationship):
            r._source_records = records.get(r.source_id.split("_")[0]) or {}
        elif isinstance(r, dict):
            src_key = r.pop("source_id")
            tgt_key = r.pop("target_id")
            rel = GoalMilestoneLink(src_key, tgt_key) if "milestone" in str(r.get("_type", "")) else Relationship(src_key, tgt_key)
            records["relationships"].append(rel)

    return records
