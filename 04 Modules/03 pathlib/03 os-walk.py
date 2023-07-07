from pathlib import Path
import os
os.system("clear")

cwd = Path.cwd()
for dirpath, dirnames, filenames in os.walk(cwd):
    
    dirpath = Path(dirpath)
    if dirpath.name != '.ipynb_checkpoints':
        print(f'\n{dirpath.name} |')
        
        for filename in filenames:
            print(f'\t|__ {filename}')
        print('-'*50)