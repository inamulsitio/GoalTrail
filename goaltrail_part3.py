# === Stage 3: Add validation helpers for required fields, identifiers, and short text values ===
# Project: GoalTrail
def validate_goal_id(gid): return isinstance(gid, str) and len(gid.strip()) > 0 and gid.replace("-", "").replace("_", "").isalnum()
def validate_milestone(m): return isinstance(m, dict) and all(isinstance(k, str) for k in m.keys()) and all(len(str(v)) <= 50 for v in m.values()) if m else False
def validate_routine(r): return isinstance(r, list) and len(r) > 0 and all(isinstance(x, str) and len(x.strip()) >= 3 for x in r)
def validate_blocker(b): return isinstance(b, dict) and "title" in b and isinstance(b["title"], str) and len(b["title"].strip()) <= 100
def validate_note(n): return isinstance(n, str) and len(n.strip()) > 0 and len(n.replace("\n", "")) <= 2000
def sanitize_text(s): return s.strip() if isinstance(s, str) else s
def is_valid_goal(g): return all([validate_goal_id(g.get("id")), validate_milestone(g.get("milestones")), validate_routine(g.get("routines")), validate_blocker(g.get("blocker")), validate_note(g.get("note"))])
