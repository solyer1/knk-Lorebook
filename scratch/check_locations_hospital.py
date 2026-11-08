import json

def check_loc():
    with open('Kara No/07_Locations.json', 'r', encoding='utf-8') as f:
        d = json.load(f)
    for k, v in d['entries'].items():
        c = v.get('content', '')
        if 'hospital' in c.lower() or 'yagami' in c.lower():
            print(f"Entry {k}: {v.get('name')}")
            for l in c.split('\n'):
                if 'hospital' in l.lower() or 'yagami' in l.lower():
                    print("  ", l)

check_loc()

