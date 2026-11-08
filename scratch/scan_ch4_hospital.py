import pypdf

reader = pypdf.PdfReader(r"Kara No\Raw novel\Kara no Kyoukai_ The Garden of Sinners - Vol 1.pdf")

print("=== CHECKING CH 4 (Pages 232 to 295) ===")
# Let's search for any mention of hospital name or room number in Ch 4
for pnum in range(232, 295):
    t = reader.pages[pnum].extract_text() or ""
    for line in t.split('\n'):
        l = line.lower()
        if any(w in l for w in ['room', 'floor', 'ward', 'hospital', 'ashika', 'clinic', 'yagami', '404', 'third floor']):
            print(f"P.{pnum+1}: {line.strip()}")

