import json

with open(r"Kara No/04_Other_Characters.json", encoding="utf-8") as f:
    data = json.load(f)

for k, v in data["entries"].items():
    print(f"Index {k}: uid={v['uid']}, name={v['name']}, order={v['order']}, keys={len(v.get('key', []))}")

