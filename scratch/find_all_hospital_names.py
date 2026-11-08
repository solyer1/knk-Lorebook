import os, pypdf, re

def search_hospital_mentions(vol_path):
    reader = pypdf.PdfReader(vol_path)
    print(f"=== {os.path.basename(vol_path)} ===")
    for idx, page in enumerate(reader.pages):
        text = page.extract_text() or ""
        # Find any word preceding Hospital or Clinic or General Hospital
        matches = re.findall(r'([A-Z][a-zA-Z\s]{1,30}(?:Hospital|Clinic|Sanatorium|Infirmary))', text)
        for m in matches:
            # print snippet around it
            for line in text.split('\n'):
                if m in line:
                    print(f"P.{idx+1}: {line.strip()}")

search_hospital_mentions(r"Kara No\Raw novel\Kara no Kyoukai_ The Garden of Sinners - Vol 1.pdf")
search_hospital_mentions(r"Kara No\Raw novel\Kara no Kyoukai_ The Garden of Sinners - Vol 2.pdf")

