import os
import pypdf

raw_dir = r"d:\Personalise\Homemad\Lorebook\Nasuverse\Kara No\Raw novel"
files = [
    "Kara no Kyoukai_ The Garden of Sinners - Vol 1.pdf",
    "Kara no Kyoukai_ The Garden of Sinners - Vol 2.pdf",
    "Kara no Kyoukai_ The Garden of Sinners - Final Record.pdf",
    "Kara no Kyoukai_ The Garden of Sinners - Future Gospel.pdf"
]

for fname in files:
    full_path = os.path.join(raw_dir, fname)
    print(f"\n========================================================")
    print(f"FILE: {fname}")
    print(f"========================================================")
    if not os.path.exists(full_path):
        print("File not found!")
        continue
    
    reader = pypdf.PdfReader(full_path)
    total_pages = len(reader.pages)
    print(f"Total Pages: {total_pages}")
    
    # Check outline / TOC
    try:
        outline = reader.outline
        print(f"Outline items count: {len(outline) if outline else 0}")
    except Exception as e:
        print(f"Outline error: {e}")
        
    # Sample text from first few pages with content
    sample_text = ""
    for p_idx in range(min(15, total_pages)):
        text = reader.pages[p_idx].extract_text() or ""
        if len(text.strip()) > 50:
            sample_text = f"--- Page {p_idx+1} ---\n" + text[:600]
            break
            
    print("Sample Text:")
    print(sample_text)

