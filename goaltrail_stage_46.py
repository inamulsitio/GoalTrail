# === Stage 46: Add a schema version field and migration helper ===
# Project: GoalTrail
SCHEMA_VERSION = "1.1"

def migrate_data(db_path):
    import sqlite3, os, json
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    try:
        cur.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='goals'")
        if not cur.fetchone(): return
        rows = cur.execute("SELECT * FROM goals").fetchall()
        for row in rows:
            goal_id, title, description, status, created_at = row[:5]
            new_row = (goal_id, title, description, status, created_at, SCHEMA_VERSION)
            cur.execute("INSERT OR REPLACE INTO goals VALUES (?, ?, ?, ?, ?, ?)", new_row)
        conn.commit()
    except Exception as e:
        print(f"Migration failed: {e}")
    finally:
        conn.close()
