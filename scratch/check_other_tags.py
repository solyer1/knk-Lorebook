import json

for fpath in ['Kara No/06_Abilities.json', 'Kara No/01_Shiki.json', 'Kara No/04_Other_Characters.json']:
    with open(fpath, 'r', encoding='utf-8') as f:
        data = json.load(f)
    print(f"=== {fpath} ===")
    for k, v in data['entries'].items():
        c = v.get('content', '')
        name = v.get('name') or v.get('comment')
        close_tag = f"</{name}>"
        if close_tag in c:
            idx = c.find(close_tag)
            trailing = c[idx + len(close_tag):].strip()
            if trailing:
                print(f"  Entry {k} ({name}) has {len(trailing)} chars of TRAILING TEXT after {close_tag}!")

