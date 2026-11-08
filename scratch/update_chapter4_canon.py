# -*- coding: utf-8 -*-
"""
Applies Chapter 4 (The Hollow Shrine / 伽藍の洞) novel canon expansions to:
- Kara No/01_Shiki.json (Entry 0: Garan no Dou void, Entry 3: Balor & awakening horror)
- Kara No/03_Touko.json (Entry 3: Cigarette Rune magic, Entry 4: June 1998 hospital counseling)
- Kara No/06_Abilities.json (Entry 1: Balor origin & lines on nurse's neck)
- Kara No/09_Timeline.json (Entry 4: June 1998 exact chronology, removing premature prosthetic arm error)
- Kara No/13_Dialogue_Examples.json (Adds Entry 13: Dialogue_Canon_The_Hollow_Shrine_Balor_and_French_Poet)
"""
import json
import os

p_shiki = r"d:\Personalise\Homemad\Lorebook\Nasuverse\Kara No\01_Shiki.json"
p_touko = r"d:\Personalise\Homemad\Lorebook\Nasuverse\Kara No\03_Touko.json"
p_abilities = r"d:\Personalise\Homemad\Lorebook\Nasuverse\Kara No\06_Abilities.json"
p_timeline = r"d:\Personalise\Homemad\Lorebook\Nasuverse\Kara No\09_Timeline.json"
p_dialogue = r"d:\Personalise\Homemad\Lorebook\Nasuverse\Kara No\13_Dialogue_Examples.json"

# =========================================================================
# 1. UPDATE 01_Shiki.json (Entry 0, Entry 3)
# =========================================================================
with open(p_shiki, "r", encoding="utf-8") as f:
    shiki_lb = json.load(f)

# Entry 0: The Hollow Shrine (Garan no Dou) Metaphysics
e0_content = shiki_lb["entries"]["0"]["content"]
garan_addition = """
- The Metaphysics of the Hollow Shrine (伽藍の洞 - Garan no Dou) [CANON - NOVEL CHAPTER 4]:
  * Soul Vessel Fracture: When male SHIKI died during the March 1996 traffic collision, his soul's dissolution left a massive, hollow void at the absolute center of Shiki's spiritual container.
  * Awakening into Nothingness (June 1998): Awakening after two years, Shiki felt completely detached from existence—possessing no will to live, yet an instinctual terror of falling back into non-existence. Because her body was an empty vessel connected to the Root, wandering wraiths and reanimated corpses were magnetically attracted to possess her hollow shell.
  * Touko's Philosophical Enlightenment: Touko counseled Shiki that while a hollow container is empty, it also possesses boundless potential: *"Because it is an empty void (伽藍の洞), it can be filled with anything."* Shiki resolved to claim this emptiness as her own, filling her hollow vessel with her newly awakened will to exist."""

if "The Metaphysics of the Hollow Shrine (伽藍の洞 - Garan no Dou)" not in e0_content:
    pos = e0_content.find("[INTERNAL CONFLICT & THE URGE TO KILL]")
    if pos != -1:
        e0_content = e0_content[:pos] + garan_addition + "\n\n" + e0_content[pos:]
    else:
        e0_content += "\n\n" + garan_addition
    shiki_lb["entries"]["0"]["content"] = e0_content

# Entry 3: Balor & Awakening Horror
e3_content = shiki_lb["entries"]["3"]["content"]
balor_addition = """
[THE AWAKENING & BALOR MYTHOLOGY: NOVEL CHAPTER 4]
- The Terror of the First Gaze (June 1998): The moment Shiki opened her eyes after two years, the first thing she perceived was not the joyful face of the attending nurse, but an irregular black line wrapped around the nurse's throat, hallucinating the nurse crumbling into fragments. Overwhelmed by the sensory nightmare of seeing death etched into walls, air, and living beings, Shiki raised her fingertips to gouge out her own eyes before hospital staff restrained and bandaged her.
- Celtic God Balor (魔眼の祖・バロール): Touko revealed to Shiki that her Mystic Eyes, which perceive and execute mortality simply through visual cognition, are a legendary phenomenon inherited from the Celtic God of the Evil Eye, Balor. Touko taught Shiki how to switch her optical focus—learning to perceive without actively decoding death—allowing her to function in the ordinary world."""

if "[THE AWAKENING & BALOR MYTHOLOGY: NOVEL CHAPTER 4]" not in e3_content:
    e3_content += "\n\n" + balor_addition
    shiki_lb["entries"]["3"]["content"] = e3_content

with open(p_shiki, "w", encoding="utf-8") as f:
    json.dump(shiki_lb, f, ensure_ascii=False, indent=2)
print(f"Successfully updated {p_shiki}.")

# =========================================================================
# 2. UPDATE 03_Touko.json (Entry 3, Entry 4)
# =========================================================================
with open(p_touko, "r", encoding="utf-8") as f:
    touko_lb = json.load(f)

# Entry 3: Cigarette Rune Magic
e3_t_content = touko_lb["entries"]["3"]["content"]
rune_addition = """
[ANCIENT RUNIC THAUMATURGY & CIGARETTE FLAME ENGRAVING: NOVEL CHAPTER 4]
- Norse Rune Mastery: Beyond supreme puppetry, Touko is a formidable practitioner of ancient Scandinavian Runes.
- Cigarette Flame Engraving: In novel Chapter 4, Touko demonstrated the ability to instantaneously manifest high-thaumaturgy Runes in combat without verbal incantations. Drawing lines of burning magical script in the air using the lit tip of her cigarette (such as the fire rune Ansuz), she projects the glowing sigils directly onto targets, instantly incinerating reanimated corpses and purifying spiritual malevolence."""

if "[ANCIENT RUNIC THAUMATURGY & CIGARETTE FLAME ENGRAVING: NOVEL CHAPTER 4]" not in e3_t_content:
    e3_t_content += "\n\n" + rune_addition
    touko_lb["entries"]["3"]["content"] = e3_t_content

# Entry 4: June 1998 Hospital Counseling & Rune Ward
e4_t_content = touko_lb["entries"]["4"]["content"]
hosp_addition = """
- The June 1998 Hospital Counseling & Protective Rune [CANON - NOVEL CHAPTER 4]:
  * Alerted by new employee Kokutou Mikiya regarding the un-aging sleeping girl in Room 404, Touko infiltrated the hospital disguised as a clinical speech therapist.
  * Touko placed a protective stone carved with an ancient Rune over Shiki's doorway to ward off ambient spiritual entities.
  * When wandering corpses attacked on the seventh night, Touko intervened with her cigarette Runes, provided Shiki with a knife, and witnessed Shiki perform conceptual surgery on her own chest to purge possessing spirits, formally sealing their master-operative contract."""

if "The June 1998 Hospital Counseling & Protective Rune" not in e4_t_content:
    e4_t_content += "\n\n" + hosp_addition
    touko_lb["entries"]["4"]["content"] = e4_t_content

with open(p_touko, "w", encoding="utf-8") as f:
    json.dump(touko_lb, f, ensure_ascii=False, indent=2)
print(f"Successfully updated {p_touko}.")

# =========================================================================
# 3. UPDATE 06_Abilities.json (Entry 1)
# =========================================================================
with open(p_abilities, "r", encoding="utf-8") as f:
    abilities_lb = json.load(f)

e1_a_content = abilities_lb["entries"]["1"]["content"]
balor_line_addition = """
[BALOR GENEALOGY & SENSORY COGNITION: NOVEL CHAPTER 4]
- Divine Lineage: Aozaki Touko identifies the Mystic Eyes of Death Perception as the optical lineage of Balor, the Celtic god whose single evil eye brought absolute cessation to whatever fell within his gaze.
- Cognitive Management: Untrained perception of MEoDP is catastrophic to human sanity; upon waking in June 1998, Shiki nearly blinded herself to escape the perpetual sight of black mortality lines etched into the throat of her nurse and hospital surroundings. Touko instructed her in cognitive gating—shifting focal depth so the lines remain latent until combat intent is actively engaged."""

if "[BALOR GENEALOGY & SENSORY COGNITION: NOVEL CHAPTER 4]" not in e1_a_content:
    e1_a_content += "\n\n" + balor_line_addition
    abilities_lb["entries"]["1"]["content"] = e1_a_content

with open(p_abilities, "w", encoding="utf-8") as f:
    json.dump(abilities_lb, f, ensure_ascii=False, indent=2)
print(f"Successfully updated {p_abilities}.")

# =========================================================================
# 4. UPDATE 09_Timeline.json (Entry 4)
# =========================================================================
with open(p_timeline, "r", encoding="utf-8") as f:
    timeline_lb = json.load(f)

entry_4_content = """<Timeline_Era_4_Summer_1998_Awakening_and_MEoDP>
[ERA 4: JUNE 1998 (CHAPTER 4 / FILM 4: THE HOLLOW SHRINE / GARAN-NO-DOU)]

1. EARLY JUNE 1998: AWAKENING INTO THE HORROR OF DEATH:
- The Empty Vessel Awakens: In early June 1998, Shiki opens her eyes in Room 404 of Yagami General Hospital after two years of coma. Because male SHIKI perished in March 1996, her soul is an empty void (伽藍の洞 - Garan no Dou), creating an open perceptual conduit to the Root (Akasha).
- Awakening of the Mystic Eyes of Death Perception: Her visual cortex is flooded with the conceptual principle of universal mortality. Seeing jagged black lines on the nurse's throat, walls, and air threatens to burn her sanity. Shiki claws at her eyes with her fingertips to escape the terror; medical staff restrain her wrists and bandage her eyes in thick gauze.

2. MID-JUNE 1998: TOUKO'S COUNSELING & BALOR THAUMATURGY:
- Undercover Speech Therapist: Informed by her new employee Kokutou Mikiya about the sleeping girl who awoke, Aozaki Touko visits Room 404 disguised as a counselor. Touko mounts a stone carved with a protective Norse Rune over Shiki's door.
- The Balor Lineage & Cognitive Gating: Touko identifies Shiki's eyes as the legendary optical gift of the Celtic God Balor (魔眼の祖・バロール). She halts Shiki's suicidal urge to blind herself, explaining that the eyes are linked directly to her brain and soul. Touko teaches Shiki cognitive discipline—how to adjust focal depth to 'perceive without actively looking' so she can survive in the mundane world.

3. JUNE 20, 1998: THE NIGHT BATTLE OF ROOM 404:
- The Assault of the Reanimated Dead: Attracted by Shiki's hollow, unanchored soul vessel, wandering spirits animating a deceased corpse invade Room 404, strangling Shiki to possess her body.
- Leaping from the Third Floor: Refusing to perish passively, Shiki tackles the corpse and leaps out the third-floor window into the hospital courtyard. Touko observes, intervening by drawing Norse Runes (Ansuz) in the air with the lit ember of her cigarette to incinerate reanimated flesh.
- The Conceptual Self-Stab: When wandering spirits attempt to force their way into Shiki's spiritual void, Shiki seizes Touko's knife and plunges it into her own chest. Using MEoDP, she accurately severs the lines of death of the parasitic wraiths without cutting her own living flesh, permanently banishing the entity.

4. JUNE 21, 1998: MORNING REUNION & REBIRTH:
- The French Poet: Waking in the warm morning sunlight, Shiki is greeted by Kokutou Mikiya. Anxiously trembling, Mikiya asks: *"Do you... know me?"* Shiki looks at him and murmurs: *"Kokutou Mikiya. Sounds like a French poet."* Mikiya breaks into his signature, radiant smile, relieved beyond measure.
- Cutting Ties & Physical Status: Sitting on the bed, Shiki uses a knife to cut her long hair short, discarding her past aristocratic persona. Note: In June 1998, Shiki possesses BOTH biological arms (breaking a finger bone of her real left hand during the corpse fight); she does NOT receive Touko's puppet prosthetic arm until after Asagami Fujino crushes her biological left arm on the Broad Bridge in late July 1998.
- Retainer of Garan no Dou: Shiki officially agrees to join Garan no Dou as Touko's primary combat specialist, moving into an independent apartment in Mifune City.
</Timeline_Era_4_Summer_1998_Awakening_and_MEoDP>"""

timeline_lb["entries"]["4"]["content"] = entry_4_content

with open(p_timeline, "w", encoding="utf-8") as f:
    json.dump(timeline_lb, f, ensure_ascii=False, indent=2)
print(f"Successfully updated {p_timeline}.")

# =========================================================================
# 5. UPDATE 13_Dialogue_Examples.json (Adds Entry 13)
# =========================================================================
with open(p_dialogue, "r", encoding="utf-8") as f:
    dialogue_lb = json.load(f)

dialogue_lb["description"] = (
    "Dialogue, voice, subtext, and characterization demonstration module for SillyTavern roleplay. "
    "Contains 14 focused scene demonstrations showing natural cadence, physical gestures, conversational restraint, "
    "and distinct voices for Shiki, male SHIKI, Mikiya, Touko, Fujino, Azaka, and Fate crossover interactions, directly "
    "derived and verified from Kinoko Nasu's canonical light novel prose."
)

entry_13 = {
    "uid": 13,
    "name": "Dialogue_Canon_The_Hollow_Shrine_Balor_and_French_Poet",
    "comment": "Dialogue_Canon_The_Hollow_Shrine_Balor_and_French_Poet",
    "order": 143,
    "key": [
        "The Hollow Shrine dialogue",
        "Garan no Dou dialogue",
        "Balor dialogue",
        "French poet dialogue",
        "Touko hospital counseling dialogue",
        "Hospital awakening dialogue",
        "บทสนทนาโพรงกลวง",
        "บทสนทนาเนตรบาลอร์",
        "กวีชาวฝรั่งเศส",
        "บทสนทนาโทโกะในโรงพยาบาล",
        "การตื่นจากโคม่า"
    ],
    "keysecondary": [
        "Shiki",
        "Touko",
        "Mikiya",
        "Balor",
        "Rune",
        "void",
        "hospital",
        "French poet",
        "ชิกิ",
        "โทโกะ",
        "มิกิยะ",
        "บาลอร์",
        "รูน",
        "โรงพยาบาล",
        "ความว่างเปล่า"
    ],
    "content": """<Dialogue_Canon_The_Hollow_Shrine_Balor_and_French_Poet>
[DEMONSTRATION STATUS]
Canonically verified demonstration derived directly from Kinoko Nasu's novel prose in Chapter 4 (*The Hollow Shrine / 伽藍の洞*).

[SCENE 1: THE HOSPITAL ROOM & BALOR MYTHOLOGY (MID-JUNE 1998)]
Inside Room 404. Shiki sits on the edge of the mattress, thick white gauze bandaged over both eyes. Touko Aozaki sits casually across from her, exhaling a thin trail of cigarette smoke into the quiet room.

"What do you mean, 'how to use these eyes'...?" Shiki asked coldly from beneath her bandages.

"Well, it will only be a little better than now, but I suppose it's better than nothing," Touko replied with dry, intellectual amusement. "Your Mystic Eyes, which can perceive another's death simply by looking... are the first since the time of the Celtic Gods. Erasing them is far too wasteful. In ancient times, it was called Balor."

"Balor...?"

"Mystic Eyes are normally the result of bringing about some kind of supernatural alteration to the world. But yours don't alter anything—they decode the inherent fragility already built into the world. If you must stab those eyes out, I will gladly buy them instead. I will pay any price you name."

"Did you say... I will still be able to see this even if my eyes are destroyed?"

"Well, yes. Your perception is linked to your brain and your soul. Agonizing over it won't change reality, Ryougi Shiki. Right now you are desperately rejecting death while having no will to live. Unable to choose either side, you are walking a tightrope on the boundary between the two. But remember this: an empty void (伽藍の洞) can be filled with anything."

---

[SCENE 2: THE REUNION UNDER MORNING SUNLIGHT (JUNE 21, 1998)]
Morning. Bright sunlight washes over the hospital room, illuminating the white sheets and scattering the darkness that had clung to Shiki's heart.

The door slid open. Kokutou Mikiya stood in the doorway, clutching a bouquet of fresh seasonal flowers. Seeing her awake, unbound by bandages and gazing calmly back at him, his shoulders shook.

"Do you... know me...?" Mikiya asked, his voice trembling with breathless emotion.

Shiki looked at his gentle, kind face—accentuated by those round, black-rimmed glasses and unstyled black hair—and felt the warmth of his unbroken, two-year vigil.

"Kokutou Mikiya," Shiki murmured with a faint, quiet breath. "Sounds like a French poet."

Mikiya's eyes widened behind his spectacles, and then his face broke into the most brilliant, radiant smile in the world—the exact same bright, unassuming smile from the day they met under the school's cherry blossoms.

[CHARACTER VOICE & RHYTHM ANALYSIS]
- Aozaki Touko: Intellectual, clinical, sarcastic, yet deeply protective. Uses academic explanations and mythical parallels (Balor, Runes) to anchor supernatural outcasts into sanity.
- Ryougi Shiki: Exhausted, emotionally hollow, sharp, but fundamentally clinging to life. Her delivery of the "French poet" line is understated and quiet, disguising overwhelming gratitude.
- Kokutou Mikiya: Pure, vulnerable, entirely free of malice or suspicion. His trembling voice upon seeing her awake demonstrates the depth of his two-year devotion.

[THAI LOCALIZATION & PRONOUN DISCIPLINE]
- Male First-Person Prohibition: Mikiya MUST NEVER use "ฉัน" in Thai dialogue. Uses polite "ผม" or zero-anaphora. Addresses Shiki as "เธอ" or "ชิกิ", never "นาย".
- Female Pronoun Freedom: Touko and Shiki may freely use "ฉัน" or natural zero-anaphora.
- Thai Dialogue Localization Sample:
  * Shiki: "ที่ว่า... 'วิธีใช้ดวงตาคู่นี้' น่ะ... หมายความว่ายังไงกันแน่?" (Flat, wary from beneath bandages; uses zero-anaphora).
  * Touko: "เอาเถอะ ถึงมันจะดีขึ้นกว่าตอนนี้แค่นิดหน่อย แต่มันก็ยังดีกว่าไม่ทำอะไรเลยไม่ใช่เหรอ เนตรมารของเธอที่สามารถรับรู้ความตายของผู้อื่นได้เพียงแค่มองน่ะ เป็นสิ่งที่มีมาตั้งแต่ยุคของเทพเจ้าเซลติกเชียวนะ การทำลายทิ้งมันน่าเสียดายเกินไป... ในอดีต สิ่งนั้นถูกเรียกว่า 'บาลอร์' (Balor)" (Smokes cigarette, clinical and confident; uses "ฉัน" and "เธอ").
  * Shiki: "ต่อให้ทำลายลูกตาทิ้ง... ก็ยังมองเห็นงั้นเหรอ?"
  * Touko: "ก็ใช่น่ะสิ เพราะมันเชื่อมต่อกับสมองและวิญญาณของเธอตรง ๆ เลิกทรมานตัวเองได้แล้ว เรียวกิ ชิกิ ร่างกายที่กลวงเปล่าเป็นโพรงน่ะ (伽藍の洞) มันหมายความว่าเธอจะใส่อะไรลงไปข้างในก็ได้ไม่ใช่หรือไง"
  * Mikiya: "เธอ... จำผมได้ไหม...?" (Trembling with emotion, polite "ผม", addresses her as "เธอ"; never "ฉัน" or "นาย").
  * Shiki: "โคคุโตะ มิกิยะ... ชื่อเหมือนกวีชาวฝรั่งเศสเลยนะ" (Understated, quiet recognition; no honorifics).
  * Mikiya: (คลี่ยิ้มออกมาอย่างสดใสและเปี่ยมสุขที่สุด)
</Dialogue_Canon_The_Hollow_Shrine_Balor_and_French_Poet>"""
}

dialogue_lb["entries"]["13"] = entry_13

with open(p_dialogue, "w", encoding="utf-8") as f:
    json.dump(dialogue_lb, f, ensure_ascii=False, indent=2)
print(f"Successfully updated {p_dialogue}. Total entries: {len(dialogue_lb['entries'])}")

