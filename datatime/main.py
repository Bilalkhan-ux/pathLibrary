# from datetime import datetime,timedelta

# now = datetime.now()
# print(now)
# # print(now.year)
# # print(now.month)
# # print(now.minute)

# # formatted = now.strftime("%d-%m-%y %H:%M:%S")
# # print(formatted)
# # formatted = now.strftime("%Y")
# # print(formatted)
# # formatted = now.strftime("%H")
# # print(formatted)
# # formatted = now.strftime("%M")
# # print(formatted)
# # formatted = now.strftime("%S")
# # print(formatted)

# future = now + timedelta(days=10)
# print(future)

# past = now - timedelta(days=3)
# print(past)

from datetime import datetime

date1 = datetime(2026,2,9)
date2 = datetime(2026,2,1)

print(date1 - date2)
print((date1 - date2).days)