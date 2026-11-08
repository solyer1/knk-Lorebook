import json

def check_merged_entries():
    targets = [
        ('Kara No/01_Shiki.json', 'Shiki_Chronological_Mindset_and_Memory_Phases'),
        ('Kara No/06_Abilities.json', 'Mechanics_Unified_Language_Gods_Word'),
        ('Kara No/08_World.json', 'Tradition_Ryougi_Yin_Yang_Tripartite_Framework'),
        ('Kara No/05_Relationships.json', 'Rel_Shiki_Mikiya_Chronological_Phases'),
    ]
    for path, entry_name in targets:
        with open(path, 'r', encoding='utf-8') as f:
            d = json.load(f)
        found = False
        for k, v in d.get('entries', {}).items():
            if v.get('name') == entry_name or v.get('comment') == entry_name:
                print(f"FOUND in {path}: uid {k} ({entry_name})")
                found = True
        if not found:
            print(f"NOT FOUND in {path}: {entry_name}")

check_merged_entries()

