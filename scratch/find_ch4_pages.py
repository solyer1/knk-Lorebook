import os, pypdf, re

raw_dir = r"Kara No\Raw novel"
vol1_path = os.path.join(raw_dir, "Kara no Kyoukai_ The Garden of Sinners - Vol 1.pdf")
reader = pypdf.PdfReader(vol1_path)

print(f"Total pages: {len(reader.pages)}")

# Search for Garan no Dou / Chapter 4 / Hollow Shrine
for i, p in enumerate(reader.pages):
    t = p.extract_text() or ""
    if any(k in t.lower() for k in ["garan", "hollow shrine", "chapter 4", "4/the hollow", "4 / the hollow", "part 4"]):
        print(f"Page {i+1}: {t[:200].strip()}...")

