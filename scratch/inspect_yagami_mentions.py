import json, os

files = [
    'Kara No/archive/01_Shiki_Expansion.json',
    'Kara No/01_Shiki.json',
    'Kara No/archive/05_Relationships_Expansion.json',
    'Kara No/05_Relationships.json',
    'Kara No/16_Everyday_Life_and_Personal_Details.json',
    'Kara No/07_Locations.json',
    'Kara No/09_Timeline.json'
]

for p in files:
    if os.path.exists(p):
        with open(p, 'r', encoding='utf-8') as f:
            d = json.load(f)
        print(f"=== {p} ===")
        for k, v in d['entries'].items():
            c = v.get('content', '')
            if 'yagami' in c.lower() or '404' in c:
                for l in c.split('\n'):
                    if 'yagami' in l.lower() or '404' in l:
                        print(f"   [{k} {v.get('name')}] {l.strip()}")

