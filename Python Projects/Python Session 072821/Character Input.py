#Import dependencies
from datetime import datetime

#Input name and age
name = input("Give me your name: ")
age = int(input("Give me your age "))

#Display year statement
year_to_100 = datetime.now().year + 100 - age
print(f"{name}, you will be 100 in: {year_to_100}")