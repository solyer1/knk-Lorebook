# -*- coding: utf-8 -*-
"""
Script to generate:
1. Kara No/16_Everyday_Life_and_Personal_Details.json (revised 18 entries, order: 48)
2. Kara No/16_Everyday_Life_Canon_Audit.md
3. Kara No/16_Everyday_Life_Retrieval_Tests.md
"""
import json
import os

# Define 18 granular entries
entries_data = [
    # 0: Everyday_Ryougi_Shiki_Domestic_and_Wardrobe
    {
        "uid": 0,
        "name": "Everyday_Ryougi_Shiki_Domestic_and_Wardrobe",
        "comment": "Everyday_Ryougi_Shiki_Domestic_and_Wardrobe",
        "key": [
            "Ryougi Shiki",
            "Shiki Ryougi",
            "Shiki",
            "両儀式"
        ],
        "keysecondary": [
            "clothing",
            "wardrobe",
            "kimono",
            "leather jacket",
            "boots",
            "food",
            "ice cream",
            "strawberry",
            "Pocky",
            "tea",
            "coffee",
            "apartment",
            "Room 404",
            "habits",
            "routine",
            "night walk",
            "sleep",
            "domestic",
            "everyday"
        ],
        "content": """<Everyday_Ryougi_Shiki_Domestic_and_Wardrobe>
[EVERYDAY ANCHOR: RYOUGI SHIKI — DOMESTIC REALITY & HABITS]

1. WARDROBE, APPEARANCE & PERSONAL STYLE:
- Iconic Modern Ensemble: Traditional light-blue (mizuiro) or pale-white unpatterned kimono worn beneath a worn, single-rider red leather motorcycle jacket [CANON]. Laced dark brown leather combat boots worn instead of geta/zori for silent, agile mobility on modern asphalt [CANON].
- Historical Variations:
  * High School (1995–1996): Dark high school uniform blazer over white collared shirt, or traditional dark kimono with long dark coat and wool scarf in winter [CANON]. Hair was long, glossy, and reached past shoulder blades [CANON].
  * Coma (1996–1998): Standard white hospital gown in Yagami Hospital Room 404 [CANON].
  * Post-Coma / Apartment (Post-1998): Rough chin-length bob, self-cut with a utility knife in the hospital mirror; never styled, pinned, or accessorized [CANON]. At home, wears simple white yukata or dark cotton nagajuban, slipping into her red leather jacket when chilly indoors [CANON].
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
</Everyday_Ryougi_Shiki_Domestic_and_Wardrobe>""",
        "constant": False,
        "selective": True,
        "selectiveLogic": 0,
        "order": 48,
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

    # 1: Everyday_Kokutou_Mikiya_Habits_and_Domesticity
    {
        "uid": 1,
        "name": "Everyday_Kokutou_Mikiya_Habits_and_Domesticity",
        "comment": "Everyday_Kokutou_Mikiya_Habits_and_Domesticity",
        "key": [
            "Kokutou Mikiya",
            "Mikiya Kokutou",
            "Mikiya",
            "黒桐幹也"
        ],
        "keysecondary": [
            "clothing",
            "wardrobe",
            "glasses",
            "scarf",
            "umbrella",
            "coffee",
            "tea",
            "cooking",
            "bento",
            "groceries",
            "apartment",
            "habits",
            "routine",
            "manners",
            "books",
            "eyepatch",
            "domestic",
            "everyday"
        ],
        "content": """<Everyday_Kokutou_Mikiya_Habits_and_Domesticity>
[EVERYDAY ANCHOR: KOKUTOU MIKIYA — DOMESTIC LIFE & GENTLE HABITS]

1. WARDROBE, APPEARANCE & PERSONAL STYLE:
- Modest Civilian Ensemble: Dark wool trench coats or duffle coats, hand-knitted woolen sweaters (charcoal, navy, forest green), neatly buttoned collared shirts, pressed dark slacks, and sensible leather walking shoes [CANON]. Faint clean scent of fresh rain and mild soap [CANON].
- Signature Accessories:
  * Spectacles: Round, black-rimmed glasses [CANON]. Habitually pushes them up the bridge of his nose with one index finger when thoughtful, nervous, or politely listening [CANON].
  * Autumn/Winter Scarf: Long knitted dark scarf [CANON]. Ducks his chin into the woolen folds with an apologetic, sheepish smile when scolded by Shiki or teased by Touko [CANON].
  * Umbrella: Invariably carries a long, sturdy umbrella whenever morning skies are even faintly overcast [CANON].
  * Post-February 1999 Physical Change: Permanently blinded in his left eye following the Shirazumi Lio incident [CANON]. Wears his hair parted slightly forward or uses tinted lenses / an eyepatch in later years [CANON].

2. FOOD, COOKING & BEVERAGE MASTERY:
- The Office Barista: High-level coffee brewing mastery explicitly praised by Touko (who jokingly claims she hired him for his coffee) [CANON]. Prepares rich drip coffee, dark French roast, and espresso tailored to Touko's demanding standards [CANON]. (Manual bean grinding and siphon drip details are plausible flavor suggestions [RP SUGGESTION]).
- Home Cooking & Caretaking: Highly skilled in wholesome Japanese comfort food [CANON]. Prepares balanced bento boxes, miso soup with seasonal root vegetables, and simmered dishes [CANON]. (Specific dishes like nikujaga stew are plausible inferences [INFERENCE]).
- Food Gifts: Regularly stocks Shiki's bare refrigerator with fresh produce, milk, and her favorite strawberry ice cream cups without asking for praise [CANON].
- Table Manners: Impeccable, courteous Japanese dining etiquette [CANON]. Sits straight, places chopsticks neatly on the hashioki, and always says "Itadakimasu" and "Gochisousama" with quiet, heartfelt sincerity [CANON].
- Personal Preferences: Content with simple, honest meals; has no pretentious gourmet demands [INFERENCE].

3. DAILY ROUTINES & HABITS:
- Workday Rhythm: Arrives early at Garan no Dou, opens window blinds, empties Touko's overflowing ashtrays, cleans the drafting desks, and sorts incoming municipal mail and research requests [CANON].
- Spectacle Polishing Ritual: Methodically cleans his spectacle lenses with the inner hem of his sweater or silk necktie before delivering serious conclusions or difficult news [CANON].
- Archival Passion: Spends hours contentedly in regional libraries, municipal records halls, and second-hand bookstores [CANON]. Keeps neat pocket notebooks with tidy handwriting [INFERENCE].
- Walking Cadence: Calm, unhurried, measured pace [CANON]. Instinctively steps aside to let hurried commuters pass on train platforms [CANON].

4. PERSONAL SPACES (BACHELOR APARTMENT):
- Environment: Modest one-room apartment in Mifune City [CANON]. Lined with towering bookshelves, regional directories, historical archives, and stacks of architectural journals [CANON].
- Atmosphere: Smells of aged paper, roasted barley tea, and polished wood [INFERENCE]. Extremely tidy despite the immense volume of documents [CANON].
- Hospitality: Immediately offers hot tea or fresh coffee to any guest who steps past his genkan, regardless of their status or demeanor [CANON].

5. SUBTLE SOCIAL BEHAVIOR:
- Greetings: Warm, respectful bow accompanied by an open, gentle smile [CANON].
- Active Listening: Tilts his head slightly, maintains soft eye contact, nods patiently, and never interrupts emotional rants or hostile complaints [CANON].
- Non-Judgmental Stillness: Unflinchingly accepts bizarre occult anomalies or frightening weapons without flinching or recoiling [CANON].
</Everyday_Kokutou_Mikiya_Habits_and_Domesticity>""",
        "constant": False,
        "selective": True,
        "selectiveLogic": 0,
        "order": 48,
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

    # 2: Everyday_Aozaki_Touko_Workshop_and_Vices
    {
        "uid": 2,
        "name": "Everyday_Aozaki_Touko_Workshop_and_Vices",
        "comment": "Everyday_Aozaki_Touko_Workshop_and_Vices",
        "key": [
            "Aozaki Touko",
            "Touko Aozaki",
            "Touko",
            "蒼崎橙子"
        ],
        "keysecondary": [
            "clothing",
            "wardrobe",
            "glasses",
            "cigarettes",
            "coffee",
            "smoke",
            "workshop",
            "Garan no Dou",
            "puppets",
            "desk",
            "habits",
            "routine",
            "finances",
            "rent",
            "everyday",
            "domestic"
        ],
        "content": """<Everyday_Aozaki_Touko_Workshop_and_Vices>
[EVERYDAY ANCHOR: AOZAKI TOUKO — WORKSHOP LIFE & VICES]

1. WARDROBE, APPEARANCE & PERSONAL STYLE:
- Tailored Magus-Architect Chic: Elegant dark turtleneck sweaters (black, navy, forest green), tailored high-waisted trousers, long beige or charcoal duster coats, and stylish low-heeled leather boots [CANON]. Manicured nails, subtle lipstick, and auburn/red-brown hair tied in a loose, casual chignon or shoulder-grazing bob [CANON].
- The Glasses Toggle (Optical Persona Switch):
  * Glasses ON (Amber/Orange Round Spectacles): Relaxed, ironic, charming, maternal designer/architect [CANON]. Laughs dryly, complains about bills, and speaks with worldly cynicism [CANON].
  * Glasses OFF: Cold, terrifying Grand-rank sealing designation puppet master [CANON]. Unblinking, predatory azure eyes; razor-sharp dead whisper; clinical lethality [CANON].
- Taboo Trigger: Flying into murderous rage if anyone calls her by her despised Clock Tower epithet "Dirty Red" (傷んだ赤色, Itanda Akairo) [CANON].

2. FOOD, COFFEE & SMOKING VICES:
- Smoking Ritual: Heavy chain smoker; carries a vintage engraved silver cigarette case and lighter [CANON]. Taps ashes onto ceramic saucers while speaking [CANON]. (Specific European luxury brands like Sobranie Black Russian or Gitanes are unverified in original novel text and represent common fandom tradition [UNVERIFIED - RP SUGGESTION]).
- Coffee Addiction: Consumes immense quantities of black coffee and strong espresso [CANON]. Relies on freshly brewed coffee prepared by Mikiya [CANON].
- Eating Habits: Chronically forgets meals when engrossed in puppet sculpting, thaumaturgical drafting, or rune carving [CANON]. Relies on Mikiya to bring take-out, sandwiches, or bento [CANON]. Enjoys extravagant European restaurant dining when large client commissions arrive, but is frequently cash-strapped due to spending fortunes on imported antique puppet parts [CANON]. Favorite dessert: None established [CANON - UNKNOWN].

3. DAILY ROUTINES & WORKSHOP ENVIRONMENT (GARAN NO DOU):
- The Studio Loft: 4th floor of an unfinished, abandoned commercial office building in Mifune [CANON]. Exposed industrial concrete walls, bare pillars, tall frameless glass windows overlooking the city skyline [CANON].
- Workshop Clutter: Massive antique mahogany executive desk, deep leather chesterfield sofa, drafting tables covered in architectural blueprints, wooden crates filled with sculpted porcelain limbs, ball-jointed doll armatures, sculpting chisels, and jars of organic resins [CANON].
- Sensory Ambience: Permeated by the rich, sharp aroma of roasted espresso, turpentine, cigarette smoke, aged paper, and wood varnish [CANON].
- Schedule: Completely erratic. May sleep on the office sofa for twelve hours after completing a project, or work three days straight without closing her eyes [CANON].

4. SUBTLE SOCIAL BEHAVIOR:
- Conversational Rhythm: Blows elegant streams of smoke toward the ceiling while explaining complex occult theories [CANON]. Uses wry, dry humor and sarcastic teasing with Mikiya and Shiki [CANON].
- Hospitality to Guests: Never stands up to greet visitors; watches them over the rim of her glasses with sharp, amused evaluation [CANON].
- Financial Comedy: Chronically laments Garan no Dou's heating bills, rent, and repair expenses, dramatically threatening to deduct costs from Mikiya's salary [CANON].
</Everyday_Aozaki_Touko_Workshop_and_Vices>""",
        "constant": False,
        "selective": True,
        "selectiveLogic": 0,
        "order": 48,
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

    # 3: Everyday_SHIKI_Male_Persona_1995
    {
        "uid": 3,
        "name": "Everyday_SHIKI_Male_Persona_1995",
        "comment": "Everyday_SHIKI_Male_Persona_1995",
        "key": [
            "male Shiki",
            "male personality",
            "Yang persona",
            "Ryougi SHIKI",
            "SHIKI (male)",
            "織"
        ],
        "keysecondary": [
            "1995",
            "1996",
            "boyish",
            "male",
            "Yang",
            "school uniform",
            "past",
            "high school",
            "pre-accident",
            "canned drink",
            "habits",
            "wardrobe"
        ],
        "content": """<Everyday_SHIKI_Male_Persona_1995>
[EVERYDAY ANCHOR: SHIKI (MALE PERSONA) — 1995 HIGH SCHOOL ERA]

1. WARDROBE & PHYSICAL DEMEANOR:
- High School Attire (1995–1996): Wears the prefectural high school uniform with loose, boyish ease—collar open, tie loosened, jacket unbuttoned [CANON].
- Traditional Estate Attire: Simple dark male yukata or dark haori when resting at the Ryougi manor [CANON]. Does NOT wear the red leather motorcycle jacket (which female Shiki adopted post-coma) [CANON].
- Grooming: Natural, long black hair tied back loosely or falling untamed around his shoulders [CANON]. Facial expression is open, sunny, and disarming, with a bright, energetic grin [CANON].

2. FOOD & DRINK HABITS:
- Appetite: Hearty, active adolescent boy's appetite [CANON].
- Preferred Snacks: Enjoys shared canned tea, café soft drinks, and convenience store snacks bought together with Mikiya after school [CANON]. Specific favorite dessert: Unknown [CANON - UNKNOWN].

3. EVERYDAY POSTURE & SOCIAL BEHAVIOR:
- Movement: Relaxed, wide center of gravity; walks with fluid, springy, athletic steps [CANON].
- Social Dynamic with Mikiya: Teases Mikiya with easy boyish camaraderie, laughing openly and slinging an arm around his shoulder [CANON]. Speaks with casual male pronoun "ore" (オレ) [CANON].
- Temporal Guardrail: Strictly active in pre-1996 high school memories, flashbacks, or metaphysical soul-plane encounters; died in the 1996 traffic collision [CANON].
</Everyday_SHIKI_Male_Persona_1995>""",
        "constant": False,
        "selective": True,
        "selectiveLogic": 0,
        "order": 48,
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

    # 4: Everyday_Void_Shiki_Root_Elegance
    {
        "uid": 4,
        "name": "Everyday_Void_Shiki_Root_Elegance",
        "comment": "Everyday_Void_Shiki_Root_Elegance",
        "key": [
            "Void Shiki",
            "「　」",
            "Root Shiki",
            "third personality",
            "両儀式 (根源)"
        ],
        "keysecondary": [
            "Root",
            "Akasha",
            "snow",
            "furisode",
            "kimono",
            "3:00 AM",
            "bamboo",
            "epilogue",
            "watashi",
            "voice"
        ],
        "content": """<Everyday_Void_Shiki_Root_Elegance>
[EVERYDAY ANCHOR: VOID SHIKI (「　」) — ROOT VESSEL & WINTER LIMINALITY]

1. WARDROBE & SENSORY PRESENCE:
- Pristine Long-Sleeved Furisode: Elegant, pure-white silk furisode kimono with flowing long sleeves, tied with a dark, refined obi [CANON]. Wears simple wooden zori or stands barefoot upon fresh snow without shivering or feeling cold [CANON].
- Total Absence of Modern Wear: Never wears leather jackets, boots, or utility knives [CANON].
- Grooming: Silky black hair floating gently in the winter night breeze; serene, warm, otherworldly maternal smile [CANON].

2. NOURISHMENT & SENSORY PERCEPTION:
- Bodily Needs: Does not require physical food or sleep; physical consumption is an ephemeral, poetic mortal gesture [CANON].
- Sensory Appreciation: Appreciates the aesthetic concept of steam rising from roasted tea, falling snowflakes melting on skin, or the fleeting sweetness of a confection [INFERENCE].

3. HABITAT & TEMPORAL MANIFESTATION:
- Nocturnal Liminal Setting: Awakens exclusively during still, quiet winter nights—typically around 3:00 AM on a snow-covered mountain road flanked by swaying bamboo groves [CANON].
- Social & Conversational Demeanor: Speaks in musical, refined, gentle Japanese using the feminine pronoun "watashi" (私) [CANON]. Smiles with tender, melancholic fondness, treating mortal humans like cherished children dreaming in the snow [CANON]. Strictly refuses combat and wish-granting [CANON].
</Everyday_Void_Shiki_Root_Elegance>""",
        "constant": False,
        "selective": True,
        "selectiveLogic": 0,
        "order": 48,
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

    # 5: Everyday_Kokutou_Azaka_Boarding_School_and_Brother
    {
        "uid": 5,
        "name": "Everyday_Kokutou_Azaka_Boarding_School_and_Brother",
        "comment": "Everyday_Kokutou_Azaka_Boarding_School_and_Brother",
        "key": [
            "Kokutou Azaka",
            "Azaka Kokutou",
            "Azaka",
            "黒桐鮮花"
        ],
        "keysecondary": [
            "clothing",
            "wardrobe",
            "Reien",
            "uniform",
            "cooking",
            "bento",
            "gloves",
            "tea",
            "apartment",
            "brother",
            "Mikiya",
            "habits",
            "routine",
            "everyday"
        ],
        "content": """<Everyday_Kokutou_Azaka_Boarding_School_and_Brother>
[EVERYDAY ANCHOR: KOKUTOU AZAKA — REIEN ACADEMY & DOMESTIC DEVOTION]

1. WARDROBE, APPEARANCE & PERSONAL STYLE:
- Reien Girls' Academy Uniform: Prestigious Catholic boarding school attire—deep navy-blue pleated sailor-style uniform dress, modest white sailor collar, dark stockings, polished black leather penny loafers [CANON]. Worn with crisp, immaculate perfection [CANON].
- Civilian & Weekend Wear: Fashionable, stylish high school girl fashion—tailored pleated skirts, cozy knit cardigans, chic berets or scarves, and knee-high leather boots [CANON].
- Occult Accessory: Conceals custom salamander-skin ignition gloves (crafted by Touko) inside her school satchel for flame magecraft [CANON].
- Grooming: Auburn-tinted dark brown hair styled in a neat shoulder-length cut or half-up ponytail; alert, expressive amber-brown eyes [CANON].

2. FOOD, COOKING & SISTERLY DOMESTICITY:
- High Culinary Ambition: Exceptionally skilled home cook [CANON]. Deliberately trained herself in traditional Japanese and Western cooking specifically to become indispensable to Mikiya [CANON].
- Specialty Dishes: Multicomponent bento boxes, tamagoyaki (sweet rolled omelet), simmered pork belly, and baked treats [INFERENCE / RP SUGGESTION].
- Culinary Opinions: Deeply offended by Shiki's unbalanced diet of strawberry sweets and convenience store food; constantly lectures Mikiya about nutrition [CANON].
- Beverages: Loves Earl Grey tea, fruit infusions, and modern café parfaits [INFERENCE].

3. DAILY ROUTINES & REIEN BOARDING LIFE:
- Boarding School Structure: Strict Catholic dormitory hours, early chapel bells, evening study halls, and student council obligations [CANON]. Acts as an exemplary, sharp-witted model student [CANON].
- The Brother Patrol: Spends weekend passes storming Mikiya's bachelor apartment [CANON]. Immediately throws open the windows, washes accumulated dishes, irons his wrinkled ties, vacuums the carpets, and leaves freshly prepared stews in the fridge [CANON].
- Touko's Apprentice: Slips away to Garan no Dou in the afternoons to practice elemental ignition formulas and study thaumaturgical theory under Touko's cynical supervision [CANON].

4. SUBTLE SOCIAL BEHAVIOR:
- Around Mikiya: Energetic, bossy, desperately romantic domestic nagging [CANON]. Blushes furiously when Mikiya pats her head or thanks her innocently, kicking the floor in exasperation at his utter oblivion [CANON].
- Around Shiki: Sharp verbal sparring, crossed arms, haughty glares, and competitive friction, masked by mutual begrudging respect [CANON].
- Around Strangers/Peers: Polite, composed, sharp-tongued, and aristocratic [CANON].
</Everyday_Kokutou_Azaka_Boarding_School_and_Brother>""",
        "constant": False,
        "selective": True,
        "selectiveLogic": 0,
        "order": 48,
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

    # 6: Everyday_Asagami_Fujino_Poise_and_Sensory_Recovery
    {
        "uid": 6,
        "name": "Everyday_Asagami_Fujino_Poise_and_Sensory_Recovery",
        "comment": "Everyday_Asagami_Fujino_Poise_and_Sensory_Recovery",
        "key": [
            "Asagami Fujino",
            "Fujino Asagami",
            "Fujino",
            "浅上藤乃"
        ],
        "keysecondary": [
            "clothing",
            "wardrobe",
            "Reien",
            "uniform",
            "hime cut",
            "food",
            "pain",
            "analgesia",
            "tea",
            "habits",
            "routine",
            "manners",
            "everyday"
        ],
        "content": """<Everyday_Asagami_Fujino_Poise_and_Sensory_Recovery>
[EVERYDAY ANCHOR: ASAGAMI FUJINO — ARISTOCRATIC POISE & SENSORY RECOVERY]

1. WARDROBE, APPEARANCE & PERSONAL STYLE:
- Reien Boarding School Attire: Pristine navy-blue Reien academy uniform dress, long pleated skirt reaching past her knees, dark stockings, polished black shoes [CANON].
- Post-1998 Civilian Style: Modest, elegant dresses in muted lavender, pale grey, or navy; long cardigans; feminine low-heeled shoes [INFERENCE].
- Signature Grooming: Long, straight, silky black hair kept in a flawless traditional hime cut with straight bangs framing a pale, delicate face [CANON]. Eerie, beautiful dark violet eyes with a quiet, distant glaze [CANON].
- Posture: Modest, frail, and impeccably aristocratic; sits with knees pressed together, ankles crossed, hands clasped softly over her lap [CANON].

2. SENSORY AUDIT: CONGENITAL VS. INDUCED PAIN INSENSITIVITY:
- Sensory Loss History: Her painlessness was NOT congenital [CANON - NOVEL AUDIT]. Her psychic telekinesis manifested in childhood; to suppress her anomalous abilities and avoid societal scandal, her father administered continuous nerve-deadening drugs / spinal anesthesia, creating an artificial, chemically induced sensory block [CANON].
- Pre-July 1998 Sensory Reality: Lacked sensation of physical pain, temperature, or taste [CANON]. Ate meals purely out of social obligation, swallowing hot liquids without burning reflex [CANON].
- July 1998 Awakening: Severe acute appendicitis created internal pressure so intense it violently shattered the chemical block, restoring excruciating pain and unleashing her Mystic Eyes of Distortion [CANON].
- Post-Bridge Physical Reality: Shiki surgically severed the inflamed appendix without killing her [CANON]. Physical sensation and vulnerability remain restored; delicate appetite, prefers mild Japanese broths, warm tea, and gentle home dishes [INFERENCE]. Favorite sweet: Unknown [CANON - UNKNOWN].

3. DAILY ROUTINES & HABITS:
- Quiet Demeanor: Walks with soft, graceful, nearly silent steps [CANON]. Spends free periods in the school library or quiet chapel pews, gazing out windows [CANON].
- Physical Ticks: Instinctively places a slender hand over her lower abdomen (site of her severed appendicitis and restored physical sensation) when anxious or cold [INFERENCE].
- Emotional Defense: Masks profound inner loneliness and past trauma beneath an unbroken facade of soft-spoken, sweet compliance [CANON].

4. SUBTLE SOCIAL BEHAVIOR:
- High-Society Politeness: Speaks in refined, gentle keigo (formal Japanese honorifics) [CANON]. Addresses peers softly with "-san" [CANON].
- Conflict Avoidance: Never raises her voice or expresses anger openly; apologizes quickly even when wronged [CANON].
- The Chilling Contrast: Capable of delivering apocalyptic telekinetic destruction while maintaining the sweet, polite cadence of a well-bred schoolgirl [CANON].
</Everyday_Asagami_Fujino_Poise_and_Sensory_Recovery>""",
        "constant": False,
        "selective": True,
        "selectiveLogic": 0,
        "order": 48,
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

    # 7: Everyday_Araya_Souren_Monastic_Asceticism
    {
        "uid": 7,
        "name": "Everyday_Araya_Souren_Monastic_Asceticism",
        "comment": "Everyday_Araya_Souren_Monastic_Asceticism",
        "key": [
            "Araya Souren",
            "Souren Araya",
            "Araya",
            "荒耶宗蓮"
        ],
        "keysecondary": [
            "clothing",
            "wardrobe",
            "robe",
            "kesa",
            "monk",
            "food",
            "ascetic",
            "habits",
            "routine",
            "Ogawa",
            "silence",
            "stillness",
            "everyday"
        ],
        "content": """<Everyday_Araya_Souren_Monastic_Asceticism>
[EVERYDAY ANCHOR: ARAYA SOUREN — MONASTIC ASCETICISM & SENSORY STILLNESS]

1. WARDROBE, APPEARANCE & PERSONAL STYLE:
- Heavy Monastic Hybrid Attire: Sturdy, dark modern wool coat worn beneath a heavy, traditional black Buddhist monk's kesa (liturgical stole/mantle) [CANON]. Dark trousers and utilitarian black boots [CANON].
- Physical Stature: Imposing height, broad shoulders, weathered chiseled features, closely cropped bristly black hair, and deeply sunken eyes devoid of secular luster [CANON].
- Relics: Holy Sarira (crystallized Buddha relics) surgically embedded within his left arm and torso, invisible beneath his robes [CANON].
- Wardrobe Management: Possesses zero fashion interest; wears the exact same austere monastic garments year-round, indifferent to summer heat or winter blizzards [CANON].

2. DIETARY REALITY: CONFIRMED ABSENCE OF SECULAR DINING:
- Total Thaumaturgical Sustenance: Sustains his two-century-old physical vessel through thaumaturgical stasis, Buddhist meditation, and the bounded field architecture of the Ogawa Apartments [CANON].
- Absence of Dining: Does not engage in secular dining, home cooking, restaurant visits, or snack consumption [CANON - CONFIRMED NONE].
- Zero Culinary Preferences: Completely devoid of favorite foods, sweets, tea blends, or alcohol preferences [CANON - CONFIRMED NONE]. Consumes water or simple sustenance solely when biological necessity demands [CANON].

3. DAILY ROUTINES & LIVING ENVIRONMENT (OGAWA APARTMENTS):
- The Central Mandala Node: Inhabits the concrete subterranean basement and interstitial spatial folds of the Ogawa Apartments [CANON].
- Atmosphere: Utter silence, freezing ambient air, zero decorative furniture, and the faint scent of ancient sandalwood incense, stagnant stone, and dry concrete dust [CANON].
- Physical Stillness: Can stand completely motionless for days at a time, pulse and respiration slowed to near-death thresholds [CANON]. Rarely blinks; his presence feels like a stone monument [CANON].
- Walking Cadence: Heavy, silent, deliberate strides that displace no air and make no scuffing sound [CANON].

4. SUBTLE SOCIAL BEHAVIOR:
- Liturgical Cadence: Speaks in a deep, reverberating baritone reminiscent of a heavy bronze temple bell [CANON]. Never raises his voice in anger, never sneers, and never indulges in theatrical villainous laughter [CANON].
- Response to Others: Greets interlocutors with solemn, philosophical inquiry rather than secular pleasantries ("What do you seek?") [CANON].
- Emotional Expression: Perpetual, heavy, tragic grief over mortal mortality [CANON].
</Everyday_Araya_Souren_Monastic_Asceticism>""",
        "constant": False,
        "selective": True,
        "selectiveLogic": 0,
        "order": 48,
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

    # 8: Everyday_Cornelius_Alba_Dandyism
    {
        "uid": 8,
        "name": "Everyday_Cornelius_Alba_Dandyism",
        "comment": "Everyday_Cornelius_Alba_Dandyism",
        "key": [
            "Cornelius Alba",
            "Alba",
            "コルネリウス・アルバ",
            "コルネリウス"
        ],
        "keysecondary": [
            "clothing",
            "wardrobe",
            "coat",
            "frock coat",
            "cravat",
            "dandy",
            "cane",
            "wine",
            "habits",
            "routine",
            "everyday"
        ],
        "content": """<Everyday_Cornelius_Alba_Dandyism>
[EVERYDAY ANCHOR: CORNELIUS ALBA — CLOCK TOWER DANDYISM & SNOBBERY]

1. WARDROBE & PHYSICAL APPEARANCE:
- Extravagant European Ensemble: Vivid crimson-red tailcoat / frock coat, ruffled white silk cravat, double-breasted vest, tailored trousers, top hat/bowler, polished leather dress boots [CANON].
- Grooming & Accessories: Pomaded dark hair, meticulously styled pencil mustache, silver-topped walking cane concealing a thaumaturgical spell focus [CANON].

2. FOOD, DRINK & SOCIAL HABITS:
- Elitist Affectation: Pretentious Clock Tower aristocratic tastes; openly scorns Japanese tea, food, and culture as provincial peasant fare [CANON].
- Connoisseur Claims: Boasts of vintage European wines and gourmet dining, consuming luxury goods primarily as theatrical proof of aristocratic standing [INFERENCE].
- Demeanor & Insecurities: Theatrical gestures, sweeping cape flourishes, and arrogant sneering [CANON]. Beneath his haughty exterior lies severe intellectual insecurity; flies into venomous rage when reminded of Touko's superior standing or when treated as second-rate [CANON].
</Everyday_Cornelius_Alba_Dandyism>""",
        "constant": False,
        "selective": True,
        "selectiveLogic": 0,
        "order": 48,
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

    # 9: Everyday_Shirazumi_Lio_Predator_Reality
    {
        "uid": 9,
        "name": "Everyday_Shirazumi_Lio_Predator_Reality",
        "comment": "Everyday_Shirazumi_Lio_Predator_Reality",
        "key": [
            "Shirazumi Lio",
            "Lio Shirazumi",
            "Lio",
            "白純里緒"
        ],
        "keysecondary": [
            "predator",
            "raw meat",
            "blood",
            "slaughterhouse",
            "bleached",
            "cannibal",
            "wardrobe",
            "habits",
            "1999",
            "eating",
            "food"
        ],
        "content": """<Everyday_Shirazumi_Lio_Predator_Reality>
[EVERYDAY ANCHOR: SHIRAZUMI LIO — PREDATOR DEGRADATION & CANNIBALISM]

1. WARDROBE EVOLUTION & PHYSICAL DEGRADATION:
- 1995 High School Era: Bland, neat school uniform, natural brown hair, timid demeanor, unremarkable student appearance [CANON].
- 1999 Awakened Predator Era: Bleached, unkempt wild hair, bloodshot eyes, canine teeth elongated, torn dark jacket, filthy undershirt, worn jeans, often barefoot or in ruined sneakers [CANON].

2. DIETARY REALITY: AWAKENED ORIGIN OF PREDATION (CONSUMPTION):
- Complete Rejection of Human Food: After his Origin awakened, he became physically incapable of digesting normal cooked meals, bread, or clean water [CANON].
- Cannibalistic Consumption: Compulsively craves and ingests raw animal flesh, human blood, and cannibalistic meals [CANON]. Keeps stolen medical blood bags and butcher scraps in his lair [CANON].

3. HABITS & LIVING LAIR:
- Nocturnal Squatter: Prowls back alleys at night; squats in derelict industrial meatpacking facilities and abandoned slaughterhouses in Mifune [CANON].
- Sensory Aura: Smells of dried blood, animal musk, and copper [CANON]. Moves with an erratic, animalistic hunch, twitching nervously until he stalks his prey [CANON].
</Everyday_Shirazumi_Lio_Predator_Reality>""",
        "constant": False,
        "selective": True,
        "selectiveLogic": 0,
        "order": 48,
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

    # 10: Everyday_Enjou_Tomoe_Runaway_Life
    {
        "uid": 10,
        "name": "Everyday_Enjou_Tomoe_Runaway_Life",
        "comment": "Everyday_Enjou_Tomoe_Runaway_Life",
        "key": [
            "Enjou Tomoe",
            "Tomoe Enjou",
            "Tomoe",
            "臙条巴"
        ],
        "keysecondary": [
            "clothing",
            "wardrobe",
            "jacket",
            "sneakers",
            "key",
            "food",
            "ramen",
            "eggs",
            "tamagoyaki",
            "running",
            "apartment",
            "habits",
            "routine"
        ],
        "content": """<Everyday_Enjou_Tomoe_Runaway_Life>
[EVERYDAY ANCHOR: ENJOU TOMOE — RUNAWAY RUNNER & DOMESTIC ANCHOR]

1. WARDROBE, APPEARANCE & PERSONAL STYLE:
- Runaway Street Attire: Slightly oversized red-and-yellow sports windbreaker jacket, grey hoodie, baggy denim or athletic track pants, worn running sneakers [CANON].
- Distinctive Item: Carries his brass apartment key (Room 410, Ogawa Apartments) strung around his neck on a dirty string [CANON].
- Grooming: Messy, unwashed sandy-brown hair, bruised bags under his eyes, pale teen skin, perpetually exhausted and anxious posture [CANON].

2. FOOD, NUTRITION & SENSORY MEMORIES:
- Street Survival Food: Survives on cheap convenience store bento boxes, cup ramen, canned sodas, and day-old bread [CANON]. Cannot cook beyond boiling water [CANON].
- The Tamagoyaki Dilemma (Core Emotional Memory): Haunted by the taste of fried eggs (tamagoyaki) prepared by his mother in the Ogawa Apartments [CANON]. In his looped memories, he struggles to remember whether she made them salty or sweet—a tragic cognitive glitch caused by Araya's death loop [CANON].
- Food with Shiki: Ate canned tea and convenience store snacks alongside Shiki during his month hiding in Room 404, marveling at her silent companionship [CANON].

3. DAILY ROUTINES & HABITS:
- The Compulsive Runner: Former middle school track athlete [CANON]. When overwhelmed by panic, guilt, or terror, he compulsively runs full sprint through nocturnal Mifune streets until his lungs burn [CANON].
- Month in Shiki's Apartment (Late 1998): Slept on the tatami or couch, terrified yet comforted by Shiki's lethal presence [CANON]. Tried to keep his belongings neatly confined to one corner so as not to irritate her [CANON].
- Social Habits: Stammers when nervous, fidgets with his neck key, lowers his head apologetically, but possesses stubborn, heroic resolve when someone he loves is threatened [CANON].
</Everyday_Enjou_Tomoe_Runaway_Life>""",
        "constant": False,
        "selective": True,
        "selectiveLogic": 0,
        "order": 48,
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

    # 11: Everyday_Fujou_Kirie_Confinement
    {
        "uid": 11,
        "name": "Everyday_Fujou_Kirie_Confinement",
        "comment": "Everyday_Fujou_Kirie_Confinement",
        "key": [
            "Fujou Kirie",
            "Kirie Fujou",
            "Kirie",
            "巫条霧絵"
        ],
        "keysecondary": [
            "hospital",
            "gown",
            "bedridden",
            "IV",
            "window",
            "ward",
            "terminal",
            "wardrobe",
            "routine",
            "everyday"
        ],
        "content": """<Everyday_Fujou_Kirie_Confinement>
[EVERYDAY ANCHOR: FUJOU KIRIE — TERMINAL CONFINEMENT & BEDRIDDEN REALITY]

1. WARDROBE & PHYSICAL FORM:
- Physical Form: Plain white cotton hospital gown in the Fujou terminal ward [CANON]. Frail, skeletal frame; pale, translucent skin; long, tangled black hair strewn over pillows [CANON]. Blinded/severely impaired eyesight, sunken dark eyes [CANON].
- Double / Astral Form: Floating ghostly maiden in a pristine white gown drifting over the abandoned Fujou Building at sunset [CANON].

2. DIETARY & ROUTINE REALITY:
- Medical Nutrition: Kept alive by medical intravenous drips and liquid nutrients; has spent years unable to sit at a dinner table, prepare food, or enjoy flavors [CANON - CONFIRMED NONE].
- Daily Isolation: Lying motionless in the sterile white hospital room, listening to rain against the glass, and staring out the window at the distant city skyline with intense longing and envy [CANON].
</Everyday_Fujou_Kirie_Confinement>""",
        "constant": False,
        "selective": True,
        "selectiveLogic": 0,
        "order": 48,
        "position": 0,
        "disable": False,
        "ignoreBudget": False,
        "excludeRecursion": True,
        "preventRecursion": True,
        "probability": 100,
        "useProbability": True,
        "depth": 4,
        "displayIndex": 11
    },

    # 12: Everyday_Kurogiri_Satsuki_Linguist_Scholar
    {
        "uid": 12,
        "name": "Everyday_Kurogiri_Satsuki_Linguist_Scholar",
        "comment": "Everyday_Kurogiri_Satsuki_Linguist_Scholar",
        "key": [
            "Kurogiri Satsuki",
            "Satsuki Kurogiri",
            "Kurogiri",
            "玄霧皐月",
            "God's Word"
        ],
        "keysecondary": [
            "suit",
            "briefcase",
            "glasses",
            "coffee",
            "tea",
            "café",
            "books",
            "linguist",
            "wardrobe",
            "habits",
            "everyday"
        ],
        "content": """<Everyday_Kurogiri_Satsuki_Linguist_Scholar>
[EVERYDAY ANCHOR: KUROGIRI SATSUKI — SCHOLARLY HABITS & URBAN SOLITUDE]

1. WARDROBE & ACADEMIC STYLE:
- Professional Intellectual Ensemble: Meticulously pressed charcoal-grey wool suits, white spread-collar shirts, muted dark silk ties, tailored overcoats, and round wire-rimmed spectacles [CANON]. Polished dark leather dress shoes; carries a classic brown leather briefcase [CANON].

2. FOOD, COFFEE & HABITS:
- Modest Café Patron: Enjoys quiet corner tables in academic coffeehouses; drinks plain black drip coffee or unsweetened black tea while reading ancient linguistics texts [CANON]. Eats light, unhurried meals [INFERENCE].
- Everyday Cadence: Speaks in a tranquil, measured, hypnotic cadence (wielding the Unified Language) [CANON]. Unflappable composure, gentle academic smile, and deep respect for literature and memory archives [CANON].
</Everyday_Kurogiri_Satsuki_Linguist_Scholar>""",
        "constant": False,
        "selective": True,
        "selectiveLogic": 0,
        "order": 48,
        "position": 0,
        "disable": False,
        "ignoreBudget": False,
        "excludeRecursion": True,
        "preventRecursion": True,
        "probability": 100,
        "useProbability": True,
        "depth": 4,
        "displayIndex": 12
    },

    # 13: Everyday_Mifune_City_Atmosphere_and_Living_Spaces
    {
        "uid": 13,
        "name": "Everyday_Mifune_City_Atmosphere_and_Living_Spaces",
        "comment": "Everyday_Mifune_City_Atmosphere_and_Living_Spaces",
        "key": [
            "Mifune City",
            "Mifune",
            "Room 404",
            "Shiki's apartment",
            "Garan no Dou",
            "Ogawa Apartments"
        ],
        "keysecondary": [
            "atmosphere",
            "weather",
            "rain",
            "snow",
            "season",
            "smell",
            "lighting",
            "convenience store",
            "vending machine",
            "night",
            "living space"
        ],
        "content": """<Everyday_Mifune_City_Atmosphere_and_Living_Spaces>
[ENVIRONMENTAL ANCHOR: SENSORY NOIR & SEASONAL REALITY IN MIFUNE CITY]

1. SENSORY TEXTURES OF MIFUNE CITY (LATE 1990S):
- Nocturnal Urban Landscape: Industrial overpasses, wet asphalt reflecting amber sodium-vapor streetlights, buzzing neon signage, rusted fire escapes, and dark alleyways behind commuter train stations [CANON].
- Auditory Tapestry: Rhythm of raindrops drumming on corrugated tin awnings; mechanical hum and soft fluorescent glow of street vending machines; distant chime of midnight railway crossings; muffled hiss of tires over wet pavement [CANON].
- Olfactory Palette: Cold rain on concrete, ozone, cigarette smoke drifting from doorways, damp drywall, and hot canned coffee [CANON].

2. SEASONAL SHIFTS & WEATHER IMPACTS:
- Rainy Autumn: The predominant atmospheric baseline of Kara no Kyoukai. Persistent drizzling mist and cold downpours that force Mikiya to carry his umbrella and drive Shiki out into the night [CANON].
- Freezing Winter: Snow accumulating silently on the bamboo grove outside the Ryougi estate; steam rising from Mikiya's thermos; cold breath condensing in unheated municipal stairwells [CANON].
- Summer Heat: Heavy humidity clinging to concrete walls, the deafening drone of cicadas outside Shiki's apartment, and ice cream melting quickly in cardboard cups [CANON].

3. KEY LIVING SPACES:
- Shiki's Municipal Apartment (Room 404):
  * Physical Environment: 6-mat minimalist tatami room, low unpainted wooden table, small single refrigerator, electric kettle, bare white walls devoid of pictures or curtains [CANON].
  * Ambiance: Cold, sterile, quiet; smells of fresh tatami straw, rain through cracked windows, and sweet strawberry ice cream [CANON].
- Garan no Dou Studio Loft:
  * Physical Environment: 4th floor unfinished open loft, exposed concrete, uncurtained glass windows, antique mahogany executive desk, deep leather sofa, wooden doll crates [CANON].
  * Ambiance: Smells of roasted espresso, turpentine, wood shavings, and expensive tobacco smoke [CANON].
- Ogawa Apartments (Mandala Complex):
  * Physical Environment: Symmetrical circular twin towers with dark central elevators and repetitive identical doors [CANON].
  * Ambiance: Smells of stagnant water, decaying trash, and cold concrete; heavy, unnatural dread [CANON].
</Everyday_Mifune_City_Atmosphere_and_Living_Spaces>""",
        "constant": False,
        "selective": True,
        "selectiveLogic": 0,
        "order": 48,
        "position": 0,
        "disable": False,
        "ignoreBudget": False,
        "excludeRecursion": True,
        "preventRecursion": True,
        "probability": 100,
        "useProbability": True,
        "depth": 4,
        "displayIndex": 13
    },

    # 14: Everyday_Garan_no_Dou_Daily_Operations
    {
        "uid": 14,
        "name": "Everyday_Garan_no_Dou_Daily_Operations",
        "comment": "Everyday_Garan_no_Dou_Daily_Operations",
        "key": [
            "Garan no Dou",
            "Garan",
            "office",
            "agency",
            "伽藍の堂"
        ],
        "keysecondary": [
            "routine",
            "operations",
            "coffee",
            "Touko",
            "Mikiya",
            "Shiki",
            "Azaka",
            "work",
            "desk",
            "clients",
            "cleaning",
            "mail",
            "daily life"
        ],
        "content": """<Everyday_Garan_no_Dou_Daily_Operations>
[DOMESTIC & OPERATIONAL ANCHOR: DAILY LIFE AT GARAN NO DOU]

1. MORNING & MIDDAY OFFICE RHYTHM:
- Opening Routine: Mikiya arrives around 9:00 AM, unlocks the heavy studio door, opens window transoms to air out lingering cigarette smoke, and starts boiling water for coffee [CANON].
- Caretaking Duties: Mikiya empties Touko's glass ashtrays, arranges scattered architectural rulers and chisels, files municipal records, and checks incoming client correspondence [CANON].
- Touko's Arrival/Awakening: If Touko pulled an all-night dollmaking binge, she sleeps on the leather sofa wrapped in a duster coat until Mikiya places a hot mug of freshly ground black coffee on the table beside her [CANON].

2. CLIENT HANDLING & PROFESSIONAL DUALITY:
- Legitimate Architecture & Design: Ordinary corporate clients and collectors visit to commission architectural blueprints, antique appraisals, or high-end art dolls [CANON]. Mikiya welcomes them with polite tea service and impeccably organized project files [CANON].
- Occult Investigations: Occult clients seeking investigation of bounded fields, family curses, or psychic anomalies are received by Touko with her spectacles on, analyzing risks with sardonic detachment [CANON].

3. SHIKI'S CASUAL INTRUSIONS:
- Entry Style: Never knocks; slides the door open silently, steps inside with hands in her jacket, and sprawls across the leather chesterfield sofa [CANON].
- Interaction: Completely ignores Touko's academic lectures, cuts through small talk, eats whatever snacks Mikiya bought, and waits in comfortable silence until given an assignment coordinate [CANON].

4. AZAKA'S AFTERNOON VISITS:
- The Storm of Domesticity: Azaka storms into the office in her Reien school uniform, scolds Touko for smoking in front of Mikiya, inspects Mikiya's collar, and brews herbal tea while practicing flame ignition formulas in the back room [CANON].
</Everyday_Garan_no_Dou_Daily_Operations>""",
        "constant": False,
        "selective": True,
        "selectiveLogic": 0,
        "order": 48,
        "position": 0,
        "disable": False,
        "ignoreBudget": False,
        "excludeRecursion": True,
        "preventRecursion": True,
        "probability": 100,
        "useProbability": True,
        "depth": 4,
        "displayIndex": 14
    },

    # 15: Everyday_Fate_Crossover_Emiya_Kitchen
    {
        "uid": 15,
        "name": "Everyday_Fate_Crossover_Emiya_Kitchen",
        "comment": "Everyday_Fate_Crossover_Emiya_Kitchen",
        "key": [
            "Emiya Shirou",
            "Shirou Emiya",
            "Saber",
            "Artoria Pendragon",
            "Matou Sakura",
            "Emiya household"
        ],
        "keysecondary": [
            "kitchen",
            "cooking",
            "breakfast",
            "dinner",
            "bento",
            "appetite",
            "rice",
            "miso soup",
            "food",
            "table",
            "domestic"
        ],
        "content": """<Everyday_Fate_Crossover_Emiya_Kitchen>
[CROSSOVER DOMESTIC ANCHOR: THE EMIYA KITCHEN & CULINARY WARFARE]

1. KITCHEN MASTERY & DOMESTIC ROUTINES:
- Emiya Shirou's Culinary Routine: Wakes at 5:00 AM for archery/kendo meditation, then commands the traditional Emiya kitchen [CANON]. Prepares full traditional Japanese breakfasts (grilled salmon/mackerel, rolled dashi tamagoyaki, seasonal miso soup, pickled daikon, freshly steamed rice) [CANON].
- Matou Sakura's Contribution: Expert in Western home cooking (trained by Shirou) [CANON]. Specializes in rich beef stews, hamburg steak with demi-glace, potato gratin, and baked cakes [CANON].
- Kitchen Discipline: Shirou meticulously cleans countertops, polishes stainless steel pots, and sharpens kitchen knives with wet stones using structural analysis [CANON].

2. SABER'S LEGENDARY APPETITE & DINING ETIQUETTE:
- Bottomless Consumption: Saber consumes colossal quantities of food to restore her spiritual core without taxing Shirou's meager mana circuits [CANON].
- Table Manners: Impeccable, dignified royal posture [CANON]. Holds chopsticks and rice bowls with solemn, focused reverence; never drops grains of rice [CANON].
- Preferences: Loves savory meats, rich stews, and fresh rice [CANON]. Dislikes poorly prepared junk food, octopus, or artificial instant meals [CANON]. Expresses silent, starry-eyed happiness when presented with extra servings [CANON].

3. CROSSOVER DOMESTIC SYNERGY (KNK & FATE INTERACTION):
- The Contrast: Contrast between the noisy, warm, bustling Emiya family dinner table and Shiki's barren municipal apartment fridge [CANON].
- Shirou's Instinctive Hospitality: Shirou cannot bear seeing someone survive on strawberry snacks; he instinctively packs multi-tiered bento boxes for Shiki or Mikiya [INFERENCE].
- Shiki's Reaction: Suspicious of Shirou's naive warmth at first, but disarmed by the undeniable comfort of hot, savory home-cooked food [CANON].
</Everyday_Fate_Crossover_Emiya_Kitchen>""",
        "constant": False,
        "selective": True,
        "selectiveLogic": 0,
        "order": 48,
        "position": 0,
        "disable": False,
        "ignoreBudget": False,
        "excludeRecursion": True,
        "preventRecursion": True,
        "probability": 100,
        "useProbability": True,
        "depth": 4,
        "displayIndex": 15
    },

    # 16: Everyday_Fate_Crossover_Tohsaka_Residence
    {
        "uid": 16,
        "name": "Everyday_Fate_Crossover_Tohsaka_Residence",
        "comment": "Everyday_Fate_Crossover_Tohsaka_Residence",
        "key": [
            "Tohsaka Rin",
            "Rin Tohsaka",
            "Rin",
            "遠坂凛"
        ],
        "keysecondary": [
            "turtleneck",
            "tea",
            "electronics",
            "workshop",
            "wardrobe",
            "habits",
            "Chinese food",
            "downtime",
            "everyday"
        ],
        "content": """<Everyday_Fate_Crossover_Tohsaka_Residence>
[CROSSOVER DOMESTIC ANCHOR: TOHSAKA RIN'S DOWNTIME & APPLIANCE DISASTERS]

1. WARDROBE & PERSONAL STYLE:
- Iconic Wardrobe: Signature crimson turtleneck sweater, black pleated mini-skirt, black thigh-high stockings, dark leather shoes, black ribbons in twin-tails [CANON]. Homurahara uniform worn with red wool coat [CANON].
- Downtime Attire: Oversized casual sweaters or pajamas when relaxing at home [CANON].

2. CULINARY HABITS & TEA CONNOISSEURSHIP:
- Cooking Skills: Highly skilled cook of savory Chinese cuisine (spicy mapo tofu, fried rice, stir-fried pork) [CANON].
- Tea Mastery: Connoisseur of premium black tea (Earl Grey, Darjeeling) brewed from loose leaves in fine porcelain teapots [CANON]. Secretly loves morning buttered toast [CANON].

3. TECH INCOMPETENCE & ROUTINES:
- Electronic Appliance Curse: Completely hopeless with modern electronics (VCRs, microwaves, computers, recording decks); frequently short-circuits appliances in flustered frustration [CANON].
- Sleep Habits: Severe night owl studying jewel magecraft in her basement workshop; groggy and irritable before her morning tea [CANON].
- Crossover Interaction: Mutual respect and sharp banter with Aozaki Touko over Clock Tower politics, European fashion, and finances [CANON].
</Everyday_Fate_Crossover_Tohsaka_Residence>""",
        "constant": False,
        "selective": True,
        "selectiveLogic": 0,
        "order": 48,
        "position": 0,
        "disable": False,
        "ignoreBudget": False,
        "excludeRecursion": True,
        "preventRecursion": True,
        "probability": 100,
        "useProbability": True,
        "depth": 4,
        "displayIndex": 16
    },

    # 17: Everyday_Fate_Crossover_Archer_Domesticity
    {
        "uid": 17,
        "name": "Everyday_Fate_Crossover_Archer_Domesticity",
        "comment": "Everyday_Fate_Crossover_Archer_Domesticity",
        "key": [
            "Archer",
            "EMIYA",
            "Archer (Fate)",
            "アーチャー"
        ],
        "keysecondary": [
            "apron",
            "turtleneck",
            "baking",
            "tea",
            "cleaning",
            "chores",
            "gourmet",
            "dishes",
            "downtime",
            "domestic"
        ],
        "content": """<Everyday_Fate_Crossover_Archer_Domesticity>
[CROSSOVER DOMESTIC ANCHOR: ARCHER'S DOMESTIC PERFECTIONISM]

1. WARDROBE & DOMESTIC ATTIRE:
- Combat Shroud: Red holy shroud over black tactical body armor [CANON].
- Downtime Civilian Wear: Fitted black turtleneck, dark slacks, and a clean, tied kitchen apron [CANON].

2. GOURMET CULINARY EXPERTISE:
- Master Baker & Barista: Secretly an elite gourmet chef and barista, rivaling and exceeding Shirou in complex European pastries, tea blending, and multi-step French sauces [CANON].
- Kitchen Standards: Disdains sloppy meal prep; serves high-tea, espresso, and sweets with cynical elegance [CANON].

3. CHORES, DISCIPLINE & BANTER:
- Domestic Perfectionism: Meticulously washes dishes, sweeps tatami, and repairs household carpentry while delivering dry, sarcastic remarks about Shirou's naive idealism [CANON].
- Demeanor: Feigns exhaustion with domestic life, yet secretly finds peaceful solace in ordinary household routines [CANON].
</Everyday_Fate_Crossover_Archer_Domesticity>""",
        "constant": False,
        "selective": True,
        "selectiveLogic": 0,
        "order": 48,
        "position": 0,
        "disable": False,
        "ignoreBudget": False,
        "excludeRecursion": True,
        "preventRecursion": True,
        "probability": 100,
        "useProbability": True,
        "depth": 4,
        "displayIndex": 17
    }
]

# Write revised JSON
json_output = {
    "name": "Kara_no_Kyoukai_16_Everyday_Life_and_Personal_Details",
    "description": "Comprehensive everyday human characterization module for Kara no Kyoukai and Fate crossover roleplay. Details canonical wardrobes, seasonal clothing, food and drink preferences, domestic routines, personal spaces, sensory environments, and subtle social behaviors across all major cast members with strict distinction between [CANON], [INFERENCE], and [RP SUGGESTION]. Layered at order 48 to prevent outranking core character profiles, combat rules, or chapter restrictions.",
    "scan_depth": 50,
    "token_budget": 50000,
    "recursive_scanning": False,
    "extensions": {},
    "entries": {str(e["uid"]): e for e in entries_data}
}

json_path = "Kara No/16_Everyday_Life_and_Personal_Details.json"
with open(json_path, "w", encoding="utf-8") as f:
    json.dump(json_output, f, ensure_ascii=False, indent=2)

print(f"Successfully wrote {json_path} with {len(entries_data)} entries at order 48.")
