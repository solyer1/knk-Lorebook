# Thai First-Person Pronoun Consistency & Dialogue Discipline Report
**Project:** Nasuverse SillyTavern Lorebook (Kara no Kyoukai & Fate/stay night)  
**Date:** 2026-10-27  
**Status:** Permanent Constant Enforcement & Full "กู" Authorization Validated (100% Pass)  

---

## 1. Executive Summary & Root Cause Resolution

### The Issue: "กู is allow and it still typing ฉัน"
During live testing in SillyTavern, the user observed two critical issues:
1. **The AI was still typing `"ฉัน"` for male characters.**
2. **`"กู"` was artificially suppressed or feared by the model instead of being fully allowed and utilized for rough/combat dialogue.**

### Root Cause Analysis in SillyTavern
1. **Lorebook Deactivation (`constant: false`):**
   - In SillyTavern, entries with `"constant": false` only get injected into the prompt if their keyword triggers match recent chat messages.
   - All roleplay guide entries in `10_RP_Guide.json` were previously configured with `"constant": false`, `"selective": true`, and English-only keys (`"RP dialogue"`, `"speech rules"`).
   - When roleplaying in Thai (`ภาษาไทย`), none of these English meta-keys ever appeared in the chat. **The AI was generating responses without seeing the Thai pronoun rules in its prompt context at all.**
2. **Lack of Thai Triggers Across Character Cards:**
   - Every single character entry in `Kara No` and `Fate` had zero Thai name triggers (`"ชิโร่"`, `"มิกิยะ"`, `"ชิกิ"`, `"อาเชอร์"`), meaning character-specific dialogue constraints also failed to activate during Thai chat.
3. **Over-restriction of `"กู"`:**
   - `"กู"` was previously described as "strictly for serial killers/feral predators". When male characters engaged in rough banter, street fights, or heated combat, the model avoided `"กู"`, found `"ผม"` too polite, and defaulted back to `"ฉัน"`.

### The Solution Implemented
1. **Dedicated Permanent Constant Entries (`constant: true`, `selective: false`):**
   - Created dedicated constant entries that are **ALWAYS injected into every single prompt** in SillyTavern at `position: 0` (top of context, order: 99).
   - Applied to:
     * [`Kara No/10_RP_Guide.json` (Entry 9, UID 9)](file:///d:/Personalise/Homemad/Lorebook/Nasuverse/Kara%20No/10_RP_Guide.json)
     * [`Fate/main_fate-stay-night.json` (Entry 53, UID 53)](file:///d:/Personalise/Homemad/Lorebook/Nasuverse/Fate/main_fate-stay-night.json)
     * [`Fate/FATE SN RP.json` (Entry 69, UID 69)](file:///d:/Personalise/Homemad/Lorebook/Nasuverse/Fate/FATE%20SN%20RP.json)
   - Updated Entry 1 and Entry 8 in `10_RP_Guide.json` to `"constant": true, "selective": false`.
2. **Full Authorization & Normalization of `"กู"`:**
   - Explicitly authorized `"กู"` (1st-person) and `"มึง"` (2nd-person) as natural, standard Thai masculine pronouns for rough, aggressive, angry, fighting, delinquent, combat taunts, and crude peer banter.
3. **Thai Name Keyword Injection Across All Cards:**
   - Added native Thai character names (`"ชิกิ"`, `"มิกิยะ"`, `"ชิโร่"`, `"อาเชอร์"`, `"แลนเซอร์"`, `"ริน"`, `"เซเบอร์"`, `"อารายะ"`, `"ริโอ"`, `"โทโมเอะ"`, `"อัลบา"`, etc.) directly into entry `key` lists so entries activate seamlessly during Thai roleplay.

---

## 2. Character-Appropriate Masculine Pronoun Registers

| Register | Thai Pronoun | Usage Context & Guidelines | Example Characters |
| :--- | :--- | :--- | :--- |
| **Natural Default** | **Zero-Anaphora** (Omitted subject) | **The #1 natural default in Thai dialogue.** Omit the pronoun whenever the verb, action, or context makes the speaker clear. Eliminates repetitive pronoun stacking. | All characters (Mikiya, Shirou, Archer, Shiki, etc.) |
| **Rough / Aggressive / Combat** | **"กู"** (pair with **"มึง"**) | **FULLY ALLOWED AND NATURAL.** Use freely whenever male characters are angry, shouting, taunting, in combat, using vulgarity, in delinquent attitude, or in crude informal male banter. **NEVER replace rough speech with "ฉัน"!** | Lancer in combat, Shinji enraged, Awakened Lio, delinquent Tomoe, Shirou when enraged/clashing, Gilgamesh when furious. |
| **Polite / Gentle / Formal** | **"ผม"** | Reserved for civilized, gentle, respectful, or formal male dialogue. Avoid overusing in casual peer conversations. | Kokutou Mikiya (ordinary life), Kurogiri Satsuki, Shirou to elders/teachers, Alba (haughty dandyism). |
| **Casual / Friendly Peer** | **"เรา"** | Boyish, relaxed, friendly peer-level register among classmates, equals, or close companions. | Male SHIKI (to Mikiya), Shirou Emiya (to Rin / classmates), Enjou Tomoe. |
| **Archaic / Martial / Heroic** | **"ข้า"** | Ancient legends, proud mythological heroes, imperious magi, or solemn proclamations. | Cú Chulainn (Lancer), Gilgamesh, Araya Souren. |
| **Absolute Ban** | **"ฉัน"** | **STRICTLY FORBIDDEN FOR ALL MALE CHARACTERS.** Male characters must NEVER refer to themselves as "ฉัน" in dialogue, thoughts, or narration tags. | **All Male Characters** |
| **Female Exemption** | **"ฉัน"** | **FULLY PERMITTED FOR FEMALE CHARACTERS.** | Ryougi Shiki, Tohsaka Rin, Saber, Sakura Matou, Touko Aozaki, Azaka, Fujino. |

---

## 3. Dedicated Constant Directive Content

The following directive is now permanently active on every prompt generation via constant entries:

```text
<RP_Global_Thai_Pronoun_Discipline_and_Register_Laws>
[CRITICAL SYSTEM DIRECTIVE: THAI FIRST-PERSON PRONOUN LAWS]
This directive is permanent and applies to EVERY response generated in Thai.

1. ZERO TOLERANCE: MALE FIRST-PERSON "ฉัน" IS FORBIDDEN:
- In Thai dialogue, thoughts, and narration tags, MALE CHARACTERS MUST NEVER REFER TO THEMSELVES AS "ฉัน" (First-Person / สรรพนามบุรุษที่ 1).
- Never allow any male character (Mikiya, Shirou, SHIKI, Archer, Lancer, Gilgamesh, Araya, Lio, Alba, Tomoe, Shinji, etc.) to say "ฉัน". Using "ฉัน" for a male character breaks roleplay immersion.

2. "กู" IS FULLY ALLOWED AND NATURAL:
- "กู" (1st person) and "มึง" (2nd person) are 100% PERMITTED, VALID, and EXPECTED whenever male characters are:
  * Speaking roughly, aggressively, angrily, or with street delinquent attitudes (Shinji, delinquent Tomoe, street thugs).
  * Shouting, taunting, or clashing in combat (Lancer in battle, Gilgamesh enraged, combatants clashing).
  * In visceral predatory bloodlust (Awakened Shirazumi Lio).
  * Engaging in close, crude, or informal peer banter between close male companions or bitter rivals.
- NEVER sanitize or substitute rough male dialogue with "ฉัน"! Use "กู", zero-anaphora, or "ข้า" instead.

3. CHARACTER-APPROPRIATE MASCULINE FIRST-PERSON CHOICES:
- Zero-Anaphora (Omitted Subject): The #1 most natural default in Thai dialogue. Omit the pronoun completely when the action/verb makes the subject clear.
- "กู": Rough, angry, aggressive, vulgar, delinquent, combat taunts, or close informal banter. (FULLY ALLOWED)
- "ผม": Polite, gentle, civilized, respectful (Mikiya in daily life, Shirou to elders/seniors, Kurogiri, Alba's haughty affectation).
- "เรา": Casual, boyish, friendly peer (Shirou with Rin/classmates, SHIKI to Mikiya, Tomoe).
- "ข้า": Archaic, martial, heroic, proud, ancient figures (Lancer, Gilgamesh, Araya in solemn declarations).

4. FEMALE CHARACTERS FREELY USE "ฉัน":
- Female characters (Ryougi Shiki, Tohsaka Rin, Saber, Sakura Matou, Touko Aozaki, Azaka Kokutou, Fujino Asagami) MAY freely use "ฉัน" according to their character style.

5. PRESERVE ESTABLISHED SECOND-PERSON RULES:
- Mikiya addressing Shiki/SHIKI: Always "เธอ" or "ชิกิ", NEVER "นาย".
- SHIKI addressing Mikiya: May use "นาย".
- Shiki addressing Mikiya: Naturally calls him by name ("โคคุโตะ" / "มิกิยะ") or zero pronoun.
</RP_Global_Thai_Pronoun_Discipline_and_Register_Laws>
```

---

## 4. Regression Test Results (Updated Suite)

Automated regression suite: [`scratch/run_thai_pronoun_regression.py`](file:///d:/Personalise/Homemad/Lorebook/Nasuverse/scratch/run_thai_pronoun_regression.py)

```text
======================================================================
  NASUVERSE THAI FIRST-PERSON PRONOUN REGRESSION TEST SUITE
======================================================================

--- PHASE 1: Dialogue Scenario Algorithmic Regression Testing ---

  [PASS] SCENARIO_1: Mikiya speaking gently to Shiki
         Speaker: Kokutou Mikiya (male)
         Pronoun registers verified: ['ผม', 'zero-anaphora']
         Negative constraints verified (No ['ฉัน', 'ข้า', 'กู'])
  [PASS] SCENARIO_2: Male SHIKI teasing Mikiya in 1995
         Speaker: SHIKI (織) (male)
         Pronoun registers verified: ['เรา', 'zero-anaphora']
         Negative constraints verified (No ['ฉัน', 'ผม', 'ข้า', 'กู'])
  [PASS] SCENARIO_3: Shirou talking casually with Rin
         Speaker: Emiya Shirou (male)
         Pronoun registers verified: ['เรา', 'zero-anaphora']
         Negative constraints verified (No ['ฉัน', 'ข้า', 'กู'])
  [PASS] SCENARIO_4: Lancer speaking during combat
         Speaker: Cú Chulainn (Lancer) (male)
         Pronoun registers verified: ['ข้า', 'กู', 'zero-anaphora']
         Negative constraints verified (No ['ฉัน', 'ผม', 'เรา'])
  [PASS] SCENARIO_5: Archer making a sarcastic remark
         Speaker: Archer (EMIYA) (male)
         Pronoun registers verified: ['zero-anaphora']
         Negative constraints verified (No ['ฉัน', 'ผม'])
  [PASS] SCENARIO_6: Araya speaking solemnly
         Speaker: Araya Souren (male)
         Pronoun registers verified: ['ข้า', 'zero-anaphora']
         Negative constraints verified (No ['ฉัน', 'ผม', 'เรา', 'กู'])
  [PASS] SCENARIO_7: Female Shiki speaking to Mikiya
         Speaker: Ryougi Shiki (Female) (female)
         Pronoun registers verified: ['ฉัน', 'zero-anaphora']
         Negative constraints verified (No ['ผม', 'ข้า'])
  [PASS] SCENARIO_8: Male character rough/delinquent/predatory speech with 'กู'
         Speaker: Awakened Lio / Delinquent / Enraged Male (male)
         Pronoun registers verified: ['กู', 'zero-anaphora']
         Negative constraints verified (No ['ฉัน', 'ผม'])

Scenario Test Score: 8/8 Passed

--- PHASE 2: Static Rule Verification Across Lorebook Modules ---

  [PASS] Kara No/10_RP_Guide.json [Entry 1]: All target rule phrases and constant settings verified.
  [PASS] Kara No/10_RP_Guide.json [Entry 8]: All target rule phrases and constant settings verified.
  [PASS] Kara No/01_Shiki.json [Entry 1]: All target rule phrases and constant settings verified.
  [PASS] Kara No/02_Mikiya.json [Entry 3]: All target rule phrases and constant settings verified.
  [PASS] Kara No/02_Mikiya.json [Entry 4]: All target rule phrases and constant settings verified.
  [PASS] Kara No/04_Other_Characters.json [Entry 0]: All target rule phrases and constant settings verified.
  [PASS] Kara No/04_Other_Characters.json [Entry 3]: All target rule phrases and constant settings verified.
  [PASS] Kara No/04_Other_Characters.json [Entry 4]: All target rule phrases and constant settings verified.
  [PASS] Kara No/05_Relationships.json [Entry 0]: All target rule phrases and constant settings verified.
  [PASS] Kara No/011_Fate_Integration.json [Entry 3]: All target rule phrases and constant settings verified.
  [PASS] Kara No/011_Fate_Integration.json [Entry 6]: All target rule phrases and constant settings verified.
  [PASS] Kara No/13_Dialogue_Examples.json [Entry 0]: All target rule phrases and constant settings verified.
  [PASS] Kara No/13_Dialogue_Examples.json [Entry 7]: All target rule phrases and constant settings verified.
  [PASS] Fate/main_fate-stay-night.json [Entry 5]: All target rule phrases and constant settings verified.
  [PASS] Fate/main_fate-stay-night.json [Entry 11]: All target rule phrases and constant settings verified.
  [PASS] Fate/main_fate-stay-night.json [Entry 13]: All target rule phrases and constant settings verified.
  [PASS] Kara No/10_RP_Guide.json [Entry 9]: All target rule phrases and constant settings verified.
  [PASS] Fate/main_fate-stay-night.json [Entry 53]: All target rule phrases and constant settings verified.
  [PASS] Fate/FATE SN RP.json [Entry 69]: All target rule phrases and constant settings verified.

Static Rule Verification Score: 19/19 Passed

--- PHASE 3: Negative Assertion Search Across Entire Repository ---

  Checking for improper male 'ฉัน' authorizations across files...
  [PASS] Negative assertion verified: Zero unauthorized male 'ฉัน' permissions found in any lorebook.

======================================================================
  REGRESSION TEST SUMMARY:
  - Scenarios Tested: 8 (Passed: 8)
  - Rules Verified:   19 (Passed: 19)
  - Status:           ALL REGRESSION SUITES PASSED (100% SUCCESS)
======================================================================
```

- **JSON Repository Integrity:** Validated all 21 JSON files (717 entries) via [`scratch/validate_all_lorebooks.py`](file:///d:/Personalise/Homemad/Lorebook/Nasuverse/scratch/validate_all_lorebooks.py) with 100% syntactic and structural validity.
