import json
import os

print("=== Starting Global Thai First-Person Consistency Patch ===")

# -------------------------------------------------------------
# 1. Kara No/10_RP_Guide.json
# -------------------------------------------------------------
rp_guide_path = "Kara No/10_RP_Guide.json"
with open(rp_guide_path, "r", encoding="utf-8") as f:
    rp_data = json.load(f)

# Entry 1: RP_Dialogue_Subtext_and_Pacing
entry_1 = rp_data["entries"]["1"]
old_c1 = entry_1["content"]

thai_rule_entry_1 = """4. Thai Dialogue & Pronoun Discipline: When generating dialogue in Thai, adhere strictly to established Japanese-to-Thai localization conventions:
- GLOBAL CORE RULE — MASCULINE FIRST-PERSON PRONOUN BAN ON "ฉัน":
  * In Thai dialogue and internal monologue, MALE CHARACTERS MUST NEVER REFER TO THEMSELVES AS "ฉัน" (First-Person Pronoun / สรรพนามบุรุษที่ 1 แทนตัวผู้พูด). "ฉัน" used by men sounds stilted, artificial, or feminine in roleplay.
  * FEMALE CHARACTERS (Ryougi Shiki, Tohsaka Rin, Saber, Touko Aozaki, Azaka, Fujino, Sakura) MAY freely use "ฉัน" where fitting to their personality.
  * Natural Subject Omission (Zero-Anaphora): Prioritize omitting the first-person subject altogether in Thai dialogue whenever the verb, action, or context makes the speaker clear. Do NOT mechanically force a pronoun into every sentence.
  * Approved Masculine First-Person Registers:
    1. "ผม": Polite, gentle, reserved, or civilized male speakers (Kokutou Mikiya in daily conversation, Kurogiri Satsuki as an academic, Shirou Emiya when addressing seniors or speaking politely).
    2. "เรา": Casual, boyish, peer-level, or familiar masculine voice (Male SHIKI with Mikiya, Shirou Emiya casually with peers like Rin, Enjou Tomoe).
    3. "ข้า": Archaic, legendary, imperious, martial, or ancient figures (Cú Chulainn / Lancer in battle, Gilgamesh, Araya Souren in solemn declarations).
    4. "กู": Strictly for rough, vulgar, or feral predators (Awakened Shirazumi Lio hunting in the slaughterhouse, street delinquents).
    5. Zero-Anaphora: Omit self-pronoun completely—often the most punchy, natural Thai cadence.
- 2nd-Person Address Consistency (Second-Person Pronouns / สรรพนามบุรุษที่ 2):
  * Mikiya Addressing Shiki / SHIKI: Mikiya consistently addresses Ryougi Shiki as "เธอ" or by name "ชิกิ", never casually addressing her as "นาย". This rule holds invariant even when Shiki's male persona, SHIKI (織), is speaking through the same body—do not alter Mikiya's address merely because the persona is masculine.
  * SHIKI Addressing Mikiya: Male SHIKI may address Mikiya as "นาย" to match his casual boyish demeanor.
  * Female Shiki Addressing Mikiya: Rarely uses 2nd-person pronouns, naturally calling him by name ("โคคุโตะ" / "มิกิยะ") or speaking with clipped imperatives."""

target_snippet_1 = """4. Thai Dialogue & Pronoun Discipline: When generating dialogue in Thai, adhere strictly to established Japanese-to-Thai localization conventions:
- Distinguish Speaker Identity First: Accurately identify who is speaking before assigning Thai pronouns.
- Mikiya Addressing Shiki / SHIKI: Mikiya consistently addresses Ryougi Shiki as "เธอ" or by name "ชิกิ", never casually addressing her as "นาย". This rule holds invariant even when Shiki's male persona, SHIKI (織), is speaking through the same body—do not alter Mikiya's address merely because the persona is masculine.
- SHIKI Addressing Mikiya: Male SHIKI may address Mikiya as "นาย" to match his casual boyish demeanor.
- Natural Subject Omission: Avoid excessive pronouns when naturally omitted subjects (zero-anaphora) or character names sound more appropriate in Thai prose."""

if target_snippet_1 in old_c1:
    entry_1["content"] = old_c1.replace(target_snippet_1, thai_rule_entry_1)
    print("✓ 10_RP_Guide.json [1] updated")
else:
    print("✗ 10_RP_Guide.json [1] snippet not found")

# Entry 8: RP_Strict_Guardrails_User_Agency
entry_8 = rp_data["entries"]["8"]
old_c8 = entry_8["content"]
target_snippet_8 = "- In Thai roleplay, preserve canonical pronoun consistency: Mikiya addresses Shiki/SHIKI as \"เธอ\" or \"ชิกิ\" (never \"นาย\"), SHIKI may address Mikiya as \"นาย\", and avoid excessive pronoun repetition."
replacement_8 = "- In Thai roleplay, preserve canonical pronoun discipline:\n  * Male characters MUST NEVER use \"ฉัน\" as a 1st-person self-reference; assign character-appropriate registers (\"ผม\", \"เรา\", \"ข้า\", or natural zero-anaphora). Female characters may use \"ฉัน\" normally.\n  * Mikiya addresses Shiki/SHIKI as \"เธอ\" or \"ชิกิ\" (never \"นาย\"), SHIKI may address Mikiya as \"นาย\", and avoid excessive pronoun repetition."

if target_snippet_8 in old_c8:
    entry_8["content"] = old_c8.replace(target_snippet_8, replacement_8)
    print("✓ 10_RP_Guide.json [8] updated")
else:
    print("✗ 10_RP_Guide.json [8] snippet not found")

with open(rp_guide_path, "w", encoding="utf-8") as f:
    json.dump(rp_data, f, ensure_ascii=False, indent=2)

# -------------------------------------------------------------
# 2. Kara No/01_Shiki.json
# -------------------------------------------------------------
shiki_path = "Kara No/01_Shiki.json"
with open(shiki_path, "r", encoding="utf-8") as f:
    shiki_data = json.load(f)

# Entry 0: Ryougi_Shiki
e0 = shiki_data["entries"]["0"]
target_s0 = r'''- Thai Localization & Pronoun Cadence: In Thai dialogue, Shiki maintains a blunt, clipped, tomboyish tone without polite feminine particles (ค่ะ/คะ). She minimizes personal pronouns, naturally omitting subjects or addressing Mikiya directly by name ("โคคุโตะ" / "มิกิยะ") rather than using repetitive pronouns. When Mikiya addresses her in Thai, he naturally and consistently calls her "เธอ" or "ชิกิ" (never "นาย"). Avoid excessive pronoun repetition in Thai narration and dialogue.'''
rep_s0 = r'''- Thai Localization & Pronoun Cadence: In Thai dialogue, Shiki maintains a blunt, clipped, tomboyish tone without polite feminine particles (ค่ะ/คะ). As a female speaker, Shiki may use "ฉัน" or naturally omit pronouns, addressing Mikiya directly by name ("โคคุโตะ" / "มิกิยะ"). When Mikiya addresses her in Thai, he naturally and consistently calls her "เธอ" or "ชิกิ" (never "นาย"). Avoid excessive pronoun repetition in Thai narration and dialogue.'''
if target_s0 in e0["content"]:
    e0["content"] = e0["content"].replace(target_s0, rep_s0)
    print("✓ 01_Shiki.json [0] updated")

# Entry 1: SHIKI
e1 = shiki_data["entries"]["1"]
target_s1 = r'''- Thai Dialogue & Persona Distinction: In Thai dialogue, SHIKI may address Mikiya as "นาย" to match his relaxed, boyish speech style. However, Mikiya does NOT switch to "นาย" in return—Mikiya continues addressing the person before him as "เธอ" or "ชิกิ". Always distinguish who is speaking before selecting Thai pronouns, preserving each speaker's distinct identity rather than assuming symmetric pronouns.'''
rep_s1 = r'''- Thai Dialogue & Persona Distinction: In Thai dialogue, male SHIKI must NEVER refer to himself as "ฉัน" (1st-person pronoun). He uses relaxed, boyish self-references like "เรา" or naturally omits the subject (zero-anaphora); avoid "ผม" (too polite/formal for his boyish demeanor). When addressing Mikiya (2nd-person pronoun), SHIKI may use "นาย". Conversely, Mikiya does NOT switch to "นาย" in return—Mikiya continues addressing the person before him as "เธอ" or "ชิกิ". Always distinguish who is speaking before selecting Thai pronouns, preserving each speaker's distinct identity rather than assuming symmetric pronouns.'''
if target_s1 in e1["content"]:
    e1["content"] = e1["content"].replace(target_s1, rep_s1)
    print("✓ 01_Shiki.json [1] updated")

# Entry 4: Shiki_Roleplay_Rules
e4 = shiki_data["entries"]["4"]
target_s4 = r'''- Thai Localization & Pronoun Consistency: In Thai dialogue, keep Shiki's cadence blunt, clipped, and tomboyish. Minimize pronouns; natural Thai speech naturally omits subjects or uses names ("โคคุโตะ", "ชิกิ") instead of pronoun stacking. When Mikiya addresses Shiki, he consistently uses "เธอ" or "ชิกิ" (never "นาย"), even when male persona SHIKI is fronting. Male SHIKI may address Mikiya as "นาย".'''
rep_s4 = r'''- Thai Localization & Pronoun Consistency: In Thai dialogue, keep Shiki's cadence blunt, clipped, and tomboyish. Female Shiki may use "ฉัน" or naturally omit pronouns; she never uses polite feminine particles (ค่ะ/คะ). Male characters must NEVER refer to themselves as "ฉัน" in Thai dialogue. Male SHIKI uses "เรา" or natural subject omission (never "ฉัน", never formal "ผม"), and may address Mikiya as "นาย". When Mikiya addresses Shiki, he consistently uses "เธอ" or "ชิกิ" (never "นาย"), even when male persona SHIKI is fronting.'''
if target_s4 in e4["content"]:
    e4["content"] = e4["content"].replace(target_s4, rep_s4)
    print("✓ 01_Shiki.json [4] updated")

with open(shiki_path, "w", encoding="utf-8") as f:
    json.dump(shiki_data, f, ensure_ascii=False, indent=2)

# -------------------------------------------------------------
# 3. Kara No/02_Mikiya.json
# -------------------------------------------------------------
mikiya_path = "Kara No/02_Mikiya.json"
with open(mikiya_path, "r", encoding="utf-8") as f:
    mikiya_data = json.load(f)

# Entry 3: Mikiya_and_Shiki
me3 = mikiya_data["entries"]["3"]
target_me3 = '- Thai Pronoun Consistency: In Thai dialogue, Mikiya consistently addresses her as "เธอ" or "ชิกิ", never as "นาย", maintaining his gentle warmth across all her mental states and personas.'
rep_me3 = '- Thai Pronoun Consistency: In Thai dialogue, Mikiya refers to himself using polite, gentle "ผม" or naturally omits the pronoun (zero-anaphora); he NEVER refers to himself as "ฉัน". When addressing Shiki, he consistently addresses her as "เธอ" or "ชิกิ", never as "นาย", maintaining his gentle warmth across all her mental states and personas.'
if target_me3 in me3["content"]:
    me3["content"] = me3["content"].replace(target_me3, rep_me3)
    print("✓ 02_Mikiya.json [3] updated")

# Entry 4: Mikiya_Roleplay_Rules
me4 = mikiya_data["entries"]["4"]
target_me4 = """- Thai Addressing & Pronoun Consistency: In Thai dialogue, when Mikiya addresses Ryougi Shiki, he naturally and consistently uses "เธอ" or refers to her by name "ชิกิ", adhering to the established Thai localization style. Mikiya NEVER casually addresses Shiki as "นาย".
- Invariance Across Personas: This rule strictly applies even when Shiki's other persona, SHIKI (織), is speaking through the same physical body. Mikiya does NOT switch to "นาย" just because SHIKI possesses a masculine personality—he continues to address the person before him as "เธอ" or "ชิกิ".
- Thai Pronoun Economy: Avoid excessive pronoun usage. Naturally omit subjects (zero-anaphora) or use character names ("ชิกิ") where natural Thai flow calls for it instead of repeating pronoun tags."""

rep_me4 = """- Thai Addressing & Pronoun Discipline:
  * First-Person Self-Reference: Mikiya refers to himself using polite, gentle "ผม" or naturally omits the pronoun entirely (zero-anaphora). Mikiya MUST NEVER use "ฉัน" to refer to himself.
  * Addressing Shiki: When Mikiya addresses Ryougi Shiki, he naturally and consistently uses "เธอ" or refers to her by name "ชิกิ", adhering to established Thai localization style. Mikiya NEVER casually addresses Shiki as "นาย".
  * Invariance Across Personas: This rule strictly applies even when Shiki's other persona, SHIKI (織), is speaking through the same physical body. Mikiya does NOT switch to "นาย" just because SHIKI possesses a masculine personality—he continues to address the person before him as "เธอ" or "ชิกิ".
  * Thai Pronoun Economy: Avoid excessive pronoun usage. Naturally omit subjects (zero-anaphora) or use character names ("ชิกิ") where natural Thai flow calls for it instead of repeating pronoun tags."""

if target_me4 in me4["content"]:
    me4["content"] = me4["content"].replace(target_me4, rep_me4)
    print("✓ 02_Mikiya.json [4] body updated")

target_me4_neg = '- NEVER have Mikiya address Shiki (or SHIKI speaking through her body) as "นาย" in Thai dialogue; use "เธอ" or "ชิกิ" consistently.'
rep_me4_neg = '- NEVER have Mikiya refer to himself as "ฉัน" in Thai dialogue; use "ผม" or omit the subject.\n- NEVER have Mikiya address Shiki (or SHIKI speaking through her body) as "นาย" in Thai dialogue; use "เธอ" or "ชิกิ" consistently.'
if target_me4_neg in me4["content"]:
    me4["content"] = me4["content"].replace(target_me4_neg, rep_me4_neg)
    print("✓ 02_Mikiya.json [4] negative constraints updated")

with open(mikiya_path, "w", encoding="utf-8") as f:
    json.dump(mikiya_data, f, ensure_ascii=False, indent=2)

# -------------------------------------------------------------
# 4. Kara No/04_Other_Characters.json
# -------------------------------------------------------------
other_path = "Kara No/04_Other_Characters.json"
with open(other_path, "r", encoding="utf-8") as f:
    other_data = json.load(f)

# 0: Araya_Souren
oe0 = other_data["entries"]["0"]
if "- Thai Dialogue Discipline:" not in oe0["content"]:
    oe0["content"] = oe0["content"].replace("</Araya_Souren>", "- Thai Dialogue Discipline: In Thai dialogue, Araya must NEVER refer to himself as \"ฉัน\". Use solemn, austere zero-anaphora (omitting subject) or archaic/imposing \"ข้า\" only when delivering heavy metaphysical proclamations. Never use casual pronouns.\n</Araya_Souren>")
    print("✓ 04_Other_Characters.json [0] Araya updated")

# 3: Cornelius_Alba
oe3 = other_data["entries"]["3"]
if "- Thai Dialogue Discipline:" not in oe3["content"]:
    oe3["content"] = oe3["content"].replace("</Cornelius_Alba>", "- Thai Dialogue Discipline: In Thai dialogue, Alba must NEVER refer to himself as \"ฉัน\". Use haughty, pretentious \"ผม\" dripping with aristocratic snobbery or grand \"ข้า\". Never use casual or feminine pronouns.\n</Cornelius_Alba>")
    print("✓ 04_Other_Characters.json [3] Alba updated")

# 4: Shirazumi_Lio
oe4 = other_data["entries"]["4"]
if "- Thai Dialogue Discipline:" not in oe4["content"]:
    oe4["content"] = oe4["content"].replace("</Shirazumi_Lio>", "- Thai Dialogue Discipline: In Thai dialogue, Lio must NEVER refer to himself as \"ฉัน\". In 1995 high school scenes, he uses timid, polite \"ผม\" or zero-anaphora. Post-awakening in 1999, his feral speech shifts to primal zero-anaphora, visceral snarling, or rough forms (\"กู\") during predatory bloodlust. Never use \"ฉัน\".\n</Shirazumi_Lio>")
    print("✓ 04_Other_Characters.json [4] Lio updated")

# 6: Enjou_Tomoe
oe6 = other_data["entries"]["6"]
if "- Thai Dialogue Discipline:" not in oe6["content"]:
    oe6["content"] = oe6["content"].replace("</Enjou_Tomoe>", "- Thai Dialogue Discipline: In Thai dialogue, Tomoe must NEVER refer to himself as \"ฉัน\". Uses natural zero-anaphora or casual boyish \"เรา\" with peers, and hesitant/polite \"ผม\" when speaking to Shiki or adults.\n</Enjou_Tomoe>")
    print("✓ 04_Other_Characters.json [6] Tomoe updated")

# 7: Kurogiri_Satsuki
oe7 = other_data["entries"]["7"]
if "- Thai Dialogue Discipline:" not in oe7["content"]:
    oe7["content"] = oe7["content"].replace("</Kurogiri_Satsuki>", "- Thai Dialogue Discipline: In Thai dialogue, Kurogiri must NEVER refer to himself as \"ฉัน\". Uses calm, refined academic \"ผม\" or natural zero-anaphora while speaking in the hypnotic cadence of the Unified Language.\n</Kurogiri_Satsuki>")
    print("✓ 04_Other_Characters.json [7] Kurogiri updated")

with open(other_path, "w", encoding="utf-8") as f:
    json.dump(other_data, f, ensure_ascii=False, indent=2)

# -------------------------------------------------------------
# 5. Kara No/05_Relationships.json
# -------------------------------------------------------------
rel_path = "Kara No/05_Relationships.json"
with open(rel_path, "r", encoding="utf-8") as f:
    rel_data = json.load(f)

re0 = rel_data["entries"]["0"]
old_re0 = re0["content"]
target_re0 = """- Thai Localization Pronoun & Register Rules:
  1. Mikiya addressing Shiki / SHIKI: Naturally and consistently uses "เธอ" or "ชิกิ", never "นาย", regardless of whether female Shiki or male SHIKI is active.
  2. SHIKI addressing Mikiya: May use "นาย" in line with SHIKI's boyish, casual male cadence.
  3. Female Shiki addressing Mikiya: Rarely uses 2nd-person pronouns, addressing him directly by name ("โคคุโตะ" / "มิกิยะ") or speaking with clipped imperatives.
  4. Natural Thai Flow: Always distinguish who is speaking before selecting pronouns, and avoid pronoun stacking where zero-anaphora (omitted subjects) or character names sound more natural in Thai."""

rep_re0 = """- Thai Localization Pronoun & Register Rules:
  1. Male First-Person Prohibition: Male characters MUST NEVER refer to themselves as "ฉัน" in Thai dialogue. Mikiya uses gentle "ผม" or natural zero-anaphora (never "ฉัน"). Male SHIKI uses boyish "เรา" or natural zero-anaphora (never "ฉัน", never formal "ผม"). Female Shiki may use "ฉัน" or omit pronouns normally.
  2. Mikiya addressing Shiki / SHIKI: Naturally and consistently uses "เธอ" or "ชิกิ", never "นาย", regardless of whether female Shiki or male SHIKI is active.
  3. SHIKI addressing Mikiya: May use "นาย" in line with SHIKI's boyish, casual male cadence.
  4. Female Shiki addressing Mikiya: Rarely uses 2nd-person pronouns, addressing him directly by name ("โคคุโตะ" / "มิกิยะ") or speaking with clipped imperatives.
  5. Natural Thai Flow: Always distinguish who is speaking before selecting pronouns, and avoid pronoun stacking where zero-anaphora (omitted subjects) or character names sound more natural in Thai."""

if target_re0 in old_re0:
    re0["content"] = old_re0.replace(target_re0, rep_re0)
    print("✓ 05_Relationships.json [0] updated")
else:
    print("✗ 05_Relationships.json [0] target not found")

with open(rel_path, "w", encoding="utf-8") as f:
    json.dump(rel_data, f, ensure_ascii=False, indent=2)

# -------------------------------------------------------------
# 6. Kara No/011_Fate_Integration.json
# -------------------------------------------------------------
fate_int_path = "Kara No/011_Fate_Integration.json"
with open(fate_int_path, "r", encoding="utf-8") as f:
    fate_int_data = json.load(f)

# Entry 3: Interaction_Rules_Shirou
fie3 = fate_int_data["entries"]["3"]
if "THAI DIALOGUE & PRONOUN DISCIPLINE" not in fie3["content"]:
    shirou_thai = """4. THAI DIALOGUE & PRONOUN DISCIPLINE:
- Shirou must NEVER refer to himself as "ฉัน" in Thai dialogue. As an earnest adolescent boy, Shirou naturally uses zero-anaphora (omitting the subject) or casual peer "เรา" with Rin, and polite "ผม" when speaking to Touko or elder magi. Female Shiki may address him bluntly as "นาย" or "เด็กน้อย" (kid) and can use "ฉัน" for herself."""
    fie3["content"] = fie3["content"].replace("</Interaction_Rules_Shirou>", shirou_thai + "\n</Interaction_Rules_Shirou>")
    print("✓ 011_Fate_Integration.json [3] Shirou updated")

# Entry 6: Interaction_Rules_Archer
fie6 = fate_int_data["entries"]["6"]
if "THAI DIALOGUE & PRONOUN DISCIPLINE" not in fie6["content"]:
    archer_thai = """4. THAI DIALOGUE & PRONOUN DISCIPLINE:
- Archer must NEVER refer to himself as "ฉัน" in Thai dialogue. He maintains a dry, mature, cynical adult masculine register—preferring natural zero-anaphora or masculine self-references appropriate to his worldly weariness. Female Shiki may use "ฉัน" or omit pronouns."""
    fie6["content"] = fie6["content"].replace("</Interaction_Rules_Archer>", archer_thai + "\n</Interaction_Rules_Archer>")
    print("✓ 011_Fate_Integration.json [6] Archer updated")

with open(fate_int_path, "w", encoding="utf-8") as f:
    json.dump(fate_int_data, f, ensure_ascii=False, indent=2)

# -------------------------------------------------------------
# 7. Kara No/13_Dialogue_Examples.json
# -------------------------------------------------------------
diag_path = "Kara No/13_Dialogue_Examples.json"
with open(diag_path, "r", encoding="utf-8") as f:
    diag_data = json.load(f)

# Entry 0: Dialogue_Shiki_Mikiya_Ordinary_Banter
de0 = diag_data["entries"]["0"]
target_de0 = '- Thai Localization Pronoun Consistency: In Thai roleplay, Mikiya addresses Shiki as "เธอ" or "ชิกิ" naturally and consistently, never as "นาย". Avoid excessive pronoun usage by naturally omitting subjects or using character names as appropriate in Thai.'
rep_de0 = """- Thai Dialogue Discipline & Banter Demonstration:
  * Male First-Person Rule: Male characters MUST NEVER refer to themselves as "ฉัน". Mikiya uses gentle "ผม" or naturally omits the pronoun (zero-anaphora).
  * 2nd-Person Address: Mikiya addresses Shiki as "เธอ" or by name "ชิกิ", never "นาย". Female Shiki may use "ฉัน" or naturally omit pronouns.
  * Thai Localization Sample Exchange:
    - Mikiya: "พยากรณ์บอกว่าฟ้าจะโปร่งจนถึงเที่ยงคืนแท้ ๆ ดันมาเจอฝนตกหนักเอาตรงหน้าสถานีพอดี..." (Natural subject omission, mild apologetic cadence; never "ฉัน").
    - Shiki: "เดินย่ำน้ำเข้ามาเฉยเลยนะ" (Low, flat; zero pronouns).
    - Mikiya: "ถอดรองเท้าบู้ทแล้วนะ ชิกิ" (Addresses her by name "ชิกิ", never "นาย").
    - Shiki: "อากาศมันชื้น... ไม่เห็นต้องดั้นด้นเดินมาแค่เพื่อจะบอกว่าฝนตกเลย"
    - Mikiya: "ซื้อไอศกรีมรสที่เธอชอบมาฝากด้วยนะ แล้วก็นึกว่าคงจะหิว... ตั้งแต่เช้าได้กินอะไรบ้างหรือยัง?" (Addresses her as "เธอ", omits self-pronoun; never "ฉัน" or "นาย")."""
if target_de0 in de0["content"]:
    de0["content"] = de0["content"].replace(target_de0, rep_de0)
    print("✓ 13_Dialogue_Examples.json [0] updated")

# Entry 7: Dialogue_Shiki_Fate_Shirou_Interaction
de7 = diag_data["entries"]["7"]
if "THAI LOCALIZATION DEMONSTRATION" not in de7["content"]:
    shirou_de7 = """[THAI LOCALIZATION DEMONSTRATION & PRONOUN DISCIPLINE]
- Shirou: "เดี๋ยวสิ—เดี๋ยวก่อน! บาดเจ็บตรงไหนหรือเปล่า? แล้วไอ้ตัวเมื่อกี้นี้มันคืออะไรกันแน่?" (Earnest, urgent; natural subject omission, never uses "ฉัน").
- Shiki: "ไม่ใช่เรื่องของนาย กลับบ้านไปซะ เจ้าหนู" (Blunt, tomboyish; addresses Shirou as "นาย" or "เจ้าหนู", may use "ฉัน" for herself).
- Shirou: "ไม่ใช่เด็กสักหน่อย! แถวนี้ตอนกลางคืนมันอันตรายนะ... ถ้ามีเรื่องแปลก ๆ เกิดขึ้น อย่าเดินคนเดียวสิ" (Defensive, stubborn; zero-anaphora, never "ฉัน").
- Shiki: "อันตรายกับใครกันแน่? นายเองนั่นแหละที่สั่นไปทั้งตัว..."
- Shirou: "เรื่องนั้นไม่เกี่ยวหรอก! ถึงจะไม่เก่ง แต่ถ้าเห็นคนกำลังตกอยู่ในอันตราย จะให้ทำเป็นไม่เห็นได้ยังไง!" (Fierce conviction without artificial self-pronouns; never "ฉัน").
- AI Takeaway: Shirou must NEVER refer to himself as "ฉัน". Use natural subject omission or "เรา" with peers, and "ผม" when speaking politely."""
    de7["content"] = de7["content"].replace("</Dialogue_Shiki_Fate_Shirou_Interaction>", shirou_de7 + "\n</Dialogue_Shiki_Fate_Shirou_Interaction>")
    print("✓ 13_Dialogue_Examples.json [7] updated")

# Entry 9: Dialogue_Respectful_Disagreement_Mikiya_Touko
de9 = diag_data["entries"]["9"]
if "Thai Dialogue Discipline" not in de9["content"]:
    touko_mikiya_thai = """- Thai Dialogue Discipline: Mikiya uses polite "ผม" or natural zero-anaphora when addressing his employer Touko, never "ฉัน". Touko as a female magus freely uses "ฉัน" or omits pronouns with worldly cynicism."""
    de9["content"] = de9["content"].replace("</Dialogue_Respectful_Disagreement_Mikiya_Touko>", touko_mikiya_thai + "\n</Dialogue_Respectful_Disagreement_Mikiya_Touko>")
    print("✓ 13_Dialogue_Examples.json [9] updated")

with open(diag_path, "w", encoding="utf-8") as f:
    json.dump(diag_data, f, ensure_ascii=False, indent=2)

# -------------------------------------------------------------
# 8. Kara No/16_Everyday_Life_and_Personal_Details.json
# -------------------------------------------------------------
everyday_path = "Kara No/16_Everyday_Life_and_Personal_Details.json"
with open(everyday_path, "r", encoding="utf-8") as f:
    ed_data = json.load(f)

# Entry 1: Kokutou Mikiya
ed1 = ed_data["entries"]["1"]
if "Thai Dialogue Discipline:" not in ed1["content"]:
    ed1["content"] = ed1["content"].replace("</Everyday_Kokutou_Mikiya_Habits_and_Domesticity>", "- Thai Dialogue Discipline: In Thai dialogue, Mikiya refers to himself as \"ผม\" or naturally omits the pronoun (zero-anaphora); he NEVER refers to himself as \"ฉัน\". Consistently addresses Shiki as \"เธอ\" or \"ชิกิ\" (never \"นาย\") [CANON].\n</Everyday_Kokutou_Mikiya_Habits_and_Domesticity>")
    print("✓ 16_Everyday_Life [1] Mikiya updated")

# Entry 3: Male SHIKI
ed3 = ed_data["entries"]["3"]
if "Thai Dialogue Discipline:" not in ed3["content"]:
    ed3["content"] = ed3["content"].replace("</Everyday_SHIKI_Male_Persona_1995>", "- Thai Dialogue Discipline: In Thai dialogue, male SHIKI must NEVER refer to himself as \"ฉัน\" (and avoids overly formal \"ผม\"). Uses relaxed boyish \"เรา\" or natural zero-anaphora; addresses Mikiya casually as \"นาย\" [CANON].\n</Everyday_SHIKI_Male_Persona_1995>")
    print("✓ 16_Everyday_Life [3] SHIKI updated")

# Entry 7: Araya Souren
ed7 = ed_data["entries"]["7"]
if "Thai Dialogue Discipline:" not in ed7["content"]:
    ed7["content"] = ed7["content"].replace("</Everyday_Araya_Souren_Monastic_Asceticism>", "- Thai Dialogue Discipline: In Thai dialogue, Araya must NEVER refer to himself as \"ฉัน\". Uses solemn zero-anaphora or imposing \"ข้า\" only when delivering heavy metaphysical proclamations [CANON].\n</Everyday_Araya_Souren_Monastic_Asceticism>")
    print("✓ 16_Everyday_Life [7] Araya updated")

# Entry 8: Cornelius Alba
ed8 = ed_data["entries"]["8"]
if "Thai Dialogue Discipline:" not in ed8["content"]:
    ed8["content"] = ed8["content"].replace("</Everyday_Cornelius_Alba_Dandyism>", "- Thai Dialogue Discipline: In Thai dialogue, Alba must NEVER refer to himself as \"ฉัน\". Uses pompous, aristocratic \"ผม\" or haughty \"ข้า\" dripping with snobbery [CANON].\n</Everyday_Cornelius_Alba_Dandyism>")
    print("✓ 16_Everyday_Life [8] Alba updated")

# Entry 9: Shirazumi Lio
ed9 = ed_data["entries"]["9"]
if "Thai Dialogue Discipline:" not in ed9["content"]:
    ed9["content"] = ed9["content"].replace("</Everyday_Shirazumi_Lio_Predator_Reality>", "- Thai Dialogue Discipline: In Thai dialogue, Lio must NEVER refer to himself as \"ฉัน\". In 1995 he uses timid \"ผม\" or zero-anaphora; in 1999 his awakened speech degrades into feral zero-anaphora or vulgar/rough forms (\"กู\") during bloodlust [CANON].\n</Everyday_Shirazumi_Lio_Predator_Reality>")
    print("✓ 16_Everyday_Life [9] Lio updated")

# Entry 10: Enjou Tomoe
ed10 = ed_data["entries"]["10"]
if "Thai Dialogue Discipline:" not in ed10["content"]:
    ed10["content"] = ed10["content"].replace("</Everyday_Enjou_Tomoe_Runaway_Life>", "- Thai Dialogue Discipline: In Thai dialogue, Tomoe must NEVER refer to himself as \"ฉัน\". Uses natural zero-anaphora or \"เรา\" with peers, and hesitant \"ผม\" with adults or Shiki [CANON].\n</Everyday_Enjou_Tomoe_Runaway_Life>")
    print("✓ 16_Everyday_Life [10] Tomoe updated")

# Entry 12: Kurogiri Satsuki
ed12 = ed_data["entries"]["12"]
if "Thai Dialogue Discipline:" not in ed12["content"]:
    ed12["content"] = ed12["content"].replace("</Everyday_Kurogiri_Satsuki_Linguist_Scholar>", "- Thai Dialogue Discipline: In Thai dialogue, Kurogiri must NEVER refer to himself as \"ฉัน\". Uses refined, calm academic \"ผม\" or natural zero-anaphora [CANON].\n</Everyday_Kurogiri_Satsuki_Linguist_Scholar>")
    print("✓ 16_Everyday_Life [12] Kurogiri updated")

# Entry 15: Fate Emiya Kitchen
ed15 = ed_data["entries"]["15"]
if "Thai Dialogue Discipline:" not in ed15["content"]:
    ed15["content"] = ed15["content"].replace("</Everyday_Fate_Crossover_Emiya_Kitchen>", "- Thai Dialogue Discipline: Shirou must NEVER refer to himself as \"ฉัน\" in Thai dialogue. Uses natural zero-anaphora or \"เรา\" with peers (Rin, classmates), and polite \"ผม\" with elders. Saber and Sakura may use \"ฉัน\" normally [CANON].\n</Everyday_Fate_Crossover_Emiya_Kitchen>")
    print("✓ 16_Everyday_Life [15] Emiya Kitchen updated")

# Entry 17: Fate Archer Domesticity
ed17 = ed_data["entries"]["17"]
if "Thai Dialogue Discipline:" not in ed17["content"]:
    ed17["content"] = ed17["content"].replace("</Everyday_Fate_Crossover_Archer_Domesticity>", "- Thai Dialogue Discipline: Archer must NEVER refer to himself as \"ฉัน\" in Thai dialogue. Uses dry, mature masculine cadence with natural subject omission (zero-anaphora) [CANON].\n</Everyday_Fate_Crossover_Archer_Domesticity>")
    print("✓ 16_Everyday_Life [17] Archer updated")

with open(everyday_path, "w", encoding="utf-8") as f:
    json.dump(ed_data, f, ensure_ascii=False, indent=2)

# -------------------------------------------------------------
# 9. Fate/main_fate-stay-night.json and Fate/FATE SN RP.json
# -------------------------------------------------------------
fate_files = ["Fate/main_fate-stay-night.json", "Fate/FATE SN RP.json"]
for fp in fate_files:
    if not os.path.exists(fp):
        continue
    with open(fp, "r", encoding="utf-8") as f:
        fd = json.load(f)

    # 5: Emiya_Shirou
    if "5" in fd["entries"]:
        fe5 = fd["entries"]["5"]
        if "THAI DIALOGUE & PRONOUN DISCIPLINE" not in fe5["content"]:
            shirou_rule = """\n[THAI DIALOGUE & PRONOUN DISCIPLINE]
In Thai dialogue, Shirou Emiya must NEVER refer to himself as "ฉัน" (1st-person self-reference). He speaks in a natural masculine adolescent register:
- Uses natural subject omission (zero-anaphora) as the primary default in everyday and combat dialogue.
- Uses casual peer "เรา" when speaking to classmates or familiar peers like Rin Tohsaka.
- Uses polite "ผม" when speaking to elders, teachers, or senior figures (e.g. Taiga, Kirei, Kiritsugu).
- Never use "ฉัน" for Shirou; "ฉัน" for male characters sounds stilted and unnatural in roleplay."""
            fe5["content"] = fe5["content"].replace("</Emiya_Shirou>", shirou_rule + "\n</Emiya_Shirou>")
            print(f"✓ {fp} [5] Shirou updated")

    # 11: Archer_EMIYA
    if "11" in fd["entries"]:
        fe11 = fd["entries"]["11"]
        if "THAI DIALOGUE & PRONOUN DISCIPLINE" not in fe11["content"]:
            archer_rule = """\n[THAI DIALOGUE & PRONOUN DISCIPLINE]
In Thai dialogue, Archer must NEVER refer to himself as "ฉัน" (1st-person self-reference). He maintains a cynical, mature, world-weary masculine cadence:
- Uses natural subject omission (zero-anaphora) for concise, cutting remarks and sarcastic banter.
- Never flatlines into generic polite "ผม" or stilted "ฉัน".
- When addressing Rin, speaks with dry familiarity while respecting the Master-Servant dynamic."""
            fe11["content"] = fe11["content"].replace("</Archer_EMIYA>", archer_rule + "\n</Archer_EMIYA>")
            print(f"✓ {fp} [11] Archer updated")

    # 13: Lancer_Cu_Chulainn
    if "13" in fd["entries"]:
        fe13 = fd["entries"]["13"]
        if "THAI DIALOGUE & PRONOUN DISCIPLINE" not in fe13["content"]:
            lancer_rule = """\n[THAI DIALOGUE & PRONOUN DISCIPLINE]
In Thai dialogue, Lancer (Cú Chulainn) must NEVER refer to himself as "ฉัน" (1st-person self-reference). He speaks in a bold, fierce, masculine warrior voice:
- Uses bold warrior self-reference "ข้า" or natural subject omission (zero-anaphora) during combat, banter, and drinks.
- Never use "ฉัน" or overly polite "ผม" for Lancer."""
            fe13["content"] = fe13["content"].replace("</Lancer_Cu_Chulainn>", lancer_rule + "\n</Lancer_Cu_Chulainn>")
            print(f"✓ {fp} [13] Lancer updated")

    with open(fp, "w", encoding="utf-8") as f:
        json.dump(fd, f, ensure_ascii=False, indent=2)

print("=== Global Thai First-Person Consistency Patch Completed Successfully ===")
