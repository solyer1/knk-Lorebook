with open('scratch/run_thai_pronoun_regression.py', 'r', encoding='utf-8') as f:
    text = f.read()

# Let's inspect how Kara No/10_RP_Guide.json is tested in run_thai_pronoun_regression.py
lines = text.split('\n')
for i, l in enumerate(lines):
    if '10_RP_Guide.json' in l:
        print('\n'.join(lines[max(0, i-5):min(len(lines), i+25)]))

