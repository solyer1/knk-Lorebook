import os
import time

check_roots = [
    r"d:\Personalise\Homemad\Lorebook",
    r"d:\Personalise\Homemad",
    r"d:\Personalise"
]

for root_dir in check_roots:
    print(f"\n--- Checking: {root_dir} ---")
    if not os.path.exists(root_dir):
        print("Path does not exist")
        continue
    items = []
    try:
        for entry in os.scandir(root_dir):
            items.append((entry.is_dir(), entry.name, entry.stat().st_mtime, entry.stat().st_size if entry.is_file() else 0))
    except Exception as e:
        print(f"Error reading {root_dir}: {e}")
        continue
    items.sort(key=lambda x: x[2], reverse=True)
    for is_dir, name, mtime, size in items[:15]:
        t_str = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(mtime))
        d_marker = "<DIR>" if is_dir else f"{size:10,d}"
        print(f"[{t_str}] {d_marker:>10} | {name}")

