import os
import pypdf
import re

raw_dir = r"Kara No\Raw novel"
vol1_path = os.path.join(raw_dir, "Kara no Kyoukai_ The Garden of Sinners - Vol 1.pdf")
vol2_path = os.path.join(raw_dir, "Kara no Kyoukai_ The Garden of Sinners - Vol 2.pdf")

def search_pdf(pdf_path, keywords, max_matches=5):
    reader = pypdf.PdfReader(pdf_path)
    print(f"\nSearching in {os.path.basename(pdf_path)} ({len(reader.pages)} pages) for {keywords}...")
    matches = 0
    for idx, page in enumerate(reader.pages):
        text = page.extract_text() or ""
        for kw in keywords:
            if re.search(r'\b' + re.escape(kw) + r'\b', text, re.IGNORECASE):
                print(f"--- Page {idx+1} [matched: {kw}] ---")
                lines = text.split('\n')
                for line_idx, line in enumerate(lines):
                    if re.search(re.escape(kw), line, re.IGNORECASE):
                        start = max(0, line_idx - 2)
                        end = min(len(lines), line_idx + 3)
                        print('\n'.join(lines[start:end]))
                        print("...")
                matches += 1
                if matches >= max_matches:
                    return

# 1. Hospital name and room number in Chapter 4 / Chapter 1
search_pdf(vol1_path, ["hospital", "clinic", "room", "404", "Yagami"], max_matches=10)


