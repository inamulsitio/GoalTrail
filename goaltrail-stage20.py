# === Stage 20: Add duplicate detection for newly created records ===
# Project: GoalTrail
class DuplicateGuard:
    def __init__(self, db):
        self.db = db

    def check_duplicate(self, record_type, **kwargs):
        query_fields = [f"{k}_id" for k in kwargs.keys()]
        if not query_fields:
            return False
        cursor = self.db.cursor()
        placeholders = ",".join(["%s"] * len(query_fields))
        sql = f"SELECT id FROM {record_type} WHERE {placeholders}"
        try:
            cursor.execute(sql, [kwargs[f] for f in query_fields])
            return cursor.fetchone() is not None
        finally:
            cursor.close()

    def get_unique_id(self, record_type, **kwargs):
        if self.check_duplicate(record_type, **kwargs):
            raise ValueError(f"Duplicate {record_type} detected")
        return f"{record_type}_{id(kwargs)}_{int(time.time())}"
