import json

# 1. Fix 14_Organizations uid 1
with open('Kara No/14_Organizations.json', 'r', encoding='utf-8') as f:
    d14 = json.load(f)
c = d14['entries']['1']['content']
c = c.replace("</Org_Demon_Hunter_Four_Families>", "").strip()
if not c.endswith("</Org_Asagami_Family>"):
    c = c + "\n</Org_Asagami_Family>"
d14['entries']['1']['content'] = c
with open('Kara No/14_Organizations.json', 'w', encoding='utf-8') as f:
    json.dump(d14, f, indent=2, ensure_ascii=False)
print("Fixed 14_Organizations uid 1 tag!")

# 2. Fix 09_Timeline key containing "Yagami hospital"
with open('Kara No/09_Timeline.json', 'r', encoding='utf-8') as f:
    d9 = json.load(f)
for k, v in d9['entries'].items():
    if 'key' in v and isinstance(v['key'], list):
        v['key'] = [x for x in v['key'] if 'yagami' not in x.lower()]
    if 'keysecondary' in v and isinstance(v['keysecondary'], list):
        v['keysecondary'] = [x for x in v['keysecondary'] if 'yagami' not in x.lower()]
with open('Kara No/09_Timeline.json', 'w', encoding='utf-8') as f:
    json.dump(d9, f, indent=2, ensure_ascii=False)
print("Removed 'Yagami hospital' from 09_Timeline keys!")

# 3. Fix 15_Chapter_Knowledge keysecondary containing "Under the Tree of Miracles"
with open('Kara No/15_Chapter_Knowledge_Fog_of_War.json', 'r', encoding='utf-8') as f:
    d15 = json.load(f)
for k, v in d15['entries'].items():
    if 'key' in v and isinstance(v['key'], list):
        v['key'] = ["The Crocodile and the Bird" if "Under the Tree of Miracles" in x else x for x in v['key']]
    if 'keysecondary' in v and isinstance(v['keysecondary'], list):
        v['keysecondary'] = ["The Crocodile and the Bird" if "Under the Tree of Miracles" in x else x for x in v['keysecondary']]
with open('Kara No/15_Chapter_Knowledge_Fog_of_War.json', 'w', encoding='utf-8') as f:
    json.dump(d15, f, indent=2, ensure_ascii=False)
print("Fixed 15_Chapter_Knowledge keysecondary 'Under the Tree of Miracles'!")

