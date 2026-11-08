import json

with open('Kara No/09_Timeline.json', 'r', encoding='utf-8') as f:
    d = json.load(f)

print("=== Entry 0 ===")
print(d['entries']['0']['content'])

print("=== Entry 6 ===")
print(d['entries']['6']['content'][:1000])

print("=== Entry 11 ===")
print(d['entries']['11']['content'])

