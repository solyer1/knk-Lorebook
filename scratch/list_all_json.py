import os

def list_json():
    for root, dirs, files in os.walk('.'):
        for f in files:
            if f.endswith('.json'):
                print(os.path.join(root, f))

list_json()

