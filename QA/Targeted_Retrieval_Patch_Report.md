# TARGETED RETRIEVAL MAINTENANCE PATCH REPORT

**Date**: 2026-10-26  
**Target Project**: Kara no Kyoukai Lorebook Suite  
**Status**: Complete, Verified, and Benchmarked  

---

## 1. BACKUP VERIFICATION

Prior to making any edits, full verified copies of all seven target files were created with cryptographic SHA-256 validation.

| File Name | Size (Bytes) | SHA-256 Hash | Primary Backup Path |
| :--- | :---: | :---: | :--- |
| `01_Shiki.json` | 19744 | `9f326448696f1239...` | `d:\Personalise\Homemad\Lorebook\Nasuverse\backups_maintenance_20261026\01_Shiki.json` |
| `01_Shiki_Expansion.json` | 13109 | `663684d580a5e0d5...` | `d:\Personalise\Homemad\Lorebook\Nasuverse\backups_maintenance_20261026\01_Shiki_Expansion.json` |
| `02_Mikiya.json` | 14851 | `79160d3f46ee717e...` | `d:\Personalise\Homemad\Lorebook\Nasuverse\backups_maintenance_20261026\02_Mikiya.json` |
| `02_Mikiya_Expansion.json` | 8750 | `80ccfe4b0f22016f...` | `d:\Personalise\Homemad\Lorebook\Nasuverse\backups_maintenance_20261026\02_Mikiya_Expansion.json` |
| `03_Touko_Expansion.json` | 9693 | `a80e9836c1f2936c...` | `d:\Personalise\Homemad\Lorebook\Nasuverse\backups_maintenance_20261026\03_Touko_Expansion.json` |
| `06_Abilities_Expansion.json` | 13395 | `aa3f870d541d2b78...` | `d:\Personalise\Homemad\Lorebook\Nasuverse\backups_maintenance_20261026\06_Abilities_Expansion.json` |
| `08_World_Expansion.json` | 9407 | `7fb9f67aaef207e0...` | `d:\Personalise\Homemad\Lorebook\Nasuverse\backups_maintenance_20261026\08_World_Expansion.json` |

*(Secondary brain backup stored at `C:\Users\ASUS\.gemini\antigravity-ide\brain\678c8bc1-c499-456e-9a8a-30239db36827\scratch\verified_backups`)*

---

## 2. MODIFIED FILES & CHANGED KEYWORD ARRAYS

All edits were strictly confined to `key` (primary) and `keysecondary` arrays. All entry UIDs, contents, comments, and unrelated entries were preserved 100% intact.

### Review of SHIKI Persona Isolation:
- **Removed Generic 'knife' Trigger**: The knife trigger was excised because female Shiki carries a spring-loaded knife in her red leather jacket. Retaining 'knife' risked firing the male persona during female combat encounters.
- **Removed Broad Combat Triggers**: Broad words like 'impulse' and 'bloodlust' were excluded because female Shiki experiences murderous impulses post-coma.
- **Resulting SHIKI Secondary Filter**: Strictly confined to unambiguous male persona anchors (`male`, `boy`, `boyish`, `Yang`, `1995`, `1996`, `split personality`, `second personality`, `other self`, `bamboo grove`, `truck`, `traffic accident`, `rain road`, `fatal crash`).

### Detailed Patch Inventory across 7 Files:

#### Entry: `SHIKI`
- **Primary Keys (`key`)**: `['male Shiki', 'male personality', 'Yang persona', 'other Shiki', 'Ryougi SHIKI', 'SHIKI']`
- **Secondary Keys (`keysecondary`)**: `['male', 'boy', 'boyish', 'Yang', '1995', '1996', 'split', 'split personality', 'second personality', 'other self', 'bamboo', 'bamboo grove', 'truck', 'traffic accident', 'rain road', 'fatal crash']`

#### Entry: `Shiki_Psychological_Defenses_and_Contradictions`
- **Primary Keys (`key`)**: `['Ryougi Shiki', 'Shiki Ryougi', 'Shiki']`
- **Secondary Keys (`keysecondary`)**: `['kindness', 'warmth', 'groceries', 'tea', 'deflection', 'fear', 'alone', 'hollow', 'feelings', 'care', 'soften', 'vulnerability', 'tsundere', 'concern']`

#### Entry: `Shiki_Solitary_Behavior_and_Daily_Habits`
- **Primary Keys (`key`)**: `['Ryougi Shiki', 'Shiki Ryougi', 'Shiki']`
- **Secondary Keys (`keysecondary`)**: `['apartment', 'kimono', 'leather jacket', 'boots', 'ice cream', 'strawberry', 'fridge', 'solitary', 'habits', 'couch', 'tea', 'sleep', 'routine', 'wardrobe']`

#### Entry: `Shiki_Chronological_Mindset_and_Memory_Phases`
- **Primary Keys (`key`)**: `['Ryougi Shiki', 'Shiki Ryougi', 'Shiki']`
- **Secondary Keys (`keysecondary`)**: `['1995', '1996', '1998', '1999', 'coma', 'awakening', 'hospital', 'Lio', 'mindset', 'phases', 'development', 'Room 404', 'haircut']`

#### Entry: `Void_Shiki_Cognitive_State_and_Conversational_Voice`
- **Primary Keys (`key`)**: `['Void Shiki', '「\u3000」', 'Root Shiki', 'third personality', 'Void']`
- **Secondary Keys (`keysecondary`)**: `['Akasha', 'Root', 'snow', 'dream', 'watashi', 'furisode', 'kimono', 'dialogue', 'voice', 'epilogue', 'bamboo', 'speech']`

#### Entry: `Mikiya_Kindness_and_Morality`
- **Primary Keys (`key`)**: `['Kokutou Mikiya', 'Mikiya Kokutou', 'Mikiya', 'killing vs murder', 'Mikiya philosophy']`
- **Secondary Keys (`keysecondary`)**: `['murder', 'kill', 'sin', 'forgive', 'kindness', 'morality', 'justice', 'execution', 'moral', 'philosophy', 'investigation']`

#### Entry: `Mikiya_Insecurities_and_Psychological_Limits`
- **Primary Keys (`key`)**: `['Kokutou Mikiya', 'Mikiya Kokutou', 'Mikiya']`
- **Secondary Keys (`keysecondary`)**: `['insecurity', 'ordinary', 'weakness', 'normal', 'guilt', 'helpless', 'frustration', 'limits', 'fear', 'mediocre']`

#### Entry: `Mikiya_Trauma_Response_and_Extreme_Situations`
- **Primary Keys (`key`)**: `['Kokutou Mikiya', 'Mikiya Kokutou', 'Mikiya']`
- **Secondary Keys (`keysecondary`)**: `['trauma', 'danger', 'torture', 'blinding', 'crushed eye', 'left eye', 'mutilation', 'calm', 'shock', 'Lio', 'warehouse', 'slaughterhouse', 'eyepatch', 'pain', 'severe injury']`

#### Entry: `Mikiya_Daily_Habits_Mannerisms_and_Quirks`
- **Primary Keys (`key`)**: `['Kokutou Mikiya', 'Mikiya Kokutou', 'Mikiya']`
- **Secondary Keys (`keysecondary`)**: `['habits', 'mannerisms', 'routine', 'quirks', 'glasses', 'coffee', 'tea', 'umbrella', 'typewriter', 'polite', 'necktie', 'cooking', 'stew']`

#### Entry: `Touko_Sister_Rivalry_and_Aoko_Trauma`
- **Primary Keys (`key`)**: `['Aozaki Touko', 'Touko Aozaki', 'Touko', 'Dirty Red']`
- **Secondary Keys (`keysecondary`)**: `['Aoko', 'sister', 'Dirty Red', 'Scarlet', 'Fifth Magic', 'Magic', 'Blue', 'crest', 'rivalry', 'trauma', 'Misaki', 'red hair']`

#### Entry: `Touko_Existential_Weariness_and_Puppet_Identity`
- **Primary Keys (`key`)**: `['Aozaki Touko', 'Touko Aozaki', 'Touko']`
- **Secondary Keys (`keysecondary`)**: `['puppet', 'duplicate', 'body', 'weariness', 'immortality', 'trunk', 'original', 'smoke', 'cigarette', 'soul', 'true self', 'death']`

#### Entry: `Touko_Mentor_Ethics_and_Occult_Pedagogy`
- **Primary Keys (`key`)**: `['Aozaki Touko', 'Touko Aozaki', 'Touko']`
- **Secondary Keys (`keysecondary`)**: `['mentor', 'apprentice', 'Azaka', 'teach', 'pedagogy', 'ethics', 'lesson', 'guidance', 'advice', 'training']`

#### Entry: `Mechanics_Ryougi_Dual_Soul_Cognitive_Switching`
- **Primary Keys (`key`)**: `['Ryougi Shiki', 'Shiki', 'SHIKI', 'Ryougi']`
- **Secondary Keys (`keysecondary`)**: `['switching', 'dual soul', 'cognitive', 'posture', 'sensory sharing', 'killing impulse', 'Yin', 'Yang', 'Void body', 'personality switch', 'male persona', 'second personality', 'other self', 'personality']`

#### Entry: `Mechanics_Ogawa_Apartments_Bounded_Field_Architecture`
- **Primary Keys (`key`)**: `['Ogawa Apartments', 'Ogawa Mansion', "Araya's bounded field", 'Paradox Spiral architecture', 'Taiji mandala']`
- **Secondary Keys (`keysecondary`)**: `['mandala', 'architecture', 'Diamond Realm', 'Womb Realm', 'puppets', 'loop', 'sarcophagus', 'isolation', 'Araya', 'building']`

#### Entry: `Tradition_Ryougi_Yin_Yang_Tripartite_Framework`
- **Primary Keys (`key`)**: `['Ryougi clan', 'Ryougi family', 'Ryougi', 'Kaname Ryougi', 'Taima Yonke']`
- **Secondary Keys (`keysecondary`)**: `['breeding', 'Yin', 'Yang', 'tradition', 'personality', 'framework', 'tripartite', 'Void', 'Kaname', 'dual mind', 'demon hunter', 'DID']`

#### Entry: `Cosmology_Mandala_Architecture_and_Root_Isolation`
- **Primary Keys (`key`)**: `['Ogawa Mansion', 'Ogawa Apartments', 'Araya Souren', 'Araya', 'Mandala']`
- **Secondary Keys (`keysecondary`)**: `['mandala', 'Root', 'isolation', 'Akasha', 'Womb Realm', 'Diamond Realm', 'Alaya', 'Gaia', 'Counter Force', 'stasis', 'cosmology', 'architecture']`

---

## 3. JSON VALIDATION RESULTS

Every modified file was parsed and verified by the standard Python JSON parser post-modification:

| File Name | Syntax Status | Entries Count |
| :--- | :---: | :---: |
| `01_Shiki.json` | **VALID** | 5 |
| `01_Shiki_Expansion.json` | **VALID** | 4 |
| `02_Mikiya.json` | **VALID** | 5 |
| `02_Mikiya_Expansion.json` | **VALID** | 3 |
| `03_Touko_Expansion.json` | **VALID** | 3 |
| `06_Abilities_Expansion.json` | **VALID** | 3 |
| `08_World_Expansion.json` | **VALID** | 2 |

---

## 4. SCENARIO BENCHMARKS & BEFORE/AFTER COMPARISON

### Summary of 22 Roleplay Scenarios:
- **Fully Passed Scenarios (PASS)**: **11 / 22** (50.0%) — *Up from 5 / 22 (+120%)*
- **Partially Passed Scenarios (PARTIAL_PASS)**: **11 / 22** (50.0%) — *Normalized from 16 / 22*
- **Failed Scenarios (FAIL)**: **0 / 22** (0.0%) — *Down from 1 / 22 (100% elimination)*

### Key Verification Highlights:

#### 1. SC-01 vs. SC-02 Persona Disambiguation Verified:
- **SC-01 (Female Shiki Ordinary Scene)**: `FAIL` -> **`PASS`**
  - *Prompt*: Mikiya brings groceries and warm tea to Shiki's apartment.
  - *Activated*: `Ryougi_Shiki`, `Kokutou_Mikiya`, `Rel_Shiki_Mikiya`, `Shiki_Psychological_Defenses_and_Contradictions`.
  - *Spurious SHIKI*: **ABSENT**. The male persona did not trigger.
- **SC-02 (Male SHIKI in High School 1995)**: `PARTIAL_PASS` -> **`PASS`**
  - *Prompt*: Male SHIKI leaning on railing in bamboo grove in 1995 twirling knife.
  - *Activated*: `SHIKI`, `Mechanics_Ryougi_Dual_Soul_Cognitive_Switching`, `Fog_of_War_Ch1_A_Study_in_Murder_Part_1_1995`, `Timeline_Era_2_1995_High_School_and_Murders`.
  - *Result*: All expected historical and dual-soul mechanics triggered accurately without needing 'knife'.

#### 2. SC-05 Touko Sister Rivalry Verified:
- **Status**: `PARTIAL_PASS` -> **`PASS`**
- *Prompt*: Touko reacting coldly to being called 'Dirty Red'.
- *Activated*: `Aozaki_Touko`, `Touko_Sister_Rivalry_and_Aoko_Trauma`, `Touko_Existential_Weariness_and_Puppet_Identity`.

#### 3. SC-16 Chapter 7 Climax Verified:
- **Status**: `PARTIAL_PASS` -> **`PASS`**
- *Prompt*: Slaughterhouse warehouse, Lio, and Mikiya's crushed left eye.
- *Activated*: `Shirazumi_Lio`, `Rel_Shiki_Mikiya_Chronological_Phases`, `Fog_of_War_Ch7_A_Study_in_Murder_Part_2_1999`, `Mikiya_Trauma_Response_and_Extreme_Situations`.
- *Isolation Verification*: In SC-14 (1995 murder alley crime scene with blood), `Mikiya_Trauma_Response_and_Extreme_Situations` did **NOT** trigger, confirming that removing generic 'blood' isolated trauma response strictly to actual severe mutilation.

### Detailed Scenario Results Table:

| ID | Scenario Title | Pre-Status | Post-Status | Pre-Tokens | Post-Tokens | Target Status |
| :--- | :--- | :---: | :---: | :---: | :---: | :--- |
| SC-01 | Shiki Psychological Defenses When Mikiya | FAIL | **PASS** | 4695 | 5318 | Matched: 4, Missed: 0 |
| SC-02 | SHIKI Male Persona in High School 1995 | PARTIAL_PASS | **PASS** | 4975 | 5732 | Matched: 4, Missed: 0 |
| SC-03 | Void Shiki Epilogue in the Snow | PARTIAL_PASS | **PASS** | 5530 | 6264 | Matched: 3, Missed: 0 |
| SC-04 | Mikiya Moral Boundaries and Investigatio | PARTIAL_PASS | **PASS** | 3642 | 4328 | Matched: 4, Missed: 0 |
| SC-05 | Touko Personality and Aoko Rivalry ('Dir | PARTIAL_PASS | **PASS** | 1813 | 2624 | Matched: 3, Missed: 0 |
| SC-06 | Shiki and Azaka Sibling Rivalry and Food | PASS | **PASS** | 6595 | 6445 | Matched: 3, Missed: 0 |
| SC-07 | Shiki-Mikiya Chronological Phase 1 (1995 | PASS | **PASS** | 4831 | 5393 | Matched: 3, Missed: 0 |
| SC-08 | Fujino Asagami Spatial Distortion atop M | PASS | **PASS** | 3598 | 3605 | Matched: 4, Missed: 0 |
| SC-09 | Araya Souren Kongo Bounded Field and Spa | PARTIAL_PASS | **PARTIAL_PASS** | 2649 | 2613 | Matched: 1, Missed: 2 |
| SC-10 | Ogawa Apartments Taiji Mandala and Death | PARTIAL_PASS | **PARTIAL_PASS** | 2666 | 4061 | Matched: 3, Missed: 1 |
| SC-11 | Kurogiri Satsuki Unified Language at Rei | PARTIAL_PASS | **PARTIAL_PASS** | 4421 | 4356 | Matched: 3, Missed: 1 |
| SC-12 | Ryougi Shiki Interacting with Shirou Emi | PASS | **PASS** | 5983 | 6336 | Matched: 3, Missed: 0 |
| SC-13 | Servant vs Human Combat (Shiki vs Servan | PARTIAL_PASS | **PARTIAL_PASS** | 8568 | 7996 | Matched: 2, Missed: 1 |
| SC-14 | Canon Chronology & 1995 Mystery (Shiki i | PARTIAL_PASS | **PARTIAL_PASS** | 6876 | 7575 | Matched: 2, Missed: 1 |
| SC-15 | Chapter 4 (Overlooking View) vs Film 1 R | PARTIAL_PASS | **PARTIAL_PASS** | 8169 | 8351 | Matched: 3, Missed: 1 |
| SC-16 | Chapter 7 Climax: Mikiya Blinding and Li | PARTIAL_PASS | **PASS** | 6782 | 6961 | Matched: 4, Missed: 0 |
| SC-17 | Enjou Tomoe Sacrifice and Kanesada Katan | PARTIAL_PASS | **PARTIAL_PASS** | 5008 | 5032 | Matched: 2, Missed: 2 |
| SC-18 | Shiki Hospital Awakening in Room 404 (Ju | PARTIAL_PASS | **PARTIAL_PASS** | 4281 | 4273 | Matched: 3, Missed: 1 |
| SC-19 | Touko Aozaki and Rin Tohsaka Clock Tower | PARTIAL_PASS | **PARTIAL_PASS** | 3553 | 4226 | Matched: 2, Missed: 1 |
| SC-20 | Scene Setting at Garan no Dou on a Rainy | PARTIAL_PASS | **PARTIAL_PASS** | 7212 | 7272 | Matched: 3, Missed: 1 |
| SC-21 | Azaka Concealed Magecraft & Reien Academ | PASS | **PASS** | 5304 | 5626 | Matched: 4, Missed: 0 |
| SC-22 | Demon Hunter Bloodlines (Taima Yonke) an | PARTIAL_PASS | **PARTIAL_PASS** | 7395 | 8073 | Matched: 2, Missed: 1 |

---

## 5. CONTEXT-BUDGET SIMULATION UNDER 2,048, 4,096, AND 8,192 TOKENS

Using SillyTavern's actual descending order allocation algorithm (`sortFn = (a, b) => b.order - a.order`), we evaluated injection survival across key scenarios:

### Scenario SC-13: Servant vs Human Combat (Shiki vs Servant Lancer)
- **Unconstrained Candidate Pool**: 34 entries (7996 tokens)
- **Budget 2048 Tokens**:
  - Injected: 6 entries (2002 tokens)
  - Dropped: 28 entries
  - Survived Top Entries: `['Rule_Shiki_Is_Not_A_Servant', 'Mechanics_Mystic_Eyes_Classifications', 'Rel_Shiki_Fate_Servants', 'Mystic_Eyes_of_Death_Perception', 'Artoria Pendragon (Lancer)']`
  - **Base Character Card (`Ryougi_Shiki`)**: DROPPED (Budget exhausted by high-order crossover rules).
- **Budget 4096 Tokens**:
  - Injected: 18 entries (4094 tokens)
  - Dropped: 16 entries
  - Survived Top Entries: `['Rule_Shiki_Is_Not_A_Servant', 'Mechanics_Mystic_Eyes_Classifications', 'Rel_Shiki_Fate_Servants', 'Mystic_Eyes_of_Death_Perception', 'Artoria Pendragon (Lancer)']`
  - **Base Character Card (`Ryougi_Shiki`)**: DROPPED (Budget exhausted by high-order crossover rules).
- **Budget 8192 Tokens**:
  - Injected: 34 entries (7996 tokens)
  - Dropped: 0 entries
  - Survived Top Entries: `['Rule_Shiki_Is_Not_A_Servant', 'Mechanics_Mystic_Eyes_Classifications', 'Rel_Shiki_Fate_Servants', 'Mystic_Eyes_of_Death_Perception', 'Artoria Pendragon (Lancer)']`
  - **Base Character Card (`Ryougi_Shiki`)**: SURVIVED and INJECTED.

### Scenario SC-12: Crossover Interaction (Ryougi Shiki & Shirou Emiya)
- **Unconstrained Candidate Pool**: 21 entries (6336 tokens)
- **Budget 2048 Tokens**: Injected 6 entries (2025 tokens). Base character card survived.
- **Budget 4096 Tokens**: Injected 12 entries (3990 tokens). Base character card survived.
- **Budget 8192 Tokens**: Injected 21 entries (6336 tokens). Base character card survived.

### Scenario SC-01: Domestic Character Interaction (Shiki & Mikiya)
- **Unconstrained Candidate Pool**: 14 entries (5318 tokens)
- **Budget 2048 Tokens**: Injected 5 entries (2006 tokens). All character psychology cards survived.
- **Budget 4096 Tokens**: Injected 11 entries (3968 tokens). All character psychology cards survived.
- **Budget 8192 Tokens**: Injected 14 entries (5318 tokens). All character psychology cards survived.

---

## 6. SIMULATOR VS. LIVE APPLICATION DISTINCTION

- **Simulator**: The simulation scripts evaluate prompt strings against keyword arrays using standard word-boundary regex (`(?<!\w)kw(?!\w)`) and SillyTavern's selective logic equations. The candidate lists represent all lore entries that pass trigger filtering.
- **Live SillyTavern Engine**: In live SillyTavern, prompt injection is mediated by `world-info.js` with active generation buffers (chat history depth, prompt prefix/suffix, extension decorators). The live engine enforces `world_info_budget` strictly, which prevents excessive context consumption but will drop lower-order entries if high-order rules fill the budget.
- **False Activation Reality**: False activations of the male `SHIKI` persona were eliminated in our 22 test scenarios because the triggers now require explicit male/1995 context. However, cross-lorebook false activations from legacy Fate entries (e.g., Billy the Kid, BB) still occur in crossover prompts because those entries in `main_fate-go-servant.json` lack selective constraints.

---

## 7. UNRESOLVED ISSUES & NEXT STEPS

1. **Legacy Fate Non-Selective Entries**: `Fate/main_fate-go-servant.json` has non-selective entries for single common English words (e.g. `BB` with `['be', 'b']`, `Billy the Kid` with `['the', 'kid']`). When crossover roleplay occurs, these flood the candidate pool. A separate Fate-only maintenance pass is recommended to add secondary constraints.
2. **Duplicate Servant Titles**: 12 Servants have identical titles across FSN and FGO modules (e.g., `Merlin`, `Cu Chulainn`, `Heracles`). When both modules are loaded, both entries activate simultaneously.
3. **Recommended User Settings in SillyTavern**:
   - Set `World Info Budget`: **4,096 tokens**.
   - Set `Scan Depth`: **50 messages**.
   - Insertion Strategy: `Character First` or `Evenly`.
