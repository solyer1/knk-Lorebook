import json
import os
import re

def move_closing_tag_to_end(content, tag_name):
    """Ensures </tag_name> is removed from inside content and placed cleanly at the very end."""
    close_tag = f"</{tag_name}>"
    if close_tag in content:
        content = content.replace(close_tag, "")
    content = content.strip() + "\n" + close_tag
    return content

# ==============================================================================
# TASK 1: DELETE REMAINING OUT-OF-TONE BIOCHEMISTRY & PHYSICS JARGON BLOCKS
# ==============================================================================
def apply_task_1():
    print("--- Executing Task 1: Deleting out-of-tone biochemistry & physics blocks ---")

    # 1. 01_Shiki.json
    p1 = 'Kara No/01_Shiki.json'
    with open(p1, 'r', encoding='utf-8') as f:
        d1 = json.load(f)

    # uid 0: Ryougi_Shiki - delete [SOMATIC & NEUROLOGICAL KORYŪ KENJUTSU RECONFIGURATION]
    c0 = d1['entries']['0']['content']
    somatic_idx = c0.find("[SOMATIC & NEUROLOGICAL KORYŪ KENJUTSU RECONFIGURATION]")
    if somatic_idx != -1:
        c0 = c0[:somatic_idx].rstrip()
    c0 = move_closing_tag_to_end(c0, "Ryougi_Shiki")
    d1['entries']['0']['content'] = c0

    # uid 3: Mystic_Eyes_of_Death_Perception - replace [NEURAL TRANSLATION: ...] with canonical bullet
    c3 = d1['entries']['3']['content']
    neural_idx = c3.find("[NEURAL TRANSLATION: BYPASSING PHOTORECEPTOR TRANSDUCTION]")
    canonical_bullet = "- Direct Spiritual Perception: Because her perception of death is routed directly from Akasha into her consciousness rather than relying on ordinary retinal light reflection, Shiki perceives the lines of death even in pitch-black darkness or with her eyelids closed."
    if neural_idx != -1:
        c3 = c3[:neural_idx].rstrip() + "\n" + canonical_bullet + "\n"
    c3 = move_closing_tag_to_end(c3, "Mystic_Eyes_of_Death_Perception")
    d1['entries']['3']['content'] = c3

    # Add Thai trigger keys in 01_Shiki.json:
    # uid 2: add "ชิกิแห่งความว่างเปล่า", "วอยด์ชิกิ", "รากเหง้าชิกิ"
    keys_uid2 = ["ชิกิแห่งความว่างเปล่า", "วอยด์ชิกิ", "รากเหง้าชิกิ"]
    for k in keys_uid2:
        if k not in d1['entries']['2']['key']:
            d1['entries']['2']['key'].append(k)

    # uid 3: add "เนตรมรณะ", "เนตรมองเห็นความตาย", "เส้นความตาย", "จุดความตาย"
    keys_uid3 = ["เนตรมรณะ", "เนตรมองเห็นความตาย", "เส้นความตาย", "จุดความตาย"]
    for k in keys_uid3:
        if k not in d1['entries']['3']['key']:
            d1['entries']['3']['key'].append(k)

    # uid 8: add "เสียงของวอยด์ชิกิ", "บุคลิกที่สามของชิกิ"
    keys_uid8 = ["เสียงของวอยด์ชิกิ", "บุคลิกที่สามของชิกิ"]
    for k in keys_uid8:
        if k not in d1['entries']['8']['key']:
            d1['entries']['8']['key'].append(k)

    with open(p1, 'w', encoding='utf-8') as f:
        json.dump(d1, f, indent=2, ensure_ascii=False)
    print("  01_Shiki.json Task 1 applied!")

    # 2. 04_Other_Characters.json
    p4 = 'Kara No/04_Other_Characters.json'
    with open(p4, 'r', encoding='utf-8') as f:
        d4 = json.load(f)

    # uid 0: Araya_Souren - delete [CELLULAR IMMUNITY & ŚARĪRA DIAMOND OSSIFICATION]
    c_araya = d4['entries']['0']['content']
    idx_araya = c_araya.find("[CELLULAR IMMUNITY & ŚARĪRA DIAMOND OSSIFICATION]")
    if idx_araya != -1:
        c_araya = c_araya[:idx_araya].rstrip()
    c_araya = move_closing_tag_to_end(c_araya, "Araya_Souren")
    d4['entries']['0']['content'] = c_araya

    # uid 1: Asagami_Fujino - delete [NOCICEPTIVE NEURO-PHARMACOLOGY & APPENDICEAL PATHOLOGY]
    c_fujino = d4['entries']['1']['content']
    idx_fujino = c_fujino.find("[NOCICEPTIVE NEURO-PHARMACOLOGY & APPENDICEAL PATHOLOGY]")
    if idx_fujino != -1:
        c_fujino = c_fujino[:idx_fujino].rstrip()
    c_fujino = move_closing_tag_to_end(c_fujino, "Asagami_Fujino")
    d4['entries']['1']['content'] = c_fujino

    # uid 4: Shirazumi_Lio - delete [CELLULAR, ODONTOLOGICAL & NEUROCHEMICAL PREDATORY MUTATION]
    c_lio = d4['entries']['4']['content']
    idx_lio = c_lio.find("[CELLULAR, ODONTOLOGICAL & NEUROCHEMICAL PREDATORY MUTATION]")
    if idx_lio != -1:
        c_lio = c_lio[:idx_lio].rstrip()
    c_lio = move_closing_tag_to_end(c_lio, "Shirazumi_Lio")
    d4['entries']['4']['content'] = c_lio

    with open(p4, 'w', encoding='utf-8') as f:
        json.dump(d4, f, indent=2, ensure_ascii=False)
    print("  04_Other_Characters.json Task 1 applied!")

    # 3. 06_Abilities.json
    p6 = 'Kara No/06_Abilities.json'
    with open(p6, 'r', encoding='utf-8') as f:
        d6 = json.load(f)

    blocks_06 = [
        ('1', '[MOLECULAR & SOMATIC BIOPHYSICS OF MEoDP]', 'Mechanics_MEoDP_Technical_Reference'),
        ('2', '[MOLECULAR SHEAR DYNAMICS & CRYSTALLINE FAILURE]', 'Mechanics_Mystic_Eyes_of_Distortion'),
        ('6', '[SYNTHETIC CYTOLOGY & BIO-THAUMATURGICAL REPLICATION]', 'Mechanics_Puppets_and_Artificial_Bodies'),
        ('7', '[QUANTUM-THAUMATURGICAL SOUL TRANSIT & IDENTITY CONTINUUM]', 'Mechanics_Touko_Puppet_Techniques'),
        ('10', '[ŚARĪRA DIAMOND-LATTICE OSSIFICATION & SPATIAL COMPRESSION]', 'Mechanics_Araya_Souren_Techniques'),
        ('11', '[BIOMECHANICAL POLYMERS & HYDRAULIC FORCE TRANSFERS]', 'Mechanics_Shiki_Prosthetic_Arm_Equipment')
    ]
    for uid, block_header, tag in blocks_06:
        c = d6['entries'][uid]['content']
        idx = c.find(block_header)
        if idx != -1:
            c = c[:idx].rstrip()
        c = move_closing_tag_to_end(c, tag)
        d6['entries'][uid]['content'] = c

    with open(p6, 'w', encoding='utf-8') as f:
        json.dump(d6, f, indent=2, ensure_ascii=False)
    print("  06_Abilities.json Task 1 applied!")

# ==============================================================================
# TASK 2: FIX SHIFTED & MISMATCHED THAI TRIGGER KEYWORDS
# ==============================================================================
def apply_task_2():
    print("--- Executing Task 2: Aligning shifted Thai keywords ---")

    # 1. 07_Locations.json (uid 4 to 10)
    p7 = 'Kara No/07_Locations.json'
    with open(p7, 'r', encoding='utf-8') as f:
        d7 = json.load(f)

    # uid 4: Location_Fujou_Building
    d7['entries']['4']['key'] = ["Fujou Building", "Fujou high-rise", "abandoned skyscraper", "Fujou Biru", "suicide building", "ตึกฟูโจ", "อาคารฟูโจ", "ตึกร้างฟูโจ"]
    d7['entries']['4']['keysecondary'] = ["จุดกระโดดตึก", "วิญญาณลอยฟ้า", "ตึกร้างคิริเอะ", "ghosts", "rooftop", "suicide site", "floating", "flight", "Kirie"]

    # uid 5: Location_Reien_Girls_Academy
    d7['entries']['5']['key'] = ["Reien Girls' Academy", "Reien Academy", "Reien", "Reien Jogakuin", "โรงเรียนสตรีเรย์เอ็น", "โรงเรียนเรย์เอ็น", "โรงเรียนหญิงล้วนเรย์เอ็น"]
    d7['entries']['5']['keysecondary'] = ["หอพักเรย์เอ็น", "ป่าหลังโรงเรียน", "โบสถ์เรย์เอ็น", "dormitory", "Catholic school", "uniform", "Azaka", "Ouryou Misaya"]

    # uid 6: Location_Shiki_Apartment
    d7['entries']['6']['key'] = ["Shiki's apartment", "Shiki's room", "Ryougi apartment", "Shiki's home", "อพาร์ตเมนต์ชิกิ", "ห้องพักชิกิ", "ห้องของชิกิ", "ห้อง 404"]
    d7['entries']['6']['keysecondary'] = ["ห้องพักมินิมอล", "ตู้เย็นชิกิ", "ที่พักของชิกิ", "futon", "bare room", "minimalist", "tatami", "strawberry ice cream"]

    # uid 7: Location_Minato_Bridge_Overpass
    d7['entries']['7']['key'] = ["Minato Bridge", "Broad Bridge", "Bay Overpass", "Minato Ohashi", "twisted bridge", "สะพานมินาโตะ", "สะพานบรอดบริดจ์", "สะพานกว้าง", "สะพานแขวนมินาโตะ"]
    d7['entries']['7']['keysecondary'] = ["สะพานบิดงอ", "จุดสู้กับฟูจิโนะ", "พายุฝน", "twisted bridge", "rainstorm", "Fujino battle", "steel cables", "distortion site"]

    # uid 8: Location_Suburban_General_Hospital
    d7['entries']['8']['key'] = ["Suburban General Hospital", "hospital", "clinic", "ward", "โรงพยาบาลชานเมือง", "โรงพยาบาลมิฟุเนะ", "ห้องพักผู้ป่วยชิกิ"]
    d7['entries']['8']['keysecondary'] = ["โคม่าสองปี", "เยี่ยมไข้", "ห้องพักชั้นสาม", "coma", "visitation", "third floor", "convalescence", "speech therapist"]

    # uid 9: Location_Bamboo_Forest_Road
    d7['entries']['9']['key'] = ["Bamboo Forest Road", "bamboo grove road", "Ryougi estate approach", "ทางเดินป่าไผ่", "ป่าไผ่ตระกูลเรียวกิ", "ถนนป่าไผ่"]
    d7['entries']['9']['keysecondary'] = ["จุดพบกันครั้งแรก", "หิมะตก", "คืนอุบัติเหตุ", "first meeting", "snowfall", "accident site", "kimono encounter", "March 1996"]

    # uid 10: Location_Ahnenelbe_Cafe
    d7['entries']['10']['key'] = ["Ahnenelbe", "Café Ahnenelbe", "Ahnenelbe coffee shop", "Kissa Ahnenelbe", "คาเฟ่อาเนนเออร์เบอ", "ร้านกาแฟอาเนนเออร์เบอ", "อาเนนเออร์เบอ"]
    d7['entries']['10']['keysecondary'] = ["ร้านกาแฟ", "จุดพบปะ", "พื้นที่เป็นกลาง", "coffee", "cafe", "crossover", "meeting", "Touko", "Mikiya", "Tsukihime", "Fate"]

    with open(p7, 'w', encoding='utf-8') as f:
        json.dump(d7, f, indent=2, ensure_ascii=False)
    print("  07_Locations.json Task 2 applied!")

    # 2. 08_World.json (uid 0 to 10)
    p8 = 'Kara No/08_World.json'
    with open(p8, 'r', encoding='utf-8') as f:
        d8 = json.load(f)

    d8['entries']['0']['key'] = ["Kara no Kyoukai setting", "KnK atmosphere", "Mifune supernatural", "urban occult", "KnK world", "บรรยากาศคาราโนะเคียวไค", "ความลี้ลับในเมือง", "โลกคู่ขนานมิฟุเนะ"]
    d8['entries']['0']['keysecondary'] = ["rain", "streets", "noir", "atmosphere", "mystery", "tone", "psychological", "เมืองยามค่ำคืน", "ความสมจริง", "การปิดบังความลับ"]

    d8['entries']['1']['key'] = ["The Root", "Swirl of the Root", "Akasha", "根源の渦", "Akashic Records", "วังวนแห่งรากเหง้า", "รากเหง้า", "อาคาชา", "ต้นกำเนิดแห่งสรรพสิ่ง"]
    d8['entries']['1']['keysecondary'] = ["origin", "source", "cosmology", "Void", "Magic", "True Magic", "Throne of Heroes", "Magecraft", "สัจธรรมสูงสุด", "ความว่างเปล่า", "จุดหมายจอมเวท"]

    d8['entries']['2']['key'] = ["Origin", "Origins", "Kigen", "起源", "soul's origin", "ต้นกำเนิด", "แก่นแท้แห่งวิญญาณ", "คิเก็น"]
    d8['entries']['2']['keysecondary'] = ["Root", "Akasha", "concept", "impulse", "drive", "awakening", "soul archetype", "primal directive", "Araya", "การสลักทิศทางชีวิต", "การตื่นของต้นกำเนิด", "แรงขับดันวิญญาณ"]

    d8['entries']['3']['key'] = ["Mystic Eyes", "Noble Colors", "Mystic Eye ranks", "ปรากฏการณ์เนตรมาร", "เนตรมารและสีแห่งขุนนาง", "ระดับสีเนตรมาร", "กฎเนตรมาร"]
    d8['entries']['3']['keysecondary'] = ["Rainbow rank", "Gold rank", "Jewel rank", "glasses seal", "optics", "perception", "สีรุ้ง", "สีทองคำ", "แว่นสะกดเนตรมาร"]

    d8['entries']['4']['key'] = ["Ryougi family tradition", "dual mind", "Demon Hunter clan", "ธรรมเนียมตระกูลเรียวกิ", "การสืบทอดสองบุคลิก", "ตระกูลนักล่าปิศาจ"]
    d8['entries']['4']['keysecondary'] = ["Yin Yang", "four demon hunter families", "Taima", "dual personality", "ชิกิหยินหยาง", "สี่ตระกูลโบราณ", "ไทมะยงเกะ"]

    d8['entries']['5']['key'] = ["Mage's Association", "Clock Tower", "Sealing Designation", "สังคมจอมเวท", "สมาคมเวทมนตร์", "หอนาฬิกา", "คำสั่งปิดตายเขตแดน"]
    d8['entries']['5']['keysecondary'] = ["Lords", "Enforcers", "magi politics", "Department of Lore", "ลอร์ดแห่งหอนาฬิกา", "การดองจอมเวท", "เอนฟอร์เซอร์"]

    d8['entries']['6']['key'] = ["hollow vessel", "Garan no Dou concept", "tripartite soul", "ภาชนะที่ว่างเปล่า", "โพรงกลวง", "ปรัชญากายจิตวิญญาณ"]
    d8['entries']['6']['keysecondary'] = ["body mind soul", "hollowness", "spiritual vacuum", "Akasha connection", "วิญญาณแฝง", "การเชื่อมต่อรากเหง้า"]

    d8['entries']['7']['key'] = ["psychics vs magi", "Esper", "natural channel", "ผู้มีพลังจิตปะทะจอมเวท", "พลังจิตกับศาสตร์เวท", "ผู้มีพลังพิเศษ"]
    d8['entries']['7']['keysecondary'] = ["channel", "circuit vs channel", "Fujino", "mutation", "teleportation", "การกลายพันธุ์", "ช่องสัญญาณจิต", "ฟูจิโนะ"]

    d8['entries']['8']['key'] = ["mundane facade", "secrecy of Mystery", "police investigation", "occult collision", "normal life", "การปกปิดความลี้ลับ", "สังคมคนธรรมดากับเรื่องลี้ลับ", "การสืบสวนของตำรวจ"]
    d8['entries']['8']['keysecondary'] = ["Mifune", "detective", "hospital", "law", "homicide", "witness", "evidence", "การหาเหตุผลทางวิทยาศาสตร์", "การเก็บกวาดคดีเวทมนตร์"]

    d8['entries']['9']['key'] = ["Ryougi tripartite framework", "Yin Yang and Void", "Ryougi Kaname", "โครงสร้างสามชั้นตระกูลเรียวกิ", "หยินหยางและความว่างเปล่า", "เรียวกิ คานาเมะ"]
    d8['entries']['9']['keysecondary'] = ["SHIKI yang", "Shiki yin", "Void Shiki origin", "Ryougi heir", "ผู้สืบทอดเรียวกิ", "ร่างกายที่เป็นรากเหง้า"]

    d8['entries']['10']['key'] = ["Ogawa Mansion", "Ogawa Apartments", "Araya Souren", "Araya", "Mandala", "สถาปัตยกรรมแมนดาลา", "การตัดขาดจากโลก", "แมนชั่นโอกาวะของอารายะ"]
    d8['entries']['10']['keysecondary'] = ["mandala", "Root", "isolation", "Akasha", "Womb Realm", "Diamond Realm", "Alaya", "Gaia", "Counter Force", "stasis", "cosmology", "architecture", "วัชรธาตุและครรภธาตุ", "เคาน์เตอร์ฟอร์ซ", "ปาฏิหาริย์ของโทโมเอะ"]

    with open(p8, 'w', encoding='utf-8') as f:
        json.dump(d8, f, indent=2, ensure_ascii=False)
    print("  08_World.json Task 2 applied!")

    # 3. 13_Dialogue_Examples.json (uid 0, 2, 3)
    p13 = 'Kara No/13_Dialogue_Examples.json'
    with open(p13, 'r', encoding='utf-8') as f:
        d13 = json.load(f)

    # uid 0: fix corrupted text
    d13['entries']['0']['key'] = ["ชิกิคุยกับมิกิยะ" if k == "ชิกิค動畫กกับมิกิยะ" else k for k in d13['entries']['0']['key']]

    # uid 2: Dialogue_Shiki_Touko_Incident_Briefing
    d13['entries']['2']['key'] = ["Dialogue_Shiki_Touko", "Shiki and Touko conversation", "incident briefing", "บทสนทนาชิกิกับโทโกะ", "โทโกะสรุปคดี", "การรับงานที่กาหลันโนะโด"]
    d13['entries']['2']['keysecondary'] = ["มีดพก", "เขตแดนเวทมนตร์", "ออฟฟิศโทโกะ", "pocket knife", "investigation briefing", "Garan no Dou office"]

    # uid 3: Dialogue_Mikiya_Investigative_Disarming
    d13['entries']['3']['key'] = ["Dialogue_Mikiya_Investigation", "Mikiya questioning witness", "investigative dialogue", "บทสนทนามิกิยะสืบสวน", "มิกิยะถามพยาน", "เทคนิคการสืบสวนของมิกิยะ"]
    d13['entries']['3']['keysecondary'] = ["ความสุภาพของมิกิยะ", "การจดบันทึก", "ความธรรมดาที่ทำให้คนไว้ใจ", "gentle questioning", "interview", "police detective style", "polite interrogation"]

    with open(p13, 'w', encoding='utf-8') as f:
        json.dump(d13, f, indent=2, ensure_ascii=False)
    print("  13_Dialogue_Examples.json Task 2 applied!")

    # 4. 06_Abilities.json (uid 14)
    p6 = 'Kara No/06_Abilities.json'
    with open(p6, 'r', encoding='utf-8') as f:
        d6 = json.load(f)

    d6['entries']['14']['key'] = ["Ogawa Apartments Bounded Field", "Mandala Bounded Field", "Araya Bounded Field", "โครงสร้างเขตแดนแมนชั่นโอกาวะ", "เขตแดนไท่จี๋อารายะ", "แมนดาลาตึกโอกาวะ"]
    d6['entries']['14']['keysecondary'] = ["วัชรธาตุและครรภธาตุ", "วงจรความตาย 24 ชั่วโมง", "การกักขังชิกิ", "Vajradhatu", "Garbhadhatu", "24-hour death cycle", "Shiki containment", "spatial isolation"]

    with open(p6, 'w', encoding='utf-8') as f:
        json.dump(d6, f, indent=2, ensure_ascii=False)
    print("  06_Abilities.json Task 2 applied!")

# ==============================================================================
# TASK 3: FIX REMAINING CANON & TIMELINE CONTRADICTIONS
# ==============================================================================
def apply_task_3():
    print("--- Executing Task 3: Fixing canon & timeline contradictions ---")

    # 1. Replace "Kirie Shizuno" -> "Fujou Kirie" across targets
    def replace_kirie_shizuno(fpath):
        with open(fpath, 'r', encoding='utf-8') as f:
            text = f.read()
        text = text.replace("Kirie Shizuno", "Fujou Kirie")
        text = text.replace("KIRIE SHIZUNO", "FUJOU KIRIE")
        with open(fpath, 'w', encoding='utf-8') as f:
            f.write(text)

    for p in ['Kara No/06_Abilities.json', 'Kara No/07_Locations.json', 'Kara No/09_Timeline.json', 'Kara No/15_Chapter_Knowledge_Fog_of_War.json']:
        replace_kirie_shizuno(p)
    print("  Kirie Shizuno -> Fujou Kirie replaced cleanly!")

    # 2. 09_Timeline.json synchronization
    p9 = 'Kara No/09_Timeline.json'
    with open(p9, 'r', encoding='utf-8') as f:
        d9 = json.load(f)

    # In uid 3 key: remove "Yagami hospital" if present
    if 'key' in d9['entries']['3'] and isinstance(d9['entries']['3']['key'], list):
        d9['entries']['3']['key'] = [k for k in d9['entries']['3']['key'] if 'yagami' not in k.lower()]

    c0 = d9['entries']['0']['content']
    # March crash date & arm sync in Entry 0
    c0 = c0.replace("[April 1995 – February 1996]", "[April 1995 – March 1996]")
    c0 = c0.replace("(Coma: Feb 1996 – June 1998)", "(Coma: March 1996 – June 1998)")
    c0 = c0.replace("Era 2: April 1995 – February 1996", "Era 2: April 1995 – March 1996")
    c0 = c0.replace("Era 3: February 1996 – May 1998", "Era 3: March 1996 – May 1998")
    c0 = c0.replace(
        "Era 4: June – July 1998 -> Awakening to the Lines of Death; Touko's therapy infiltration; corpse puppet battle; first prosthetic puppet arm fitted.",
        "Era 4: June – July 1998 -> Awakening to the Lines of Death; Touko's therapy infiltration; corpse puppet battle in hospital room (Shiki has both biological arms); hair cut short; dual personality lost, leaving empty void."
    )
    c0 = c0.replace(
        "Era 5: Late July 1998 -> Asagami Fujino incident; appendicitis triggers sensory return & Mystic Eyes of Distortion; Minato Bridge duel; Shiki severs appendix.",
        "Era 5: Late July 1998 -> Broad Bridge battle against Asagami Fujino; Shiki loses biological left arm on July 24, 1998; appendix mortality severed."
    )
    c0 = c0.replace(
        "Era 6: August – September 1998 -> Fujou Building rooftop suicide wave; Fujou Kirie's astral double; Mikiya's trance; Shiki's arm crushed; Kirie's fall; October arm upgrade.",
        "Era 6: August – September 1998 -> Touko crafts puppet prosthetic left arm (August 1998); Fujou Building rooftop suicide wave; Fujou Kirie's astral projection; Mikiya's trance; Shiki detaches puppet arm; Kirie's fall; October arm upgrade."
    )
    c0 = c0.replace("Shiki's Vision: Ordinary human eyesight (1995–Feb 1996)", "Shiki's Vision: Ordinary human eyesight (1995–March 1996)")
    c0 = c0.replace(
        "Shiki's Arms: Two biological arms (1995–Feb 1996) -> Paralyzed/atrophied biological arms (Coma) -> First puppet left arm (July 1998) -> Lost arm against Kirie (Sept 1998) -> Upgraded combat-hardened puppet arm capable of crushing stone and grasping spirits (October 1998 onward).",
        "Shiki's Arms: Two biological arms (1995–July 1998) -> Lost biological left arm against Fujino on Broad Bridge (July 24, 1998) -> Fitted with Touko's custom puppet prosthetic left arm (August 1998) -> Detached/sacrificed puppet left arm against Fujou Kirie's wraiths at Fujou Building (September 1998) -> Repaired and combat-hardened puppet arm capable of crushing stone and grasping spirits (October 1998 onward)."
    )
    c0 = c0.replace("Shiki's Personas: Dual soul Shiki & SHIKI active (1995–Feb 1996)", "Shiki's Personas: Dual soul Shiki & SHIKI active (1995–March 1996)")
    c0 = c0.replace(
        "Hospital Room 404 (1996–1998) -> Minimalist single-room apartment with tatami and unlocked lock (July 1998–1999)",
        "Suburban hospital third-floor private room (1996–1998) -> Minimalist single-room municipal apartment (Room 404) with tatami and unlocked lock (July 1998–1999)"
    )
    c0 = move_closing_tag_to_end(c0, "Chronology_Structure_and_Viewing_Guide")
    d9['entries']['0']['content'] = c0

    # In uid 6:
    c6 = d9['entries']['6']['content']
    c6 = c6.replace(
        "5. OCTOBER 1998: THE UPGRADED COMBAT PUPPET ARM:\n- Following the destruction of Shiki's first puppet arm in the battle with Kirie, Touko spends October 1998 crafting Shiki's definitive, high-grade magical combat prosthetic arm.",
        "5. OCTOBER 1998: THE UPGRADED COMBAT PUPPET ARM:\n- Following Shiki detaching her August 1998 puppet prosthetic arm in the battle with Kirie, Touko spends October 1998 repairing, refining, and reinforcing Shiki's definitive high-grade magical combat prosthetic arm."
    )
    c6 = move_closing_tag_to_end(c6, "Timeline_Era_6_September_1998_Overlooking_View")
    d9['entries']['6']['content'] = c6

    # In uid 11:
    c11 = d9['entries']['11']['content']
    c11 = c11.replace("(until February 1996)", "(until March 1996)")
    c11 = c11.replace(
        "2. BEFORE LATE JULY 1998 (PRE-FUJINO INCIDENT):\n- Asagami Fujino is an ordinary, sensory-deprived high school girl. She has NOT awakened her Mystic Eyes of Distortion and has killed no one.\n- Shiki has Touko's first, basic puppet arm (which can be damaged).",
        "2. BEFORE LATE JULY 1998 (PRE-FUJINO INCIDENT):\n- Asagami Fujino is an ordinary, sensory-deprived high school girl with chemically induced analgesia. She has NOT awakened her Mystic Eyes of Distortion and has killed no one.\n- Shiki has TWO biological arms until July 24, 1998 (losing her left arm against Fujino on Broad Bridge)."
    )
    c11 = c11.replace(
        "3. BEFORE SEPTEMBER 1998 (PRE-OVERLOOKING VIEW):\n- Fujou Kirie has NOT committed mass suicide. The Fujou Building is merely an abandoned skyscraper.\n- Shiki's first puppet arm is intact until crushed in September 1998.",
        "3. BEFORE SEPTEMBER 1998 (PRE-OVERLOOKING VIEW):\n- Fujou Kirie has NOT committed mass suicide. The Fujou Building is merely an abandoned skyscraper.\n- Shiki has Touko's puppet prosthetic arm (fitted in August 1998), intact until detached in September 1998."
    )
    c11 = move_closing_tag_to_end(c11, "Timeline_Roleplay_Guardrails_Anachronisms")
    d9['entries']['11']['content'] = c11

    with open(p9, 'w', encoding='utf-8') as f:
        json.dump(d9, f, indent=2, ensure_ascii=False)
    print("  09_Timeline.json synchronized!")

    # 3. 15_Chapter_Knowledge_Fog_of_War.json synchronization
    p15 = 'Kara No/15_Chapter_Knowledge_Fog_of_War.json'
    with open(p15, 'r', encoding='utf-8') as f:
        d15 = json.load(f)

    # uid 0:
    c15_0 = d15['entries']['0']['content']
    c15_0 = c15_0.replace("[April 1995 – February 1996]", "[April 1995 – March 1996]")
    c15_0 = c15_0.replace(
        "In 1995–1996: Shiki has NO Mystic Eyes, NO prosthetic arm, and has NEVER met Touko. Mikiya has both eyes.",
        "In 1995–1996: Shiki has NO Mystic Eyes, has two biological arms (NO prosthetic arm), and has NEVER met Touko. Mikiya has both eyes."
    )
    c15_0 = c15_0.replace(
        "In Summer 1998: Shiki has newly awakened Mystic Eyes and Touko's first prosthetic arm. Araya Souren is completely unknown.",
        "In Summer 1998: Shiki awakens Mystic Eyes in June (with both biological arms); loses biological left arm to Fujino on July 24, 1998; receives Touko's puppet arm in August 1998. Araya Souren is completely unknown."
    )
    c15_0 = move_closing_tag_to_end(c15_0, "Fog_of_War_Master_Chronology_and_Rules")
    d15['entries']['0']['content'] = c15_0

    # uid 1:
    c15_1 = d15['entries']['1']['content']
    c15_1 = c15_1.replace("[TEMPORAL SETTING: APRIL 1995 – FEBRUARY 1996]", "[TEMPORAL SETTING: APRIL 1995 – MARCH 1996]")
    c15_1 = c15_1.replace(
        "February 1996 (Climax on the rain-lashed road, traffic collision). Note: Early February 1996 is the established timeframe for the accident; specific calendar day (e.g., Feb 3) is traditional/inferred.",
        "March 1996 (Climax on the rain-lashed road, traffic collision on March 5, 1996)."
    )
    c15_1 = move_closing_tag_to_end(c15_1, "Fog_of_War_Ch1_A_Study_in_Murder_Part_1_1995")
    d15['entries']['1']['content'] = c15_1

    # uid 2:
    c15_2 = d15['entries']['2']['content']
    c15_2 = c15_2.replace(
        "Canonical Timeline: February 1996 – June 1998 (2-year comatose state at the suburban hospital); June 1998 (Shiki awakens in Room 404, claws at eyes, eyes bandaged); July 1998 (Touko infiltrates as speech therapist); Late July / Early August 1998 (Corpse spirit attack, Shiki accepts MEoDP, Touko fits puppet arm, hair cut).",
        "Canonical Timeline: March 1996 – June 1998 (2-year comatose state at the suburban hospital); June 1998 (Shiki awakens in the third-floor private room, claws at eyes, eyes bandaged; Touko infiltrates as counselor; corpse spirit attack in hospital room, Shiki accepts MEoDP, cuts hair short; has both biological arms)."
    )
    c15_2 = c15_2.replace(
        "Physical Status: Weakened from two years of muscle atrophy; newly fitted magical puppet left arm; cuts her hair short.",
        "Physical Status: Weakened from two years of muscle atrophy; both biological arms present (prosthetic arm not yet fitted until August 1998); cuts her hair short."
    )
    c15_2 = move_closing_tag_to_end(c15_2, "Fog_of_War_Ch2_The_Hollow_Shrine_1998")
    d15['entries']['2']['content'] = c15_2

    # uid 3:
    c15_3 = d15['entries']['3']['content']
    c15_3 = c15_3.replace("(congenital analgesia)", "(chemically induced analgesia (acquired sensory block))")
    c15_3 = move_closing_tag_to_end(c15_3, "Fog_of_War_Ch3_Remaining_Sense_of_Pain_1998")
    d15['entries']['3']['content'] = c15_3

    # uid 5:
    c15_5 = d15['entries']['5']['content']
    c15_5 = c15_5.replace(
        "Upgrades: Replaces Shiki's standard puppet arm with a masterwork combat prosthetic capable of physically grasping spirits and conceptual entities.",
        "Upgrades: Touko repairs and reinforces Shiki's August 1998 puppet prosthetic arm after Shiki detached it against Kirie's wraiths."
    )
    c15_5 = move_closing_tag_to_end(c15_5, "Fog_of_War_Ch4_Overlooking_View_1998")
    d15['entries']['5']['content'] = c15_5

    # uid 10: Mitsuru picture book title
    c15_10 = d15['entries']['10']['content']
    c15_10 = c15_10.replace("*Under the Tree of Miracles*", "*The Crocodile and the Bird* (ワニと小鳥)")
    c15_10 = move_closing_tag_to_end(c15_10, "Fog_of_War_Mirai_Fukuin_2008_2010_Adult_Era")
    d15['entries']['10']['content'] = c15_10

    # uid 11:
    c15_11 = d15['entries']['11']['content']
    c15_11 = c15_11.replace(
        "Prosthetic Arm: Shiki has her biological left arm until June 1998; uses Touko's standard puppet arm from July 1998; uses the upgraded spirit-gripping arm from September 1998 onward.",
        "Prosthetic Arm: Shiki has two biological arms until July 24, 1998 (lost against Fujino on Broad Bridge); uses Touko's puppet prosthetic arm from August 1998; uses the repaired/upgraded combat puppet arm after September 1998."
    )
    c15_11 = move_closing_tag_to_end(c15_11, "Fog_of_War_Dynamic_Enforcement_and_Overrides")
    d15['entries']['11']['content'] = c15_11

    with open(p15, 'w', encoding='utf-8') as f:
        json.dump(d15, f, indent=2, ensure_ascii=False)
    print("  15_Chapter_Knowledge_Fog_of_War.json synchronized!")

    p4 = 'Kara No/04_Other_Characters.json'
    p6 = 'Kara No/06_Abilities.json'
    p13 = 'Kara No/13_Dialogue_Examples.json'
    # 4. 04_Other_Characters.json: Fujou Kirie hospital & Kamekura Mitsuru book & Fujino analgesia
    with open(p4, 'r', encoding='utf-8') as f:
        d4 = json.load(f)

    # uid 1: Fujino analgesia
    c1_f = d4['entries']['1']['content']
    c1_f = c1_f.replace("congenital analgesia", "chemically induced analgesia (acquired sensory block)")
    c1_f = move_closing_tag_to_end(c1_f, "Asagami_Fujino")
    d4['entries']['1']['content'] = c1_f

    # uid 5: Kirie hospital
    c5_k = d4['entries']['5']['content']
    c5_k = c5_k.replace("confined to a sterile bed on the top floor of Yagami General Hospital in Mifune City.", "confined to a sterile bed on the sixth-floor terminal ward of the suburban general hospital in Mifune City.")
    c5_k = c5_k.replace("While her physical shell remained hooked to medical monitors in Room 404,", "While her physical shell remained hooked to medical monitors in the hospital's sixth-floor terminal ward,")
    c5_k = move_closing_tag_to_end(c5_k, "Fujou_Kirie")
    d4['entries']['5']['content'] = c5_k

    # uid 8: Kamekura Mitsuru book
    c8_m = d4['entries']['8']['content']
    c8_m = c8_m.replace("*Under the Tree of Miracles* / 奇跡の木の下で", "*The Crocodile and the Bird* (ワニと小鳥)")
    c8_m = c8_m.replace("*Under the Tree of Miracles*", "*The Crocodile and the Bird* (ワニと小鳥)")
    c8_m = move_closing_tag_to_end(c8_m, "Kamekura_Mitsuru")
    d4['entries']['8']['content'] = c8_m

    with open(p4, 'w', encoding='utf-8') as f:
        json.dump(d4, f, indent=2, ensure_ascii=False)
    print("  04_Other_Characters.json Kirie hospital & Mitsuru book updated!")

    # 5. 13_Dialogue_Examples.json (uid 13)
    with open(p13, 'r', encoding='utf-8') as f:
        d13 = json.load(f)
    c13_13 = d13['entries']['13']['content']
    c13_13 = c13_13.replace("Inside Room 404. Shiki sits on the edge of the mattress", "Inside the suburban hospital's third-floor private room. Shiki sits on the edge of the mattress")
    c13_13 = move_closing_tag_to_end(c13_13, "Dialogue_Canon_The_Hollow_Shrine_Balor_and_French_Poet")
    d13['entries']['13']['content'] = c13_13
    with open(p13, 'w', encoding='utf-8') as f:
        json.dump(d13, f, indent=2, ensure_ascii=False)
    print("  13_Dialogue_Examples.json uid 13 updated!")

    # 6. Standardize "congenital analgesia" in 06_Abilities and 14_Organizations
    with open(p6, 'r', encoding='utf-8') as f:
        d6 = json.load(f)
    c6_2 = d6['entries']['2']['content']
    c6_2 = c6_2.replace("congenital analgesia", "chemically induced analgesia (acquired sensory block)")
    c6_2 = move_closing_tag_to_end(c6_2, "Mechanics_Mystic_Eyes_of_Distortion")
    d6['entries']['2']['content'] = c6_2
    with open(p6, 'w', encoding='utf-8') as f:
        json.dump(d6, f, indent=2, ensure_ascii=False)

    p14 = 'Kara No/14_Organizations.json'
    with open(p14, 'r', encoding='utf-8') as f:
        d14 = json.load(f)
    c14_1 = d14['entries']['1']['content']
    c14_1 = c14_1.replace("congenital analgesia", "chemically induced analgesia (acquired sensory block)")
    c14_1 = move_closing_tag_to_end(c14_1, "Org_Demon_Hunter_Four_Families")
    d14['entries']['1']['content'] = c14_1
    with open(p14, 'w', encoding='utf-8') as f:
        json.dump(d14, f, indent=2, ensure_ascii=False)
    print("  congenital analgesia -> chemically induced analgesia standardized across 06 and 14!")

# ==============================================================================
# TASK 4: DISABLE EXPANSIONS & ASSIGN SEQUENTIAL NON-OVERLAPPING ORDERS
# ==============================================================================
def apply_task_4():
    print("--- Executing Task 4: Disabling expansion files & setting sequential orders ---")

    # 1. Disable all entries in 6 expansion files
    exp_files = [
        'Kara No/archive/01_Shiki_Expansion.json',
        'Kara No/archive/02_Mikiya_Expansion.json',
        'Kara No/archive/03_Touko_Expansion.json',
        'Kara No/archive/05_Relationships_Expansion.json',
        'Kara No/archive/06_Abilities_Expansion.json',
        'Kara No/archive/08_World_Expansion.json'
    ]
    for ep in exp_files:
        if os.path.exists(ep):
            with open(ep, 'r', encoding='utf-8') as f:
                ed = json.load(f)
            for k, v in ed.get('entries', {}).items():
                v['disable'] = True
            with open(ep, 'w', encoding='utf-8') as f:
                json.dump(ed, f, indent=2, ensure_ascii=False)
            print(f"  Disabled all entries in {ep}")

    # 2. Sequential non-overlapping order assignments
    order_plan = [
        ('Kara No/01_Shiki.json', 10),                            # 9 entries: 10..18
        ('Kara No/02_Mikiya.json', 20),                           # 8 entries: 20..27
        ('Kara No/03_Touko.json', 30),                            # 12 entries: 30..41
        ('Kara No/04_Other_Characters.json', 45),                 # 12 entries: 45..56
        ('Kara No/05_Relationships.json', 60),                    # 10 entries: 60..69
        ('Kara No/06_Abilities.json', 75),                        # 16 entries: 75..90
        ('Kara No/07_Locations.json', 95),                        # 11 entries: 95..105
        ('Kara No/08_World.json', 110),                           # 11 entries: 110..120
        ('Kara No/09_Timeline.json', 125),                        # 12 entries: 125..136
        ('Kara No/10_RP_Guide.json', 140),                        # 10 entries: 140..149
        ('Kara No/011_Fate_Integration.json', 155),               # 8 entries: 155..162
        ('Kara No/12_Crossover_Dynamics.json', 165),              # 12 entries: 165..176
        ('Kara No/13_Dialogue_Examples.json', 180),               # 18 entries: 180..197
        ('Kara No/14_Organizations.json', 200),                   # 10 entries: 200..209
        ('Kara No/15_Chapter_Knowledge_Fog_of_War.json', 215),     # 12 entries: 215..226
        ('Kara No/16_Everyday_Life_and_Personal_Details.json', 230) # 19 entries: 230..248
    ]

    for fpath, start_order in order_plan:
        with open(fpath, 'r', encoding='utf-8') as f:
            d = json.load(f)
        # Sort keys numerically if possible
        sorted_keys = sorted(d['entries'].keys(), key=lambda x: int(x) if x.isdigit() else x)
        for idx, k in enumerate(sorted_keys):
            d['entries'][k]['order'] = start_order + idx
        with open(fpath, 'w', encoding='utf-8') as f:
            json.dump(d, f, indent=2, ensure_ascii=False)
        print(f"  Assigned sequential orders {start_order}..{start_order + len(sorted_keys) - 1} to {fpath}")

if __name__ == '__main__':
    apply_task_1()
    apply_task_2()
    apply_task_3()
    apply_task_4()
    print("\nALL TASKS COMPLETED DETERMINISTICALLY!")
