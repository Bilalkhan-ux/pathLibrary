import re

text = """
Users:
ahmed@gmail.com
sara123@yahoo.com
admin@company.com

Their IDs are 1023, 5555, and 98765.
"""

emails = re.findall(r"\S+@\S+", text)
print(emails)
print(len(emails))
ids = re.findall(r"\d{4,}", text)
print(ids)
print(len(ids))


text = "User_123 scored 95 points in 2026! 546"

numbers = re.findall(r"\b\d{3}\b",text)
print(numbers) #but it is printing 202 also from 2026

numbers = re.findall(r"\b\d{2,5}\b", text)
print(numbers)


words = re.findall(r"\w+",text)
print(words)
non_words = re.findall(r"\W+", text)
print(non_words)
number= re.findall(r"\d+",text)
print(number)


text = "Python ABC xyz 123!"

upper_text = re.findall(r"[A-Z]", text)
print(upper_text)
lower_text = re.findall(r"[a-z]", text)
print(lower_text)

digits = re.findall(r"[1-9]+",text)
print(digits)

text = """
Users: Ali_123, Sara_456, John99
Emails: ali@gmail.com, sara123@yahoo.com
Scores: 95, 87, 100
Codes: AB-123, XY-4567, Z-99
"""

users = re.findall(r"\b[a-zA-Z_]+\d+\b",text)
print(users)

emails = re.findall(r"\S+@\S+",text)
print(emails)

scores = re.search(r"Scores:\s*(.*)" ,text).group(1)
print(scores)

codes = re.findall(r"[A-Z]+-\d+", text)
print(codes)


text = "My email is test@gmail.com and my age is 23."

word = re.search(r"\S+@\S+", text).group()
print(word)

text = "I am learning Python and Python is fun."

s1 = re.search(r"Python",text).group()
print(s1)
s2 = re.match(r"Python",text)
print(s2)

text = "My phone number is 123-456-7890"

new_text = re.sub(r"[0-9]", "x",text)
print(new_text)