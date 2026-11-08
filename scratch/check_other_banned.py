import json

with open('Kara No/06_Abilities.json', 'r', encoding='utf-8') as f:
    d6 = json.load(f)
for k, v in d6['entries'].items():
    if 'baryonic mass' in v['content']:
        print(f"06_Abilities entry {k}:")
        for l in v['content'].split('\n'):
            if 'baryonic mass' in l:
                print("  ", l)

with open('Kara No/15_Chapter_Knowledge_Fog_of_War.json', 'r', encoding='utf-8') as f:
    d15 = json.load(f)
for k, v in d15['entries'].items():
    c = v['content']
    if 'matsuguruma' in c.lower() or 'yagami' in c.lower():
        print(f"15_Chapter_Knowledge entry {k}:")
        for l in c.split('\n'):
            if 'matsuguruma' in l.lower() or 'yagami' in l.lower():
                print("  ", l)

