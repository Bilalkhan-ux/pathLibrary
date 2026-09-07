from pathlib import Path
import os
# import dotenv

main_folder = Path("automation_project")
main_folder.mkdir(exist_ok=True)

notes = Path(main_folder, "notes.txt")
notes.touch()

print(main_folder.is_dir())
print(notes.is_file())

print(os.getcwd())
test_folder = "automation_project/test_folder"
os.mkdir(test_folder)
file1 = os.path.join(test_folder, "file1.txt")
file2 = os.path.join(test_folder, "file2.txt")
open(file1, "w").close()
open(file2, "w").close()
for item in os.listdir(test_folder):
    print(item)

print(os.path.isfile(os.path.join(test_folder,"file1.txt")))

print(os.environ.get("USERNAME"))
from pathlib import Path
import json
user = {
    "name": "Mr President",
    "age": 23,
    "language": "Python",
    "skills": ["OOP", "APIs", "JSON"]
}

file = Path("automation_project/user.json")
file.touch(exist_ok=True)

with open(file, "w")as file:
    json.dump(user,file,indent = 4)

new_user = {}

with open(file, "r") as file:
   new_user =  json.load(file)

print(new_user["name"])
print(new_user["language"])
print(len(new_user["skills"]))

from datetime import datetime, timedelta
now = datetime.now()
print(now)
formatted = now.strftime("%d-%m-%y %H:%M:%S")
print(formatted)

future = now + timedelta(days=7)
past = now - timedelta(days=3)

print(future)
print(past)

print((future-past).days)
import re
text = """
Name: Ali
Email: ali123@gmail.com
Phone: 0300-1234567
Order ID: ORD-2026-00452
"""

email = re.search(r"\S+@\S+",text).group()
print(email)

ph_number = re.search(r"\d+-\d+",text).group()
print(ph_number)

order_id = re.search(r"\w+-\d+-\d+",text).group()
print(order_id)

new_num = re.sub(r"Phone:\s*(.*)", "x",text)
print(new_num)


from dotenv import load_dotenv
import os

load_dotenv()

name = os.getenv("NAME")
lang = os.getenv("LANGUAGE")

print(name)
print(lang)

import requests

response = requests.get("https://jsonplaceholder.typicode.com/users/1")

print(response.status_code)
data = response.json()
print(data["name"])
print(data["email"])
print(data["address"]["city"])


try:
    num = int(input("Enter number: "))
    result = 100/num
    print(result)

except ValueError:
    print("Enter a number not text")
except ZeroDivisionError:
    print("Can't devide by zero")







