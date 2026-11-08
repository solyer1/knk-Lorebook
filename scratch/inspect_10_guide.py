import json

with open('Kara No/10_RP_Guide.json', 'r', encoding='utf-8') as f:
    d = json.load(f)

print("=== 10_RP_Guide.json uid 1 ===")
for l in d['entries']['1']['content'].split('\n'):
    if 'thai' in l.lower() or 'pronoun' in l.lower() or '4.' in l:
        print("  ", l)

print("\n=== 10_RP_Guide.json uid 8 ===")
for l in d['entries']['8']['content'].split('\n'):
    if 'thai' in l.lower() or 'pronoun' in l.lower() or 'guardrails' in l.lower() or 'discipline' in l.lower():
        print("  ", l)

