# === Stage 73: Add a lightweight HTML report export ===
# Project: GoalTrail
def export_html_report(self, output_path="goaltrail_report.html"):
    """Export a compact HTML progress report for the current goal."""
    lines = ["<html><head><meta charset='utf-8'>", "<title>GoalTrail Report</title>",
             "<style>body{font-family:monospace;max-width:800px;margin:20px auto;}"]
    lines.append("<h1>Goal Report</h1>")
    if self.goal_name:
        lines.append(f"<p><b>{self.goal_name}</b></p>")
    for m in self.milestones:
        status = "✅ Done" if m.done else "<span style='color:red'>❌ Pending</span>"
        lines.append(f"<li>{m.title} — {status}</li>")
    for r in self.routines:
        lines.append(f"<p>📋 Routine: <b>{r.name}</b></p>")
        if r.tasks:
            done = sum(1 for t in r.tasks.values() if t["done"])
            total = len(r.tasks)
            pct = int(done / total * 100) if total else 0
            lines.append(f"<p>Progress: {done}/{total} ({pct}%)</p>")
    if self.blockers and any(self.blockers.values()):
        active = [b for b in self.blockers.values() if not b["resolved"]]
        lines.append("<h2>Active Blockers</h2><ul>")
        for b in active:
            lines.append(f"<li>{b['text']}</li>")
        lines.append("</ul>")
    lines.append("</body></html>")
    with open(output_path, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))
