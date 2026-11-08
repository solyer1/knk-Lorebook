import json
import difflib
import os

# Let's inspect Kara No/01_Shiki.json and Kara No/02_Mikiya.json specifically!

def inspect_entries(filepath):
    print("*" * 60)
    print("INSPECTING:", filepath)
    print("*" * 60)
    with open(filepath, "r", encoding="utf-8") as f:
        curr = json.load(f)
    
    bak_path = os.path.join("scratch/backups_thai_constant_and_gu_20261026", os.path.basename(filepath))
    with open(bak_path, "r", encoding="utf-8") as f:
        bak = json.load(f)

    for k, ec in curr["entries"].items():
        eb = bak["entries"].get(k, {})
        cc = ec.get("content", "")
        cb = eb.get("content", "")
        
        # Check if there are content differences
        if cc != cb:
            # Let's see if this difference is just the "Thai Pronoun" change that our script did or something else
            diff = list(difflib.unified_diff(cb.splitlines(), cc.splitlines(), lineterm=""))
            # Check if diff contains anything other than Thai lines
            is_only_thai = True
            for l in diff:
                if (l.startswith("+") or l.startswith("-")) and not any(marker in l for marker in ["---", "+++"]):
                    if not any(thai_word in l for thai_word in ["ไทย", "กู", "ฉัน", "ผม", "เรา", "ข้า", "นาย", "เธอ", "มิกิยะ", "ชิกิ", "Thai"]):
                        is_only_thai = False
            
            print(f"\n--- Entry {k}: {ec.get('comment', ec.get('name'))} --- (Only Thai update: {is_only_thai})")
            for l in diff:
                if l.startswith("+") or l.startswith("-"):
                    print("  ", l)

inspect_entries("Kara No/01_Shiki.json")
inspect_entries("Kara No/02_Mikiya.json")

