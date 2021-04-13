# Age in decades
age = int(input("How old are you? \n"))
# (//) This outputs only whole numbers 
decades = age // 10
# This outputs only remainders
years = age % 10

print("You are " + str(decades) + " decades and " + str(years) + " years old")