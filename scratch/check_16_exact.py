import json
import difflib

with open('Kara No/16_Everyday_Life_and_Personal_Details.json', 'r', encoding='utf-8') as f:
    curr = json.load(f)

with open('scratch/backups_thai_constant_and_gu_20261026/16_Everyday_Life_and_Personal_Details.json', 'r', encoding='utf-8') as f:
    bak = json.load(f)

for k in curr['entries']:
    c1 = curr['entries'][k]['content']
    c2 = bak['entries'][k]['content']
    if c1 != c2:
        print(f"Entry {k} ({curr['entries'][k].get('comment')}):")
        diff = difflib.unified_diff(c2.splitlines(), c1.splitlines(), lineterm="")
        for line in diff:
            if line.startswith('+') or line.startswith('-'):
                print(" ", line)

