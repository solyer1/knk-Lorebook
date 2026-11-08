import pypdf

reader = pypdf.PdfReader(r"Kara No\Raw novel\Kara no Kyoukai_ The Garden of Sinners - Vol 1.pdf")

print("=== CHECKING CH 2 END (Pages 110 to 145) ===")
for pnum in range(110, 145):
    t = reader.pages[pnum].extract_text() or ""
    for line in t.split('\n'):
        if any(w in line.lower() for w in ['march', 'snow', 'accident', 'car', 'vigil', 'bamboo', 'february', '1996']):
            print(f"P.{pnum+1}: {line.strip()}")

