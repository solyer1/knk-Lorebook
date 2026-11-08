import json

def inspect_touko_cigs():
    with open('Kara No/03_Touko.json', 'r', encoding='utf-8') as f:
        t_data = json.load(f)
    print("=== 03_Touko.json ===")
    for u in ['0', '3', '10']:
        entry = t_data['entries'][u]
        print(f"\n--- uid {u} ({entry.get('name')}) ---")
        for line in entry['content'].split('\n'):
            if any(w in line.lower() for w in ['smoke', 'cigarette', 'brand', 'tobacco', 'sobranie', 'gitanes']):
                print("  ", line.strip())

    with open('Kara No/16_Everyday_Life_and_Personal_Details.json', 'r', encoding='utf-8') as f:
        e_data = json.load(f)
    print("\n=== 16_Everyday_Life_and_Personal_Details.json ===")
    entry2 = e_data['entries']['2']
    print(f"--- uid 2 ({entry2.get('name')}) ---")
    for line in entry2['content'].split('\n'):
        if any(w in line.lower() for w in ['smoke', 'cigarette', 'brand', 'tobacco', 'sobranie', 'gitanes']):
            print("  ", line.strip())

inspect_touko_cigs()

