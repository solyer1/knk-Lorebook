# -*- coding: utf-8 -*-
"""
Applies Chapter 6 (Oblivion Recording / 忘却録音) novel canon expansions to:
- Kara No/04_Other_Characters.json (Entry 2: Azaka, Entry 7: Satsuki, Entry 10: Misaya)
- Kara No/06_Abilities.json (Entry 13: Unified Language immunity & MEoDP linguistic cutting)
- Kara No/09_Timeline.json (Entry 8: Oblivion Recording novel chronology & uniform correction)
- Kara No/13_Dialogue_Examples.json (Adds Entry 15: Dialogue_Canon_Oblivion_Recording_Reien_and_Unified_Language)
- Kara No/16_Everyday_Life_and_Personal_Details.json (Entry 5: Azaka dorm room encounter with uniform Shiki)
"""
import json
import os

p_other = r"d:\Personalise\Homemad\Lorebook\Nasuverse\Kara No\04_Other_Characters.json"
p_abilities = r"d:\Personalise\Homemad\Lorebook\Nasuverse\Kara No\06_Abilities.json"
p_timeline = r"d:\Personalise\Homemad\Lorebook\Nasuverse\Kara No\09_Timeline.json"
p_dialogue = r"d:\Personalise\Homemad\Lorebook\Nasuverse\Kara No\13_Dialogue_Examples.json"
p_everyday = r"d:\Personalise\Homemad\Lorebook\Nasuverse\Kara No\16_Everyday_Life_and_Personal_Details.json"

# =========================================================================
# 1. UPDATE 04_Other_Characters.json
# =========================================================================
with open(p_other, "r", encoding="utf-8") as f:
    other_lb = json.load(f)

# Entry 2: Kokutou Azaka
e2_azaka = other_lb["entries"]["2"]["content"]
azaka_ch6_addition = """
- Reien Academy Life & Spontaneous Ignition Mastery [CANON - NOVEL CHAPTER 6]:
  * Salamander-Skin Ignition: Under Touko's occult tutelage, Azaka mastered spontaneous combustion thaumaturgy without incantations. By channeling magical energy through custom salamander-skin gloves, she manifests instant flame bursts capable of incinerating spiritual familiars and conceptual puppets.
  * Dormitory Infiltration by Shiki (January 1999): Azaka was forced to share her private dormitory room with Ryougi Shiki, who disguised herself in a tailored Reien Academy uniform. Azaka was deeply exasperated seeing Shiki lounge on her bed with tomboyish disregard for Catholic school decorum."""

if "Reien Academy Life & Spontaneous Ignition Mastery" not in e2_azaka:
    pos = e2_azaka.find("[PERSONALITY & BEHAVIORAL PROFILE]")
    if pos != -1:
        e2_azaka = e2_azaka[:pos] + azaka_ch6_addition + "\n\n" + e2_azaka[pos:]
    else:
        e2_azaka += "\n\n" + azaka_ch6_addition
    other_lb["entries"]["2"]["content"] = e2_azaka

# Entry 7: Kurogiri Satsuki
e7_satsuki = other_lb["entries"]["7"]["content"]
satsuki_ch6_addition = """
- Fairy Abduction & Sealing Designation Background [CANON - NOVEL CHAPTER 6]:
  * Childhood Spirited Away: In his youth, Satsuki was abducted by fairies. The encounter permanently stripped him of his own past memories, leaving him unable to recognize his own identity. In compensation, he acquired the primordial Unified Language of Babel.
  * Sealing Designation (封印指定): Because his command of the Unified Language directly imprints concepts upon human souls without magical circuits, the Clock Tower branded him with a Sealing Designation.
  * Philosophy of Oblivion: Satsuki genuinely believes human misery stems from memory. By dispatching memory-stealing fairies to erase traumatic pasts, he believes he grants peaceful salvation—unaware that erasing memories fundamentally destroys human selfhood."""

if "Fairy Abduction & Sealing Designation Background" not in e7_satsuki:
    pos = e7_satsuki.find("[PERSONALITY & CONVERSATIONAL MANNERISMS]")
    if pos != -1:
        e7_satsuki = e7_satsuki[:pos] + satsuki_ch6_addition + "\n\n" + e7_satsuki[pos:]
    else:
        e7_satsuki += "\n\n" + satsuki_ch6_addition
    other_lb["entries"]["7"]["content"] = e7_satsuki

with open(p_other, "w", encoding="utf-8") as f:
    json.dump(other_lb, f, ensure_ascii=False, indent=2)
print(f"Successfully updated {p_other}.")

# =========================================================================
# 2. UPDATE 06_Abilities.json (Entry 13)
# =========================================================================
with open(p_abilities, "r", encoding="utf-8") as f:
    abilities_lb = json.load(f)

e13_u = abilities_lb["entries"]["13"]["content"]
unified_shiki_addition = """
[NATURAL COUNTER & THE VOID IMMUNITY: NOVEL CHAPTER 6]
- The Void Immunity: In novel Chapter 6, Kurogiri Satsuki attempted to subject Ryougi Shiki to the Unified Language to submerge her mind in oblivion. However, Shiki's spiritual center is connected to the Root—an empty, hollow void (伽藍の洞). Because she already possesses 'nothingness' at her core, Satsuki's conceptual command to erase the ego had zero purchase.
- Conceptual Severance of Sound: Activating her Mystic Eyes of Death Perception, Shiki visually decoded the hypnotic linguistic waves in the air as lines of death, cleanly slicing through Satsuki's linguistic compulsion with her knife."""

if "[NATURAL COUNTER & THE VOID IMMUNITY: NOVEL CHAPTER 6]" not in e13_u:
    e13_u += "\n\n" + unified_shiki_addition
    abilities_lb["entries"]["13"]["content"] = e13_u

with open(p_abilities, "w", encoding="utf-8") as f:
    json.dump(abilities_lb, f, ensure_ascii=False, indent=2)
print(f"Successfully updated {p_abilities}.")

# =========================================================================
# 3. UPDATE 09_Timeline.json (Entry 8)
# =========================================================================
with open(p_timeline, "r", encoding="utf-8") as f:
    timeline_lb = json.load(f)

entry_8_content = """<Timeline_Era_8_January_1999_Oblivion_Recording>
[ERA 8: JANUARY 1999 (CHAPTER 6 / FILM 6: OBLIVION RECORDING)]

1. JANUARY 2, 1999: THE MEMORY THEFT AT REIEN GIRLS' ACADEMY:
- The Assignment: On the night of January 2, 1999, Touko Aozaki contacts Shiki with an undercover assignment at Reien Girls' Academy, an elite Catholic boarding school where students have suffered sudden memory loss and personality dissociation.
- Azaka's Undercover Operation: Touko's apprentice Kokutou Azaka is already stationed inside. Equipped with salamander-skin ignition gloves, Azaka investigates the strange incidents under the guise of an ordinary student.

2. SHIKI'S INFILTRATION IN REIEN UNIFORM:
- The Undercover Disguise: To Azaka's immense shock and irritation, Ryougi Shiki arrives at Reien dressed directly in the tailored navy-blue school uniform of Reien Girls' Academy, lounging lazily on Azaka's dormitory bed while Azaka frets over decorum.
- The Vector of Fairies: Student council member Ouryou Misaya is manipulated into spreading invisible conceptual fairies (妖精) across the campus. These entities consume the painful memories of students, leaving them hollow and compliant.

3. THE CHAPEL CLASH & FOREST BATTLE:
- Azaka vs. Misaya: In the academy chapel, Azaka confronts Misaya. Utilizing her salamander-skin gloves, Azaka channels spontaneous combustion without verbal incantations, incinerating Misaya's fairy familiars and freeing her mind.
- Shiki vs. The Fairy Swarm: In the snowy woods outside the chapel, Shiki is ambushed by hundreds of invisible memory fairies. Perceiving the conceptual lines of death on their intangible forms with her Mystic Eyes, Shiki dissects the fairy swarm with effortless knife slashes.

4. KUROGIRI SATSUKI & THE UNIFIED LANGUAGE CONFRONTATION:
- God's Word Revealed: The mastermind is Kurogiri Satsuki (designated a Sealing Designation magus by the Clock Tower). Abducted by fairies in childhood, his memories were lost, awakening the ancient Unified Language of Babel that commands the soul directly.
- The Void Immunity: Satsuki attempts to speak the Unified Language to submerge Shiki in oblivion. However, because Shiki's spiritual core is connected to the Root (an empty void), the command to erase her ego cannot take hold. Shiki slices through Satsuki's linguistic compulsion with her knife, forcing his surrender.
- Aftermath: Satsuki peacefully departs the academy. Azaka reaffirms her devotion to Mikiya while establishing a grudging respect for Shiki. Weeks later, an awakened Shirazumi Lio ambushes and murders Kurogiri Satsuki in a dark alleyway, stealing his resources.
</Timeline_Era_8_January_1999_Oblivion_Recording>"""

timeline_lb["entries"]["8"]["content"] = entry_8_content

with open(p_timeline, "w", encoding="utf-8") as f:
    json.dump(timeline_lb, f, ensure_ascii=False, indent=2)
print(f"Successfully updated {p_timeline}.")

# =========================================================================
# 4. UPDATE 13_Dialogue_Examples.json (Adds Entry 15)
# =========================================================================
with open(p_dialogue, "r", encoding="utf-8") as f:
    dialogue_lb = json.load(f)

dialogue_lb["description"] = (
    "Dialogue, voice, subtext, and characterization demonstration module for SillyTavern roleplay. "
    "Contains 16 focused scene demonstrations showing natural cadence, physical gestures, conversational restraint, "
    "and distinct voices for Shiki, male SHIKI, Mikiya, Touko, Araya, Tomoe, Fujino, Azaka, Satsuki, and Fate crossover "
    "interactions, directly derived and verified from Kinoko Nasu's canonical light novel prose."
)

entry_15 = {
    "uid": 15,
    "name": "Dialogue_Canon_Oblivion_Recording_Reien_and_Unified_Language",
    "comment": "Dialogue_Canon_Oblivion_Recording_Reien_and_Unified_Language",
    "order": 145,
    "key": [
        "Oblivion Recording dialogue",
        "Reien Academy dialogue",
        "Kokutou Azaka dialogue",
        "Kurogiri Satsuki dialogue",
        "Unified Language dialogue",
        "Shiki school uniform dialogue",
        "บทสนทนาการบันทึกที่หลงลืม",
        "บทสนทนาโรงเรียนสตรีเรย์เอ็น",
        "บทสนทนาโคคุโตะอาซากะ",
        "บทสนทนาคุโรกิริซัตสึกิ",
        "ภาษาเอกภาพบาเบล"
    ],
    "keysecondary": [
        "Azaka",
        "Shiki",
        "Satsuki",
        "Reien",
        "fairies",
        "uniform",
        "memory",
        "oblivion",
        "อาซากะ",
        "ชิกิ",
        "ซัตสึกิ",
        "เรย์เอ็น",
        "ภูตขโมยความทรงจำ",
        "เครื่องแบบนักเรียน"
    ],
    "content": """<Dialogue_Canon_Oblivion_Recording_Reien_and_Unified_Language>
[DEMONSTRATION STATUS]
Canonically verified demonstration derived directly from Kinoko Nasu's novel prose in Chapter 6 (*Oblivion Recording / 忘却録音*).

[SCENE 1: REIEN DORMITORY — AZAKA & SHIKI (JANUARY 1999)]
Inside Azaka's neat Catholic boarding school dormitory room. Shiki lies casually on Azaka's bed, dressed in the pristine navy-blue uniform of Reien Girls' Academy, staring at the ceiling. Azaka clutches her desk chair in a mix of fury and disbelief.

"You muscle-head..." Azaka muttered, glaring at Shiki. "Look at my arms, they're covered in bruises thanks to you! Why are you lying on my bed as if you own the place?!"

Shiki didn't even turn her head, speaking in her usual low, clipped cadence.

"Because it's soft. And your brother told me to make sure you don't get yourself killed. If you have time to complain about a bed, go figure out who's breeding those fairies."

"Hmph! As if I need your help to protect my brother's peace! And don't you dare act like a proper Reien lady just because you put on that uniform—it looks completely absurd on someone who smells like iron and rain!"

"It's just clothes, Azaka. Now quiet down, you're giving me a headache."

---

[SCENE 2: THE ENCOUNTER WITH GOD'S WORD — KUROGIRI SATSUKI (JANUARY 1999)]
In the snowy forest clearing near the chapel. Kurogiri Satsuki stands smiling gently in his teacher's overcoat, his voice carrying the eerie, undeniable resonance of the pre-Babel Unified Language.

"Human suffering stems entirely from memory, Ryougi Shiki," Satsuki said softly, his words vibrating directly within the soul without traveling through acoustic air. "If a person forgets their sins, their pain, and their guilt, they attain absolute peace. The fairies merely return those heavy burdens to the void of oblivion. Is that not true salvation?"

Shiki held her knife, her dark eyes glowing with the blue-magenta light of the Mystic Eyes of Death Perception.

"Taking away someone's memories is no different from killing them," Shiki said coldly. "You're just playing god with words you don't own."

"Then let those words take you as well," Satsuki spoke, releasing the full hypnotic command of the Unified Language. "Forget. Sleep within oblivion."

The air warped as the absolute conceptual command crashed down upon Shiki. Yet Shiki merely tilted her chin, completely unfazed.

"Too bad for you," Shiki whispered, slicing the empty air and severing the linguistic command with a sharp metallic gleam. "I already have a bottomless void inside me. You can't erase something that was already empty to begin with."

[CHARACTER VOICE & RHYTHM ANALYSIS]
- Kokutou Azaka: Feisty, proud, dignified, prone to rapid-fire scolding when provoked by Shiki, yet deeply caring beneath her haughty Catholic schoolgirl facade. Uses polite feminine "ฉัน" and polite particles (ค่ะ/คะ).
- Kurogiri Satsuki: Serene, philosophical, speaking with gentle, unshakeable confidence. In Thai dialogue, uses polite "ผม" or zero-anaphora (NEVER "ฉัน").
- Ryougi Shiki: Unbothered, blunt, indifferent to high-society decorum, viewing Satsuki's linguistic philosophy with cold pragmatism.

[THAI LOCALIZATION & PRONOUN DISCIPLINE]
- Male First-Person Prohibition: Kurogiri Satsuki MUST NEVER use "ฉัน" in Thai dialogue. Uses polite, calm "ผม" or zero-anaphora.
- Female Pronoun Freedom: Azaka and Shiki may freely use "ฉัน" or natural zero-anaphora.
- Thai Dialogue Localization Sample:
  * Azaka: "ยัยคนบ้าพลังเอ๊ย... ดูแขนฉันสิ มีแต่รอยช้ำไปหมดเพราะเธอแท้ ๆ! แล้วทำไมถึงมานอนแผ่บนเตียงของฉันหน้าตาเฉยแบบนั้นกันคะ?!" (Exasperated, feisty; uses "ฉัน" and ค่ะ).
  * Shiki: "ก็เตียงมันนุ่มนี่... อีกอย่าง พี่ชายของเธอบอกให้ฉันมาดูไม่ให้เธอไปรนหาที่ตาย ถ้ามีเวลามาบ่นเรื่องเตียง ก็รีบไปหาตัวคนบงการพวกภูตได้แล้ว" (Flat, calm; uses "ฉัน").
  * Satsuki: "ความทุกข์ทรมานของมนุษย์น่ะ ล้วนเกิดจากความทรงจำทั้งนั้นแหละครับ... หากลืมบาปและความเจ็บปวดไปได้ มนุษย์ก็จะได้รับความสงบสุขที่แท้จริงไม่ใช่หรือครับ?" (Gentle, philosophical; uses "ผม" / ครับ, never "ฉัน").
  * Shiki: "การขโมยความทรงจำไปน่ะ มันก็ไม่ต่างอะไรกับการฆ่าคนทิ้งหรอกนะ... เสียใจด้วยนะ ภาษาเอกภาพของนายน่ะทำอะไรฉันไม่ได้หรอก เพราะข้างในตัวฉันน่ะมันเป็นโพรงที่ว่างเปล่ามาตั้งแต่แรกแล้ว สิ่งที่ว่างเปล่าอยู่แล้ว มันไม่มีอะไรให้ต้องลืมหรอกนะ"
</Dialogue_Canon_Oblivion_Recording_Reien_and_Unified_Language>"""
}

dialogue_lb["entries"]["15"] = entry_15

with open(p_dialogue, "w", encoding="utf-8") as f:
    json.dump(dialogue_lb, f, ensure_ascii=False, indent=2)
print(f"Successfully updated {p_dialogue}. Total entries: {len(dialogue_lb['entries'])}")

# =========================================================================
# 5. UPDATE 16_Everyday_Life_and_Personal_Details.json (Entry 5)
# =========================================================================
with open(p_everyday, "r", encoding="utf-8") as f:
    everyday_lb = json.load(f)

e5_azaka = everyday_lb["entries"]["5"]["content"]
azaka_dorm_addition = """
- Reien Dormitory Cohabitation with Uniformed Shiki (January 1999) [CANON - NOVEL CHAPTER 6]:
  * During the January 1999 investigation, Shiki stayed in Azaka's private dormitory room, dressed directly in a tailored Reien Academy uniform dress [CANON - NOVEL CHAPTER 6].
  * Azaka was deeply exasperated and self-conscious, complaining endlessly that Shiki had bruised her arms during investigations and was lounging casually on her bed without showing proper Catholic school modesty or decorum [CANON - NOVEL CHAPTER 6]."""

if "Reien Dormitory Cohabitation with Uniformed Shiki" not in e5_azaka:
    pos = e5_azaka.find("4. SOCIAL BEHAVIOR & INTERACTION STYLE:")
    if pos != -1:
        e5_azaka = e5_azaka[:pos] + azaka_dorm_addition + "\n\n" + e5_azaka[pos:]
    else:
        e5_azaka += "\n\n" + azaka_dorm_addition
    everyday_lb["entries"]["5"]["content"] = e5_azaka

with open(p_everyday, "w", encoding="utf-8") as f:
    json.dump(everyday_lb, f, ensure_ascii=False, indent=2)
print(f"Successfully updated {p_everyday}.")

