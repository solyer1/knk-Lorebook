import json
import glob
import os

target_files = [
    'Kara No/01_Shiki.json',
    'Kara No/02_Mikiya.json',
    'Kara No/05_Relationships.json',
    'Kara No/10_RP_Guide.json',
    'Kara No/13_Dialogue_Examples.json'
]

for tf in target_files:
    print(f"=== {tf} ===")
    with open(tf, 'r', encoding='utf-8') as f:
        data = json.load(f)
    for k, v in data.get('entries', {}).items():
        name = v.get('name', '')
        comment = v.get('comment', '')
        content = v.get('content', '')
        if any(term in name.lower() or term in comment.lower() for term in ['shiki', 'mikiya', 'dialogue', 'subtext', 'tone']):
            print(f"  Entry {k}: {name} ({len(content)} chars)")
