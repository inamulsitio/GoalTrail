# === Stage 42: Add CSV export without external dependencies ===
# Project: GoalTrail
def export_to_csv(data, filename="goaltrail_export.csv"):
    import csv
    if not data: return False
    headers = list(data[0].keys())
    with open(filename, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=headers)
        writer.writeheader()
        for row in data:
            # Ensure all rows have same keys by filling missing with empty string
            clean_row = {k: row.get(k, "") for k in headers}
            writer.writerow(clean_row)
    return True
