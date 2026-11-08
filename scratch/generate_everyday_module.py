# -*- coding: utf-8 -*-
"""
Generator script for:
1. Kara No/16_Everyday_Life_and_Personal_Details.json
2. Kara No/16_Everyday_Life_Research_Notes.md
"""
import json
import os

os.makedirs("Kara No", exist_ok=True)

# Define entries for 16_Everyday_Life_and_Personal_Details.json
entries_data = [
    # Entry 0: Everyday_Ryougi_Shiki_Domestic_and_Wardrobe
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
            "habits",
            "routine",
            "night walk",
            "sleep",
            "everyday",
            "lifestyle"
        ],
        "content": """<Everyday_Ryougi_Shiki_Domestic_and_Wardrobe>
[EVERYDAY ANCHOR: RYOUGI SHIKI — DOMESTIC REALITY & HABITS]

1. WARDROBE, APPEARANCE & PERSONAL STYLE:
- Iconic Ensemble: Traditional light-blue (mizuiro) or pale-white unpatterned kimono worn beneath a worn, single-rider red leather motorcycle jacket [CANON]. Laced dark brown leather combat boots worn instead of geta/zori for agile, silent mobility on modern asphalt [CANON].
- Historical Variations:
  * High School (1995-1996): Dark high school uniform blazer over white collared shirt, or traditional long-sleeved dark kimono with long dark coat and wool scarf in winter [CANON]. Hair was long, glossy, and reached past her shoulder blades [CANON].
  * Coma (1996-1998): Standard white hospital gown in Yagami Hospital Room 404 [CANON].
  * Post-Coma / Apartment (Post-1998): Rough chin-length bob, self-cut with a utility knife in the hospital mirror; never styled, pinned, or accessorized [CANON]. At home, wears simple white yukata or dark cotton nagajuban, slipping into her red leather jacket when chilly indoors [CANON].
- Clothing Fit & Mannerisms: Jacket cuffs are worn soft at the wrists; hands are almost perpetually buried deep inside the leather jacket pockets [CANON]. Never wears jewelry, makeup, perfume, or hairpins [CANON]. Pulls collar up over her lower face when flustered, cold, or hiding embarrassment [CANON].

2. FOOD, SWEETS & DRINK HABITS:
- Established Favorites: Häagen-Dazs strawberry ice cream cups (specifically brought by Mikiya; she pretends indifference but eats it immediately) [CANON]. Strawberry Pocky (frequently seen idly holding or chewing a stick while brooding) [CANON].
- Drinks: Canned hot black coffee from street vending machines in winter [CANON]. Canned green tea and hot roasted barley tea (mugicha) brewed by Mikiya [CANON].
- Dislikes & Unknowns: Dislikes elaborate, overly rich banquet food or pretentious cuisine [INFERENCE]. Alcohol preference: Completely unknown in canon; does not drink casually [CANON - UNKNOWN].
- Cooking & Dining: Zero domestic cooking skills [CANON]. Her apartment kitchen contains an electric kettle and a few chopsticks; she survives on convenience store buns (anpan), instant noodles, and takeout unless Mikiya brings groceries or bento [CANON]. Table manners are solitary, casual, and minimalist—sits cross-legged or in loose seiza on tatami, holding bowls close [CANON].

3. DAILY ROUTINES & HABITS:
- Nighttime Prowl: Severe night owl. Wanders deserted Mifune streets between 1:00 AM and 4:00 AM, particularly during rain or snow, listening to water hitting asphalt [CANON].
- Posture & Movement: Walks with an unnervingly silent, predatory glide; leaves no heavy heel strike [CANON]. Leans back against walls with one boot propped up [CANON].
- Sensory Responses: Loves rain, mist, cold air, and snowfall [CANON]. Deeply dislikes noisy, brightly lit commercial crowds [CANON].
- Smoking: Brooding habit; occasionally lights a cigarette when stressed, taking one of Touko's, though Mikiya scolds her [CANON].

4. PERSONAL SPACE (ROOM 404 MUNICIPAL APARTMENT):
- Environment: Minimalist, bare tatami apartment. Unadorned white walls, no posters, television, or ornamental clutter [CANON]. Low wooden table, single small refrigerator (often empty except for tea and sweets), futon stowed in closet [CANON].
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
        "order": 140,
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

    # Entry 1: Everyday_Kokutou_Mikiya_Habits_and_Domesticity
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
            "everyday",
            "lifestyle"
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
- The Office Barista: High-level coffee brewing mastery [CANON]. Grinds whole beans manually at Garan no Dou; prepares rich siphon drip coffee, dark French roast, and espresso tailored to Touko's demanding standards [CANON].
- Home Cooking & Caretaking: Highly skilled in wholesome Japanese comfort food [CANON]. Prepares balanced bento boxes, nikujaga (beef and potato stew), miso soup with seasonal root vegetables, and simmered fish [CANON].
- Food Gifts: Regularly stocks Shiki's bare refrigerator with fresh produce, milk, and her favorite strawberry ice cream cups without asking for praise [CANON].
- Table Manners: Impeccable, courteous Japanese dining etiquette [CANON]. Sits straight, places chopsticks neatly on the hashioki, and always says "Itadakimasu" and "Gochisousama" with quiet, heartfelt sincerity [CANON].
- Personal Preferences: Content with simple, honest meals; has no pretentious gourmet demands [INFERENCE].

3. DAILY ROUTINES & HABITS:
- Workday Rhythm: Arrives early at Garan no Dou, opens window blinds, empties Touko's overflowing ashtrays, cleans the drafting desks, and sorts incoming municipal mail and research requests [CANON].
- Spectacle Polishing Ritual: Methodically cleans his spectacle lenses with the inner hem of his sweater or silk necktie before delivering serious conclusions or difficult news [CANON].
- Archival Passion: Spends hours contentedly in regional libraries, municipal records halls, and second-hand bookstores [CANON]. Keeps meticulous, tidy pocket notebooks written in miniature, printed-like handwriting [CANON].
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
        "order": 141,
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

    # Entry 2: Everyday_Aozaki_Touko_Workshop_and_Vices
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
            "lifestyle"
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
- Smoking Ritual: Chain smoker of imported high-grade European cigarettes (Sobranie Black Russian, French Gitanes/Gauloises, or Marlboro Lights) [CANON]. Carries a vintage engraved silver cigarette case and matching lighter [CANON]. Taps ashes onto ceramic saucers while speaking [CANON].
- Coffee Addiction: Consumes immense quantities of black coffee and strong espresso [CANON]. Demands freshly ground roasts brewed by Mikiya, jokingly claiming she hired him purely for his coffee skills [CANON].
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
        "order": 142,
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

    # Entry 3: Everyday_SHIKI_and_Void_Shiki
    {
        "uid": 3,
        "name": "Everyday_SHIKI_and_Void_Shiki",
        "comment": "Everyday_SHIKI_and_Void_Shiki",
        "key": [
            "SHIKI",
            "male Shiki",
            "Void Shiki",
            "「　」",
            "Root Shiki"
        ],
        "keysecondary": [
            "clothing",
            "wardrobe",
            "kimono",
            "furisode",
            "snow",
            "bamboo",
            "food",
            "tea",
            "habits",
            "routine",
            "boyish",
            "1995",
            "1996",
            "everyday",
            "lifestyle"
        ],
        "content": """<Everyday_SHIKI_and_Void_Shiki>
[EVERYDAY ANCHORS: SHIKI (MALE PERSONA) & VOID SHIKI (ROOT)]

1. SHIKI (MALE PERSONA — PRE-1996 HIGH SCHOOL ERA):
- Wardrobe & Appearance:
  * High School Attire: Wears the prefectural high school uniform with loose, boyish ease—collar open, tie loosened, jacket unbuttoned [CANON].
  * Traditional Estate Attire: Simple dark male yukata or dark haori when resting at the Ryougi manor [CANON]. Does NOT wear the red leather jacket (which female Shiki adopted post-coma) [CANON].
  * Grooming: Natural, long black hair tied back loosely or falling untamed around his shoulders [CANON]. Facial expression is open, sunny, and disarming, with a bright grin [CANON].
- Food & Drink Habits:
  * Hearty, active boy's appetite [CANON]. Enjoys shared canned tea, café soft drinks, and snacks bought together with Mikiya after school [CANON]. Specific favorite dessert: Unknown [CANON - UNKNOWN].
- Everyday Posture & Demeanor:
  * Relaxed, wide center of gravity; walks with fluid, springy steps [CANON].
  * Teases Mikiya with easy boyish camaraderie, laughing openly and slinging an arm around his shoulder [CANON]. Speaks with casual male pronoun "ore" (オレ) [CANON].

2. VOID SHIKI (`「　」` — THE ROOT VESSEL):
- Wardrobe & Appearance:
  * Pristine Long-Sleeved Furisode: Elegant, pure-white silk furisode kimono with flowing sleeves, tied with a dark, refined obi [CANON]. Wears simple wooden zori or stands barefoot upon fresh snow without shivering [CANON].
  * Total Absence of Modern Wear: Never wears leather jackets, boots, or utility knives [CANON].
  * Grooming: Beautiful, silky black hair floating gently in the winter night breeze; serene, warm, otherworldly maternal smile [CANON].
- Food & Drink:
  * Does not require sustenance; eating is a purely aesthetic, ephemeral human gesture [CANON]. Appreciates the sensory idea of steam rising from roasted tea or the melting sweetness of a confection [INFERENCE].
- Habitat & Temporal Setting:
  * Awakens exclusively during liminal, quiet winter moments—typically around 3:00 AM on a snow-covered mountain road flanked by swaying bamboo groves [CANON].
- Subtle Social Demeanor:
  * Speaks in musical, refined, gentle Japanese using the feminine pronoun "watashi" (私) [CANON].
  * Smiles with tender, melancholic fondness, treating mortal humans like cherished children dreaming in the snow [CANON]. Refuses combat and wish-granting [CANON].
</Everyday_SHIKI_and_Void_Shiki>""",
        "constant": False,
        "selective": True,
        "selectiveLogic": 0,
        "order": 143,
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

    # Entry 4: Everyday_Kokutou_Azaka_Boarding_School_and_Brother
    {
        "uid": 4,
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
            "everyday",
            "lifestyle"
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
- Specialty Dishes: Multicomponent bento boxes, tamagoyaki (sweet rolled omelet), simmered pork belly, homemade cookies, and fruit tarts [INFERENCE].
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
        "order": 144,
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

    # Entry 5: Everyday_Asagami_Fujino_Poise_and_Sensory_Void
    {
        "uid": 5,
        "name": "Everyday_Asagami_Fujino_Poise_and_Sensory_Void",
        "comment": "Everyday_Asagami_Fujino_Poise_and_Sensory_Void",
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
            "everyday",
            "lifestyle"
        ],
        "content": """<Everyday_Asagami_Fujino_Poise_and_Sensory_Void>
[EVERYDAY ANCHOR: ASAGAMI FUJINO — ARISTOCRATIC POISE & SENSORY RECOVERY]

1. WARDROBE, APPEARANCE & PERSONAL STYLE:
- Reien Boarding School Attire: Pristine navy-blue Reien academy uniform dress, long pleated skirt reaching past her knees, dark stockings, polished black shoes [CANON].
- Post-1998 Civilian Style: Modest, elegant dresses in muted lavender, pale grey, or navy; long cardigans; feminine low-heeled shoes [INFERENCE].
- Signature Grooming: Long, straight, silky black hair kept in a flawless traditional hime cut with straight bangs framing a pale, delicate face [CANON]. Eerie, beautiful dark violet eyes with a quiet, distant glaze [CANON].
- Posture: Modest, frail, and impeccably aristocratic; sits with knees pressed together, ankles crossed, hands clasped softly over her lap [CANON].

2. FOOD, SENSORY EXPERIENCE & PHYSICAL SHIFTS:
- Pre-July 1998 (Congenital Analgesia Era):
  * Total sensory numbness due to childhood trauma and nerve-suppressing medication [CANON]. Could not feel physical pain, hot, cold, or taste flavors [CANON].
  * Ate meals entirely out of social performance; swallowed boiling soup or spicy dishes with a blank smile, unable to perceive temperature or taste [CANON].
- Post-July 1998 (Post-Appendicitis & Bridge Sparing):
  * Sensation and physical vulnerability restored [CANON]. Delicate appetite; prefers mild Japanese broths, warm barley tea, and gentle, un-spiced home dishes [INFERENCE]. Favorite dessert: None established [CANON - UNKNOWN].
- Physical Frailty: Chronic physical fragility post-bridge; tires easily after long walks and handles damp cold poorly [CANON].

3. DAILY ROUTINES & HABITS:
- Quiet Demeanor: Walks with soft, graceful, nearly silent steps [CANON]. Spends free periods in the school library or quiet chapel pews, gazing out windows [CANON].
- Physical Ticks: Instinctively places a slender hand over her lower abdomen (the site of her severed appendicitis and restored physical sensation) when anxious or cold [INFERENCE].
- Emotional Defense: Masks profound inner loneliness and past trauma beneath an unbroken facade of soft-spoken, sweet compliance [CANON].

4. SUBTLE SOCIAL BEHAVIOR:
- High-Society Politeness: Speaks in refined, gentle keigo (formal Japanese honorifics) [CANON]. Addresses peers softly with "-san" [CANON].
- Conflict Avoidance: Never raises her voice or expresses anger openly; apologizes quickly even when wronged [CANON].
- The Chilling Contrast: Capable of delivering apocalyptic telekinetic destruction while maintaining the sweet, polite cadence of a well-bred schoolgirl [CANON].
</Everyday_Asagami_Fujino_Poise_and_Sensory_Void>""",
        "constant": False,
        "selective": True,
        "selectiveLogic": 0,
        "order": 145,
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

    # Entry 6: Everyday_Araya_Souren_Monastic_Asceticism
    {
        "uid": 6,
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
            "everyday",
            "lifestyle"
        ],
        "content": """<Everyday_Araya_Souren_Monastic_Asceticism>
[EVERYDAY ANCHOR: ARAYA SOUREN — MONASTIC ASCETICISM & SENSORY STILLNESS]

1. WARDROBE, APPEARANCE & PERSONAL STYLE:
- Heavy Monastic Hybrid Attire: Sturdy, dark modern wool coat worn beneath a heavy, traditional black Buddhist monk's kesa (liturgical stole/mantle) [CANON]. Dark trousers and utilitarian black boots [CANON].
- Physical Stature: Imposing height, broad shoulders, weathered chiseled features, closely cropped bristly black hair, and deeply sunken eyes devoid of secular luster [CANON].
- Relics: Holy Sarira (crystallized Buddha relics) surgically embedded within his left arm and torso, invisible beneath his robes [CANON].
- Wardrobe Management: Possesses zero fashion interest; wears the exact same austere monastic garments year-round, indifferent to summer heat or winter blizzards [CANON].

2. FOOD, DRINK & COMPLETE CULINARY ASCETICISM:
- Absolute Ascetic Regimen: Food is strictly biological fuel required to sustain his ancient physical container [CANON].
- Diet: Plain boiled rice, dry grains, pure water, and basic rations [CANON]. Zero culinary preferences, indulgences, sweets, or luxury drinks [CANON - CONFIRMED NONE].
- Alcohol & Vices: Completely absent. Does not drink sake, tea blends, or coffee; does not smoke [CANON].
- Table Manners: Silent, mechanical, solitary sustenance consumption; eats without enjoyment or disgust [CANON].

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
        "order": 146,
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

    # Entry 7: Everyday_Alba_and_Lio_Extreme_Lifestyles
    {
        "uid": 7,
        "name": "Everyday_Alba_and_Lio_Extreme_Lifestyles",
        "comment": "Everyday_Alba_and_Lio_Extreme_Lifestyles",
        "key": [
            "Cornelius Alba",
            "Alba",
            "Shirazumi Lio",
            "Lio Shirazumi",
            "Lio",
            "コルネリウス",
            "白純里緒"
        ],
        "keysecondary": [
            "clothing",
            "wardrobe",
            "coat",
            "dandy",
            "cane",
            "feral",
            "predator",
            "food",
            "cannibal",
            "wine",
            "habits",
            "routine",
            "slaughterhouse",
            "everyday",
            "lifestyle"
        ],
        "content": """<Everyday_Alba_and_Lio_Extreme_Lifestyles>
[EVERYDAY ANCHORS: CORNELIUS ALBA & SHIRAZUMI LIO — POLAR EXTREMES]

1. CORNELIUS ALBA (THE DANDY MAGUS ELITIST):
- Wardrobe & Appearance:
  * Extravagant European Frock Coat: Vivid crimson-red tailcoat, ruffled white silk cravat, double-breasted vest, tailored trousers, top hat/bowler, polished leather boots [CANON].
  * Grooming & Accessories: Pomaded hair, groomed pencil mustache, silver-topped walking cane concealing a thaumaturgical spell focus [CANON].
- Food & Drink Habits:
  * Pretentious High-Society Tastes: Claims expertise in vintage French wines, brandies, and gourmet European cuisine, consuming them primarily for status display [CANON]. Dislikes Japanese tea or common fare [INFERENCE].
- Habits & Demeanor:
  * Flamboyant, theatrical gestures, sweeping cape flourishes, and arrogant posture [CANON]. Deeply insecure; flies into hysterical rage when reminded of Touko's superior magical rank or when mocked [CANON].

2. SHIRAZUMI LIO (THE AWAKENED PREDATOR):
- Wardrobe & Appearance Evolution:
  * 1995 High School Era: Bland, neat school uniform, natural brown hair, timid demeanor, unremarkable student appearance [CANON].
  * 1999 Awakened Predator Era: Bleached, unkempt wild hair, bloodshot eyes, canine teeth elongated, torn dark jacket, filthy undershirt, worn jeans, often barefoot or in ruined sneakers [CANON].
- Food, Drink & Predatory Consumption:
  * Origin of Predation / Consumption (食べる): After his Origin awakened, he completely rejected normal human food [CANON]. Normal bread, cooked meat, or water makes him sick; he craves and ingests raw animal flesh, human blood, and cannibalistic meals [CANON]. Keeps stolen medical blood bags in his lair [CANON].
- Habits & Living Environment:
  * Nocturnal hunter; squats in derelict industrial meatpacking facilities and abandoned slaughterhouses in Mifune [CANON].
  * Smells of dried blood, animal musk, and copper [CANON]. Moves with an erratic, animalistic hunch, twitching nervously until he stalks his prey [CANON].
</Everyday_Alba_and_Lio_Extreme_Lifestyles>""",
        "constant": False,
        "selective": True,
        "selectiveLogic": 0,
        "order": 147,
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

    # Entry 8: Everyday_Enjou_Tomoe_Runaway_Life
    {
        "uid": 8,
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
            "running",
            "apartment",
            "Shiki",
            "habits",
            "routine",
            "everyday",
            "lifestyle"
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
        "order": 148,
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

    # Entry 9: Everyday_Fujou_Kirie_and_Kurogiri_Satsuki
    {
        "uid": 9,
        "name": "Everyday_Fujou_Kirie_and_Kurogiri_Satsuki",
        "comment": "Everyday_Fujou_Kirie_and_Kurogiri_Satsuki",
        "key": [
            "Fujou Kirie",
            "Kirie Fujou",
            "Kurogiri Satsuki",
            "Satsuki Kurogiri",
            "Kirie",
            "巫条霧絵",
            "玄霧皐月"
        ],
        "keysecondary": [
            "clothing",
            "wardrobe",
            "hospital",
            "suit",
            "glasses",
            "food",
            "coffee",
            "tea",
            "habits",
            "routine",
            "window",
            "books",
            "everyday",
            "lifestyle"
        ],
        "content": """<Everyday_Fujou_Kirie_and_Kurogiri_Satsuki>
[EVERYDAY ANCHORS: FUJOU KIRIE & KUROGIRI SATSUKI — ISOLATION & SCHOLARSHIP]

1. FUJOU KIRIE (THE BEDRIDDEN SPECTER):
- Wardrobe & Appearance:
  * Physical Form: Plain white cotton hospital gown in the Fujou terminal ward [CANON]. Frail, skeletal frame; pale, translucent skin; long, tangled black hair strewn over pillows [CANON]. Blinded/diminished eyesight, sunken dark eyes [CANON].
  * Double / Astral Form: Floating ghostly maiden in a pristine white gown drifting over the abandoned Fujou Building at sunset [CANON].
- Food & Daily Existence:
  * Hospital Care: Kept alive by medical intravenous drips and liquid nutrients; has spent years unable to sit at a dinner table, prepare food, or enjoy flavors [CANON - CONFIRMED NONE].
  * Routine: Lying motionless in the sterile white hospital room, listening to rain against the glass, and staring out the window at the distant city skyline with intense longing and envy [CANON].

2. KUROGIRI SATSUKI (THE SCHOLAR OF GOD'S WORD):
- Wardrobe & Appearance:
  * Intellectual Academic Ensemble: Meticulously pressed charcoal-grey wool suits, white spread-collar shirts, muted dark silk ties, tailored overcoats, and round wire-rimmed spectacles [CANON]. Polished dark leather dress shoes; carries a classic brown leather briefcase [CANON].
- Food & Drink Habits:
  * Modest Café Patron: Enjoys quiet corner tables in academic coffeehouses; drinks plain black drip coffee or unsweetened black tea while reading ancient linguistics texts [CANON]. Eats light, unhurried meals [INFERENCE].
- Habits & Social Demeanor:
  * Speaks in a tranquil, measured, hypnotic cadence (wielding the Unified Language) [CANON]. Unflappable composure, gentle academic smile, and deep respect for literature and memory archives [CANON].
</Everyday_Fujou_Kirie_and_Kurogiri_Satsuki>""",
        "constant": False,
        "selective": True,
        "selectiveLogic": 0,
        "order": 149,
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

    # Entry 10: Everyday_Mifune_City_Atmosphere_and_Living_Spaces
    {
        "uid": 10,
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
            "living space",
            "sensory"
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
        "order": 150,
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

    # Entry 11: Everyday_Garan_no_Dou_Daily_Operations
    {
        "uid": 11,
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
            "daily life",
            "day"
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
        "order": 151,
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

    # Entry 12: Everyday_Fate_Crossover_Emiya_Household_Kitchen
    {
        "uid": 12,
        "name": "Everyday_Fate_Crossover_Emiya_Household_Kitchen",
        "comment": "Everyday_Fate_Crossover_Emiya_Household_Kitchen",
        "key": [
            "Emiya household",
            "Emiya Shirou",
            "Shirou Emiya",
            "Saber",
            "Sakura Matou",
            "cooking Fate"
        ],
        "keysecondary": [
            "kitchen",
            "food",
            "breakfast",
            "dinner",
            "bento",
            "appetite",
            "rice",
            "miso soup",
            "habits",
            "routine",
            "domestic",
            "crossover",
            "table"
        ],
        "content": """<Everyday_Fate_Crossover_Emiya_Household_Kitchen>
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
</Everyday_Fate_Crossover_Emiya_Household_Kitchen>""",
        "constant": False,
        "selective": True,
        "selectiveLogic": 0,
        "order": 152,
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

    # Entry 13: Everyday_Fate_Crossover_Wardrobe_and_Downtime
    {
        "uid": 13,
        "name": "Everyday_Fate_Crossover_Wardrobe_and_Downtime",
        "comment": "Everyday_Fate_Crossover_Wardrobe_and_Downtime",
        "key": [
            "Tohsaka Rin",
            "Archer",
            "Emiya Shirou",
            "Saber",
            "crossover everyday"
        ],
        "keysecondary": [
            "clothing",
            "wardrobe",
            "turtleneck",
            "tea",
            "chores",
            "workshop",
            "electronics",
            "downtime",
            "habits",
            "routine",
            "lifestyle"
        ],
        "content": """<Everyday_Fate_Crossover_Wardrobe_and_Downtime>
[CROSSOVER DOMESTIC ANCHOR: DOWNTIME, WARDROBES & APPLIANCE DISASTERS]

1. TOHSAKA RIN'S EVERYDAY LIFE & IDIOSYNCRASIES:
- Iconic Wardrobe: Signature crimson turtleneck sweater, black pleated mini-skirt, black thigh-high stockings, dark leather shoes, black ribbons in twin-tails [CANON]. Homurahara uniform worn with red wool coat [CANON].
- Culinary Preferences: Highly skilled cook of savory Chinese cuisine (spicy mapo tofu, fried rice, stir-fried pork) [CANON]. Connoisseur of premium black tea (Earl Grey, Darjeeling) brewed from loose leaves in porcelain teapots [CANON]. Secretly loves morning buttered toast [CANON].
- Tech Incompetence: Completely hopeless with modern electronics (VCRs, microwaves, computers, recording decks); frequently short-circuits appliances in flustered frustration [CANON].
- Sleep Habits: Severe night owl studying jewel magecraft in her basement workshop; groggy and irritable before her morning tea [CANON].

2. ARCHER (EMIYA) — DOMESTIC PERFECTIONIST:
- Wardrobe: Red holy shroud over black tactical body armor; in civilian downtime, wears a fitted black turtleneck, dark slacks, and a clean kitchen apron [CANON].
- Gourmet Standards: Secretly an elite gourmet chef and barista, rivaling and exceeding Shirou in complex European pastries, tea blending, and multi-step sauces [CANON].
- Chores & Quips: Meticulously washes dishes, sweeps tatami, and repairs household carpentry while delivering dry, sarcastic remarks about Shirou's naive idealism [CANON].

3. CROSSOVER DIALOGUE & CULTURAL CONTRASTS:
- Rin & Touko: Two elite, stylish modern magi sparring over Clock Tower politics, finances, and tea while maintaining glamorous composure [CANON].
- Saber & Shiki: Silent recognition between two women bound to blades; relaxing on opposite ends of a porch in comfortable silence [CANON].
</Everyday_Fate_Crossover_Wardrobe_and_Downtime>""",
        "constant": False,
        "selective": True,
        "selectiveLogic": 0,
        "order": 153,
        "position": 0,
        "disable": False,
        "ignoreBudget": False,
        "excludeRecursion": True,
        "preventRecursion": True,
        "probability": 100,
        "useProbability": True,
        "depth": 4,
        "displayIndex": 13
    }
]

# Write JSON
json_output = {
    "name": "Kara_no_Kyoukai_16_Everyday_Life_and_Personal_Details",
    "description": "Comprehensive everyday human characterization module for Kara no Kyoukai and Fate crossover roleplay. Details canonical wardrobes, seasonal clothing, food and drink preferences, domestic routines, personal spaces, sensory environments, and subtle social behaviors across all major cast members with strict distinction between [CANON], [INFERENCE], and [RP SUGGESTION].",
    "scan_depth": 50,
    "token_budget": 50000,
    "recursive_scanning": False,
    "extensions": {},
    "entries": {str(e["uid"]): e for e in entries_data}
}

json_path = "Kara No/16_Everyday_Life_and_Personal_Details.json"
with open(json_path, "w", encoding="utf-8") as f:
    json.dump(json_output, f, ensure_ascii=False, indent=2)

print(f"Successfully created {json_path} with {len(entries_data)} entries.")

# Write Research Notes Markdown
md_content = """# Kara no Kyoukai & Fate Crossover: Everyday Life and Personal Details Research Notes
**Companion Documentation for `16_Everyday_Life_and_Personal_Details.json`**

---

## 1. Executive Summary & Source Hierarchy

This research document provides the canonical evidence, textual analysis, and evidentiary tagging for `16_Everyday_Life_and_Personal_Details.json`. While previous modules focused on thaumaturgical cosmology, combat mechanics, psychological trauma, and narrative guardrails, this module establishes **everyday human characterization**—the sensory, domestic, culinary, and sartorial realities that make characters feel alive in natural roleplay.

### Primary Source Hierarchy:
1. **Original Light Novels (Kinoko Nasu / Kodansha, 1998–2004)**:
   - *Kara no Kyoukai: The Garden of Sinners* (Chapters 1–7, Epilogue `「　」`).
   - *Mirai Fukuin* (Future Gospel) & *Extra Chorus*.
2. **Official Film Adaptations (Ufotable / Aniplex, 2007–2013)**:
   - Theatrical Movies 1–7, *Epilogue*, and *Mirai Fukuin*.
3. **Official Type-Moon Character & Reference Materials**:
   - *Kara no Kyoukai Material* (Type-Moon, 2008).
   - *Type-Moon Character Material* (2006).
   - *Fate/stay night Visual Novel & Fate/side material* (2004).
   - *Today's Menu for the Emiya Family (Emiya-san Chi no Kyou no Gohan)* (official domestic canon reference).

### Evidentiary Standard Tags:
- `[CANON]`: Explicitly documented in primary source texts, visual designs, or official Type-Moon material.
- `[INFERENCE]`: Logical, cautious deductions derived directly from established psychological states or historical contexts.
- `[RP SUGGESTION]`: Optional, non-conflicting flavor details designed to enrich everyday roleplay scenes without violating canon.
- `[CANON - UNKNOWN]`: Explicit acknowledgement when canon provides no established preference, preventing artificial fabrication.

---

## 2. Character-by-Character Evidentiary Audit

### 1. Ryougi Shiki (両儀式)
- **Wardrobe & Personal Style**:
  - `[CANON]`: Wears an unpatterned light blue (mizuiro) or pale white kimono under a single-rider red leather motorcycle jacket, paired with laced dark brown leather boots.
  - `[CANON]`: Self-cut rough chin-length bob done with a folding knife in June 1998 in Yagami Hospital. Never styles her hair or uses accessories/makeup.
  - `[CANON]`: Wears white hospital gown during 1996–1998 coma; wore dark high school blazer uniform or formal dark kimono with winter scarf prior to 1996.
  - `[CANON]`: Habitually keeps both hands buried deep inside her leather jacket pockets and pulls her collar over her chin when embarrassed or flustered.
- **Food & Beverage Preferences**:
  - `[CANON]`: Häagen-Dazs strawberry ice cream cups (specifically purchased by Mikiya; accepts it with feigned indifference).
  - `[CANON]`: Strawberry Pocky (frequently held or eaten while brooding).
  - `[CANON]`: Warmed canned black coffee from street vending machines in winter; canned green tea; hot barley tea brewed by Mikiya.
  - `[CANON]`: Completely lacks culinary skills. Kitchen is almost unused except for a water kettle; survives on convenience store buns and instant ramen unless Mikiya brings food.
  - `[CANON - UNKNOWN]`: Alcohol preferences (none established in canon; does not drink casually).
- **Routines & Living Space**:
  - `[CANON]`: Severe night owl; wanders deserted Mifune streets between 1:00 AM and 4:00 AM in rain or snow.
  - `[CANON]`: Room 404 municipal apartment: minimalist tatami, unadorned white walls, empty fridge, folding knife in jacket, Kanesada katana in closet, unlocked door for Mikiya.

---

### 2. Kokutou Mikiya (黒桐幹也)
- **Wardrobe & Personal Style**:
  - `[CANON]`: Modest dark wool coats, hand-knitted woolen sweaters, collared shirts, dark slacks, brown/black leather walking shoes. Round black-rimmed spectacles.
  - `[CANON]`: Long knitted scarf in winter (tucks chin into it when teased). Always carries a long umbrella when rain is possible.
  - `[CANON]`: Permanently blinded in left eye in February 1999 (Shirazumi Lio incident); hair parted forward, later uses eyepatch/tinted lens.
  - `[CANON]`: Faint scent of fresh rain and clean unscented soap.
- **Food & Beverage Preferences**:
  - `[CANON]`: Master coffee brewer; grinds beans manually at Garan no Dou; prepares custom espresso and drip for Touko.
  - `[CANON]`: Skilled in wholesome Japanese home cooking (nikujaga stew, miso soup, balanced bento boxes); cooks for Shiki and stocks her fridge.
  - `[CANON]`: Impeccable table manners; always expresses sincere gratitude before and after meals.
  - `[INFERENCE]`: Modest, content with simple home cooking; has no gourmet snobbery.
- **Routines & Living Space**:
  - `[CANON]`: Cleans glasses on sweater/tie hem when thoughtful or embarrassed.
  - `[CANON]`: Modest bachelor apartment filled with regional archives, directories, and books. Meticulous miniature handwriting.
  - `[CANON]`: Domestic caretaker of Garan no Dou (cleans, sorts mail, manages receipts, prepares coffee).

---

### 3. Aozaki Touko (蒼崎橙子)
- **Wardrobe & Personal Style**:
  - `[CANON]`: Tailored dark turtlenecks, high-waisted trousers, long beige/charcoal duster coats, stylish boots, manicured nails, auburn chignon/bob.
  - `[CANON]`: Amber/orange round spectacles function as the optical personality toggle:
    * Glasses ON: Friendly, sarcastic, worldly designer/architect.
    * Glasses OFF: Terrifying Grand-rank sealing designation puppet master.
  - `[CANON]`: Lethal taboo trigger: Instant homicidal rage if addressed by her hated title "Dirty Red" (傷んだ赤色).
- **Food, Vices & Living Space**:
  - `[CANON]`: Heavy chain smoker of European imported cigarettes (Sobranie Black Russian, Gitanes, Gauloises); uses silver case and lighter.
  - `[CANON]`: Heavy black coffee and espresso drinker.
  - `[CANON]`: Often skips meals during dollmaking benders; relies on Mikiya to bring take-out or bento; indulges in expensive dining when commissions arrive.
  - `[CANON - UNKNOWN]`: Favorite dessert (none established).
  - `[CANON]`: Garan no Dou studio: 4th floor unfinished open loft, exposed concrete, tall frameless glass windows, mahogany desk, leather sofa, crates of porcelain limbs and doll armatures.

---

### 4. SHIKI (Male Persona) & Void Shiki (「　」)
- **SHIKI (Male, Pre-1996)**:
  - `[CANON]`: High school uniform worn unbuttoned and loose; dark male yukata at Ryougi manor. Does NOT wear the red leather jacket.
  - `[CANON]`: Long black hair tied back loosely; bright, disarming smile; fluid boyish posture; casual male pronoun *ore* (オレ).
  - `[CANON]`: Hearty adolescent appetite; enjoys canned drinks and shared café snacks with Mikiya. Favorite sweet: `[CANON - UNKNOWN]`.
- **Void Shiki (`「　」`)**:
  - `[CANON]`: Pure-white silk furisode kimono, dark obi, barefoot or simple zori in snow; no modern leather jacket, boots, or weapons.
  - `[CANON]`: Awakens only during still winter nights (~3:00 AM) on snow-covered roads flanked by bamboo.
  - `[CANON]`: Does not require food; appreciates the aesthetic idea of warm tea or a fleeting sweet.
  - `[CANON]`: Soft maternal/divine presence, musical refined feminine speech (*watashi*), contemplative poetic demeanor.

---

### 5. Kokutou Azaka (黒桐鮮花)
- **Wardrobe & Habits**:
  - `[CANON]`: Reien Girls' Academy navy-blue sailor dress uniform with pleated skirt and white collar. Outside school: stylish modern teenage skirts, coats, boots.
  - `[CANON]`: Conceals salamander-skin ignition gloves in her school satchel.
  - `[CANON]`: Exceptional domestic cook (trained specifically to take care of Mikiya). Bakes sweets and prepares bentos.
  - `[CANON]`: Raids Mikiya's apartment on weekends to aggressively clean, iron ties, and cook.
  - `[CANON]`: Fierce tsundere dynamic with Shiki; deeply jealous of Shiki's connection to Mikiya.

---

### 6. Asagami Fujino (浅上藤乃)
- **Wardrobe & Sensory Realities**:
  - `[CANON]`: Reien Girls' Academy uniform worn with perfect aristocratic modesty. Straight black hime cut hair with neat bangs.
  - `[CANON]`: Pre-July 1998 Congenital Analgesia: Complete sensory numbness; could not feel pain, temperature, or taste; ate meals purely out of social obligation.
  - `[CANON]`: Post-July 1998 / Bridge Sparing: Sensation restored; delicate appetite, physically fragile, handles cold/damp poorly.
  - `[CANON - UNKNOWN]`: Favorite dessert (none established).
  - `[CANON]`: Gentle, refined keigo honorifics; quiet, modest posture with hands folded over lap.

---

### 7. Araya Souren (荒耶宗蓮)
- **Wardrobe & Asceticism**:
  - `[CANON]`: Black Buddhist monk's kesa draped over a heavy dark modern coat; cropped black hair; stone-carved chiseled face.
  - `[CANON - CONFIRMED NONE]`: Absolute culinary asceticism. Eats plain boiled rice, dry grains, and water strictly to maintain his biological vessel. Zero culinary indulgences, sweets, alcohol, or smoking.
  - `[CANON]`: Resides in the concrete basement/mandala node of the Ogawa Apartments. Capable of standing motionless for days like a stone statue.
  - `[CANON]`: Deep bell-like baritone; speaks with solemn liturgical gravity ("What do you seek?").

---

### 8. Cornelius Alba & Shirazumi Lio
- **Cornelius Alba**:
  - `[CANON]`: Crimson-red frock coat, ruffled cravat, top hat, silver-topped cane (spell focus), groomed mustache.
  - `[CANON]`: Pretentious European dandy; drinks vintage wines and brandies for status display. Theatrical flourishes masking deep academic insecurity.
- **Shirazumi Lio**:
  - `[CANON]`: 1995: Plain, unremarkable schoolboy. 1999: Bleached wild hair, bloodshot eyes, canine teeth, tattered jacket, feral posture.
  - `[CANON]`: Origin of Predation/Consumption: Disgust toward normal food; craves and ingests raw meat, blood bags, and cannibalistic human flesh.
  - `[CANON]`: Squats in abandoned industrial slaughterhouses; smells of blood and copper.

---

### 9. Enjou Tomoe (臙条巴)
- **Wardrobe & Daily Realities**:
  - `[CANON]`: Red/yellow sports jacket, hoodie, baggy sweatpants, worn running sneakers. Wears his apartment key on a string around his neck.
  - `[CANON]`: Survives on cheap convenience store bento and cup ramen.
  - `[CANON]`: Core emotional memory: Mother's fried eggs (tamagoyaki)—confused over whether she made them sweet or salty in the Ogawa loop.
  - `[CANON]`: Compulsive runner when panicked. Slept on Shiki's tatami/couch for a month in Room 404.

---

### 10. Fujou Kirie & Kurogiri Satsuki
- **Fujou Kirie**:
  - `[CANON]`: Bedridden in white hospital gown in Fujou terminal ward. Pale skin, tangled hair on pillows.
  - `[CANON - CONFIRMED NONE]`: Maintained entirely on medical IV drips and liquid nutrition; has no everyday meals or food preferences.
  - `[CANON]`: Lies motionless staring out the window at the distant skyline.
- **Kurogiri Satsuki**:
  - `[CANON]`: Pressed dark wool suits, overcoats, wire-rimmed glasses, leather briefcase.
  - `[CANON]`: Enjoys quiet corner café tables with plain black coffee/tea while reading linguistics texts. Measured, hypnotic speech.

---

### 11. Fate Crossover Cast (Shirou, Saber, Rin, Archer, Sakura)
- **Emiya Shirou**:
  - `[CANON]`: Master chef of the Emiya household. Wakes at 5:00 AM; cooks traditional Japanese breakfasts; cleans kitchens meticulously.
- **Saber (Artoria)**:
  - `[CANON]`: Immense appetite; eats colossal portions with formal royal dignity and laser focus. Loves Shirou's cooking; dislikes junk food.
- **Tohsaka Rin**:
  - `[CANON]`: Red turtleneck, black mini-skirt, twin-tails. Skilled in Chinese cooking; brews fine black tea; completely hopeless with modern electronics.
- **Archer (EMIYA)**:
  - `[CANON]`: Professional gourmet baker and tea specialist; wears kitchen apron during downtime; perfectionist cleaner.
- **Matou Sakura**:
  - `[CANON]`: Specializes in Western home cooking (stews, hamburg steak, gratin, pastries); gentle table manners.

---

## 3. SillyTavern Retrieval Architecture & Keywords Strategy

To prevent spurious activations while ensuring robust contextual triggering:
1. **Character-Specific Dual Filtering**: Each entry pairs character primary keys (`key`: `['Ryougi Shiki', 'Shiki', ...]`) with specific domestic/everyday secondary keys (`keysecondary`: `['clothing', 'wardrobe', 'food', 'tea', 'apartment', 'habits', ...]`).
2. **Selective Logic (AND ANY, value 0)**: Ensures that combat or purely philosophical scenes mentioning "Shiki" do NOT drag in paragraph-long descriptions of strawberry ice cream or wardrobe details unless the conversation context warrants everyday details.
3. **Budget & Order**: Set to `order: 140–153` to integrate seamlessly after base profiles (10–40) and RP guides (120–139).
"""

md_path = "Kara No/16_Everyday_Life_Research_Notes.md"
with open(md_path, "w", encoding="utf-8") as f:
    f.write(md_content)

print(f"Successfully created {md_path}.")
