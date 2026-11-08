import json
import difflib
import os

filepath = "Kara No/16_Everyday_Life_and_Personal_Details.json"
bak_path = os.path.join("scratch/backups_thai_constant_and_gu_20261026", os.path.basename(filepath))

with open(filepath, "r", encoding="utf-8") as f:
    curr = json.load(f)
with open(bak_path, "r", encoding="utf-8") as f:
    bak = json.load(f)

print(f"Total entries curr: {len(curr['entries'])}, bak: {len(bak['entries'])}")

for k in curr["entries"]:
    cc = curr["entries"][k]["content"]
    cb = bak["entries"][k]["content"] if k in bak["entries"] else ""
    if cc != cb:
        diff = list(difflib.unified_diff(cb.splitlines(), cc.splitlines(), lineterm=""))
        print(f"\n--- Entry {k}: {curr['entries'][k].get('comment')} ---")
        for l in diff:
            if l.startswith("+") or l.startswith("-"):
                print("  ", l)

