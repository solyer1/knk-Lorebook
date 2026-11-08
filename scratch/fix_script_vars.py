with open('scratch/execute_master_patch.py', 'r', encoding='utf-8') as f:
    text = f.read()

# Fix p4, p6, p13 in apply_task_3
old_snippet = """    # 4. 04_Other_Characters.json: Fujou Kirie hospital & Kamekura Mitsuru book & Fujino analgesia
    with open(p4, 'r', encoding='utf-8') as f:
        d4 = json.load(f)"""

new_snippet = """    p4 = 'Kara No/04_Other_Characters.json'
    p6 = 'Kara No/06_Abilities.json'
    p13 = 'Kara No/13_Dialogue_Examples.json'
    # 4. 04_Other_Characters.json: Fujou Kirie hospital & Kamekura Mitsuru book & Fujino analgesia
    with open(p4, 'r', encoding='utf-8') as f:
        d4 = json.load(f)"""

text = text.replace(old_snippet, new_snippet)
with open('scratch/execute_master_patch.py', 'w', encoding='utf-8') as f:
    f.write(text)
print("Fixed variable definitions in execute_master_patch.py!")

