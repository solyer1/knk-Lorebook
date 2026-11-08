import pypdf

reader = pypdf.PdfReader(r"Kara No\Raw novel\Kara no Kyoukai_ The Garden of Sinners - Vol 2.pdf")

print("=== CHECKING KUROGIRI SATSUKI IN VOL 2 ===")
for pnum, page in enumerate(reader.pages):
    text = page.extract_text() or ""
    if any(k in text.lower() for k in ["kurogiri", "satsuki", "sadamitsu", "matsuguruma", "godword", "god's word", "mayday"]):
        print(f"P.{pnum+1}:")
        for line in text.split('\n'):
            if any(k in line.lower() for k in ["kurogiri", "satsuki", "sadamitsu", "matsuguruma", "godword", "god's word", "mayday", "welsh", "clock tower"]):
                print("  ", line.strip())

