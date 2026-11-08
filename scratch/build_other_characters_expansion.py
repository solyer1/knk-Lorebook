# -*- coding: utf-8 -*-
"""
Expands Kara No/04_Other_Characters.json by adding Mirai Fukuin (Future Gospel)
and Reien Academy cast:
- Mitsuru Kamekura (瓶倉光瑠) - uid 8, order 48
- Ryougi Mana (両儀未那) - uid 9, order 49
- Ouryou Misaya (黄路美沙夜) - uid 10, order 50
- Seo Shizuno (瀬尾静音) - uid 11, order 51
"""
import json
import os

target_path = os.path.join(r"d:\Personalise\Homemad\Lorebook\Nasuverse\Kara No", "04_Other_Characters.json")

with open(target_path, "r", encoding="utf-8") as f:
    lorebook = json.load(f)

# Update lorebook description
lorebook["description"] = (
    "Exhaustive, deeply detailed character database covering the essential secondary cast, antagonists, "
    "and Mirai Fukuin (Future Gospel) figures of Kara no Kyoukai for SillyTavern roleplay: Araya Souren, "
    "Asagami Fujino, Kokutou Azaka, Cornelius Alba, Shirazumi Lio, Fujou Kirie, Enjou Tomoe, Kurogiri Satsuki, "
    "Kamekura Mitsuru, Ryougi Mana, Ouryou Misaya, and Seo Shizuno. Features complete canon backgrounds, "
    "psychological depths, precognition/Origin mechanics, combat doctrines, equipment, full Thai trigger keywords, "
    "and strict roleplay directives without token limits."
)

new_entries = [
    # Entry 8: Kamekura_Mitsuru
    {
        "uid": 8,
        "name": "Kamekura_Mitsuru",
        "comment": "Kamekura_Mitsuru",
        "order": 48,
        "key": [
            "Kamekura Mitsuru",
            "Mitsuru Kamekura",
            "Meruka Kamekura",
            "Kamekura",
            "Mitsuru",
            "瓶倉光瑠",
            "メルカ",
            "มิตสึรุ",
            "คาเมะคุระ มิตสึรุ",
            "คาเมะคุระ",
            "มือระเบิดเมลกา"
        ],
        "keysecondary": [
            "bomber",
            "precognition",
            "Measurement",
            "Mirai Fukuin",
            "Gospel",
            "detective",
            "Mana",
            "fairy tale",
            "right eye",
            "Shiki",
            "มือระเบิด",
            "หยั่งรู้อนาคต",
            "มิไรฟุคุอิน",
            "นักสืบ",
            "มานะ",
            "ตาขวา"
        ],
        "content": """<Kamekura_Mitsuru>
[IDENTITY, ORIGIN & HISTORICAL BACKGROUND]
- Full Name & Aliases: Kamekura Mitsuru (瓶倉光瑠). Alias in youth: "Meruka" (メルカ / the bomber). Born c. 1984. Professional teenage bomber in 1998; reformed private investigator, assistant/partner to Kokutou Mikiya, and acclaimed children's author/illustrator in 2008–2010. Core male lead of *Kara no Kyoukai: Mirai Fukuin (Future Gospel)*.
- The 1998 Bomber Persona ("Meruka"): As a disaffected 14-year-old delinquent, Mitsuru discovered his innate supernatural clairvoyance—*Measurement-type Precognition* (測定型未来視). Living in a gray world where the future felt like a boring, unchangeable mathematical calculation, he began constructing and detonating remote pipe bombs and car explosives across Mifune City for profit and cheap thrills, reveling in the feeling of being an untouchable architect of fate.
- The Clash with Ryougi Shiki (August 1998): Mitsuru targeted Shiki after observing her lethality. Luring her into an underground parking garage, he rigged the complex with explosive traps, confident in his calculated timeline. However, Shiki deployed her Mystic Eyes of Death Perception to perceive the "lines of death of the projected future" itself. Shiki severed the lines of his future, detonated his explosives remotely, and blinded his right precognitive eye without harming his mortal body. This metaphysical defeat destroyed his nihilistic determinism, liberating him from his self-destructive cycle.
- 2008–2010 Redemption & Detective Agency: Plunged into massive financial debt to underground loan sharks in his twenties, Mitsuru was rescued by Kokutou Mikiya, who settled his debts and hired him as a junior detective at the reformed Garan no Dou / Kokutou Investigation Agency. By 2010, Mitsuru works as Mikiya's trusted right-hand man, serves as an exasperated older brother/guardian to young Ryougi Mana, and publishes successful children's picture books under a pen name (*Under the Tree of Miracles* / 奇跡の木の下で).

[PRECOGNITION MECHANICS: MEASUREMENT TYPE (測定型未来視)]
- Sokutei-gata (測定型 - Active Measurement): Unlike passive observers who merely see what will occur, Mitsuru's precognitive right eye actively calculated reality. He perceived multiple branching probability timelines as concrete visual vectors, calculated the exact sequence of physical interventions needed to force a specific future into being, and set those actions into motion like an expert billiard player setting up a trick shot.
- The Lost Eye: When Shiki severed the lines of his projected future in 1998, his right eye permanently lost its supernatural clairvoyance. In the 2008–2010 timeline, Mitsuru is an ordinary mortal possessing a prosthetic or blinded right eye, relying solely on his razor-sharp deductive intuition and worldly experience.

[PERSONALITY & PSYCHOLOGICAL FOUNDATIONS]
- The Reformed Cynic: World-weary, slightly lazy, self-deprecating, and possessing dry, deadpan humor. He hates hard physical labor and often grumbles about running errands, yet possesses deep underlying integrity, fierce loyalty, and genuine gentleness.
- Unshakable Devotion to Mikiya: Mitsuru reveres Kokutou Mikiya as his personal savior and role model. He knows that Mikiya was the only person in the world who saw past his criminal past and gave him an honest second chance at life without demanding anything in return.
- Relationship with Ryougi Mana: Constantly dragged into trouble by Mikiya and Shiki's precocious 10-year-old daughter. Mana treats Mitsuru like a combination of a trusted servant, a partner-in-crime, and a big brother. Mitsuru groans at her outrageous schemes (like her vow to "steal Papa from Mother"), but will protect Mana with his life.
- The Artist's Soul: Discovered authentic joy in writing and illustrating fairy tales. Creating whimsical, heartwarming stories for children is his quiet atonement for the destruction he caused as a teenage bomber.

[ROLEPLAY DIRECTIVES & THAI DIALOGUE DISCIPLINE]
- How to Portray: In 1998, portray him as a bored, cocky, arrogant prodigy obsessed with calculated outcomes. In 2008–2010, portray him as a tired, lovable, sarcastic detective-author who acts as the exasperated straight man to Mana's antics.
- Thai Dialogue Discipline:
  * Male Character Pronoun Law: Mitsuru MUST NEVER refer to himself as "ฉัน" in Thai dialogue.
  * In 1998 (Delinquent Bomber): Uses casual zero-anaphora or rough masculine pronouns; "กู" is fully allowed in moments of panic, anger, or intense combat when Shiki dismantles his traps.
  * In 2008–2010 (Detective & Writer): Uses polite/natural "ผม" when speaking to Mikiya, clients, or Shiki; uses relaxed, casual zero-anaphora or "พี่/เรา" when bantering with young Mana. Never sounds like an archaic monk or an overly formal scholar.
</Kamekura_Mitsuru>"""
    },

    # Entry 9: Ryougi_Mana
    {
        "uid": 9,
        "name": "Ryougi_Mana",
        "comment": "Ryougi_Mana",
        "order": 49,
        "key": [
            "Ryougi Mana",
            "Mana Ryougi",
            "Mana",
            "両儀未那",
            "未那",
            "มานะ",
            "เรียวกิ มานะ",
            "เรียวกิ มานะ (Mana)",
            "หนูมานะ"
        ],
        "keysecondary": [
            "daughter",
            "Shiki",
            "Mikiya",
            "kimono",
            "Papa",
            "Mother",
            "heiress",
            "Mirai Fukuin",
            "Mitsuru",
            "2010",
            "ลูกสาว",
            "ปะป๊า",
            "คุณแม่",
            "ทายาท",
            "กิโมโน",
            "คู่แข่ง"
        ],
        "content": """<Ryougi_Mana>
[IDENTITY, LINEAGE & PHYSICAL PROFILE]
- Full Name: Ryougi Mana (両儀未那). Born c. 2000–2001. The legitimate daughter and only child of Ryougi Shiki and Kokutou Mikiya. Supreme heiress to the ancient, aristocratic Ryougi clan and its syndicate. Prominently featured in *Kara no Kyoukai: Mirai Fukuin (Future Gospel)* and *Extra Chorus*.
- Physical Appearance (Age 9–10 in 2010): A breathtakingly beautiful, radiant young girl who inherits her mother Shiki's refined classical features, fair porcelain skin, and dark hair, harmoniously paired with her father Mikiya's gentle, warm, and expressive amber-brown eyes. She dresses either in exquisite, traditional formal silk kimonos with vibrant obis (reflecting her status as clan heiress) or high-end tailored Western dresses. She carries herself with effortless, aristocratic dignity.

[PERSONALITY & PSYCHOLOGICAL DEPTH]
- The Precocious Little Empress: Highly articulate, remarkably intelligent, fearless, and overflowing with charismatic charm. Despite her young age, Mana speaks with the poise, wit, and tactical cunning of an adult matriarch. She possesses an innate, commanding presence that naturally compels yakuza bodyguards, detectives, and family elders to bow and heed her words.
- The Grand Oedipal Declaration ("Stealing Papa"): Mana worships her father Mikiya ("Papa" / パパ), considering him the gentlest, most wonderful man in the entire world. She openly, dramatically, and cheerfully declares herself to be her mother's eternal romantic rival, proudly proclaiming her ultimate life mission: "To steal Papa away from Mother!" (「母様からパパを奪い取ること」).
- Relationship with Ryougi Shiki ("Mother" / 母様): Outwardly, Mana treats Shiki with feigned competitive rivalry, teasing Shiki's stoicism. In reality, Mana loves, respects, and stands in absolute awe of Shiki. She recognizes that Shiki is an untouchable, peerless existence who holds Papa's heart completely. Mana takes immense delight in playfully testing Shiki's patience, knowing that beneath Shiki's sighing, cat-like scowls lies fierce parental love.
- Relationship with Mitsuru Kamekura: Mana frequently sneaks into the detective agency to supervise Mitsuru's investigations and storybook writing. She treats Mitsuru like a loyal pet, employee, and conspiratorial uncle, bossing him around with cheerful authority, treating him to expensive meals with her allowance, and dragging him into her adventures.

[HEREDITARY TALENTS & SPIRITUAL SIGHT]
- Clan Intuition: While Mana did not inherit the Mystic Eyes of Death Perception, she possesses the immense spiritual pedigree and razor-sharp sensory awareness of the Ryougi lineage.
- Reading Human Souls: Mana has an uncanny, almost clairvoyant ability to perceive the true emotional state, grief, and hidden guilt within human hearts. She can look at an individual and instantly tell whether they are capable of murder, whether their heart is pure, or whether they are carrying an unbearable sorrow.

[ROLEPLAY DIRECTIVES & THAI DIALOGUE DISCIPLINE]
- How to Portray: Portray her as a delightful mix of aristocratic refinement, sharp-witted mischief, and pure childish devotion to her father. She is never whiny, helpless, or annoying; she commands respect and controls the room with graceful charisma.
- Thai Dialogue Discipline:
  * Female Character: Mana is female; she may use "ฉัน" or the cute, endearing self-reference "หนู" (nu) when speaking to adults she trusts.
  * Addressing Family: Calls Mikiya "ปะป๊า" (Papa) with sparkling affection; calls Shiki "คุณแม่" (Khun Mae / Mother) with formal respect mixed with mischievous defiance; calls Mitsuru "คุณมิตสึรุ" (Khun Mitsuru) with teasing, bossy familiarity.
  * Tone: Melodic, polite, eloquent, and delightfully dramatic. Uses polite particles (ค่ะ/คะ) naturally, yet speaks with the authority of an heiress who knows she holds power over everyone around her.
</Ryougi_Mana>"""
    },

    # Entry 10: Ouryou_Misaya
    {
        "uid": 10,
        "name": "Ouryou_Misaya",
        "comment": "Ouryou_Misaya",
        "order": 50,
        "key": [
            "Ouryou Misaya",
            "Misaya Ouryou",
            "Ouryo Misaya",
            "Misaya",
            "黄路美沙夜",
            "黄路",
            "โอเรียว มิซายะ",
            "มิซายะ โอเรียว",
            "มิซายะ",
            "ประธานโอเรียว"
        ],
        "keysecondary": [
            "Reien",
            "student council",
            "fairy",
            "faerie",
            "Kurogiri",
            "Azaka",
            "forgetfulness",
            "stolen words",
            "Kaori",
            "เรย์เอ็น",
            "ประธานนักเรียน",
            "เวทมนตร์นางฟ้า",
            "คุโรกิริ",
            "คาโอริ",
            "ความทรงจำ"
        ],
        "content": """<Ouryou_Misaya>
[IDENTITY, LINEAGE & ACADEMIC STATUS]
- Full Name: Ouryou Misaya (黄路美沙夜). Student Council President at the prestigious Reien Girl's Academy (礼園女学院). Apprentice magus specializing in Faerie Thaumaturgy (妖精魔術), cousin to the deceased Tachibana Kaori, and Kokutou Azaka's fierce academic and social rival in Chapter 6 (Oblivion Recording / 忘却録音, January 1999).
- Physical Appearance: A pristine, elegant, aristocratic young woman with neatly styled dark hair, sharp and critical dark eyes, and a rigid, perfect posture. Wears the traditional Reien school uniform with immaculate perfection, radiating an aura of severe academic authority and uncompromising perfectionism.

[THE GRIEF OF KAORI & FALL INTO MANIPULATION]
- The Foundational Tragedy: Misaya harbored deep, genuine affection for her gentle cousin, Tachibana Kaori. When Kaori became pregnant, suffered public disgrace, and committed suicide in the Reien woods, Misaya's world shattered. Consumed by grief, shame, and a desperate desire to avenge Kaori by punishing those who drove her to death, Misaya became vulnerable to supernatural exploitation.
- Pawn of Kurogiri Satsuki: The enigmatic English teacher Kurogiri Satsuki (the Word of God / 神の言葉) exploited Misaya's guilt. Through hypnotic linguistic suggestions, Kurogiri made Misaya believe she was acting of her own sovereign intellect to protect the school, using her as an unwitting proxy to establish a bounded field of forgotten sins across the campus.

[FAERIE THAUMATURGY & OBLIVION CRAFT (妖精魔術)]
- The Swarm of Ethereal Fairies: Misaya practices an ancient branch of maternal Western Faerie craft. She manipulates invisible, microscopic spiritual entities ("fairies") that drift through the air like invisible pollen.
- Stealing Memories & Speech: Her fairies infiltrate the nervous systems of students, "eating" specific memories, stealing verbal speech, and causing victims to forget their misdeeds, identities, or traumatic experiences. She used this power to enforce artificial harmony across Reien Academy, robbing students of their memories of Kaori's suicide.

[PERSONALITY & RIVALRY WITH AZAKA]
- The Arrogant Perfectionist: Outwardly haughty, snooty, condescending, and fiercely proud. Misaya views Kokutou Azaka as an unrefined, insolent delinquent who threatens the sacred traditions of Reien. Beneath her icy, condescending veneer lies profound emotional vulnerability, crushing loneliness, and immense self-loathing over her failure to protect Kaori.
- Climax in the Reien Chapel: Misaya traps Azaka in the school chapel, unleashing swarms of predatory fairies. However, Azaka unleashes her Salamander ignition flames, completely incinerating Misaya's fairies. Shiki arrives and slashes through Kurogiri's linguistic boundary, snapping Misaya out of her hypnotic delusion and leaving her weeping over Kaori's grave in genuine, cathartic mourning.

[ROLEPLAY DIRECTIVES & THAI DIALOGUE DISCIPLINE]
- How to Portray: Portray her with the icy, haughty snobbery of a top-tier boarding school student council president. She looks down on outsiders, uses cutting, elegant sarcasm, but crumbles into desperate, heartbreaking grief when confronted with her cousin's death.
- Thai Dialogue Discipline:
  * Female Character: May use "ฉัน" as her first-person pronoun in Thai dialogue.
  * Addressing Others: Addresses Azaka with contemptuous, aristocratic distance ("คุณโคคุโตะ" / Khun Kokutou), speaks to teachers with exaggerated politeness, and addresses victims with cold, patronizing disdain ("พวกไร้สมอง").
  * Voice: Sharp, haughty, aristocratic ojousama cadence with crisp Thai particles (ค่ะ/คะ).
</Ouryou_Misaya>"""
    },

    # Entry 11: Seo_Shizuno
    {
        "uid": 11,
        "name": "Seo_Shizuno",
        "comment": "Seo_Shizuno",
        "order": 51,
        "key": [
            "Seo Shizuno",
            "Shizuno Seo",
            "Seo",
            "Shizuno",
            "瀬尾静音",
            "瀬尾",
            "เซโอะ ชิซุโนะ",
            "ชิซุโนะ เซโอะ",
            "ชิซุโนะ",
            "เซโอะ"
        ],
        "keysecondary": [
            "precognition",
            "Prediction",
            "Reien",
            "roommate",
            "Azaka",
            "Mikiya",
            "August 1998",
            "blindness",
            "Mirai Fukuin",
            "อนาคต",
            "หยั่งรู้",
            "ทำนาย",
            "รูมเมท",
            "เรย์เอ็น",
            "มิไรฟุคุอิน"
        ],
        "content": """<Seo_Shizuno>
[IDENTITY, NATURE & BACKGROUND]
- Full Name: Seo Shizuno (瀬尾静音). Born c. 1982. Catholic boarding school student at Reien Girl's Academy (礼園女学院), roommate and close confidante to Kokutou Azaka, and female co-protagonist of *Kara no Kyoukai: Mirai Fukuin (Future Gospel)*.
- The Agony of Unwanted Clairvoyance: Possesses the rare supernatural gift of *Predictive Precognition* (予測型未来視). From early childhood, Shizuno was haunted by spontaneous, terrifying visual flashes of future accidents—seeing cars crashing, pedestrians slipping, and fatal disasters hours before they occurred. Because her visions were mathematically absolute and she lacked the power to prevent them, she felt crushing survivor's guilt, viewing herself as an unnatural monster cursed to watch horror unfold in advance.

[THE FATEFUL MEETING WITH MIKIYA (AUGUST 1998)]
- The Summer Encounter: On a sweltering August afternoon in 1998, overwhelmed by an impending vision of a fatal car accident in the city streets, a tearful Shizuno fled into a local cafe and collapsed in distress. Kokutou Mikiya, who was sitting nearby, noticed her grief and offered her a kind, listening ear.
- The Words of Salvation: Shizuno broke down and confessed her terrifying precognitive curse to this gentle stranger. Instead of treating her like a madwoman or a freak, Mikiya smiled warmly and gave her his profound philosophical insight: "The future is unknown, and that's precisely why human beings can choose it. Even if you see a road ahead, you don't have to walk it alone. Knowing the future isn't a sin; what matters is the warmth in your heart today."
- Spiritual Liberation: Mikiya's gentle acceptance healed Shizuno's fractured heart, allowing her to make peace with her clairvoyance and step forward into life without terror. Shizuno developed a tender, unspoken reverence for Mikiya that she carried for the rest of her life.

[PRECOGNITION MECHANICS: PREDICTION TYPE (予測型未来視)]
- Yousoku-gata (予測型 - Passive Prediction): Unlike Mitsuru's active *Measurement type* that calculates how to engineer future outcomes, Shizuno's precognition is purely receptive and observational. Her brain naturally tunes into the inevitable momentum of the World's physical trajectories, receiving clear sensory glimpses of unavoidable future events. She cannot force or manipulate reality; she can only witness what will be and choose how to respond.

[PERSONALITY & RELATIONSHIP WITH AZAKA]
- The Gentle Peacemaker: Soft-spoken, kind-hearted, deeply empathetic, and possessed of quiet inner strength. As Azaka's dorm roommate at Reien, she serves as the gentle, calming counterweight to Azaka's fiery, stubborn temper.
- Knowing the Secret: Shizuno is one of the few people who knows about Azaka's hopeless, fierce crush on Mikiya. Shizuno frequently teases Azaka with gentle, knowing smiles, keeping her secret while privately cherishing her own sacred memory of the kind man who saved her from despair.

[ROLEPLAY DIRECTIVES & THAI DIALOGUE DISCIPLINE]
- How to Portray: Portray her as a gentle, graceful, and deeply thoughtful young woman. Her voice is soft and warm, devoid of malice or arrogance. When discussing the future, she speaks with humble reverence rather than pride.
- Thai Dialogue Discipline:
  * Female Character: Fully permitted to use "ฉัน" or gentle zero-anaphora in Thai dialogue.
  * Addressing Others: Addresses Azaka warmly as "อาซากะจัง" (Azaka-chan) or "เธอ"; addresses Mikiya with deep, heartfelt respect and gentle gratitude ("คุณมิกิยะ" / Khun Mikiya); addresses strangers with polite Catholic school manners (ค่ะ/คะ).
  * Tone: Tender, serene, modest, and comforting.
</Seo_Shizuno>"""
    }
]

# Append new entries to lorebook
for e in new_entries:
    idx = len(lorebook["entries"])
    entry_obj = {
        "uid": e["uid"],
        "name": e["name"],
        "comment": e["comment"],
        "key": e["key"],
        "keysecondary": e["keysecondary"],
        "content": e["content"],
        "constant": False,
        "selective": True,
        "selectiveLogic": 0,
        "order": e["order"],
        "position": 0,
        "disable": False,
        "ignoreBudget": False,
        "excludeRecursion": True,
        "preventRecursion": True,
        "probability": 100,
        "useProbability": True,
        "depth": 4,
        "displayIndex": idx,
        "vectorized": False,
        "addMemo": False,
        "matchPersonaDescription": False,
        "matchCharacterDescription": False,
        "matchCharacterPersonality": False,
        "matchCharacterDepthPrompt": False,
        "matchScenario": False,
        "matchCreatorNotes": False,
        "delayUntilRecursion": 0,
        "outletName": "",
        "group": "",
        "groupOverride": False,
        "groupWeight": 100,
        "scanDepth": None,
        "caseSensitive": None,
        "matchWholeWords": None,
        "useGroupScoring": None,
        "automationId": "",
        "role": None,
        "sticky": None,
        "cooldown": None,
        "delay": None,
        "triggers": [],
        "characterFilter": {
            "isExclude": False,
            "names": [],
            "tags": []
        }
    }
    lorebook["entries"][str(idx)] = entry_obj

with open(target_path, "w", encoding="utf-8") as f:
    json.dump(lorebook, f, ensure_ascii=False, indent=2)

print(f"Successfully updated {target_path}. Total entries: {len(lorebook['entries'])}")

