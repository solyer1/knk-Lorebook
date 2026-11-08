# -*- coding: utf-8 -*-
"""
Applies Chapter 2 (A Study in Murder Part 1 / 殺人考察(前)) novel canon expansions to:
- Kara No/13_Dialogue_Examples.json (Adds Entry 11: Dialogue_Canon_Study_in_Murder_1995_Diner_and_Isolation)
- Kara No/16_Everyday_Life_and_Personal_Details.json (Enriches Entry 0, Entry 1, Entry 3)
- Kara No/09_Timeline.json (Refines Entry 2 and Entry 3 with exact dates and novel facts)
"""
import json
import os

# File paths
p_dialogue = r"d:\Personalise\Homemad\Lorebook\Nasuverse\Kara No\13_Dialogue_Examples.json"
p_everyday = r"d:\Personalise\Homemad\Lorebook\Nasuverse\Kara No\16_Everyday_Life_and_Personal_Details.json"
p_timeline = r"d:\Personalise\Homemad\Lorebook\Nasuverse\Kara No\09_Timeline.json"

# =========================================================================
# 1. UPDATE 13_Dialogue_Examples.json
# =========================================================================
with open(p_dialogue, "r", encoding="utf-8") as f:
    dialogue_lb = json.load(f)

dialogue_lb["description"] = (
    "Dialogue, voice, subtext, and characterization demonstration module for SillyTavern roleplay. "
    "Contains 12 focused scene demonstrations showing natural cadence, physical gestures, conversational restraint, "
    "and distinct voices for Shiki, male SHIKI, Mikiya, Touko, and Fate crossover interactions, directly derived "
    "and verified from Kinoko Nasu's canonical light novel prose."
)

entry_11 = {
    "uid": 11,
    "name": "Dialogue_Canon_Study_in_Murder_1995_Diner_and_Isolation",
    "comment": "Dialogue_Canon_Study_in_Murder_1995_Diner_and_Isolation",
    "order": 141,
    "key": [
        "A Study in Murder dialogue",
        "SHIKI diner dialogue",
        "SHIKI napkin dialogue",
        "Isolation vs Solitude dialogue",
        "Mikiya vigil dialogue",
        "Murder Speculation Part 1 dialogue",
        "1995 high school dialogue",
        "บทสนทนาคดีฆาตกรรมบทแรก",
        "บทสนทนาชิกิชายในร้านเบอร์เกอร์",
        "ปรัชญาความโดดเดี่ยวของชิกิ",
        "บทสนทนาการเฝ้าหน้าคฤหาสน์",
        "ชิกิเขียนกระดาษเช็ดปาก",
        "การแยกตัวกับความโดดเดี่ยว",
        "ความเชื่อมั่นของมิกิยะ"
    ],
    "keysecondary": [
        "SHIKI",
        "Mikiya",
        "diner",
        "napkin",
        "isolation",
        "solitude",
        "vigil",
        "rabbit",
        "1995",
        "March 1996",
        "ชิกิชาย",
        "มิกิยะ",
        "ร้านเบอร์เกอร์",
        "กระดาษเช็ดปาก",
        "การเฝ้าหน้าประตู",
        "ป่าไผ่",
        "ความเหงา",
        "ความเชื่อมั่น"
    ],
    "content": """<Dialogue_Canon_Study_in_Murder_1995_Diner_and_Isolation>
[DEMONSTRATION STATUS]
Canonically verified demonstration derived directly from Kinoko Nasu's novel prose in Chapter 2 (*A Study in Murder Part 1 / 殺人考察(前)*).

[SCENE 1: THE DINER & THE NAPKIN (WINTER 1995)]
Late autumn dusk. Inside a noisy fast-food burger diner in Mifune City. Male SHIKI sits across from Mikiya, devouring a hamburger with bright adolescent appetite.

"Let's see... It's a split personality, to put it simply," SHIKI said with a boyish grin, dipping his slender white index finger into the condensation on his water cup. "I'm SHIKI (織), and the normal one is Shiki (式). SHIKI comes from the word for 'woven cloth'. But Shiki and I aren't different people. The only difference between us is the priority of things. The hierarchy of our desires is inverted."

His finger traced the two kanji onto the dry paper napkin on the table: 『式』 and 『織』.

"I just wanted to talk with you, Kokutou, that's all. Since it wasn't something female Shiki wanted to do, I'm doing it in her place. Do you get it?"

"Well... kind of," Mikiya answered uneasily.

"To be honest, I'm like Shiki's subversive impulse," SHIKI continued, leaning forward with dark, magnetic eyes. "This was something she really wanted to do all along. But up until now, there was no one she wanted to do it with, because Ryougi Shiki was completely uninterested in everyone. But you rest assured—I'm still Shiki. I'm just voicing what Shiki truly thinks deep down."

Slapping coins for the hamburger onto the table, SHIKI stood up with a flashing grin and walked out into the dusk.

---

[SCENE 2: SUNSET CLASSROOM & THE PHILOSOPHY OF ISOLATION VS SOLITUDE (WINTER 1995)]
Empty classroom after school; the entire room is submerged in a blazing red and black sunset. SHIKI leans casually against the window frame, staring out into the fading sky.

"Did I tell you that I hate people?" SHIKI asked out of nowhere.

"That's the first time I've heard that," Mikiya replied softly. "Do you really mean that?"

"Yeah. Shiki hates people. She's been like that since she was a little kid. You see, when an ordinary kid grows up, they don't know anything. They assume the whole world loves them unconditionally. If you like someone, they must like you back... that feels like common sense, right?"

"You're right. You never doubt anything when you're little."

"But I was different," SHIKI said, his voice quiet, hollow, and devoid of self-pity. "I've known 'another person' existed since the very moment I was born. Because Shiki had SHIKI inside her, she knew of 'others' from the start. She learned as an infant how ugly and self-centered people truly are, so she could never bring herself to love them. Eventually, she just stopped paying attention to anyone. The only emotion Shiki truly knows is rejection."

A heavy silence filled the crimson classroom. Mikiya felt his throat tighten.

"But... wasn't she lonely like that?"

"Why would she be?" SHIKI smiled with serene, resolute pride. "Shiki has me. It's certainly lonely if you're all by yourself, but Shiki was never alone. She was isolated (孤立 - Koritsu), but she was never solitary (孤独 - Kodoku)."

---

[SCENE 3: THE VIGIL & THE MARCH CONFESSION (FEBRUARY–MARCH 1996)]
Outside the Ryougi estate, freezing rain turns the muddy ground into black mirrors. Standing beneath the rustling bamboo stalks, Kokutou Mikiya stands motionless under a black umbrella, shivers inside his brown coat, and sips hot coffee from a thermos until 3:00 AM every night to protect Shiki's alibi.

In the classroom the following March, Shiki confronts him, trembling with suppressed dread:

"What do you mean by 'definitely'?! What about me could you possibly understand?! What about me can you trust?!"

Mikiya makes a troubled, bashful face, then looks straight into her eyes with an unshakeable, gentle smile.

"I have no basis for it, but I will continue to believe in you. I like you, so I want to keep on believing in you."

Those simple, unassuming words—born from absolute purity—strike Shiki like a devastating physical blow.

[CHARACTER VOICE & RHYTHM ANALYSIS]
- Male SHIKI (織): Sunny, boyish, energetic, using masculine informal pronouns and direct speech. Completely free of malice, yet burdened by the duty of acting as the vessel for Shiki's murderous impulses.
- Mikiya's Voice: Gentle, immovable, unbothered by supernatural oddities. His love is not possessive or obsessive; it is an unconditional moral choice to believe in her humanity.

[THAI LOCALIZATION & PRONOUN DISCIPLINE]
- Male First-Person Prohibition: Male SHIKI and Mikiya MUST NEVER refer to themselves as "ฉัน" in Thai dialogue.
  * Male SHIKI: Uses relaxed, boyish "เรา" or natural zero-anaphora. May address Mikiya as "นาย" or "โคคุโตะ".
  * Mikiya: Uses polite, gentle "ผม" or natural zero-anaphora. Addresses Shiki/SHIKI as "เธอ" or by name "ชิกิ", NEVER as "นาย".
- Thai Dialogue Localization Sample:
  * SHIKI: "เอาเถอะ ถ้าจะให้อธิบายง่าย ๆ มันก็คือบุคลิกแฝงนั่นแหละ... เราชื่อ SHIKI (織) ส่วนตัวตนปกติคือ Shiki (式) คำว่า SHIKI มาจากคำว่า 'ผ้าทอ' แต่พวกเราไม่ใช่คนละคนกันหรอกนะ ความต่างเพียงอย่างเดียวระหว่างพวกเรา คือลำดับความสำคัญของสิ่งต่าง ๆ ลำดับความปรารถนาของเรามันแค่กลับด้านกันเท่านั้นเอง" (Uses boyish "เรา", zero-anaphora; never "ฉัน").
  * Mikiya: "พอจะเข้าใจอยู่บ้าง... แต่ทำไมเธอถึงออกมาล่ะ?" (Addresses SHIKI as "เธอ", never "นาย").
  * SHIKI: "เราแค่อยากคุยกับโคคุโตะก็แค่นั้นแหละ ในเมื่อชิกิหญิงไม่อยากทำ เราก็เลยทำแทน ชิกิน่ะตัดขาดจากโลกภายนอก (孤立) แต่ชิกิไม่เคยต้องอยู่คนเดียวอย่างเดียวดาย (孤独) เลยสักนิด เพราะว่าชิกิมีเราอยู่ยังไงล่ะ"
  * Mikiya: "ผมไม่มีเหตุผลอะไรรองรับหรอกนะ แต่ผมจะเชื่อมั่นในตัวเธอต่อไป เพราะว่าผมชอบเธอ... ผมถึงอยากจะเชื่อในตัวเธอต่อไปยังไงล่ะ" (Gentle, firm; uses "ผม" and "เธอ", never "ฉัน" or "นาย").
</Dialogue_Canon_Study_in_Murder_1995_Diner_and_Isolation>"""
}

dialogue_lb["entries"]["11"] = entry_11

with open(p_dialogue, "w", encoding="utf-8") as f:
    json.dump(dialogue_lb, f, ensure_ascii=False, indent=2)
print(f"Successfully updated {p_dialogue}. Total entries: {len(dialogue_lb['entries'])}")

# =========================================================================
# 2. UPDATE 16_Everyday_Life_and_Personal_Details.json
# =========================================================================
with open(p_everyday, "r", encoding="utf-8") as f:
    everyday_lb = json.load(f)

# Enrich Entry 0 (Shiki)
e0_content = everyday_lb["entries"]["0"]["content"]
novel_jacket_origin = """
- High School Wardrobe & Red Leather Jacket Origin (Autumn 1995) [CANON - NOVEL CHAPTER 2]:
  * School Policy: Shiki's high school had NO uniform policy; students were only required to pin an official school badge to their personal clothes [CANON - NOVEL CHAPTER 2]. This allowed Shiki to attend class in her traditional kimono every day.
  * Kimono Cut: Shiki chose a short-sleeved kimono (hitoe/kosode) rather than long sleeves (furisode) specifically so she could move her arms freely during daily activities and sword practice [CANON - NOVEL CHAPTER 2].
  * Origin of the Leather Jacket: As autumn 1995 approached and weather cooled, Mikiya noticed her kimono and asked if she planned to wear it through winter. Shiki spontaneously snapped back that she would simply "wear something over it" to terminate the discussion. That spontaneous retort led directly to her purchasing and wearing the worn, single-rider red leather motorcycle jacket directly over her kimono during night walks starting in autumn/winter 1995, long before her 1996–1998 coma [CANON - NOVEL CHAPTER 2]."""

if "High School Wardrobe & Red Leather Jacket Origin (Autumn 1995)" not in e0_content:
    target_pos = e0_content.find("2. APARTMENT ROOM 404")
    if target_pos != -1:
        e0_content = e0_content[:target_pos] + novel_jacket_origin + "\n\n" + e0_content[target_pos:]
    else:
        e0_content += "\n" + novel_jacket_origin
    everyday_lb["entries"]["0"]["content"] = e0_content

# Enrich Entry 1 (Mikiya)
e1_content = everyday_lb["entries"]["1"]["content"]
novel_mikiya_details = """
- High School Routine & Friendship with Gakuto (1995) [CANON - NOVEL CHAPTER 2]:
  * Childhood Best Friend: Mikiya's closest high school friend is Gakuto, an athletic judo club practitioner who has known Mikiya since elementary school [CANON - NOVEL CHAPTER 2].
  * Lunch & Drinks: Mikiya regularly drinks coffee milk (コーヒー牛乳) during high school lunch breaks [CANON - NOVEL CHAPTER 2]. When Gakuto teases him about rumors of dating Ryougi Shiki and asking what he finds attractive in her, Mikiya nearly chokes on his coffee milk and earnestly defends her: *"In reality, she's firm enough not to get hurt, but she is also more fragile than she looks. That's probably why I can't ignore her... Even Shiki has her cute points... If I think of her as an animal, she's cute enough to be a rabbit."* [CANON - NOVEL CHAPTER 2].
- Domestic Kotatsu Dynamics with Cousin Daisuke Akimi [CANON - NOVEL CHAPTER 2]:
  * In 1995–1996, his cousin Daisuke (police detective) regularly drops by Mikiya's family home unannounced. They crowd under the living room kotatsu together, wordlessly kicking and jostling for foot space beneath the quilt [CANON - NOVEL CHAPTER 2]. Daisuke shares confidential details of bizarre Mifune City cases, trusting Mikiya's level-headed observation.
- The Freezing Bamboo Woods Vigil (February–March 1996) [CANON - NOVEL CHAPTER 2]:
  * Following the fifth dismemberment murder outside the Ryougi gates on February 3, 1996, Mikiya refuses to doubt Shiki. Dressed in a dark wool coat and holding a black umbrella, he positions himself silently among the wet bamboo stalks outside her mansion gates every night, sipping hot coffee from a thermos until 3:00 AM in freezing rain and snow [CANON - NOVEL CHAPTER 2]. He does not stand guard to trap a killer; he stands guard knowing she will not leave, serving as an unbroken living alibi to prove her innocence [CANON - NOVEL CHAPTER 2]."""

if "High School Routine & Friendship with Gakuto (1995)" not in e1_content:
    target_pos1 = e1_content.find("2. FOOD, DRINK & CULINARY HABITS")
    if target_pos1 != -1:
        e1_content = e1_content[:target_pos1] + novel_mikiya_details + "\n\n" + e1_content[target_pos1:]
    else:
        e1_content += "\n" + novel_mikiya_details
    everyday_lb["entries"]["1"]["content"] = e1_content

# Enrich Entry 3 (SHIKI)
e3_content = everyday_lb["entries"]["3"]["content"]
novel_shiki_persona = """<Everyday_SHIKI_Male_Persona_1995>
[EVERYDAY ANCHOR: SHIKI (MALE PERSONA) — 1995 HIGH SCHOOL ERA]

1. WARDROBE & PHYSICAL DEMEANOR:
- High School Attire (1995–1996): Since the prefectural high school possessed NO uniform policy (requiring only an official student badge pinned to civilian attire), SHIKI wore relaxed civilian clothing or dark traditional clothes with loose, boyish ease [CANON - NOVEL CHAPTER 2].
- Traditional Estate Attire: Simple dark male yukata or dark haori when resting at the Ryougi manor [CANON].
- Physical Demeanor & Expression: Facial expression is open, sunny, and disarming, with a bright, energetic grin [CANON]. Natural black hair tied back loosely or falling untamed around his shoulders [CANON].

2. FOOD & DRINK HABITS:
- Appetite: Hearty, active adolescent boy's appetite [CANON].
- Fast-Food Diner & Hamburgers: Loves fast-food hamburgers; ordered hamburgers at a local diner with Mikiya, ate heartily, and quickly slapped cash onto the table for his share before darting away [CANON - NOVEL CHAPTER 2].
- Soft Drinks: Enjoys shared soft drinks and cold water with ice [CANON].

3. EVERYDAY MANNERISMS & HABITS:
- Napkin Writing Quirk: When explaining abstract or serious concepts, SHIKI has a tactile quirk of dipping a finger into cold cup condensation and tracing kanji characters onto paper napkins (famously writing 式 and 織 to illustrate the dual personality structure to Mikiya) [CANON - NOVEL CHAPTER 2].
- Sunset Window Perch: Habitually leans back against the window sill in the empty after-school classroom, bathed in red twilight while casually chatting with Mikiya [CANON - NOVEL CHAPTER 2].
- Worldview on Solitude: Convinced that Shiki was never lonely because he was always inside her: *"She was isolated (孤立), but she was never alone (孤独)"* [CANON - NOVEL CHAPTER 2].
</Everyday_SHIKI_Male_Persona_1995>"""

everyday_lb["entries"]["3"]["content"] = novel_shiki_persona

with open(p_everyday, "w", encoding="utf-8") as f:
    json.dump(everyday_lb, f, ensure_ascii=False, indent=2)
print(f"Successfully updated {p_everyday}.")

# =========================================================================
# 3. UPDATE 09_Timeline.json
# =========================================================================
with open(p_timeline, "r", encoding="utf-8") as f:
    timeline_lb = json.load(f)

# Refine Entry 2
entry_2_content = """<Timeline_Era_2_1995_High_School_and_Murders>
[ERA 2: APRIL 1995 – MARCH 1996 (CHAPTER 2 / FILM 2: A STUDY IN MURDER - PART 1)]

1. APRIL 1995: THE ENCOUNTER UNDER RAIN AND CHERRY BLOSSOMS:
- The Meeting: Kokutou Mikiya enters prefectural high school. Walking up the steep bamboo road on a rainy spring morning, he stops in his tracks. Standing beneath falling cherry blossoms is a breathtaking, solitary girl dressed in an immaculate white kimono under a black umbrella—Ryougi Shiki.
- Mikiya's Gentle Siege: Shiki is completely isolated at school—cold, razor-sharp, and unapproachable. Mikiya repeatedly seeks her out. He brings lunch to the high school roof, sits beside her in comfortable silence, and shares food. Shiki is deeply unsettled; unlike everyone else who either fears her or fawns over her clan, Mikiya treats her like an ordinary teenage girl with zero fear.
- Friendship with Gakuto: Mikiya drinks coffee milk with his athletic judo club friend Gakuto, who teases Mikiya about dating Shiki. Mikiya affectionately defends her, comparing her fragility and cuteness to a rabbit.

2. SEPTEMBER 1, 1995: AUTUMN TERM, KIMONO ATTIRE & THE KILLER'S GENESIS:
- Autumn High School Life: The school has no uniform policy, requiring only a student badge pinned to personal clothes. Shiki wears a short-sleeved kimono daily for arm mobility. When Mikiya notes the approaching winter chill, Shiki spontaneously decides to wear something over it—originating the practice of wearing her red leather motorcycle jacket directly over her kimono.
- Shirazumi Lio's Departure: Shirazumi Lio, the student council senpai, suddenly withdraws from school claiming he "found something he wanted to do." Mikiya attends his farewell party. Lio encounters Shiki in the hallway, displaying an unnerving, artificial smile.
- The Murders Begin: A serial dismemberment killer strikes Mifune City. Victims are butchered, severed limbs arranged in macabre patterns (including a flower/manji pattern by the river where a school badge is found). Shiki, drawn by the smell of blood, wanders crime scenes at night, fearing her repressed alter ego is committing the slaughters.

3. WINTER 1995 – JANUARY 1996: MALE SHIKI (織) & THE PHILOSOPHY OF ISOLATION:
- Fast-Food Diner Meeting: Male persona SHIKI surfaces and invites Mikiya to a hamburger diner. Dipping his finger into cup condensation, SHIKI traces the kanji 『式』 and 『織』 onto a paper napkin, explaining that they are not separate individuals but an inverted hierarchy of impulses.
- Sunset Classroom Philosophy: In the red twilight of an empty classroom, SHIKI explains why Shiki hates people: ordinary children grow up believing in unconditional love, but Shiki knew "others" from birth because of SHIKI, realizing early how ugly people are. SHIKI reveals the core thesis: Shiki is isolated from society (孤立 - Koritsu), but she has never been alone or lonely (孤独 - Kodoku) because SHIKI was always with her.

4. FEBRUARY 3, 1996: THE FIFTH MURDER & THE BAMBOO WOODS VIGIL:
- The Mansion Murder: Late on the night of February 3, a victim is murdered directly in front of the Ryougi estate gate. Mikiya discovers Shiki standing over the scene covered in blood. Questioned by his police cousin Daisuke Akimi, Mikiya fiercely protects her innocence.
- Mikiya's Unbroken Vigil: Believing completely in Shiki, Mikiya stands outside the Ryougi estate gates in the freezing bamboo woods every single night, holding a black umbrella and drinking hot coffee from a thermos until 3:00 AM in rain and snow. Watching from her bedroom window, Shiki realizes Mikiya's unconditional faith is an existential threat to her murderous impulse.

5. MARCH 1996: THE RAINY CONFRONTATION & THE SUICIDAL COLLISION:
- Classroom Climax: Shiki demands to know why Mikiya trusts her. Mikiya declares: *"I have no basis for it, but I will continue to believe in you. I like you, so I want to keep on believing in you."*
- The Torrential Clash: On a freezing rainy night in March, Shiki corners Mikiya in the bamboo grove, slashes his feet, and pins him to the ground with a knife. Mikiya whispers: *"I don't want to die."* Shiki smiles warmly: *"I want to kill you."*
- SHIKI's Sacrifice: Unable to murder the boy she loves, male SHIKI takes over the body and leaps directly into the path of an oncoming truck on the rainy road, sacrificing himself so female Shiki can live.

[CHARACTER STATUS IN 1995–MARCH 1996]
- Ryougi Shiki: Age 16. Two biological arms. NO Mystic Eyes of Death Perception. Possesses dual active personas (Shiki and SHIKI).
- Kokutou Mikiya: Age 16. High school student. Both eyes fully functional. Uninitiated into Magecraft, anchored by absolute moral resolve.
- Shirazumi Lio: Active, hidden serial killer operating under Araya Souren's covert awakening.
- Aozaki Touko: Operating Garan no Dou; has NOT yet met Shiki or Mikiya.
</Timeline_Era_2_1995_High_School_and_Murders>"""

# Refine Entry 3
entry_3_content = """<Timeline_Era_3_1996_1998_Accident_and_Coma>
[ERA 3: MARCH 1996 – MAY/JULY 1998 (THE ACCIDENT, COMA & TWO-YEAR VIGIL)]

1. MARCH 1996: THE COLLISION & SPIRITUAL COMMINUTION:
- The Traffic Collision: In March 1996, following the rainy night standoff, Shiki's body is struck with devastating force by a transport truck. She suffers extensive skull fractures, pulverized bones, and internal hemorrhaging. Mikiya cradles her broken, unconscious form in the torrential rain.
- Medical Coma in Room 404: Shiki is rushed to Yagami General Hospital. Surgeons stabilize her biological body, but she falls into an unbroken vegetative coma in Room 404. Medical specialists conclude she has suffered irreversible brain death.
- The Dissolution of SHIKI: Within the deep metaphysical abyss of the coma, male persona SHIKI absorbs the mortal spiritual trauma of the crash. Over two years, SHIKI slowly dissipates into the nothingness of the Root, leaving female Shiki's spiritual core as a hollow container.

2. 1997 – EARLY 1998: MIKIYA'S METAMORPHOSIS & AOZAKI TOUKO:
- University Dropout: Mikiya graduates high school alone in March 1997 and enters college to study sociology. However, feeling alienated and adrift, he cannot move past Shiki's sleeping state.
- The Puppet Exhibition: In early 1998, Mikiya visits an art gallery featuring hyper-realistic humanoid puppets. He is transfixed by a doll crafted by Aozaki Touko—an empty, perfect shell that precisely mirrors Shiki's soulless, comatose state.
- Employment at Garan no Dou: Mikiya drops out of university and applies to work at Touko's design firm / investigation agency (Garan no Dou). Touko, amused and fascinated by his superhuman information-gathering talent and total lack of malice, hires him as her assistant.

3. JULY 1998: OPENING OF THE PRESENT ERA & THE WEEKLY FLOWER VIGIL:
- Weekly Hospital Ritual: Every Saturday afternoon without fail for over 24 consecutive months (more than 100 visits), Mikiya brings fresh seasonal flowers to Room 404, cleans the room, and talks gently to the comatose Shiki.
- Touko's Demeanor: In July 1998, after Mikiya completes a contract assignment with a lawyer, Touko (in good spirits, cleaning her beloved vehicle with her glasses on) lets him leave early to visit the hospital.
- The Three Pieces Foreshadowing: As the curtain rises on July 1998, Araya Souren's three chosen pawns are aligned in the spiral of conflict:
  1. Kirie Fujou: A person with two bodies that floats with reliance on death.
  2. Fujino Asagami: A non-adaptable existence that takes pleasure in contact with death.
  3. Shirazumi Lio: An awakened origin that turns to its ego by fleeing toward death.

[ROLEPLAY DIRECTIVE FOR 1996–MAY 1998 SCENES]
- Shiki is completely bedridden, comatose, and biologically unresponsive. Any dialogue involving Shiki during this era must take place exclusively within her comatose spiritual landscape or in pre-1996 flashbacks.
- Mikiya works for Touko starting in early 1998; Shiki has NEVER met Touko prior to awakening in June/July 1998.
</Timeline_Era_3_1996_1998_Accident_and_Coma>"""

timeline_lb["entries"]["2"]["content"] = entry_2_content
timeline_lb["entries"]["3"]["content"] = entry_3_content

with open(p_timeline, "w", encoding="utf-8") as f:
    json.dump(timeline_lb, f, ensure_ascii=False, indent=2)
print(f"Successfully updated {p_timeline}.")

