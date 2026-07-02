# === Stage 43: Add CSV import for the primary record type ===
# Project: GoalTrail
import csv, json, sys
from pathlib import Path
def load_csv(file_path: str) -> list[dict]:
    records = []
    path = Path(file_path)
    if not path.exists(): return records
    with open(path, newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            try:
                clean_row = {k.strip() if k else '': v.strip() or '' for k, v in zip(reader.fieldnames or [], row)}
                records.append(clean_row)
            except Exception: pass
    return records

def save_csv(records: list[dict], file_path: str):
    path = Path(file_path)
    if not records: return
    fieldnames = list(records[0].keys())
    with open(path, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(records)

def import_to_jsonl(csv_path: str, jsonl_path: str):
    records = load_csv(csv_path)
    if not records: return 0
    Path(jsonl_path).write_text('\n'.join(f"{json.dumps(r)}" for r in records), encoding='utf-8')
    save_jsonl(records, jsonl_path)
    print(f"Imported {len(records)} records from {csv_path} to {jsonl_path}")
