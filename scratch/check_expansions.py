import os, json

expansion_files = [
    'Kara No/01_Shiki_Expansion.json',
    'Kara No/archive/01_Shiki_Expansion.json',
    'Kara No/02_Mikiya_Expansion.json',
    'Kara No/archive/02_Mikiya_Expansion.json',
    'Kara No/03_Touko_Expansion.json',
    'Kara No/archive/03_Touko_Expansion.json',
    'Kara No/05_Relationships_Expansion.json',
    'Kara No/archive/05_Relationships_Expansion.json',
    'Kara No/06_Abilities_Expansion.json',
    'Kara No/archive/06_Abilities_Expansion.json',
    'Kara No/08_World_Expansion.json',
    'Kara No/archive/08_World_Expansion.json',
]

for p in expansion_files:
    if os.path.exists(p):
        print(f"EXISTS: {p}")
        try:
            with open(p, 'r', encoding='utf-8') as f:
                d = json.load(f)
            print(f"  Entries count: {len(d.get('entries', {}))}")
            for k, v in list(d.get('entries', {}).items())[:3]:
                print(f"    uid {k}: {v.get('name') or v.get('comment')}")
        except Exception as e:
            print(f"  Error loading: {e}")
    else:
        print(f"NOT FOUND: {p}")

