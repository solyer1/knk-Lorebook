# -*- coding: utf-8 -*-
"""
Applies Chapter 5 (Paradox Spiral / 矛盾螺旋) novel canon expansions to:
- Kara No/01_Shiki.json (Kanesada Katana & Edo-era swordsmanship brain reconfiguration)
- Kara No/03_Touko.json (Puppet seamless resurrection & Briefcase shadow beast familiar)
- Kara No/04_Other_Characters.json (Araya Śarīra & Arayashiki irony, Alba briefcase death, Tomoe aluminum key)
- Kara No/06_Abilities.json (Kanesada Katana mechanics & Araya Triple Bounded Field / Śarīra)
- Kara No/09_Timeline.json (Entry 7: Paradox Spiral full novel canon refinement)
- Kara No/13_Dialogue_Examples.json (Adds Entry 14: Dialogue_Canon_Paradox_Spiral_Araya_Catechism_and_Tomoe)
- Kara No/16_Everyday_Life_and_Personal_Details.json (Entry 10: Tomoe aluminum key canon audit)
"""
import json
import os

p_shiki = r"d:\Personalise\Homemad\Lorebook\Nasuverse\Kara No\01_Shiki.json"
p_touko = r"d:\Personalise\Homemad\Lorebook\Nasuverse\Kara No\03_Touko.json"
p_other = r"d:\Personalise\Homemad\Lorebook\Nasuverse\Kara No\04_Other_Characters.json"
p_abilities = r"d:\Personalise\Homemad\Lorebook\Nasuverse\Kara No\06_Abilities.json"
p_timeline = r"d:\Personalise\Homemad\Lorebook\Nasuverse\Kara No\09_Timeline.json"
p_dialogue = r"d:\Personalise\Homemad\Lorebook\Nasuverse\Kara No\13_Dialogue_Examples.json"
p_everyday = r"d:\Personalise\Homemad\Lorebook\Nasuverse\Kara No\16_Everyday_Life_and_Personal_Details.json"

# =========================================================================
# 1. UPDATE 01_Shiki.json
# =========================================================================
with open(p_shiki, "r", encoding="utf-8") as f:
    shiki_lb = json.load(f)

e0_s_content = shiki_lb["entries"]["0"]["content"]
kanesada_brain_shift = """
- The Kanesada Katana & Edo-Era Swordsmanship Brain Reconfiguration [CANON - NOVEL CHAPTER 5]:
  * Katana vs. Knife Disparity: While Shiki is dangerous with a knife, Kinoko Nasu explicitly confirms that Shiki wielding a katana is an entirely different order of lethal entity.
  * Brain Function Reorganization: As observed by Araya Souren in novel Chapter 5, when classical Edo-period samurai drew their blades, their brains physically altered the biological operation of their bodies:
    - Vascular circulation routes shift to prioritize muscle groups.
    - Biological respiration ceases normal breathing, entering combat stillness.
    - Muscle actuation operates at impossible, un-living physical angles.
    - All human sensory and psychological functions useless for slaughter are cleanly eliminated.
  * Combat Velocity: With a single step, Shiki reduces a four-meter distance to zero, severing high-thaumaturgy Bounded Fields and deflecting relics blessed by saints with pure, blinding martial execution."""

if "The Kanesada Katana & Edo-Era Swordsmanship Brain Reconfiguration" not in e0_s_content:
    pos = e0_s_content.find("[INTERNAL CONFLICT & THE URGE TO KILL]")
    if pos != -1:
        e0_s_content = e0_s_content[:pos] + kanesada_brain_shift + "\n\n" + e0_s_content[pos:]
    else:
        e0_s_content += "\n\n" + kanesada_brain_shift
    shiki_lb["entries"]["0"]["content"] = e0_s_content

with open(p_shiki, "w", encoding="utf-8") as f:
    json.dump(shiki_lb, f, ensure_ascii=False, indent=2)
print(f"Successfully updated {p_shiki}.")

# =========================================================================
# 2. UPDATE 03_Touko.json
# =========================================================================
with open(p_touko, "r", encoding="utf-8") as f:
    touko_lb = json.load(f)

# Entry 3: Puppet resurrection
e3_t = touko_lb["entries"]["3"]["content"]
puppet_res_addition = """
- Instantaneous Puppet Resurrection Mechanism [CANON - NOVEL CHAPTER 5]:
  * In Paradox Spiral, when Cornelius Alba decapitates Touko's body in the basement of Ogawa Apartments, her death is completely meaningless.
  * Touko maintains multiple identical biological puppet bodies in stasis across various hidden workshops. The instant one body suffers physical destruction, her soul and consciousness awaken in a standby replica with zero temporal disruption or existential loss, lighting a cigarette as if merely awakening from an afternoon nap."""

if "Instantaneous Puppet Resurrection Mechanism" not in e3_t:
    e3_t += "\n\n" + puppet_res_addition
    touko_lb["entries"]["3"]["content"] = e3_t

# Entry 9: Leather briefcase familiar
e9_t = touko_lb["entries"]["9"]["content"]
briefcase_addition = """
- The Heavy Leather Briefcase Familiar (Shadow Beast) [CANON - NOVEL CHAPTER 5]:
  * In novel Chapter 5, Touko arrived at Ogawa Apartments carrying a massive, heavy leather briefcase.
  * Inside is bound an ancient, grotesque phantom beast / familiar composed of pure shadowy darkness.
  * Upon confronting Cornelius Alba, Touko opened the briefcase clasps, releasing the shadow creature to engulf Alba, slowly devouring him alive from the feet up while Alba screamed in helpless hysteria."""

if "The Heavy Leather Briefcase Familiar" not in e9_t:
    e9_t += "\n\n" + briefcase_addition
    touko_lb["entries"]["9"]["content"] = e9_t

with open(p_touko, "w", encoding="utf-8") as f:
    json.dump(touko_lb, f, ensure_ascii=False, indent=2)
print(f"Successfully updated {p_touko}.")

# =========================================================================
# 3. UPDATE 04_Other_Characters.json
# =========================================================================
with open(p_other, "r", encoding="utf-8") as f:
    other_lb = json.load(f)

# Entry 0: Araya Souren
e0_a = other_lb["entries"]["0"]["content"]
araya_novel_addition = """
- Śarīra Relic (Left Arm) & The Arayashiki Counter Force Irony [CANON - NOVEL CHAPTER 5]:
  * Holy Relic Embedding: Araya embedded a genuine Śarīra (Buddha's bone relic) within the flesh of his left arm, granting the limb divine immunity and structural reinforcement capable of parrying Shiki's Mystic Eyes of Death Perception.
  * The Arayashiki Irony: In the climax, Touko reveals the cruel joke of Araya's existence: Araya Souren (荒耶宗蓮) bears the exact same name as the Counter Force of humanity's collective unconsciousness—Arayashiki (阿頼耶識 / Alaya-vijnana). His lifelong crusade against human despair was an unconscious, doomed revolt against the very concept of humanity that shared his name.
  * The Three Dying Inquiries: In his final moments as his body crumbled to ash under the moonlight, Touko posed the ancient catechism: Seeking what? (*"I just want a conclusion for these filthy humans."*) Seeking where? (*"Only within myself."*) Seeking where to reach? (*"The end of this paradox spiral."*)"""

if "Śarīra Relic (Left Arm) & The Arayashiki Counter Force Irony" not in e0_a:
    pos = e0_a.find("[RELATIONSHIPS WITH EXISTING CAST]")
    if pos != -1:
        e0_a = e0_a[:pos] + araya_novel_addition + "\n\n" + e0_a[pos:]
    else:
        e0_a += "\n\n" + araya_novel_addition
    other_lb["entries"]["0"]["content"] = e0_a

# Entry 3: Cornelius Alba
e3_a = other_lb["entries"]["3"]["content"]
alba_death_addition = """
- Execution by the Briefcase Shadow Beast [CANON - NOVEL CHAPTER 5]:
  * In the climax of Paradox Spiral, Alba gleefully decapitated Touko's puppet body, believing he had finally surpassed his rival.
  * When a duplicate Touko strolled into the complex completely unharmed, Alba's sanity shattered. Touko unlocked her massive leather briefcase, releasing an ancient, shapeless shadow beast that pinned Alba to the floor, devouring his lower torso and limbs inch by agonizing inch as Alba shrieked in unhinged terror."""

if "Execution by the Briefcase Shadow Beast" not in e3_a:
    e3_a += "\n\n" + alba_death_addition
    other_lb["entries"]["3"]["content"] = e3_a

# Entry 6: Enjou Tomoe
e6_tomoe = other_lb["entries"]["6"]["content"]
tomoe_key_addition = """
- The Aluminum Key without a Lock & Defiance of Araya [CANON - NOVEL CHAPTER 5]:
  * The Useless Key: The silver aluminum key Tomoe treasured since childhood as his proudest possession was completely worthless; the Ogawa Apartments utilized solely electronic card-key locks. The key unlocked nothing in reality—it was an artificial psychological anchor.
  * Overcoming the Origin: Despite being a synthetic puppet constructed by Araya with false memories, Tomoe's genuine, stubborn human love for his family and for Shiki allowed him to break through Araya's calculations, sprinting to the elevator to deliver Shiki's Kanesada katana before dying a hero."""

if "The Aluminum Key without a Lock & Defiance of Araya" not in e6_tomoe:
    e6_tomoe += "\n\n" + tomoe_key_addition
    other_lb["entries"]["6"]["content"] = e6_tomoe

with open(p_other, "w", encoding="utf-8") as f:
    json.dump(other_lb, f, ensure_ascii=False, indent=2)
print(f"Successfully updated {p_other}.")

# =========================================================================
# 4. UPDATE 06_Abilities.json
# =========================================================================
with open(p_abilities, "r", encoding="utf-8") as f:
    abilities_lb = json.load(f)

# Entry 10: Araya Souren Techniques
e10_a = abilities_lb["entries"]["10"]["content"]
araya_fields_addition = """
[TRIPLE BOUNDED FIELD & ŚARĪRA RELIC: NOVEL CHAPTER 5]
- Fugu (不倶): A personal-range spatial Bounded Field that distorts immediate physical distance, making an enemy's steps and weapon strikes land too shallow to inflict fatal damage.
- Shakujou (錫杖): A crushing spatial barrier that anchors and binds the target's physical and metaphysical movement.
- Shukuchi (縮地): A spatial compression technique allowing Araya to instantly collapse distance between points.
- Śarīra Blessing: A holy relic of the Buddha's bone embedded in his left arm, providing supreme conceptual protection that resists even direct slashes from Mystic Eyes of Death Perception unless struck with overwhelming martial force."""

if "[TRIPLE BOUNDED FIELD & ŚARĪRA RELIC: NOVEL CHAPTER 5]" not in e10_a:
    e10_a += "\n\n" + araya_fields_addition
    abilities_lb["entries"]["10"]["content"] = e10_a

# Entry 15: Add Kanesada Swordsmanship Mechanics
e15_s = abilities_lb["entries"]["15"]["content"]
kanesada_mech = """
[KANESADA KATANA & CLASSICAL EDO SWORDSMANSHIP BIOLOGY: NOVEL CHAPTER 5]
When Ryougi Shiki wields her ancestral Kanesada katana, her neurological and somatic systems switch into classical Edo-period samurai execution mode:
- Somatic Reconfiguration: The brain alters circulation pathways, suspends normal biological respiration, and actuates skeletal-muscular structures at impossible, un-living geometric angles.
- Zero Acceleration Transit: Reduces a four-meter gap to zero in a single fluid stride that feels as though time itself is flowing backwards.
- Conceptual Severance: Slices through multilayered spatial compression barriers and severing the spiritual conduits of grand-tier magi with effortless, surgical lethality."""

if "[KANESADA KATANA & CLASSICAL EDO SWORDSMANSHIP BIOLOGY: NOVEL CHAPTER 5]" not in e15_s:
    e15_s += "\n\n" + kanesada_mech
    abilities_lb["entries"]["15"]["content"] = e15_s

with open(p_abilities, "w", encoding="utf-8") as f:
    json.dump(abilities_lb, f, ensure_ascii=False, indent=2)
print(f"Successfully updated {p_abilities}.")

# =========================================================================
# 5. UPDATE 09_Timeline.json (Entry 7)
# =========================================================================
with open(p_timeline, "r", encoding="utf-8") as f:
    timeline_lb = json.load(f)

entry_7_content = """<Timeline_Era_7_November_1998_Paradox_Spiral>
[ERA 7: OCTOBER – NOVEMBER 1998 (CHAPTER 5 / FILM 5: PARADOX SPIRAL)]

1. THE ARCHITECTURAL HORROR OF OGAWA MANSION:
- The Taiji Crucible: Araya Souren designs Ogawa Mansion, a colossal circular 10-story apartment complex in Mifune City built explicitly in the shape of a Taoist Taiji diagram.
- The 50 Family Loop: Araya fills the complex with 50 dysfunctional families, using his Bounded Field to amplify their paranoia until they slaughter one another, resetting their synthetic corpses every midnight in an infinite recursive cycle to harvest the essence of death.

2. OCTOBER 1998: ENJOU TOMOE'S ESCAPE & DOMESTIC SANCTUARY:
- The Encounter: Runaway teenager Enjou Tomoe believes he murdered his parents in Room 405. Wandering the rainy streets, he is ambushed by thugs and rescued by Shiki. Tomoe carries a childhood aluminum key around his neck—unaware that the complex used purely electronic card-key locks, making the key completely useless in reality.
- Domestic Sanctuary: Shiki brings Tomoe to Room 404. For one month, Tomoe cleans, buys groceries, and experiences quiet domestic cohabitation with the aloof, guarded Shiki.

3. NOVEMBER 1998: THE INFILTRATION & THE CRUEL TRUTH:
- Infiltration: Tomoe and Shiki enter Ogawa Mansion. Investigating Room 405, they discover the rotting corpses of Tomoe's parents—and the rotting corpse of Enjou Tomoe himself. The Tomoe beside Shiki is an artificial puppet infused with dying memories.
- The Spatial Trap: Araya traps Shiki within a pocket dimension between space, sealing her empty vessel in stasis.

4. THE DUEL OF THE MAGI & TOUKO'S RESURRECTION:
- Infiltration: Touko infiltrates to rescue Shiki. Araya crushes Touko's heart, and Cornelius Alba gleefully decapitates her body.
- The Seamless Duplicate: Miles away, a standby puppet of Touko awakens with zero loss of consciousness. Touko arrives at Ogawa Mansion with a giant leather briefcase, releasing an ancient shadow beast familiar that devours Alba alive from the feet up.

5. TOMOE'S SACRIFICE & THE KANESADA KATANA CLIMAX:
- The Final Sprint: Defying Araya's calculations through authentic human love, puppet Tomoe sprints into the elevator to deliver Shiki's ancestral Kanesada katana before Araya crushes his skull.
- Brain Function Reconfiguration: Wielding the Kanesada katana, Shiki's brain physically reorganizes her body into an Edo-period killing machine. In a single fluid step reducing four meters to zero, she severs Araya's Fugu and Shakujou Bounded Fields and deflects his Śarīra relic arm.
- The Tenth-Floor Leap: As Araya attempts to escape and materialize in the courtyard, Shiki leaps from the tenth floor, bisecting Araya from shoulder to waist as he appears below.
- The Arayashiki Catechism: Touko confronts the dying Araya under the moonlight, revealing the irony of his name (Araya vs. Arayashiki / Alaya-vijnana). Araya answers Touko's three questions: Seeking what? (*"I just want a conclusion."*) Seeking where? (*"Only within myself."*) Seeking where to reach? (*"The end of this paradox spiral."*) Araya dissolves into ash.
</Timeline_Era_7_November_1998_Paradox_Spiral>"""

timeline_lb["entries"]["7"]["content"] = entry_7_content

with open(p_timeline, "w", encoding="utf-8") as f:
    json.dump(timeline_lb, f, ensure_ascii=False, indent=2)
print(f"Successfully updated {p_timeline}.")

# =========================================================================
# 6. UPDATE 13_Dialogue_Examples.json (Adds Entry 14)
# =========================================================================
with open(p_dialogue, "r", encoding="utf-8") as f:
    dialogue_lb = json.load(f)

dialogue_lb["description"] = (
    "Dialogue, voice, subtext, and characterization demonstration module for SillyTavern roleplay. "
    "Contains 15 focused scene demonstrations showing natural cadence, physical gestures, conversational restraint, "
    "and distinct voices for Shiki, male SHIKI, Mikiya, Touko, Araya, Tomoe, Fujino, Azaka, and Fate crossover interactions, "
    "directly derived and verified from Kinoko Nasu's canonical light novel prose."
)

entry_14 = {
    "uid": 14,
    "name": "Dialogue_Canon_Paradox_Spiral_Araya_Catechism_and_Tomoe",
    "comment": "Dialogue_Canon_Paradox_Spiral_Araya_Catechism_and_Tomoe",
    "order": 144,
    "key": [
        "Paradox Spiral dialogue",
        "Araya Souren dialogue",
        "Araya catechism dialogue",
        "Enjou Tomoe dialogue",
        "Ogawa Apartments dialogue",
        "Kanesada katana dialogue",
        "บทสนทนาวงกตเกลียวที่ขัดแย้ง",
        "บทสนทนาอารายะโซเรน",
        "คำถามอมตะสามข้อ",
        "บทสนทนาเอนโจโทโมเอะ",
        "ดาบคะเนะซาดะ"
    ],
    "keysecondary": [
        "Araya",
        "Touko",
        "Tomoe",
        "Shiki",
        "Alba",
        "briefcase",
        "Kanesada",
        "Arayashiki",
        "อารายะ",
        "โทโกะ",
        "โทโมเอะ",
        "ชิกิ",
        "กระเป๋าหนัง",
        "อาลยวิชญาณ"
    ],
    "content": """<Dialogue_Canon_Paradox_Spiral_Araya_Catechism_and_Tomoe>
[DEMONSTRATION STATUS]
Canonically verified demonstration derived directly from Kinoko Nasu's novel prose in Chapter 5 (*Paradox Spiral / 矛盾螺旋*).

[SCENE 1: ROOM 404 — SHIKI & ENJOU TOMOE (OCTOBER 1998)]
Inside Shiki's minimalist apartment. Rain taps against the window glass. Enjou Tomoe sits shivering on the tatami, holding his useless aluminum key, his voice cracking with guilt.

"I killed someone... my mother and my father," Tomoe whispered, staring at his trembling hands. "Why did you bring someone like me to your room?"

Shiki leaned against the edge of her bed, her gaze chillingly flat and distant.

"If you're asking if I'm afraid, the answer is no," Shiki said softly. "You reek of blood, but you don't have the smell of a killer. A real murderer kills because they have a reason, or because their nature drives them to it. But you... you're just running away from something you don't even understand."

"Running away...?"

"Shut up and sleep. If you have time to whine, sweep the floor tomorrow."

---

[SCENE 2: THE MOONLIGHT CATECHISM — TOUKO & ARAYA SOUREN (NOVEMBER 1998)]
The courtyard of the collapsing Ogawa Mansion. Moonlight bathes the green lawn in cold silver. Araya Souren stands motionless, both arms severed, his body bisected from shoulder to waist, turning into powdery ash in the wind. Aozaki Touko approaches casually, lighting a cigarette.

"You failed again, Araya," Touko remarked calmly, exhaling smoke into the starry sky. "It's funny, isn't it? The Counter Force of humanity's collective unconsciousness is called Arayashiki (阿頼耶識). You were born with the exact same name as your lifelong enemy, yet you never noticed. What a cruel trap this world set for you."

Araya's lips parted, blood scattering like dark powder in the night breeze.

"Araya, what do you seek?" Touko asked softly. (荒耶、何を求める)

"Nothing," Araya answered, his voice deep, hollow, and devoid of hatred. "I just want a conclusion. If an ugly, hopeless existence is all that remains of humanity, I would be relieved to know that such ugliness is our true value."

"Araya, where do you seek it?" (荒耶、何処に求める)

"Only within myself." (ただ己が内のみ)

"Araya, where are you trying to reach?" (荒耶、何処を目指す)

The black cloak scattered into the wind. Half of his torso dissolved into floating ash.

"That's obvious," Araya's dying whisper resonated without a voice. "The end of this paradox spiral..." (この矛盾螺旋の果てを)

[CHARACTER VOICE & RHYTHM ANALYSIS]
- Araya Souren: Austere, monastic, absolute solemnity. Speaks with heavy Buddhist cadences and total lack of petty malice. In Thai dialogue, uses imposing "ข้า" or natural zero-anaphora (NEVER "ฉัน").
- Enjou Tomoe: Desperate, breathless, adolescent fragility. Uses boyish "เรา" or zero-anaphora (NEVER "ฉัน").
- Aozaki Touko: Intellectual, world-weary, clinical detachment laced with ancient sorrow. Uses "ฉัน" freely.

[THAI LOCALIZATION & PRONOUN DISCIPLINE]
- Male First-Person Prohibition: Araya and Tomoe MUST NEVER refer to themselves as "ฉัน" in Thai dialogue.
  * Araya: Uses austere, solemn "ข้า" or zero-anaphora.
  * Tomoe: Uses boyish, desperate "เรา" or zero-anaphora.
  * Touko / Shiki: May freely use "ฉัน" or natural zero-anaphora.
- Thai Dialogue Localization Sample:
  * Tomoe: "เรา... ฆ่าคนมานะ ทั้งพ่อทั้งแม่เลย... ทำไมเธอถึงพาคนอย่างเรามาที่ห้องล่ะ?" (Trembling adolescent fear; uses "เรา", never "ฉัน").
  * Shiki: "ถ้าจะถามว่าฉันกลัวนายไหม คำตอบคือไม่... กลิ่นคาวเลือดติดตัวนายมาก็จริง แต่นายไม่มีกลิ่นอายของฆาตกรเลยสักนิด คนที่ฆ่าคนจริง ๆ น่ะ มันไม่ใช่แบบนี้หรอก เงียบแล้วก็นอนไปซะ" (Uses "ฉัน" and "นาย").
  * Touko: "เจ้าล้มเหลวอีกแล้วนะ อารายะ... น่าขันดีใช่ไหมล่ะ? พลังปรามปรามของเจตจำนงร่วมในมนุษย์น่ะ ถูกเรียกว่า 'อารายาชิกิ' (阿頼耶識) แท้ ๆ แต่เจ้ากลับเกิดมาพร้อมชื่อเดียวกับศัตรูคู่อาฆาตของตัวเอง ช่างเป็นกับดักที่โหดร้ายจริง ๆ"
  * Touko: "อารายะ สิ่งที่เจ้าแสวงหาคืออะไร?"
  * Araya: "ข้าเพียงต้องการบทสรุป... ของมนุษย์ที่แสนโสมมเหล่านี้เท่านั้น" (Austere, deep; uses "ข้า", never "ฉัน").
  * Touko: "อารายะ เจ้าแสวงหามันจากที่ใด?"
  * Araya: "เพียงแค่ภายในตัวของข้าเท่านั้น" (ข้า).
  * Touko: "อารายะ จุดหมายที่เจ้ามุ่งไปคือที่ไหน?"
  * Araya: "...ย่อมชัดเจนอยู่แล้ว ปลายทางแห่งวงกตเกลียวที่ขัดแย้งนี้..."
</Dialogue_Canon_Paradox_Spiral_Araya_Catechism_and_Tomoe>"""
}

dialogue_lb["entries"]["14"] = entry_14

with open(p_dialogue, "w", encoding="utf-8") as f:
    json.dump(dialogue_lb, f, ensure_ascii=False, indent=2)
print(f"Successfully updated {p_dialogue}. Total entries: {len(dialogue_lb['entries'])}")

# =========================================================================
# 7. UPDATE 16_Everyday_Life_and_Personal_Details.json (Entry 10)
# =========================================================================
with open(p_everyday, "r", encoding="utf-8") as f:
    everyday_lb = json.load(f)

e10_t = everyday_lb["entries"]["10"]["content"]
e10_t = e10_t.replace(
    "Carries his brass apartment key (Room 410, Ogawa Apartments) strung around his neck on a dirty string [CANON].",
    "Carries a cold, bulky aluminum key strung around his neck as his proudest childhood treasure [CANON - NOVEL CHAPTER 5]. However, the Ogawa Apartments utilized solely electronic card-key locks, meaning the aluminum key never had a lock that it could open in reality—it was a purely psychological anchor of his fabricated domestic life [CANON - NOVEL CHAPTER 5]."
)
everyday_lb["entries"]["10"]["content"] = e10_t

with open(p_everyday, "w", encoding="utf-8") as f:
    json.dump(everyday_lb, f, ensure_ascii=False, indent=2)
print(f"Successfully updated {p_everyday}.")

