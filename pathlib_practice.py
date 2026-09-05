# from pathlib import Path

# folder = Path("practice")
# folder.mkdir(exist_ok=True)

# print(folder.exists())
# print(folder.is_dir())

# file =folder/ "python.txt"
# file.touch(exist_ok=True)

# file = folder / "notes.txt"
# file.touch(exist_ok=True)

# file = folder / "data.json"
# file.touch(exist_ok=True)

# file =folder / "script.py"
# file.touch(exist_ok=True)

# for files in folder.iterdir():
#     print(files)

# for files in folder.glob("*.txt"):
#     print(files)

# folder2 = folder / "backup"
# folder2.mkdir(exist_ok=True)

# file = folder / "notes.txt"
# file.rename(folder2 / "old_notes.txt")

# for files in folder.rglob("*"):
#     print(files)

# file = folder / "python.txt"
# file.unlink()
# file = folder / "data.json"
# file.unlink()
# file = folder / "script.py"
# file.unlink()

# file = folder2 / "old_notes.txt"
# file.unlink()

# folder2.rmdir()


from pathlib import Path

file = Path("pathlib_practice.py")

print(file.name)
print(file.stem)
print(file.parent)
print(file.suffix)
print(file.absolute())