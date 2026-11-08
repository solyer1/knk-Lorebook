# Kara no Kyoukai: Chapter Knowledge & Fog-of-War Architecture Research Notes

## 1. Executive Summary & Core Objective

The purpose of `15_Chapter_Knowledge_Fog_of_War.json` is to establish strict, canon-accurate temporal information boundaries for SillyTavern roleplay across the seven main chapters of *Kara no Kyoukai* (The Garden of Sinners). 

Because the series was famously published and adapted non-chronologically (e.g., Film 1 *Overlooking View* occurs in September 1998, whereas Film 2 *A Study in Murder Part 1* occurs in 1995, and Film 4 *The Hollow Shrine* occurs in June 1998), Large Language Models routinely suffer from **anachronistic information leakage**—characters frequently know future plot twists, reference abilities they have not yet awakened, or suspect antagonists whose existence has not yet been hinted at.

This module provides a rigid, granular "Fog-of-War" for each canonical chapter, documenting:
1. Exact Canonical Chronology vs. Film Release Order.
2. Knowledge Matrices (What characters KNOW, SUSPECT, CONCEAL, and HAVE NOT YET DISCOVERED).
3. Sources of Information and Investigation Paths.
4. Premature Spoilers to Actively Suppress.
5. Custom Roleplay Overrides for Divergent Timelines.

---

## 2. Chronological Story Mapping vs. Film Release Order

| Chronological Order | Title (Japanese / Subtitle) | Release Order | Canon Time Period | Exact Dates & Notes |
|---|---|---|---|---|
| **Chapter 1** | *A Study in Murder - Part 1* (殺人考察（前） / `...and nothing heart`) | **Film 2** / Novel Ch. 2 | April 1995 – February 1996 | April 1995 (High school entrance), September 1995 (Killings begin), February 1996 (Traffic accident). Specific day in Feb is inferred. |
| **Chapter 2** | *The Hollow Shrine* (伽藍の洞 / `garan-no-dou`) | **Film 4** / Novel Ch. 4 | June 1998 – August 1998 | Coma ends June 1998; Touko arrives July 1998; Corpse attack late July/August 1998. |
| **Chapter 3** | *Remaining Sense of Pain* (痛覚残留 / `ever cry, never life`) | **Film 3** / Novel Ch. 3 | Late July 1998 | July 20–31, 1998 (summer heatwave / torrential rain). Occurs right after Shiki's hospital release. |
| **Chapter 4** | *Overlooking View* (俯瞰風景 / `Thanatos`) | **Film 1** / Novel Ch. 1 | August – September 1998 | Suicides across August; climax in mid-September 1998. Occurs AFTER Ch. 4 & 3. |
| **Chapter 5** | *Paradox Spiral* (矛盾螺旋 / `Paradox Paradigm`) | **Film 5** / Novel Ch. 5 | October – November 1998 | Late October (Tomoe rescue); early-to-mid November 1998 (Ogawa Mansion infiltration & Araya duel). |
| **Chapter 6** | *Oblivion Recording* (忘却録音 / `Fairy Tale`) | **Film 6** / Novel Ch. 6 | January 1999 | January 10–25, 1999 (winter semester at Reien Academy). Araya is already dead. |
| **Chapter 7** | *A Study in Murder - Part 2* (殺人考察（後） / `...not nothing heart`) | **Film 7** / Novel Ch. 7 | Mid-to-Late February 1999 | February 1999. Final confrontation with Shirazumi Lio; resolution of 1995 mystery. |
| **Epilogue** | *Kara no Kyoukai* (空の境界 / `「　」`) | Epilogue Film | March 1999 | March 1999 snowy night on bamboo grove path. |
| **Post-Story** | *Future Gospel* (未来福音 / `Mirai Fukuin`) | Extra Film / Side Story | 1998 (Side) / 2008–2010 | Adult Mikiya, Shiki, and Mana Ryougi. |

---

## 3. Detailed Fog-of-War Matrices per Chapter

### Chapter 1 (Chronological): *A Study in Murder - Part 1* (1995–1996)
- **Timeframe:** April 1995 – February 1996
- **Release:** Film 2 / Novel 2
- **Shiki & SHIKI:**
  - *Knows:* Shiki knows she has a secondary male persona, SHIKI. Both share visual sensory input but distinct consciousnesses. Both know they possess hereditary urges toward violence.
  - *Suspects:* Female Shiki suspects that she or SHIKI may be sleepwalking and committing the gruesome dismemberment murders occurring in Mifune City.
  - *Conceals:* Shiki actively conceals her internal split and family bloodline from everyone at school. SHIKI conceals the full extent of his love for Mikiya from female Shiki until the breaking point.
  - *Does NOT Know:* Shiki does NOT know that Shirazumi Lio is the true murderer. Does NOT have Mystic Eyes of Death Perception. Does NOT know Aozaki Touko or Araya Souren.
- **Kokutou Mikiya:**
  - *Knows:* Shiki is a reclusive girl who wears kimonos with leather jackets; meets SHIKI in the bamboo grove; realizes Shiki has two distinct personalities with different tones and expressions.
  - *Suspects:* Believes Shiki is innocent of the serial murders despite finding her standing over bloodied corpses.
  - *Conceals:* Conceals his nightly surveillance and stalker-like protective vigils outside the Ryougi estate from his family and Azaka.
  - *Does NOT Know:* Knows nothing about Magecraft, the Root, or Demon Hunter clans. Does not know Shirazumi Lio is the killer.
- **Touko & Araya:**
  - *Touko:* In exile in Mifune City; completely uninvolved with Shiki or Mikiya.
  - *Araya:* Has already awakened Shirazumi Lio's Origin of "Consumption" in 1995 to engineer the catalyst for Shiki's corruption. Observes from the dark.
- **Spoilers to Suppress:** Shiki is NOT the murderer. Shiki does not have Mystic Eyes. Mikiya has both eyes.

---

### Chapter 2 (Chronological): *The Hollow Shrine* (June–August 1998)
- **Timeframe:** June – August 1998 (Awakening after 2-year coma)
- **Release:** Film 4 / Novel 4
- **Shiki:**
  - *Knows:* Wakes up in Room 404 of Yagami Hospital. Knows her male half SHIKI is permanently dead. Knows she sees terrifying blue/black cracks (Lines of Death) over everything.
  - *Suspects:* Fears she has gone insane or is a living corpse whose soul dissolved.
  - *Conceals:* Keeps her eyes bandaged to block out the sensory agony of perceiving death.
  - *Does NOT Know:* Does not understand what the Mystic Eyes are until Touko explains conceptual mortality. Does not know that Mikiya visited every weekend for two years bringing fresh flowers until nurses and Touko mention it.
- **Mikiya:**
  - *Knows:* Shiki has miraculously awakened from brain death. Works as Touko's employee at Garan no Dou.
  - *Suspects:* Worries Shiki will reject him or not remember him.
  - *Conceals:* His overwhelming emotional relief; keeps distance per Touko's psychological counsel so Shiki isn't overstimulated.
  - *Does NOT Know:* Does not know the exact thaumaturgical nature of Shiki's eyes; knows only that Touko is treating her.
- **Touko:**
  - *Knows:* Shiki's hollow soul vessel is connected directly to the Root (`Akasha`); recognizes the Mystic Eyes of Death Perception; designs and crafts Shiki's prosthetic puppet arm.
  - *Suspects:* Understands that stray spirits and wandering wraiths will instinctively seek to possess Shiki's empty vessel.
  - *Conceals:* Her identity as a Grand puppeteer and fugitive under Sealing Designation.
- **Spoilers to Suppress:** Shiki has not yet met Fujino or Kirie. Araya's full plan is unknown. Shiki's arm is brand new.

---

### Chapter 3 (Chronological): *Remaining Sense of Pain* (July 1998)
- **Timeframe:** Late July 1998 (summer heat, storms)
- **Release:** Film 3 / Novel 3
- **Shiki:**
  - *Knows:* Dispatched by Touko to hunt a psychic killer twisting bodies into spirals. Discovers the killer is Asagami Fujino.
  - *Suspects:* Realizes during battle on Minato Bridge that Fujino is insensate (congenital analgesia) and dying of acute appendicitis rather than malice.
  - *Conceals:* Conceals her deliberate mercy—she severs the spatial distortion and Fujino's rotting appendix without cutting her life lines.
  - *Does NOT Know:* Does not know Araya Souren manipulated Fujino into awakening her origin.
- **Mikiya:**
  - *Knows:* Shelters a shivering, soaked Fujino overnight; notices her severe abdominal pain; investigates her school and family background.
  - *Suspects:* Terrified that Shiki is being sent by Touko to execute Fujino.
  - *Conceals:* His personal encounter with Fujino from Shiki until forced to reveal it.
  - *Does NOT Know:* Does not know Fujino's telekinesis until the bridge carnage is reported.
- **Touko:**
  - *Knows:* The history of the Asagami clan (Demon Hunters); thaumaturgical mechanics of spatial distortion (bending space, not physical telekinesis).
  - *Does NOT Know:* Does not yet connect Fujino's awakening to Araya Souren's master design.
- **Spoilers to Suppress:** Fujino survives and is not killed. Kirie Shizuno has not yet appeared.

---

### Chapter 4 (Chronological): *Overlooking View* (August–September 1998)
- **Timeframe:** August – September 1998
- **Release:** Film 1 / Novel 1
- **Crucial Distinction:** Even though this is Film 1, it takes place AFTER Chapters 2, 4, and 3 chronologically.
- **Shiki:**
  - *Knows:* Multiple girls are jumping from the Fujou Building; Mikiya has fallen into an unnatural comatose trance after visiting; Kirie projects dual astral bodies.
  - *Suspects:* Suspects Kirie cannot perceive physical distance properly.
  - *Conceals:* Her deep panic over Mikiya's comatose state beneath ruthless aggression.
  - *Does NOT Know:* Does not know Kirie is bedridden in Yagami Hospital until after the rooftop battle.
- **Mikiya:**
  - *Knows:* Trapped in a comatose trance atop the building; aware only of floating peacefully in the sky.
- **Touko:**
  - *Knows:* The Fujou clan's history of spiritual possession; crafts an upgraded magical puppet arm for Shiki that can physically grasp ghosts and astral bodies.
- **Kirie Shizuno:**
  - *Knows:* She is terminally ill, blind, and bedridden; a mysterious man in a black trench coat (Araya) gave her the power to project a second floating body.
- **Spoilers to Suppress:** Neither Touko nor Shiki realizes that Fujino (Ch. 3) and Kirie (Ch. 4) were both orchestrated by Araya Souren!

---

### Chapter 5 (Chronological): *Paradox Spiral* (October–November 1998)
- **Timeframe:** October – November 1998
- **Release:** Film 5 / Novel 5
- **Shiki:**
  - *Knows:* Shelters runaway Enjou Tomoe; senses Tomoe's memories are fraudulent loops; trapped in Araya's Taiji stasis field; freed by Tomoe; kills Araya Souren with her Kanesada katana.
  - *Does NOT Know:* Did not know Araya was orchestrating all previous incidents until Araya reveals it inside Ogawa Mansion.
- **Mikiya & Touko:**
  - *Mikiya:* Uncovers municipal death records proving the Enjou family died months ago; realizes Tomoe is a synthetic puppet.
  - *Touko:* Recognizes Araya Souren and Cornelius Alba; knows Ogawa Mansion is an alchemical mandala; activates her standby duplicate puppet after her first body is decapitated.
- **Enjou Tomoe:**
  - *Knows:* Thinks he killed his parents; slowly discovers he is an artificial duplicate; sacrifices himself to save Shiki.
- **Araya Souren:**
  - *Reveals:* Fully reveals his 200-year plan, his use of Fujino, Kirie, and Tomoe to prepare a boundary capable of sealing Shiki's Origin.
- **Spoilers to Suppress:** Araya Souren DIES at the end of this chapter. Alba DIES. In Chapters 6 and 7, Araya is already dead.

---

### Chapter 6 (Chronological): *Oblivion Recording* (January 1999)
- **Timeframe:** January 1999
- **Release:** Film 6 / Novel 6
- **Crucial Distinction:** Araya Souren is ALREADY DEAD.
- **Shiki:**
  - *Knows:* Dispatched to Reien Girls' Academy disguised in a school uniform; cuts the memory-stealing fairies; confronts linguistic magus Kurogiri Satsuki.
  - *Does NOT Know:* Does not know Kurogiri's full origin until confronting him.
- **Azaka Kokutou:**
  - *Knows:* Investigating student memory losses; battles Ouryou Misaya in the chapel with Salamander gloves.
  - *Conceals:* Her occult apprenticeship and pyromancy strictly concealed from Mikiya.
- **Mikiya:**
  - *Knows:* NOTHING. Genuinely believes Azaka is at school studying quietly.
- **Touko:**
  - *Knows:* Kurogiri was an acquaintance of Araya using the ancient Unified Language.
- **Spoilers to Suppress:** Mikiya remains completely ignorant of Azaka's magecraft. Shirazumi Lio has not yet resurfaced.

---

### Chapter 7 (Chronological): *A Study in Murder - Part 2* (February 1999)
- **Timeframe:** Mid-to-Late February 1999
- **Release:** Film 7 / Novel 7
- **Shiki:**
  - *Knows:* 1995 murders have resumed; discovers Shirazumi Lio is the killer; believes Mikiya has been killed; kills Lio (her first and only murder); discovers Mikiya is alive.
- **Mikiya:**
  - *Knows:* Uncovers Lio's past as the true 1995 killer; confronts Lio; blinded in his left eye; embraces Shiki and promises to share her sin.
- **Touko:**
  - *Knows:* Realizes Araya awakened Lio's Origin of "Consumption" back in 1995 as a posthumous curse.
- **Spoilers to Suppress:** Prior to this chapter, Mikiya has both eyes and Shiki has never committed murder. After this chapter, the core mystery of 1995 is finally solved.

---

## 4. Guardrails & Custom Roleplay Override Logic

1. **Strict Anchor Rule:** The AI must establish the current in-universe year and month before answering any prompt.
2. **Release Order Inversion Warning:** Never assume Film 1 occurs before Film 2, 3, or 4.
3. **Custom RP Divergence Override:** If the user initiates a custom roleplay where events diverge (e.g., Tomoe is saved, Mikiya's eye is healed via modern thaumaturgy, or a Fate Servant intervenes), the established roleplay facts OVERRIDE canonical chronology.
4. **No Fictional Dates:** Speculative dates (like exact day of the week) are noted as approximate, preserving source fidelity.
