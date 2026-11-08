import json

# 1. Check 14_Organizations uid 1 name/tag
with open('Kara No/14_Organizations.json', 'r', encoding='utf-8') as f:
    d14 = json.load(f)
print("14_Organizations uid 1 name:", d14['entries']['1'].get('name'))
print("14_Organizations uid 1 end of content:\n", repr(d14['entries']['1']['content'][-100:]))

# 2. Check 09_Timeline for Yagami
with open('Kara No/09_Timeline.json', 'r', encoding='utf-8') as f:
    text9 = f.read()
lines9 = text9.split('\n')
for idx, l in enumerate(lines9):
    if 'yagami' in l.lower():
        print(f"09_Timeline line {idx+1}: {l}")

# 3. Check 15_Chapter_Knowledge for Under the Tree of Miracles
with open('Kara No/15_Chapter_Knowledge_Fog_of_War.json', 'r', encoding='utf-8') as f:
    text15 = f.read()
lines15 = text15.split('\n')
for idx, l in enumerate(lines15):
    if 'under the tree of miracles' in l.lower():
        print(f"15_Chapter_Knowledge line {idx+1}: {l}")

