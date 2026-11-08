import os
import pypdf

raw_dir = r"d:\Personalise\Homemad\Lorebook\Nasuverse\Kara No\Raw novel"
vol1_path = os.path.join(raw_dir, "Kara no Kyoukai_ The Garden of Sinners - Vol 1.pdf")

reader = pypdf.PdfReader(vol1_path)

def extract_range(start_p, end_p):
    text_blocks = []
    for p in range(start_p - 1, end_p):
        t = reader.pages[p].extract_text() or ""
        text_blocks.append(f"--- [PAGE {p+1}] ---\n" + t)
    return "\n".join(text_blocks)

# Let's inspect:
# 1. Opening banter (Page 6-10)
# 2. Touko's discussion on floating vs flying (Page 32-38)
# 3. Rooftop climax (Page 55-65)
# 4. Kirie's ending and Touko's epilogue lecture (Page 70-76)

samples = {
    "opening": extract_range(6, 10),
    "touko_philosophy": extract_range(33, 37),
    "climax_combat": extract_range(58, 63),
    "ending_resolution": extract_range(72, 77)
}

for k, v in samples.items():
    print(f"\n=================== {k.upper()} ===================")
    print(v[:1200])
    print("...\n[LENGTH:", len(v), "chars]")

