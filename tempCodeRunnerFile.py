file = folder / "python.txt"
file.unlink()
file = folder / "data.json"
file.unlink()
file = folder / "script.py"
file.unlink()

file = folder2 / "old_notes.txt"
file.unlink()

folder2.rmdir()