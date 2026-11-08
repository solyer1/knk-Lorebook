import os
import time

workspace = r"d:\Personalise\Homemad\Lorebook\Nasuverse"

print("Scanning workspace:", workspace)
found_items = []

for root, dirs, files in os.walk(workspace):
    # skip scratch directory from ranking if needed, or list everything
    for f in files:
        full_path = os.path.join(root, f)
        try:
            mtime = os.path.getmtime(full_path)
            size = os.path.getsize(full_path)
            found_items.append((mtime, size, full_path))
        except Exception:
            pass

found_items.sort(key=lambda x: x[0], reverse=True)

print(f"Total files found: {len(found_items)}")
print("\nTop 30 most recently modified/added files:")
for mtime, size, path in found_items[:30]:
    t_str = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(mtime))
    rel_path = os.path.relpath(path, workspace)
    print(f"[{t_str}] {size:10,d} bytes | {rel_path}")

