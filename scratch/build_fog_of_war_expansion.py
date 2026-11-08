# -*- coding: utf-8 -*-
"""
Builder script to expand Kara No/15_Chapter_Knowledge_Fog_of_War.json to Canonical Masterwork Depth.
Synchronizes completely with 09_Timeline.json, adding:
- Entry 8: Fog_of_War_Ch8_Epilogue_The_Void_Shiki_1999 (uid 8, order 158)
- Entry 9: Fog_of_War_Mirai_Fukuin_August_1998 (uid 9, order 159)
- Entry 10: Fog_of_War_Mirai_Fukuin_2008_2010_Adult_Era (uid 10, order 160)
- Entry 11: Fog_of_War_Dynamic_Enforcement_and_Overrides (uid 11, order 161)
"""
import json
import os

target_path = os.path.join(r"d:\Personalise\Homemad\Lorebook\Nasuverse\Kara No", "15_Chapter_Knowledge_Fog_of_War.json")

entries_data = [
    # Entry 0: Fog_of_War_Master_Chronology_and_Rules
    {
        "uid": 0,
        "name": "Fog_of_War_Master_Chronology_and_Rules",
        "comment": "Fog_of_War_Master_Chronology_and_Rules",
        "order": 150,
        "key": [
            "Fog of War",
            "KnK chapter knowledge",
            "Kara no Kyoukai chronology rules",
            "KnK timeline rules",
            "กฎหมอกแห่งสงคราม",
            "กฎความรู้ตามไทม์ไลน์",
            "การป้องกันสปอยล์บท"
        ],
        "keysecondary": [
            "rules",
            "chronology",
            "knowledge",
            "spoilers",
            "twists",
            "information",
            "release order",
            "override",
            "ไทม์ไลน์คาราโนะเคียวไค",
            "ความรู้ตามช่วงเวลา",
            "การสวมบทบาท"
        ],
        "content": """<Fog_of_War_Master_Chronology_and_Rules>
[SYSTEM RULE: INFORMATION CONFINEMENT & ANCHOR INTEGRITY]
In Kara no Kyoukai roleplay, characters must NEVER possess knowledge of future plot twists, unrevealed antagonists, or unawakened abilities. Because the anime films and light novels were released out of chronological order, the AI must anchor the scene to its IN-UNIVERSE CHRONOLOGICAL DATE, not film numbering.

[CHRONOLOGICAL VS. RELEASE ORDER MAPPING]
1. Chronological Chapter 1: Film 2 / Novel 2 — A Study in Murder (Part 1) [April 1995 – February 1996]
2. Chronological Chapter 2: Film 4 / Novel 4 — The Hollow Shrine [June 1998 – August 1998] (Coma: Feb 1996 – June 1998)
3. Chronological Chapter 3: Film 3 / Novel 3 — Remaining Sense of Pain [Late July 1998]
- Side-Event Interlude: Mirai Fukuin (Mobius Ring) [August 1998 — Seo Shizuno & Bomber Meruka]
4. Chronological Chapter 4: Film 1 / Novel 1 — Overlooking View [Late August – September 1998]
5. Chronological Chapter 5: Film 5 / Novel 5 — Paradox Spiral [October – November 1998]
6. Chronological Chapter 6: Film 6 / Novel 6 — Oblivion Recording [January 1999]
7. Chronological Chapter 7: Film 7 / Novel 7 — A Study in Murder (Part 2) [February 1999]
8. Chronological Chapter 8: Film 8 / Novel 8 — Epilogue (Kara no Kyoukai / Void Shiki `「　」`) [March 1999]
- Post-Story Adult Era: Mirai Fukuin (Extra Chorus & 2008–2010 Adult Era / Mana Ryougi & Mitsuru Kamekura)

[TEMPORAL ANCHORING DIRECTIVE]
Before generating dialogue or internal thoughts, determine the scene's current year and month:
- In 1995–1996: Shiki has NO Mystic Eyes, NO prosthetic arm, and has NEVER met Touko. Mikiya has both eyes.
- In Summer 1998: Shiki has newly awakened Mystic Eyes and Touko's first prosthetic arm. Araya Souren is completely unknown.
- In August 1998: Mirai Fukuin bomb clash occurs in secret; Shiki kills Meruka's projected future.
- In Autumn 1998: Film 1 (Overlooking View) occurs in September AFTER Film 3 & 4. Do not treat Film 1 as the story's starting point.
- In November 1998: Araya Souren and Cornelius Alba are killed at Ogawa Mansion.
- In January 1999: Araya is already dead. Mikiya does NOT know Azaka is studying magecraft.
- In February 1999: Mikiya loses his left eye. Shiki commits her first and only murder (Shirazumi Lio).
- In March 1999: Void Shiki manifests to Mikiya on the snowy road.
- In 2008–2010: Shiki and Mikiya are married with daughter Mana; Mitsuru is their detective partner.

[CUSTOM ROLEPLAY CONTINUITY OVERRIDE]
If {{user}}'s roleplay establishes events that diverge from canon (e.g., saving Enjou Tomoe, unmasking Lio in 1995, preventing Mikiya's blinding, or crossover interventions with Fate characters), the USER'S ESTABLISHED EVENTS OVERRIDE CANONICAL HISTORY. Do not force canon outcomes over user choices.
</Fog_of_War_Master_Chronology_and_Rules>"""
    },

    # Entry 1: Fog_of_War_Ch1_A_Study_in_Murder_Part_1_1995
    {
        "uid": 1,
        "name": "Fog_of_War_Ch1_A_Study_in_Murder_Part_1_1995",
        "comment": "Fog_of_War_Ch1_A_Study_in_Murder_Part_1_1995",
        "order": 151,
        "key": [
            "A Study in Murder Part 1",
            "1995",
            "1996",
            "Film 2",
            "Novel Chapter 2",
            "คดีฆาตกรรมบทที่ 1 (1995)",
            "บทคดีฆาตกรรมภาคแรก",
            "ปี 1995"
        ],
        "keysecondary": [
            "Shiki",
            "SHIKI",
            "Mikiya",
            "murders",
            "serial killings",
            "rain",
            "umbrella",
            "accident",
            "ชิกิกับมิกิยะม.ปลาย",
            "คดีฆาตกรรมต่อเนื่อง",
            "อุบัติเหตุ 1996"
        ],
        "content": """<Fog_of_War_Ch1_A_Study_in_Murder_Part_1_1995>
[TEMPORAL SETTING: APRIL 1995 – FEBRUARY 1996]
[RELEASE ORDER COMPARISON: FILM 2 / NOVEL CHAPTER 2]
Canonical Timeline: April 1995 (High school entrance, Mikiya meets Shiki under cherry blossoms); September 1995 (Serial dismemberment murders begin); December 1995 (Mikiya meets male SHIKI in bamboo grove); February 1996 (Climax on the rain-lashed road, traffic collision). Note: Early February 1996 is the established timeframe for the accident; specific calendar day (e.g., Feb 3) is traditional/inferred.

[KNOWLEDGE MATRIX: WHAT CHARACTERS KNOW, SUSPECT & CONCEAL]
1. RYOUGI SHIKI & SHIKI:
- Knows: Female Shiki knows she shares her body with a male persona, SHIKI. Both possess inherited impulses toward killing. Female Shiki knows she was wandering near crime scenes with blood on her kimono.
- Suspects: Shiki genuinely suspects she or SHIKI may be the serial killer sleepwalking at night. She fears her own murderous urge is slipping out of control.
- Conceals: Conceals her dual personality and clan heritage from all peers. SHIKI conceals the depth of his protective affection for Mikiya from female Shiki until the breaking point.
- Does NOT Know: Does NOT know Shirazumi Lio exists or that Lio is the true murderer. Does NOT possess Mystic Eyes of Death Perception. Does NOT know Aozaki Touko or Araya Souren.
- Physical Status: Two biological arms, long hair, wearing kimono and red leather jacket, wooden geta.

2. KOKUTOU MIKIYA:
- Knows: Shiki is an isolated classmate; discovers her dual personas after meeting SHIKI at night; discovers gruesome mutilated corpses near the Ryougi estate.
- Suspects: Suspects Shiki is innocent despite seeing her drenched in blood; intuitively trusts her humanity.
- Conceals: Conceals his nightly surveillance and stakeout vigils outside the Ryougi compound from his parents and sister Azaka.
- Does NOT Know: Knows nothing about Magecraft, Akasha, or Demon Hunter clans. Does not suspect Shirazumi Lio. Has both eyes functioning normally.

3. AOZAKI TOUKO & ARAYA SOUREN:
- Touko: Living in exile in Mifune City; completely unaware of Shiki and Mikiya.
- Araya: Secretly awakened Shirazumi Lio's Origin ("Consumption") in 1995 to engineer the catalyst for Shiki's future awakening. Observes passively from the shadows.

[CRITICAL SPOILERS TO SUPPRESS]
- Shiki is NOT the serial killer.
- Shiki CANNOT see Lines of Death.
- Touko is NOT Shiki's physician.
</Fog_of_War_Ch1_A_Study_in_Murder_Part_1_1995>"""
    },

    # Entry 2: Fog_of_War_Ch2_The_Hollow_Shrine_1998
    {
        "uid": 2,
        "name": "Fog_of_War_Ch2_The_Hollow_Shrine_1998",
        "comment": "Fog_of_War_Ch2_The_Hollow_Shrine_1998",
        "order": 152,
        "key": [
            "The Hollow Shrine",
            "June 1998",
            "July 1998",
            "Film 4",
            "Novel Chapter 4",
            "วิหารว่างเปล่าบทที่ 4",
            "โรงพยาบาลฟื้นจากโคม่า",
            "ปี 1998 มิถุนา"
        ],
        "keysecondary": [
            "Room 404",
            "hospital",
            "awakening",
            "coma",
            "MEoDP",
            "prosthetic arm",
            "Touko",
            "vigil",
            "การตื่นของเนตรมรณะ",
            "การพบโทโกะ",
            "ห้อง 404"
        ],
        "content": """<Fog_of_War_Ch2_The_Hollow_Shrine_1998>
[TEMPORAL SETTING: JUNE – AUGUST 1998]
[RELEASE ORDER COMPARISON: FILM 4 / NOVEL CHAPTER 4]
Canonical Timeline: February 1996 – June 1998 (2-year comatose state at Yagami General Hospital); June 1998 (Shiki awakens in Room 404, claws at eyes, eyes bandaged); July 1998 (Touko infiltrates as speech therapist); Late July / Early August 1998 (Corpse spirit attack, Shiki accepts MEoDP, Touko fits puppet arm, hair cut).

[KNOWLEDGE MATRIX: WHAT CHARACTERS KNOW, SUSPECT & CONCEAL]
1. RYOUGI SHIKI:
- Knows: Male persona SHIKI died during the 1996 traffic collision. She feels an agonizing emptiness inside. She perceives terrifying glowing blue/black lines across everything.
- Suspects: Believes she is a walking corpse whose soul dissolved, or that she has gone completely mad.
- Conceals: Keeps her eyes tightly bandaged in terror of seeing death. Conceals her emotional grief over SHIKI's death.
- Does NOT Know: Does not know what the Mystic Eyes of Death Perception are until Touko explains conceptual mortality. Does not know Mikiya visited every weekend for two years bringing fresh flowers until Touko and nurses mention it.
- Physical Status: Weakened from two years of muscle atrophy; newly fitted magical puppet left arm; cuts her hair short.

2. KOKUTOU MIKIYA:
- Knows: Shiki has miraculously awakened from suspended brain death. Has dropped out of college in April 1998 to apprentice at Garan no Dou under Touko.
- Suspects: Worries Shiki may have lost her memories of high school or will despise him for letting SHIKI die.
- Conceals: His overwhelming joy and desire to visit her daily; stays away per Touko's strict instructions to avoid overwhelming Shiki's fragile mental state.
- Does NOT Know: Does not comprehend the supernatural terror of the Mystic Eyes; knows only that Touko is managing Shiki's sensory therapy.

3. AOZAKI TOUKO:
- Knows: Shiki's empty vessel is directly linked to the Root (`Akasha`); recognizes the true nature of the Mystic Eyes of Death Perception; knows wandering spirits will swarm toward Shiki's hollow container.
- Suspects: Suspects someone orchestrated Shiki's awakening, but lacks concrete proof.
- Conceals: Her identity as a Grand puppeteer under Sealing Designation; conceals her dangerous occult history from Mikiya.

[CRITICAL SPOILERS TO SUPPRESS]
- Shiki has not yet encountered Fujino Asagami, Kirie Shizuno, or Enjou Tomoe.
- Araya Souren's overall architectural trap is still completely undiscovered.
</Fog_of_War_Ch2_The_Hollow_Shrine_1998>"""
    },

    # Entry 3: Fog_of_War_Ch3_Remaining_Sense_of_Pain_1998
    {
        "uid": 3,
        "name": "Fog_of_War_Ch3_Remaining_Sense_of_Pain_1998",
        "comment": "Fog_of_War_Ch3_Remaining_Sense_of_Pain_1998",
        "order": 153,
        "key": [
            "Remaining Sense of Pain",
            "July 1998",
            "Film 3",
            "Novel Chapter 3",
            "Fujino incident",
            "ความเจ็บปวดที่หลงเหลือบทที่ 3",
            "คดีฟูจิโนะสะพานมินาโตะ",
            "กรกฎาคม 1998"
        ],
        "keysecondary": [
            "Fujino",
            "Asagami",
            "Minato Bridge",
            "appendix",
            "distortion",
            "delinquents",
            "pain",
            "ฟูจิโนะตาบิด",
            "ไส้ติ่งอักเสบ",
            "สะพานมินาโตะ"
        ],
        "content": """<Fog_of_War_Ch3_Remaining_Sense_of_Pain_1998>
[TEMPORAL SETTING: LATE JULY 1998 (ROUGHLY JULY 20–31)]
[RELEASE ORDER COMPARISON: FILM 3 / NOVEL CHAPTER 3]
Canonical Timeline: Occurs immediately after Shiki is discharged from Yagami Hospital. Summer heatwave and heavy torrential rain. Incidents: Delinquents assaulted by mysterious telekinetic force; Mikiya shelters Fujino; Minato (Broad) Bridge battle at month's end.

[KNOWLEDGE MATRIX: WHAT CHARACTERS KNOW, SUSPECT & CONCEAL]
1. RYOUGI SHIKI:
- Knows: Commissioned by Touko to stop a dangerous psychic twisting human bodies into mangled spirals; discovers the killer is high-school student Asagami Fujino.
- Suspects: Realizes during the bridge battle that Fujino cannot feel physical pain (congenital analgesia) and is dying from an inflamed, ruptured appendix.
- Conceals: Conceals her mercy—she deliberately cuts Fujino's spatial distortion axis and gangrenous appendix instead of severing her life lines.
- Does NOT Know: Does not know that Araya Souren unsealed Fujino's sensory blocks to trigger her awakening.

2. KOKUTOU MIKIYA:
- Knows: Encountered a shivering, rain-soaked girl (Fujino) on the street and gave her shelter in his apartment overnight; noticed her severe abdominal pain.
- Suspects: Fears that the gentle girl he sheltered is the spiral killer; suspects Shiki intends to murder her.
- Conceals: Keeps his overnight shelter of Fujino secret from Shiki until forced to confess during the investigation.
- Does NOT Know: Does not understand the nature of Demon Hunter bloodlines or spatial distortion until Touko explains.

3. AOZAKI TOUKO:
- Knows: The history of the Asagami clan (ancient Demon Hunters); thaumaturgical mechanics of spatial distortion (bending coordinates rather than physical force); knows Fujino's painlessness acted as a psychic seal.
- Does NOT Know: Does not yet realize that Araya Souren intentionally awakened Fujino as a calibration experiment to test Shiki's Mystic Eyes.

4. ASAGAMI FUJINO:
- Knows: She was brutally violated in an abandoned bar; her sensation of pain returned with acute appendicitis; she can twist any object she perceives.
- Does NOT Know: Does not know Shiki or Touko; does not understand she is dying of appendicitis rather than internal combat damage.

[CRITICAL SPOILERS TO SUPPRESS]
- Fujino is NOT dead. She survives, is hospitalized, and recovers.
- Kirie Shizuno has not yet begun her suicide wave.
- Araya Souren remains completely unmasked.
</Fog_of_War_Ch3_Remaining_Sense_of_Pain_1998>"""
    },

    # Entry 4: Fog_of_War_Mirai_Fukuin_August_1998 (NEW)
    {
        "uid": 4,
        "name": "Fog_of_War_Mirai_Fukuin_August_1998",
        "comment": "Fog_of_War_Mirai_Fukuin_August_1998",
        "order": 154,
        "key": [
            "Mirai Fukuin August 1998",
            "Future Gospel 1998",
            "Mobius Ring 1998",
            "Kamekura Mitsuru 1998",
            "Seo Shizuno 1998",
            "มิไรฟุคุอิน สิงหาคม 1998",
            "คดีมือระเบิดเมลกา",
            "เซโอะ ชิซุโนะ 1998"
        ],
        "keysecondary": [
            "precognition",
            "bomber",
            "Meruka",
            "cafe",
            "parking garage",
            "killing future",
            "มือระเบิด",
            "หยั่งรู้อนาคต",
            "การฆ่าอนาคต",
            "ลานจอดรถ"
        ],
        "content": """<Fog_of_War_Mirai_Fukuin_August_1998>
[TEMPORAL SETTING: AUGUST 1998 (MOBIUS RING / FUTURE GOSPEL)]
[CHRONOLOGICAL POSITION: BETWEEN CHAPTER 3 (JULY) & CHAPTER 4 (SEPTEMBER)]
Canonical Timeline: Mid-August 1998. Incidents: Kokutou Mikiya encounters Seo Shizuno in a cafe; Shiki duels teenage bomber "Meruka" (Kamekura Mitsuru) in an underground parking garage.

[KNOWLEDGE MATRIX: WHAT CHARACTERS KNOW, SUSPECT & CONCEAL]
1. SEO SHIZUNO:
- Knows: Trapped in despair over her Predictive Precognition (予測型未来視); sees inevitable fatal traffic accidents before they happen.
- Experience: Breaks down crying in a city cafe, confiding her curse to gentle stranger Kokutou Mikiya.
- Salvation: Receives Mikiya's life-changing philosophy: "The future is unknown, and that's precisely why human beings can choose it." Finds peace and returns to Reien Academy.
- Does NOT Know: Does not know Mikiya's girlfriend is Ryougi Shiki; does not know anything about Magecraft or the Root.

2. KAMEKURA MITSURU ("MERUKA"):
- Knows: Operates as a 14-year-old delinquent bomber using Measurement Precognition (測定型未来視) to calculate explosive ambushes.
- Clash with Shiki: Lures Shiki into a parking garage; detonates traps.
- Defeat: Shiki perceives the "lines of death of the projected future" itself, severing his calculated future and blinding his precognitive right eye without taking his life.
- Does NOT Know: Does not know Shiki spared his life out of restraint; does not know that a decade later Mikiya will save him from yakuza debt.

3. RYOUGI SHIKI:
- Knows: Discovered that intangible "future timelines" possess lines of death if they are manifested in human perception. Slices Meruka's future to neutralize the bomb.
- Conceals: Never tells Mikiya about the underground garage duel with the teenage bomber.

4. KOKUTOU MIKIYA:
- Knows: Comforted a crying Catholic schoolgirl in a cafe on August 3.
- Completely Unaware: Completely ignorant of Shiki's battle with the bomber in the parking garage that same week.

[CRITICAL SPOILERS TO SUPPRESS]
- Meruka is NOT dead. He survives, reforms, and becomes Mitsuru Kamekura.
- Shizuno will reappear in January 1999 as Azaka's roommate at Reien Academy.
</Fog_of_War_Mirai_Fukuin_August_1998>"""
    },

    # Entry 5: Fog_of_War_Ch4_Overlooking_View_1998
    {
        "uid": 5,
        "name": "Fog_of_War_Ch4_Overlooking_View_1998",
        "comment": "Fog_of_War_Ch4_Overlooking_View_1998",
        "order": 155,
        "key": [
            "Overlooking View",
            "August 1998",
            "September 1998",
            "Film 1",
            "Novel Chapter 1",
            "ทิวทัศน์เบื้องสูงบทที่ 1",
            "คดีคิริเอะตึกฟูโจ",
            "กันยายน 1998"
        ],
        "keysecondary": [
            "Fujou Building",
            "Kirie",
            "suicide",
            "floating",
            "flying",
            "Thanatos",
            "comatose",
            "การกระโดดตึกแปดศพ",
            "วิญญาณลอยฟ้า",
            "แขนเทียมหัก"
        ],
        "content": """<Fog_of_War_Ch4_Overlooking_View_1998>
[TEMPORAL SETTING: LATE AUGUST – SEPTEMBER 1998]
[RELEASE ORDER COMPARISON: FILM 1 / NOVEL CHAPTER 1]
CRITICAL CHRONOLOGY WARNING: Even though this is FILM 1, chronologically it occurs AFTER Chapters 2, 4, 3, and Mirai Fukuin (August)! Shiki has already lived in her apartment for months, already has Mystic Eyes, and has already neutralized Fujino.
Canonical Timeline: Late August 1998 (Series of unexplained high-school girl suicides at the condemned Fujou Building); September 1998 (Mikiya investigates, falls into comatose trance; Shiki assaults building, loses first puppet arm; Touko upgrades arm; Shiki severs Kirie's projection).

[KNOWLEDGE MATRIX: WHAT CHARACTERS KNOW, SUSPECT & CONCEAL]
1. RYOUGI SHIKI:
- Knows: Eight girls have leapt to their deaths without motive; Mikiya is trapped in an unnatural coma after visiting the site; Kirie Shizuno is projecting ghostly double-bodies.
- Suspects: Suspects Kirie cannot perceive physical boundaries or distance.
- Conceals: Her profound terror and panic over Mikiya's comatose condition, masking it behind aggressive hostility toward Touko and cold detachment.
- Does NOT Know: Does not know Kirie's real physical body is bedridden and dying in Yagami Hospital until after the rooftop battle.

2. KOKUTOU MIKIYA:
- Knows: NOTHING during the climax. Trapped in an unnatural hypnotic coma, his soul anchored to the skyscraper roof, drifting in a pleasant dream of floating.

3. AOZAKI TOUKO:
- Knows: The Fujou clan's occult lineage (spirit channeling and spiritual possession); analyzes the conceptual difference between "floating" (aimless drift without agency) and "flying" (directed will with clear purpose).
- Upgrades: Replaces Shiki's standard puppet arm with a masterwork combat prosthetic capable of physically grasping spirits and conceptual entities.

4. FUJOU KIRIE:
- Knows: She is terminally blind and paralyzed in a hospital bed; a trench-coated man (Araya) gave her the power to project a second mobile body.
- Does NOT Know: Does not understand why ordinary girls jump to their deaths when she attempts to share her sensation of floating with them.

[CRITICAL SPOILERS TO SUPPRESS]
- Neither Touko nor Shiki realizes that Fujino (Ch. 3) and Kirie (Ch. 4) were both pawn experiments created by Araya Souren.
- Enjou Tomoe has not yet appeared.
</Fog_of_War_Ch4_Overlooking_View_1998>"""
    },

    # Entry 6: Fog_of_War_Ch5_Paradox_Spiral_1998
    {
        "uid": 6,
        "name": "Fog_of_War_Ch5_Paradox_Spiral_1998",
        "comment": "Fog_of_War_Ch5_Paradox_Spiral_1998",
        "order": 156,
        "key": [
            "Paradox Spiral",
            "October 1998",
            "November 1998",
            "Film 5",
            "Novel Chapter 5",
            "วงกตสไปรัลบทที่ 5",
            "คดีแมนชั่นโอกาวะ",
            "พฤศจิกายน 1998"
        ],
        "keysecondary": [
            "Ogawa Mansion",
            "Araya",
            "Tomoe",
            "Alba",
            "katana",
            "mandala",
            "Taiji",
            "puppet body",
            "เอ็นโจ โทโมเอะ",
            "อารายะ โซเร็น",
            "ดาบคาเนซาดะ"
        ],
        "content": """<Fog_of_War_Ch5_Paradox_Spiral_1998>
[TEMPORAL SETTING: OCTOBER – NOVEMBER 1998]
[RELEASE ORDER COMPARISON: FILM 5 / NOVEL CHAPTER 5]
Canonical Timeline: Late October 1998 (Shiki rescues runaway Enjou Tomoe in a rainy alley; Tomoe stays at her apartment); Early-to-Mid November 1998 (Infiltration of Ogawa Mansion; Shiki sealed in Taiji field; Touko killed and revived; Tomoe retrieves Kanesada; Shiki executes Araya Souren).

[KNOWLEDGE MATRIX: WHAT CHARACTERS KNOW, SUSPECT & CONCEAL]
1. RYOUGI SHIKI:
- Knows: Shelters Tomoe; discovers Ogawa Mansion is an alchemical mandala trapping residents in synthetic looping days; discovers Araya Souren is the mastermind behind the recent supernatural incidents.
- Conceals: Her ancestral Kanesada katana stored in her apartment closet until Tomoe retrieves it.
- Does NOT Know: Did not realize Araya engineered Fujino, Kirie, and the Ogawa apartments specifically to isolate and capture her body until Araya declares it in the central sanctum.

2. KOKUTOU MIKIYA:
- Knows: Uncovers municipal family registry records proving Enjou Tomoe and his parents died months earlier in a murder-suicide; realizes the Tomoe living with Shiki cannot be human.
- Conceals: His investigation findings until he can warn Touko.

3. AOZAKI TOUKO:
- Knows: Recognizes Ogawa Mansion as a Taiji bounded field constructed by her Clock Tower rival Araya Souren; recognizes Cornelius Alba as Araya's pawn.
- Conceals: Her ultimate trump card: absolute duplicate puppet immortality. Standby puppet bodies awaken upon the death of the active body.

4. ENJOU TOMOE:
- Knows: Believes he killed his parents; gradually discovers through Shiki and Touko that he is an artificial puppet with transplanted memories. Sacrifices himself to save Shiki.

5. ARAYA SOUREN:
- Fully Reveals: His 200-year quest to reach the Root by collecting deaths; reveals that Kirie (Origin of Contact), Fujino (Origin of Distortion), and Lio (Origin of Consumption) were his instruments to corner Shiki.

[CRITICAL SPOILERS TO SUPPRESS]
- Araya Souren DIES at the climax of this chapter. Alba DIES.
- In all subsequent chapters (Chapters 6 & 7), Araya is already dead and gone.
</Fog_of_War_Ch5_Paradox_Spiral_1998>"""
    },

    # Entry 7: Fog_of_War_Ch6_Oblivion_Recording_1999
    {
        "uid": 7,
        "name": "Fog_of_War_Ch6_Oblivion_Recording_1999",
        "comment": "Fog_of_War_Ch6_Oblivion_Recording_1999",
        "order": 157,
        "key": [
            "Oblivion Recording",
            "January 1999",
            "Film 6",
            "Novel Chapter 6",
            "Reien incident",
            "บันทึกการลืมเลือนบทที่ 6",
            "คดีโรงเรียนเรย์เอ็น",
            "มกราคม 1999"
        ],
        "keysecondary": [
            "Reien Academy",
            "Azaka",
            "fairies",
            "Kurogiri",
            "Misaya",
            "memory loss",
            "Unified Language",
            "อาซากะจุดไฟ",
            "เวทมนตร์นางฟ้า",
            "คุโรกิริ ซัตสึกิ"
        ],
        "content": """<Fog_of_War_Ch6_Oblivion_Recording_1999>
[TEMPORAL SETTING: JANUARY 1999]
[RELEASE ORDER COMPARISON: FILM 6 / NOVEL CHAPTER 6]
CRITICAL CHRONOLOGY WARNING: Araya Souren is ALREADY DEAD. This incident represents the unraveling of Araya's residual influence.
Canonical Timeline: Winter semester at Reien Girls' Academy (January 10–25, 1999). Strange memory-loss incidents occur; Touko sends Azaka to investigate; Shiki infiltrates in school uniform; chapel confrontation with Misaya and Kurogiri Satsuki.

[KNOWLEDGE MATRIX: WHAT CHARACTERS KNOW, SUSPECT & CONCEAL]
1. RYOUGI SHIKI:
- Knows: Dispatched to assist Azaka undercover; can perceive and cut the conceptual bodies of memory-stealing fairies; confronts Kurogiri Satsuki; realizes Kurogiri has no homicidal malice.
- Conceals: Her presence as a guest/relative inside Reien; conceals her sharp amusement at Azaka's frantic jealousy.
- Does NOT Know: Does not know Kurogiri's true history or his connection to Araya until Touko explains.

2. KOKUTOU AZAKA:
- Knows: Investigating memory-theft among peers at Reien; wields Salamander ignition gloves; battles student council president Ouryou Misaya in the chapel.
- Conceals: STRICTLY CONCEALS her magecraft apprenticeship and combat training from Mikiya. Terrified Mikiya will discover she is a magus.
- Suspects: Suspects Shiki is only helping to mock her or get closer to Mikiya.

3. KOKUTOU MIKIYA:
- Knows: ABSOLUTELY NOTHING ABOUT THE INCIDENT. Genuinely believes Azaka is peacefully studying for winter midterms at Reien Academy.
- Conceals: None. Completely in the dark.

4. AOZAKI TOUKO:
- Knows: Kurogiri Satsuki (Sadamitsu Matsuguruma) is a linguistic magus utilizing the ancient Unified Language (God's Word); knows Kurogiri was hired/influenced by Araya prior to Araya's death.
- Motivation: Dispatches Azaka as a practical examination to test her maturity as an apprentice.

5. KUROGIRI SATSUKI:
- Knows: Uses the Unified Language to rewrite memories and conceptual reality; manipulated Misaya; has no interest in reaching the Root; departs peacefully into the snowfall after his boundary is severed.

[CRITICAL SPOILERS TO SUPPRESS]
- Mikiya STILL does NOT know Azaka is a magus.
- Shirazumi Lio has not yet resurfaced.
</Fog_of_War_Ch6_Oblivion_Recording_1999>"""
    },

    # Entry 8: Fog_of_War_Ch7_A_Study_in_Murder_Part_2_1999
    {
        "uid": 8,
        "name": "Fog_of_War_Ch7_A_Study_in_Murder_Part_2_1999",
        "comment": "Fog_of_War_Ch7_A_Study_in_Murder_Part_2_1999",
        "order": 158,
        "key": [
            "A Study in Murder Part 2",
            "February 1999",
            "Film 7",
            "Novel Chapter 7",
            "คดีฆาตกรรมบทที่ 7 (1999)",
            "คดีชิราซุมิ ริโอะ",
            "กุมภาพันธ์ 1999"
        ],
        "keysecondary": [
            "Lio Shirazumi",
            "Consumption",
            "murder",
            "Mikiya blinding",
            "left eye",
            "warehouse",
            "first kill",
            "ริโอะคลั่งกินคน",
            "มิกิยะตาบอด",
            "จุดสิ้นสุดคดีฆาตกรรม"
        ],
        "content": """<Fog_of_War_Ch7_A_Study_in_Murder_Part_2_1999>
[TEMPORAL SETTING: MID-TO-LATE FEBRUARY 1999]
[RELEASE ORDER COMPARISON: FILM 7 / NOVEL CHAPTER 7]
Canonical Timeline: The story's ultimate winter climax. Incidents: Dismemberment murders matching the 1995 killings resume; Mikiya uncovers Shirazumi Lio's identity; Lio kidnaps Mikiya, crushes Mikiya's left eye; Shiki duels and kills Lio (her only human murder); Mikiya forgives her and vows to share her burden.

[KNOWLEDGE MATRIX: WHAT CHARACTERS KNOW, SUSPECT & CONCEAL]
1. RYOUGI SHIKI:
- Knows: The 1995 murder pattern has resumed; she did not commit them; Shirazumi Lio is the true killer; Lio has captured Mikiya; arrives at the warehouse, finds Mikiya's bloody jacket and eye, and believes Mikiya was slaughtered.
- Action: Believing Mikiya dead, her sanity breaks. She kills Shirazumi Lio in a ferocious, visceral duel—her FIRST AND ONLY deliberate murder of a human being.
- Revelation: Discovers Mikiya survived. Broken with guilt over breaking her vow, she is embraced by Mikiya.

2. KOKUTOU MIKIYA:
- Knows: Uncovers high school dropout records and police cold files connecting the 1995 murders and the new drug "Blood Chip" to former classmate Shirazumi Lio.
- Suspects: Believes Lio can still be talked down; goes to meet Lio alone without weapons.
- Consequence: Brutally assaulted and blinded in his left eye by Lio. Regains consciousness in time to stop Shiki from abandoning the human world, vowing to shoulder her sin forever.

3. AOZAKI TOUKO:
- Knows: Lio's Origin of "Consumption" was awakened by Araya Souren in 1995 as a posthumous curse aimed at forcing Shiki to kill; provides forensic backing to Mikiya; prepares to close Garan no Dou and depart Mifune City.

4. SHIRAZUMI LIO:
- Knows: He was the 1995 serial killer; obsessed with Shiki; believes forcing Shiki to kill will unite their souls; blinded Mikiya to break Shiki's anchor.

[CRITICAL SPOILERS TO SUPPRESS]
- Prior to this chapter: Mikiya has BOTH eyes functioning.
- Prior to this chapter: Shiki has NEVER committed murder.
- After this chapter: The 1995 serial murder mystery is permanently solved.
</Fog_of_War_Ch7_A_Study_in_Murder_Part_2_1999>"""
    },

    # Entry 9: Fog_of_War_Ch8_Epilogue_The_Void_Shiki_1999 (NEW)
    {
        "uid": 9,
        "name": "Fog_of_War_Ch8_Epilogue_The_Void_Shiki_1999",
        "comment": "Fog_of_War_Ch8_Epilogue_The_Void_Shiki_1999",
        "order": 159,
        "key": [
            "Epilogue Kara no Kyoukai",
            "Void Shiki Epilogue",
            "March 1999",
            "Film 8",
            "Novel Chapter 8",
            "บทส่งท้าย คาราโนะเคียวไค",
            "ชิกิแห่งความว่างเปล่า",
            "มีนาคม 1999",
            "เรียวกิ ชิกิ รากเหง้า"
        ],
        "keysecondary": [
            "Void Shiki",
            "snowy hill",
            "Root",
            "Akasha",
            "eyepatch",
            "wish",
            "third personality",
            "ถนนหิมะ",
            "ตาซ้ายบอด",
            "บุคลิกที่สาม",
            "รากเหง้า"
        ],
        "content": """<Fog_of_War_Ch8_Epilogue_The_Void_Shiki_1999>
[TEMPORAL SETTING: LATE MARCH 1999]
[RELEASE ORDER COMPARISON: EPILOGUE FILM / NOVEL CHAPTER 8 (KARA NO KYOUKAI)]
Canonical Timeline: Roughly one month after Shirazumi Lio's death. Midnight on a quiet, snow-covered hill road overlooking Mifune City.

[KNOWLEDGE MATRIX: WHAT CHARACTERS KNOW, SUSPECT & CONCEAL]
1. VOID SHIKI (`「　」` / THE ROOT PERSONALITY):
- Nature: The primordial, foundational consciousness of Ryougi Shiki's physical body, directly connected to the Swirl of the Root (`Akasha`). Manifests only when female Shiki is asleep and the world is in absolute tranquility.
- Demeanor & Voice: Gentle, refined, graceful, speaking in classical polite Japanese (watashi / 私, desu/masu). Unlike female Shiki's clipped tomboyish "ore", Void Shiki speaks with sublime maternal warmth.
- Dialogue with Mikiya: Explains the metaphysical nature of human Origin, why male SHIKI had to die, and the truth of existence.
- The Offered Miracle: Confesses her quiet love for Mikiya and offers to rewrite reality or heal his blinded left eye. Mikiya gently declines, choosing to carry his wound as an eternal physical bond with Shiki.
- Absolute Secrecy: Female Shiki and male SHIKI have ZERO memory or awareness of Void Shiki's conversations with Mikiya.

2. KOKUTOU MIKIYA:
- Knows: Wears a bandage or eyepatch over his blind left eye. Meets this ethereal, polite version of Shiki in the snow, realizing she is neither female Shiki nor male SHIKI, but the very vessel itself.
- Choice: Refuses the miracle of healing his eye, accepting his mortal scars and vowing to live by Shiki's side.
- Conceals: NEVER reveals this midnight conversation to Touko, Azaka, or even female Shiki herself. It remains his sacred, unspoken secret.

[CRITICAL SPOILERS TO SUPPRESS]
- Void Shiki NEVER manifests in daylight, combat, or social situations.
- Female Shiki does NOT know Void Shiki spoke to Mikiya.
</Fog_of_War_Ch8_Epilogue_The_Void_Shiki_1999>"""
    },

    # Entry 10: Fog_of_War_Mirai_Fukuin_2008_2010_Adult_Era (NEW)
    {
        "uid": 10,
        "name": "Fog_of_War_Mirai_Fukuin_2008_2010_Adult_Era",
        "comment": "Fog_of_War_Mirai_Fukuin_2008_2010_Adult_Era",
        "order": 160,
        "key": [
            "Mirai Fukuin Adult Era",
            "Future Gospel 2008 2010",
            "Mana Ryougi Era",
            "Mitsuru Detective Era",
            "มิไรฟุคุอิน ยุคผู้ใหญ่",
            "ยุค 2008 2010",
            "ยุคเรียวกิ มานะ"
        ],
        "keysecondary": [
            "married",
            "Mana",
            "Mitsuru",
            "detective agency",
            "Under the Tree of Miracles",
            "eyepatch Mikiya",
            "มานะ",
            "มิตสึรุ",
            "แต่งงานแล้ว",
            "สำนักงานนักสืบ"
        ],
        "content": """<Fog_of_War_Mirai_Fukuin_2008_2010_Adult_Era>
[TEMPORAL SETTING: 2008 – 2010 (MIRAI FUKUIN / EXTRA CHORUS / FUKAN FUUKEI)]
[CHRONOLOGICAL POSITION: ADULT EPILOGUE ERA — A DECADE AFTER MAIN STORY]
Canonical Timeline: 2008 (Mikiya settles Mitsuru's debt and hires him); 2010 (Summer / New Year incidents; young Mana Ryougi visits detective agency; Mitsuru publishes picture books).

[KNOWLEDGE MATRIX: WHAT CHARACTERS KNOW, SUSPECT & CONCEAL]
1. RYOUGI SHIKI & KOKUTOU MIKIYA:
- Status: Officially married. Shiki has inherited the Ryougi clan leadership, carrying herself as a poised, mature matriarch in traditional kimonos. Mikiya runs the private detective agency (reformed Garan no Dou).
- Health: Mikiya permanently wears glasses concealing his blinded left eye; Shiki's spiritual unrest is peaceful.
- Family Life: Deeply loving, peaceful domestic bond, occasionally exasperated by their precocious daughter Mana.

2. RYOUGI MANA:
- Knows: Age 9–10 in 2010. Supreme clan heiress. Admires Papa Mikiya above all mortals; playfully declares her mission to "steal Papa from Mother".
- Dynamic with Mitsuru: Treats ex-bomber Mitsuru as a trusted servant, uncle, and partner-in-crime, funding his investigations.

3. KAMEKURA MITSURU:
- Knows: Blind in his right eye (from Shiki's MEoDP strike in 1998). Completely reformed; works as Mikiya's detective assistant and writes acclaimed fairy tales (*Under the Tree of Miracles*).
- Gratitude: Forever loyal to Mikiya for saving him from criminal ruin.

4. AOZAKI TOUKO & KOKUTOU AZAKA:
- Touko: Left Mifune City in early 1999; travels the world evading the Sealing Designation.
- Azaka: Fully certified adult magus, still working closely with the family, retaining her fond affection for Mikiya.

[CRITICAL SPOILERS & TIMELINE RULES]
- In 2010, the supernatural tragedies of 1995–1999 are completely in the past.
- Never portray Shiki as a brooding, lonely teenager in this era; she is a fulfilled mother and clan head.
</Fog_of_War_Mirai_Fukuin_2008_2010_Adult_Era>"""
    },

    # Entry 11: Fog_of_War_Dynamic_Enforcement_and_Overrides
    {
        "uid": 11,
        "name": "Fog_of_War_Dynamic_Enforcement_and_Overrides",
        "comment": "Fog_of_War_Dynamic_Enforcement_and_Overrides",
        "order": 161,
        "key": [
            "Fog of War enforcement",
            "timeline enforcement",
            "anachronism prevention",
            "custom RP overrides",
            "การบังคับใช้หมอกแห่งสงคราม",
            "การป้องกันความจำรั่วไหลข้ามบท"
        ],
        "keysecondary": [
            "guardrails",
            "rules",
            "runtime",
            "memory leakage",
            "divergence",
            "canon override",
            "alternate timeline",
            "การคุมสปอยล์",
            "กฎเวลา",
            "การตั้งค่าโรลเพลย์"
        ],
        "content": """<Fog_of_War_Dynamic_Enforcement_and_Overrides>
[OPERATIONAL DIRECTIVE FOR AI NARRATION & CHARACTER DIALOGUE]
When roleplaying any scene in the Nasuverse / Kara no Kyoukai setting, the AI must strictly enforce the Fog-of-War rules below:

1. ABSOLUTE PROHIBITION ON PREMATURE LEAKS:
- Never allow characters to drop knowing hints about future twists (e.g., Touko hinting that Araya is behind Fujino in July 1998, or Mikiya suspecting Lio before February 1999).
- If a character lacks canonical knowledge, their responses must reflect genuine ignorance, mundane civilian assumptions, or plausible occult misdirection.

2. VERIFYING TEMPORAL MILESTONES:
- Eye Injury: Mikiya has full vision in both eyes until the climax of Chapter 7 (February 1999). Never mention an eyepatch or blindness before this date.
- Murder Counter: Shiki's human kill count is exactly ZERO until the climax of Chapter 7 (February 1999). She has destroyed spirits, wraiths, and severed spatial axes/appendixes, but has never ended a human life.
- Mystic Eyes: Non-existent in Shiki prior to June 1998.
- Prosthetic Arm: Shiki has her biological left arm until June 1998; uses Touko's standard puppet arm from July 1998; uses the upgraded spirit-gripping arm from September 1998 onward.

3. CUSTOM ROLEPLAY DIVERGENCE (USER CHOICES OVERRIDE CANON):
- If {{user}} initiates an alternate timeline or takes actions that alter events:
  a. Example 1: If {{user}} intervenes in November 1998 and saves Enjou Tomoe, Tomoe survives and remains an active NPC.
  b. Example 2: If {{user}} investigates the 1995 murders with modern/crossover means and exposes Shirazumi Lio early, the 1996 traffic collision may be averted.
  c. Example 3: If {{user}} provides thaumaturgical or Servant-based healing to Mikiya's eye in February 1999, his blindness is healed.
- IN ALL DIVERGENT CASES: The established narrative in the chat history TAKES ABSOLUTE PRECEDENCE over canonical lore. Do not force characters back onto canonical rails if the user has intentionally changed the course of history.
</Fog_of_War_Dynamic_Enforcement_and_Overrides>"""
    }
]

lorebook = {
    "name": "Kara_no_Kyoukai_15_Chapter_Knowledge_Fog_of_War",
    "description": "Exhaustive, canon-accurate temporal knowledge and Fog-of-War reference module for Kara no Kyoukai. Fully synchronized with 09_Timeline. Maps all story chapters, interludes, and epilogues chronologically (1995-1996, Room 404, Remaining Sense of Pain, Mirai Fukuin 1998, Overlooking View, Paradox Spiral, Oblivion Recording, A Study in Murder Part 2, Epilogue Void Shiki, and Mirai Fukuin 2008-2010 Adult Era). Details what characters know, suspect, conceal, and have not yet discovered, with strict guardrails against premature spoilers while supporting user-driven alternate timeline overrides.",
    "scan_depth": 50,
    "token_budget": 50000,
    "recursive_scanning": False,
    "extensions": {},
    "entries": {}
}

for idx, e in enumerate(entries_data):
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

print(f"Successfully generated {target_path} with {len(entries_data)} entries.")

