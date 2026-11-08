import json
import difflib
import os

def check_file(rel_path):
    print("=" * 60)
    print(f"CHECKING: {rel_path}")
    print("=" * 60)
    bak_path = os.path.join("scratch/backups_thai_constant_and_gu_20261026", os.path.basename(rel_path))
    if not os.path.exists(bak_path):
        print(f"No backup found at {bak_path}")
        return

    with open(bak_path, "r", encoding="utf-8") as f:
        d_bak = json.load(f)
    with open(rel_path, "r", encoding="utf-8") as f:
        d_curr = json.load(f)

    # Check top-level keys
    for k in set(list(d_bak.keys()) + list(d_curr.keys())):
        if k != "entries" and d_bak.get(k) != d_curr.get(k):
            print(f"[TOP LEVEL CHANGED] {k}:")
            print(f"  Bak : {d_bak.get(k)}")
            print(f"  Curr: {d_curr.get(k)}")

    # Check entries
    bak_entries = d_bak.get("entries", {})
    curr_entries = d_curr.get("entries", {})

    all_keys = sorted(list(set(list(bak_entries.keys()) + list(curr_entries.keys()))), key=lambda x: int(x) if x.isdigit() else x)

    for k in all_keys:
        if k not in bak_entries:
            print(f"\n[NEW ENTRY ADDED] Entry {k} ({curr_entries[k].get('comment', curr_entries[k].get('name'))})")
            continue
        if k not in curr_entries:
            print(f"\n[ENTRY DELETED] Entry {k} ({bak_entries[k].get('comment', bak_entries[k].get('name'))})")
            continue

        eb = bak_entries[k]
        ec = curr_entries[k]

        # Check metadata
        meta_diffs = []
        for mk in set(list(eb.keys()) + list(ec.keys())):
            if mk != "content" and eb.get(mk) != ec.get(mk):
                meta_diffs.append((mk, eb.get(mk), ec.get(mk)))

        # Check content
        cb = eb.get("content", "")
        cc = ec.get("content", "")

        if cb != cc or meta_diffs:
            print(f"\n>>> ENTRY {k} MODIFIED: {ec.get('comment', ec.get('name'))}")
            if meta_diffs:
                print("  Metadata changes:")
                for mk, old_v, new_v in meta_diffs:
                    print(f"    - {mk}: {old_v} -> {new_v}")
            if cb != cc:
                print("  Content differences:")
                diff = list(difflib.unified_diff(
                    cb.splitlines(keepends=True),
                    cc.splitlines(keepends=True),
                    fromfile="original",
                    tofile="current",
                    n=2
                ))
                for line in diff:
                    print("   ", line, end="")

if __name__ == "__main__":
    for f in [
        "Kara No/01_Shiki.json",
        "Kara No/02_Mikiya.json",
        "Kara No/16_Everyday_Life_and_Personal_Details.json",
        "Kara No/10_RP_Guide.json",
        "Kara No/12_Crossover_Dynamics.json",
        "Kara No/09_Timeline.json",
        "Fate/main_fate-stay-night.json",
        "Fate/FATE SN RP.json"
    ]:
        if os.path.exists(f):
            check_file(f)

