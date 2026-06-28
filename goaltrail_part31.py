# === Stage 31: Add compact table rendering for long lists ===
# Project: GoalTrail
def render_compact_table(items, columns):
    if not items: return "No data."
    widths = [max(len(str(x.get(c))) for x in items) + 2 for c in columns]
    header = " | ".join(w.center(wd) for w, wd in zip(columns, widths))
    line = "-+-".join("-" * (wd - 1) for wd in widths)
    rows = [header, line]
    for item in items:
        rows.append(" | ".join(str(item.get(c, ""))[:widths[i]-2].ljust(widths[i]) for i, c in enumerate(columns)))
    return "\n".join(rows)
