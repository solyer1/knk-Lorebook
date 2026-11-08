import json

def check_task2():
    print("=== TASK 2: Checking shifted Thai keywords ===")
    
    # 07_Locations uid 4-10
    with open('Kara No/07_Locations.json', 'r', encoding='utf-8') as f:
        d7 = json.load(f)
    for u in range(4, 11):
        e = d7['entries'][str(u)]
        print(f"07_Locations [{u} {e.get('name')}]:\n  key: {e.get('key')}\n  keysecondary: {e.get('keysecondary')}")

    # 08_World uid 0-10
    with open('Kara No/08_World.json', 'r', encoding='utf-8') as f:
        d8 = json.load(f)
    for u in range(0, 11):
        e = d8['entries'][str(u)]
        print(f"08_World [{u} {e.get('name')}]:\n  key: {e.get('key')}\n  keysecondary: {e.get('keysecondary')}")

    # 13_Dialogue uid 0, 2, 3
    with open('Kara No/13_Dialogue_Examples.json', 'r', encoding='utf-8') as f:
        d13 = json.load(f)
    for u in [0, 2, 3]:
        e = d13['entries'][str(u)]
        print(f"13_Dialogue [{u} {e.get('name')}]:\n  key: {e.get('key')}\n  keysecondary: {e.get('keysecondary')}")

    # 06_Abilities uid 14
    with open('Kara No/06_Abilities.json', 'r', encoding='utf-8') as f:
        d6 = json.load(f)
    e14 = d6['entries']['14']
    print(f"06_Abilities [14 {e14.get('name')}]:\n  key: {e14.get('key')}\n  keysecondary: {e14.get('keysecondary')}")

check_task2()

