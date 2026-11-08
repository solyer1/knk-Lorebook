import json
import os
import sys

# Set stdout to UTF-8
if sys.platform == "win32":
    sys.stdout.reconfigure(encoding="utf-8")

print("=== Starting Constant & 'กู is allowed' Lorebook Enhancement ===")

THAI_GLOBAL_RULE_CONTENT = """<RP_Global_Thai_Pronoun_Discipline_and_Register_Laws>
[CRITICAL SYSTEM DIRECTIVE: THAI FIRST-PERSON PRONOUN LAWS]
This directive is permanent and applies to EVERY response generated in Thai.

1. ZERO TOLERANCE: MALE FIRST-PERSON "ฉัน" IS FORBIDDEN:
- In Thai dialogue, thoughts, and narration tags, MALE CHARACTERS MUST NEVER REFER TO THEMSELVES AS "ฉัน" (First-Person / สรรพนามบุรุษที่ 1).
- Never allow any male character (Mikiya, Shirou, SHIKI, Archer, Lancer, Gilgamesh, Araya, Lio, Alba, Tomoe, Shinji, etc.) to say "ฉัน". Using "ฉัน" for a male character breaks roleplay immersion.

2. "กู" IS FULLY ALLOWED AND NATURAL:
- "กู" (1st person) and "มึง" (2nd person) are 100% PERMITTED, VALID, and EXPECTED whenever male characters are:
  * Speaking roughly, aggressively, angrily, or with street delinquent attitudes (Shinji, delinquent Tomoe, street thugs).
  * Shouting, taunting, or clashing in combat (Lancer in battle, Gilgamesh enraged, combatants clashing).
  * In visceral predatory bloodlust (Awakened Shirazumi Lio).
  * Engaging in close, crude, or informal peer banter between close male companions or bitter rivals.
- NEVER sanitize or substitute rough male dialogue with "ฉัน"! Use "กู", zero-anaphora, or "ข้า" instead.

3. CHARACTER-APPROPRIATE MASCULINE FIRST-PERSON CHOICES:
- Zero-Anaphora (Omitted Subject): The #1 most natural default in Thai dialogue. Omit the pronoun completely when the action/verb makes the subject clear.
- "กู": Rough, angry, aggressive, vulgar, delinquent, combat taunts, or close informal banter. (FULLY ALLOWED)
- "ผม": Polite, gentle, civilized, respectful (Mikiya in daily life, Shirou to elders/seniors, Kurogiri, Alba's haughty affectation).
- "เรา": Casual, boyish, friendly peer (Shirou with Rin/classmates, SHIKI to Mikiya, Tomoe).
- "ข้า": Archaic, martial, heroic, proud, ancient figures (Lancer, Gilgamesh, Araya in solemn declarations).

4. FEMALE CHARACTERS FREELY USE "ฉัน":
- Female characters (Ryougi Shiki, Tohsaka Rin, Saber, Sakura Matou, Touko Aozaki, Azaka Kokutou, Fujino Asagami) MAY freely use "ฉัน" according to their character style.

5. PRESERVE ESTABLISHED SECOND-PERSON RULES:
- Mikiya addressing Shiki/SHIKI: Always "เธอ" or "ชิกิ", NEVER "นาย".
- SHIKI addressing Mikiya: May use "นาย".
- Shiki addressing Mikiya: Naturally calls him by name ("โคคุโตะ" / "มิกิยะ") or zero pronoun.
</RP_Global_Thai_Pronoun_Discipline_and_Register_Laws>"""

THAI_TRIGGER_KEYS = ["ฉัน", "ผม", "เรา", "ข้า", "กู", "นาย", "เธอ", "มึง", "ชิกิ", "มิกิยะ", "ชิโร่", "ริน", "เซเบอร์", "อาเชอร์", "แลนเซอร์", "ภาษาไทย", "สรรพนาม"]

# -------------------------------------------------------------------
# 1. Kara No/10_RP_Guide.json
# -------------------------------------------------------------------
rp_path = "Kara No/10_RP_Guide.json"
with open(rp_path, "r", encoding="utf-8") as f:
    rp_data = json.load(f)

# Make Entry 1 constant and non-selective
e1 = rp_data["entries"]["1"]
e1["constant"] = True
e1["selective"] = False
e1["disable"] = False
for k in THAI_TRIGGER_KEYS:
    if k not in e1["key"]:
        e1["key"].append(k)

# Update "กู" in Entry 1 content
old_c1 = e1["content"]
target_gu_1 = '4. "กู": Strictly for rough, vulgar, or feral predators (Awakened Shirazumi Lio hunting in the slaughterhouse, street delinquents).'
rep_gu_1 = '4. "กู": FULLY ALLOWED and natural. Use whenever speaking roughly, aggressively, angrily, in combat/taunts, delinquent mode, vulgar speech, or crude informal peer banter (pair with "มึง"). NEVER replace rough speech with "ฉัน"!'
if target_gu_1 in old_c1:
    e1["content"] = old_c1.replace(target_gu_1, rep_gu_1)
    print("✓ 10_RP_Guide.json [1] content 'กู' updated to fully allowed")

# Make Entry 8 constant and non-selective
e8 = rp_data["entries"]["8"]
e8["constant"] = True
e8["selective"] = False
e8["disable"] = False
for k in THAI_TRIGGER_KEYS:
    if k not in e8["key"]:
        e8["key"].append(k)

target_e8_rule = 'Male characters MUST NEVER use "ฉัน" as a 1st-person self-reference; assign character-appropriate registers ("ผม", "เรา", "ข้า", or natural zero-anaphora). Female characters may use "ฉัน" normally.'
rep_e8_rule = 'Male characters MUST NEVER use "ฉัน" as a 1st-person self-reference under any circumstances. "กู" is FULLY ALLOWED for rough, angry, fighting, delinquent, or crude banter. Female characters may use "ฉัน" normally.'
if target_e8_rule in e8["content"]:
    e8["content"] = e8["content"].replace(target_e8_rule, rep_e8_rule)
    print("✓ 10_RP_Guide.json [8] content 'กู' updated")

# Add dedicated constant Entry 9 to 10_RP_Guide.json
rp_data["entries"]["9"] = {
    "uid": 9,
    "name": "RP_Global_Thai_Pronoun_Discipline_and_Register_Laws",
    "comment": "RP_Global_Thai_Pronoun_Discipline_and_Register_Laws",
    "key": THAI_TRIGGER_KEYS,
    "keysecondary": [],
    "content": THAI_GLOBAL_RULE_CONTENT,
    "constant": True,
    "selective": False,
    "selectiveLogic": 0,
    "order": 99,
    "position": 0,
    "disable": False,
    "enabled": True,
    "ignoreBudget": False,
    "excludeRecursion": True,
    "preventRecursion": True,
    "probability": 100,
    "useProbability": True,
    "depth": 4,
    "displayIndex": 9
}
print("✓ 10_RP_Guide.json [9] dedicated constant Thai rule entry added")

with open(rp_path, "w", encoding="utf-8") as f:
    json.dump(rp_data, f, ensure_ascii=False, indent=2)

# -------------------------------------------------------------------
# 2. Fate/main_fate-stay-night.json and Fate/FATE SN RP.json
# -------------------------------------------------------------------
fate_files = ["Fate/main_fate-stay-night.json", "Fate/FATE SN RP.json"]
for fp in fate_files:
    if not os.path.exists(fp):
        continue
    with open(fp, "r", encoding="utf-8") as f:
        fd = json.load(f)

    # Determine new UID
    existing_uids = [int(v.get("uid", k)) for k, v in fd["entries"].items() if str(v.get("uid", k)).isdigit()]
    new_uid = max(existing_uids) + 1 if existing_uids else len(fd["entries"])
    new_key = str(new_uid)

    fd["entries"][new_key] = {
        "uid": new_uid,
        "name": "RP_Global_Thai_Pronoun_Discipline_and_Register_Laws",
        "comment": "RP_Global_Thai_Pronoun_Discipline_and_Register_Laws",
        "key": THAI_TRIGGER_KEYS,
        "keysecondary": [],
        "content": THAI_GLOBAL_RULE_CONTENT,
        "constant": True,
        "selective": False,
        "selectiveLogic": 0,
        "order": 99,
        "position": 0,
        "disable": False,
        "enabled": True,
        "ignoreBudget": False,
        "excludeRecursion": True,
        "preventRecursion": True,
        "probability": 100,
        "useProbability": True,
        "depth": 4,
        "displayIndex": new_uid
    }
    print(f"✓ {fp} added constant entry [{new_key}] with UID {new_uid}")

    # Add Thai keys and update "กู is allowed" in character entries
    # Shirou (5)
    if "5" in fd["entries"]:
        sh_entry = fd["entries"]["5"]
        for tk in ["ชิโร่", "เอมิยะ", "เอมิยะ ชิโร่"]:
            if tk not in sh_entry["key"]:
                sh_entry["key"].append(tk)
        sh_old = sh_entry["content"]
        target_sh_gu = '- Never use "ฉัน" for Shirou; "ฉัน" for male characters sounds stilted and unnatural in roleplay.'
        rep_sh_gu = '- "กู" is FULLY ALLOWED when Shirou is enraged, fighting desperately, or in heated conflict with enemies/Shinji.\n- Never use "ฉัน" for Shirou; "ฉัน" for male characters is strictly forbidden.'
        if target_sh_gu in sh_old:
            sh_entry["content"] = sh_old.replace(target_sh_gu, rep_sh_gu)

    # Archer (11)
    if "11" in fd["entries"]:
        ar_entry = fd["entries"]["11"]
        for tk in ["อาเชอร์", "เอมิยะ"]:
            if tk not in ar_entry["key"]:
                ar_entry["key"].append(tk)
        ar_old = ar_entry["content"]
        target_ar_gu = '- Never flatlines into generic polite "ผม" or stilted "ฉัน".'
        rep_ar_gu = '- Never flatlines into generic polite "ผม" or stilted "ฉัน" ("กู" is fully allowed when enraged or delivering blunt, aggressive contempt).'
        if target_ar_gu in ar_old:
            ar_entry["content"] = ar_old.replace(target_ar_gu, rep_ar_gu)

    # Lancer (13)
    if "13" in fd["entries"]:
        la_entry = fd["entries"]["13"]
        for tk in ["แลนเซอร์", "คูฮูลินน์"]:
            if tk not in la_entry["key"]:
                la_entry["key"].append(tk)
        la_old = la_entry["content"]
        target_la_gu = '- Never use "ฉัน" or overly polite "ผม" for Lancer.'
        rep_la_gu = '- "กู" is FULLY ALLOWED during combat, heated taunts, and rough warrior banter (pair with "มึง").\n- Never use "ฉัน" or overly polite "ผม" for Lancer.'
        if target_la_gu in la_old:
            la_entry["content"] = la_old.replace(target_la_gu, rep_la_gu)

    # Add Thai keys to Rin (6), Saber (7), Gilgamesh (14), Shinji (8)
    for cid, tkeys in [("6", ["ริน", "โทซากะ"]), ("7", ["เซเบอร์", "อาร์โทเรีย"]), ("14", ["กิลกาเมช", "กิล"]), ("8", ["ชินจิ", "มาโต้"])]:
        if cid in fd["entries"]:
            centry = fd["entries"][cid]
            for tk in tkeys:
                if tk not in centry["key"]:
                    centry["key"].append(tk)

    with open(fp, "w", encoding="utf-8") as f:
        json.dump(fd, f, ensure_ascii=False, indent=2)

# -------------------------------------------------------------------
# 3. Kara No/01_Shiki.json
# -------------------------------------------------------------------
shiki_path = "Kara No/01_Shiki.json"
with open(shiki_path, "r", encoding="utf-8") as f:
    shiki_data = json.load(f)

# Entry 0: Ryougi Shiki
e0 = shiki_data["entries"]["0"]
for tk in ["ชิกิ", "เรียวกิ", "เรียวกิ ชิกิ"]:
    if tk not in e0["key"]:
        e0["key"].append(tk)

# Entry 1: SHIKI
e1 = shiki_data["entries"]["1"]
for tk in ["ชิกิ", "ชิกิชาย", "ชิกิ (織)"]:
    if tk not in e1["key"]:
        e1["key"].append(tk)
old_s1 = e1["content"]
target_s1_gu = 'avoid "ผม" (too polite/formal for his boyish demeanor).'
rep_s1_gu = 'avoid "ผม" (too polite/formal for his boyish demeanor); "กู" is fully allowed when speaking roughly, playfully aggressive, or with delinquent edge.'
if target_s1_gu in old_s1:
    e1["content"] = old_s1.replace(target_s1_gu, rep_s1_gu)
    print("✓ 01_Shiki.json [1] updated with 'กู is allowed'")

# Entry 4: Shiki_Roleplay_Rules
e4 = shiki_data["entries"]["4"]
for tk in ["ชิกิ", "เรียวกิ ชิกิ"]:
    if tk not in e4["key"]:
        e4["key"].append(tk)

with open(shiki_path, "w", encoding="utf-8") as f:
    json.dump(shiki_data, f, ensure_ascii=False, indent=2)

# -------------------------------------------------------------------
# 4. Kara No/02_Mikiya.json
# -------------------------------------------------------------------
mikiya_path = "Kara No/02_Mikiya.json"
with open(mikiya_path, "r", encoding="utf-8") as f:
    mikiya_data = json.load(f)

for eid in ["0", "3", "4"]:
    if eid in mikiya_data["entries"]:
        me = mikiya_data["entries"][eid]
        for tk in ["มิกิยะ", "โคคุโตะ", "โคคุโตะ มิกิยะ"]:
            if tk not in me["key"]:
                me["key"].append(tk)
print("✓ 02_Mikiya.json Thai keys added")

with open(mikiya_path, "w", encoding="utf-8") as f:
    json.dump(mikiya_data, f, ensure_ascii=False, indent=2)

# -------------------------------------------------------------------
# 5. Kara No/04_Other_Characters.json
# -------------------------------------------------------------------
other_path = "Kara No/04_Other_Characters.json"
with open(other_path, "r", encoding="utf-8") as f:
    other_data = json.load(f)

# Araya (0)
if "0" in other_data["entries"]:
    oe0 = other_data["entries"]["0"]
    for tk in ["อารายะ", "โซเร็น", "อารายะ โซเร็น"]:
        if tk not in oe0["key"]:
            oe0["key"].append(tk)

# Alba (3)
if "3" in other_data["entries"]:
    oe3 = other_data["entries"]["3"]
    for tk in ["อัลบา", "คอร์เนเลียส"]:
        if tk not in oe3["key"]:
            oe3["key"].append(tk)

# Lio (4)
if "4" in other_data["entries"]:
    oe4 = other_data["entries"]["4"]
    for tk in ["ริโอ", "ชิราซุมิ", "ชิราซุมิ ริโอ"]:
        if tk not in oe4["key"]:
            oe4["key"].append(tk)
    old_lio = oe4["content"]
    target_lio_gu = 'rough forms ("กู") during predatory bloodlust. Never use "ฉัน".'
    rep_lio_gu = '"กู" is FULLY ALLOWED and expected during his predatory bloodlust and violent mania. Male characters must NEVER use "ฉัน".'
    if target_lio_gu in old_lio:
        oe4["content"] = old_lio.replace(target_lio_gu, rep_lio_gu)
        print("✓ 04_Other_Characters.json [4] Lio 'กู' reinforced")

# Tomoe (6)
if "6" in other_data["entries"]:
    oe6 = other_data["entries"]["6"]
    for tk in ["โทโมเอะ", "เอ็นโจ", "เอ็นโจ โทโมเอะ"]:
        if tk not in oe6["key"]:
            oe6["key"].append(tk)
    old_tomoe = oe6["content"]
    target_tomoe_gu = 'hesitant/polite "ผม" when speaking to Shiki or adults.'
    rep_tomoe_gu = 'hesitant/polite "ผม" when speaking to Shiki or adults; "กู" is fully allowed when speaking with street delinquents or in desperate defensive anger.'
    if target_tomoe_gu in old_tomoe:
        oe6["content"] = old_tomoe.replace(target_tomoe_gu, rep_tomoe_gu)
        print("✓ 04_Other_Characters.json [6] Tomoe 'กู' updated")

# Kurogiri (7)
if "7" in other_data["entries"]:
    oe7 = other_data["entries"]["7"]
    for tk in ["คุโรกิริ", "ซัตสึกิ"]:
        if tk not in oe7["key"]:
            oe7["key"].append(tk)

with open(other_path, "w", encoding="utf-8") as f:
    json.dump(other_data, f, ensure_ascii=False, indent=2)

# -------------------------------------------------------------------
# 6. Kara No/05_Relationships.json
# -------------------------------------------------------------------
rel_path = "Kara No/05_Relationships.json"
with open(rel_path, "r", encoding="utf-8") as f:
    rel_data = json.load(f)

re0 = rel_data["entries"]["0"]
for tk in ["ชิกิ", "มิกิยะ"]:
    if tk not in re0["key"]:
        re0["key"].append(tk)
old_re0 = re0["content"]
target_re0_gu = 'Male SHIKI uses boyish "เรา" or natural zero-anaphora (never "ฉัน", never formal "ผม").'
rep_re0_gu = 'Male SHIKI uses boyish "เรา" or natural zero-anaphora ("กู" is allowed when rough/playfully aggressive; never "ฉัน", never formal "ผม").'
if target_re0_gu in old_re0:
    re0["content"] = old_re0.replace(target_re0_gu, rep_re0_gu)
    print("✓ 05_Relationships.json [0] updated with 'กู is allowed'")

with open(rel_path, "w", encoding="utf-8") as f:
    json.dump(rel_data, f, ensure_ascii=False, indent=2)

# -------------------------------------------------------------------
# 7. Kara No/011_Fate_Integration.json
# -------------------------------------------------------------------
fate_int_path = "Kara No/011_Fate_Integration.json"
with open(fate_int_path, "r", encoding="utf-8") as f:
    fate_int_data = json.load(f)

# Shirou (3)
if "3" in fate_int_data["entries"]:
    fe3 = fate_int_data["entries"]["3"]
    for tk in ["ชิโร่", "เอมิยะ", "ชิกิ"]:
        if tk not in fe3["key"]:
            fe3["key"].append(tk)
    old_fe3 = fe3["content"]
    target_fe3_gu = 'polite "ผม" when speaking to Touko or elder magi.'
    rep_fe3_gu = 'polite "ผม" when speaking to Touko or elder magi ("กู" is fully allowed when enraged, fighting, or in extreme clashes; never "ฉัน").'
    if target_fe3_gu in old_fe3:
        fe3["content"] = old_fe3.replace(target_fe3_gu, rep_fe3_gu)

# Archer (6)
if "6" in fate_int_data["entries"]:
    fe6 = fate_int_data["entries"]["6"]
    for tk in ["อาเชอร์", "เอมิยะ", "ชิกิ"]:
        if tk not in fe6["key"]:
            fe6["key"].append(tk)
    old_fe6 = fe6["content"]
    target_fe6_gu = 'worldly weariness.'
    rep_fe6_gu = 'worldly weariness ("กู" is fully allowed during ferocious combat clashes or contemptuous fury; never "ฉัน").'
    if target_fe6_gu in old_fe6:
        fe6["content"] = old_fe6.replace(target_fe6_gu, rep_fe6_gu)

with open(fate_int_path, "w", encoding="utf-8") as f:
    json.dump(fate_int_data, f, ensure_ascii=False, indent=2)

# -------------------------------------------------------------------
# 8. Kara No/16_Everyday_Life_and_Personal_Details.json
# -------------------------------------------------------------------
ed_path = "Kara No/16_Everyday_Life_and_Personal_Details.json"
with open(ed_path, "r", encoding="utf-8") as f:
    ed_data = json.load(f)

# Add Thai keys to entries
key_map = {
    "1": ["มิกิยะ", "โคคุโตะ"],
    "3": ["ชิกิ", "ชิกิชาย"],
    "7": ["อารายะ", "โซเร็น"],
    "8": ["อัลบา"],
    "9": ["ริโอ", "ชิราซุมิ"],
    "10": ["โทโมเอะ", "เอ็นโจ"],
    "12": ["คุโรกิริ"],
    "15": ["ชิโร่", "เอมิยะ"],
    "17": ["อาเชอร์", "เอมิยะ"]
}
for k_id, t_keys in key_map.items():
    if k_id in ed_data["entries"]:
        entry = ed_data["entries"][k_id]
        for tk in t_keys:
            if tk not in entry["key"]:
                entry["key"].append(tk)

# Entry 9 (Lio)
if "9" in ed_data["entries"]:
    ed9 = ed_data["entries"]["9"]
    old_ed9 = ed9["content"]
    target_ed9_gu = 'vulgar/rough forms ("กู") during bloodlust [CANON].'
    rep_ed9_gu = '"กู" is FULLY ALLOWED and expected during his predatory bloodlust; never "ฉัน" [CANON].'
    if target_ed9_gu in old_ed9:
        ed9["content"] = old_ed9.replace(target_ed9_gu, rep_ed9_gu)

# Entry 10 (Tomoe)
if "10" in ed_data["entries"]:
    ed10 = ed_data["entries"]["10"]
    old_ed10 = ed10["content"]
    target_ed10_gu = 'hesitant "ผม" with adults or Shiki [CANON].'
    rep_ed10_gu = 'hesitant "ผม" with adults or Shiki ("กู" is fully allowed with delinquent peers or in anger; never "ฉัน") [CANON].'
    if target_ed10_gu in old_ed10:
        ed10["content"] = old_ed10.replace(target_ed10_gu, rep_ed10_gu)

print("✓ 16_Everyday_Life_and_Personal_Details.json updated with Thai keys and 'กู is allowed'")

with open(ed_path, "w", encoding="utf-8") as f:
    json.dump(ed_data, f, ensure_ascii=False, indent=2)

print("=== Constant & 'กู is allowed' Lorebook Enhancement Completed Successfully ===")
