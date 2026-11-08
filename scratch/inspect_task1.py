import json, os

def check_task1():
    print("=== TASK 1: Checking remaining biochemistry/physics blocks ===")
    
    # 01_Shiki.json uid 0 & 3
    with open('Kara No/01_Shiki.json', 'r', encoding='utf-8') as f:
        d1 = json.load(f)
    print("01_Shiki uid 0 has SOMATIC block?", "[SOMATIC & NEUROLOGICAL KORYŪ KENJUTSU RECONFIGURATION]" in d1['entries']['0']['content'])
    print("01_Shiki uid 3 has NEURAL TRANSLATION block?", "[NEURAL TRANSLATION: BYPASSING PHOTORECEPTOR TRANSDUCTION]" in d1['entries']['3']['content'])

    # 04_Other_Characters.json uid 0, 1, 4
    with open('Kara No/04_Other_Characters.json', 'r', encoding='utf-8') as f:
        d4 = json.load(f)
    print("04_Other uid 0 has ŚARĪRA DIAMOND OSSIFICATION?", "[CELLULAR IMMUNITY & ŚARĪRA DIAMOND OSSIFICATION]" in d4['entries']['0']['content'])
    print("04_Other uid 1 has NOCICEPTIVE block?", "[NOCICEPTIVE NEURO-PHARMACOLOGY & APPENDICEAL PATHOLOGY]" in d4['entries']['1']['content'])
    print("04_Other uid 4 has PREDATORY MUTATION block?", "[CELLULAR, ODONTOLOGICAL & NEUROCHEMICAL PREDATORY MUTATION]" in d4['entries']['4']['content'])

    # 06_Abilities.json uid 1, 2, 6, 7, 10, 11
    with open('Kara No/06_Abilities.json', 'r', encoding='utf-8') as f:
        d6 = json.load(f)
    for u in ['1', '2', '6', '7', '10', '11']:
        c = d6['entries'][u]['content']
        print(f"06_Abilities uid {u} has molecular block?", any(w in c for w in [
            "[MOLECULAR & SOMATIC BIOPHYSICS OF MEoDP]",
            "[MOLECULAR SHEAR DYNAMICS & CRYSTALLINE FAILURE]",
            "[SYNTHETIC CYTOLOGY & BIO-THAUMATURGICAL REPLICATION]",
            "[QUANTUM-THAUMATURGICAL SOUL TRANSIT & IDENTITY CONTINUUM]",
            "[ŚARĪRA DIAMOND-LATTICE OSSIFICATION & SPATIAL COMPRESSION]",
            "[BIOMECHANICAL POLYMERS & HYDRAULIC FORCE TRANSFERS]"
        ]))

check_task1()

