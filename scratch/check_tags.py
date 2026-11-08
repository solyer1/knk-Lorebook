import json

def check_xml_tags(filepath, tag_names):
    with open(filepath, 'r', encoding='utf-8') as f:
        data = json.load(f)
    print(f"=== {filepath} ===")
    for k, v in data['entries'].items():
        c = v.get('content', '')
        name = v.get('name') or v.get('comment')
        close_tag = f"</{name}>"
        if close_tag in c:
            idx = c.find(close_tag)
            trailing = c[idx + len(close_tag):].strip()
            if trailing:
                print(f"Entry {k} ({name}) has {len(trailing)} chars of TRAILING TEXT after {close_tag}!")
                print("  Trailing sample:", repr(trailing[:80]))
            else:
                print(f"Entry {k} ({name}) ends cleanly with {close_tag}.")
        else:
            print(f"Entry {k} ({name}) DOES NOT HAVE {close_tag}!")

check_xml_tags('Kara No/16_Everyday_Life_and_Personal_Details.json', [])
check_xml_tags('Kara No/03_Touko.json', [])

