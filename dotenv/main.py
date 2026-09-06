from dotenv import load_dotenv
import os
load_dotenv()
name = os.getenv("My_name")

print(name)