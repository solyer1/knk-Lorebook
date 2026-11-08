import pypdf, re

def search_cigarettes(vol_path):
    reader = pypdf.PdfReader(vol_path)
    print(f"=== CIGARETTE SEARCH IN {vol_path} ===")
    for idx, page in enumerate(reader.pages):
        text = page.extract_text() or ""
        for line in text.split('\n'):
            if any(w in line.lower() for w in ['cigarette', 'tobacco', 'smoke', 'lighter', 'sobranie', 'gitanes', 'marlboro', 'clove', 'brand']):
                if any(w in line.lower() for w in ['touko', 'brand', 'case', 'box', 'silver', 'filter', 'light']):
                    print(f"P.{idx+1}: {line.strip()}")

search_cigarettes(r"Kara No\Raw novel\Kara no Kyoukai_ The Garden of Sinners - Vol 1.pdf")

