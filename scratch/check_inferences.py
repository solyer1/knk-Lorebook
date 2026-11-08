import json

with open('Kara No/16_Everyday_Life_and_Personal_Details.json', 'r', encoding='utf-8') as f:
    d = json.load(f)

for k, v in d['entries'].items():
    c = v['content']
    lines = c.split('\n')
    for l in lines:
        if '[INFERENCE]' in l or '[UNVERIFIED' in l:
            print(f"uid {k} ({v.get('name')}): {l.strip()}")

