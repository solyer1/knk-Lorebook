import json

def check_keys():
    for fpath in ['Kara No/01_Shiki.json', 'Kara No/03_Touko.json', 'Kara No/04_Other_Characters.json', 'Kara No/06_Abilities.json', 'Kara No/16_Everyday_Life_and_Personal_Details.json']:
        with open(fpath, 'r', encoding='utf-8') as f:
            data = json.load(f)
        print(fpath, "loaded successfully, total entries:", len(data['entries']))

check_keys()

