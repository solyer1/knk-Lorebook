import pypdf

for vol_name in ["Kara no Kyoukai_ The Garden of Sinners - Vol 1.pdf", "Kara no Kyoukai_ The Garden of Sinners - Vol 2.pdf"]:
    reader = pypdf.PdfReader(f"Kara No\\Raw novel\\{vol_name}")
    print(f"=== {vol_name} ===")
    for idx, page in enumerate(reader.pages):
        text = page.extract_text() or ""
        if "404" in text:
            print(f"P.{idx+1}:")
            for line in text.split('\n'):
                if "404" in line:
                    print("  ", line.strip())

