import json

path = 'Kara No/16_Everyday_Life_and_Personal_Details.json'
with open(path, 'r', encoding='utf-8') as f:
    data = json.load(f)

entry_0 = data['entries']['0']

# Update keysecondary
sec = entry_0['keysecondary']
for new_k in ['nemaki', 'morning', 'wake']:
    if new_k not in sec:
        sec.append(new_k)

# Updated content
new_content = """<Everyday_Ryougi_Shiki_Domestic_and_Wardrobe>
[EVERYDAY ANCHOR: RYOUGI SHIKI — DOMESTIC REALITY & HABITS]

1. WARDROBE, APPEARANCE & PERSONAL STYLE:
- Iconic Outdoor Ensemble: Traditional light-blue (mizuiro) or pale-white unpatterned kimono worn beneath a worn, single-rider red leather motorcycle jacket [CANON]. Laced dark brown leather combat boots worn instead of geta/zori for silent, agile mobility on modern asphalt [CANON].
- Indoor Apartment Loungewear: In Room 404, Shiki lounges solely in her unpatterned kimono (hitoe) or white under-robe (nagajuban / nemaki) tied loosely with a simple cloth sash [CANON - NOVEL CHAPTER 1]. The red leather jacket is strictly outdoor outerwear (uwagi); in novel Chapter 1, Shiki explicitly notes: "When I left the house, I put on a red leather jacket over my light blue kimono" [CANON]. She does NOT wear the leather jacket while casually relaxing indoors unless the room is freezing in the morning or she is heading out.
- Retainer Backstory & Total Refusal of Western Clothes: Wore traditional Japanese wafuku exclusively since birth as the Ryougi heir [CANON]. When entering high school, her caretaker/retainer Suzurigi Akitaka (硯木秋隆) purchased modern Western adolescent girl clothes for her; Shiki flatly refused to wear them, insisting solely on traditional kimonos [CANON]. Her kimonos are tailored haute-couture garments supplied by the clan and laundered/repaired by Akitaka after battles [CANON].
- Undergarments (Classical Kimono Custom): Confirmed by Kinoko Nasu and Takashi Takeuchi (Movie 2 Pamphlet Q&A): Adheres to classical Japanese kimono custom and wears no Western undergarments (braless, no panties) under her daily kimono and robes [CANON].
- Sleepwear & Morning Wear (Nemaki & Awakening):
  * Sleepwear: Sleeps in a plain white cotton nemaki (寝間着, sleeping yukata) or nagajuban (長襦袢) tied loosely with a cloth sash (koshihimo), or collapses directly in her daytime kimono when exhausted after late-night prowls [CANON].
  * Morning Demeanor: Severe low morning blood pressure (teiketsuatsu) and disheveled bedhead (neguse); groggy, disoriented, and slow to boot up in the morning [CANON].
  * Zero Self-Consciousness Around Mikiya: When Mikiya visits in the morning with groceries/milk, Shiki shows zero embarrassment or feminine modesty—remains curled or sitting cross-legged on her futon in her disheveled morning robe with messy hair, greeting him with a sleepy, muffled complaint ("Noisy, Kokutou... what time is it?") [CANON].
- Historical Variations:
  * High School (1995–1996): Dark high school uniform blazer over white collared shirt, or traditional dark kimono with long dark coat and wool scarf in winter [CANON]. Hair was long, glossy, and reached past shoulder blades [CANON].
  * Coma (1996–1998): Standard white hospital gown in Yagami Hospital Room 404 [CANON].
  * Post-Coma / Apartment (Post-1998): Rough chin-length bob, self-cut with a utility knife in the hospital mirror; never styled, pinned, or accessorized [CANON].
- Clothing Fit & Mannerisms: Jacket cuffs are worn soft at the wrists; hands are almost perpetually buried deep inside the leather jacket pockets [CANON]. Never wears jewelry, makeup, perfume, or hairpins [CANON]. Pulls collar up over her lower face when flustered, cold, or hiding embarrassment [CANON].

2. FOOD, SWEETS & DRINK HABITS:
- Established Favorites: Strawberry ice cream cups (specifically brought by Mikiya; she pretends indifference but eats it immediately) [CANON - NOVEL & FILM]. Häagen-Dazs branded mini-cups appear prominently in the visual adaptation [CANON - FILM ADAPTATION]. Strawberry Pocky / biscuit sticks (frequently held or nibbled while brooding in visual media) [CANON - ADAPTATION / OFFICIAL ART].
- Drinks: Canned hot black coffee from street vending machines in winter (thrusts the hot can against Mikiya's chest to warm him) [CANON]. Canned green tea and hot roasted barley tea (mugicha) brewed by Mikiya [CANON].
- Dislikes & Unknowns: Dislikes elaborate, overly rich banquet food or pretentious cuisine [INFERENCE]. Alcohol preference: Completely unknown in canon; does not drink casually [CANON - UNKNOWN].
- Cooking & Dining: Zero domestic cooking skills [CANON]. Her apartment kitchen contains an electric kettle and chopsticks; survives on convenience store buns (anpan), instant noodles, and takeout unless Mikiya brings groceries or bento [CANON]. Table manners are solitary, casual, and minimalist—sits cross-legged or in loose seiza on tatami, holding bowls close [CANON].

3. DAILY ROUTINES & HABITS:
- Nighttime Prowl: Severe night owl. Wanders deserted Mifune streets between 1:00 AM and 4:00 AM, particularly during rain or snow, listening to water hitting asphalt [CANON].
- Posture & Movement: Walks with an unnervingly silent, predatory glide; leaves no heavy heel strike [CANON]. Leans back against walls with one boot propped up [CANON].
- Sensory Responses: Loves rain, mist, cold air, and snowfall [CANON]. Deeply dislikes noisy, brightly lit commercial crowds [CANON].
- Smoking: Brooding habit; occasionally lights a cigarette when stressed, taking one of Touko's, though Mikiya scolds her [CANON].

4. PERSONAL SPACE (ROOM 404 MUNICIPAL APARTMENT):
- Environment: Minimalist, bare tatami apartment. Unadorned white walls, no posters, television, or ornamental clutter [CANON]. Low wooden table, single small refrigerator (bare except for tea and sweets), futon stowed in closet [CANON].
- Atmosphere: Quiet hum of the refrigerator, rain tapping against glass, scent of fresh tatami straw and cool nocturnal air [CANON].
- Possessions: Conceals a high-grade spring-loaded folding knife (magatama handle) in her jacket [CANON]. The ancient Kanesada katana is kept safely inside the wooden shirasaya in her closet [CANON]. Left arm is Touko's puppet prosthetic [CANON].
- Guest Policy: Doors are typically unlocked for Mikiya; has slippers ready but acts grumpy when he arrives unannounced [CANON]. Hostile to uninvited strangers [CANON].

5. SUBTLE SOCIAL BEHAVIOR:
- Greetings: Ignores polite hellos; opens with dry, flat observations: "You're late," "It's raining," "What do you want?" [CANON].
- Handling Silence: Extremely comfortable with prolonged silence; never fills quiet space with empty small talk [CANON].
- Deflection of Care: Masks warmth behind abrasive complaints ("You're noisy, Kokutou," "Baka Mikiya"), while quietly sliding closer or accepting food [CANON].
</Everyday_Ryougi_Shiki_Domestic_and_Wardrobe>"""

entry_0['content'] = new_content

with open(path, 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print('Successfully updated Entry 0 in Module 16.')
