import os, json

targets = [
    "Kirie Shizuno",
    "KIRIE SHIZUNO",
    "Under the Tree of Miracles",
    "奇跡の木の下で",
    "congenital analgesia",
    "Doctor Ashika",
    "Dr. Araya",
    "ชิกิค動畫กกับมิกิยะ",
    "เดดอะพอลเซิล",
    "quadriceps femoris",
    "London dispersion forces",
    "Lennard-Jones",
    "Minkowski",
    "Na_v 1.7",
    "Mohs scale",
    "12,000 Newtons",
    "Yagami"
]

for root, dirs, files in os.walk('.'):
    if 'scratch' in root or 'backups_' in root:
        continue
    for f in files:
        if f.endswith('.json'):
            p = os.path.join(root, f)
            with open(p, 'r', encoding='utf-8') as fp:
                c = fp.read()
            for t in targets:
                if t in c:
                    print(f"[{t}] in {p}")

