import os, json

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

for root in ['Kara No', 'Kara No/archive']:
    for f in os.listdir(root):
        if f.endswith('.json'):
            p = os.path.join(root, f)
            with open(p, 'r', encoding='utf-8') as fp:
                c = fp.read()
            for bw in banned_words:
                if bw in c:
                    print(f"Found '{bw}' in {p}")

