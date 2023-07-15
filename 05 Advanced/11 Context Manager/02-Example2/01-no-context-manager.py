import os
os.system("clear")

def generator(file_path, mode="r"):
    print("Opening file...")
    f = open(file_path, mode)
    yield f
    print("Closing file...")
    f.close()

open_file = generator("data/file.txt", "r+")
file = next(open_file)
file.write("This is a new line")
file.seek(0)
print(file.read())
next(open_file, None)


