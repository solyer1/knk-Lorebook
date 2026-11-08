import os

def find_files():
    for root, dirs, files in os.walk('.'):
        for f in files:
            ext = os.path.splitext(f)[1].lower()
            if ext in ['.txt', '.pdf', '.epub', '.md', '.doc', '.docx', '.html']:
                print(os.path.join(root, f))
            elif any(w in f.lower() for w in ['novel', 'knk', 'kara', 'kyoukai', 'vol', 'chapter']):
                print(os.path.join(root, f))

find_files()

