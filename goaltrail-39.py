# === Stage 39: Add a repair function for simple data integrity issues ===
# Project: GoalTrail
def repair_data_integrity(db_path):
    import sqlite3, json, os
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    try:
        # Ensure goals table exists with required columns
        cur.execute("""CREATE TABLE IF NOT EXISTS goals (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT UNIQUE NOT NULL, description TEXT, status TEXT DEFAULT 'active', created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP);""")
        # Ensure milestones table exists and is linked to goals
        cur.execute("""CREATE TABLE IF NOT EXISTS milestones (id INTEGER PRIMARY KEY AUTOINCREMENT, goal_id INTEGER NOT NULL, title TEXT NOT NULL, completed BOOLEAN DEFAULT FALSE, order_index INTEGER DEFAULT 0, FOREIGN KEY(goal_id) REFERENCES goals(id));""")
        # Ensure routines table exists and is linked to goals
        cur.execute("""CREATE TABLE IF NOT EXISTS routines (id INTEGER PRIMARY KEY AUTOINCREMENT, goal_id INTEGER NOT NULL, title TEXT NOT NULL, frequency TEXT DEFAULT 'daily', completed BOOLEAN DEFAULT FALSE, FOREIGN KEY(goal_id) REFERENCES goals(id));""")
        # Ensure blockers table exists and is linked to goals
        cur.execute("""CREATE TABLE IF NOT EXISTS blockers (id INTEGER PRIMARY KEY AUTOINCREMENT, goal_id INTEGER NOT NULL, description TEXT NOT NULL, resolved BOOLEAN DEFAULT FALSE, FOREIGN KEY(goal_id) REFERENCES goals(id));""")
        # Ensure notes table exists and is linked to goals
        cur.execute("""CREATE TABLE IF NOT EXISTS notes (id INTEGER PRIMARY KEY AUTOINCREMENT, goal_id INTEGER NOT NULL, content TEXT NOT NULL, created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP);""")
        
        # Repair orphaned milestones/routines/blockers/notes by removing them if their parent goal does not exist
        for table in ['milestones', 'routines', 'blockers', 'notes']:
            cur.execute(f"DELETE FROM {table} WHERE NOT EXISTS (SELECT 1 FROM goals WHERE goals.id = {table}.goal_id)")
        
        # Repair duplicate goal names by appending a numeric suffix to duplicates while preserving data
        cur.execute("SELECT id, name FROM goals")
        seen_names = {}
        for row in cur.fetchall():
            gid, gname = row
            if gname not in seen_names:
                seen_names[gname] = 0
            else:
                seen_names[gname] += 1
                new_name = f"{gname} ({seen_names[gname]})"
                cur.execute("UPDATE goals SET name = ? WHERE id = ?", (new_name, gid))
        
        conn.commit()
    except Exception as e:
        print(f"Repair failed: {e}")
    finally:
        conn.close()
