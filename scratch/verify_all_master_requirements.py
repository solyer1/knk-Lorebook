import json
import os
import re

def verify_all():
    print("======================================================================")
    print("       MANDATORY MASTER PATCH VERIFICATION SUITE")
    print("======================================================================")

    # 1. Check all JSON parsing
    all_json = []
    for root, dirs, files in os.walk('.'):
        if 'scratch' in root or 'backups_' in root:
            continue
        for f in files:
            if f.endswith('.json'):
                all_json.append(os.path.join(root, f))

    parse_fails = []
    for p in all_json:
        try:
            with open(p, 'r', encoding='utf-8') as f:
                json.load(f)
        except Exception as e:
            parse_fails.append((p, str(e)))

    if not parse_fails:
        print(f"[PASS] 1. All {len(all_json)} JSON files parsed cleanly with json.load() (zero syntax errors).")
    else:
        print(f"[FAIL] 1. Syntax errors in {len(parse_fails)} files:")
        for p, err in parse_fails:
            print(f"       {p}: {err}")

    # 2. Check XML tag format across Kara No files
    kara_no_files = [p for p in all_json if 'Kara No' in p]
    tag_fails = []
    for p in kara_no_files:
        with open(p, 'r', encoding='utf-8') as f:
            d = json.load(f)
        for k, v in d.get('entries', {}).items():
            name = v.get('name') or v.get('comment')
            c = v.get('content', '')
            open_m = re.match(r'^\s*<([a-zA-Z0-9_]+)>', c)
            if not open_m:
                tag_fails.append(f"{p} [uid {k} ({name})]: Missing leading <Tag>")
            else:
                tag = open_m.group(1)
                close_tag = f"</{tag}>"
                if not c.strip().endswith(close_tag):
                    tag_fails.append(f"{p} [uid {k} ({name})]: Content does not end with {close_tag}")

    if not tag_fails:
        print(f"[PASS] 2. Every entry's 'content' starts with <Tag> and ends with </Tag> (zero trailing text).")
    else:
        print(f"[FAIL] 2. Tag format errors in {len(tag_fails)} entries:")
        for err in tag_fails[:15]:
            print(f"       {err}")

    # 3. Check banned words
    banned_words = [
        "Kirie Shizuno",
        "Yagami",
        "Under the Tree of Miracles",
        "Doctor Ashika",
        "ชิกิค動畫กกับมิกิยะ",
        "เดดอะพอลเซิล",
        "quadriceps femoris",
        "London dispersion forces",
        "Lennard-Jones",
        "Minkowski",
        "Na_v 1.7",
        "Mohs scale",
        "12,000 Newtons"
    ]
    banned_found = []
    for p in all_json:
        with open(p, 'r', encoding='utf-8') as f:
            c = f.read()
        for bw in banned_words:
            if bw in c:
                banned_found.append((p, bw))

    if not banned_found:
        print(f"[PASS] 3. Zero occurrences of banned words found across all JSON files.")
    else:
        print(f"[FAIL] 3. Banned words found in {len(banned_found)} locations:")
        for p, bw in banned_found:
            print(f"       {p}: contains '{bw}'")

    # 4. Check all expansion files are disabled
    exp_files = [
        'Kara No/archive/01_Shiki_Expansion.json',
        'Kara No/archive/02_Mikiya_Expansion.json',
        'Kara No/archive/03_Touko_Expansion.json',
        'Kara No/archive/05_Relationships_Expansion.json',
        'Kara No/archive/06_Abilities_Expansion.json',
        'Kara No/archive/08_World_Expansion.json'
    ]
    all_disabled = True
    for ep in exp_files:
        with open(ep, 'r', encoding='utf-8') as f:
            ed = json.load(f)
        for k, v in ed.get('entries', {}).items():
            if not v.get('disable'):
                all_disabled = False
                print(f"[FAIL] {ep} uid {k} is NOT disabled!")
    if all_disabled:
        print("[PASS] 4. All 6 redundant expansion files have all entries disabled.")

    # 5. Check unique sequential order assignment
    active_files = [
        'Kara No/01_Shiki.json',
        'Kara No/02_Mikiya.json',
        'Kara No/03_Touko.json',
        'Kara No/04_Other_Characters.json',
        'Kara No/05_Relationships.json',
        'Kara No/06_Abilities.json',
        'Kara No/07_Locations.json',
        'Kara No/08_World.json',
        'Kara No/09_Timeline.json',
        'Kara No/10_RP_Guide.json',
        'Kara No/011_Fate_Integration.json',
        'Kara No/12_Crossover_Dynamics.json',
        'Kara No/13_Dialogue_Examples.json',
        'Kara No/14_Organizations.json',
        'Kara No/15_Chapter_Knowledge_Fog_of_War.json',
        'Kara No/16_Everyday_Life_and_Personal_Details.json'
    ]
    seen_orders = {}
    collisions = []
    for af in active_files:
        with open(af, 'r', encoding='utf-8') as f:
            d = json.load(f)
        for k, v in d.get('entries', {}).items():
            ord_val = v.get('order')
            name = v.get('name') or v.get('comment')
            if ord_val in seen_orders:
                collisions.append((ord_val, seen_orders[ord_val], f"{af} [uid {k}: {name}]"))
            else:
                seen_orders[ord_val] = f"{af} [uid {k}: {name}]"

    if not collisions:
        print(f"[PASS] 5. All {len(seen_orders)} active entries have unique, non-overlapping sequential orders.")
    else:
        print(f"[FAIL] 5. Found {len(collisions)} order collisions:")
        for o, a, b in collisions:
            print(f"       Order {o}: {a} vs {b}")

    print("\n======================================================================")

if __name__ == '__main__':
    verify_all()

