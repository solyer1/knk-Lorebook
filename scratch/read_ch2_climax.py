import pypdf

reader = pypdf.PdfReader(r"Kara No\Raw novel\Kara no Kyoukai_ The Garden of Sinners - Vol 1.pdf")

for pnum in range(113, 122):
    print(f"=== PAGE {pnum+1} ===")
    t = reader.pages[pnum].extract_text() or ""
    print(t[:800])

