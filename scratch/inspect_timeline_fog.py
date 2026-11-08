import json

def inspect_timeline_and_fog():
    # 09_Timeline
    with open('Kara No/09_Timeline.json', 'r', encoding='utf-8') as f:
        t_data = json.load(f)
    print("=== 09_Timeline.json ===")
    for u in ['0', '3', '6', '11']:
        e = t_data['entries'][u]
        print(f"\n--- uid {u} ({e.get('name')}) ---")
        for l in e['content'].split('\n'):
            if any(w in l.lower() for w in ['arm', 'prosthetic', 'kirie', 'shizuno', 'yagami', 'february 1996', 'feb 1996']):
                print("  ", l.strip())

    # 15_Chapter_Knowledge
    with open('Kara No/15_Chapter_Knowledge_Fog_of_War.json', 'r', encoding='utf-8') as f:
        f_data = json.load(f)
    print("\n=== 15_Chapter_Knowledge_Fog_of_War.json ===")
    for u in ['0', '1', '2', '3', '5', '10', '11']:
        e = f_data['entries'][u]
        print(f"\n--- uid {u} ({e.get('name')}) ---")
        for l in e['content'].split('\n'):
            if any(w in l.lower() for w in ['arm', 'prosthetic', 'kirie', 'shizuno', 'february 1996', 'tree of miracles', 'analgesia']):
                print("  ", l.strip())

inspect_timeline_and_fog()

