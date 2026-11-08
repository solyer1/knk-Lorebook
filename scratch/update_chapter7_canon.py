# -*- coding: utf-8 -*-
"""
Applies Chapter 7 (A Study in Murder Part 2 / 殺人考察(後)) and Epilogue (Kara no Kyoukai / 空の境界) novel canon expansions to:
- Kara No/01_Shiki.json (Entry 0: Murder vs Slaughter, Entry 2: Void Shiki Epilogue & Eye healing refusal)
- Kara No/02_Mikiya.json (Entry 0 & 3: Left eye blindness, long bangs, rain vow, healing refusal)
- Kara No/04_Other_Characters.json (Entry 4: Shirazumi Lio's climax, Bloodchip, and demise)
- Kara No/09_Timeline.json (Entries 9 & 10: Complete Chapter 7 & Epilogue novel chronology)
- Kara No/13_Dialogue_Examples.json (Adds Entry 16: Dialogue_Canon_Study_in_Murder_Part_2_and_Void_Epilogue)
- Kara No/16_Everyday_Life_and_Personal_Details.json (Entry 1: Mikiya's blinded eye styling, Entry 4: Void Shiki snow encounter)
"""
import json
import os

p_shiki = r"d:\Personalise\Homemad\Lorebook\Nasuverse\Kara No\01_Shiki.json"
p_mikiya = r"d:\Personalise\Homemad\Lorebook\Nasuverse\Kara No\02_Mikiya.json"
p_other = r"d:\Personalise\Homemad\Lorebook\Nasuverse\Kara No\04_Other_Characters.json"
p_timeline = r"d:\Personalise\Homemad\Lorebook\Nasuverse\Kara No\09_Timeline.json"
p_dialogue = r"d:\Personalise\Homemad\Lorebook\Nasuverse\Kara No\13_Dialogue_Examples.json"
p_everyday = r"d:\Personalise\Homemad\Lorebook\Nasuverse\Kara No\16_Everyday_Life_and_Personal_Details.json"

# =========================================================================
# 1. UPDATE 01_Shiki.json
# =========================================================================
with open(p_shiki, "r", encoding="utf-8") as f:
    shiki_lb = json.load(f)

# Entry 0: Murder vs. Slaughter
e0_s = shiki_lb["entries"]["0"]["content"]
murder_slaughter_addition = """
- The Core Philosophy: Murder (殺人) vs. Slaughter (殺戮) [CANON - NOVEL CHAPTER 7]:
  * Nasu's Golden Rule: *"A human can only truly murder one person in their entire lifetime"* (人は一生に一度しか人を殺せない).
  * Murder (殺人 - Satsujin): Recognizes the victim as a fellow human being with equal weight of existence, intentionally terminating their life and permanently consuming a piece of the killer's own soul. The sin and memory of the victim are borne forever.
  * Slaughter (殺戮 - Satsuriku): The unthinking butchery of multiple beings like a wild animal or natural disaster, lacking mutual human recognition (as demonstrated by Shirazumi Lio).
  * Shiki's Sole Murder: Throughout her entire life, Shiki engaged in self-defense and eliminated non-human monsters, familiars, and spirits. Her single, irreversible act of true human murder was slaying Shirazumi Lio in February 1999 to protect Kokutou Mikiya."""

if "The Core Philosophy: Murder (殺人) vs. Slaughter (殺戮)" not in e0_s:
    pos = e0_s.find("[INTERNAL CONFLICT & THE URGE TO KILL]")
    if pos != -1:
        e0_s = e0_s[:pos] + murder_slaughter_addition + "\n\n" + e0_s[pos:]
    else:
        e0_s += "\n\n" + murder_slaughter_addition
    shiki_lb["entries"]["0"]["content"] = e0_s

# Entry 2: Void Shiki & The March 1999 Epilogue
e2_v = shiki_lb["entries"]["2"]["content"]
void_epilogue_addition = """
- The March 1999 Epilogue Encounter & The Refusal of Miracles [CANON - NOVEL EPILOGUE]:
  * In March 1999, exactly four years after Mikiya first encountered Shiki, Void Shiki manifested on the snowy hill road.
  * Speaking with soft, warm, feminine grace, she conversed with Mikiya about the nature of humanity, the Root, and the preciousness of mundane life.
  * Omnipotent Benevolence: Void Shiki offered to grant Mikiya any impossible miracle—including completely healing and restoring his blinded left eye.
  * Mikiya's Refusal: Mikiya gently declined, stating that the blinded eye was the sacred, irreplaceable physical proof of the journey he shared with Shiki. Deeply moved, Void Shiki smiled with tranquil affection and dissolved back into the falling snow."""

if "The March 1999 Epilogue Encounter & The Refusal of Miracles" not in e2_v:
    e2_v += "\n\n" + void_epilogue_addition
    shiki_lb["entries"]["2"]["content"] = e2_v

with open(p_shiki, "w", encoding="utf-8") as f:
    json.dump(shiki_lb, f, ensure_ascii=False, indent=2)
print(f"Successfully updated {p_shiki}.")

# =========================================================================
# 2. UPDATE 02_Mikiya.json
# =========================================================================
with open(p_mikiya, "r", encoding="utf-8") as f:
    mikiya_lb = json.load(f)

# Entry 0: Permanent Physical Profile (Blinded Left Eye)
e0_m = mikiya_lb["entries"]["0"]["content"]
mikiya_eye_addition = """
- Post-February 1999 Physical Profile (Blinded Left Eye & Long Bangs) [CANON - NOVEL CHAPTER 7]:
  * During his torture by Shirazumi Lio in February 1999, Mikiya suffered catastrophic trauma resulting in the permanent loss of vision in his left eye.
  * He allowed his black hair to grow out, especially his front bangs, deliberately draping them over the left side of his face to conceal the damaged eye.
  * When Void Shiki offered to supernaturally restore his eye in March 1999, Mikiya flatly refused, cherishing the blindness as an eternal physical bond linking him to Shiki's salvation."""

if "Post-February 1999 Physical Profile (Blinded Left Eye & Long Bangs)" not in e0_m:
    pos = e0_m.find("Mikiya represents what Touko calls")
    if pos != -1:
        e0_m = e0_m[:pos] + mikiya_eye_addition + "\n\n" + e0_m[pos:]
    else:
        e0_m += "\n\n" + mikiya_eye_addition
    mikiya_lb["entries"]["0"]["content"] = e0_m

# Entry 3: The Rain Vow
e3_m = mikiya_lb["entries"]["3"]["content"]
rain_vow_addition = """
- The Rain Vow: 'I Will Never Forgive You' (February 1999) [CANON - NOVEL CHAPTER 7]:
  * When Mikiya dragged his bleeding, blinded body from the warehouse basement to find Shiki sobbing in the rain over Lio's corpse, Shiki confessed in despair: *"I am a murderer."*
  * Mikiya embraced her tightly, uttering his supreme vow: *"Shiki. For as long as you live, I will never forgive you."*
  * Refusing to forgive her means Mikiya refuses to let her atone in solitary despair; instead, he bound his soul to hers, choosing to carry the moral weight of her murder alongside her until the day they die."""

if "The Rain Vow: 'I Will Never Forgive You'" not in e3_m:
    e3_m += "\n\n" + rain_vow_addition
    mikiya_lb["entries"]["3"]["content"] = e3_m

with open(p_mikiya, "w", encoding="utf-8") as f:
    json.dump(mikiya_lb, f, ensure_ascii=False, indent=2)
print(f"Successfully updated {p_mikiya}.")

# =========================================================================
# 3. UPDATE 04_Other_Characters.json (Entry 4: Shirazumi Lio)
# =========================================================================
with open(p_other, "r", encoding="utf-8") as f:
    other_lb = json.load(f)

e4_lio = other_lb["entries"]["4"]["content"]
lio_novel_addition = """
- Bloodchip Distribution, Cannibalism & Demise (February 1999) [CANON - NOVEL CHAPTER 7]:
  * In February 1999, Lio returned to Mifune City, distributing the psychotropic narcotic 'Bloodchip' to foster an occult bloodlust throughout the underworld.
  * Believing Shiki was an identical predatory beast, Lio murdered linguist magus Kurogiri Satsuki and abducted Kokutou Mikiya, gouging out Mikiya's left eye in an attempt to break Mikiya's unconditional love.
  * Confronting Shiki in the abandoned warehouse cannabis field, Lio fought with beast-like predation, spraying blood and biting like a rabid animal, before Shiki cleanly executed him—marking her sole act of true human murder."""

if "Bloodchip Distribution, Cannibalism & Demise" not in e4_lio:
    pos = e4_lio.find("[PERSONALITY & PREDATORY PSYCHOLOGY]")
    if pos != -1:
        e4_lio = e4_lio[:pos] + lio_novel_addition + "\n\n" + e4_lio[pos:]
    else:
        e4_lio += "\n\n" + lio_novel_addition
    other_lb["entries"]["4"]["content"] = e4_lio

with open(p_other, "w", encoding="utf-8") as f:
    json.dump(other_lb, f, ensure_ascii=False, indent=2)
print(f"Successfully updated {p_other}.")

# =========================================================================
# 4. UPDATE 09_Timeline.json (Entries 9 & 10)
# =========================================================================
with open(p_timeline, "r", encoding="utf-8") as f:
    timeline_lb = json.load(f)

# Entry 9: Chapter 7 Climax
entry_9_content = """<Timeline_Era_9_February_1999_A_Study_in_Murder_Part_2>
[ERA 9: FEBRUARY 1999 (CHAPTER 7 / FILM 7: A STUDY IN MURDER - PART 2) - THE CLIMAX]

1. THE RETURN OF THE PREDATOR & BLOODCHIP:
- The Slaughter Resumes: In early February 1999, the exact dismemberment murders from 1995 resume in Mifune City. Victims are butchered and partially consumed.
- Shirazumi Lio's Predation: Lio (awakened to the Origin of Consumption) emerges, distributing the 'Bloodchip' narcotic. Lio murders Kurogiri Satsuki, seeking to prove that Shiki is a monster identical to himself.
- Murder vs. Slaughter: Shiki and Touko discuss the killings, articulating Nasu's core thesis: *"Murder and slaughter are different. A human can only truly murder one person in their entire lifetime."*

2. THE ABDUCTION & BLINDING OF MIKIYA:
- The Kidnapping: Mikiya tracks down Lio to save his former schoolmate without weapons. Lio captures Mikiya, torturing him and permanently destroying his left eye. Lio leaves Mikiya bleeding in a cellar, believing him dead.
- Shiki's Wrath: Discovering Mikiya's bloodied coat, Shiki believes Mikiya has been killed. Her desire to kill transforms from a detached instinct into scorching, personal vengeance.

3. THE WAREHOUSE CLASH & SHIKI'S SOLE MURDER:
- The Beast Unleashed: Shiki corners Lio in an abandoned warehouse. Lio fights like a rabid predatory animal, biting and clawing. Shiki dissects him with her knife, killing Shirazumi Lio—her first and only act of human murder.

4. THE RAIN VOW & THE CRUTCH:
- Mikiya's Survival: Bleeding from his ruined left eye, Mikiya crawls into the rain to find Shiki weeping in despair: *"I killed him... I am a murderer."*
- The Eternal Vow: Mikiya embraces her tightly, uttering his unforgettable vow: *"Shiki. For as long as you live, I will never forgive you."* Binding their souls together, Mikiya vows to carry the weight of her sin forever.
- Walking Together: Post-hospital, Mikiya grows out his bangs to cover his blinded left eye. He playfully demands that Shiki act as his 'crutch' while walking, openly declaring his selfish choice to look after her forever. Shiki blushes, silently yielding to his love.
</Timeline_Era_9_February_1999_A_Study_in_Murder_Part_2>"""

# Entry 10: Epilogue & Future
entry_10_content = """<Timeline_Era_10_March_1999_Epilogue_and_Future>
[ERA 10: MARCH 1999 & POST-STORY (EPILOGUE / MIRAI FUKUIN / 2008–2010)]

1. MARCH 1999: THE EPILOGUE IN THE FALLING SNOW:
- The Snowy Bamboo Road: Exactly four years after first meeting Shiki in April 1995, Kokutou Mikiya walks along the snowy hill road, his left eye bandaged and vision permanently lost.
- Manifestation of Void Shiki (`「　」` / Root Shiki): Emerging from the falling snow in a pristine white furisode kimono is the third personality, Void Shiki.
- Nature of the Root: Void Shiki speaks with gentle, feminine, motherly grace. Connected directly to the Swirl of the Root, she embodies the omnipotence of Akasha, yet experiences the universe as a fleeting, beautiful dream.
- Refusal of the Miracle: Void Shiki offers to supernaturally restore and heal Mikiya's blinded left eye. Mikiya gently declines, declaring the wound to be the sacred physical proof of the journey he shared with Shiki. Void Shiki smiles with tranquil warmth and fades into the snow, leaving female Shiki to walk beside Mikiya.

2. AUGUST 1998 – 2010: MIRAI FUKUIN & THE ADULT ERA:
- August 1998 (Mirai Fukuin): Mikiya meets precognitive junior high school student Seo Shizuno at a cafe (who foretells his future eye injury), while Shiki confronts bomber Kuramitsu Meruka (Mitsuru Kamekura).
- 2008–2010 (Adult Era): Mikiya and Shiki are happily married, living together in domestic peace. They have a daughter, Ryougi Mana, who inherits Shiki's beauty and adores her father. Mitsuru Kamekura works under the Ryougi family as an agency investigator and author.
</Timeline_Era_10_March_1999_Epilogue_and_Future>"""

timeline_lb["entries"]["9"]["content"] = entry_9_content
timeline_lb["entries"]["10"]["content"] = entry_10_content

with open(p_timeline, "w", encoding="utf-8") as f:
    json.dump(timeline_lb, f, ensure_ascii=False, indent=2)
print(f"Successfully updated {p_timeline}.")

# =========================================================================
# 5. UPDATE 13_Dialogue_Examples.json (Adds Entry 16)
# =========================================================================
with open(p_dialogue, "r", encoding="utf-8") as f:
    dialogue_lb = json.load(f)

dialogue_lb["description"] = (
    "Dialogue, voice, subtext, and characterization demonstration module for SillyTavern roleplay. "
    "Contains 17 focused scene demonstrations showing natural cadence, physical gestures, conversational restraint, "
    "and distinct voices for Shiki, male SHIKI, Void Shiki (「　」), Mikiya, Touko, Araya, Tomoe, Fujino, Azaka, Satsuki, "
    "and Fate crossover interactions, directly derived and verified from Kinoko Nasu's canonical light novel prose."
)

entry_16 = {
    "uid": 16,
    "name": "Dialogue_Canon_Study_in_Murder_Part_2_and_Void_Epilogue",
    "comment": "Dialogue_Canon_Study_in_Murder_Part_2_and_Void_Epilogue",
    "order": 146,
    "key": [
        "A Study in Murder Part 2 dialogue",
        "Void Shiki Epilogue dialogue",
        "Murder vs slaughter dialogue",
        "Rain vow dialogue",
        "Mikiya blinded left eye dialogue",
        "Snowy road dialogue",
        "บทสนทนาคดีฆาตกรรมบทหลัง",
        "บทสนทนาชิกิแห่งความว่างเปล่า",
        "การฆ่าคนกับการเข่นฆ่า",
        "คำสาบานใต้สายฝน",
        "ตาซ้ายของมิกิยะ",
        "บทสนทนาส่งท้ายบนเนินหิมะ"
    ],
    "keysecondary": [
        "Mikiya",
        "Shiki",
        "Void Shiki",
        "Lio",
        "rain vow",
        "left eye",
        "Root",
        "Epilogue",
        "มิกิยะ",
        "ชิกิ",
        "ชิกิว่างเปล่า",
        "ลิโอ",
        "คำสาบาน",
        "ตาซ้าย",
        "รากเหง้า",
        "บทส่งท้าย"
    ],
    "content": """<Dialogue_Canon_Study_in_Murder_Part_2_and_Void_Epilogue>
[DEMONSTRATION STATUS]
Canonically verified demonstration derived directly from Kinoko Nasu's novel prose in Chapter 7 (*A Study in Murder Part 2*) and the *Epilogue (The Boundary of Emptiness)*.

[SCENE 1: THE RAINY CLIMAX & THE ETERNAL VOW (FEBRUARY 1999)]
Torrential winter rain pounds against the mud of the warehouse clearing. Shirazumi Lio lies lifeless in the dark. Shiki sits collapsed beside his corpse, her knife falling limply from her hand. Blood drips like crimson tears down her pale face.

Crawling out from the flooded cellar, his clothes torn and blood streaming from his permanently destroyed left eye, Kokutou Mikiya reaches her side.

"I... killed Shirazumi," Shiki whispered, her voice hollow, cracking like a frightened child on the verge of weeping. "With this, I've lost everything. I am... a murderer."

Mikiya didn't lecture or condemn her. With the last of his strength, he pulled her shivering body into his arms, embracing her so tightly it felt as though both of them would cease breathing.

"I told you, didn't I? We humans must never take the life of another person," Mikiya whispered into her soaked hair, his voice choked with blood and tears. "Shiki... for as long as you live, I will never forgive you."

He would never forgive her—which meant he would never let her bear the burden of murder alone. He bound his life to her sin forever.

---

[SCENE 2: THE WALKING CRUTCH (LATE FEBRUARY 1999)]
Descending the gentle slope toward the station. Mikiya's dark hair has grown out, long bangs draped over the left side of his face to hide his blinded eye.

"Your left eye," Shiki murmured quietly, looking down at his feet.

Mikiya smiled with cheerful unconcern. "Ruined, just like Shizuno predicted. For the next week until I get used to walking like this, I'll be using you as my crutch, okay?"

"The hell? Why me?"

"Because I want you to," Mikiya said with complete earnestness. "No matter how much you resist, I've made the selfish choice to take care of you forever."

Shiki turned her face away, blushing intensely, swallowing down her usual prickly retort:

"...Well, I don't mind."

---

[SCENE 3: THE SNOWY HILL ROAD & VOID SHIKI (MARCH 1999)]
Snow falls softly upon the bamboo hill road. A breathtaking figure in a pristine white furisode kimono stands under the snow—Void Shiki (`「　」`).

"Good evening, Kokutou-san," she greeted him with a voice like warm silk, smiling with enchanting femininity. "It's been a long time, hasn't it?"

"You're... Shiki, aren't you?" Mikiya asked gently.

"Yes, but also no. I am the consciousness of this physical body... the one sleeping within the void," Void Shiki explained softly, gazing at the falling flakes. "Kokutou-san, you've suffered so much. If you wish, I can grant you any miracle. I can rewrite the world... or I can restore that left eye of yours back to perfection in an instant."

Mikiya looked into her dreamlike eyes and smiled with gentle, unshakable resolve.

"Thank you, Shiki. But I don't need any wishes granted. This wound... is the proof of the path I've walked with Shiki."

Void Shiki's smile deepened with infinite, quiet warmth.

"I thought you would say that," she whispered softly, her form gradually blurring into the dancing white snow. "Take care of Shiki, Kokutou-san."

[CHARACTER VOICE & RHYTHM ANALYSIS]
- Void Shiki (「　」): Gentle, soft-spoken, feminine, warm, motherly. Speaks with refined cadence without Shiki's tomboyish harshness. Uses gentle "ฉัน".
- Kokutou Mikiya: Pure, immovable, selfless. His vow of "never forgiving" is the ultimate expression of devoted love—refusing to let her suffer alone. Uses polite "ผม" (never "ฉัน").
- Ryougi Shiki: Prickly, vulnerable, easily embarrassed when confronted with Mikiya's open affection.

[THAI LOCALIZATION & PRONOUN DISCIPLINE]
- Male First-Person Prohibition: Mikiya MUST NEVER use "ฉัน" in Thai dialogue. Uses polite, gentle "ผม" or zero-anaphora. Addresses Shiki / Void Shiki as "เธอ" or "ชิกิ", never "นาย".
- Void Shiki's Tone: Gentle, warm, polite feminine voice with natural "ฉัน".
- Thai Dialogue Localization Sample:
  * Shiki: "ฉัน... ฆ่าชิราซุมิไปแล้ว... ตอนนี้ฉันกลายเป็นฆาตกรไปแล้วจริง ๆ" (Hollow, weeping; uses "ฉัน").
  * Mikiya: "ผมบอกเธอแล้วไม่ใช่เหรอ ว่าคนเราน่ะต้องไม่พรากชีวิตของคนอื่น... ชิกิ ตราบใดที่เธอยังมีชีวิตอยู่ ผมจะไม่มีวันให้อภัยเธอเด็ดขาด" (Tearful, resolute embrace; uses "ผม" and "เธอ", never "ฉัน").
  * Mikiya: "ระหว่างที่ตายังไม่ชิน ผมคงต้องพึ่งเธอเป็นไม้เท้าคอยพยุงเดินแล้วล่ะนะ... ไม่ว่าเธอจะปฏิเสธยังไง ผมก็ตัดสินใจอย่างเห็นแก่ตัวไปแล้วว่าจะดูแลเธอไปตลอดชีวิต" (Gentle, teasing; uses "ผม" and "เธอ").
  * Shiki: "...ก็ ไม่ได้ว่าอะไรสักหน่อยนี่" (Blushing, turning away).
  * Void Shiki: "สวัสดีตอนค่ำค่ะ โคคุโตะซัง... ถ้าเธอต้องการ ฉันจะมอบปาฏิหาริย์ให้ก็ได้นะ จะรักษาตาซ้ายของเธอให้กลับมามองเห็นเป็นปกติในพริบตาก็ยังได้" (Warm, silk-like feminine tone).
  * Mikiya: "ขอบคุณนะ ชิกิ แต่ผมไม่ต้องการพรใด ๆ หรอกครับ บาดแผลนี้... คือเครื่องพิสูจน์ถึงเส้นทางที่ผมได้เดินร่วมกับเธอมาตลอด"
</Dialogue_Canon_Study_in_Murder_Part_2_and_Void_Epilogue>"""
}

dialogue_lb["entries"]["16"] = entry_16

with open(p_dialogue, "w", encoding="utf-8") as f:
    json.dump(dialogue_lb, f, ensure_ascii=False, indent=2)
print(f"Successfully updated {p_dialogue}. Total entries: {len(dialogue_lb['entries'])}")

# =========================================================================
# 6. UPDATE 16_Everyday_Life_and_Personal_Details.json (Entries 1 & 4)
# =========================================================================
with open(p_everyday, "r", encoding="utf-8") as f:
    everyday_lb = json.load(f)

# Entry 1: Mikiya Left Eye & Bangs
e1_m = everyday_lb["entries"]["1"]["content"]
mikiya_style_update = """
- Post-1999 Hair & Blinded Left Eye Grooming [CANON - NOVEL CHAPTER 7]:
  * Following the trauma inflicted by Shirazumi Lio in February 1999, Mikiya permanently lost vision in his left eye [CANON - NOVEL CHAPTER 7].
  * He grew his front bangs longer, styling them so they naturally sweep down over the left side of his face to shade and conceal the damaged, unseeing eye [CANON - NOVEL CHAPTER 7].
  * Refused Void Shiki's offer to supernaturally regenerate the eye, accepting the scar as his eternal badge of devotion to Shiki [CANON - NOVEL EPILOGUE].
  * In the immediate weeks following his hospital release, he playfully demanded that Shiki act as his physical 'crutch' when walking down slopes and streets [CANON - NOVEL CHAPTER 7]."""

if "Post-1999 Hair & Blinded Left Eye Grooming" not in e1_m:
    pos = e1_m.find("2. FOOD, DRINK & CULINARY HABITS:")
    if pos != -1:
        e1_m = e1_m[:pos] + mikiya_style_update + "\n\n" + e1_m[pos:]
    else:
        e1_m += "\n\n" + mikiya_style_update
    everyday_lb["entries"]["1"]["content"] = e1_m

# Entry 4: Void Shiki Snow Encounter
e4_v = everyday_lb["entries"]["4"]["content"]
void_snow_addition = """
- The March 1999 Snowy Hill Road Appearance [CANON - NOVEL EPILOGUE]:
  * Manifests on the quiet, snow-covered bamboo hill road at night, draped in a pure, spotless white furisode kimono tied with an immaculate sash [CANON - NOVEL EPILOGUE].
  * Speaks with warm, silk-smooth feminine eloquence, breathing softly into the cold air while watching the snow fall with tranquil amusement [CANON - NOVEL EPILOGUE].
  * Offered to heal Mikiya's damaged left eye, expressing serene admiration when he gently declined [CANON - NOVEL EPILOGUE]."""

if "The March 1999 Snowy Hill Road Appearance" not in e4_v:
    pos = e4_v.find("2. COSMIC PERCEPTION & DAILY DETACHMENT:")
    if pos != -1:
        e4_v = e4_v[:pos] + void_snow_addition + "\n\n" + e4_v[pos:]
    else:
        e4_v += "\n\n" + void_snow_addition
    everyday_lb["entries"]["4"]["content"] = e4_v

with open(p_everyday, "w", encoding="utf-8") as f:
    json.dump(everyday_lb, f, ensure_ascii=False, indent=2)
print(f"Successfully updated {p_everyday}.")

