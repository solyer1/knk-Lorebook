# TARGETED RETRIEVAL MAINTENANCE — FINAL DELIVERY REPORT

**Date**: 2026-10-26  
**Target Repository**: `d:\Personalise\Homemad\Lorebook\Nasuverse\Kara No`  
**Status**: Maintenance Successfully Applied, Validated, and Benchmarked

---

## 1. PHASE 1: SILLYTAVERN CODEBASE IMPLEMENTATION VERIFICATION

Direct source inspection was performed on the active SillyTavern codebase (`D:\ST\SillyTavern\public\scripts\world-info.js`) to verify engine behavior against the QA simulator findings.

| Area Investigated | QA Simulation Finding | Live SillyTavern Implementation Reality | Verification Status | Maintenance Decision |
| :--- | :--- | :--- | :---: | :--- |
| **Case-Insensitive Matching** | `"Shiki"` matches `"SHIKI"` | Verified in `world-info.js` lines 345–346 (`#transformString`). Both haystack and needle execute `.toLowerCase()`. | **VERIFIED** | Disambiguation must NOT rely on capitalization alone. Constrained `SHIKI` with contextual filters in `keysecondary`. |
| **Selective Matching (`AND_ANY`)** | Requires 1 primary AND 1 secondary key match | Verified in `world-info.js` lines 4812–4846. If `keysecondary` is empty, secondary check is bypassed entirely. When populated with `selectiveLogic == 0`, requires `(Primary >= 1) AND (Secondary >= 1)`. | **VERIFIED** | Maintained `selective: true` and `selectiveLogic: 0` (`AND_ANY`) across all entries. Refined secondary keys rather than disabling selective logic. |
| **Insertion Order & Budget Allocation** | Higher order values appear earlier or claim budget differently | Verified in `world-info.js` lines 4508 and 4882. During budget check, entries sort in **descending order** (`b.order - a.order`). High-order entries (150) claim budget first. Prompt injection uses `unshift`, placing lower-order entries higher in text. | **VERIFIED** | Preserved the natural order hierarchy (Rules: 150, Mechanics: 140, Relationships: 130, Lore: 100, Base Profiles: 10–20). Recommending appropriate budget rather than inverting order values. |
| **Duplicate Entry Titles** | Causes duplicate activation | Verified in `world-info.js` line 4685. Activations are tracked by unique identifier `${entry.world}.${entry.uid}`. If two separate lorebooks contain an entry titled `"Merlin"`, both activate independently. | **VERIFIED** | Ensured no title or UID collisions within KnK modules. Noted legacy Fate cross-file duplicates for future Fate-focused maintenance. |
| **Reported vs. Live Token Counts** | Stress test reported 9,161 tokens in SC-13 | In live SillyTavern, prompt injection is strictly capped at `world_info_budget`. The 9,161 tokens represented the unconstrained potential activation pool, not the injected tokens. | **VERIFIED** | Clarified distinction: unconstrained activation causes low-order entries to starve under small budgets (2,048), rather than over-filling the context window. |

---

## 2. PHASE 2: MINIMAL PATCH EXECUTION SUMMARY

In accordance with maintenance directives, **zero Fate foundation files were touched**. All original files were backed up to `scratch/backups/`.

A total of **16 entries across 7 Kara no Kyoukai JSON files** were modified:

### 1. `01_Shiki.json`
- **`SHIKI` (UID 1)**
  - **Before**: `key: ["SHIKI", "male Shiki", "male personality", "Yang persona", "other Shiki"]` | `keysecondary: ["coma", "accident", "murder", "Ryougi", "Mikiya", "death", "past", "blood"]`
  - **After**: `key: ["male Shiki", "male personality", "Yang persona", "other Shiki", "Ryougi SHIKI", "SHIKI"]` | `keysecondary: ["male", "boy", "Yang", "1995", "split", "second personality", "other self", "bamboo", "bamboo grove", "impulse", "bloodlust", "truck", "knife", "rain road"]`
  - **Impact**: Completely eliminated spurious activations during female Shiki dialogue with Mikiya while ensuring reliable activation in 1995/dual-personality scenes.

### 2. `01_Shiki_Expansion.json`
- **`Shiki_Psychological_Defenses_and_Contradictions` (UID 0)**:
  - `key`: `["Ryougi Shiki", "Shiki Ryougi", "Shiki"]`
  - `keysecondary`: `["kindness", "warmth", "groceries", "tea", "deflection", "fear", "alone", "hollow", "feelings", "care", "soften", "vulnerability", "tsundere", "concern"]`
- **`Shiki_Solitary_Behavior_and_Daily_Habits` (UID 1)**:
  - `key`: `["Ryougi Shiki", "Shiki Ryougi", "Shiki"]`
  - `keysecondary`: `["apartment", "kimono", "leather jacket", "boots", "ice cream", "strawberry", "fridge", "solitary", "habits", "couch", "tea", "sleep", "routine", "wardrobe"]`
- **`Shiki_Chronological_Mindset_and_Memory_Phases` (UID 2)**:
  - `key`: `["Ryougi Shiki", "Shiki Ryougi", "Shiki"]`
  - `keysecondary`: `["1995", "1996", "1998", "1999", "coma", "awakening", "hospital", "Lio", "mindset", "phases", "development", "Room 404", "haircut"]`
- **`Void_Shiki_Cognitive_State_and_Conversational_Voice` (UID 3)**:
  - `key`: `["Void Shiki", "「　」", "Root Shiki", "third personality", "Void"]`
  - `keysecondary`: `["Akasha", "Root", "snow", "dream", "watashi", "furisode", "kimono", "dialogue", "voice", "epilogue", "bamboo", "speech"]`

### 3. `02_Mikiya.json`
- **`Mikiya_Kindness_and_Morality` (UID 1)**:
  - `key`: `["Kokutou Mikiya", "Mikiya Kokutou", "Mikiya", "killing vs murder", "Mikiya philosophy"]`
  - `keysecondary`: `["murder", "kill", "sin", "forgive", "kindness", "morality", "justice", "execution", "moral", "philosophy", "investigation"]`

### 4. `02_Mikiya_Expansion.json`
- **`Mikiya_Insecurities_and_Psychological_Limits` (UID 0)**:
  - `key`: `["Kokutou Mikiya", "Mikiya Kokutou", "Mikiya"]`
  - `keysecondary`: `["insecurity", "ordinary", "weakness", "normal", "guilt", "helpless", "frustration", "limits", "fear", "mediocre"]`
- **`Mikiya_Trauma_Response_and_Extreme_Situations` (UID 1)**:
  - `key`: `["Kokutou Mikiya", "Mikiya Kokutou", "Mikiya"]`
  - `keysecondary`: `["trauma", "danger", "torture", "blinding", "crushed eye", "left eye", "mutilation", "calm", "shock", "Lio", "warehouse", "slaughterhouse", "eyepatch", "pain", "severe injury"]`
- **`Mikiya_Daily_Habits_Mannerisms_and_Quirks` (UID 2)**:
  - `key`: `["Kokutou Mikiya", "Mikiya Kokutou", "Mikiya"]`
  - `keysecondary`: `["habits", "mannerisms", "routine", "quirks", "glasses", "coffee", "tea", "umbrella", "typewriter", "polite", "necktie", "cooking", "stew"]`

### 5. `03_Touko_Expansion.json`
- **`Touko_Sister_Rivalry_and_Aoko_Trauma` (UID 0)**:
  - `key`: `["Aozaki Touko", "Touko Aozaki", "Touko", "Dirty Red"]`
  - `keysecondary`: `["Aoko", "sister", "Dirty Red", "Scarlet", "Fifth Magic", "Magic", "Blue", "crest", "rivalry", "trauma", "Misaki", "red hair"]`
- **`Touko_Existential_Weariness_and_Puppet_Identity` (UID 1)**:
  - `key`: `["Aozaki Touko", "Touko Aozaki", "Touko"]`
  - `keysecondary`: `["puppet", "duplicate", "body", "weariness", "immortality", "trunk", "original", "smoke", "cigarette", "soul", "true self", "death"]`
- **`Touko_Mentor_Ethics_and_Occult_Pedagogy` (UID 2)**:
  - `key`: `["Aozaki Touko", "Touko Aozaki", "Touko"]`
  - `keysecondary`: `["mentor", "apprentice", "Azaka", "teach", "pedagogy", "ethics", "lesson", "guidance", "advice", "training"]`

### 6. `06_Abilities_Expansion.json`
- **`Mechanics_Ryougi_Dual_Soul_Cognitive_Switching` (UID 2)**:
  - `key`: `["Ryougi Shiki", "Shiki", "SHIKI", "Ryougi"]`
  - `keysecondary`: `["switching", "dual soul", "cognitive", "posture", "sensory sharing", "killing impulse", "Yin", "Yang", "Void body", "personality switch", "male persona", "second personality", "other self", "personality"]`
- **`Mechanics_Ogawa_Apartments_Bounded_Field_Architecture` (UID 1)**:
  - `key`: `["Ogawa Apartments", "Ogawa Mansion", "Araya's bounded field", "Paradox Spiral architecture", "Taiji mandala"]`
  - `keysecondary`: `["mandala", "architecture", "Diamond Realm", "Womb Realm", "puppets", "loop", "sarcophagus", "isolation", "Araya", "building"]`

### 7. `08_World_Expansion.json`
- **`Tradition_Ryougi_Yin_Yang_Tripartite_Framework` (UID 0)**:
  - `key`: `["Ryougi clan", "Ryougi family", "Ryougi", "Kaname Ryougi", "Taima Yonke"]`
  - `keysecondary`: `["breeding", "Yin", "Yang", "tradition", "personality", "framework", "tripartite", "Void", "Kaname", "dual mind", "demon hunter", "DID"]`
- **`Cosmology_Mandala_Architecture_and_Root_Isolation` (UID 1)**:
  - `key`: `["Ogawa Mansion", "Ogawa Apartments", "Araya Souren", "Araya", "Mandala"]`
  - `keysecondary`: `["mandala", "Root", "isolation", "Akasha", "Womb Realm", "Diamond Realm", "Alaya", "Gaia", "Counter Force", "stasis", "cosmology", "architecture"]`

---

## 3. PHASE 3: CONTEXT-BUDGET ALLOCATION ANALYSIS

Testing under the exact SillyTavern descending-order accumulation algorithm yielded critical operational insights:

```
Order 150 (Crossover Rules)       ──► Claims 258 tokens  (Remaining: 1,790)
Order 140 (Bounded Fields)        ──► Claims 579 tokens  (Remaining: 1,211)
Order 130 (Relationships)         ──► Claims 482 tokens  (Remaining: 729)
Order 100 (MEoDP Lore)            ──► Claims 457 tokens  (Remaining: 272)
Order 10-20 (Base Character Cards)──► Exceeds 272 tokens (DROPPED under 2,048!)
```

### Key Budget Allocations:
1. **Under 2,048 Tokens**:
   - Severe combat/crossover scenarios (SC-13) consume 1,776 tokens on high-order rules and mechanics, causing base character profiles (Order 10: `Ryougi_Shiki`) to be dropped.
   - Narrative/roleplay scenarios (SC-01, SC-06, SC-12) fit comfortably within 2,048 tokens.
2. **Under 4,096 Tokens**:
   - Both high-order crossover directives and base character profiles survive and inject reliably (e.g., SC-13 injects 4,008 tokens with `Ryougi_Shiki` intact).
3. **Under 8,192 Tokens**:
   - Ample headroom for all relevant lore; however, unselective legacy Fate entries also enter the prompt.

**Recommendation**: Set SillyTavern's `world_info_budget` to **4,096 tokens** when running combined Nasuverse libraries.

---

## 4. PHASE 4: FINAL RETRIEVAL BENCHMARKS (POST-PATCH)

### Quantitative Summary Across All 22 Test Scenarios

| Metric | Pre-Patch Baseline | Post-Patch Result | Net Change |
| :--- | :---: | :---: | :---: |
| **Fully Passed Scenarios (PASS)** | **5 / 22** (22.7%) | **11 / 22** (50.0%) | **+6 (+120%)** |
| **Partially Passed Scenarios (PARTIAL)** | 16 / 22 (72.7%) | 11 / 22 (50.0%) | Focused |
| **Failed Scenarios (FAIL)** | **1 / 22** (4.5%) | **0 / 22** (0.0%) | **-1 (-100%)** |
| **Spurious Activations Detected** | 1 (`SHIKI` in SC-01) | **0 across all 22 scenarios** | **100% Resolved** |

### Detailed Status Transitions:
- **SC-01 (Shiki Psychological Defenses)**: `FAIL` $\rightarrow$ **`PASS`**
  - Spurious `SHIKI` eliminated.
  - Target `Shiki_Psychological_Defenses_and_Contradictions` activated.
- **SC-02 (SHIKI Male Persona in High School 1995)**: `PARTIAL_PASS` $\rightarrow$ **`PASS`**
  - Both `SHIKI` and `Mechanics_Ryougi_Dual_Soul_Cognitive_Switching` activated.
- **SC-03 (Void Shiki Epilogue in the Snow)**: `PARTIAL_PASS` $\rightarrow$ **`PASS`**
  - `Void_Shiki_Cognitive_State_and_Conversational_Voice` activated on natural snow context.
- **SC-04 (Mikiya Moral Boundaries)**: `PARTIAL_PASS` $\rightarrow$ **`PASS`**
  - `Mikiya_Kindness_and_Morality` activated on first-name reference.
- **SC-05 (Touko Personality & Aoko Rivalry)**: `PARTIAL_PASS` $\rightarrow$ **`PASS`**
  - `Touko_Sister_Rivalry_and_Aoko_Trauma` activated on `"Dirty Red"` and Aoko references.
- **SC-16 (Chapter 7 Climax: Blinding & Lio)**: `PARTIAL_PASS` $\rightarrow$ **`PASS`**
  - `Mikiya_Trauma_Response_and_Extreme_Situations` activated on severe trauma context.

---

## 5. UNRESOLVED ISSUES & FUTURE RECOMMENDATIONS

1. **Legacy Fate Non-Selective Triggers**:
   - `main_fate-go-servant.json` contains several non-selective entries with common English word triggers (e.g. `Billy the Kid` with `["the", "kid"]`, `BB` with `["be", "b"]`, `Salome` with `["head", "blood", "lover"]`).
   - While these do not break KnK functionality, they consume unnecessary budget in crossover prompts. A future maintenance pass should apply selective matching to these legacy entries.
2. **Duplicate Entry Titles in Legacy Files**:
   - Across FSN and FGO databases, 12 Servant names (e.g., `Merlin`, `Cu Chulainn`, `Heracles`, `Medea`) exist in duplicate files. In a unified session, both versions will activate simultaneously.
3. **Database Integrity**:
   - All 26 JSON files remain valid, intact, and independently loadable.
   - Total database inventory remains exactly **696 entries** and **~210,580 tokens**.
