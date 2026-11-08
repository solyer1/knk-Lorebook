import os

workspace = r"d:\Personalise\Homemad\Lorebook\Nasuverse"
for root, dirs, files in os.walk(workspace):
    if "scratch" in root:
        continue
    print(f"Directory: {root}")
    for d in dirs:
        if d != "scratch":
            print(f"  [DIR]  {d}")
    for f in files:
        full = os.path.join(root, f)
        print(f"  [FILE] {f} ({os.path.getsize(full)} bytes)")

