import json
import difflib
import os

backup_dir = "scratch/backups_thai_constant_and_gu_20261026"

# Script changes from apply_constant_and_gu_update.py:
# - Added Thai keys
# - Added entry 9 to 10_RP_Guide.json, entry 53 to main_fate-stay-night.json, entry 69 to FATE SN RP.json
# - Modified Entry 1 and 8 in 10_RP_Guide.json (constant/selective and text for "กู")
# - Modified Shirou, Archer, Lancer in Fate files (keys and "กู")
# - Modified Lio, Tomoe, SHIKI, etc. for "กู"

for folder in ["Kara No", "Fate"]:
    for f in sorted(os.listdir(folder)):
        if not f.endswith(".json"):
            continue
        curr_p = os.path.join(folder, f)
        bak_p = os.path.join(backup_dir, f)
        if not os.path.exists(bak_p):
            print(f"[NO BACKUP] {curr_p}")
            continue

        with open(curr_p, "r", encoding="utf-8") as fp1, open(bak_p, "r", encoding="utf-8") as fp2:
            d_curr = json.load(fp1)
            d_bak = json.load(fp2)

        curr_entries = d_curr.get("entries", {})
        bak_entries = d_bak.get("entries", {})

        for k in curr_entries:
            if k not in bak_entries:
                continue
            cc = curr_entries[k].get("content", "")
            cb = bak_entries[k].get("content", "")

            if cc != cb:
                # Compare lines
                diff_lines = [l for l in difflib.unified_diff(cb.splitlines(), cc.splitlines(), lineterm="") if l.startswith("+") or l.startswith("-")]
                
                # Check if this diff is NOT just the automated Thai update
                user_lines = []
                for l in diff_lines:
                    # filter out known script additions
                    if any(phrase in l for phrase in [
                        "\"กู\" is FULLY ALLOWED",
                        "\"กู\" is fully allowed",
                        "never \"ฉัน\"",
                        "Never use \"ฉัน\"",
                        "strictly forbidden",
                        "MALE CHARACTERS MUST NEVER",
                        "---", "+++"
                    ]):
                        continue
                    user_lines.append(l)

                if user_lines:
                    print(f"\n=======================================================")
                    print(f"USER MODIFICATION FOUND in: {curr_p} -> Entry {k} ({curr_entries[k].get('comment', curr_entries[k].get('name'))})")
                    print(f"=======================================================")
                    for ul in user_lines:
                        print("  ", ul)

