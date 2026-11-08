import pypdf

reader = pypdf.PdfReader(r"Kara No\Raw novel\Kara no Kyoukai_ The Garden of Sinners - Vol 1.pdf")

print("=== CHECKING CH 1 (Pages 1 to 55) ===")
for pnum in range(0, 55):
    t = reader.pages[pnum].extract_text() or ""
    for line in t.split('\n'):
        l = line.lower()
        if any(w in l for w in ['404', 'room 4', 'apartment', 'door', 'fourth floor']):
            print(f"P.{pnum+1}: {line.strip()}")

