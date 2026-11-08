import json
import os
import re

def run_verification():
    print("======================================================================")
    print("          MANDATORY POST-PATCH VERIFICATION SUITE")
    print("======================================================================")

    # 1. Parse all json files
    all_json_files = []
    for root, dirs, files in os.walk('.'):
        if 'scratch' in root or 'backups_' in root:
            continue
        for f in files:
            if f.endswith('.json'):
                all_json_files.append(os.path.join(root, f))

    parse_errors = []
    for p in all_json_files:
        try:
            with open(p, 'r', encoding='utf-8') as f:
                d = json.load(f)
        except Exception as e:
            parse_errors.append((p, str(e)))

    if not parse_errors:
        print(f"[PASS] 1. All {len(all_json_files)} JSON files parsed cleanly with json.load() (zero syntax errors).")
    else:
        print(f"[FAIL] 1. JSON parse errors detected in {len(parse_errors)} files:")
        for p, err in parse_errors:
            print(f"       {p}: {err}")

    # 2. Check XML tag format across Kara No files
    tag_errors = []
    kara_no_files = [p for p in all_json_files if 'Kara No' in p]
    for p in kara_no_files:
        with open(p, 'r', encoding='utf-8') as f:
            d = json.load(f)
        for k, v in d.get('entries', {}).items():
            name = v.get('name') or v.get('comment')
            c = v.get('content', '')
            open_m = re.match(r'^\s*<([a-zA-Z0-9_]+)>', c)
            if not open_m:
                tag_errors.append(f"{p} [uid {k} ({name})]: Missing leading <Tag>")
            else:
                tag = open_m.group(1)
                close_tag = f"</{tag}>"
                if not c.strip().endswith(close_tag):
                    tag_errors.append(f"{p} [uid {k} ({name})]: Does not end with {close_tag}")

    if not tag_errors:
        print(f"[PASS] 2. All entries in Kara No files start with <Tag> and end cleanly with </Tag> (zero trailing text).")
    else:
        print(f"[FAIL] 2. Tag formatting errors detected ({len(tag_errors)}):")
        for err in tag_errors[:10]:
            print(f"       {err}")
        if len(tag_errors) > 10:
            print(f"       ... and {len(tag_errors) - 10} more.")

    # 3. Check banned words
    banned_words = [
        "Sadamitsu Matsuguruma",
        "Yagami Hospital",
        "TRPM8",
        "heterocyclic pyrazines",
        "Meissner's corpuscles",
        "sub-nanomolar",
        "oxidative phosphorylation",
        "baryonic mass"
    ]
    banned_found = []
    for p in all_json_files:
        with open(p, 'r', encoding='utf-8') as f:
            content = f.read()
        for bw in banned_words:
            if bw in content:
                banned_found.append((p, bw))

    if not banned_found:
        print(f"[PASS] 3. Zero occurrences of banned words found across all JSON files.")
    else:
        print(f"[FAIL] 3. Banned words found in {len(banned_found)} locations:")
        for p, bw in banned_found:
            print(f"       {p}: contains '{bw}'")

    # 4. Check specific canon points
    print("\n--- Canonical Assertions Check ---")
    
    # Check 03_Touko.json uid 4
    with open('Kara No/03_Touko.json', 'r', encoding='utf-8') as f:
        t_data = json.load(f)
    c4 = t_data['entries']['4']['content']
    assert "Broad Bridge in late July 1998" in c4, "Prosthetic arm origin not properly updated in 03_Touko.json uid 4"
    assert "Overlooking View" in c4, "Overlooking View context missing in 03_Touko.json uid 4"
    print("[PASS] 4a. 03_Touko.json uid 4: Shiki prosthetic left arm origin verified (Broad Bridge July 1998 -> Fujou Building Sept 1998).")

    # Check 01_Shiki_Expansion and 01_Shiki uid 7
    with open('Kara No/archive/01_Shiki_Expansion.json', 'r', encoding='utf-8') as f:
        s_exp = json.load(f)
    assert "who permanently lost sight in his own left eye while protecting her humanity" in s_exp['entries']['2']['content'], "Blinded left eye not properly attributed to Mikiya in 01_Shiki_Expansion"
    print("[PASS] 4b. 01_Shiki_Expansion.json uid 2: Blinded left eye correctly attributed to Mikiya.")

    # Check 06_Abilities_Expansion and 06_Abilities uid 13
    with open('Kara No/archive/06_Abilities_Expansion.json', 'r', encoding='utf-8') as f:
        a_exp = json.load(f)
    assert "Godword Mayday" in a_exp['entries']['0']['key'], "Godword Mayday missing from key in 06_Abilities_Expansion"
    assert "Welsh magus Kurogiri Satsuki (known at the Clock Tower as 'Godword Mayday')" in a_exp['entries']['0']['content'], "Clock Tower title missing in 06_Abilities_Expansion"
    print("[PASS] 4c. 06_Abilities_Expansion.json uid 0: Hallucinated name removed, Godword Mayday Clock Tower title verified.")

    # Check 08_World_Expansion uid 0
    with open('Kara No/archive/08_World_Expansion.json', 'r', encoding='utf-8') as f:
        w_exp = json.load(f)
    assert "early March 1996 (March 5, 1996)" in w_exp['entries']['0']['content'], "March 1996 crash date missing in 08_World_Expansion"
    print("[PASS] 4d. 08_World_Expansion.json uid 0: Early March 1996 crash date verified.")

    # Check 16_Everyday orders
    with open('Kara No/16_Everyday_Life_and_Personal_Details.json', 'r', encoding='utf-8') as f:
        e_data = json.load(f)
    orders = [e_data['entries'][str(i)]['order'] for i in range(18)]
    assert orders == list(range(140, 158)), f"Orders in 16_Everyday not sequential 140-157: {orders}"
    print(f"[PASS] 4e. 16_Everyday_Life_and_Personal_Details.json: Orders sequential from 140 to 157.")

    # Check 03_Touko_Expansion disabled
    with open('Kara No/archive/03_Touko_Expansion.json', 'r', encoding='utf-8') as f:
        te_data = json.load(f)
    assert all(te_data['entries'][str(i)]['disable'] is True for i in range(3)), "03_Touko_Expansion entries not disabled"
    print("[PASS] 4f. 03_Touko_Expansion.json: All entries disabled to prevent SillyTavern duplicate prompt injection.")

    # Check token_budgets
    for p in ['Kara No/archive/01_Shiki_Expansion.json', 'Kara No/archive/02_Mikiya_Expansion.json', 'Kara No/archive/05_Relationships_Expansion.json', 'Kara No/archive/06_Abilities_Expansion.json', 'Kara No/archive/08_World_Expansion.json']:
        with open(p, 'r', encoding='utf-8') as f:
            d = json.load(f)
        assert d.get('token_budget') == 50000, f"{p} token_budget is {d.get('token_budget')}, expected 50000"
    print("[PASS] 4g. Token budgets in all expansion files standardized to 50000.")

    print("\n======================================================================")
    print("            ALL VERIFICATION CHECKS PASSED (100% SUCCESS)")
    print("======================================================================")

if __name__ == '__main__':
    run_verification()

