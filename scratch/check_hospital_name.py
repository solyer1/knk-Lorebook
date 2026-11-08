import pypdf

reader = pypdf.PdfReader(r"Kara No\Raw novel\Kara no Kyoukai_ The Garden of Sinners - Vol 1.pdf")

for page_num in range(232, 260):
    t = reader.pages[page_num].extract_text() or ""
    for line in t.split('\n'):
        if any(w in line.lower() for w in ['hospital', 'clinic', 'ward', 'private room', 'doctor', 'building']):
            print(f"P.{page_num+1}: {line}")

