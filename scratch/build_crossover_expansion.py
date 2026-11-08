# -*- coding: utf-8 -*-
"""
Builder script to expand Kara No/12_Crossover_Dynamics.json to Canonical Masterwork Depth.
Fixes all pairing Thai keywords and adds 4 exhaustive combat physics entries:
- Entry 8: Crossover_Physics_MEoDP_vs_Servant_Spiritual_Cores (uid 8, order 138)
- Entry 9: Crossover_Physics_MEoDP_vs_God_Hand_Heracles (uid 9, order 139)
- Entry 10: Crossover_Physics_MEoDP_vs_Gate_of_Babylon_Gilgamesh (uid 10, order 140)
- Entry 11: Crossover_Physics_Magic_Resistance_and_Conceptual_Noble_Phantasms (uid 11, order 141)
"""
import json
import os

target_path = os.path.join(r"d:\Personalise\Homemad\Lorebook\Nasuverse\Kara No", "12_Crossover_Dynamics.json")

# Backup existing file before rewriting
backup_path = os.path.join(r"d:\Personalise\Homemad\Lorebook\Nasuverse\scratch\backups_crossover_expansion", "12_Crossover_Dynamics.json.orig")
os.makedirs(os.path.dirname(backup_path), exist_ok=True)
with open(target_path, "r", encoding="utf-8") as f:
    orig_content = f.read()
with open(backup_path, "w", encoding="utf-8") as f:
    f.write(orig_content)

entries_data = [
    # Entry 0: Pairing_Shiki_and_Shirou
    {
        "uid": 0,
        "name": "Pairing_Shiki_and_Shirou",
        "comment": "Pairing_Shiki_and_Shirou",
        "order": 130,
        "key": [
            "Ryougi Shiki",
            "Shiki Ryougi",
            "Shiki",
            "Emiya Shirou",
            "Shirou Emiya",
            "Shirou",
            "ชิกิกับชิโร่",
            "ชิโร่กับชิกิ",
            "เอมิยะกับเรียวกิ",
            "ชิกิกับเอมิยะ ชิโร่"
        ],
        "keysecondary": [
            "pairing",
            "crossover",
            "ideals",
            "cooking",
            "knife",
            "projection",
            "sword",
            "ความว่างเปล่ากับอุดมคติ",
            "การทำอาหาร",
            "มีดกับดาบ",
            "การสนทนาข้ามเรื่อง"
        ],
        "content": """<Pairing_Shiki_and_Shirou>
[CROSSOVER DYNAMICS: RYOUGI SHIKI & EMIYA SHIROU]

1. CONTRASTING VALUES & WORLDVIEWS:
- Shiki's worldview is defined by existential isolation, her hollow container, and a fierce, disciplined restraint against her murderous Origin. She values individual life with quiet realism and refuses to kill without absolute necessity.
- Shirou's worldview is defined by severe survivor's guilt, borrowed ideals, and a suicidal compulsion to save every person in front of him, even at the cost of his own life.

2. INITIAL IMPRESSIONS:
- What Shiki Notices: Shiki immediately senses Shirou's complete lack of self-preservation. She sees his "Hero of Justice" mindset not as noble heroism, but as a severe psychological pathology—a broken boy seeking an honorable excuse to die.
- What Shirou Notices: Shirou is unnerved by Shiki's predatory stillness, the cold weight of her dark eyes, and the lethal efficiency of her movements. Yet, his domestic instincts are triggered by her solitary demeanor, thin frame, and poor dietary habits.

3. SOURCES OF CONFLICT & RESPECT:
- Friction: Shiki openly mocks Shirou's naive altruism: "Throwing your life away for strangers who wouldn't care if you died isn't justice, kid. It's just trash disposal." Shirou is frustrated by her cold, unyielding pragmatism.
- Mutual Respect: Shiki recognizes that Shirou's foolish ideals are backed by genuine, unbending steel. When Shirou fights, he does not waver. Shirou, in turn, realizes Shiki is not a cruel monster, but someone fighting an agonizing internal war to protect her humanity.

4. NATURAL CONVERSATIONAL TOPICS:
- Food & Domestic Care: Shirou cooking proper Japanese meals (which disarms Shiki's emotional walls) versus Shiki surviving on strawberry Pocky, Häagen-Dazs, and canned coffee.
- The Nature of Blades: Shirou's Origin of "Sword" clashing with Shiki's understanding of cutting mortality.
- Dealing with Mikiya: Shiki's subtle realization that Shirou's stubborn earnestness uncomfortably resembles Mikiya's, making her softer on him than she would ever admit out loud.

5. ABILITIES & COMBAT INTERPLAY:
- Shiki's MEoDP can perceive the Lines of Death along Shirou's projected bladed weapons and shatter them with minimal contact. Shirou must rely on overwhelming ranged barrage (Projection) rather than close-quarters knife sparring.

6. DEVELOPMENT OVER REPEATED ENCOUNTERS:
- Evolves from sharp mutual suspicion into a begrudging, unspoken camaraderie. Shiki becomes an unsentimental sounding board who cuts through Shirou's self-deceptions; Shirou becomes a reliable ally whose cooking Shiki secretly looks forward to.

7. WHAT MUST NOT BE ASSUMED:
- Do NOT assume Shiki views Shirou romantically or treats him as a substitute for Mikiya.
- Do NOT assume Shirou convinces Shiki to become a hero, or that Shiki convinces Shirou to abandon his ideals.
</Pairing_Shiki_and_Shirou>"""
    },

    # Entry 1: Pairing_Shiki_and_Saber_Artoria
    {
        "uid": 1,
        "name": "Pairing_Shiki_and_Saber_Artoria",
        "comment": "Pairing_Shiki_and_Saber_Artoria",
        "order": 131,
        "key": [
            "Ryougi Shiki",
            "Shiki Ryougi",
            "Shiki",
            "Saber",
            "Artoria",
            "Artoria Pendragon",
            "King of Knights",
            "ชิกิกับเซเบอร์",
            "ชิกิกับอาร์โทเรีย",
            "เซเบอร์กับชิกิ"
        ],
        "keysecondary": [
            "knight",
            "chivalry",
            "blade",
            "Excalibur",
            "Invisible Air",
            "food",
            "ราชาอัศวินกับหญิงชุดกิโมโน",
            "เกียรตินักดาบ",
            "การประดาบ"
        ],
        "content": """<Pairing_Shiki_and_Saber_Artoria>
[CROSSOVER DYNAMICS: RYOUGI SHIKI & ARTORIA PENDRAGON (SABER)]

1. CONTRASTING VALUES & WORLDVIEWS:
- Shiki is a modern, street-level pragmatic assassin who fights with brutal economy, zero chivalry, and complete indifference to status, monarchies, or titles.
- Artoria is a legendary medieval monarch governed by formal knightly chivalry, royal duty, and an agonizing desire to undo the fall of Britain through the Holy Grail.

2. INITIAL IMPRESSIONS:
- What Shiki Notices: Shiki is completely unimpressed by Artoria's royal legend. To her eyes, Artoria is a tragic ghost trapped in ancient regrets, weighed down by heavy armor that conceals a fragile, stubborn young woman.
- What Saber Notices: Saber's Instinct skill blares with acute alarm. Despite Shiki's normal human body, Saber senses a chilling, conceptual lethality that completely bypasses standard magical defenses and armor.

3. CONFLICT & MUTUAL RECOGNITION:
- Philosophical Clash: Saber disapproves of Shiki's street-knife methods and lack of formal honor. Shiki mocks Saber's martyrdom: "A king who spends eternity crying over a fallen kingdom is just a fool who doesn't know when to bury the dead."
- Mutual Steel: Both are martial purists who have dedicated their lives to wielding edged weapons. When forced to fight side-by-side, their combat synchronization is razor-sharp.

4. NATURAL CONVERSATIONAL TOPICS:
- The Burden of Holding a Blade: What it means to take a life, the weight of the sword, and the scars left behind.
- Food & Rest: Artoria's legendary appetite confronting Shiki's deadpan observation of how much food a petite Servant can consume without exploding.
- Invisible Air: Shiki casually commenting on the true dimensions of Excalibur, which she can see right through the compressed wind by tracking its lines of death.

5. ABILITIES & COMBAT INTERPLAY:
- In a straight sprint, Saber's superhuman parameters (A-rank speed, Mana Burst) easily outclass Shiki's human muscles. However, Saber must fight with extreme defensive care; a single touch from Shiki's blade along Saber's lines of death will bypass her magical armor and sever her spiritual core.

6. DEVELOPMENT OVER REPEATED ENCOUNTERS:
- Shifts from wary standoff to mutual respect between warriors. Saber comes to understand that Shiki's lethality is governed by strict moral restraint; Shiki acknowledges that Saber's kingly resolve is forged in genuine, uncorrupted conviction.

7. WHAT MUST NOT BE ASSUMED:
- Do NOT assume Shiki is intimidated by Saber's legend or royal authority.
- Do NOT assume Saber treats Shiki as an evil monster without seeing her actions first.
</Pairing_Shiki_and_Saber_Artoria>"""
    },

    # Entry 2: Pairing_Shiki_and_Rin_Tohsaka
    {
        "uid": 2,
        "name": "Pairing_Shiki_and_Rin_Tohsaka",
        "comment": "Pairing_Shiki_and_Rin_Tohsaka",
        "order": 132,
        "key": [
            "Ryougi Shiki",
            "Shiki Ryougi",
            "Shiki",
            "Rin Tohsaka",
            "Tosaka Rin",
            "Tohsaka",
            "Rin",
            "ชิกิกับริน",
            "รินกับชิกิ",
            "โทซากะกับเรียวกิ",
            "ชิกิกับโทซากะ ริน"
        ],
        "keysecondary": [
            "jewels",
            "magus",
            "Clock Tower",
            "Gandr",
            "bickering",
            "Touko",
            "จอมเวทอัญมณีกับนักฆ่า",
            "ความสงสัยของริน",
            "พันธมิตรจำเป็น"
        ],
        "content": """<Pairing_Shiki_and_Rin_Tohsaka>
[CROSSOVER DYNAMICS: RYOUGI SHIKI & RIN TOHSAKA]

1. CONTRASTING VALUES & WORLDVIEWS:
- Shiki represents Japan's secretive, indigenous Demon Hunter aristocracy—practical, secretive, and dismissive of formal thaumaturgical hierarchy.
- Rin is an elite, proud Clock Tower magus educated in formal European foundations, obsessed with family legacy, prestige, and orthodox thaumaturgical perfection.

2. INITIAL IMPRESSIONS:
- What Shiki Notices: Shiki finds Rin's high-maintenance pride, sharp tongue, and aristocratic posturing exhausting. She immediately punctures Rin's serious persona with blunt disinterest.
- What Rin Notices: Rin is outraged by Shiki's casual disrespect for thaumaturgical traditions. She is deeply suspicious of Shiki's affiliation with Aozaki Touko (a notorious Clock Tower fugitive).

3. FRICTION & BANTER:
- Constant High-Tension Bickering: Rin lectures on thaumaturgical theory and leyline calculations; Shiki yawns, taps her pocket knife, and asks who needs to be cut. Shiki mocks Rin's expensive Jewel Magecraft as "throwing fifty thousand yen just to open a locked door."
- Mutual Irritation: Rin gets flustered and sputters when Shiki completely ignores her tactical plans and takes the most direct, lethal route.

4. NATURAL CONVERSATIONAL TOPICS:
- Aozaki Touko: Rin grilling Shiki about Touko's whereabouts, research, and personality; Shiki dryly responding that Touko is just a lazy chain-smoker who doesn't pay her bills.
- Urban Investigation: Comparing Clock Tower scrying with street-level tracking.
- Dealing with Difficult Partners: Rin complaining about Archer/Shirou; Shiki listening with deadpan silence.

5. ABILITIES & COMBAT INTERPLAY:
- Devastating Tactical Synergy: Rin provides high-output ranged bombardment (Gandr, jewel detonations, bounded fields), while Shiki functions as the frontline breach executioner, slicing through enemy barriers and spiritual defenses.

6. DEVELOPMENT OVER REPEATED ENCOUNTERS:
- Evolves into a sharp, highly effective partnership. Rin realizes Shiki's eyes can solve occult deadlocks that baffle formal academia; Shiki recognizes that Rin's sharp intellect and quick reflexes make her a genuinely dependable ally.

7. WHAT MUST NOT BE ASSUMED:
- Do NOT assume Rin can command or hire Shiki as an operative without Shiki's personal consent.
- Do NOT assume Shiki cares about the Tohsaka lineage or Association rules.
</Pairing_Shiki_and_Rin_Tohsaka>"""
    },

    # Entry 3: Pairing_Shiki_and_Archer_EMIYA
    {
        "uid": 3,
        "name": "Pairing_Shiki_and_Archer_EMIYA",
        "comment": "Pairing_Shiki_and_Archer_EMIYA",
        "order": 133,
        "key": [
            "Ryougi Shiki",
            "Shiki Ryougi",
            "Shiki",
            "Archer",
            "EMIYA",
            "Counter Guardian",
            "Heroic Spirit Emiya",
            "ชิกิกับอาร์เชอร์",
            "อาร์เชอร์กับชิกิ",
            "เอมิยะกับชิกิ"
        ],
        "keysecondary": [
            "Alaya",
            "Counter Force",
            "cynicism",
            "bow",
            "projection",
            "lines of death",
            "ผู้พิทักษ์แห่งการยับยั้ง",
            "มือสังหารสองคน",
            "นักธนูกับมีด"
        ],
        "content": """<Pairing_Shiki_and_Archer_EMIYA>
[CROSSOVER DYNAMICS: RYOUGI SHIKI & COUNTER GUARDIAN EMIYA]

1. CONTRASTING VALUES & WORLDVIEWS:
- Shiki is a living mortal connected to the Root who chose to restrain her murderous instincts to preserve her human soul.
- Archer is a cynical Heroic Spirit and Counter Guardian who traded his afterlife to become an eternal executioner for the Counter Force (Alaya), trapped in a cycle of endless slaughter.

2. INITIAL IMPRESSIONS:
- What Shiki Notices: Shiki immediately senses that Archer is not an ordinary human or even a standard spirit; she perceives the heavy, metallic stench of the Counter Force on him. She sees a ghost who has killed millions and hates himself for it.
- What Archer Notices: Archer recognizes Shiki's connection to the Root and her status as a living, natural corrective mechanism of the World. He treats her with immense wariness and professional distance.

3. WEARY CYNICISM & MUTUAL SUBTEXT:
- Dialogue Style: Razor-sharp, dry, and laconic. Neither character wastes words on flattery or heroics. They exchange biting, cynical observations about Shirou's stupidity, Rin's temper, or the absurdity of human desires.
- Shared Bleakness: Both understand what it means to be stained by blood. Archer never lectures Shiki; Shiki never pities Archer.

4. NATURAL CONVERSATIONAL TOPICS:
- The Weight of Alaya: The cold, utilitarian nature of the Counter Force and the horror of becoming a cleaner for humanity's mistakes.
- Weapon Mechanics: Archer examining the structural flaws in Shiki's knife; Shiki noting that all of Archer's projected blades possess visible lines of death.
- Quiet Tea/Coffee Moments: Sitting in silence while others argue, sharing a mutual appreciation for quiet rooms.

5. COMBAT INTERACTION & ENGAGEMENT RULES:
- Archer's Protocol: Archer is an experienced veteran who will NEVER engage Shiki in close-quarters melee if it can be avoided. He knows Kanshou and Bakuya will be sliced like chalk. In any conflict, Archer will maintain hundreds of meters of distance on rooftops, engaging purely as a sniper with projected arrows (Caladbolg, Hrunting).

6. DEVELOPMENT OVER REPEATED ENCOUNTERS:
- A quiet, unspoken understanding between two killers. Archer respects Shiki's discipline in keeping her promise to Mikiya; Shiki respects Archer's lethal competence.

7. WHAT MUST NOT BE ASSUMED:
- Do NOT assume Archer attacks Shiki without orders from the Counter Force or his Master.
- Do NOT assume Shiki can easily close the distance against Archer across open ground.
</Pairing_Shiki_and_Archer_EMIYA>"""
    },

    # Entry 4: Pairing_Touko_and_Rin_Tohsaka
    {
        "uid": 4,
        "name": "Pairing_Touko_and_Rin_Tohsaka",
        "comment": "Pairing_Touko_and_Rin_Tohsaka",
        "order": 134,
        "key": [
            "Aozaki Touko",
            "Touko Aozaki",
            "Touko",
            "Rin Tohsaka",
            "Tosaka Rin",
            "Tohsaka",
            "Rin",
            "โทโกะกับริน",
            "รินกับโทโกะ",
            "อาจารย์โทโกะกับริน"
        ],
        "keysecondary": [
            "Clock Tower",
            "mentorship",
            "Heaven's Feel",
            "puppet",
            "Shirou body",
            "Department of Policies",
            "การสั่งสอนริน",
            "หุ่นเชิดชิโร่",
            "ลอนดอน"
        ],
        "content": """<Pairing_Touko_and_Rin_Tohsaka>
[CROSSOVER DYNAMICS: AOZAKI TOUKO & RIN TOHSAKA]

1. CONTRASTING VALUES & WORLDVIEWS:
- Touko is an autonomous, worldly Grand-rank magus who discarded the petty dogmas of the Clock Tower and survived a Sealing Designation through sheer genius and cynicism.
- Rin is an ambitious, young heir to the Tohsaka family, determined to uphold her late father's legacy and excel within the orthodox Clock Tower system.

2. INITIAL IMPRESSIONS:
- What Touko Notices: Touko sees right through Rin's aristocratic composure. She recognizes Rin as a brilliantly talented, fundamentally decent young woman who is desperately trying to suppress her natural kindness to be a "proper, ruthless magus."
- What Rin Notices: Rin is deeply intimidated yet professionally fascinated. She knows Touko is a living legend in the Department of Puppetry and a dangerous fugitive who slaughtered Association Enforcers.

3. MENTORSHIP & SARDONIC TEASING:
- The Older Sister Dynamic: Touko delights in teasing Rin about her financial troubles, her romantic headaches with Shirou, and her stiff formal posture. She treats Rin like a talented younger student who takes textbooks far too seriously.
- Practical Magus Lessons: Touko offers harsh, realistic advice about the Clock Tower: "If you go to London expecting a scholarly paradise, Tohsaka, they'll carve your crest out before your second term. Trust no one who smiles politely in the Department of Policies."

4. CANON HEAVEN'S FEEL LINK:
- In Fate/stay night's Heaven's Feel True End, Rin travels to London and later encounters Touko, purchasing the masterwork puppet body that saves Shirou's soul. In roleplay, this establishes a canon baseline: Rin knows Touko's puppets are miracles that bypass soul rejection.

5. NATURAL CONVERSATIONAL TOPICS:
- Jewel Magecraft & Mineralogy: Touko critiquing Rin's gem expenditures and suggesting more efficient thaumaturgical conductors.
- Survival in the Clock Tower: Dealing with Lord El-Melloi II, the Barthomeloi faction, and avoiding Sealing Designations.
- Smoking & Espresso: Touko blowing smoke while Rin complains about secondhand tobacco ruining her coat.

6. DEVELOPMENT OVER REPEATED ENCOUNTERS:
- Evolves into an invaluable, informal mentorship. Rin gains a cynical, worldly advisor outside the rigid family hierarchy; Touko finds quiet amusement in helping a competent young magus avoid the traps that nearly killed her in London.

7. WHAT MUST NOT BE ASSUMED:
- Do NOT assume Touko gives Rin free magical items or assistance without compensation or mutual benefit.
- Do NOT assume Rin forgets the danger of Touko taking off her glasses.
</Pairing_Touko_and_Rin_Tohsaka>"""
    },

    # Entry 5: Pairing_Touko_and_Fuyuki_Magi_Kirei_Zouken
    {
        "uid": 5,
        "name": "Pairing_Touko_and_Fuyuki_Magi_Kirei_Zouken",
        "comment": "Pairing_Touko_and_Fuyuki_Magi_Kirei_Zouken",
        "order": 135,
        "key": [
            "Aozaki Touko",
            "Touko Aozaki",
            "Touko",
            "Kotomine Kirei",
            "Kirei",
            "Matou Zouken",
            "Zouken",
            "โทโกะกับคิเรย์",
            "โทโกะกับโซเคน",
            "โทโกะในฟุยุกิ"
        ],
        "keysecondary": [
            "worms",
            "Church",
            "Executor",
            "corruption",
            "Angra Mainyu",
            "container",
            "หนอนเวท",
            "นักบวชคิเรย์",
            "การดูถูกโซเคน"
        ],
        "content": """<Pairing_Touko_and_Fuyuki_Magi_Kirei_Zouken>
[CROSSOVER DYNAMICS: AOZAKI TOUKO & FUYUKI'S VETERAN OCCULTISTS]

1. TOUKO & MATOU ZOUKEN (THE CONTRAST OF CONTAINERS):
- Worldview Clash: Zouken spent 500 years decaying inside rotting crest worms in a desperate, grotesque attempt to avoid soul death. Touko achieved effortless functional immortality through identical biological puppet bodies.
- Touko's Reaction: Absolute professional disdain. Touko views Zouken not as a terrifying elder, but as a pathetic thaumaturgical failure who disgraced the art of container craft: "Living for centuries just to become a nest of filthy maggots? What a vulgar, second-rate excuse for a magus."
- Zouken's Reaction: Deep envy and avarice. Zouken covets Touko's masterwork puppet techniques to escape his decaying worm flesh.

2. TOUKO & KOTOMINE KIREI (CHILLING INTELLECTUAL WARINESS):
- Worldview Clash: Kirei is a hollow, sadistic Executor of the Holy Church seeking to understand his twisted existence through the birth of Angra Mainyu. Touko is an autonomous magus who rejected religious and thaumaturgical dogmas alike.
- Mutual Assessment: Kirei recognizes Touko as a ruthless, lethal magus who cannot be emotionally manipulated with simple guilt or moral traps. Touko identifies Kirei's sociopathy beneath his priestly robes, keeping her distance and hand near her coat.
- Conversation: Cold, razor-sharp dialogue masked by polite theological and thaumaturgical terminology. Both understand that any physical clash would be an instantaneous, lethal duel.

3. TOUKO & MEDEA (AGE OF GODS VS. MODERN GRAND):
- Dynamic: Medea looks down on modern magi as crude children; Touko acknowledges Medea's superior Divine Words, but views Medea's emotional obsession with Kuzuki as a fatal weakness.

4. WHAT MUST NOT BE ASSUMED:
- Touko does NOT participate in the Holy Grail War as a Master. She views the Fuyuki ritual as an archaic, corrupt death trap designed by dead men.
- Kirei and Zouken cannot easily ambush Touko due to her defensive Runic wards and duplicate immortality.
</Pairing_Touko_and_Fuyuki_Magi_Kirei_Zouken>"""
    },

    # Entry 6: Pairing_Touko_and_Bazett_Enforcer_Dynamics
    {
        "uid": 6,
        "name": "Pairing_Touko_and_Bazett_Enforcer_Dynamics",
        "comment": "Pairing_Touko_and_Bazett_Enforcer_Dynamics",
        "order": 136,
        "key": [
            "Aozaki Touko",
            "Touko Aozaki",
            "Touko",
            "Bazett",
            "Bazett Fraga McRemitz",
            "Fraga",
            "โทโกะกับบาเซ็ตต์",
            "บาเซ็ตต์กับโทโกะ",
            "โทโกะกับเอนฟอร์เซอร์"
        ],
        "keysecondary": [
            "Enforcer",
            "Sealing Designation",
            "Runes",
            "Fragarach",
            "boxing",
            "neutrality",
            "รูนปะทะรูน",
            "การปิดตายเขตแดน",
            "ฟราการัค"
        ],
        "content": """<Pairing_Touko_and_Bazett_Enforcer_Dynamics>
[CROSSOVER DYNAMICS: AOZAKI TOUKO & BAZETT FRAGA MCREMITZ]

1. CONTRASTING VALUES & ROLES:
- Touko is a Clock Tower *Grand* puppeteer living under an active Sealing Designation (封印指定).
- Bazett is the premier combat Enforcer (執行者) of the Clock Tower, officially tasked with hunting down, incapacitating, and capturing Sealing Designation targets.

2. INITIAL TENSION & PROFESSIONAL PROTOCOL:
- The Threat of Arrest: When they cross paths, tension is immediate. Bazett's duty demands she evaluate Touko's status; Touko's survival demands she be prepared to execute Bazett instantly if an arrest is attempted.
- The Pragmatic Neutrality: Bazett is not an unthinking butcher; she only executes active contracts issued by the Department of Policies. If Bazett is in Japan on a separate assignment (such as the Holy Grail War), Touko will calmly point out that taking a contract on a Grand magus without Association backup is a quick way to end up in a coffin.

3. SHARED RUNIC ARCANUM:
- Both Touko and Bazett are masters of ancient Runic Magecraft, but their applications are completely opposite:
  * Bazett uses Runes to reinforce her physical flesh and boxing gloves for close-quarters superhuman martial arts.
  * Touko uses Primeval Nordic Runes to rewrite environmental geometry, trigger instantaneous infernos, and construct defensive wards.
- This creates deep, begrudging technical respect. They can critique and analyze each other's runic craftsmanship with professional precision.

4. SOCIAL CONTRAST:
- Touko is worldly, cynical, and manipulative; Bazett is earnest, socially clumsy, and easily flustered outside of combat. Touko quickly realizes Bazett is surprisingly naive in civilian matters and enjoys teasing her awkwardness over tea.

5. DEVELOPMENT OVER REPEATED ENCOUNTERS:
- Transitions from tense, hand-on-weapon standoff into a cautious truce. They can share intelligence on dangerous third-party rogue magi (like Araya or Zouken) while maintaining professional boundaries.

6. WHAT MUST NOT BE ASSUMED:
- Do NOT assume Bazett blindly attacks Touko without an active mission contract.
- Do NOT assume Touko lets her guard down around an Enforcer carrying Fragarach.
</Pairing_Touko_and_Bazett_Enforcer_Dynamics>"""
    },

    # Entry 7: Pairing_Mikiya_and_Fate_Cast_Shirou_Caren
    {
        "uid": 7,
        "name": "Pairing_Mikiya_and_Fate_Cast_Shirou_Caren",
        "comment": "Pairing_Mikiya_and_Fate_Cast_Shirou_Caren",
        "order": 137,
        "key": [
            "Kokutou Mikiya",
            "Mikiya Kokutou",
            "Mikiya",
            "Emiya Shirou",
            "Caren Hortensia",
            "Bazett",
            "มิกิยะกับชิโร่",
            "มิกิยะกับคาเรน",
            "มิกิยะกับบาเซ็ตต์"
        ],
        "keysecondary": [
            "kindness",
            "cooking",
            "caregiver",
            "ordinary human",
            "stabilizer",
            "hospitality",
            "ความใจดีของมิกิยะ",
            "การทำอาหาร",
            "ความสงบสุข"
        ],
        "content": """<Pairing_Mikiya_and_Fate_Cast_Shirou_Caren>
[CROSSOVER DYNAMICS: KOKUTOU MIKIYA & THE FATE CAST]

1. MIKIYA & EMIYA SHIROU (THE BROTHERHOOD OF CAREGIVERS):
- Worldview Dynamics: Mikiya is the grounded, ordinary human who values life; Shirou is the traumatized teenager ready to die for ideals. Mikiya acts like an older brother who sees through Shirou's martyr complex: "Emiya-kun, saving people is admirable, but if you don't care whether you survive, the people who love you will carry that grief forever."
- Natural Interactions: Exchanging home cooking recipes, grocery shopping for stubborn girls (Shiki and Saber/Rin), discussing household chores, and providing quiet emotional sanctuary amidst supernatural danger.
- Shirou's Reaction: Shirou feels completely disarmed by Mikiya's total lack of ambition, greed, or malice. Mikiya becomes one of the very few adults Shirou can confide in without putting up a defensive guard.

2. MIKIYA & CAREN HORTENSIA (THE UNFLAPPABLE KINDNESS):
- The Psychological Clash: Caren's nature is cynical, masochistic, and sharp-tongued; she exposes human weakness and mocks self-righteousness. When she encounters Mikiya, she expects him to have hidden perversions or hypocrisies.
- Mikiya's Disarming Reaction: Caren's barbs fail completely against Mikiya. When Caren tries to needle him about his devotion to a killer, Mikiya simply asks if she is cold, wraps a warm scarf around her shoulders, and brings her hot soup. Caren is left completely disoriented and frustrated by a human being whose kindness contains zero selfish motives.

3. MIKIYA & BAZETT:
- Bazett is socially insecure and isolated outside her enforcer duties. Mikiya treats her with authentic, polite human respect, praising her diligence and offering warm coffee. Bazett finds herself flustered by his gentlemanly courtesy.

4. ROLEPLAY SCENE USAGE:
- Mikiya functions as the universal emotional stabilizer. In any crossover gathering, Mikiya prevents magi and Servants from murdering each other through the sheer, disarming power of ordinary hospitality.

5. WHAT MUST NOT BE ASSUMED:
- Do NOT give Mikiya combat skills or make him participate in Servant skirmishes.
- Do NOT assume Mikiya condones the Holy Grail War; he views the ritual with quiet, deep sorrow for the human lives wasted.
</Pairing_Mikiya_and_Fate_Cast_Shirou_Caren>"""
    },

    # Entry 8: Crossover_Physics_MEoDP_vs_Servant_Spiritual_Cores (NEW)
    {
        "uid": 8,
        "name": "Crossover_Physics_MEoDP_vs_Servant_Spiritual_Cores",
        "comment": "Crossover_Physics_MEoDP_vs_Servant_Spiritual_Cores",
        "order": 138,
        "key": [
            "MEoDP vs Servants",
            "Mystic Eyes vs Servant",
            "Spiritual Core death",
            "Saint Graph death",
            "Shiki vs Servants",
            "เนตรมรณะกับเซอร์แวนท์",
            "ชิกิปะทะเซอร์แวนท์",
            "การตัดแก่นวิญญาณ",
            "เส้นตายของเซอร์แวนท์",
            "เนตรมองเห็นความตายกับวิญญาณวีรชน"
        ],
        "keysecondary": [
            "Spiritual Core",
            "Saint Graph",
            "Ether",
            "Prana",
            "dissipation",
            "supersonic",
            "graze",
            "fatal",
            "แก่นวิญญาณ",
            "กายทิพย์",
            "ความเร็วเหนือเสียง",
            "การสลายตัว"
        ],
        "content": """<Crossover_Physics_MEoDP_vs_Servant_Spiritual_Cores>
[CROSSOVER COMBAT PHYSICS: MEoDP VS. SERVANT SPIRITUAL CORES & SAINT GRAPHS]

1. METAPHYSICAL NATURE OF SERVANTS IN RELATION TO DEATH:
- Servants are not flesh-and-blood biological organisms. They are spiritual familiars constructed from condensed magical energy (Ether / กายทิพย์) summoned from the Throne of Heroes. Their material existence in the physical World is anchored by two pillars:
  * The Master's Prana Link (the fuel line).
  * The Saint Graph (霊基 / Spiritual Foundation) housing the Spiritual Core (霊核 / Reikaku).
- Do Servants Have Mortality? YES. In Nasuverse ontology, anything manifested within the World that possesses a beginning and an end is subject to cessation. Because a Servant is a temporary phenomenon summoned into the finite present, Ryougi Shiki perceives the Lines of Death (死の線) webbed across their etheric form and a dense, pulsing Point of Death (死の点) situated over their Spiritual Core (typically the chest/heart or forehead).

2. THE MECHANICS OF CUTTING SPIRITUAL BODIES:
- Bypassing Physical Toughness: Shiki's Mystic Eyes of Death Perception do not calculate kinetic blunt force, piercing trauma, or thermal yield. They enforce the ontological non-existence of the targeted concept.
- Slashing a Line of Death: When Shiki's knife traces a line of death across a Servant's arm or torso, she is NOT slicing ghost meat; she is severing the causal link that binds that section of the Saint Graph together. The sliced limb or torso section dematerializes instantaneously into evaporating prana. Armor cannot block it, and conventional healing spells cannot regenerate a limb whose death has been actualized.
- Piercing the Point of Death: If Shiki drives her blade into the Point of Death on a Servant's Spiritual Core, the entire Saint Graph shatters instantly. The Servant does not bleed out or enter a death throe; their existence collapses immediately into dispersing golden motes of prana. Command Spells cannot intervene in time to reverse a conceptual death.

3. THE HARSH TACTICAL BOTTLENECK: STATISTICAL DISPARITY:
- Absolute Lethality vs. Human Frailty: While Shiki holds absolute offensive lethality, her physical vessel is a mortal human body (augmented only by Ryougi martial conditioning and Touko's prosthetic arm).
- Superhuman Parameters: A standard Servant possesses B-rank to A-rank Agility, moving at supersonic velocities, reacting in microseconds, and delivering strikes capable of fracturing bedrock. In an open, head-on sprint, Shiki cannot match a Servant's running speed or raw kinetic violence.
- Shiki's Combat Doctrine Against Servants:
  * Never engage in sustained melee parries against high-parameter Servants (their kinetic force will break her bones through her blade).
  * Use urban geometry, stealth, darkness, and bounded-field concealment to ambush.
  * Exploit Servant Arrogance: Servants frequently mistake Shiki for a fragile modern human girl holding a utility knife. When they deliver a careless thrust or leave an opening, Shiki evades by millimeters and executes a single, fatal intercept along their lines of death.
</Crossover_Physics_MEoDP_vs_Servant_Spiritual_Cores>"""
    },

    # Entry 9: Crossover_Physics_MEoDP_vs_God_Hand_Heracles (NEW)
    {
        "uid": 9,
        "name": "Crossover_Physics_MEoDP_vs_God_Hand_Heracles",
        "comment": "Crossover_Physics_MEoDP_vs_God_Hand_Heracles",
        "order": 139,
        "key": [
            "MEoDP vs God Hand",
            "Shiki vs Heracles",
            "MEoDP vs Berserker",
            "Twelve Labors death",
            "เนตรมรณะปะทะก็อดแฮนด์",
            "ชิกิปะทะเฮอร์คิวลีส",
            "เนตรมรณะกับเบอร์เซิร์กเกอร์",
            "การตัดสิบสองชีวิต",
            "ก็อดแฮนด์ปะทะจุดตาย"
        ],
        "keysecondary": [
            "God Hand",
            "Heracles",
            "Twelve Labors",
            "resurrection",
            "Point of Death",
            "Line of Death",
            "nullification",
            "ก็อดแฮนด์",
            "เฮอร์คิวลีส",
            "การคืนชีพ",
            "จุดตาย",
            "ตัดการมีอยู่"
        ],
        "content": """<Crossover_Physics_MEoDP_vs_God_Hand_Heracles>
[CROSSOVER COMBAT PHYSICS: MEoDP VS. GOD HAND (TWELVE LABORS)]

1. THE CANONICAL ARCHITECTURE OF GOD HAND (十二の試練):
- Berserker Heracles' Noble Phantasm, God Hand, operates on two distinct defensive principles:
  1. Attack Nullification: Completely nullifies and invalidates any physical or magical attack ranked below A-rank.
  2. Conceptual Resurrection: Grants eleven reserve lives (twelve lives total). Upon fatal trauma, Heracles regenerates, developing conceptual resistance/immunity against the specific attack that killed him.

2. HOW MEoDP INTERACTS WITH GOD HAND'S DAMAGE NULLIFICATION:
- The Non-Ranked Nature of MEoDP: The Mystic Eyes of Death Perception do NOT deal damage, nor do they possess a numerical or letter grade (they are not B-rank, A-rank, or Noble Phantasm energy). They are the realization of a universal metaphysical truth directly linked to the Root (`「　」`).
- Slicing Lines Bypasses Armor: When Shiki cuts a Line of Death, no kinetic impact or magical projectile is fired against Heracles' hardened skin. The World itself enacts the cessation of that body part. Therefore, God Hand's rule ("nullifying attacks below A-rank") FAILS ENTIRELY against MEoDP. Shiki's knife slices through Heracles' limbs, tendons, and flesh as easily as paper.

3. SLICING A LINE OF DEATH (死の線) VS. PIERCING THE POINT OF DEATH (死の点):
- Slicing a Line of Death (Single-Life Depletion): If Shiki severs a Line of Death through Heracles' neck or heart, she inflicts absolute death on his physical container. This successfully takes ONE of his twelve lives. God Hand's resurrection triggers, restoring Heracles to life. Because MEoDP is not an elemental spell or a specific weapon type, God Hand cannot "become immune to the concept of death"—Shiki will still see lines of death on his resurrected body.
- Piercing the Point of Death (Complete Conceptual Annihilation): If Shiki drives her blade directly into a Point of Death (死の点) on Heracles' torso or forehead, the interaction reaches absolute finality. Piercing the Point of Death does not inflict mortal injury; it extinguishes the conceptual existence of the entity "Heracles" from the World. Because God Hand's stock of eleven reserve lives relies upon the continued existence of Heracles' foundational Saint Graph, extinguishing the root concept of his being DESTROYS ALL TWELVE LIVES SIMULTANEOUSLY. Heracles dies permanently, with zero resurrection.

4. THE PRACTICAL COMBAT NIGHTMARE:
- While Shiki holds the theoretical one-hit-kill key against Heracles, attempting to execute it in open 1v1 combat is near-suicidal:
  * Heracles stands over 250 cm tall, moves at supersonic speeds, and swings a massive rock axe-sword.
  * The mere atmospheric shockwave created by Heracles' swings can crush human ribs and rupture internal organs from meters away.
  * Shiki has zero margin for error. A single glancing blow from Heracles will obliterate her body.
  * Realistic Victory Condition: Shiki can only land a strike on Heracles' Point of Death if he is completely immobilized by external forces (e.g., Gilgamesh's Enkidu chains, Touko's high-tier Runic spatial locks, or Saber drawing his full attention in a lethal clash).
</Crossover_Physics_MEoDP_vs_God_Hand_Heracles>"""
    },

    # Entry 10: Crossover_Physics_MEoDP_vs_Gate_of_Babylon_Gilgamesh (NEW)
    {
        "uid": 10,
        "name": "Crossover_Physics_MEoDP_vs_Gate_of_Babylon_Gilgamesh",
        "comment": "Crossover_Physics_MEoDP_vs_Gate_of_Babylon_Gilgamesh",
        "order": 140,
        "key": [
            "MEoDP vs Gate of Babylon",
            "Shiki vs Gilgamesh",
            "Shiki vs King of Heroes",
            "cutting Noble Phantasms",
            "เนตรมรณะปะทะเกทออฟบาบิโลน",
            "ชิกิปะทะกิลกาเมช",
            "การฟันสมบัติวีรชน",
            "ชิกิกับราชาแห่งวีรชน"
        ],
        "keysecondary": [
            "Gate of Babylon",
            "Gilgamesh",
            "Bizen Kanesada",
            "range",
            "supersonic barrage",
            "conceptual cutting",
            "เกทออฟบาบิโลน",
            "กิลกาเมช",
            "ดาบคาเนซาดะ",
            "ระยะห่าง",
            "ห่ากระสุนดาบ"
        ],
        "content": """<Crossover_Physics_MEoDP_vs_Gate_of_Babylon_Gilgamesh>
[CROSSOVER COMBAT PHYSICS: MEoDP VS. GATE OF BABYLON (GILGAMESH)]

1. THE SUPREME RANGE ADVANTAGE OF THE KING OF HEROES:
- Gilgamesh represents the most tactically disadvantageous matchup for Ryougi Shiki in the entire Nasuverse.
- The Range Dilemma: Gilgamesh never fights in close quarters unless forced. He hovers on golden platforms (Vimana) or perches on distant rooftops hundreds of meters away, opening dozens to hundreds of golden ripples and launching original Noble Phantasms as supersonic artillery.

2. CAN SHIKI CUT INCOMING NOBLE PHANTASMS? YES:
- Inanimate Objects Possess Death: In *Kara no Kyoukai*, Shiki demonstrated the ability to cut through telekinetic axes, bounded fields, and physical matter. Every weapon fired from the Gate of Babylon was forged by mortal or divine hands and possesses an origin and an inevitable end.
- Slicing Flying Weapons: Shiki clearly perceives the Lines of Death etched along incoming flying swords, spears, and axes. If she intercepts a flying Noble Phantasm with her knife or katana along its line of death, the weapon's concept instantly dies. It does not deflect; it crumbles into inert, rusted fragments or dissipates into harmless dust mid-air.

3. THE HUMAN REACTION BOTTLENECK:
- The Math of the Barrage: While Shiki's Mystic Eyes can see the lines of death on twenty incoming Noble Phantasms simultaneously, her human arms cannot physically swing twenty times in a microsecond.
- Against a wide-spread saturation barrage from the Gate of Babylon, Shiki cannot slice every projectile. In an open field (like Fuyuki Bridge or an open plain), she would be overwhelmed by sheer numbers and impaled.

4. THE BIZEN KANESADA KATANA FACTOR:
- Expanding the Cutting Territory: When Shiki draws the ancestral Bizen Kanesada katana, her combat efficacy transforms. With the katana, her defensive sphere expands dramatically. She enters a state of effortless martial flow, deflecting projectiles by grazing their lines of death with the blade's flat or tip, creating safe blind spots in the barrage.
- Environmental Navigation: In a dense urban environment (narrow alleys, ruined buildings, or indoor hallways), Shiki can use concrete walls as temporary visual shields, cutting through structural pillars to drop rubble and block Gilgamesh's firing vectors.

5. GILGAMESH'S FATAL FLAW: MELEE ENGAGEMENT:
- Blinding Arrogance: Gilgamesh views modern humans as beneath his notice, labeling them "mongrels" and refusing to wear his golden armor or draw Ea against them.
- The Close-Quarters Trap: If Shiki closes distance through stealth, optical illusions, or an ally's distraction:
  * Gilgamesh has zero conceptual protection against MEoDP once within arm's reach.
  * Gilgamesh's close-quarters swordsmanship is crude and arrogant compared to Shiki's surgical martial mastery.
  * A single, clean incision from Shiki across Gilgamesh's torso severs his Saint Graph, killing the King of Heroes instantly before he can comprehend what struck him.
</Crossover_Physics_MEoDP_vs_Gate_of_Babylon_Gilgamesh>"""
    },

    # Entry 11: Crossover_Physics_Magic_Resistance_and_Conceptual_Noble_Phantasms (NEW)
    {
        "uid": 11,
        "name": "Crossover_Physics_Magic_Resistance_and_Conceptual_Noble_Phantasms",
        "comment": "Crossover_Physics_Magic_Resistance_and_Conceptual_Noble_Phantasms",
        "order": 141,
        "key": [
            "Magic Resistance vs MEoDP",
            "Avalon vs MEoDP",
            "Gae Bolg vs Shiki",
            "Conceptual Weapons Nasuverse",
            "ความต้านทานเวทปะทะเนตรมรณะ",
            "อวาลอนปะทะเนตรมรณะ",
            "เกโบล์กปะทะชิกิ",
            "สมบัติวีรชนเชิงคอนเซ็ปต์"
        ],
        "keysecondary": [
            "Magic Resistance",
            "Avalon",
            "Gae Bolg",
            "Rule Breaker",
            "reversal of causality",
            "absolute defense",
            "ความต้านทานเวท",
            "อวาลอน",
            "เกโบล์ก",
            "การกลับตาลปัตรแห่งเหตุและผล"
        ],
        "content": """<Crossover_Physics_Magic_Resistance_and_Conceptual_Noble_Phantasms>
[CROSSOVER COMBAT PHYSICS: MAGIC RESISTANCE & CONCEPTUAL NOBLE PHANTASMS]

1. WHY MAGIC RESISTANCE (対魔力) PROVIDES ZERO DEFENSE AGAINST MEoDP:
- The Nature of Magic Resistance: Magic Resistance is an innate Class skill that passively repels and dissipates thaumaturgical spells, curses, and foreign prana. (For instance, Saber's A-rank Magic Resistance completely nullifies High Thaumaturgy from modern magi and Medea's Divine Words).
- Why MEoDP Ignores Magic Resistance:
  * The Mystic Eyes of Death Perception are NOT Magecraft.
  * They do not project prana, chant incantations, or emit external magical energy toward the target.
  * They are an open circuit directly touching the Root (`「　」`), allowing the user to perceive the inherent mortality already woven into the World.
  * When Shiki's blade traces a line of death, no magical force clashes against the target's resistance; the World simply enforces the cessation of that part.
  * Conclusion: Whether a Servant has E-rank, A-rank, or EX-rank Magic Resistance, it provides ZERO protection against MEoDP.

2. THE ABSOLUTE DEFENSE: AVALON (THE EVERDISTANT UTOPIA):
- The Fairy Realm Isolation: When Artoria deploys the true release of Avalon (Excalibur's holy scabbard), she is conceptually transported into the realm of the Fairies.
- Can MEoDP Cut Avalon? NO.
  * Avalon places Artoria in a completely isolated metaphysical dimension, shielded from all physical interference, the five True Magics, and the physical causality of the World.
  * Because death is a law of the mortal World, the concept of death cannot reach the domain of Avalon.
  * While Avalon is active, Shiki CANNOT see Lines of Death on Artoria, because Artoria does not exist within the physical universe's mortal framework during that state.

3. REVERSAL OF CAUSALITY: GÁE BOLG (CÚ CHULAINN):
- The Causal Dilemma: Cú Chulainn's thrust reverses causality—the effect ("heart is pierced") is established before the cause ("spear is thrust").
- Can Shiki Avoid Gáe Bolg?
  * Shiki can clearly see Lines of Death on Gáe Bolg itself. If she strikes the spear before Cú Chulainn speaks its True Name and releases the curse, she can destroy the spear.
  * However, once the True Name is spoken, causality is inverted. Because Shiki is an ordinary mortal without divine Luck (which Saber required to survive with a minor wound), the spear's curse will mathematically curve around her blade and pierce her heart.
  * Tactical Solution: Shiki must never let Lancer assume the thrust stance or speak the True Name; she must strike aggressively to force him into defensive retreats.

4. CUTTING BOUNDED FIELDS & CONTRACTS (RULE BREAKER PARALLELS):
- Conceptual Slicing: Shiki can perceive the Lines of Death on active Bounded Fields, Master-Servant mana tethers, and magical contracts.
- Slicing through the air where a Master's mana connection runs will sever the tether, starving the Servant of prana just like Medea's Rule Breaker. Slicing the focal anchor of Blood Fort Andromeda collapses Rider's barrier instantly.
</Crossover_Physics_Magic_Resistance_and_Conceptual_Noble_Phantasms>"""
    }
]

lorebook = {
    "name": "Kara_no_Kyoukai_12_Crossover_Dynamics",
    "description": "Exhaustive crossover dynamics and combat physics module bridging Kara no Kyoukai and Fate/stay night for SillyTavern roleplay. Features in-depth character pairings (Shiki & Shirou, Shiki & Saber, Shiki & Rin, Shiki & Archer, Touko & Rin, Touko & Fuyuki Magi, Touko & Bazett, Mikiya & Fate Cast) and rigorous combat physics: MEoDP vs. Servant Spiritual Cores, MEoDP vs. God Hand 12 lives, MEoDP vs. Gate of Babylon, and Magic Resistance vs. Conceptual Noble Phantasms (Avalon, Gae Bolg). Equipped with complete Thai trigger keywords without token limits.",
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

