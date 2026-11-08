import json
import difflib

# Let's inspect 01_Shiki.json user changes
print("==================================================")
print("DETAILED USER CHANGES IN 01_Shiki.json")
print("==================================================")

with open('Kara No/01_Shiki.json', 'r', encoding='utf-8') as f:
    s_curr = json.load(f)
with open('scratch/backups_thai_constant_and_gu_20261026/01_Shiki.json', 'r', encoding='utf-8') as f:
    s_bak = json.load(f)

for k in ["0", "4", "5", "6"]:
    e_curr = s_curr['entries'][k]
    e_bak = s_bak['entries'][k]
    print(f"\n--- Entry {k}: {e_curr.get('comment')} ---")
    c_curr = e_curr['content']
    c_bak = e_bak['content']
    
    diff = list(difflib.unified_diff(c_bak.splitlines(), c_curr.splitlines(), lineterm=""))
    for l in diff:
        if l.startswith("+") and not l.startswith("+++"):
            print("  [ADDED]", l[1:].strip())
        elif l.startswith("-") and not l.startswith("---"):
            print("  [REMOVED]", l[1:].strip())

print("\n==================================================")
print("DETAILED USER CHANGES IN 02_Mikiya.json")
print("==================================================")

with open('Kara No/02_Mikiya.json', 'r', encoding='utf-8') as f:
    m_curr = json.load(f)
with open('scratch/backups_thai_constant_and_gu_20261026/02_Mikiya.json', 'r', encoding='utf-8') as f:
    m_bak = json.load(f)

for k in ["4", "5"]:
    e_curr = m_curr['entries'][k]
    e_bak = m_bak['entries'][k]
    print(f"\n--- Entry {k}: {e_curr.get('comment')} ---")
    c_curr = e_curr['content']
    c_bak = e_bak['content']
    
    diff = list(difflib.unified_diff(c_bak.splitlines(), c_curr.splitlines(), lineterm=""))
    for l in diff:
        if l.startswith("+") and not l.startswith("+++"):
            print("  [ADDED]", l[1:].strip())
        elif l.startswith("-") and not l.startswith("---"):
            print("  [REMOVED]", l[1:].strip())

