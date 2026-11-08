# -*- coding: utf-8 -*-
"""
Builder script to generate the exhaustive, deep canon timeline for Kara no Kyoukai.
File: Kara No/09_Timeline.json
"""
import json
import os

timeline_entries = {
  "0": {
    "uid": 0,
    "name": "Chronology_Structure_and_Viewing_Guide",
    "comment": "Chronology_Structure_and_Viewing_Guide",
    "key": [
      "Kara no Kyoukai timeline",
      "KnK chronology",
      "viewing order vs chronological",
      "KnK timeline guide",
      "ไทม์ไลน์",
      "ลำดับเวลา",
      "Kara no Kyoukai"
    ],
    "keysecondary": [
      "chronological",
      "release order",
      "chapters",
      "order",
      "timeline",
      "year",
      "date",
      "canon timeline"
    ],
    "content": """<Chronology_Structure_and_Viewing_Guide>
[THE CHRONOLOGY PARADOX: FILMS VS. TRUE IN-UNIVERSE TIME]
Kara no Kyoukai (The Garden of Sinners) is famously structured and published out of chronological order by Kinoko Nasu. The non-linear structure was deliberately chosen to present Shiki's fractured psyche as a puzzle that the audience pieces together alongside Kokutou Mikiya.

When setting an AI roleplay scene, generating narrative events, or retrieving character memories, the AI MUST anchor itself to the IN-UNIVERSE CHRONOLOGICAL DATE, NEVER the novel or film release number.

[1. FILM / NOVEL RELEASE ORDER VS. TRUE CHRONOLOGICAL ORDER]
- Film 1 / Novel 1: Overlooking View (Thanatos / 俯瞰風景) -> Occurs 4th chronologically [September 1998]
- Film 2 / Novel 2: A Study in Murder - Part 1 (...and nothing heart / 殺人考察(前)) -> Occurs 1st chronologically [April 1995 – February 1996]
- Film 3 / Novel 3: Remaining Sense of Pain (ever cry, never life / 痛覚残留) -> Occurs 3rd chronologically [Late July 1998]
- Film 4 / Novel 4: The Hollow Shrine (garan-no-dou / 伽藍の洞) -> Occurs 2nd chronologically [June – July 1998] (Coma: Feb 1996 – June 1998)
- Film 5 / Novel 5: Paradox Spiral (Paradox Paradigm / 矛盾螺旋) -> Occurs 5th chronologically [October – November 1998]
- Film 6 / Novel 6: Oblivion Recording (Fairy Tale / 忘却録音) -> Occurs 6th chronologically [January 1999]
- Film 7 / Novel 7: A Study in Murder - Part 2 (...not nothing heart / 殺人考察(後)) -> Occurs 7th chronologically [February 1999]
- Epilogue Film: Kara no Kyoukai (The Garden of Sinners / 空の境界) -> Occurs 8th chronologically [March 1999]
- Side-Story / Epilogue: Future Gospel (Mirai Fukuin / 未来福音) -> Spans August–October 1998 side-events and 2008–2010 adult epilogue.

[2. MASTER IN-UNIVERSE CHRONOLOGICAL TIMELINE (OVERVIEW)]
- Era 1: Pre-1995 -> Ancient Demon Hunter Clan foundations; Sengoku monk Araya Souren at Enryaku-ji; Aozaki Touko's Clock Tower years in London & Sealing Designation escape.
- Era 2: April 1995 – February 1996 -> High school meeting; 1995 dismemberment murders; male SHIKI revealed.
- Era 3: February 1996 – May 1998 -> The bamboo road accident; male SHIKI's suicidal dive; 2-year hospital coma in Room 404; Mikiya's flower vigil.
- Era 4: June – July 1998 -> Awakening to the Lines of Death; Touko's therapy infiltration; corpse puppet battle; first prosthetic puppet arm fitted.
- Era 5: Late July 1998 -> Asagami Fujino incident; appendicitis triggers sensory return & Mystic Eyes of Distortion; Minato Bridge duel; Shiki severs appendix.
- Era 6: August – September 1998 -> Fujou Building rooftop suicide wave; Kirie Shizuno's astral double; Mikiya's trance; Shiki's arm crushed; Kirie's fall; October arm upgrade.
- Era 7: October – November 1998 -> Ogawa Mansion Taiji trap; Enjou Tomoe runaway; Araya captures Shiki; Touko duplicate immortality destroys Alba; Kanesada katana duel kills Araya Souren.
- Era 8: January 1999 -> Reien Girls' Academy memory loss; Kokutou Azaka undercover; Kurogiri Satsuki (*God's Word*) & memory fairies; Shiki severs conceptual fairies.
- Era 9: February 1999 -> 1995 killings resume; Shirazumi Lio (*Consumption*) unmasked; Mikiya kidnapped & blinded in left eye; Shiki commits her first & only human murder (killing Lio); Mikiya's eternal vow.
- Era 10: March 1999 -> Snowy bamboo road epilogue; Void Shiki (`「　」`) in furisode converses with Mikiya regarding the Root and human nature.
- Era 11: 2008 – 2010 -> Future Gospel (*Mirai Fukuin*); married life of Mikiya (eyepatch) and Shiki; detective agency with Mitsuru; daughter Ryougi Mana.
- Fate Crossover Anchor: February 2004 -> Fuyuki 5th Holy Grail War occurs when Shiki and Mikiya are ~24-25 years old in Mifune City; Araya has been dead for ~6 years.

[3. PHYSICAL & COGNITIVE STATE ANCHORS ACROSS TIME]
When narrating or roleplaying, verify character states against the active date:
- Shiki's Vision: Ordinary human eyesight (1995–Feb 1996) -> Pitch-black coma (1996–May 1998) -> Terrifying raw perception of Lines of Death (June 1998) -> Controlled Mystic Eyes of Death Perception (July 1998 onward).
- Shiki's Arms: Two biological arms (1995–Feb 1996) -> Paralyzed/atrophied biological arms (Coma) -> First puppet left arm (July 1998) -> Lost arm against Kirie (Sept 1998) -> Upgraded combat-hardened puppet arm capable of crushing stone and grasping spirits (October 1998 onward).
- Shiki's Personas: Dual soul Shiki & SHIKI active (1995–Feb 1996) -> SHIKI dead, leaving an agonizing empty void (June 1998 onward) -> Void Shiki (`「　」`) resting silently at the base of her connection to Akasha.
- Mikiya's Vision: Both eyes perfectly healthy (1995–Feb 1999) -> Left eye gouged/crushed by Lio (Feb 1999) -> Permanent left-eye blindness / black eyepatch (Feb 1999 onward).
- Residence: Ryougi Clan traditional mansion (1995–1996) -> Hospital Room 404 (1996–1998) -> Minimalist single-room apartment with tatami and unlocked lock (July 1998–1999) -> Joint home with Mikiya and daughter Mana (post-2000s).
</Chronology_Structure_and_Viewing_Guide>""",
    "constant": False,
    "selective": True,
    "selectiveLogic": 0,
    "order": 100,
    "position": 0,
    "disable": False,
    "ignoreBudget": False,
    "excludeRecursion": True,
    "preventRecursion": True,
    "probability": 100,
    "useProbability": True,
    "depth": 4,
    "displayIndex": 0
  },
  "1": {
    "uid": 1,
    "name": "Timeline_Era_1_Ancient_and_Pre_1995",
    "comment": "Timeline_Era_1_Ancient_and_Pre_1995",
    "key": [
      "Pre-1995",
      "KnK history",
      "Araya background",
      "Touko background",
      "Demon Hunter origin",
      "อารายะ",
      "โทโกะ",
      "ประวัติศาสตร์"
    ],
    "keysecondary": [
      "ancient",
      "London",
      "Enryaku-ji",
      "Clock Tower",
      "Aoko",
      "Sealing Designation",
      "Asagami",
      "Demon Hunter"
    ],
    "content": """<Timeline_Era_1_Ancient_and_Pre_1995>
[ERA 1: PRE-STORY HISTORICAL FOUNDATIONS & ANCIENT ROOTS]

1. THE SENGOKU ERA & ARAYA SOUREN'S ORIGIN (CIRCA 16TH CENTURY):
- The Monastery on Mount Hiei: Araya Souren was an ordained Buddhist monk of the Tendai sect residing on Mount Hiei at Enryaku-ji. Witnessing the horrific bloodshed, famine, and atrocities of the Sengoku Civil War—culminating in Oda Nobunaga's brutal siege and burning of Mount Hiei in 1571—Araya dedicated his existence to saving dying mortals.
- The Despair of Mortality: Araya tended to countless dying soldiers, women, and children. Yet no matter how desperately he prayed or applied medicine, every person died screaming in terror, despair, or agony. Araya realized the horrifying truth of human existence: saving individual lives is meaningless because death is the absolute, unavoidable conclusion of all living things.
- Awakening of his Origin: His psychological revulsion and longing for permanence awakened his Origin: "Stillness" / "Extinction" / "Taiji" (静止 / 無).
- The Sacred Sarira: Araya abandoned conventional salvation. Resolving to breach the Swirl of the Root (Akasha) to record the totality of all human deaths and uncover the ultimate meaning of existence, he surgically embedded sacred Sarira (calcified relics of ancient Buddhist arhats/saints) directly into his bone structure and spine. This granted him unaging biological immortality, immense physical density, and absolute spatial Bounded Fields (Kongo / 金剛).

2. THE FOUR ANCIENT DEMON HUNTER CLANS (TAIMA YONKE / 退魔四家):
- Origins: Ancient lineages in Japan that cultivated eugenic bloodline traits to slaughter non-human entities (demons, oni, phantasmal beasts, spiritual abominations) completely independent of the Western Mage's Association and the Holy Church:
  1. The Ryougi Clan (両儀): Masters of spatial mastery and dual-personality soul division (Kanji Shiki 式 [female/yin] and SHIKI 織 [male/yang]), creating human containers with split moral faculties to commit violence without karmic erosion.
  2. The Asagami Clan (浅神): Channelers possessing latent telekinetic spatial distortion (Mystic Eyes of Distortion), historically worshiped and feared as living calamities.
  3. The Fujou Clan (巫条): Spiritual mediums capable of detaching their souls as floating airborne projections and possessing the dead; afflicted with hereditary genetic blindness and frailty.
  4. The Nanaya Clan (七夜): Assassins bred for superhuman spatial movement, sensory reading, and instinctive slaughter of non-humans.

3. AOZAKI TOUKO'S CLOCK TOWER YEARS & SEALING DESIGNATION (1980S – EARLY 1990S):
- Department of Puppetry in London: Touko studies at the Clock Tower, achieving the supreme title of "Grand" (冠位 / Color designation: Red, which she violently despises).
- The London Triumvirate: Touko Aozaki, Araya Souren, and Cornelius Alba study together under Clock Tower auspices. Araya observes Touko's pursuit of the body; Alba develops a festering, obsessive inferiority complex toward Touko's genius.
- The Masterwork Puppet Bodies: Touko achieves a thaumaturgical miracle: fabricating autonomous, self-replicating puppet bodies identical to her living self down to cellular memory, soul resonance, and Magic Circuits. If Touko dies, a duplicate puppet immediately activates and continues living without identity loss—achieving functional immortality.
- The Sealing Designation: Terrified and covetous of her puppet technology, the Mage's Association issues an absolute Sealing Designation (封印指定) to dissect Touko's brain and preserve her talent in formaldehyde.
- Flight to Mifune City: Touko abandons London, kills multiple Clock Tower Enforcers, and establishes an undercover design and detective office, "Garan no Dou" (伽藍の洞), inside an abandoned, half-finished architectural high-rise in Mifune City.

4. PRE-1995 CHILDHOOD ANCHORS:
- 1979/1980: Ryougi Shiki is born to the head of the Ryougi clan. Her dual personas—female Shiki and male SHIKI—are rigorously trained in kenjutsu, etiquette, and clan traditions. Unknown even to her family, a third consciousness—Void Shiki (`「　」`), the Root itself—rests dormant at her core.
- Asagami Fujino: The Asagami branch declines into financial ruin; Fujino is adopted into the secondary Asagami household. After displaying telekinetic anomalies, her stepfather administers sensory-depressant drugs to paralyze her nervous system, rendering her completely insensate to physical pain.
- Shirazumi Lio: Born with the dormant Origin of "Consumption" (喰・捕食); lives a quiet, repressed school life until Araya scouts him in 1995.
- Kokutou Mikiya: Raised in peaceful, suburban normalcy in Mifune City alongside his younger sister Azaka.
</Timeline_Era_1_Ancient_and_Pre_1995>""",
    "constant": False,
    "selective": True,
    "selectiveLogic": 0,
    "order": 101,
    "position": 0,
    "disable": False,
    "ignoreBudget": False,
    "excludeRecursion": True,
    "preventRecursion": True,
    "probability": 100,
    "useProbability": True,
    "depth": 4,
    "displayIndex": 1
  },
  "2": {
    "uid": 2,
    "name": "Timeline_Era_2_1995_High_School_and_Murders",
    "comment": "Timeline_Era_2_1995_High_School_and_Murders",
    "key": [
      "1995",
      "A Study in Murder Part 1",
      "High school Shiki",
      "1995 serial killings",
      "ฆาตกรรม 1995",
      "ชิกิมัธยม"
    ],
    "keysecondary": [
      "meeting",
      "cherry blossoms",
      "kimono",
      "murders",
      "Mikiya",
      "SHIKI",
      "rain",
      "Shirazumi Lio"
    ],
    "content": """<Timeline_Era_2_1995_High_School_and_Murders>
[ERA 2: APRIL 1995 – FEBRUARY 1996 (CHAPTER 2 / FILM 2: A STUDY IN MURDER - PART 1)]

1. APRIL 1995: THE MEETING UNDER RAIN AND CHERRY BLOSSOMS:
- The Encounter: Kokutou Mikiya enters prefectural high school. Walking up the steep bamboo road on a rainy spring morning, he stops in his tracks. Standing beneath falling cherry blossoms is a breathtaking, solitary girl dressed in an immaculate white kimono under a black umbrella—Ryougi Shiki.
- Mikiya's Gentle Siege: Shiki is completely isolated at school—cold, razor-sharp, and unapproachable. Mikiya, possessing an extraordinary and immovable human empathy, repeatedly seeks her out. He brings lunch to the high school roof, sits beside her in comfortable silence, and shares his food. Shiki is deeply unsettled by Mikiya; unlike everyone else who either fears her or fawns over her clan status, Mikiya treats her like an ordinary teenage girl with zero fear and zero ulterior motives.

2. SEPTEMBER 1995: THE DISMEMBERMENT SERIAL MURDERS:
- The Inciting Massacre: Shirazumi Lio, an ordinary high school senior, is cornered by delinquent classmates. Lio snaps and bludgeons a bully to death in a dark alley. Araya Souren, who has been monitoring Mifune City for individuals with extreme Origins, appears before Lio. Araya awakens Lio's latent Origin of "Consumption" (喰・捕食) and commands him to embrace his nature.
- The Slaughterhouse Unleashed: Lio drinks his victim's blood, dismembers the corpse, and embarks on a grotesque serial murder spree across Mifune City. Victims are butchered, drained of blood, and arranged like artistic slaughterhouse exhibits.
- Shiki's Internal Nightmare: Shiki smells the fresh blood on the night air and wanders the crime scenes. Her innate hereditary impulse to kill begins resonating uncontrollably with the slaughter. Believing that her male persona, SHIKI, is sneaking out at night and butchering humans in fugue states, Shiki's mental stability deteriorates rapidly.

3. AUTUMN – WINTER 1995: THE DUAL IDENTITY & THE RAINY VIGIL:
- Mikiya Meets SHIKI (織): Walking late at night, Mikiya encounters Shiki on a pedestrian bridge. But the person standing before him smiles warmly with bright, boyish, energetic charm, speaking in casual masculine "ore" (オレ)—male persona SHIKI.
- SHIKI's Warning: SHIKI openly confesses his nature to Mikiya: *"Shiki and I are two sides of one coin. I am the impulse to destroy. And Mikiya... I want to kill you more than anything in the world. Stop coming near us."*
- Mikiya's Unyielding Faith: Despite knowing Shiki's murderous obsession, Mikiya refuses to abandon her. Every night, Mikiya sits on the curb outside the massive wooden gate of the Ryougi estate in the freezing rain, keeping vigil so Shiki knows she is tethered to humanity.
- Shiki's Torment: Watching Mikiya through her mansion window, Shiki realizes Mikiya's unconditional kindness is an existential threat to her murderous nature. To preserve her predatory identity, she must kill him; yet killing him will destroy her only anchor to sanity.

[CHARACTER STATUS IN 1995–EARLY 1996]
- Ryougi Shiki: Age 16. Two biological arms. NO Mystic Eyes of Death Perception. Possesses dual active personas (Shiki and SHIKI).
- Kokutou Mikiya: Age 16. High school student. Both eyes fully functional. Completely uninitiated into formal Magecraft, but anchored by absolute moral resolve.
- Shirazumi Lio: Active, hidden serial killer operating under Araya Souren's covert observation.
- Aozaki Touko: Residing at Garan no Dou; has NOT yet met Shiki or Mikiya.
</Timeline_Era_2_1995_High_School_and_Murders>""",
    "constant": False,
    "selective": True,
    "selectiveLogic": 0,
    "order": 102,
    "position": 0,
    "disable": False,
    "ignoreBudget": False,
    "excludeRecursion": True,
    "preventRecursion": True,
    "probability": 100,
    "useProbability": True,
    "depth": 4,
    "displayIndex": 2
  },
  "3": {
    "uid": 3,
    "name": "Timeline_Era_3_1996_1998_Accident_and_Coma",
    "comment": "Timeline_Era_3_1996_1998_Accident_and_Coma",
    "key": [
      "1996",
      "1997",
      "traffic accident 1996",
      "Shiki's coma",
      "hospital vigil",
      "อุบัติเหตุ 1996",
      "โคม่า 2 ปี"
    ],
    "keysecondary": [
      "crash",
      "truck",
      "SHIKI death",
      "coma",
      "flowers",
      "Mikiya",
      "Touko",
      "Yagami hospital"
    ],
    "content": """<Timeline_Era_3_1996_1998_Accident_and_Coma>
[ERA 3: FEBRUARY 1996 – MAY 1998 (THE ACCIDENT, COMA & TWO-YEAR VIGIL)]

1. FEBRUARY 1996: THE MIDNIGHT TORRENT & SHIKI'S SUICIDAL SACRIFICE:
- The Bamboo Forest Confrontation: On a night of torrential winter rain, Mikiya meets Shiki along the dark bamboo road. Shiki's containment breaks. In a frenzy of conflicting impulses, she tackles Mikiya into the mud, brandishing a blade against his throat.
- The Crisis of Love: Male SHIKI is fronting. He stares down into Mikiya's gentle, unresisting eyes. Mikiya does not fight back or plead; he simply accepts whatever Shiki chooses. SHIKI realizes with blinding clarity: He loves Mikiya too deeply to murder him, but his hereditary programming makes living beside Mikiya without killing him impossible.
- The Choice to Die: To permanently eliminate the murderous male persona and allow female Shiki to live a normal human life with Mikiya, SHIKI makes a split-second decision. Releasing Mikiya, SHIKI sprints into the middle of the road and dives directly into the headlights of an oncoming transport truck.
- The Collision: The truck strikes Shiki violently. Her body is thrown through the air, suffering catastrophic skull fractures, internal bleeding, and pulverized bones. Mikiya crawls through the mud, cradling her limp, bleeding form in his arms as the rain turns crimson.

2. MARCH 1996 – MAY 1998: THE TWO-YEAR COMA (ROOM 404, YAGAMI GENERAL HOSPITAL):
- Medical Brain Death: Shiki is rushed to Yagami General Hospital. Surgeons repair her shattered body, but she falls into a deep, vegetative coma. Doctors conclude she has suffered irreversible brain death and will never wake up.
- The Dissolution of SHIKI: Within the deep metaphysical darkness of the coma, male persona SHIKI absorbs the full impact of spiritual death. Over two agonizing years, SHIKI's soul slowly dissolves and dissipates into the nothingness of the Root. Female Shiki's body survives, but her internal spiritual structure is left as a hollow, gutted container.
- Mikiya's Metamorphosis:
  * Mikiya graduates high school alone in March 1997. He enrolls in university to study sociology, but feels hollow and detached from campus life.
  * In early 1998, Mikiya visits an art exhibition showcasing uncanny, lifelike puppet dolls. He is transfixed by a doll crafted by Aozaki Touko—a vessel so biologically perfect yet completely devoid of a soul, exactly like the comatose Shiki.
  * Mikiya drops out of university immediately, visits Garan no Dou, and begs Touko for employment. Impressed by his absurdly superhuman investigative talent and absolute lack of self-interest, Touko hires him as her primary detective.
- The Weekly Flower Vigil:
  * Every single weekend without fail for 24 consecutive months (over 100 visits), Mikiya walks to Room 404 of Yagami General Hospital.
  * He replaces the vase with fresh seasonal flowers, sits beside Shiki's bed, gently reads books aloud, and speaks of everyday weather, never doubting for a single second that she will open her eyes.

[ROLEPLAY DIRECTIVE FOR 1996–MAY 1998 SCENES]
- Shiki is completely bedridden, comatose, and biologically unresponsive. Any dialogue involving Shiki during this era must take place exclusively within her comatose spiritual landscape or in pre-1996 flashbacks.
- Mikiya works for Touko starting in early 1998, but Shiki has NEVER met Touko during this time.
</Timeline_Era_3_1996_1998_Accident_and_Coma>""",
    "constant": False,
    "selective": True,
    "selectiveLogic": 0,
    "order": 103,
    "position": 0,
    "disable": False,
    "ignoreBudget": False,
    "excludeRecursion": True,
    "preventRecursion": True,
    "probability": 100,
    "useProbability": True,
    "depth": 4,
    "displayIndex": 3
  },
  "4": {
    "uid": 4,
    "name": "Timeline_Era_4_Summer_1998_Awakening_and_MEoDP",
    "comment": "Timeline_Era_4_Summer_1998_Awakening_and_MEoDP",
    "key": [
      "June 1998",
      "The Hollow Shrine",
      "Shiki awakening",
      "Summer 1998",
      "Garan no Dou chapter",
      "ตื่นจากโคม่า",
      "เนตรมรณะตื่น"
    ],
    "keysecondary": [
      "hospital",
      "bandages",
      "corpse",
      "MEoDP",
      "prosthetic",
      "Touko",
      "awakening",
      "Room 404"
    ],
    "content": """<Timeline_Era_4_Summer_1998_Awakening_and_MEoDP>
[ERA 4: JUNE – JULY 1998 (CHAPTER 4 / FILM 4: THE HOLLOW SHRINE / GARAN-NO-DOU)]

1. JUNE 1998: AWAKENING INTO THE HORROR OF DEATH:
- The Empty Vessel Awakens: In early June 1998, Shiki suddenly opens her eyes in Room 404. But the world she awakens to is an incomprehensible nightmare. Because male SHIKI died, her soul container is hollow, creating an open gateway connected directly to the Swirl of the Root (Akasha).
- Manifestation of the Mystic Eyes of Death Perception (直死の魔眼): Her visual cortex is flooded with the conceptual principle of mortality. She sees irregular, jagged black lines and glowing points of cessation (Shisen and Shiten) etched into every surface—the walls, the hospital sheets, the IV tubes, the flesh of nurses, and the drifting dust motes.
- Sensory Madness: Seeing death as a living, vibrating physical reality overwhelms her psyche. Terrified that touching a line will obliterate existence, and believing herself to be a grotesque monster, Shiki claws savagely at her own eyes with her fingernails. Hospital doctors restrain her wrists and wrap thick layers of medical gauze over her eyes, plunging her into pitch-black confinement.

2. JULY 1998: TOUKO'S UNDERCOVER ENTRY & CONCEPTUAL LESSONS:
- The Speech Therapist: Alerted by Mikiya that Shiki has awakened, Aozaki Touko infiltrates Yagami General Hospital disguised as a clinical speech therapist.
- The Anatomy of the Mystic Eyes: Touko sits beside Shiki's bed in the dark. She explains that Shiki's eyes are not an optical curse, but a rare cognitive circuit linked to the origin of the universe:
  * "You aren't seeing the future, Shiki. You are perceiving the inherent mortality built into all matter from the moment it came into being. Everything that has a beginning must have an end. If you can perceive that end, you can sever it."
  * Touko teaches Shiki cognitive discipline: to close off the perceptual channel and see the world normally unless she intentionally focuses her intent to kill.

3. THE BATTLE OF ROOM 404 (CORPSE PUPPET ASSAULT):
- Attracted by the Void: A swarm of wandering spirits and restless dead, magnetically drawn to the bottomless void connecting Shiki to the Root, gather outside the hospital. They possess a freshly deceased male corpse and break into Room 404 in the dead of night, seeking to drag Shiki's empty vessel into the underworld.
- Tearing Away the Bandages: With the corpse strangling her and Touko observing to test her resolve, Shiki makes her choice. Refusing to die passively like a hollow ghost, she tears the gauze bandages from her face.
- The First Incision: Glowing with iridescent blue-magenta luminance, Shiki draws a medical scalpel, perceives the single black line of conceptual possession anchoring the dead souls to the corpse, and executes a clean, precise incision. The spirit's existence is extinguished instantly; the corpse collapses into inanimate matter.

4. THE AFTERMATH & REBIRTH:
- Severing the Past: Sitting on her hospital bed, Shiki takes the scalpel and hacks off her long hair, symbolically severing her ties to the aristocratic Ryougi heiress of 1995.
- The First Prosthetic Arm: To replace her partially atrophied left arm, Touko fits Shiki with a custom magical prosthetic puppet arm made of enchanted resins, completely indistinguishable from real skin.
- Independence: Shiki refuses to return to her family estate. She rents a spartan, single-room apartment in Mifune City and officially accepts a retainer contract as Garan no Dou's primary combat specialist.
</Timeline_Era_4_Summer_1998_Awakening_and_MEoDP>""",
    "constant": False,
    "selective": True,
    "selectiveLogic": 0,
    "order": 104,
    "position": 0,
    "disable": False,
    "ignoreBudget": False,
    "excludeRecursion": True,
    "preventRecursion": True,
    "probability": 100,
    "useProbability": True,
    "depth": 4,
    "displayIndex": 4
  },
  "5": {
    "uid": 5,
    "name": "Timeline_Era_5_July_1998_Remaining_Sense_of_Pain",
    "comment": "Timeline_Era_5_July_1998_Remaining_Sense_of_Pain",
    "key": [
      "July 1998",
      "Remaining Sense of Pain",
      "Fujino incident",
      "Minato bridge battle",
      "ฟูจิโนะ",
      "สะพานมินาโตะ 1998"
    ],
    "keysecondary": [
      "Fujino",
      "distortion",
      "bridge",
      "appendix",
      "pain",
      "delinquents",
      "rain",
      "Asagami"
    ],
    "content": """<Timeline_Era_5_July_1998_Remaining_Sense_of_Pain>
[ERA 5: LATE JULY 1998 (CHAPTER 3 / FILM 3: REMAINING SENSE OF PAIN)]

1. THE ASSAULT IN THE DOCKS & THE RETURN OF PAIN:
- The Violation: In an abandoned dive bar in Mifune's industrial warehouse district, Asagami Fujino is held captive and repeatedly assaulted by a gang of local high school delinquents led by Keita.
- The Acute Appendicitis Catalyst: During the brutal assault, Fujino suffers a sudden, catastrophic attack of acute appendicitis. The intense internal inflammation sends a massive shockwave through her chemically suppressed nervous system, breaking through the sedation drugs administered by her stepfather since childhood.
- The Awakening of Distortion: For the first time in years, Fujino feels real, agonizing physical pain. The psychological shock violently re-awakens her dormant psychic bloodline: the Mystic Eyes of Distortion (歪曲の魔眼).
- The Slaughter: Perceiving telekinetic axes of rotation (green and magenta rotational fields), Fujino turns her gaze on her abusers. She telekinetically twists their limbs, spines, and torsos into mangled spirals of bone and meat, butchering the entire gang except for Keita, who flees in sheer terror.

2. THE REVENGE HUNT & MIKIYA'S ENCOUNTER:
- The Citywide Purge: Fujino stalks the surviving delinquents across Mifune City. Wherever she finds them, she bends steel telephone booths, shipping containers, and human bodies like twisted wet rags.
- Shelter in the Storm: On a rainy night, Kokutou Mikiya discovers Fujino shivering and feverish near a payphone. Completely unaware that she is the perpetrator of the gruesome murders, Mikiya takes her back to his apartment, cooks hot soup, gives her fever medicine, and provides a safe bed. Fujino is profoundly touched by Mikiya's gentle, unconditional kindness, leaving quietly the next morning to complete her vengeance.

3. THE MINATO BRIDGE DUEL:
- The Interception: Touko traces Fujino's telekinetic trajectory to the massive Minato suspension bridge, which Fujino has chosen as the execution ground for Keita. Touko dispatches Shiki to neutralize Fujino.
- The Battle in the Typhoon: A torrential storm lashes the bridge. Fujino unleashes the full, terrifying magnitude of her psychic power: she looks at the massive steel support cables, concrete roadbeds, and structural towers of the bridge, telekinetically twisting the entire bridge framework into warped spirals.
- Shiki's Conceptual Incision: Trapped on the collapsing bridge, Shiki realizes that Fujino's telekinesis is not a physical object, but a conceptual field of spatial rotation. Activating her Mystic Eyes of Death Perception, Shiki literally perceives the "rotational axis" of the distortion in the air—and cuts it. With a slash of her knife, Shiki slices the telekinetic field itself, neutralizing Fujino's attack.
- The Surgical Mercy: Shiki closes the distance, plunging her knife into Fujino's abdomen. Instead of killing Fujino, Shiki uses her Mystic Eyes to locate the lines of death of Fujino's gangrenous, burst appendix. Shiki cleanly excises the diseased organ from Fujino's body, ending her killing spree while deliberately sparing her life.
- Aftermath: Fujino collapses from blood loss and exhaustion, surviving the duel. Touko arrives with medical transport, hospitalizes Fujino under psychiatric isolation, and legally suppresses her involvement in the murders, leaving Fujino alive to recover in peace.
</Timeline_Era_5_July_1998_Remaining_Sense_of_Pain>""",
    "constant": False,
    "selective": True,
    "selectiveLogic": 0,
    "order": 105,
    "position": 0,
    "disable": False,
    "ignoreBudget": False,
    "excludeRecursion": True,
    "preventRecursion": True,
    "probability": 100,
    "useProbability": True,
    "depth": 4,
    "displayIndex": 5
  },
  "6": {
    "uid": 6,
    "name": "Timeline_Era_6_September_1998_Overlooking_View",
    "comment": "Timeline_Era_6_September_1998_Overlooking_View",
    "key": [
      "September 1998",
      "Overlooking View",
      "Fujou suicides",
      "Kirie Shizuno incident",
      "ตึกฟุโจ",
      "คิริเอะ 1998"
    ],
    "keysecondary": [
      "Kirie",
      "rooftop",
      "suicide",
      "floating",
      "skyscraper",
      "Thanatos",
      "fall",
      "Fujou building"
    ],
    "content": """<Timeline_Era_6_September_1998_Overlooking_View>
[ERA 6: AUGUST – SEPTEMBER 1998 (CHAPTER 1 / FILM 1: OVERLOOKING VIEW)]

1. THE SUICIDE WAVE AT THE FUJOU BUILDING:
- The Epidemic of Falls: Between August and September 1998, eight high school girls leap to their deaths from the rooftop of the condemned 32-story Fujou Building in Mifune City.
- The Anomalies: None of the victims attend the same school; none have histories of depression; none leave suicide notes; and all are discovered with serene, blissful expressions on their faces. The police are completely baffled, treating it as an inexplicable contagion of mass hysteria.

2. KIRIE SHIZUNO & ARAYA'S EXPERIMENT:
- The Dying Medium: Kirie Shizuno, the sole surviving daughter of the ancient Fujou demon-hunting clan, lies bedridden in the terminal ward of Yagami General Hospital. Blind, bedridden, and dying from a chronic wasting illness, Kirie has spent years staring out her window at the towering silhouette of the Fujou Building.
- Araya's Catalyst: Araya Souren visits Kirie's hospital room. Recognizing her latent medium capabilities, Araya bestows upon her the ability to detach her spiritual consciousness, manifesting an autonomous, airborne astral double.
- The Illusion of Flight: Kirie's astral projection drifts across the night skies of Mifune City. Desperately lonely and intoxicatingly addicted to the sensation of floating above the earth, her projection gathers atop the Fujou Building. When spiritually sensitive girls wander near the rooftop, Kirie's projection connects with their latent desires to escape reality, offering them the "gift" of flight—which results in their bodies plunging thirty-two floors to the concrete below.

3. MIKIYA'S SPIRITUAL CAPTURE:
- The Hypnotic Trance: Investigating the deaths on Touko's orders, Kokutou Mikiya visits the Fujou Building at dusk. Reaching the rooftop, he encounters Kirie's floating astral projection.
- The Bound Soul: Sensing Mikiya's bottomless empathy and gentle warmth, Kirie's spirit clings to him, anchoring his consciousness to the sky. Mikiya falls into an unresponsive comatose trance at his apartment, his soul trapped in spiritual stasis on the rooftop.

4. SHIKI'S ROOFTOP ASSAULT & CLIMAX:
- Confrontation in the Mist: Enraged by Mikiya's capture, Shiki ascends to the roof of the Fujou Building in the dead of night. She finds eight floating, ghostly phantom doubles of Kirie drifting like pale specters above the abyss.
- The Sacrifice of the Arm: During the combat, Kirie's phantom doubles seize Shiki's left arm with superhuman crushing force, attempting to pull her over the ledge. Refusing to yield, Shiki draws her utility knife and severs her own puppet arm at the elbow joint to free herself.
- The Conceptual Severance: Activating her Mystic Eyes of Death Perception, Shiki sees the pale conceptual thread connecting Kirie's astral projection to the distant hospital. Shiki lunges and slices through the conceptual tether, permanently destroying Kirie's astral projection and freeing Mikiya's soul from the sky.
- Kirie's Final Awakening: In her hospital bed, Kirie wakes up completely alone. Touko visits her, explaining the cruel difference between "floating" (aimless escape) and "flying" (navigating gravity with purpose). Wanting to experience the real, physical sensation of the world before she dies, Kirie wheels her chair to the hospital roof and throws herself over the edge, experiencing a true fall.

5. OCTOBER 1998: THE UPGRADED COMBAT PUPPET ARM:
- Following the destruction of Shiki's first puppet arm in the battle with Kirie, Touko spends October 1998 crafting Shiki's definitive, high-grade magical combat prosthetic arm.
- Constructed from hardened composite resins and enchanted puppet fibers, the new arm possesses superhuman crushing power (capable of cracking concrete and pulverizing bone), can grasp intangible spiritual entities, and features a specialized release mechanism at the elbow.
</Timeline_Era_6_September_1998_Overlooking_View>""",
    "constant": False,
    "selective": True,
    "selectiveLogic": 0,
    "order": 106,
    "position": 0,
    "disable": False,
    "ignoreBudget": False,
    "excludeRecursion": True,
    "preventRecursion": True,
    "probability": 100,
    "useProbability": True,
    "depth": 4,
    "displayIndex": 6
  },
  "7": {
    "uid": 7,
    "name": "Timeline_Era_7_November_1998_Paradox_Spiral",
    "comment": "Timeline_Era_7_November_1998_Paradox_Spiral",
    "key": [
      "November 1998",
      "Paradox Spiral",
      "Araya Souren incident",
      "Ogawa Mansion battle",
      "ตึกโอกาวะ 1998",
      "อารายะ โซเร็น",
      "เอ็นโจ โทโมเอะ"
    ],
    "keysecondary": [
      "Araya",
      "Tomoe",
      "Alba",
      "katana",
      "Kanesada",
      "Taiji",
      "puppet body",
      "Ogawa Mansion"
    ],
    "content": """<Timeline_Era_7_November_1998_Paradox_Spiral>
[ERA 7: OCTOBER – NOVEMBER 1998 (CHAPTER 5 / FILM 5: PARADOX SPIRAL)]

1. THE ARCHITECTURAL HORROR OF OGAWA MANSION:
- The Taiji Crucible: Araya Souren designs and oversees the construction of Ogawa Mansion, a colossal, circular 10-story apartment complex in Mifune City. Built explicitly in the shape of a Taoist Taiji (Yin-Yang) diagram, the complex is divided into an East wing and a West wing.
- The 50 Family Loop: Araya fills the building with 50 dysfunctional families. His Bounded Field slowly amplifies their psychological paranoia, jealousy, and rage until every single family murders one another.
- The Recursive Rebirth: Using synthetic puppet corpses, Araya resets the complex every midnight. The residents wake up believing it is still the same day, repeat their daily arguments, and murder each other anew every night. Through this infinite recursive loop of human slaughter, Araya extracts the conceptual essence of human death to drill an opening directly into the Root.

2. OCTOBER 1998: ENJOU TOMOE'S RUNAWAY COMPANIONSHIP:
- The Escape: Runaway teenager Enjou Tomoe believes he snapped and butchered his parents in Room 405. Wandering the rain-slicked night streets clutching his bloodied utility knife, he is ambushed by street punks and rescued by Shiki.
- Living in Shiki's Apartment: Shiki takes Tomoe into her minimalist single-room apartment. For one month (late October to late November 1998), they share quiet, domestic life. Tomoe cooks meals, buys groceries, and falls deeply in love with Shiki's aloof, guarded vulnerability.

3. NOVEMBER 1998: THE INFILTRATION & THE CRUEL TRUTH:
- Entering Ogawa Mansion: Tomoe convinces Shiki to accompany him to Ogawa Mansion to face his past. Investigating Room 405, they find his parents alive, eating dinner, repeating the identical argument.
- The Corpse in the Back: Breaking through the partition, they find the terrifying reality: the rotting, decomposing corpses of Tomoe's parents—and the rotting corpse of Enjou Tomoe himself. The Tomoe standing beside Shiki is merely a synthetic puppet duplicate fabricated by Araya, endowed with the real Tomoe's dying memories.
- The Spatial Stasis Trap: Araya Souren manifests. Activating his absolute spatial Bounded Field, Araya captures Shiki within a pocket dimension between dimensions, freezing her in stasis to seal her empty vessel forever.

4. THE DUEL OF THE MAGI & TOUKO'S RESURRECTION:
- Touko Infiltrates: Alerted by Mikiya, Aozaki Touko enters the building to rescue Shiki. She is confronted by her former London classmate Cornelius Alba and Araya Souren in the central atrium.
- Touko's "Death": Alba unleashes scorching fire magecraft; Touko counters with ancient Norse runes. However, Araya intervenes, bypasses Touko's defenses, and crushes her heart with his bare hands. Alba gleefully decapitates Touko's corpse with a spell.
- The Duplicate Awakens: Miles away in a secure facility, a standby duplicate puppet of Touko awakens, lights a cigarette, and heads to Ogawa Mansion. Entering the complex, she confronts the horrified Alba: *"Did you really think killing one body would end me?"* She opens her leather briefcase familiar; the eldritch monstrosity inside tears Alba apart and devours him alive.

5. TOMOE'S SACRIFICE & THE FINAL CLIMAX:
- Reclaiming Humanity: Puppet Tomoe, overcoming his artificial programming through pure, stubborn human devotion to Shiki, charges into the collapsing building to retrieve Shiki's ancestral Kanesada katana from Araya's central altar.
- Tomoe's Death: Tomoe stabs Araya with his pocket knife, buying the vital seconds Shiki needs to break free from the spatial barrier. Araya crushes Tomoe's skull, solemnly acknowledging that Tomoe's artificial soul became authentically human through love.
- The Kanesada Duel: Shiki breaks the stasis, equips the ancient Kanesada katana, and engages Araya in the central courtyard. Dual-wielding blade and knife with the full, terrifying martial lineage of the Ryougi clan, Shiki slices through Araya's triple Kongo Bounded Fields, parries his spatial compression strikes, and plunges the blade through his Point of Death in his sternum.
- The Dissolution: As Ogawa Mansion collapses into ruin, Araya Souren accepts that an empty vessel can never be grasped, dissolving into the nothingness of the Root.
</Timeline_Era_7_November_1998_Paradox_Spiral>""",
    "constant": False,
    "selective": True,
    "selectiveLogic": 0,
    "order": 107,
    "position": 0,
    "disable": False,
    "ignoreBudget": False,
    "excludeRecursion": True,
    "preventRecursion": True,
    "probability": 100,
    "useProbability": True,
    "depth": 4,
    "displayIndex": 7
  },
  "8": {
    "uid": 8,
    "name": "Timeline_Era_8_January_1999_Oblivion_Recording",
    "comment": "Timeline_Era_8_January_1999_Oblivion_Recording",
    "key": [
      "January 1999",
      "Oblivion Recording",
      "Reien Academy incident",
      "Azaka investigation",
      "โรงเรียนเรเอ็น 1999",
      "คุโรกิริ ซัตสึกิ",
      "อาซากะ"
    ],
    "keysecondary": [
      "Azaka",
      "fairy",
      "Misaya",
      "Kurogiri",
      "God's Word",
      "memory",
      "chapel",
      "Reien Academy"
    ],
    "content": """<Timeline_Era_8_January_1999_Oblivion_Recording>
[ERA 8: JANUARY 1999 (CHAPTER 6 / FILM 6: OBLIVION RECORDING)]

1. THE MEMORY THEFT AT REIEN GIRLS' ACADEMY:
- The Incident: In January 1999, Touko Aozaki receives an urgent request from the administration of Reien Girls' Academy, an elite Catholic boarding school. Multiple students have suffered sudden, inexplicable memory erasure, emotional apathy, and personality dissociation.
- Azaka's Undercover Mission: Touko dispatches her apprentice—Kokutou Azaka (Mikiya's younger sister)—to investigate the academy undercover. Touko equips Azaka with enchanted salamander-skin gloves to channel her latent Ignition Magecraft (発火魔術).

2. KUROGIRI SATSUKI & THE UNIFIED LANGUAGE:
- The Master of God's Word: Behind the memory theft is Kurogiri Satsuki (*God's Word* / 言葉の魔術師), an enigmatic magus born with the Origin of "Forgetfulness" (忘却). Kurogiri speaks the Unified Language (the pre-Tower of Babel universal tongue) which directly overwrites the listener's subconscious mind, forcing whatever he speaks to become absolute truth.
- The Fairy Infestation: Kurogiri manipulates student council member Ouryou Misaya, deploying invisible, conceptual "fairies" (妖精) throughout the school grounds. These fairies feed upon the traumatic, painful memories of students, leaving them peaceful, empty, and spiritually lobotomized.

3. SHIKI'S INFILTRATION & THE CHAPEL CLASH:
- Shiki Enters Reien: Touko dispatches Shiki to back up Azaka. Disguised in a French-style school uniform worn beneath her traditional kimono, Shiki infiltrates the academy grounds, immediately sensing the conceptual distortion in the air.
- Azaka vs. Misaya: Azaka confronts Misaya in the academy chapel. Using her salamander gloves, Azaka ignites the telekinetic puppets and threads manipulated by Misaya, defeating her through sheer magical firepower and personal conviction.
- Shiki vs. The Conceptual Fairies: Shiki enters the snowy forest outside the chapel, where a swarm of hundreds of invisible memory fairies attacks her. Because fairies are pure conceptual entities without physical bodies, conventional weapons are useless. Activating her Mystic Eyes of Death Perception, Shiki perceives the glowing lines of death on their invisible wings and slices the swarm out of reality with surgical precision.

4. THE CONFRONTATION WITH GOD'S WORD & AFTERMATH:
- The Conceptual Severance: Shiki confronts Kurogiri Satsuki. Kurogiri attempts to speak his Unified Language to erase her memories, but Shiki's connection to the Root renders her immune to linguistic manipulation. Shiki draws her knife and slices through the conceptual Bounded Field anchoring Kurogiri's magic to the academy.
- The Peaceful Departure: Shiki spares Kurogiri's life; Kurogiri calmly concedes defeat and departs the academy grounds. The stolen memories return to the students, leaving Azaka to reconcile her feelings for Mikiya.
- Foreshadowing the Climax: Weeks later in late January 1999, an awakened Shirazumi Lio tracks down Kurogiri Satsuki in a dark alleyway and brutally murders him, stealing his blood and resources.
</Timeline_Era_8_January_1999_Oblivion_Recording>""",
    "constant": False,
    "selective": True,
    "selectiveLogic": 0,
    "order": 108,
    "position": 0,
    "disable": False,
    "ignoreBudget": False,
    "excludeRecursion": True,
    "preventRecursion": True,
    "probability": 100,
    "useProbability": True,
    "depth": 4,
    "displayIndex": 8
  },
  "9": {
    "uid": 9,
    "name": "Timeline_Era_9_February_1999_A_Study_in_Murder_Part_2",
    "comment": "Timeline_Era_9_February_1999_A_Study_in_Murder_Part_2",
    "key": [
      "February 1999",
      "A Study in Murder Part 2",
      "Lio Shirazumi incident",
      "Shiki's murder",
      "Mikiya's blinding",
      "ฆาตกรรม 1999",
      "ชิราซุมิ ริโอ",
      "มิกิยะตาบอด"
    ],
    "keysecondary": [
      "Lio",
      "Consumption",
      "blinded",
      "eye",
      "first kill",
      "promise",
      "sin",
      "warehouse",
      "murder"
    ],
    "content": """<Timeline_Era_9_February_1999_A_Study_in_Murder_Part_2>
[ERA 9: FEBRUARY 1999 (CHAPTER 7 / FILM 7: A STUDY IN MURDER - PART 2) - THE CLIMAX]

1. THE RESUMPTION OF THE 1995 SLAUGHTER:
- The Murders Return: In early February 1999, the exact dismemberment homicides from 1995 suddenly resume across Mifune City. Bodies are found torn to shreds, disemboweled, and gnawed.
- The Truth Revealed: Shirazumi Lio, whose Origin of "Consumption" was awakened by Araya Souren in 1995, emerges from the shadows. Lio was the true killer behind the 1995 murders all along; Shiki was completely innocent. Lio has been distributing a narcotic called "Blood Chip" to create an occult feeding frenzy throughout the criminal underworld.

2. THE CAPTURE & BLINDING OF KOKUTOU MIKIYA:
- The Abduction: Lio stalks and kidnaps Kokutou Mikiya, dragging him to an abandoned slaughterhouse warehouse.
- The Interrogation: Lio is obsessed with forcing Mikiya to despair. Lio demands that Mikiya renounce his love for Shiki and admit that Shiki is an irredeemable monster just like him.
- Mikiya's Unshakable Faith: Bound, beaten, and covered in blood, Mikiya looks directly at Lio and quietly refuses: *"Shiki has never murdered anyone. And even if the whole world calls her a monster, I will believe in her until the end."*
- The Blinding: Enraged beyond reason by Mikiya's pure moral conviction, Lio brutally gouges and crushes Mikiya's left eye with his fingers, leaving Mikiya bleeding, unconscious, and dying on the cold concrete.

3. THE SLAUGHTERHOUSE CLIMAX & SHIKI'S FIRST MURDER:
- The Descent into Madness: Shiki tracks the scent of blood to the warehouse. Discovering Mikiya's motionless body lying in a pool of blood with his eye gouged out, Shiki believes Mikiya is dead.
- The Rupture of the Vow: The fragile thread holding Shiki's humanity together snaps completely. Her four-year vow to Mikiya—never to cross the line into becoming a murderer—crumbles into blinding, homicidal fury.
- The Feral Duel: Lio drinks his own concoctions, transforming into a feral, rabid beast that moves with terrifying speed. Shiki meets his frenzy with cold, lethal precision. In a whirlwind of blood and flashing steel, Shiki drives her utility knife into Lio's chest, perceives his lines of death, and carves through his heart, killing Shirazumi Lio.
- The Threshold Crossed: This is Shiki's first, only, and permanent murder of an authentic human being in her lifetime.

4. THE FULFILLED VOW IN THE BLOOD:
- The Weeping Killer: Standing over Lio's corpse in the pouring rain, Shiki collapses to her knees. She weeps in despair, believing she has broken her promise, destroyed her soul, and lost Mikiya forever.
- The Resurrection of Hope: Stirring from the darkness, Mikiya crawls across the blood-slicked concrete. Holding his bleeding, ruined eye, Mikiya wraps his arms around Shiki's trembling form.
- The Eternal Promise: Mikiya whispers into her hair: *"I won't let you carry this alone, Shiki. Four years ago, I promised you that I would bear your sin with you. Even if you become a murderer, we will carry this burden together for the rest of our lives."*
</Timeline_Era_9_February_1999_A_Study_in_Murder_Part_2>""",
    "constant": False,
    "selective": True,
    "selectiveLogic": 0,
    "order": 109,
    "position": 0,
    "disable": False,
    "ignoreBudget": False,
    "excludeRecursion": True,
    "preventRecursion": True,
    "probability": 100,
    "useProbability": True,
    "depth": 4,
    "displayIndex": 9
  },
  "10": {
    "uid": 10,
    "name": "Timeline_Era_10_March_1999_Epilogue_and_Future",
    "comment": "Timeline_Era_10_March_1999_Epilogue_and_Future",
    "key": [
      "March 1999",
      "KnK Epilogue",
      "Void Shiki conversation",
      "Mirai Fukuin",
      "Future Gospel",
      "2008",
      "2010",
      "วอยด์ชิกิ",
      "มิไร ฟุคุอิน",
      "เรียวกิ มานะ"
    ],
    "keysecondary": [
      "snow",
      "bamboo",
      "Mana",
      "Mitsuru",
      "marriage",
      "daughter",
      "adult Shiki",
      "eyepatch",
      "Ryougi Mana"
    ],
    "content": """<Timeline_Era_10_March_1999_Epilogue_and_Future>
[ERA 10: MARCH 1999 & POST-STORY (EPILOGUE / MIRAI FUKUIN / 2008–2010)]

1. MARCH 1999: THE EPILOGUE IN THE FALLING SNOW:
- The Snowy Bamboo Road: One month after Lio's death, Kokutou Mikiya—his left eye bandaged and vision permanently lost—walks down the snow-covered bamboo road where he first saw Shiki in 1995.
- Manifestation of Void Shiki (`「　」` / Root Shiki): Emerging from the falling snowflakes is a breathtaking figure dressed in a lavish, long-sleeved furisode kimono—the third personality, Void Shiki.
- The Nature of the Void: Void Shiki speaks with gentle, feminine, motherly warmth. She explains the deepest mystery of her existence:
  * She is the consciousness of the Swirl of the Root (Akasha) itself, directly embodied in Shiki's physical form. Because she is connected to everything that was, is, and ever will be, she can rewrite reality, alter causality, or dissolve the universe with a single thought.
  * Yet she chooses not to act: *"Living as an omnipotent god is lonely and boring, Mikiya. Watching you and human Shiki struggle, make mistakes, and love each other is the only thing that gives warmth to existence."*
- The Parting Gift: Void Shiki offers to heal Mikiya's blinded left eye using reality-warping authority. Mikiya gently declines, explaining that his blind eye is the eternal physical proof of the promise he made to Shiki. Touched by his purity, Void Shiki smiles, grants him a peaceful farewell, and withdraws deep into the slumber of the soul, allowing human Shiki to live her life.

2. 1998 SIDE-STORIES: MIRAI FUKUIN (FUTURE GOSPEL / 未来福音):
- August 1998 (Mifune Bomber): Mitsuru Kamekura, a professional hitman possessing precognitive calculation (Measurement Precognition), plants bombs in Mifune City. Shiki intercepts him. Using her Mystic Eyes of Death Perception, Shiki literally cuts through his precognitive visual trajectory, saving his life and destroying his psychic curse.
- Shizuno Mana & Mother of Mifune: The clairvoyant fortune teller and the spiritual remnants of the city.

3. 2008 – 2010: THE ADULT DOMESTIC ERA (MIRAI FUKUIN EPILOGUE):
- Marriage & Clan Leadership: Mikiya and Shiki are legally married and living together as heads of the Ryougi clan in Mifune City. Shiki's hereditary murderous impulse has been completely subdued and healed by her peaceful family life with Mikiya.
- Mikiya's Detective Agency: Mikiya wears a distinguished black leather eyepatch over his blind left eye. Having taken in former bomber Mitsuru Kamekura, Mikiya runs an independent private investigation firm.
- Ryougi Mana (両儀未那):
  * Mikiya and Shiki have a vibrant, sharp-witted daughter named Ryougi Mana.
  * Mana possesses Shiki's sharp violet-black eyes and Mikiya's warm, gentle charisma. She adores her father unconditionally, playfully declaring war on her mother to "steal Papa away." Shiki watches their banter with quiet, deadpan maternal affection.

[FATE/STAY NIGHT 2004 CROSSOVER SYNCHRONIZATION]
- When the 5th Holy Grail War occurs in Fuyuki City in February 2004:
  * Ryougi Shiki and Kokutou Mikiya are 24–25 years old, living together as adults in Mifune City (~150 km away).
  * Araya Souren and Cornelius Alba have been dead for over 5 years.
  * Touko Aozaki has concluded her Sealing Designation negotiations with the Clock Tower, travels freely, and crafts the masterwork puppet body that saves Emiya Shirou in the Heaven's Feel true ending.
</Timeline_Era_10_March_1999_Epilogue_and_Future>""",
    "constant": False,
    "selective": True,
    "selectiveLogic": 0,
    "order": 110,
    "position": 0,
    "disable": False,
    "ignoreBudget": False,
    "excludeRecursion": True,
    "preventRecursion": True,
    "probability": 100,
    "useProbability": True,
    "depth": 4,
    "displayIndex": 10
  },
  "11": {
    "uid": 11,
    "name": "Timeline_Roleplay_Guardrails_Anachronisms",
    "comment": "Timeline_Roleplay_Guardrails_Anachronisms",
    "key": [
      "KnK anachronism rules",
      "timeline guardrails",
      "roleplay timeline rules",
      "KnK date rules",
      "กฎเวลา",
      "ป้องกันสปอยล์ข้ามเวลา"
    ],
    "keysecondary": [
      "rules",
      "spoilers",
      "memory",
      "future",
      "guidelines",
      "prompt",
      "dates",
      "anachronism"
    ],
    "content": """<Timeline_Roleplay_Guardrails_Anachronisms>
[ABSOLUTE MANDATORY ROLEPLAY LAWS: PREVENTING PREMATURE CHARACTER MEMORY]
When generating responses, dialogue, or internal thoughts in Kara no Kyoukai and crossover roleplay, the AI MUST strictly enforce these temporal boundaries based on the scene's active date:

1. BEFORE JUNE 1998 (HIGH SCHOOL & COMA ERA):
- Shiki CANNOT see Lines of Death. Do NOT describe glowing eyes, points of death, or death perception.
- Shiki has TWO biological arms. She does NOT have a puppet arm.
- Shiki and Touko Aozaki have NEVER met and do NOT know each other.
- Male SHIKI is alive and active (until February 1996). Shiki must exhibit the dual soul dichotomy.

2. BEFORE LATE JULY 1998 (PRE-FUJINO INCIDENT):
- Asagami Fujino is an ordinary, sensory-deprived high school girl. She has NOT awakened her Mystic Eyes of Distortion and has killed no one.
- Shiki has Touko's first, basic puppet arm (which can be damaged).

3. BEFORE SEPTEMBER 1998 (PRE-OVERLOOKING VIEW):
- Kirie Shizuno has NOT committed mass suicide. The Fujou Building is merely an abandoned skyscraper.
- Shiki's first puppet arm is intact until crushed in September 1998.

4. BEFORE NOVEMBER 1998 (PRE-PARADOX SPIRAL):
- Araya Souren and Cornelius Alba are ALIVE and actively orchestrating events from the shadows.
- Enjou Tomoe has NOT met Shiki.
- Shiki does NOT possess the Kanesada katana in her apartment (it is in the Ryougi clan vault / Araya's possession).

5. BEFORE FEBRUARY 1999 (PRE-A STUDY IN MURDER PART 2):
- Kokutou Mikiya has BOTH EYES FULLY FUNCTIONAL. He does NOT wear an eyepatch or suffer impaired vision.
- Shiki has NEVER COMMITTED MURDER. She has destroyed spirits, severed appendicitis, and neutralized barriers, but has NEVER taken an authentic human life.
- Shirazumi Lio is assumed to be an ordinary delinquent, NOT the 1995 serial killer.

6. IN FEBRUARY 2004 (FATE/STAY NIGHT ERA):
- Shiki and Mikiya are mature adults (age ~24-25), living together in Mifune City.
- Araya Souren and Cornelius Alba have been dead for over five years.
- Mikiya wears his black eyepatch over his blind left eye.
- Touko Aozaki travels between London and Japan, having resolved her Sealing Designation conflict.

7. CUSTOM ROLEPLAY OVERRIDE PROTOCOL:
- If {{user}}'s roleplay establishes an alternate timeline (e.g., saving Enjou Tomoe from death, unmasking Shirazumi Lio in 1995, preventing Mikiya from losing his eye, or intervening with Fate Servants), THE USER'S CHOICES OVERRIDE CANONICAL TIMELINE OUTCOMES. Do not force tragedy over user agency.
</Timeline_Roleplay_Guardrails_Anachronisms>""",
    "constant": False,
    "selective": True,
    "selectiveLogic": 0,
    "order": 111,
    "position": 0,
    "disable": False,
    "ignoreBudget": False,
    "excludeRecursion": True,
    "preventRecursion": True,
    "probability": 100,
    "useProbability": True,
    "depth": 4,
    "displayIndex": 11
  }
}

timeline_data = {
  "name": "Kara_no_Kyoukai_09_Timeline",
  "description": "Exhaustive, deeply detailed chronological reference module for Kara no Kyoukai and Nasuverse crossovers. Follows the canon story across all eras with scene-by-scene sequencing, character psychological states, antagonist grand designs, ability awakenings, temporal guardrails, and Fate 2004 synchronization without token constraints.",
  "scan_depth": 50,
  "token_budget": 50000,
  "recursive_scanning": False,
  "extensions": {},
  "entries": timeline_entries
}

output_path = "Kara No/09_Timeline.json"
with open(output_path, "w", encoding="utf-8") as f:
    json.dump(timeline_data, f, ensure_ascii=False, indent=2)

print("Exhaustive timeline successfully written to:", output_path)

