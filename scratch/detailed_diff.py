import json
import difflib
import os
import shutil

# Let's recreate what apply_constant_and_gu_update.py produced in memory or temp dir
# We have scratch/backups_thai_constant_and_gu_20261026/
# Let's run apply_constant_and_gu_update logic on the backup and compare with the current files!

backup_dir = "scratch/backups_thai_constant_and_gu_20261026"

for filename in os.listdir(backup_dir):
    rel_path = None
    for folder in ["Kara No", "Fate"]:
        cand = os.path.join(folder, filename)
        if os.path.exists(cand):
            rel_path = cand
            break
    if not rel_path:
        continue

    # Let's load the current file and the backup file
    with open(rel_path, "r", encoding="utf-8") as f:
        curr_data = json.load(f)
    with open(os.path.join(backup_dir, filename), "r", encoding="utf-8") as f:
        bak_data = json.load(f)

    # Let's check entry by entry
    curr_entries = curr_data.get("entries", {})
    bak_entries = bak_data.get("entries", {})

    diff_entries = []
    for k in sorted(list(set(list(curr_entries.keys()) + list(bak_entries.keys()))), key=lambda x: int(x) if x.isdigit() else x):
        if k not in bak_entries:
            diff_entries.append((k, "NEW", None, curr_entries[k]))
            continue
        if k not in curr_entries:
            diff_entries.append((k, "DELETED", bak_entries[k], None))
            continue
        
        cb = bak_entries[k].get("content", "")
        cc = curr_entries[k].get("content", "")

        kb = bak_entries[k].get("key", [])
        kc = curr_entries[k].get("key", [])

        if cb != cc or kb != kc:
            diff_entries.append((k, "MODIFIED", bak_entries[k], curr_entries[k]))

    if diff_entries:
        print(f"==================================================")
        print(f"FILE: {rel_path} (entries with diffs: {len(diff_entries)})")
        print(f"==================================================")
        for k, change_type, eb, ec in diff_entries:
            cname = (ec or eb).get("comment", (ec or eb).get("name"))
            print(f"--- Entry {k}: {cname} [{change_type}] ---")
            if change_type == "MODIFIED":
                kb = eb.get("key", [])
                kc = ec.get("key", [])
                added_keys = [x for x in kc if x not in kb]
                removed_keys = [x for x in kb if x not in kc]
                if added_keys:
                    print(f"  + Added keys: {added_keys}")
                if removed_keys:
                    print(f"  - Removed keys: {removed_keys}")

                cb = eb.get("content", "").splitlines()
                cc = ec.get("content", "").splitlines()
                diff = list(difflib.unified_diff(cb, cc, fromfile="bak", tofile="curr", lineterm="", n=1))
                # Filter out diffs that were purely from apply_constant_and_gu_update
                for l in diff:
                    print("   ", l)

