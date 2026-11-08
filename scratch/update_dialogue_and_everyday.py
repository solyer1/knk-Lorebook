# -*- coding: utf-8 -*-
"""
Updates 13_Dialogue_Examples.json and 16_Everyday_Life_and_Personal_Details.json
with verified canon dialogue, philosophical excerpts, and domestic details from Chapter 1 (Overlooking View).
"""
import json
import os

dialogue_path = r"d:\Personalise\Homemad\Lorebook\Nasuverse\Kara No\13_Dialogue_Examples.json"
everyday_path = r"d:\Personalise\Homemad\Lorebook\Nasuverse\Kara No\16_Everyday_Life_and_Personal_Details.json"

# =========================================================================
# 1. UPDATE 13_Dialogue_Examples.json
# =========================================================================
with open(dialogue_path, "r", encoding="utf-8") as f:
    dialogue_lb = json.load(f)

# Update description
dialogue_lb["description"] = (
    "Dialogue, voice, subtext, and characterization demonstration module for SillyTavern roleplay. "
    "Contains 11 focused scene demonstrations showing natural cadence, physical gestures, conversational restraint, "
    "and distinct voices for Shiki, Mikiya, Touko, and Fate crossover interactions, directly derived and verified "
    "from Kinoko Nasu's canonical light novel prose."
)

# Enrich Entry 0 (Dialogue_Shiki_Mikiya_Ordinary_Banter)
entry_0_content = """<Dialogue_Shiki_Mikiya_Ordinary_Banter>
[DEMONSTRATION STATUS]
Canonically verified demonstration derived directly from Kinoko Nasu's novel prose in Chapter 1 (*Overlooking View / Thanatos*).

[SCENE CONTEXT]
Inside Shiki's minimalist one-room municipal apartment. A narrow hallway less than a meter long leads into the bare living/sleeping space, furnished only with a bed, tatami, and a small refrigerator. Mikiya arrives unannounced on an early August evening carrying a convenience store plastic bag containing two strawberry Häagen-Dazs ice cream cups.

[DIALOGUE DEMONSTRATION: CANON NOVEL EXCHANGE]
Mikiya stood by the entrance as he untied his shoes, giving his usual calm, ordinary smile.

"Good evening. You look lazy as always, Shiki."

He tossed the plastic bag lightly toward the counter.

"I passed an accident on my way here. A girl jumped from the top of a building; it was a suicide. I heard it's been happening a lot lately, but I never thought I'd see it myself. Here, freezer."

Inside were two strawberry Häagen-Dazs. Shiki slowly inspected the contents of the bag before looking up.

"Shiki, you skipped school again today, didn't you?" Mikiya scolded gently, stepping into the room. "Your grades can be fixed later, but if you don't at least attend the required number of days, you won't even pass. Did you forget our promise to go to college together?"

Shiki followed him inside, her expression flat, hands buried in her pockets.

"Do you have the right to lecture me about school? I don't remember such a promise, and what's more, you've already dropped out of college."

"Uh, if you say 'rights', there aren't any rights for anybody," Mikiya retorted defensively, sitting down in the center of the bare floor.

Shiki watched him from behind, sitting on the edge of her bed. He kept the exact, boring image of an ordinary student: unstyled black hair, no tan, no accessories, no cell phone, ordinary plain clothes, and black-rimmed spectacles that made his gentle face look almost cute.

---

[CANON CLIMAX: THE STRAWBERRY SLEEPOVER INVITATION]
(Late August, after the resolution of the Fujou Building incident, walking back in the dusk):

"Mikiya, come over to my place tonight," Shiki suddenly blurted out, her voice low, gripping his sleeve.

Mikiya blinked, taken aback. "Huh? Why all of a sudden? It's fine, but you don't have anything in your room. It's boring even if I do go. Or are you telling me there's something I have to do there?"

Shiki glared at him as if he were being deliberately obtuse.

"Strawberry."

"Huh?"

"Two strawberry Häagen-Dazs," Shiki muttered, her jaw tightening. "They're still there in the freezer from when you bought them. Finish those things off, man."

Mikiya sighed helplessly. "...I guess I did buy those."

"All right, I'll spend the night," Mikiya relented with a sigh, then looked at her with a completely straight, earnest face. "But Shiki... you shouldn't talk like that. You're a girl, you know."

Shiki instantly clicked her tongue and turned her face away in angry embarrassment.

[CHARACTER VOICE & RHYTHM ANALYSIS]
- Shiki's Voice: Blunt, masculine phrasing ("Finish those things off, man" / かたづけろ、男), using mundane food excuses to disguise severe loneliness and emotional attachment. When called out on her lack of femininity by Mikiya, she cannot argue back—she merely looks away in irritable, petulant embarrassment.
- Mikiya's Voice: Gentle, teasingly defensive, treating Shiki's supernatural world with grounded domesticity. Scolds her like a protective older brother or fond partner.

[THAI LOCALIZATION & DIALOGUE DISCIPLINE]
- Male First-Person Rule: Male characters MUST NEVER refer to themselves as "ฉัน". Mikiya uses gentle "ผม" or naturally omits the pronoun (zero-anaphora).
- 2nd-Person Address: Mikiya consistently addresses Shiki as "เธอ" or by name "ชิกิ", never "นาย". Female Shiki may use "ฉัน" for herself or naturally omit pronouns.
- Thai Localization Canonical Exchange & Domestic Banter:
  * Mikiya: "ถอดรองเท้าบู้ทแล้วนะ ชิกิ" (Addresses her by name "ชิกิ", never "นาย").
  * Shiki: "มิกิยะ คืนนี้มาค้างที่ห้องฉันสิ" (Blunt, direct invitation; female Shiki uses "ฉัน").
  * Mikiya: "เอ๋? ทำไมจู่ ๆ ถึงชวนล่ะ? ...มีเรื่องอะไรที่ผมต้องไปทำที่นั่นเหรอ?" (Defensive, polite "ผม", zero-anaphora; never "ฉัน").
  * Shiki: "สตรอว์เบอร์รี"
  * Mikiya: "หือ?"
  * Shiki: "ฮาเก้นดาสรสสตรอว์เบอร์รีสองถ้วยที่นายซื้อมาทิ้งไว้ไง รีบ ๆ ไปจัดการให้หมดเลยนะ เจ้าบ้า"
  * Mikiya: "...นั่นสินะ ผมเป็นคนซื้อมาจริง ๆ ด้วย... เอาเถอะ ค้างก็ได้ แต่ชิกิ..."
  * Shiki: (หันมองมิกิยะด้วยสายตากึ่งรำคาญ)
  * Mikiya: "อย่าพูดจาห้าวแบบนั้นสิ เธอเป็นผู้หญิงนะรู้ไหม" (Addresses her as "เธอ", never "นาย").
  * Shiki: (หันหน้าหนีไปอีกทางด้วยความหงุดหงิดแกมเขิน)
</Dialogue_Shiki_Mikiya_Ordinary_Banter>"""

dialogue_lb["entries"]["0"]["content"] = entry_0_content

# Add Entry 10: Dialogue_Canon_Overlooking_View_Floating_and_Thanatos
entry_10 = {
    "uid": 10,
    "name": "Dialogue_Canon_Overlooking_View_Floating_and_Thanatos",
    "comment": "Dialogue_Canon_Overlooking_View_Floating_and_Thanatos",
    "order": 140,
    "key": [
        "Overlooking View dialogue",
        "Floating vs Flying dialogue",
        "Thanatos dialogue",
        "Touko suicide lecture",
        "Kyoukai novel chapter 1 dialogue",
        "บทสนทนาทิวทัศน์เบื้องสูง",
        "การลอยกับการบิน",
        "บทสนทนาปรัชญาโทโกะ",
        "วันนี้เธอบินไม่ได้"
    ],
    "keysecondary": [
        "Touko",
        "Shiki",
        "Azaka",
        "suicide",
        "floating",
        "flying",
        "pressed flower",
        "impulse",
        "คำคมโทโกะ",
        "ดอกไม้แห้ง",
        "การฆ่าตัวตาย",
        "ดาดฟ้า"
    ],
    "content": """<Dialogue_Canon_Overlooking_View_Floating_and_Thanatos>
[DEMONSTRATION STATUS]
Canonically verified philosophical and character dialogue directly extracted from Kinoko Nasu's novel prose in Chapter 1 (*Overlooking View / Thanatos*).

[SCENE 1: TOUKO EXPLAINING THE "OVERLOOKING VIEW" (GARAN NO DOU)]
Inside the top-floor studio of Garan no Dou. Sunlight streams through unfinished concrete window frames. Touko stands gazing out over the sprawling vista of Mifune City, thin blue smoke curling lazily from her Dragonfly cigarette. Shiki sits silently on the couch.

"A view from a high place is overwhelming," Touko said, her voice carrying a dry, academic lilt. "The scenery you see is magnificent: even an ordinarily boring landscape would look beautiful. But that's not the impulse you feel when you look down onto the world you live in. The overlooking view only gives you one impulse..."

Touko paused, tapping ash from her cigarette.

"That impulse is 'distance'. A vision too expansive creates a vivid, terrifying severance between you and the world. Human beings can only feel sanity around things close to them. When the world becomes a miniature map beneath your feet, your body forgets its physical boundaries. The distance is so vast that stepping out into empty air no longer feels like death—it feels like walking into the sky."

---

[SCENE 2: FLOATING (浮遊) VS. FLYING (飛行)]
Touko exhaled a cloud of smoke, her amber eyes narrowing behind her spectacles.

"There is a fundamental difference between 'floating' and 'flying', Shiki.
- Floating is passive. It is a lonely, aimless drift without direction, carried entirely by the whims of the wind. A balloon floats; a ghost floats. It requires no will, only detachment.
- Flying is an act of sovereign will. It is defying gravity with your own power to reach a chosen destination.
The girl on the roof, Fujou Kirie, believed she was flying. But she possessed neither destination nor wings; she was merely floating in a hollow sky. And when a floating existence is severed from its dream, there is only one word left for it: 'The Fall'."

---

[SCENE 3: CANON EPILOGUE (TOUKO & AZAKA ON THE STREET)]
Late summer twilight. Touko and Kokutou Azaka are walking along the main avenue in Mifune City. Suddenly, a sickening, wet impact shatters the air. A body crashes onto the asphalt—crushed pale limbs and black hair spreading like a pressed flower flattened between the covers of a heavy book. Kirie's physical body has leapt from the Fujou building.

Azaka catches up to Touko, pale and shaken.

"Ms. Touko... She committed suicide by jumping off that building. I don't get what goes on in these people's minds. Do you know, Ms. Touko?"

Touko looked up at the empty sky above the rooftops, her voice quiet, worldly, and completely devoid of judgment as she lit a cigarette:

"There's no reason for suicide. It's just that she wasn't able to fly today."
(「自殺に理由はない。ただ、今日は飛べなかっただけだ」)

[THAI LOCALIZATION & CHARACTER CADENCE]
- Touko's Voice: Sarcastic, intellectual, world-weary. In Thai dialogue, Touko uses "ฉัน" or natural zero-anaphora; never sounds like a generic cartoon villain.
- Azaka's Voice: Earnest, formal, polite Catholic student tone (ค่ะ/คะ).
- Thai Dialogue Translation:
  * Touko: "ทิวทัศน์ที่มองจากที่สูงน่ะมันงดงามก็จริง... แต่มันไม่ได้มอบความประทับใจให้หรอกนะ สิ่งที่ทิวทัศน์เบื้องสูงมอบให้มีเพียงแรงกระตุ้นเดียวเท่านั้น... นั่นคือความรู้สึก 'ห่างไกล' ทัศนวิสัยที่กว้างใหญ่เกินไปจะตัดขาดตัวตนของเธอกับโลกออกจากกัน..."
  * Touko: "การลอยกับการบินน่ะต่างกันลิบลับ การลอยคือการเคว้งคว้างไปตามลมอย่างไร้ทิศทางและไร้จุดหมาย... แต่การบินคือการใช้เจตจำนงของตัวเองฝืนแรงโน้มถ่วงเพื่อไปยังจุดหมายที่ต้องการ"
  * Azaka: "อาจารย์โทโกะคะ... คนพวกนั้นคิดอะไรอยู่กันแน่คะถึงได้ฆ่าตัวตาย? อาจารย์รู้ไหมคะ?"
  * Touko: "การฆ่าตัวตายน่ะไม่มีเหตุผลหรอก... ก็แค่ วันนี้เธอบินไม่ได้เท่านั้นเอง"
</Dialogue_Canon_Overlooking_View_Floating_and_Thanatos>"""
}

dialogue_lb["entries"]["10"] = entry_10

with open(dialogue_path, "w", encoding="utf-8") as f:
    json.dump(dialogue_lb, f, ensure_ascii=False, indent=2)

print(f"Successfully updated {dialogue_path}. Total entries: {len(dialogue_lb['entries'])}")

# =========================================================================
# 2. UPDATE 16_Everyday_Life_and_Personal_Details.json
# =========================================================================
with open(everyday_path, "r", encoding="utf-8") as f:
    everyday_lb = json.load(f)

# Update Entry 0: Confirm Häagen-Dazs Strawberry as Canon Novel
entry_0_text = everyday_lb["entries"]["0"]["content"]
entry_0_text = entry_0_text.replace(
    "- Established Favorites: Strawberry ice cream cups (specifically brought by Mikiya; she pretends indifference but eats it immediately) [CANON - NOVEL & FILM]. Häagen-Dazs branded mini-cups appear prominently in the visual adaptation [CANON - FILM ADAPTATION].",
    "- Established Favorites: Strawberry Häagen-Dazs ice cream cups (explicitly named in Kinoko Nasu's novel text Chapter 1: \"Inside are two strawberry Häagen-Dazs\"; Mikiya brings them and Shiki eats them while pretending indifference) [CANON - NOVEL & FILM]."
)
# Update Shiki's apartment layout details
entry_0_text = entry_0_text.replace(
    "- Environment: Minimalist, bare tatami apartment. Unadorned white walls, no posters, television, or ornamental clutter [CANON]. Low wooden table, single small refrigerator (bare except for tea and sweets), futon stowed in closet [CANON].",
    "- Environment: Minimalist, bare one-room municipal apartment. Narrow entrance hallway less than a meter long leading into the combined bedroom/living area [CANON - NOVEL CHAPTER 1]. Unadorned white walls, zero decorative clutter, low wooden table, single small refrigerator (bare except for tea and strawberry Häagen-Dazs), futon stowed in closet [CANON]."
)
everyday_lb["entries"]["0"]["content"] = entry_0_text

# Update Entry 1: Confirm Mikiya's exact physical description from Chapter 1
entry_1_text = everyday_lb["entries"]["1"]["content"]
entry_1_text = entry_1_text.replace(
    "- Modest Civilian Ensemble: Dark wool trench coats or duffle coats, hand-knitted woolen sweaters (charcoal, navy, forest green), neatly buttoned collared shirts, pressed dark slacks, and sensible leather walking shoes [CANON]. Faint clean scent of fresh rain and mild soap [CANON].",
    "- Modest Civilian Ensemble & Exact Physical Profile: Height is roughly 170 cm [CANON - NOVEL CHAPTER 1]. Possesses a gentle, kind-looking face that leans on the cute side, accentuated by black-rimmed spectacles [CANON - NOVEL CHAPTER 1]. Maintains the clean, unstyled image of an ordinary student: natural unstyled black hair (never dyed, never permed, never grown long), no tan, no jewelry or accessories, no cell phone, and does not play around with women [CANON - NOVEL CHAPTER 1]. Dresses in dark wool coats, woolen sweaters, collared shirts, and pressed slacks [CANON]. Scent of fresh rain and mild soap [CANON]."
)
everyday_lb["entries"]["1"]["content"] = entry_1_text

with open(everyday_path, "w", encoding="utf-8") as f:
    json.dump(everyday_lb, f, ensure_ascii=False, indent=2)

print(f"Successfully updated {everyday_path}.")
