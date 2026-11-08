import json
import glob
import os

target_files = [
    r"Kara No/05_Relationships.json",
    r"Kara No/06_Abilities.json",
    r"Kara No/07_Locations.json",
    r"Kara No/08_World.json",
    r"Kara No/12_Crossover_Dynamics.json",
    r"Kara No/13_Dialogue_Examples.json",
    r"Kara No/14_Organizations.json",
    r"Kara No/15_Chapter_Knowledge_Fog_of_War.json"
]

for tf in target_files:
    if os.path.exists(tf):
        with open(tf, encoding="utf-8") as f:
            data = json.load(f)
        print(f"\n=== FILE: {tf} (Entries: {len(data['entries'])}) ===")
        for k, v in data["entries"].items():
            print(f"  [{k}] uid={v['uid']}, name={v['name']}")
            print(f"      keys: {v.get('key', [])[:5]}")
            print(f"      keysec: {v.get('keysecondary', [])[:5]}")

