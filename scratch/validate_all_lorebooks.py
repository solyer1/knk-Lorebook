import json
import glob
import os

all_json_files = sorted(glob.glob("Kara No/*.json") + glob.glob("Fate/*.json"))
print(f"Total JSON files found: {len(all_json_files)}")

total_entries = 0
valid_files = 0
errors = []

for fpath in all_json_files:
    try:
        with open(fpath, "r", encoding="utf-8") as f:
            data = json.load(f)
        entries = data.get("entries", {})
        total_entries += len(entries)
        valid_files += 1
    except Exception as e:
        errors.append((fpath, str(e)))

print(f"Valid JSON files: {valid_files}/{len(all_json_files)}")
print(f"Total entries across repository: {total_entries}")
if errors:
    print("ERRORS DETECTED:")
    for f, err in errors:
        print(f"  {f}: {err}")
else:
    print("All JSON files are syntactically valid!")

# Verify Thai rules are in place
print("\n--- Verifying Thai Rules across updated files ---")
check_files = [
    "Kara No/01_Shiki.json",
    "Kara No/02_Mikiya.json",
    "Kara No/05_Relationships.json",
    "Kara No/06_Abilities.json",
    "Kara No/10_RP_Guide.json",
    "Kara No/13_Dialogue_Examples.json"
]

for cf in check_files:
    with open(cf, "r", encoding="utf-8") as f:
        data = json.load(f)
    print(f"\nFile: {cf}")
    found = False
    for k, v in data.get("entries", {}).items():
        c = v.get("content", "")
        if "เธอ" in c or "ชิกิ" in c or "นาย" in c or "Thai" in c:
            lines = c.split("\n")
            matching_lines = [l for l in lines if any(w in l for w in ["เธอ", "ชิกิ", "นาย", "Thai"])]
            print(f"  Entry {k} ({v.get('name')}): {len(matching_lines)} relevant lines")
            for ml in matching_lines[:3]:
                print(f"    -> {ml.strip()[:110]}...")
            found = True
    if not found:
        print("  WARNING: No Thai rules found in file!")
