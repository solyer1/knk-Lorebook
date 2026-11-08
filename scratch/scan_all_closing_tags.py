import os, json, re

def check_all_xml_tags():
    paths = []
    for root in ['Kara No', 'Kara No/archive']:
        for f in os.listdir(root):
            if f.endswith('.json'):
                paths.append(os.path.join(root, f))

    for p in paths:
        with open(p, 'r', encoding='utf-8') as f:
            d = json.load(f)
        issues = []
        for k, v in d.get('entries', {}).items():
            name = v.get('name') or v.get('comment')
            c = v.get('content', '')
            # Find open tag
            open_m = re.match(r'^\s*<([a-zA-Z0-9_]+)>', c)
            if not open_m:
                issues.append(f"Entry {k} ({name}): No leading <Tag>")
            else:
                tag = open_m.group(1)
                close_tag = f"</{tag}>"
                if close_tag not in c:
                    issues.append(f"Entry {k} ({name}): Missing closing {close_tag}")
                else:
                    idx = c.rfind(close_tag)
                    trailing = c[idx + len(close_tag):].strip()
                    if trailing:
                        issues.append(f"Entry {k} ({name}): {len(trailing)} chars trailing after {close_tag}")
        if issues:
            print(f"\n=== {p} ({len(issues)} issues) ===")
            for iss in issues:
                print("  ", iss)

check_all_xml_tags()

