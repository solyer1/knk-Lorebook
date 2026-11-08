import os
import pypdf

raw_dir = r"d:\Personalise\Homemad\Lorebook\Nasuverse\Kara No\Raw novel"
vol1_path = os.path.join(raw_dir, "Kara no Kyoukai_ The Garden of Sinners - Vol 1.pdf")

reader = pypdf.PdfReader(vol1_path)
for p in range(5, 8):
    text = reader.pages[p].extract_text()
    print(f"=== PAGE {p+1} ===")
    print(text[:1000])

