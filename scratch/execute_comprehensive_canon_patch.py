import json
import os
import re

def move_closing_tag_to_end(content, tag_name):
    """Ensures </tag_name> is removed from the middle and placed cleanly at the very end of content."""
    close_tag = f"</{tag_name}>"
    if close_tag in content:
        content = content.replace(close_tag, "")
    content = content.strip() + "\n" + close_tag
    return content

def patch_03_touko():
    p = 'Kara No/03_Touko.json'
    with open(p, 'r', encoding='utf-8') as f:
        d = json.load(f)

    # uid 0: cigarette wording
    c0 = d['entries']['0']['content']
    c0 = c0.replace(
        "her preferred imported brands: Dragonfly (Dragonfly cigarettes) or Sobranie Cocktail.",
        "her imported cigarettes (frequently referenced in roleplay traditions as Sobranie or Dragonfly)."
    )
    d['entries']['0']['content'] = c0

    # uid 3: delete molecular block, fix Sobranie, move tag
    c3 = d['entries']['3']['content']
    # delete [MOLECULAR HOMOLOGY IN GRAND PUPPET CELLULAR ARCHITECTURE]
    mol_idx = c3.find("[MOLECULAR HOMOLOGY IN GRAND PUPPET CELLULAR ARCHITECTURE]")
    if mol_idx != -1:
        # find the end or trailing
        c3 = c3[:mol_idx].rstrip()
    c3 = c3.replace("fresh pack of Sobranie cigarettes.", "fresh pack of imported cigarettes.")
    c3 = move_closing_tag_to_end(c3, "Touko_Magecraft_and_Puppetry")
    d['entries']['3']['content'] = c3

    # uid 4: fix prosthetic arm origin, move tag
    c4 = d['entries']['4']['content']
    old_arm = "When Shiki sacrificed her biological left arm during the battle against the wraiths at Fujou Building (Overlooking View), Touko designed, constructed, and surgically attached a custom-engineered puppet prosthetic arm."
    new_arm = "When Shiki lost her biological left arm against Asagami Fujino's Mystic Eyes of Distortion on the Broad Bridge in late July 1998 (Remaining Sense of Pain), Touko designed, constructed, and surgically attached a custom-engineered puppet prosthetic arm, which Shiki subsequently used (and had destroyed and rebuilt) against Kirie Fujou's wraiths at the Fujou Building in September 1998 (Overlooking View)."
    if old_arm in c4:
        c4 = c4.replace(old_arm, new_arm)
    c4 = move_closing_tag_to_end(c4, "Touko_and_Shiki")
    d['entries']['4']['content'] = c4

    # uid 9: delete rune plasma block, move tag
    c9 = d['entries']['9']['content']
    rune_idx = c9.find("[RUNE PLASMA KINETICS & GLOOM BEAST ETHER DENSITY]")
    if rune_idx != -1:
        c9 = c9[:rune_idx].rstrip()
    c9 = move_closing_tag_to_end(c9, "Touko_Combat_Arsenal_and_Familiar")
    d['entries']['9']['content'] = c9

    # uid 10: cigarette wording
    c10 = d['entries']['10']['content']
    c10 = c10.replace("chain-smoking Dragonfly cigarettes", "chain-smoking imported cigarettes")
    d['entries']['10']['content'] = c10

    with open(p, 'w', encoding='utf-8') as f:
        json.dump(d, f, indent=2, ensure_ascii=False)
    print("03_Touko.json patched successfully!")

def patch_16_everyday():
    p = 'Kara No/16_Everyday_Life_and_Personal_Details.json'
    with open(p, 'r', encoding='utf-8') as f:
        d = json.load(f)

    # uid 0: delete [MICROSCOPIC TEXTILES...], fix hospital, move tag
    c0 = d['entries']['0']['content']
    idx0 = c0.find("[MICROSCOPIC TEXTILES & TACTILE THERMAL SENSITIVITY]")
    if idx0 != -1:
        c0 = c0[:idx0].rstrip()
    c0 = c0.replace(
        "* Coma (1996–1998): Standard white hospital gown in Yagami Hospital Room 404 [CANON].",
        "* Coma (1996–1998): Standard white hospital gown in the suburban hospital's third-floor private room [CANON - NOVEL CHAPTER 4]."
    )
    c0 = move_closing_tag_to_end(c0, "Everyday_Ryougi_Shiki_Domestic_and_Wardrobe")
    d['entries']['0']['content'] = c0

    # uid 1: move tag
    c1 = d['entries']['1']['content']
    c1 = move_closing_tag_to_end(c1, "Everyday_Kokutou_Mikiya_Habits_and_Domesticity")
    d['entries']['1']['content'] = c1

    # uid 2: delete [CHEMICAL PYROLYSIS...], move tag
    c2 = d['entries']['2']['content']
    idx2 = c2.find("[CHEMICAL PYROLYSIS & TOBACCO ALKALOID AEROSOLS]")
    if idx2 != -1:
        c2 = c2[:idx2].rstrip()
    c2 = move_closing_tag_to_end(c2, "Everyday_Aozaki_Touko_Workshop_and_Vices")
    d['entries']['2']['content'] = c2

    # uid 4: move tag
    c4 = d['entries']['4']['content']
    c4 = move_closing_tag_to_end(c4, "Everyday_Void_Shiki_Root_Elegance")
    d['entries']['4']['content'] = c4

    # uid 5: move tag
    c5 = d['entries']['5']['content']
    c5 = move_closing_tag_to_end(c5, "Everyday_Kokutou_Azaka_Boarding_School_and_Brother")
    d['entries']['5']['content'] = c5

    # uid 6: delete [MICRO-NOCICEPTION...], move tag
    c6 = d['entries']['6']['content']
    idx6 = c6.find("[MICRO-NOCICEPTION & CUTANEOUS SENSORY RE-INNERVATION]")
    if idx6 != -1:
        c6 = c6[:idx6].rstrip()
    c6 = move_closing_tag_to_end(c6, "Everyday_Asagami_Fujino_Poise_and_Sensory_Recovery")
    d['entries']['6']['content'] = c6

    # uid 9: delete [MICRO-OLFACTORY...], move tag
    c9 = d['entries']['9']['content']
    idx9 = c9.find("[MICRO-OLFACTORY PARSING & CHEMICAL VOLATILITY]")
    if idx9 != -1:
        c9 = c9[:idx9].rstrip()
    c9 = move_closing_tag_to_end(c9, "Everyday_Shirazumi_Lio_Predator_Reality")
    d['entries']['9']['content'] = c9

    # Reassign orders 140 to 157 for uid 0 to 17
    for i in range(18):
        uid_str = str(i)
        if uid_str in d['entries']:
            d['entries'][uid_str]['order'] = 140 + i

    with open(p, 'w', encoding='utf-8') as f:
        json.dump(d, f, indent=2, ensure_ascii=False)
    print("16_Everyday_Life_and_Personal_Details.json patched successfully!")

def patch_shiki():
    targets = [
        ('Kara No/archive/01_Shiki_Expansion.json', '2', 50000),
        ('Kara No/01_Shiki.json', '7', None)
    ]
    for path, entry_id, token_budget in targets:
        if not os.path.exists(path):
            continue
        with open(path, 'r', encoding='utf-8') as f:
            d = json.load(f)
        if token_budget:
            d['token_budget'] = token_budget
        
        c = d['entries'][entry_id]['content']
        old_str = "In February 1999, after killing Lio Shirazumi to save Mikiya, she bears the permanent moral weight of having taken a human life, losing sight in her left eye."
        new_str = "In February 1999, after killing Lio Shirazumi to save Mikiya—who permanently lost sight in his own left eye while protecting her humanity—she bears the permanent moral weight of having taken a human life."
        if old_str in c:
            c = c.replace(old_str, new_str)
        c = c.replace("Her body sleeps in Yagami Hospital", "Her body sleeps in the suburban hospital's third-floor private room")
        d['entries'][entry_id]['content'] = c

        # In 01_Shiki.json, check uid 3 hospital room 404 and closing tags
        if path == 'Kara No/01_Shiki.json':
            c3 = d['entries']['3']['content']
            c3 = c3.replace("pitch-black darkness of hospital room 404 in June 1998", "pitch-black darkness of the suburban hospital's third-floor private room in June 1998")
            d['entries']['3']['content'] = c3
            # move closing tags on 0, 2, 3, 7
            for u in ['0', '2', '3', '7']:
                tag = d['entries'][u].get('name') or d['entries'][u].get('comment')
                d['entries'][u]['content'] = move_closing_tag_to_end(d['entries'][u]['content'], tag)

        with open(path, 'w', encoding='utf-8') as f:
            json.dump(d, f, indent=2, ensure_ascii=False)
        print(f"{path} patched successfully!")

def patch_abilities():
    targets = [
        ('Kara No/archive/06_Abilities_Expansion.json', '0', 50000),
        ('Kara No/06_Abilities.json', '13', None)
    ]
    for path, entry_id, token_budget in targets:
        if not os.path.exists(path):
            continue
        with open(path, 'r', encoding='utf-8') as f:
            d = json.load(f)
        if token_budget:
            d['token_budget'] = token_budget

        entry = d['entries'][entry_id]
        # Replace key
        if 'key' in entry and isinstance(entry['key'], list):
            entry['key'] = ["Godword Mayday" if k == "Sadamitsu Matsuguruma" else k for k in entry['key']]
        
        # Replace content
        c = entry['content']
        c = c.replace(
            "Possessed by magus Kurogiri Satsuki (real name Sadamitsu Matsuguruma)",
            "Possessed by Welsh magus Kurogiri Satsuki (known at the Clock Tower as 'Godword Mayday')"
        )
        entry['content'] = c

        if path == 'Kara No/06_Abilities.json':
            # Remove "baryonic mass" from entry 11
            c11 = d['entries']['11']['content']
            c11 = c11.replace("lacking baryonic mass", "lacking physical mass")
            d['entries']['11']['content'] = c11

            # Fix closing tags for 1, 2, 6, 7, 10, 11, 13, 15
            for u in ['1', '2', '6', '7', '10', '11', '13', '15']:
                tag = d['entries'][u].get('name') or d['entries'][u].get('comment')
                d['entries'][u]['content'] = move_closing_tag_to_end(d['entries'][u]['content'], tag)

        with open(path, 'w', encoding='utf-8') as f:
            json.dump(d, f, indent=2, ensure_ascii=False)
        print(f"{path} patched successfully!")

def patch_relationships():
    targets = [
        ('Kara No/archive/05_Relationships_Expansion.json', '0', 50000),
        ('Kara No/05_Relationships.json', '6', None)
    ]
    for path, entry_id, token_budget in targets:
        if not os.path.exists(path):
            continue
        with open(path, 'r', encoding='utf-8') as f:
            d = json.load(f)
        if token_budget:
            d['token_budget'] = token_budget
        
        c = d['entries'][entry_id]['content']
        c = c.replace("Shiki's body sleeps unresponsive in Yagami Hospital", "Shiki's body sleeps unresponsive in the suburban hospital's third-floor private room")
        d['entries'][entry_id]['content'] = c

        with open(path, 'w', encoding='utf-8') as f:
            json.dump(d, f, indent=2, ensure_ascii=False)
        print(f"{path} patched successfully!")

def patch_world():
    targets = [
        ('Kara No/archive/08_World_Expansion.json', '0', 50000),
        ('Kara No/08_World.json', '9', None)
    ]
    for path, entry_id, token_budget in targets:
        if not os.path.exists(path):
            continue
        with open(path, 'r', encoding='utf-8') as f:
            d = json.load(f)
        if token_budget:
            d['token_budget'] = token_budget

        c = d['entries'][entry_id]['content']
        c = c.replace("leading to his self-sacrifice in February 1996.", "leading to his self-sacrifice in early March 1996 (March 5, 1996).")
        d['entries'][entry_id]['content'] = c

        with open(path, 'w', encoding='utf-8') as f:
            json.dump(d, f, indent=2, ensure_ascii=False)
        print(f"{path} patched successfully!")

def patch_mikiya():
    # 02_Mikiya_Expansion
    p_exp = 'Kara No/archive/02_Mikiya_Expansion.json'
    if os.path.exists(p_exp):
        with open(p_exp, 'r', encoding='utf-8') as f:
            d = json.load(f)
        d['token_budget'] = 50000
        with open(p_exp, 'w', encoding='utf-8') as f:
            json.dump(d, f, indent=2, ensure_ascii=False)
        print(f"{p_exp} token budget set to 50000!")

    # 02_Mikiya.json closing tag on uid 3
    p_main = 'Kara No/02_Mikiya.json'
    if os.path.exists(p_main):
        with open(p_main, 'r', encoding='utf-8') as f:
            d = json.load(f)
        tag = d['entries']['3'].get('name') or d['entries']['3'].get('comment')
        d['entries']['3']['content'] = move_closing_tag_to_end(d['entries']['3']['content'], tag)
        with open(p_main, 'w', encoding='utf-8') as f:
            json.dump(d, f, indent=2, ensure_ascii=False)
        print(f"{p_main} uid 3 closing tag moved!")

def patch_touko_expansion():
    p = 'Kara No/archive/03_Touko_Expansion.json'
    if os.path.exists(p):
        with open(p, 'r', encoding='utf-8') as f:
            d = json.load(f)
        for k in ['0', '1', '2']:
            if k in d['entries']:
                d['entries'][k]['disable'] = True
        with open(p, 'w', encoding='utf-8') as f:
            json.dump(d, f, indent=2, ensure_ascii=False)
        print("03_Touko_Expansion entries disabled!")

def patch_rp_guide():
    p = 'Kara No/10_RP_Guide.json'
    with open(p, 'r', encoding='utf-8') as f:
        d = json.load(f)

    # uid 1: replace long sub-list under 4. Thai Dialogue & Pronoun Discipline:
    c1 = d['entries']['1']['content']
    pattern1 = r'4\. Thai Dialogue & Pronoun Discipline:.*?(?=\n\n|\Z)'
    replacement1 = "4. Thai Dialogue & Pronoun Discipline: Strictly obey all masculine/feminine first-person and second-person pronoun laws defined in <RP_Global_Thai_Pronoun_Discipline_and_Register_Laws> (male characters MUST NEVER use 'ฉัน'; 'กู' is fully allowed for rough/combat speech; Mikiya always addresses Shiki/SHIKI as 'เธอ' or 'ชิกิ', never 'นาย')."
    c1 = re.sub(pattern1, replacement1, c1, flags=re.DOTALL)
    d['entries']['1']['content'] = c1

    # uid 8: replace sub-bullets under - In Thai roleplay, preserve canonical pronoun discipline:
    c8 = d['entries']['8']['content']
    pattern8 = r'- In Thai roleplay, preserve canonical pronoun discipline:.*?(?=</RP_Strict_Guardrails_User_Agency>|\Z)'
    replacement8 = "- In Thai roleplay, strictly enforce <RP_Global_Thai_Pronoun_Discipline_and_Register_Laws> (zero tolerance for male 'ฉัน'; Mikiya addresses Shiki/SHIKI as 'เธอ' or 'ชิกิ').\n"
    c8 = re.sub(pattern8, replacement8, c8, flags=re.DOTALL)
    c8 = move_closing_tag_to_end(c8, "RP_Strict_Guardrails_User_Agency")
    d['entries']['8']['content'] = c8

    with open(p, 'w', encoding='utf-8') as f:
        json.dump(d, f, indent=2, ensure_ascii=False)
    print("10_RP_Guide.json patched successfully!")

def patch_locations_timeline_fog():
    # 07_Locations.json
    p_loc = 'Kara No/07_Locations.json'
    with open(p_loc, 'r', encoding='utf-8') as f:
        d_loc = json.load(f)
    e8 = d_loc['entries']['8']
    e8['name'] = "Location_Suburban_General_Hospital"
    e8['comment'] = "Location_Suburban_General_Hospital"
    e8['key'] = ["Suburban General Hospital", "hospital", "clinic", "ward", "Doctor Ashika", "Dr. Araya"]
    e8['content'] = """<Location_Suburban_General_Hospital>
Suburban General Hospital (郊外の総合病院). The medical facility where Shiki was hospitalized for two years (1996–1998) during her coma, and the primary setting of The Hollow Shrine (Chapter 4).
A quiet, slightly dated regional hospital on the suburban edge of Mifune. Because of the Ryougi family's influence and funding, Shiki was placed in a secluded private room on the third floor away from public patient wards.
- Third-Floor Private Ward: A quiet corner room on the third floor with pale walls, a mechanical hospital bed, an IV drip stand, a nightstand holding a glass vase, and a large window overlooking the quiet residential suburbs and distant mountain treeline.
Ideal for convalescence scenes, emotional visits between Mikiya and Shiki, medical examinations of occult injuries by Touko, or horror scenes involving spectral hospital hauntings.
</Location_Suburban_General_Hospital>"""
    with open(p_loc, 'w', encoding='utf-8') as f:
        json.dump(d_loc, f, indent=2, ensure_ascii=False)
    print("07_Locations.json patched successfully!")

    # 09_Timeline.json
    p_time = 'Kara No/09_Timeline.json'
    with open(p_time, 'r', encoding='utf-8') as f:
        d_time = json.load(f)
    for k, v in d_time['entries'].items():
        c = v['content']
        c = c.replace("2-year hospital coma in Room 404", "2-year coma in the suburban hospital's third-floor private room")
        c = c.replace("rushed to Yagami General Hospital. Surgeons stabilize her biological body, but she falls into an unbroken vegetative coma in Room 404.", "rushed to the suburban hospital. Surgeons stabilize her biological body, but she falls into an unbroken vegetative coma in the third-floor private room.")
        c = c.replace("fresh seasonal flowers to Room 404", "fresh seasonal flowers to her third-floor hospital room")
        c = c.replace("opens her eyes in Room 404 of Yagami General Hospital", "opens her eyes in the third-floor private room of the suburban hospital")
        c = c.replace("Aozaki Touko visits Room 404", "Aozaki Touko visits Shiki's hospital room")
        c = c.replace("3. JUNE 20, 1998: THE NIGHT BATTLE OF ROOM 404:", "3. JUNE 20, 1998: THE NIGHT BATTLE IN THE THIRD-FLOOR HOSPITAL ROOM:")
        c = c.replace("invade Room 404", "invade the third-floor private room")
        c = c.replace("terminal ward of Yagami General Hospital", "terminal ward of the suburban hospital")
        tag = v.get('name') or v.get('comment')
        v['content'] = move_closing_tag_to_end(c, tag)
    with open(p_time, 'w', encoding='utf-8') as f:
        json.dump(d_time, f, indent=2, ensure_ascii=False)
    print("09_Timeline.json patched successfully!")

    # 15_Chapter_Knowledge_Fog_of_War.json
    p_fog = 'Kara No/15_Chapter_Knowledge_Fog_of_War.json'
    with open(p_fog, 'r', encoding='utf-8') as f:
        d_fog = json.load(f)
    for k, v in d_fog['entries'].items():
        c = v['content']
        c = c.replace("Yagami General Hospital", "the suburban hospital")
        c = c.replace("Yagami Hospital", "the suburban hospital")
        c = c.replace("Sadamitsu Matsuguruma", "known at the Clock Tower as 'Godword Mayday'")
        v['content'] = c
    with open(p_fog, 'w', encoding='utf-8') as f:
        json.dump(d_fog, f, indent=2, ensure_ascii=False)
    print("15_Chapter_Knowledge_Fog_of_War.json patched successfully!")

    # 04_Other_Characters.json closing tags
    p_04 = 'Kara No/04_Other_Characters.json'
    with open(p_04, 'r', encoding='utf-8') as f:
        d_04 = json.load(f)
    for k, v in d_04['entries'].items():
        tag = v.get('name') or v.get('comment')
        v['content'] = move_closing_tag_to_end(v['content'], tag)
    with open(p_04, 'w', encoding='utf-8') as f:
        json.dump(d_04, f, indent=2, ensure_ascii=False)
    print("04_Other_Characters.json closing tags moved successfully!")

if __name__ == '__main__':
    patch_03_touko()
    patch_16_everyday()
    patch_shiki()
    patch_abilities()
    patch_relationships()
    patch_world()
    patch_mikiya()
    patch_touko_expansion()
    patch_rp_guide()
    patch_locations_timeline_fog()
    print("ALL PATCHES APPLIED!")

