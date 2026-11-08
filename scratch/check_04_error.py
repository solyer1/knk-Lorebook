with open('Kara No/04_Other_Characters.json', 'r', encoding='utf-8', errors='replace') as f:
    lines = f.readlines()

print(f"Total lines: {len(lines)}")
start = max(0, 645)
end = min(len(lines), 665)
for i in range(start, end):
    print(f"{i+1}: {repr(lines[i])}")

