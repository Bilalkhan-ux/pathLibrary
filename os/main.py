import os

print(os.getcwd())
print(os.listdir())

print(os.path.isdir("git"))
print(os.path.isfile("git"))

items = os.listdir()

for item in items:
    print(item)

print(os.path.exists("os"))
print(os.path.isdir("os"))
print(os.path.isfile("os"))

path = os.path.join("os", "main.py")
print(path)

import os

print(os.environ.get("USERNAME"))
print(os.environ.get("OS"))

print(os.environ.get("My_name"))

print(os.getcwd())

os.chdir("os")
print(os.getcwd())

original  = os.getcwd()
print(os.getcwd())

print(os.listdir())

os.chdir("os")
print(os.getcwd())
print(os.listdir())
os.chdir(original)