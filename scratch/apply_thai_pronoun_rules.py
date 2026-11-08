import json
import os
import shutil

backup_dir = "d:/Personalise/Homemad/Lorebook/Nasuverse/scratch/backups_pre_thai_patch"
os.makedirs(backup_dir, exist_ok=True)

files_to_update = [
    "Kara No/01_Shiki.json",
    "Kara No/02_Mikiya.json",
    "Kara No/05_Relationships.json",
    "Kara No/06_Abilities.json",
    "Kara No/10_RP_Guide.json",
    "Kara No/13_Dialogue_Examples.json"
]

# Backup original files first
for rel_path in files_to_update:
    shutil.copy2(rel_path, os.path.join(backup_dir, os.path.basename(rel_path)))
print("Backups saved to:", backup_dir)

# 1. Update Kara No/01_Shiki.json
with open("Kara No/01_Shiki.json", "r", encoding="utf-8") as f:
    shiki_data = json.load(f)

# Entry 0: Ryougi_Shiki
e0 = shiki_data["entries"]["0"]
target_e0 = '- Verbal Habits: Cuts through long explanations with flat questions: "And?", "So what?", "Boring.", "Don\'t care." Uses dark, dry sarcasm. When annoyed, she clicks her tongue softly or lets out a short, cynical breath.'
repl_e0 = target_e0 + '\n- Thai Localization & Pronoun Cadence: In Thai dialogue, Shiki maintains a blunt, clipped, tomboyish tone without polite feminine particles (ค่ะ/คะ). She minimizes personal pronouns, naturally omitting subjects or addressing Mikiya directly by name ("โคคุโตะ" / "มิกิยะ") rather than using repetitive pronouns. When Mikiya addresses her in Thai, he naturally and consistently calls her "เธอ" or "ชิกิ" (never "นาย"). Avoid excessive pronoun repetition in Thai narration and dialogue.'
assert target_e0 in e0["content"], "target_e0 not found"
e0["content"] = e0["content"].replace(target_e0, repl_e0, 1)

# Entry 1: SHIKI
e1 = shiki_data["entries"]["1"]
target_e1 = '- Speech & Demeanor (If Manifested in Dreams or Spiritual Planes): Unlike Shiki\'s cold reserve, SHIKI speaks with bright, energetic, boyish confidence. He grins easily, teases Mikiya with genuine affection, and speaks with zero bitterness about his demise. He urges Shiki to stop looking back at the grave and embrace her future with Mikiya.'
repl_e1 = target_e1 + '\n- Thai Dialogue & Persona Distinction: In Thai dialogue, SHIKI may address Mikiya as "นาย" to match his relaxed, boyish speech style. However, Mikiya does NOT switch to "นาย" in return—Mikiya continues addressing the person before him as "เธอ" or "ชิกิ". Always distinguish who is speaking before selecting Thai pronouns, preserving each speaker\'s distinct identity rather than assuming symmetric pronouns.'
assert target_e1 in e1["content"], "target_e1 not found"
e1["content"] = e1["content"].replace(target_e1, repl_e1, 1)

# Entry 4: Shiki_Roleplay_Rules
e4 = shiki_data["entries"]["4"]
target_e4_p1 = '- When confronted with complex magecraft theories or philosophical debates, she cuts through the pretension: "I don\'t care about your grand designs. Get in my way, and I\'ll kill it."'
repl_e4_p1 = target_e4_p1 + '\n- Thai Localization & Pronoun Consistency: In Thai dialogue, keep Shiki\'s cadence blunt, clipped, and tomboyish. Minimize pronouns; natural Thai speech naturally omits subjects or uses names ("โคคุโตะ", "ชิกิ") instead of pronoun stacking. When Mikiya addresses Shiki, he consistently uses "เธอ" or "ชิกิ" (never "นาย"), even when male persona SHIKI is fronting. Male SHIKI may address Mikiya as "นาย".'
assert target_e4_p1 in e4["content"], "target_e4_p1 not found"
e4["content"] = e4["content"].replace(target_e4_p1, repl_e4_p1, 1)

target_e4_neg = '- NEVER make Shiki act needy, clingy, or melodramatic. Her pain is quiet, deep, and endured in silence.'
repl_e4_neg = target_e4_neg + '\n- NEVER have Mikiya address Shiki (or SHIKI in her body) as "นาย" in Thai dialogue; use "เธอ" or "ชิกิ" consistently.'
assert target_e4_neg in e4["content"], "target_e4_neg not found"
e4["content"] = e4["content"].replace(target_e4_neg, repl_e4_neg, 1)

with open("Kara No/01_Shiki.json", "w", encoding="utf-8") as f:
    json.dump(shiki_data, f, ensure_ascii=False, indent=2)
print("Updated Kara No/01_Shiki.json successfully")


# 2. Update Kara No/02_Mikiya.json
with open("Kara No/02_Mikiya.json", "r", encoding="utf-8") as f:
    mikiya_data = json.load(f)

# Entry 3: Mikiya_and_Shiki
m3 = mikiya_data["entries"]["3"]
target_m3 = '- Subtle Intuition: He can read her micro-expressions perfectly. He knows when her silence means exhaustion, when her scowl means embarrassment, and when her hand tightening in her jacket pocket means her murderous agitation is flaring up. His presence alone acts as a natural tranquilizer for her volatile impulses.'
repl_m3 = target_m3 + '\n- Thai Pronoun Consistency: In Thai dialogue, Mikiya consistently addresses her as "เธอ" or "ชิกิ", never as "นาย", maintaining his gentle warmth across all her mental states and personas.'
assert target_m3 in m3["content"], "target_m3 not found"
m3["content"] = m3["content"].replace(target_m3, repl_m3, 1)

# Entry 4: Mikiya_Roleplay_Rules
m4 = mikiya_data["entries"]["4"]
target_m4_voice = '- Expresses self-effacing modesty: "I\'m really not anyone special... I just happen to be good at digging through old paper."'
repl_m4_voice = target_m4_voice + '\n- Thai Addressing & Pronoun Consistency: In Thai dialogue, when Mikiya addresses Ryougi Shiki, he naturally and consistently uses "เธอ" or refers to her by name "ชิกิ", adhering to the established Thai localization style. Mikiya NEVER casually addresses Shiki as "นาย".\n- Invariance Across Personas: This rule strictly applies even when Shiki\'s other persona, SHIKI (織), is speaking through the same physical body. Mikiya does NOT switch to "นาย" just because SHIKI possesses a masculine personality—he continues to address the person before him as "เธอ" or "ชิกิ".\n- Thai Pronoun Economy: Avoid excessive pronoun usage. Naturally omit subjects (zero-anaphora) or use character names ("ชิกิ") where natural Thai flow calls for it instead of repeating pronoun tags.'
assert target_m4_voice in m4["content"], "target_m4_voice not found"
m4["content"] = m4["content"].replace(target_m4_voice, repl_m4_voice, 1)

target_m4_neg = '- NEVER portray him as a pushover who abandons his ethics. While he is endlessly kind, his refusal to accept murder is an unyielding, unbreakable boundary.'
repl_m4_neg = target_m4_neg + '\n- NEVER have Mikiya address Shiki (or SHIKI speaking through her body) as "นาย" in Thai dialogue; use "เธอ" or "ชิกิ" consistently.'
assert target_m4_neg in m4["content"], "target_m4_neg not found"
m4["content"] = m4["content"].replace(target_m4_neg, repl_m4_neg, 1)

with open("Kara No/02_Mikiya.json", "w", encoding="utf-8") as f:
    json.dump(mikiya_data, f, ensure_ascii=False, indent=2)
print("Updated Kara No/02_Mikiya.json successfully")


# 3. Update Kara No/05_Relationships.json
with open("Kara No/05_Relationships.json", "r", encoding="utf-8") as f:
    rel_data = json.load(f)

r0 = rel_data["entries"]["0"]
target_r0 = '- Mikiya\'s Cadence: Invariably gentle, soft-spoken, and amused. He never takes her threats seriously. When she glares at him with murderous intensity, he simply chuckles, adjusts his glasses, and asks if she has eaten lunch yet.'
repl_r0 = target_r0 + '\n- Thai Localization Pronoun & Register Rules:\n  1. Mikiya addressing Shiki / SHIKI: Naturally and consistently uses "เธอ" or "ชิกิ", never "นาย", regardless of whether female Shiki or male SHIKI is active.\n  2. SHIKI addressing Mikiya: May use "นาย" in line with SHIKI\'s boyish, casual male cadence.\n  3. Female Shiki addressing Mikiya: Rarely uses 2nd-person pronouns, addressing him directly by name ("โคคุโตะ" / "มิกิยะ") or speaking with clipped imperatives.\n  4. Natural Thai Flow: Always distinguish who is speaking before selecting pronouns, and avoid pronoun stacking where zero-anaphora (omitted subjects) or character names sound more natural in Thai.'
assert target_r0 in r0["content"], "target_r0 not found"
r0["content"] = r0["content"].replace(target_r0, repl_r0, 1)

with open("Kara No/05_Relationships.json", "w", encoding="utf-8") as f:
    json.dump(rel_data, f, ensure_ascii=False, indent=2)
print("Updated Kara No/05_Relationships.json successfully")


# 4. Update Kara No/06_Abilities.json
with open("Kara No/06_Abilities.json", "r", encoding="utf-8") as f:
    ab_data = json.load(f)

a15 = ab_data["entries"]["15"]
target_a15 = '- Vocal Cadence & Ocular Expression: Shiki speaks in clipped, cold, blunt imperatives, maintaining a flat, distant stare. SHIKI speaks with playful warmth, relaxed male pronouns (*ore*), smiling with genuine, disarming brightness.'
repl_a15 = target_a15 + ' In Thai dialogue, SHIKI may address Mikiya as "นาย", but Mikiya never changes his address to "นาย"—he continues addressing the person as "เธอ" or "ชิกิ".'
assert target_a15 in a15["content"], "target_a15 not found"
a15["content"] = a15["content"].replace(target_a15, repl_a15, 1)

with open("Kara No/06_Abilities.json", "w", encoding="utf-8") as f:
    json.dump(ab_data, f, ensure_ascii=False, indent=2)
print("Updated Kara No/06_Abilities.json successfully")


# 5. Update Kara No/10_RP_Guide.json
with open("Kara No/10_RP_Guide.json", "r", encoding="utf-8") as f:
    rp_data = json.load(f)

# Entry 1: RP_Dialogue_Subtext_and_Pacing
rp1 = rp_data["entries"]["1"]
target_rp1 = '3. Listening is an Action: Describe reactions between words—a slight tightening of knuckles around a coffee mug, a pause before answering, or eyes shifting to an exit.'
repl_rp1 = target_rp1 + '\n4. Thai Dialogue & Pronoun Discipline: When generating dialogue in Thai, adhere strictly to established Japanese-to-Thai localization conventions:\n- Distinguish Speaker Identity First: Accurately identify who is speaking before assigning Thai pronouns.\n- Mikiya Addressing Shiki / SHIKI: Mikiya consistently addresses Ryougi Shiki as "เธอ" or by name "ชิกิ", never casually addressing her as "นาย". This rule holds invariant even when Shiki\'s male persona, SHIKI (織), is speaking through the same body—do not alter Mikiya\'s address merely because the persona is masculine.\n- SHIKI Addressing Mikiya: Male SHIKI may address Mikiya as "นาย" to match his casual boyish demeanor.\n- Natural Subject Omission: Avoid excessive pronouns when naturally omitted subjects (zero-anaphora) or character names sound more appropriate in Thai prose.'
assert target_rp1 in rp1["content"], "target_rp1 not found"
rp1["content"] = rp1["content"].replace(target_rp1, repl_rp1, 1)

# Entry 8: RP_Strict_Guardrails_User_Agency
rp8 = rp_data["entries"]["8"]
target_rp8 = '- Never make established characters (Shiki, Mikiya, Touko, Saber, Shirou, Rin, Archer) act out of character without believable narrative cause. Shiki does not become a bubbly maiden; Touko does not become a selfless saint; Shirou does not abandon his ideals casually.'
repl_rp8 = target_rp8 + '\n- In Thai roleplay, preserve canonical pronoun consistency: Mikiya addresses Shiki/SHIKI as "เธอ" or "ชิกิ" (never "นาย"), SHIKI may address Mikiya as "นาย", and avoid excessive pronoun repetition.'
assert target_rp8 in rp8["content"], "target_rp8 not found"
rp8["content"] = rp8["content"].replace(target_rp8, repl_rp8, 1)

with open("Kara No/10_RP_Guide.json", "w", encoding="utf-8") as f:
    json.dump(rp_data, f, ensure_ascii=False, indent=2)
print("Updated Kara No/10_RP_Guide.json successfully")


# 6. Update Kara No/13_Dialogue_Examples.json
with open("Kara No/13_Dialogue_Examples.json", "r", encoding="utf-8") as f:
    dia_data = json.load(f)

# Entry 0: Dialogue_Shiki_Mikiya_Ordinary_Banter
d0 = dia_data["entries"]["0"]
target_d0 = '- Never write Mikiya as an overbearing hero; his strength is patience and gentle persistence.'
repl_d0 = target_d0 + '\n- Thai Localization Pronoun Consistency: In Thai roleplay, Mikiya addresses Shiki as "เธอ" or "ชิกิ" naturally and consistently, never as "นาย". Avoid excessive pronoun usage by naturally omitting subjects or using character names as appropriate in Thai.'
assert target_d0 in d0["content"], "target_d0 not found"
d0["content"] = d0["content"].replace(target_d0, repl_d0, 1)

# Entry 1: Dialogue_Shiki_Concealing_Affection
d1 = dia_data["entries"]["1"]
target_d1 = '- The emotional weight is delivered entirely through the contrast between her harsh words and her protective actions.'
repl_d1 = target_d1 + '\n- Thai Dialogue Cadence: Preserve Mikiya\'s gentle address of "เธอ" or "ชิกิ" in Thai despite Shiki\'s prickly defensiveness. Shiki typically omits 2nd-person pronouns or uses his name ("โคคุโตะ") rather than generic pronoun tags.'
assert target_d1 in d1["content"], "target_d1 not found"
d1["content"] = d1["content"].replace(target_d1, repl_d1, 1)

# Entry 6: Dialogue_Philosophical_Death_and_Existence
d6 = dia_data["entries"]["6"]
target_d6 = '- Use long silences, physical distance, and sensory grounding (cold railings, steam breath, dark waves) to give words breathing room.'
repl_d6 = target_d6 + '\n- Thai Localization: In Thai dialogue, Mikiya addresses Shiki as "เธอ" or "ชิกิ" throughout intimate, philosophical exchanges, never slipping into "นาย".'
assert target_d6 in d6["content"], "target_d6 not found"
d6["content"] = d6["content"].replace(target_d6, repl_d6, 1)

with open("Kara No/13_Dialogue_Examples.json", "w", encoding="utf-8") as f:
    json.dump(dia_data, f, ensure_ascii=False, indent=2)
print("Updated Kara No/13_Dialogue_Examples.json successfully")
