with open('scratch/run_thai_pronoun_regression.py', 'r', encoding='utf-8') as f:
    text = f.read()

# Replace entry 1 checks with the deduplicated rule check
old_entry_1 = """        {
            "file": "Kara No/10_RP_Guide.json",
            "entry": "1",
            "must_contain": [
                'MALE CHARACTERS MUST NEVER REFER TO THEMSELVES AS "ฉัน"',
                'FEMALE CHARACTERS (Ryougi Shiki, Tohsaka Rin, Saber, Touko Aozaki, Azaka, Fujino, Sakura) MAY freely use "ฉัน"',
                'Natural Subject Omission (Zero-Anaphora)',
                '"ผม": Polite, gentle, reserved, or civilized male speakers',
                '"เรา": Casual, boyish, peer-level, or familiar masculine voice',
                '"ข้า": Archaic, legendary, imperious, martial, or ancient figures',
                'Mikiya consistently addresses Ryougi Shiki as "เธอ" or by name "ชิกิ", never casually addressing her as "นาย"'
            ]
        },
        {
            "file": "Kara No/10_RP_Guide.json",
            "entry": "8",
            "must_contain": [
                'Male characters MUST NEVER use "ฉัน" as a 1st-person self-reference',
                'Mikiya addresses Shiki/SHIKI as "เธอ" or "ชิกิ" (never "นาย")'
            ]
        },"""

new_entry_1 = """        {
            "file": "Kara No/10_RP_Guide.json",
            "entry": "1",
            "must_contain": [
                '4. Thai Dialogue & Pronoun Discipline: Strictly obey all masculine/feminine first-person and second-person pronoun laws defined in <RP_Global_Thai_Pronoun_Discipline_and_Register_Laws>',
                "male characters MUST NEVER use 'ฉัน'",
                "Mikiya always addresses Shiki/SHIKI as 'เธอ' or 'ชิกิ', never 'นาย'"
            ]
        },
        {
            "file": "Kara No/10_RP_Guide.json",
            "entry": "8",
            "must_contain": [
                "- In Thai roleplay, strictly enforce <RP_Global_Thai_Pronoun_Discipline_and_Register_Laws>",
                "Mikiya addresses Shiki/SHIKI as 'เธอ' or 'ชิกิ'"
            ]
        },"""

if old_entry_1 in text:
    text = text.replace(old_entry_1, new_entry_1)
    with open('scratch/run_thai_pronoun_regression.py', 'w', encoding='utf-8') as f:
        f.write(text)
    print("Updated run_thai_pronoun_regression.py!")
else:
    print("Pattern not matched!")

