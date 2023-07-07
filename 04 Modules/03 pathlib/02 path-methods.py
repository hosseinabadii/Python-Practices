from pathlib import Path
import os
os.system("clear")


# Current working directory
cwd = Path.cwd()
print(f"{'cwd':15}: {cwd}")

# home directory
home = Path.home()
print(f"{'home directory':15}: {home}")


# Turn a relative path to its absolute form
rel_path = Path("run.py")
full_path = rel_path.resolve()
print(f"\n{'relative path':15}: {rel_path}")
print(f"{'resolved path':15}: {full_path}")


# Check the existance
print(f"\n{'exits run.py':15}: {Path('run.py').exists()}")
print(f"{'exist main.py':15}: {Path('main.py').exists()}")


# Create a new path from an existing path 
# with new suffix, new stem, new name
BASE_PATH = Path("home") / "templates" / "index.html"
new_suffix = BASE_PATH.with_suffix(".txt")
new_stem = BASE_PATH.with_stem("utils")
new_name = BASE_PATH.with_name("page.css")
print(f"\n{'BASE PATH':15}: {BASE_PATH}")
print(f"{'new suffix':15}: {new_suffix}")
print(f"{'new stem':15}: {new_stem}")
print(f"{'new name':15}: {new_name}")


# Check is directory and is file
print(f"\n{'Is dir cwd':15}: {Path.cwd().is_dir()}")
print(f"{'Is dir home':15}: {Path('home').is_dir()}")
print(f"{'Is file main.py':15}: {Path('main.py').is_file()}")
print(f"{'Is file run.py':15}: {Path('run.py').is_file()}")


# Create a new directory
# mkdir() method by default raise error if the directory 
# is already exists. but you can use
# mkdir(exist_ok=True) that not raise the error
path = Path.cwd() / "new folder"
# path.mkdir()
path.mkdir(exist_ok=True)

nested_path = Path.cwd() / "new folder" / "modules" / "functions"
# nested_path.mkdir()  # raise error if the directories not exist.
nested_path.mkdir(parents=True, exist_ok=True) # Also create the parent.


# Iterate the directory
print()
for path in Path.cwd().iterdir():
    print(path.name)
