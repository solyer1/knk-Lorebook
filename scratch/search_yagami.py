import os, json

for root, dirs, files in os.walk('.'):
    for f in files:
        if f.endswith('.json') or f.endswith('.md'):
            p = os.path.join(root, f)
            try:
                with open(p, 'r', encoding='utf-8') as fp:
                    content = fp.read()
                if 'Yagami' in content or 'yagami' in content:
                    print(f"Found in {p}")
            except Exception:
                pass

