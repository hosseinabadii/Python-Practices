from pathlib import Path
import os
os.system("clear")

# Create a Path object
new_path = Path("hello")
print(f"{new_path!r}, {new_path!s}")


# Use forward slash to join the Path objects and text
BASE_DIR = Path("Home")
dir1 = BASE_DIR / "templates"
dir2 = BASE_DIR / "templates" / "index.html"
print(f"\n{'BASE DIR':15}: {BASE_DIR}")
print(f"{'dir1':15}: {dir1}")
print(f"{'dir2':15}: {dir2}")


# pathath attributes
path = Path.cwd() / 'main.py'
print()
print('path           :', path)
print('parent         :', path.parent)
print('parent-parent  :', path.parent.parent)
print('suffixes       :', path.suffixes)
print('suffix         :', path.suffix)
print('stem           :', path.stem)
print('name           :', path.name)

print('\nparts       :')
for part in path.parts:
    print(f"\t\t{part}")

print('\nparents     :')
for parent in path.parents:
    print(f"\t\t{parent}")