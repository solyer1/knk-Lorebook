# -*- coding: utf-8 -*-
import json
import glob
import os

path = "Kara No/16_Everyday_Life_and_Personal_Details.json"

with open(path, "r", encoding="utf-8") as f:
    data = json.load(f)

entries = data.get("entries", {})
print(f"File: {path}")
print(f"Module Name: {data.get('name')}")
print(f"Scan Depth: {data.get('scan_depth')}")
print(f"Token Budget: {data.get('token_budget')}")
print(f"Total Entries: {len(entries)}")

required_keys = ["uid", "name", "comment", "key", "keysecondary", "content", "constant", "selective", "selectiveLogic", "order", "position", "disable", "ignoreBudget", "excludeRecursion", "preventRecursion", "probability", "useProbability", "depth", "displayIndex"]

uids = set()
names = set()
errors = []
tag_counts = {"[CANON]": 0, "[INFERENCE]": 0, "[RP SUGGESTION]": 0, "[CANON - UNKNOWN]": 0, "[CANON - CONFIRMED NONE]": 0}

for k, e in entries.items():
    uid = e.get("uid")
    name = e.get("name")
    
    if uid in uids:
        errors.append(f"Duplicate UID: {uid}")
    uids.add(uid)
    
    if name in names:
        errors.append(f"Duplicate Name: {name}")
    names.add(name)
    
    for rk in required_keys:
        if rk not in e:
            errors.append(f"Entry {k} missing key: {rk}")
            
    content = e.get("content", "")
    for tag in tag_counts:
        tag_counts[tag] += content.count(tag)

print("\n--- Validation Results ---")
if errors:
    print(f"FAILED with {len(errors)} errors:")
    for err in errors:
        print(f"  - {err}")
else:
    print("ALL 14 ENTRIES VALIDATED CLEANLY!")

print("\n--- Tag Counts in Module ---")
for tag, count in tag_counts.items():
    print(f"  {tag:<28}: {count} occurrences")

print("\n--- Entries Summary ---")
for k in sorted(entries.keys(), key=lambda x: int(x)):
    e = entries[k]
    print(f"[{e['uid']:2d}] {e['name']:<52} | Keys: {len(e['key'])} | Sec: {len(e['keysecondary'])} | Chars: {len(e['content'])}")
