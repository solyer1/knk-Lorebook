import json, glob, os

files = sorted(glob.glob('Kara No/*.json'))
file_stats = []
all_entries = []

for fpath in files:
    fname = os.path.basename(fpath)
    with open(fpath, 'r', encoding='utf-8') as f:
        data = json.load(f)
    entries = data.get('entries', {})
    total_words = 0
    total_chars = 0
    for k, v in entries.items():
        c = v.get('content', '')
        w = len(c.split())
        ch = len(c)
        tok = int(w * 1.33)
        total_words += w
        total_chars += ch
        all_entries.append({
            'file': fname,
            'uid': k,
            'name': v.get('comment', v.get('name', 'unnamed')),
            'words': w,
            'chars': ch,
            'tokens': tok
        })
    f_tok = int(total_words * 1.33)
    file_stats.append({
        'file': fname,
        'entries': len(entries),
        'words': total_words,
        'chars': total_chars,
        'tokens': f_tok
    })

print("=== FILES RANKED BY TOTAL TOKENS ===")
file_stats.sort(key=lambda x: x['tokens'], reverse=True)
for s in file_stats:
    print(f"{s['file']:<25} | Entries: {s['entries']:<2} | Words: {s['words']:<5} | Chars: {s['chars']:<6} | Tokens: ~{s['tokens']:<5}")

print("\n=== TOP 10 INDIVIDUAL ENTRIES RANKED BY TOKENS ===")
all_entries.sort(key=lambda x: x['tokens'], reverse=True)
for i, e in enumerate(all_entries[:10], 1):
    print(f"{i:2}. {e['file']:<23} | {e['name']:<35} | Words: {e['words']:<4} | Chars: {e['chars']:<5} | Tokens: ~{e['tokens']}")
