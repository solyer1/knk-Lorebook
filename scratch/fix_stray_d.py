with open('Kara No/04_Other_Characters.json', 'r', encoding='utf-8') as f:
    text = f.read()

# Fix the stray 'd' at line 654: 'd    }\n  }\n}' -> '    }\n  }\n}'
if 'd    }\n  }\n}' in text:
    text = text.replace('d    }\n  }\n}', '    }\n  }\n}')
    with open('Kara No/04_Other_Characters.json', 'w', encoding='utf-8') as f:
        f.write(text)
    print("Fixed stray 'd' in 04_Other_Characters.json!")
else:
    print("Pattern not found, checking...")

