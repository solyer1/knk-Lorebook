import json

files_and_entries = [
    ('Kara No/01_Shiki.json', ['0', '1', '4']),
    ('Kara No/02_Mikiya.json', ['3', '4']),
    ('Kara No/05_Relationships.json', ['0']),
    ('Kara No/06_Abilities.json', ['15']),
    ('Kara No/10_RP_Guide.json', ['1', '8']),
    ('Kara No/13_Dialogue_Examples.json', ['0', '1', '6'])
]

for fpath, entries in files_and_entries:
    with open(fpath, 'r', encoding='utf-8') as f:
        data = json.load(f)
    print(f"================ {fpath} ================")
    for e_id in entries:
        e = data['entries'][e_id]
        print(f"--- Entry {e_id}: {e['name']} ---")
        lines = e['content'].split('\n')
        for i, l in enumerate(lines):
            if any(h in l for h in ['SPEECH STYLE', 'Speech & Demeanor', 'DIALOGUE', 'NEGATIVE CONSTRAINTS', 'CONVERSATION STYLE', 'Vocal Cadence', 'TAKEAWAYS', 'SUBTEXT', 'PRESERVE CHARACTER']):
                print(f"  [{i}] {l}")
                for sub in lines[i+1:i+6]:
                    print(f"      {sub}")
