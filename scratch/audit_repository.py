import json
import glob
import os

print(f"{'FILE':<48} | {'ENTRIES':<8} | {'SIZE KB':<10} | {'THAI KEYS':<10} | {'CONST ENTRIES':<14}")
print("-" * 100)

for p in sorted(glob.glob("*/*.json")):
    if "backups" in p or "scratch" in p:
        continue
    with open(p, "r", encoding="utf-8") as f:
        d = json.load(f)
    entries = d.get("entries", {})
    size_kb = os.path.getsize(p) / 1024
    
    thai_keys = 0
    const_count = 0
    for e in entries.values():
        if e.get("constant"):
            const_count += 1
        for k in e.get("key", []) + e.get("keysecondary", []):
            if any('\u0e00' <= c <= '\u0e7f' for c in k):
                thai_keys += 1

    print(f"{p:<48} | {len(entries):<8} | {size_kb:<10.1f} | {thai_keys:<10} | {const_count:<14}")

