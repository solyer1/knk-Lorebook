import os, json

active_files = [
    '01_Shiki.json',
    '02_Mikiya.json',
    '03_Touko.json',
    '04_Other_Characters.json',
    '05_Relationships.json',
    '06_Abilities.json',
    '07_Locations.json',
    '08_World.json',
    '09_Timeline.json',
    '10_RP_Guide.json',
    '011_Fate_Integration.json',
    '12_Crossover_Dynamics.json',
    '13_Dialogue_Examples.json',
    '14_Organizations.json',
    '15_Chapter_Knowledge_Fog_of_War.json',
    '16_Everyday_Life_and_Personal_Details.json'
]

total = 0
for af in active_files:
    p = os.path.join('Kara No', af)
    with open(p, 'r', encoding='utf-8') as f:
        d = json.load(f)
    entries = d.get('entries', {})
    total += len(entries)
    orders = [v.get('order') for v in entries.values()]
    print(f"{af}: {len(entries)} entries, min order={min(orders)}, max order={max(orders)}")

print(f"Total active entries in Kara No: {total}")

