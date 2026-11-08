import json

files = [
    'Kara No/01_Shiki.json',
    'Kara No/03_Touko.json',
    'Kara No/04_Other_Characters.json',
    'Kara No/06_Abilities.json',
    'Kara No/16_Everyday_Life_and_Personal_Details.json'
]

for fpath in files:
    with open(fpath, 'r', encoding='utf-8') as f:
        data = json.load(f)
    print(f"=== {fpath} ({len(data['entries'])} entries) ===")
    for k, v in data['entries'].items():
        name = v.get('name') or v.get('comment')
        print(f"  [{k}] {name}")

