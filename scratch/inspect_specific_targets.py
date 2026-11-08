import json, os

def inspect_targets():
    # 1. 03_Touko.json
    with open('Kara No/03_Touko.json', 'r', encoding='utf-8') as f:
        t = json.load(f)
    print("=== 03_Touko.json uid 4 prosthetic arm snippet ===")
    for l in t['entries']['4']['content'].split('\n'):
        if 'prosthetic' in l.lower() or 'arm' in l.lower() or 'fujou' in l.lower():
            print("  ", l)

    # 2. Check Shiki expansion & main for blinded eye
    for p in ['Kara No/archive/01_Shiki_Expansion.json', 'Kara No/01_Shiki.json']:
        if os.path.exists(p):
            with open(p, 'r', encoding='utf-8') as f:
                d = json.load(f)
            print(f"=== {p} checking blinded left eye ===")
            for k, v in d['entries'].items():
                if 'left eye' in v['content'].lower() or 'blind' in v['content'].lower():
                    for l in v['content'].split('\n'):
                        if 'left eye' in l.lower() or 'blind' in l.lower():
                            print(f"   [{k}] {l}")

    # 3. Check Kurogiri in 06 abilities expansion & main
    for p in ['Kara No/archive/06_Abilities_Expansion.json', 'Kara No/06_Abilities.json']:
        if os.path.exists(p):
            with open(p, 'r', encoding='utf-8') as f:
                d = json.load(f)
            print(f"=== {p} checking Matsuguruma ===")
            for k, v in d['entries'].items():
                if 'matsuguruma' in str(v).lower() or 'sadamitsu' in str(v).lower():
                    print(f"   [{k}] Key: {v.get('key')}")
                    for l in v['content'].split('\n'):
                        if 'matsuguruma' in l.lower() or 'sadamitsu' in l.lower() or 'kurogiri' in l.lower():
                            print(f"     {l}")

    # 4. Check 1996 crash in 08_World_Expansion and 08_World
    for p in ['Kara No/archive/08_World_Expansion.json', 'Kara No/08_World.json']:
        if os.path.exists(p):
            with open(p, 'r', encoding='utf-8') as f:
                d = json.load(f)
            print(f"=== {p} checking 1996 crash ===")
            for k, v in d['entries'].items():
                if '1996' in v['content']:
                    for l in v['content'].split('\n'):
                        if '1996' in l:
                            print(f"   [{k}] {l}")

inspect_targets()

