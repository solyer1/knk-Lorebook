import json

with open('Kara No/16_Everyday_Life_and_Personal_Details.json', 'r', encoding='utf-8') as f:
    d = json.load(f)

print("token_budget:", d.get('token_budget'))
for k, v in d['entries'].items():
    print(f"uid {k} ({v.get('name')}): order = {v.get('order')}")

