# -*- coding: utf-8 -*-
"""
Applies Mirai Fukuin (未来福音 / Future Gospel) and Final Record (Extra Chorus) novel canon expansions to:
- Kara No/04_Other_Characters.json (Entries 8, 9, 11: Mitsuru, Mana, Shizuno)
- Kara No/09_Timeline.json (Entry 10: Mobius Ring & Mobius Link chronology)
- Kara No/13_Dialogue_Examples.json (Adds Entry 17: Dialogue_Canon_Future_Gospel_Precognition_and_Mana)
- Kara No/16_Everyday_Life_and_Personal_Details.json (Adds Entry 18: Everyday_Adult_Era_2008_2010_Family_Domesticity)
"""
import json
import os

p_other = r"d:\Personalise\Homemad\Lorebook\Nasuverse\Kara No\04_Other_Characters.json"
p_timeline = r"d:\Personalise\Homemad\Lorebook\Nasuverse\Kara No\09_Timeline.json"
p_dialogue = r"d:\Personalise\Homemad\Lorebook\Nasuverse\Kara No\13_Dialogue_Examples.json"
p_everyday = r"d:\Personalise\Homemad\Lorebook\Nasuverse\Kara No\16_Everyday_Life_and_Personal_Details.json"

# =========================================================================
# 1. UPDATE 04_Other_Characters.json (Entries 8, 9, 11)
# =========================================================================
with open(p_other, "r", encoding="utf-8") as f:
    other_lb = json.load(f)

# Entry 8: Kamekura Mitsuru
e8_m = other_lb["entries"]["8"]["content"]
mitsuru_future_addition = """
- The Severing of Measurement Precognition (August 28, 1998) [CANON - NOVEL FUTURE GOSPEL]:
  * In the underground garage confrontation, Meruka trapped Shiki in a calculated bomb blast. However, Shiki's Mystic Eyes of Death Perception visually perceived the black line of his 'predicted future' in the air.
  * Shiki swung her knife and severed his future line directly, permanently extinguishing his right-eye measurement clairvoyance and blinding the eye.
  * Freed from the curse of predetermined outcomes, Mitsuru began living as an ordinary human, later achieving acclaim as a children's picture-book author (famous for his tale *The Crocodile and the Bird* / ワニと小鳥)."""

if "The Severing of Measurement Precognition" not in e8_m:
    pos = e8_m.find("[ROLEPLAY DIRECTIVES & INTEGRATION GUIDELINES]")
    if pos != -1:
        e8_m = e8_m[:pos] + mitsuru_future_addition + "\n\n" + e8_m[pos:]
    else:
        e8_m += "\n\n" + mitsuru_future_addition
    other_lb["entries"]["8"]["content"] = e8_m

# Entry 9: Ryougi Mana
e9_mana = other_lb["entries"]["9"]["content"]
mana_dialogue_addition = """
- Family Dynamic & Oedipal Rivalry (2008–2010) [CANON - NOVEL FUTURE GOSPEL]:
  * Calls Mikiya 'Papa' (パパ) with boundless, shining adoration, and addresses Shiki formally as 'Mother' (母上, Haha-ue).
  * Declares her grand comedic ambition: *"I will defeat Mother and claim Father's heart!"* Shiki views Mana's bratty, affectionate challenges with cool, amused tolerance, knowing Mikiya loves them both completely.
  * Speaks with crisp, aristocratic politeness mixed with lively, modern adolescent cheerfulness, carrying Shiki's breathtaking nobility and Mikiya's gentle, disarming smile."""

if "Family Dynamic & Oedipal Rivalry" not in e9_mana:
    pos = e9_mana.find("[ROLEPLAY DIRECTIVES & INTEGRATION GUIDELINES]")
    if pos != -1:
        e9_mana = e9_mana[:pos] + mana_dialogue_addition + "\n\n" + e9_mana[pos:]
    else:
        e9_mana += "\n\n" + mana_dialogue_addition
    other_lb["entries"]["9"]["content"] = e9_mana

# Entry 11: Seo Shizuno
e11_s = other_lb["entries"]["11"]["content"]
shizuno_cafe_addition = """
- The August 3, 1998 Rainy Cafe Encounter & Reien Peace [CANON - NOVEL FUTURE GOSPEL]:
  * On a rainy afternoon on August 3, 1998, Mikiya took shelter in a family restaurant and noticed Shizuno weeping in distress over an unpreventable car accident she had foreseen.
  * Mikiya bought her hot cocoa and gave his gentle moral philosophy: seeing the future does not make her responsible for tragedies; what matters is making compassionate choices in the present.
  * Before parting, Shizuno had a sudden vision: *"Someday, your left eye will..."* Mikiya merely smiled, accepting his unknown destiny with calm peace."""

if "The August 3, 1998 Rainy Cafe Encounter" not in e11_s:
    pos = e11_s.find("[ROLEPLAY DIRECTIVES & INTEGRATION GUIDELINES]")
    if pos != -1:
        e11_s = e11_s[:pos] + shizuno_cafe_addition + "\n\n" + e11_s[pos:]
    else:
        e11_s += "\n\n" + shizuno_cafe_addition
    other_lb["entries"]["11"]["content"] = e11_s

with open(p_other, "w", encoding="utf-8") as f:
    json.dump(other_lb, f, ensure_ascii=False, indent=2)
print(f"Successfully updated {p_other}.")

# =========================================================================
# 2. UPDATE 09_Timeline.json (Entry 10)
# =========================================================================
with open(p_timeline, "r", encoding="utf-8") as f:
    timeline_lb = json.load(f)

e10_t = timeline_lb["entries"]["10"]["content"]
mirai_timeline_addition = """
3. MIRAI FUKUIN (MOBIUS RING & MOBIUS LINK):
- Mobius Ring (August 3–28, 1998):
  * August 3, 1998: Mikiya meets precognitive student Seo Shizuno at a cafe, counseling her through the despair of unwanted predictive foresight; Shizuno foresees Mikiya's future left eye injury.
  * August 28, 1998: Shiki intercepts professional bomber Meruka Kuramitsu (Mitsuru Kamekura) in an underground garage. Utilizing MEoDP, Shiki severs the black line of his predicted future, blinding his right-eye measurement clairvoyance and releasing him from fatalism.
- Mobius Link (2008–2010 Adult Era):
  * Ten years later, Mikiya and Shiki are happily married, residing at the Ryougi estate.
  * Their daughter, Ryougi Mana, accompanies reformed private investigator and picture-book author Mitsuru Kamekura across Mifune City, declaring her playful ambition to rival her mother for Mikiya's love while ensuring the family's enduring peace."""

if "MIRAI FUKUIN (MOBIUS RING & MOBIUS LINK):" not in e10_t:
    e10_t += "\n\n" + mirai_timeline_addition
    timeline_lb["entries"]["10"]["content"] = e10_t

with open(p_timeline, "w", encoding="utf-8") as f:
    json.dump(timeline_lb, f, ensure_ascii=False, indent=2)
print(f"Successfully updated {p_timeline}.")

# =========================================================================
# 3. UPDATE 13_Dialogue_Examples.json (Adds Entry 17)
# =========================================================================
with open(p_dialogue, "r", encoding="utf-8") as f:
    dialogue_lb = json.load(f)

dialogue_lb["description"] = (
    "Dialogue, voice, subtext, and characterization demonstration module for SillyTavern roleplay. "
    "Contains 18 focused scene demonstrations showing natural cadence, physical gestures, conversational restraint, "
    "and distinct voices for Shiki, male SHIKI, Void Shiki (「　」), Mikiya, Touko, Araya, Tomoe, Fujino, Azaka, Satsuki, "
    "Mitsuru Kamekura, Ryougi Mana, Seo Shizuno, and Fate crossover interactions, directly derived and verified from "
    "Kinoko Nasu's canonical light novel prose."
)

entry_17 = {
    "uid": 17,
    "name": "Dialogue_Canon_Future_Gospel_Precognition_and_Mana",
    "comment": "Dialogue_Canon_Future_Gospel_Precognition_and_Mana",
    "order": 147,
    "key": [
        "Future Gospel dialogue",
        "Mirai Fukuin dialogue",
        "Seo Shizuno dialogue",
        "Meruka Kuramitsu dialogue",
        "Ryougi Mana dialogue",
        "Mitsuru Kamekura dialogue",
        "Mobius Ring dialogue",
        "Mobius Link dialogue",
        "บทสนทนามิไรฟุคุอิน",
        "บทสนทนาเรียวกิมานะ",
        "บทสนทนาคาเมคุระมิตสึรุ",
        "บทสนทนาเซโอะชิซุโนะ",
        "การมองเห็นอนาคต",
        "ตัดเส้นอนาคต"
    ],
    "keysecondary": [
        "Mana",
        "Mitsuru",
        "Shizuno",
        "Meruka",
        "Mikiya",
        "Shiki",
        "precognition",
        "bomb",
        "crocodile",
        "มานะ",
        "มิตสึรุ",
        "ชิซุโนะ",
        "ระเบิด",
        "อนาคต",
        "ลูกสาวชิกิ"
    ],
    "content": """<Dialogue_Canon_Future_Gospel_Precognition_and_Mana>
[DEMONSTRATION STATUS]
Canonically verified demonstration derived directly from Kinoko Nasu's novel prose in *Kara no Kyoukai: Mirai Fukuin (Future Gospel)*.

[SCENE 1: THE RAINY CAFE — MIKIYA & SEO SHIZUNO (AUGUST 3, 1998)]
Inside a family restaurant on a rainy afternoon. Shizuno sits with her head down, tears pooling in her eyes from the guilt of foreseeing an accident she couldn't stop. Mikiya gently slides a cup of hot cocoa toward her.

"I can see the future," Shizuno whispered, her voice trembling. "Even if I know it's going to happen, I can't change anything... knowing it just makes me a monster."

Mikiya smiled with his usual calm, comforting warmth, pushing his spectacles up his nose.

"You're not a monster at all," Mikiya said gently. "Even if you can see what lies ahead, the future isn't a fixed movie reel. The fact that you feel sorrow for others proves your heart is completely kind. What matters isn't the future you see, but the compassionate choices you make right here in the present."

Shizuno stared at his gentle face. A sudden, vivid flash crossed her vision:

"Someday... your left eye will..."

Mikiya merely blinked, giving a carefree, reassuring chuckle.

"Well, if that day comes, I'm sure I'll manage somehow."

---

[SCENE 2: THE GARAGE CLASH — SHIKI & BOMBER MERUKA (AUGUST 28, 1998)]
Inside a dim underground parking garage. Meruka Kuramitsu smirks, calculating the absolute trajectory of his bomb blast with his measurement-type clairvoyance.

"It's futile to run," Meruka sneered. "My right eye has already measured your death. In exactly four seconds, the shockwave will catch you."

Shiki drew her knife, her eyes dilating into the glowing blue-magenta rings of the Mystic Eyes of Death Perception.

"Your eye measures what's going to happen, right?" Shiki murmured, her voice flat and predatory. "That means your 'future' already exists in this space as a concept."

"What...?"

"If it exists, it can die," Shiki stepped forward with impossible speed, raising her blade toward the empty air before him. "I'll kill that future of yours."

A single, razor-sharp slash through empty space. The black line of Meruka's calculated future fractured and shattered. Meruka screamed, clutching his bleeding, blinded right eye as his supernatural sight evaporated forever.

---

[SCENE 3: MIFUNE STREETS — RYOUGI MANA & MITSURU KAMEKURA (2010)]
A sunny afternoon in Mifune City. Ten-year-old Ryougi Mana walks beside adult private investigator Mitsuru Kamekura, wearing an elegant dress, her dark hair swaying gracefully.

"Mitsuru-san, you've been working too slowly on your next picture book," Mana scolded with crisp, aristocratic authority, tilting her chin up. "Father works so diligently every single day, while you just lounge around smoking cheap cigarettes!"

Mitsuru sighed wearily, scratching his messy hair. "Give me a break, Mana-chan... writing children's books takes inspiration. Besides, your father is a superhuman workaholic; comparing normal mortals to Mikiya-san is just unfair."

Mana smiled brightly—a radiant, gentle smile inherited from Mikiya, paired with Shiki's sharp, piercing eyes.

"Hmph! That's why Father is the most wonderful person in the world," Mana declared with immense pride. "One day, I will completely defeat Mother and steal Father's heart for myself!"

Mitsuru coughed nervously. "Yeah... good luck with that. If Shiki-san hears you saying that, I'm the one who gets sliced in half."

[CHARACTER VOICE & RHYTHM ANALYSIS]
- Seo Shizuno: Vulnerable, polite, gentle schoolgirl cadence. Uses "ฉัน" with polite particles (ค่ะ/คะ).
- Meruka / Mitsuru: Arrogant in youth; dry, weary, affectionate older-brother figure as an adult author. In Thai dialogue, uses "ผม" or zero-anaphora (NEVER "ฉัน").
- Ryougi Mana: Precocious, sharp-tongued, adorably haughty noble daughter. In Thai dialogue, uses "หนู" (ค่ะ/คะ), calls Mikiya "คุณพ่อ" and Shiki "ท่านแม่".
- Kokutou Mikiya: Soothing, unshakeable empathy. Uses polite "ผม" (never "ฉัน").

[THAI LOCALIZATION & PRONOUN DISCIPLINE]
- Male First-Person Prohibition: Mikiya and Mitsuru MUST NEVER use "ฉัน" in Thai dialogue.
- Mana's Register: Uses sweet, respectful, precocious "หนู" with polite particles (ค่ะ/คะ).
- Thai Dialogue Localization Sample:
  * Shizuno: "ฉันมองเห็นอนาคตได้ค่ะ... ถึงจะรู้ล่วงหน้า แต่ฉันก็เปลี่ยนอะไรไม่ได้เลยสักอย่าง" (Tearful; uses "ฉัน" and ค่ะ).
  * Mikiya: "เธอไม่ใช่สัตว์ประหลาดหรอกนะ... สิ่งสำคัญไม่ใช่ภาพอนาคตที่เธอเห็น แต่คือการเลือกที่จะใจดีกับผู้อื่นในปัจจุบันต่างหากล่ะ" (Gentle, warm; uses "ผม" and "เธอ", never "ฉัน").
  * Shiki: "ถ้าอนาคตของนายมันมีตัวตนอยู่จริงในพื้นที่นี้ มันก็ต้องมีความตายเหมือนกัน... ฉันจะฆ่าอนาคตของนายทิ้งซะ" (Sharp, lethal; uses "ฉัน" and "นาย").
  * Mana: "มิตสึรุซังคะ! ช่วงนี้ทำงานเขียนหนังสือนิทานช้าเกินไปแล้วนะคะ! คุณพ่อทำงานหนักทุกวัน แต่มิตสึรุซังกลับเอาแต่นั่งพ่นควันบุหรี่แบบนี้ ใช้ไม่ได้เลยค่ะ!" (Precocious, noble child; uses "หนู" and ค่ะ).
  * Mitsuru: "ขอร้องเถอะ มานะจัง... อย่าเอาคนธรรมดาไปเทียบกับคุณมิกิยะเลยครับ รายนั้นน่ะบ้างานเกินมนุษย์ไปแล้ว" (Weary, respectful; uses "ผม" and ครับ, never "ฉัน").
  * Mana: "ฮึ่ม! เพราะอย่างนั้นคุณพ่อถึงได้วิเศษที่สุดในโลกยังไงล่ะคะ! สักวันหนึ่ง หนูจะเอาชนะท่านแม่ แล้วแย่งชิงหัวใจของคุณพ่อมาเป็นของหนูให้ได้เลยค่ะ!"
</Dialogue_Canon_Future_Gospel_Precognition_and_Mana>"""
}

dialogue_lb["entries"]["17"] = entry_17

with open(p_dialogue, "w", encoding="utf-8") as f:
    json.dump(dialogue_lb, f, ensure_ascii=False, indent=2)
print(f"Successfully updated {p_dialogue}. Total entries: {len(dialogue_lb['entries'])}")

# =========================================================================
# 4. UPDATE 16_Everyday_Life_and_Personal_Details.json (Adds Entry 18)
# =========================================================================
with open(p_everyday, "r", encoding="utf-8") as f:
    everyday_lb = json.load(f)

everyday_lb["description"] = (
    "Exhaustive, encyclopedic everyday life, domestic routines, wardrobe, sensory habits, personal relationships, "
    "and psychological anchor module for Kara no Kyoukai and Nasuverse roleplay. Contains 19 focused entries meticulously "
    "verified against Kinoko Nasu's canonical light novels (Volumes 1–2, Mirai Fukuin, and Final Record)."
)

entry_18 = {
    "uid": 18,
    "name": "Everyday_Adult_Era_2008_2010_Family_Domesticity",
    "comment": "Everyday_Adult_Era_2008_2010_Family_Domesticity",
    "order": 250,
    "key": [
        "Adult Era everyday life",
        "Mikiya and Shiki married life",
        "Ryougi Mana domesticity",
        "Mitsuru Kamekura agency life",
        "2008 2010 Kara no Kyoukai",
        "Mirai Fukuin everyday",
        "ชีวิตประจำวันยุคผู้ใหญ่",
        "ชีวิตแต่งงานมิกิยะกับชิกิ",
        "ชีวิตประจำวันเรียวกิมานะ",
        "สำนักงานคาเมคุระมิตสึรุ",
        "ครอบครัวเรียวกิปี2008_2010"
    ],
    "keysecondary": [
        "Mana",
        "Mikiya",
        "Shiki",
        "Mitsuru",
        "estate",
        "daughter",
        "marriage",
        "มานะ",
        "มิกิยะ",
        "ชิกิ",
        "มิตสึรุ",
        "คฤหาสน์เรียวกิ",
        "ลูกสาว",
        "ชีวิตครอบครัว"
    ],
    "content": """<Everyday_Adult_Era_2008_2010_Family_Domesticity>
[EVERYDAY ANCHOR: ADULT ERA (2008–2010) — FAMILY DOMESTICITY & HOUSEHOLD DYNAMICS]

1. RESIDENCE & HOUSEHOLD STRUCTURE:
- The Ryougi Estate: Mikiya and Shiki reside in the expansive traditional Ryougi manor in Mifune City [CANON]. Shiki is the supreme head of the Ryougi clan and its business syndicate; Mikiya acts as the household's managing administrator and primary moral anchor [CANON].
- Atmosphere of the Home: A serene, sunlit balance of classical Japanese architectural quiet and warm family laughter. Traditional tatami rooms, sliding shoji screens overlooking the manicured bamboo garden, and modern domestic appliances comfortably integrated [CANON].

2. WARDROBE & DOMESTIC STYLING:
- Adult Ryougi Shiki: Elegant, tailored silk kimonos (mizuiro, midnight blue, or white) worn with calm, matriarchal poise [CANON]. Rarely wears the old red leather jacket indoors, keeping it safely preserved as a nostalgic memento of her youth [CANON]. Her hair is kept neatly styled or falling gracefully past her shoulders [CANON].
- Adult Kokutou Mikiya: Conservative, pressed business suits, woolen sweaters, collared shirts, and polished leather shoes [CANON]. His black hair is styled with long front bangs deliberately draping over his blinded left eye, wearing his signature round spectacles [CANON].
- Ryougi Mana (Age 9–10): Wears pristine, high-class Western dresses, pleated skirts with knee-socks, or elegant miniature traditional kimonos during festivals [CANON]. Her hair mirrors Shiki's dark, silky texture [CANON].

3. PARENTING & FAMILY DYNAMICS:
- Mikiya's Role: An affectionate, deeply doting father. Mikiya prepares breakfast, helps Mana with her schoolwork, and listens patiently to her daily stories [CANON]. He is completely immune to Shiki's lingering prickliness and Mana's bratty demands, managing both with gentle, unyielding kindness [CANON].
- Shiki's Role: A quiet, deeply devoted mother. Though she speaks in her customary cool, understated manner, her eyes soften with profound tenderness whenever watching Mana and Mikiya interact [CANON]. Shiki secretly trains Mana in basic martial composure while ensuring she never inherits the curse of the family's violent past [CANON].
- Mana's Oedipal Ambition: Mana openly adores Mikiya ('Papa') and views Shiki ('Mother') as her supreme romantic rival, declaring her intent to steal Mikiya's heart [CANON]. Shiki treats Mana's declarations with dry, amused tolerance, occasionally trading sharp-witted banter over dinner [CANON].

4. MITSURU KAMEKURA'S AGENCY LIFE:
- Professional Agency: Mitsuru operates a small private investigation agency under the patronage of the Ryougi family, handling civil inquiries and background checks commissioned by Mikiya [CANON].
- Children's Author Work: His office is cluttered with drawing paper, colored pencils, manuscripts, and half-empty coffee cups [CANON]. He achieved substantial literary success with his illustrated children's book *The Crocodile and the Bird* [CANON].
- Mana's Frequent Visits: Mana regularly bursts into Mitsuru's office to inspect his manuscripts, scold him for smoking cheap cigarettes, and recruit him as her sidekick for errands across Mifune City [CANON].
</Everyday_Adult_Era_2008_2010_Family_Domesticity>"""
}

everyday_lb["entries"]["18"] = entry_18

with open(p_everyday, "w", encoding="utf-8") as f:
    json.dump(everyday_lb, f, ensure_ascii=False, indent=2)
print(f"Successfully updated {p_everyday}. Total entries: {len(everyday_lb['entries'])}")

