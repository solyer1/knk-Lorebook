import os
import pypdf

raw_dir = r"d:\Personalise\Homemad\Lorebook\Nasuverse\Kara No\Raw novel"
vol1_path = os.path.join(raw_dir, "Kara no Kyoukai_ The Garden of Sinners - Vol 1.pdf")

reader = pypdf.PdfReader(vol1_path)
print(f"Total pages: {len(reader.pages)}")

# Search for chapter headings
chapter_markers = []
for idx in range(min(120, len(reader.pages))):
    text = reader.pages[idx].extract_text() or ""
    if "Overlooking View" in text or "Thanatos" in text or "Murder Speculation" in text or "A Study in Murder" in text:
        # print header snippets
        first_line = text.strip().split("\n")[0] if text.strip() else ""
        if any(marker in text for marker in ["／1", "／2", "／3", "／4", "／5", "Table of Contents"]):
            chapter_markers.append((idx + 1, first_line, text[:150].replace("\n", " ")))

for page_num, first_line, snippet in chapter_markers:
    print(f"Page {page_num:3d}: {first_line} | {snippet[:90]}")

