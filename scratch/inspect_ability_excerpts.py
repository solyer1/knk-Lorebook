import json

def preview_entry(filepath, entry_id, max_lines=25):
    with open(filepath, 'r', encoding='utf-8') as f:
        data = json.load(f)
    entry = data['entries'][str(entry_id)]
    print(f"=== {filepath} [Entry {entry_id}: {entry.get('name')}] ===")
    lines = entry['content'].split('\n')
    for line in lines[:max_lines]:
        print(line)
    if len(lines) > max_lines:
        print(f"... ({len(lines) - max_lines} more lines)")
    print("\n")

preview_entry('Kara No/06_Abilities.json', 1, 30)
preview_entry('Kara No/06_Abilities.json', 2, 30)
preview_entry('Kara No/06_Abilities.json', 11, 30)

