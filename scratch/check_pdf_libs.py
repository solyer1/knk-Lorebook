import sys

for pkg in ["pypdf", "pypdf2", "fitz", "pdfplumber", "pdfminer"]:
    try:
        __import__(pkg)
        print(f"Package '{pkg}' is INSTALLED.")
    except ImportError:
        print(f"Package '{pkg}' is NOT installed.")

